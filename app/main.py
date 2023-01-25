from flask import render_template, render_template_string, request, redirect, url_for,send_file
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, logout_user, UserMixin, current_user
from app import app, db
from app.models.contactMessage import ContactMessage
from app.models.user import User
from app.models.review import Review
from app.models.test_result import TestResult
from app.static.Scripts.Pdf_Generator import generate_pdf


@app.route('/', methods=['GET', 'POST'])
def home():
    # Static Review that gets rendered by the template
    # We need to implement getters that will get this from the Database
    try:
        review = Review.query.filter_by(rating=5).order_by(-Review.id).first()
        if review:
            user = User.query.filter_by(id=review.user_id).first()
            review_content = review.message
            review_username=user.username
        else:
            review_content = "Such good deals!"
            review_username= "Totally not a robot"

        # Specialities Select Options
        medical_specialties = ["Cardiovascular","Dermatology","Pediatrics","Urology","Family medicine","Ophthalmology"]

        return render_template('home.html', review_content=review_content, review_username=review_username, medical_specialties=medical_specialties)
    except:
        return render_template('home.html')

@app.route('/register', methods=['POST'])
def register():

    username = request.form['username']
    password = request.form['password']

    new_user= User(username, password)
    db.session.add(new_user)
    db.session.commit()

    login_user(new_user)

    result = db.engine.execute(f'SELECT * FROM users WHERE username="{username}" and password="{password}" ')
    records = [r for r in result.fetchall()]

 

    new_result = TestResult("The Fluu", "dr.Fran", records[0][0])
    db.session.add(new_result)
    db.session.commit()

    return redirect(url_for('home'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    result = db.engine.execute(f'SELECT username FROM users WHERE username="{username}" and password="{password}" ')
    records = [r for r in result.fetchall()]

    # If there's an user that matches username and password...
    if len(records) > 0:
        username = records[0][0]
        login_user(User(username, password))
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/review', methods=['POST'])
def review():
    print(request.form)
    message = request.form['message']
    user_id = current_user.id

    review = Review(message, 5, user_id)
    db.session.add(review)
    db.session.commit()

    return redirect(url_for('home'))


@app.route('/message', methods=['POST'])
def message():

    print(request.form)

    message = request.form['textMessage']
    textMessageEmail = request.form['textMessageEmail']
    textMessageName = request.form['textMessageName']
    SQLcommand  = f'insert into contactMessage(textMessage,name,email) values ("{message}","{textMessageName}","{textMessageEmail}")'
    print(SQLcommand)

    conn_dsdb = db.engine.raw_connection()
    conn_dsdb.cursor().executescript(SQLcommand)



    result = db.engine.execute(f'SELECT * FROM contactMessage ')
    print(result.fetchall())


    return redirect(url_for('home'))


@app.route('/testresults',methods=['GET'])
def testresults():
    	
    code = request.args.get('testCode')

    result = db.engine.execute(f'SELECT * FROM test_results WHERE id="{code}" ')
    records = [r for r in result.fetchall()]

    doc_name= records[0][2]
    info = records[0][1] 
    user_id = records[0][3] 

    result = db.engine.execute(f'SELECT username FROM users WHERE id="{user_id}" ')
    records = [r for r in result.fetchall()]
    username = records[0][0]

    # If there's an user that matches username and password...
    if len(records) > 0:

        filename = generate_pdf(username, doc_name, code, info)
        return send_file(filename, download_name='file.pdf')   

    return redirect(url_for('home'))

   


@app.route('/medics', methods=['GET'])
def medics():

    if request.args.get('search'):
        search_term = f"Searching for '{request.args.get('search')}'"
    else:
        search_term = ''

    return render_template_string(medic_html.replace('{search_term}', search_term))

    #return render_template('medics.html')


if __name__ == "__main__":

    file_path = os.path.relpath("app/templates/medics.html")
    with open(file_path, 'r') as file:
        medic_html = file.read().replace('\n', '')

    with app.app_context():
        db.create_all()

        # Create admin login
        #admin = User('admin', 'admin')
        #db.session.add(admin)
        #db.session.commit()

        port = int(os.environ.get('PORT', 5000))
        app.run(debug=True, host='0.0.0.0', port=port)
