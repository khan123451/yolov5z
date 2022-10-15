FROM python:latest

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

RUN pip install flask

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
ENTRYPOINT ["flask", "--app", "server", "run", "--host=0.0.0.0"]

