from flask import Flask,request,url_for,redirect,render_template
import urllib2, json, api

app=Flask(__name__)
@app.route("/")
def index():
    ''' movie=request.args.get["movie"]
    values=api.final(movie) '''
    return render_template("home.html")

@app.route("/movies")
def movies():
    return render_template("results.html")

if __name__=="__main__":
    app.debug=True
    app.run()
