from flask import Flask
from flask.wrappers import Request
from twilio.rest import Client
from flask import request
from marketstack import get_stock_price
import os

app = Flask(__name__)

ACCOUNT_ID = os.environ.get('TWILIO_ACCOUNT')
TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN')
client = Client(ACCOUNT_ID,TWILIO_TOKEN)
TWILIO_NUMBER = 'whatsapp:+14155238886'

def send_msg(msg,recipient):
    client.messages.create(
        from_=TWILIO_NUMBER,
        body=msg,
        to=recipient
    )

def process_msg(msg):
    response= ""
    if msg == "hi":
        response = "Hello, Welcome to the stock market Bot!"
        response+="Type sym:<stock_symbol> to know the price of the stock."
    elif 'sym:' in msg:
        data = msg.split(":")
        stock_symbol = data[1]
        stock_price = get_stock_price(stock_symbol)
        last_price = stock_price['last_price']
        last_price_str = str(last_price)
        response = "the stock price of "+ stock_symbol +" is: $"+ last_price_str

    else:
        response = "Please type hi to get Started."
    return response 


@app.route("/webhook", methods = ["POST"])
def webhook():
    f=request.form 
    msg=f['Body']
    sender=f['From']
    response = process_msg(msg)
    send_msg(response,sender)
    return "OK",200
      

     
