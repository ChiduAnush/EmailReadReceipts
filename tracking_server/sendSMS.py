import os
from twilio.rest import Client


account_sid = "AC163244aee3909a200ebc7bc3d705cc6b"
auth_token = "fd51d6d6253915854bc20b9fa1606601"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="i will do it!",
    from_="+14342774822",
    to="+919136490125",
)

print(message.sid)
