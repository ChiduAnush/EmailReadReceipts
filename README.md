A simple program which can detect when your email was opened by the recipient and then send an sms message to your phone, telling you the timestamp and the email subject, wich was opened.

fill up all your required data, email, phone numbers, and id for twilio sms to work.
check the 2 files `app.py` and `send_html.py`

after you are done,
run `python app.py` inside the tracker_server folder,
ru the command `ngrok http https://localhost:5055`

copy the forward link you get and replace it with the matching part of the link in the send_html.py file.

then run `python send_html.py`
