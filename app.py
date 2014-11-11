from flask import Flask,request,url_for,redirect,render_template
import urllib2, json, api

app=Flask(__name__)
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/movies")
def movies():
    return render_template("results.html")

if __name__=="__main__":
    app.debug=True
    app.run()
