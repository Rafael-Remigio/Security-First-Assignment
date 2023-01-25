from fpdf import FPDF

def generate_pdf(User, Doc, Code, Disease):

    file_path = "/"+ str(Code)+"_result.pdf"
    
    # save FPDF() class into a
    # variable pdf
    pdf = FPDF()
    
    # Add a page
    pdf.add_page()
    
    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size = 15)

     # create a cell
    pdf.cell(200, 10, txt = "Doctor: " + str(Doc),
            ln = 1, align = 'L')

    # create a cell
    pdf.cell(200, 10, txt = "User: " + str(User),
            ln = 1, align = 'L')
    
    # add another cell
    pdf.cell(200, 10, txt = str(Code),
            ln = 2, align = 'C')
    
      # add another cell
    pdf.cell(200, 10, txt = "Unfortunately the tests concluded that you have " + str(Disease),
            ln = 2, align = 'C')
    

    # save the pdf with name .pdf
    pdf.output(file_path)  

    return file_path

