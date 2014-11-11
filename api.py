import urllib2, json

t_url="http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=au5nf6pd9fwwh4kjbqqt6jws&q=%s"
article_url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=%s&end_date=%s&api-key=c45e227370aff9e7405b5f40db5249cf:12:70174992"


def getMovie(query):
    request = urllib2.urlopen(t_url % (query))
    result = request.read()
    d = json.loads(result)
    return d["movie"][0]  # returns first movie that gets returned 

def getDate(movie):
    return movie['relase_dates']['theater']

def getArticles(date):
    '''
    date: in the form YYYYMMDD
    '''
    request = urllib2.urlopen(article_url % (date,date))
    result = request.read()
    d = json.loads(result)
    articles = d['response']['docs']
    for i in range(5):
        print articles[i]['headline']['main']

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
    #getStuff("Toy+Story+3")
    getArticles(20141111)

"""
TOMATOES:
names of stuff:
"title"
"ratings"["critics_score","audience_score"]
"abridged_cast" ["name": , "characters ]
"""

"""
NYTIMES ARTICLES: 
articles_url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=%s&end_date=%s]&api-key=c45e227370aff9e7405b5f40db5249cf:12:70174992"

under fq: &fq=news_desk:("Sports" "Foreign")
    pub_date	Timestamp (YYYY-MM-DD)
    news_desk	Single token
    news_desk.contains	Multiple tokens

begin_date = YYYYMMDD
end_date = YYYYMMDD

"""
