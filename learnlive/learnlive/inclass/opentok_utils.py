# This is a utility file to handle the basics
# of the opentok server side initialization and
# management.
import OpenTokSDK

API_KEY='44594972'
API_SECRET='399c29f1e39b4af29e4445ba1cfc21afda9aa65d'
opentok_object = OpenTokSDK.OpenTokSDK(API_KEY, API_SECRET)

def create_session(isEnabled):
    session_prop = {OpenTokSDK.SessionProperties.p2p_preference: isEnabled}
    session = opentok_object.create_session(None, session_prop).session_id
    return session

def generate_token(session_id):
    token = opentok_object.generate_token(session_id)
    return token
