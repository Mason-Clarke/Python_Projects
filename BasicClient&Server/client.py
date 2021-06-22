from flask.globals import request
from flask.json import jsonify
import requests
import json

def send(b00, message):
    url = "http://10.8.0.11:8085"
    body = { "b00": b00, "message": message}

    response = requests.post(url, json = body)

    

    if response.status_code == 200:
        print("Ok")
    else:
        print(response.status_code, response.text)



    

print("Welcome to the chat!")
print("Please enter your B00", end = " ")
b00 = input()
print()

while True:
    print("> ", end = "")
    message = input()

    if message == "quit":
        break

    send(b00, message)


