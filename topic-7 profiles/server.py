from bottle import run, template, default_app
from bottle import get, post 
from bottle import debug
from bottle import request, response, redirect

from session import load_session, save_session

#####

import os 
import json

def new_profile(username):
    profile = {
        'username' : username,
        'password' : 'no_password'
    }
    os.makedirs('data/profiles', exist_ok=True)
    with open(f'data/profiles/{username}.profile','w') as f:
        json.dump(profile, f)
    return profile

def load_profile(username):
    try:
        os.makedirs('data/profiles', exist_ok=True)
        with open(f'data/profiles/{username}.profile','r') as f:
            profile = json.load(f)
    except Exception as e:
        print(f'Profile error:{e}')
        profile = new_profile(username)
    print('loaded profile = ',profile)
    return profile

def save_profile(profile):
    username = profile['username']
    if username == 'guest':
        return
    os.makedirs('data/profiles', exist_ok=True)
    with open(f'data/profiles/{username}.profile','w') as f:
        json.dump(profile, f)
    
#####

def not_logged_in(session):
    if 'username' not in session:
        return True
    if session['username'] == 'guest':
        return True

@get('/')
@get('/hello')
def get_hello(name=None):
    # get the current session
    session = load_session(request)

    # if not logged in, redirect to someplace
    if not_logged_in(session):
        redirect("/login")

    # get the username from session
    username = session.get('username', 'guest')

    # get the profile
    profile = load_profile(username)
    favcolor = profile.get('favcolor', 'not known')

    # save the session 
    print('saving loaded session',session)
    save_session(session, response)

    #return the requested web page
    return template('hello', name=username, color=favcolor)

@get('/signup')
def get_login():
    session = load_session(request)
    session['username'] = 'guest'
    save_session(session, response)
    return template('signup', message='')

@post('/signup')
def post_signup():
    # load the session
    session = load_session(request)

    # get the form information
    username = request.forms['username']
    password = request.forms['password']
    password_again = request.forms['password_again']

    # get the profile if there is one
    profile = load_profile(username)
    print('signup starting ',profile)

    # see if it's an established profile
    if profile['password'] != 'no_password':
        print("ALREADY A CUSTOMER")
        save_session(session, response)
        redirect('/login')

    # finish the login
    profile['password'] = password
    session['username'] = username

    # save_profile(profile)
    save_profile(profile)
    save_session(session, response)
    redirect('/hello')

@get('/login')
def get_login():
    session = load_session(request)
    session['username'] = 'guest'
    save_session(session, response)
    return template('login', message='')

@post('/login')
def post_login():
    # load the session
    session = load_session(request)

    # get the form information
    username = request.forms['username']
    password = request.forms['password']
    favcolor = request.forms['favcolor']

    # get the profile for username
    profile = load_profile(username)
    print("loaded profile",profile)
    print('password',password)
    if profile['password'] != password:
        save_session(session, response)
        redirect('/hello')

    print("logged in")

    # save user in the session
    session['username'] = username

    # get profile for the user
    profile['favcolor'] = favcolor

    save_profile(profile)
    save_session(session, response)
    redirect('/hello')

debug(True)
run(host='localhost', port=8060, reloader=True)
