import urllib2, json

t_url="http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=au5nf6pd9fwwh4kjbqqt6jws&q=%s"
article_url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?&fq=pub_date:(%s) AND news_desk:(\"Movies\")&api-key=c45e227370aff9e7405b5f40db5249cf:12:70174992"
a = "http://api.nytimes.com/svc/search/v2/articlesearch.json?&fq=pub_date:(%s)&api-key=c45e227370aff9e7405b5f40db5249cf:12:70174992"

def getMovie(query):
    '''
    query: words+words
    returns: YYYY-MM-DD
    '''
    request = urllib2.urlopen(t_url % (query))
    result = request.read()
    d = json.loads(result)
    return d["movies"][0]  # returns first movie that gets returned 

def getDate(movie):
    thing = getMovie(movie)
    return thing['release_dates']['theater']

def getArticles(date):
    '''
    date: in the form YYYY-MM-DD
    '''
    #request = urllib2.urlopen(article_url % (date))
    
    request = urllib2.urlopen(a % (date))
    result = request.read()
    d = json.loads(result)
    articles = d['response']['docs']
    i = 0
    while i < len(articles) and i < 5:
        print articles[i]['headline']['main']
        i=i+1

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

    print getDate("Toy+Story+3")
    #getArticles("1997-01-07")
    #a = a % ("2014-11-11", "Sports")
    
    

"""
TOMATOES:
names of stuff:
"title"
"ratings"["critics_score","audience_score"]
"abridged_cast" ["name": , "characters ]
"""

"""
NYTIMES ARTICLES: 
http://api.nytimes.com/svc/search/v2/articlesearch.json?&fq=pub_date:(2014-11-11)%20AND%20news_desk:(%22Movies%22)&api-key=c45e227370aff9e7405b5f40db5249cf:12:70174992

under fq: &fq=news_desk:("Sports" "Foreign")
    pub_date	Timestamp (YYYY-MM-DD)
    news_desk	Single token
    news_desk.contains	Multiple tokens

begin_date = YYYYMMDD
end_date = YYYYMMDD

"""
