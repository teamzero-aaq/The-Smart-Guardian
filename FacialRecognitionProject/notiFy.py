from pyfcm import FCMNotification
def sendNoti():
    push_service = FCMNotification(api_key="AAAA0sNkm4M:APA91bFdYzj8GLrHvFvT6EMfFNSb2evCVAetsHFAkQPnj7423TNtXQJmtnTtVYYlsdFcxTrQn3R1u8HrTeGLXuPAh6GKYj2WmI6b1VsTQgP0BsC8rumpy7TajFlP6Kagl2Bc6G0fADpg")

    # OR initialize with proxies

    #proxy_dict = {
              #"http"  : "http://127.0.0.1",
             # "https" : "http://127.0.0.1",
            #}
    push_service = FCMNotification(api_key="AAAA0sNkm4M:APA91bFdYzj8GLrHvFvT6EMfFNSb2evCVAetsHFAkQPnj7423TNtXQJmtnTtVYYlsdFcxTrQn3R1u8HrTeGLXuPAh6GKYj2WmI6b1VsTQgP0BsC8rumpy7TajFlP6Kagl2Bc6G0fADpg")#, proxy_dict=proxy_dict)

    # Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

    #registration_id=db.child("Student").child(stdid).child("name").get().val()
    registration_id = "c_SOyDR4QYk:APA91bG77mb6dRCMtqe6JsVdN753Pa8huGnhJt5-0eG4-PGjtZGTnYKLCsOCDozYn9TT_GKrQU1WTYtV9MxdzcqVUxah44S3XOxLGBjKLV3gO_u2gRGOd-nh53UwSHOh2XrIP2QI9iWa"
    message_title = "The Guardian Bus Update"
    message_body = "Hi, your son is in Bus"
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

if __name__=='__main__' :
    sendNoti()


#print(result)