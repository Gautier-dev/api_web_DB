FROM debian
ARG DBNAME=${DBNAME}
ARG POSTGRES_USER=${POSTGRES_USER}
ARG POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ARG URL_DB=${URL_DB}
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install flask
RUN pip3 install psycopg2-binary
COPY . /app/
WORKDIR /app
CMD ["export", "FLASK_APP=app.py"]
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]