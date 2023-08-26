from flask import Flask
import datetime  # Import the datetime module
import ssl  # Import the ssl module

from twilio.rest import Client

app = Flask(__name__)

account_sid = "AC163244aee3909a200ebc7bc3d705cc6b"
auth_token = "fd51d6d6253915854bc20b9fa1606601"
client = Client(account_sid, auth_token)


@app.route("/tracking_pixel/<email_subject>.png")
def track_email(email_subject):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("tracking_log.txt", "a") as log_file:
        log_file.write(
            f"get request received at {timestamp} for email subject: {email_subject}\n"
        )

    message = client.messages.create(
        body=f"your email with subject {email_subject}was opened at {timestamp}",
        from_="+14342774822",
        to="+919136490125",
    )

    print(message.sid)

    return "", 204  # Empty response with 204 No Content status


if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(
        certfile="cert.pem", keyfile="key.pem"
    )  # Use your generated certificate and key
    app.run(host="0.0.0.0", port=5055, ssl_context=context)
