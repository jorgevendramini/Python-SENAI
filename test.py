from twilio.rest import Client

account_sid = "AC10b298fcf30ed2dd19b571cc9d94aa23"

auth_token = "1bf5352aceaa5de3eb4a3656fcd02877"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5511977020912",
    from_="+18325147987",
    body="Oiii m"
)

print(message.sid)
