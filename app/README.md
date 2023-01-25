## How to run

Builds the image
```console
$  docker image build -t flask_docker .
```

Runs the image
```console
$  docker run -p 5000:5000 -d flask_docker

```
In one line
```console
$  docker image build -t flask_docker . ; docker run -p 5000:5000 flask_docker
```
