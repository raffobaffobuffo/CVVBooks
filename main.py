from flask import Flask, render_template
from client import Client
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
    books = client.GetBooks()
    return render_template("results.html", books=books)

if __name__=="__main__":
    app.run()
