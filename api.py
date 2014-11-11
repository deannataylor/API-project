import urllib2
import json

url="http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=au5nf6pd9fwwh4kjbqqt6jws&q=%s"
key = "au5nf6pd9fwwh4kjbqqt6jws"

def getStuff(query):
    request = urllib2.urlopen(url % (query))
    result = request.read()
    d = json.loads(result)
    print d["total"]
    movies = d["movies"] 
    for m in movies:
        print m["title"]

def search(query):
    request = urllib2.urlopen(url % (query))
    result = request.read()
    d = json.loads(result)
    movies = d["movies"]
    for m in movies:
        for a in m["abridged_cast"]:
            if a["name"] == query:
                print url

if __name__ == "__main__":
    getStuff("Toy+Story+3")
    

"""
names of stuff:
"title"
"ratings"["critics_score","audience_score"]
"abridged_cast" ["name": , "characters ]
"""


