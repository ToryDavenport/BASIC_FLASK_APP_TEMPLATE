import flask
from flask import Flask
from flask import request
from flask import render_template
import pytest   

sample = Flask(__name__)
template = "idex.html"

@sample.route("/")
def main(): 
    return render_template(template)

def test():
    assert template == "index.html" 
if __name__ == "__main__": 
    sample.run(port=8080, host="10.2.0.100")
