from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

conn = psycopg2.connect(dbname=os.environ['DBNAME'], user=os.environ['POSTGRES_USER'],
                            password=os.environ['POSTGRES_PASSWORD'], host=os.environ['URL_DB'], port="5432")
print("Connected to the data base")

cur = conn.cursor()


@app.route('/')
def home():
    return render_template('home.html', url="http://surveillancedevieux-flask.apps.asidiras.dev")

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        try:
            print("Executing SQL query")
            print(request.form['POST-SQL'])
            cur.execute(request.form['POST-SQL'])
        except:
            return render_template("post_data.html", msg="Error")
        return render_template("post_data.html", msg="Success")
    else:
        try:
            print("Executing SQL query")
            print(request.args.get('GET-SQL'))
            cur.execute(request.args.get('GET-SQL'))
        except:
            return render_template("get_data.html", msg="Error")
        data = cur.fetchall()
        return str(data)