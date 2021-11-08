from bottle import Response, run, template, default_app
from bottle import get, post 
from bottle import request 
from bottle import debug
from bottle import response
 

@get("/")
def get_index():
    return ("home page!")

@get("/hello")
@get("/hello/<name>")
def get_hello(name=None):
    current_user = request.get_cookie("username", default="world")
    print("current user = ",current_user)
    if name == None:
       name = current_user
    return template('hello', name=name, extra=None)

@get("/greet")
@get("/greet/<name>")
def get_greet(name="world"):
    return template("hello", name="Maddy", extra="Cheerssssssssss!")

@get("/greeting/<names>")
def get_greeting(names):
    names = names.split(',')
    return template('greetings', names=names)

@get("/login")
def get_login():
    return template("login", message="")

@post("/login")
def post_login():
    global current_user
    username = request.forms['username']
    password = request.forms['password']
    if password != "magic":
        return template("login", message="Bad password")
    current_user = username
    response.set_cookie("username",username)
    return template("hello", name=username+"!!!!", extra="Cheerssssssssss!")

debug(True)
run(host="localhost", port=8060, reloader=True)