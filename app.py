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
  account_sid = 'AC3e6f069fc91041066f0f8f8d21a39780'
  auth_token = '72f15924d14fa7ea6dfea469a3c79b5a'
  client = Client(account_sid, auth_token)
 

  # Use the Twilio API to send a message
  message = client.messages.create(body=response,from_='whatsapp:+14155238886',to='whatsapp:+918341655595')
  #print(message)
  print(message.sid)
  return 'Response sent'


if __name__ == "__main__":
  app.debug = True
  app.run()
