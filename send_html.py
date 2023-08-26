import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "trials.chiduanush@gmail.com"
receiver_email = "pariketrao2709@gmail.com"
password = "uhtedjvnczphlosd"

message = MIMEMultipart("alternative")
email_subject = "pariket trial1"
message["Subject"] = email_subject
message["From"] = sender_email
message["To"] = receiver_email

text = """

Hey, 
wassupp?

time to build stuff 
0~0

"""
html = f"""\

<html>
    <body>
        <p>Hello there, <br>
            Here's somthing you wanna see. <br>
            <img src=" https://8622-103-4-221-252.ngrok.io/tracking_pixel/{email_subject}.png" alt=""> <br>
            Email Subject: {email_subject} <br>


        </p>
    </body>
</html>


"""


part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1)
message.attach(part2)


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
