# sessions.py
 
import os 
import json
import random
import string
from bottle import request, response

def random_id():
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=16))

def new_session():
    session_id = random_id()
    session = { 'session_id':session_id }
    os.makedirs('data/sessions', exist_ok=True)
    with open(f'data/sessions/{session_id}.session', 'w') as f:
        json.dump(session, f)
    response.set_cookie('session_id',session_id)
    return session

def load_session(request):
    session_id = request.get_cookie('session_id', default=None)
    try:
        if session_id == None:
            raise Exception('No session id cookie found.')
        os.makedirs('data/sessions', exist_ok=True)
        with open(f'data/sessions/{session_id}.session', 'r') as f:
            session = json.load(f)
    except Exception as e:
        print('session error:', e)
        session = new_session()
    print('loaded session', session)
    return session

def save_session(session, response):
    session_id = session['session_id']
    os.makedirs('data/sessions', exist_ok=True)
    with open(f'data/sessions/{session_id}.session', 'w') as f:
        json.dump(session, f)
    response.set_cookie('session_id',session_id)
    print('saved session', session)