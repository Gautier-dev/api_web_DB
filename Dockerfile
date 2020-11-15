FROM debian
RUN apt-get update
RUN apt-get python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install flask
COPY . /app/
WORKDIR /app
CMD ["export", "FLASK_APP=app_flask.py"]
CMD ["flask", "run"]