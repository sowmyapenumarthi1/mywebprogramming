import os 
import json

def load_profile(username):
    try:
        os.makedirs('data/profiles', exist_ok=True)
        with open(f'data/profiles/{username}.profile','r') as f:
            profile = json.load(f)
    except Exception as e:
        profile = {}
    print('loaded profile = ',profile)
    return profile

def save_profile(profile):
    if 'username' not in profile:
        return
    username = profile['username']
    if username == 'guest':
        return
    os.makedirs('data/profiles', exist_ok=True)
    with open(f'data/profiles/{username}.profile','w') as f:
        json.dump(profile, f)