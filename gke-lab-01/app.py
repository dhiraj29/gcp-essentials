# The Docker image contains the following code
from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def showPinehead():
    html = "<div style='text-align:center;margin:20px;'><h1>Greetings from My Excellent Blog...!!!</h1><img src='https://storage.cloud.google.com/vital-reef-274105/my-excellent-blog.png' width='40%' alt='Pinehead @Radical Technology'></div>"
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)