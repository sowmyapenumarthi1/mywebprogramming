from bottle import route, run



@route("/")
def get_index():
    return ("Home page --")
@route("/hello")
def get_hello():
    return ("hello!")
@route("/hello/<name>")
def get_hello(name):
    return (f"hello! {name}!")

run(host="localhost", port=8060)
