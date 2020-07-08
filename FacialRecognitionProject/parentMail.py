import pyrebase



def getParentMail():
    config = {
            "apiKey": "AIzaSyAzxtmgFs5yVJYbX3PzHrOvs0uv2JWvCos",
            "authDomain": "the-smart-guardian.firebaseapp.com",
            "databaseURL": "https://the-smart-guardian.firebaseio.com",
            "projectId": "the-smart-guardian",
            "storageBucket": "the-smart-guardian.appspot.com",
            "messagingSenderId": "905221282691"
          }
    firebase = pyrebase.initialize_app(config)

        # Get a reference to the auth service
    auth = firebase.auth()
    db = firebase.database()
    storage = firebase.storage()
    pmail={
        }
    all_users = db.child("Student").get()
    for user in all_users.each():
        id=user.key() 
        phone=db.child("Student").child(id).child("parent_phone").get().val()
        mail=db.child("Parent").child(phone).child("email").get().val()
        pmail[id]=mail
        #sname=db.child("Student").child(stdid).child("name").get().val()
    return pmail

if __name__=='__main__' :
    getParentMail()
