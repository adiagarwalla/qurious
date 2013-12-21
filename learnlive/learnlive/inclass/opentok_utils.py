# This is a utility file to handle the basics
# of the opentok server side initialization and
# management.
import OpenTokSDK

API_KEY='44586332'
API_SECRET='9233963d604d4d8a944468b1e135aaf213db1285'
opentok_object = OpenTokSDK.OpenTokSDK(API_KEY, API_SECRET)

def create_session(isEnabled):
    session_prop = {OpenTokSDK.SessionProperties.p2p_preference: isEnabled}
    session = opentok_object.create_session(None, session_prop)
    return session

def generate_token(session_id):
    token = opentok_object.generate_token(session_id)
    return token
