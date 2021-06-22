from flask_cors.decorator import cross_origin
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
@cross_origin()
def receive ():
    content = request.get_json()
    message = content["message"]
    print(message)
    print(content)

    return("", 200)
