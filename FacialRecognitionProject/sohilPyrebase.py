from datetime import datetime
import pyrebase
import os
import uuid


def sendmsg(id):
    
    
        
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
    #upload file to db
    dir='786image.jpg'
    
    file=uuid.uuid4().hex[:10]
    #print(dir)
    #print(file)
    storage.child("BusImages").child(file).put(dir)
    img=storage.child("BusImages").child(file).get_url(1)


    # create message local
    stdid=id
    #print(d)
    date=str(datetime.now().day)+"-"+datetime.now().strftime("%B")

    sname=db.child("Student").child(stdid).child("name").get().val()

    message="Your son "+sname+" is in bus at "+datetime.now().strftime("%I:%M")

    #create msg in jsno
    data = {
        "date": date, "message": message, "photo": img
    }

    #send message
    db.child("Message").child(stdid).set(data)
    print("Image updated.")



if __name__=='__main__' :
    sendmsg()