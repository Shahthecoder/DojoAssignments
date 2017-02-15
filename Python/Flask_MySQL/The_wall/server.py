from flask import Flask, request, redirect, render_template, session, flash, escape
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = 'CodingNinja'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'Wall')
