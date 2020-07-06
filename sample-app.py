import flask
from flask import Flask
from flask import request
from flask import render_template

sample = Flask(__name__)

@sample.route("/")
def main():
     return render_template("index.html")

if __name__ == "__main__":
     sample.run(port=8080, host="10.2.0.100")
