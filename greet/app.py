from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def welcome_pg():
    return "Welcome"

@app.route('/welcome/home')
def welcome_home_pg():
    return "Welcome Home"

@app.route('/welcome/back')
def welcome_back_pg():
    return "Welcome Back"