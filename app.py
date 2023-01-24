from flask import Flask, request
from twilio.rest import Client
import os

app = Flask(__name__)


@app.route("/sms", methods=['POST'])
def sms():
  message_body = request.form.get('Body')
  phone_number = request.form.get('From')
  response = "hi, how you doin"

  # Twilio account information
  account_sid = os.environ['TWILIO_ACCOUNT_SID']
  auth_token = os.environ['TWILIO_AUTH_TOKEN']
  client = Client(account_sid, auth_token)
 

  # Use the Twilio API to send a message
  message = client.messages.create(body=response,from_='whatsapp:+14155238886',to='whatsapp:+918341655595')
  #print(message)
  print(message.sid)
  return 'Response sent'


if __name__ == "__main__":
  app.debug = True
  app.run()
