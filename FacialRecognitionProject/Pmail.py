import RPi.GPIO as gpio
import picamera
import time

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from email.mime.image import MIMEImage
 
##fromaddr = "moinuddin.ub@somaiya.edu"    # change the email address accordingly
##toaddr = ""
## 
##mail = MIMEMultipart()
## 
##mail['From'] = fromaddr
##mail['To'] = toaddr
##mail['Subject'] = "Attachment"
##body = "Please find the attachment"
##
##
##
##data=""

def sendMail(data):
    fromaddr = "moinuddin.ub@somaiya.edu"    # change the email address accordingly
    toaddr = data
 
    mail = MIMEMultipart()
 
    mail['From'] = fromaddr
    mail['To'] = toaddr
    mail['Subject'] = "Attachment"
    body = "Please find the attachment.Your child is safe and is inside the bus"



    data="hi" 
     
    
    mail.attach(MIMEText(body, 'plain'))
    print data
    dat='786image.jpg'
    print dat
    attachment = open(dat, 'rb')
    print("attach")
    image=MIMEImage(attachment.read())
    attachment.close()
    mail.attach(image)
    print("img att")
    server = smtplib.SMTP('smtp.gmail.com', 46)#587)
    print("stmp")
    print("starttls")
    server.starttls()
    print("starttls complted")
    
    server.login(fromaddr, "sadiq6786")
    
    print("Log in success")
    text = mail.as_string()
    server.sendmail(fromaddr, toaddr, text)
    print("message sent")
    server.quit()

##def capture_image():
##    data= time.strftime("%d_%b_%Y|%H:%M:%S")
##    camera.start_preview()
##    time.sleep(5)
##    print data
##    camera.capture('%s.jpg'%data)
##    camera.stop_preview()
##    time.sleep(1)
##    sendMail(data)

##gpio.output(led , 0)
##camera = picamera.PiCamera()
##camera.rotation=180
##camera.awb_mode= 'auto'
##camera.brightness=55
##while 1:
##    if gpio.input(pir)==1:
##        gpio.output(led, HIGH)
##        capture_image()
##        while(gpio.input(pir)==1):
##            time.sleep(1)
##        
##    else:
##        gpio.output(led, LOW)
##        time.sleep(0.01)

if __name__=='__main__' :
    sendMail()
