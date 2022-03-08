from client import Client
from flask import Flask, jsonify
import json
import sys

uid, pwd = sys.argv[1], sys.argv[2]

while True:
    try:
        client = Client(uid, pwd)
        break
    except AssertionError:
        print("Wrong credentials")
        uid = input("UID: ")
        pwd = input("PWD: ")

app = Flask(__name__)

@app.route("/")
def showBook():
    client.GetBooks()
    books = json.dumps(client.Books)
    return books

if __name__=="__main__":
    app.run()
