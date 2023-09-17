import ssl
import smtplib
from email.message import EmailMessage

def sendInvite(email_receiver):
    email_sender= 'harry#####@gmail.com'
    # email_receiver= "harshdeutschland@gmail.com"
    password= '############'
    subject=" hushHush Recruiter"
    body= f''' Dear Candidate,

            We are delighted to inform you that you have been selected as one of the top candidates for our open position of Full Stack Developer at Doodle. Congratulations!

            As the next step of our hiring process, we would like to invite you to participate in a coding challenge. The coding challenge will test your technical skills and problem-solving abilities.

            We encourage you to take your time and do your best on the challenge. You can use any programming language.

            To participate in the coding challenge, please follow the instructions below:

            Click on the following link to access the challenge: {"https://open.kattis.com/contests/d4zg4m"}
            Click on the "Start Challenge" button to begin.
            Complete the challenge within the allotted time.
            If you have any questions or concerns about the coding challenge, please do not hesitate to reach out to us. We are happy to help.

            We look forward to seeing your skills in action and wish you the best of luck!

            Best regards,

            Doodle 
            
            '''
          

    msg= EmailMessage()
    msg['from']= email_sender
    msg['to']= email_receiver
    msg['Subject']= subject
    msg.set_content(body)
    context = ssl.create_default_context() # Setting our SSL server
    smtp= smtplib.SMTP_SSL('smtp.gmail.com',port=465, context=context) # providing port and connection information
    smtp.login(email_sender,password)
    smtp.sendmail(email_sender,email_receiver,msg.as_string())

