from flask import Flask, render_template, redirect, request
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "codingdojo"
mysql = MySQLConnector(app, 'lead_gen_business')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    #EMAIL_REGEX =
    re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    email = request.form['useremail']
    if EMAIL_REGEX.match(email):
        myquery = "INSERT INTO emails (email, created_at, updated_at) VALUES (:userinput, NOW(), NOW())"

        mydata = {"userinput": useremail}

        newuserid = mysql.query_db(myquery, mydata)
        flash("The email you entered ({}), is a valid email address! Thank you!".format(useremail))
        return redirect('/success')
    else:
        print "Not a valid email", useremail
        flash("Not a valid email")

    return redirect('/')

@app.route('/success')
def success():
    allemails = mysql.query_db("SELECT * FROM emails")
    print "all the emails", allemails
    for em in allemails:
        em['created_at'] = em['created_at'].strftime("%m/%d/%Y %I: %M %p")
    return render_template('success.html')

app.run(debug=True)
