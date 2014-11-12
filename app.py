from flask import flash, Flask,request,url_for,redirect,render_template
import urllib2, json, api

app=Flask(__name__)
app.secret_key = 'a'

@app.route("/")
def index():  
    return render_template("home.html")

@app.route("/movies", methods=['POST','GET'])
def movies():
    if request.method == 'POST':
        movie=request.form["movie"]
        articles=api.final(movie) 
        return render_template("results.html",articles=articles)
    else:
        flash("Enter a movie")
        return redirect('/')

if __name__=="__main__":
    app.debug=True
    app.run()
