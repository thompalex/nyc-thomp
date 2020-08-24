import os, random
from flask import Flask, session, render_template, redirect, url_for, request, flash
import json
app = Flask(__name__)
app.secret_key = "2"

@app.route("/") #assign following fxn to run when root route requested
def hello_world():
    print(__name__) #where will this go?
    return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
