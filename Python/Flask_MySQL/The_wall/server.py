from flask import Flask, request, redirect, render_template, session, flash, escape
from mysqlconnection import MySQLConnector
#from flask.ext.bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = 'CodingNinja'
#bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'Wall')

@app.route('/')
def index():
    # Login / Reg display
    return render_template('index.html')

@app.route('/logoff')
def logoff():
    if session.has_key('user'):
    #session['user'].pop()
    #pop(session['user'])
    session.pop('user')
    return redirect('/')

@app.route('/process_login', methods=['POST'])
def process_login():
    if not request.form.has_key('email') or len(request.form['email']) <9:
        flash('Please enter your email')
        redirect('/')
    elif not request.form.has_key('password') or len(request.form['password']) <8:
        flash('Plesse enter your password')
        redirect('/')

    # log the user in:
    email/password
    query = "SELECT * FROM users WHERE email=:em AND password=MD5(:pw) LIMIT 1;"
    data = {'em': request.form['email'],
            'pw': request.form['password']
            }
    result = mysql.query_db(query, data)

    if len(reslts) != 1:
        flash('Could not find email/password combination')
        return redirect('/')


    # save in session
    session['user'] = result[0]
    return redirect('/wall')

@app.route('/process_register', methods=['POST'])
def process_register():
    if not request.form.has_key('fist_name') or len(request.form['first_name']) <2:
        flash('Please enter your first_name')
        redirect('/')
    elif not request.form.has_key('last_name') or len(request.form['last_name']) <2:
        flash('Please enter your last_name')
        redirect('/')
    elif not request.form.has_key('email') or len(request.form['email']) <9:
        flash('Please enter your email')
        redirect('/')
    elif not request.form.has_key('password') or len(request.form['password']) <8:
        flash('Plesse enter your password')
        redirect('/')

    query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:fn, :ln, :em, MD5(:pw), NOW(), NOW() );"
    data = {
        'fn' : request.form['first_name'],
        'ln' : request.form['last_name'],
        'em' : request.form['email'],
        'pw' : request.form['password']
    }
    user_id = mysql.query_db(query, data)
    if int(user_id) == 0:
        flash('Unexpected error!')
        redirect('/')

    # log the user in:
    query = "SELECT * FROM users WHERE id=:id"
    data = {'id': user_id}
    result = mysql.query_db(query, data)
    session['user'] = result[0]

    return redirect('/wall')

@app.route('/wall')
def wall():
    if not session.has_key('user'):
      flash('Please login')
      redirect('/')

      query = "SELECT users.first_name + ' ' + users.last_name AS message_creator, users.last_name, message.id, messages.message, messages.created_at"
      query += "FROM users JOIN messages ON users.id = messages.user_id"
      messages[] = [{}, {}, {}] // first_name, last_name, created_at, message,

    return render_template('wall.html', user=session['user'])

app.run(debug=True)
