from bottle import route, run, template



@route("/")
def get_index():
    return ("Home page --")
@route("/hello")
def get_hello():
    return ("hello!")
@route("/hello/<name>")
def get_hello(name="World"):
    return template("hello", name="Maddy", extra=None)
@route("/greet")
@route("/greet/<name>")
def get_greet(name="world"):
    return template("hello", name="Maddy", extra="Cheeeeeeeers!")
@route("/greeting/<names>")
def get_greeting(names):
    names = names.split(',')
    return template("greetings", names=names)

run(host="localhost", port=8060)
