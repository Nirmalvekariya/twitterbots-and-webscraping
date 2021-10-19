from tweepy  import OAuthHandler, API
import requests
from bs4 import BeautifulSoup


# Credentials to access Twitter APIs
ACCESS_TOKEN    = 'paste your access token here'
ACCESS_SECRET   = 'paste your access secret here'
CONSUMER_KEY    = 'paste your consumer key here'
CONSUMER_SECRET = 'paste your consumer secret here'


Auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
Auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
TwitterBot = API(Auth)


r=requests.get("http://zeenews.india.com/")
c=r.content

soup=BeautifulSoup(c,"html.parser")

#Find Items
all=soup.find_all("div",{"class":"lead-head"})
for item in all:
    TwitterBot.update_status(item.find_all("h1")[0].text+' '+"#zeenews"+"#newsofday")
