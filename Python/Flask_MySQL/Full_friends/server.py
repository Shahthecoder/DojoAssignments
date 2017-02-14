from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'fullfriendsdb')

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    print request.form['first_name']
    print request.form['last_name']
    print request.form['occupation']

    fname =  request.form['first_name']
    lname =  request.form['last_name']
    occ =  request.form['occupation']

    query = 'insert into friends(first_name, last_name, occupation) values (:first, :last, :occ)'
    data = {'first' : fname, 'last' : lname, 'occ' : occ}

    inserted_friend = mysql.query_db(query,data)
    print inserted_friend
    return redirect('/')
app.run(debug=True)
