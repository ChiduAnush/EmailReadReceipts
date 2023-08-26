import smtplib, ssl
import getpass


port = 465
smtp_server = "smtp.gmail.com"
sender_email = "trials.chiduanush@gmail.com"
receiver_email = "puranjaybhargava@gmail.com"
# password = getpass.getpass("enter your password: ")
password = "uhtedjvnczphlosd"

message = """\
Subject: VERY IMPORTANT!

This message is sent from Python, hello from chiduanush.
OOLALALALA UOOOOOLELOOOOOOOOO

Anime dekhna band karle, zyada hi fan service hai tere anime me.
tsk tsk.

vaise, aaj blue shirt me bade segsy lag rahe ho ;)

"""

print("all inputs accepted")

context = ssl.create_default_context()

print("context created")
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    print("logged in")
    server.sendmail(sender_email, receiver_email, message)

print("donesies!")
