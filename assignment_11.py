#Q1. What is access token? Generate access token for any API.


"""
Access tokens are the thing that applications use to make API requests on behalf of a user. The access token represents the authorization of a specific application to access specific parts of a user’s data.
An access token is a unique string of letters and numbers that we pass with every API call.
Each access token is associated with:
   - API application.
   - The user we are acting on behalf of (for merchants, etc).
   - The permissions our app has for that user.

Access Token for twitter via JWT online generator:

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE1Mjk0ODY5MzQsImV4cCI6MTU2MTAyMjkzNCwiYXVkIjoid3d3LnR3aXR0ZXIuY29tIiwic3ViIjoiU2F1cmF2IFZlcm1hIiwiR2l2ZW5OYW1lIjoiU2F1cmF2IiwiU3VybmFtZSI6IlZlcm1hIiwiRW1haWwiOiJ2ZXJtYWdldUBnbWFpbC5jb20iLCJSb2xlIjpbIlN0dWRlbnQiLCJUcmFpbmVlIl19.pjtOqyCfjGlYnZ_wC0mKEIeEfF8TWQ2Lv_oysOrs2IU
"""




#Q2. Get Ip Address of some sites using DNS Lookup.


import socket
addr1 = socket.gethostbyname('www.google.com')
addr2 = socket.gethostbyname('www.facebook.com')
print("IP Address of google.com: %s\nIP Address of facebook.com: %s " % (addr1, addr2))




#Q3. Using tweepy extract tweets from twitter


import tweepy
from datetime import datetime, date, time, timedelta
import sys
import textblob
#The actual keys & secrets aren't shared for obvious reasons here
consumer_key = "tR0N4gxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret = "8qvl96Rkvxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_key = " 861540811514xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_secret = " 1BteblELkbxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)
api=tweepy.API(auth)
account_list = []
if (len(sys.argv) > 1):
    account_list = sys.argv[1:]
else:
    print("Please provide a list of usernames at the command line.")
    sys.exit(0)
if len(account_list) > 0:
    for target in account_list:
        print("Getting data for " + target)
        item = auth_api.get_user(target)
        print("name: " + item.name)
        print("screen_name: " + item.screen_name)
        print("description: " + item.description)
        print("statuses_count: " + str(item.statuses_count))
        print("friends_count: " + str(item.friends_count))
        print("followers_count: " + str(item.followers_count))




#Q4. Difference Between Library & API


"""
-------------------------------------------------------------------------------------------------------------------------------------------
               LIBRARY                                                       |                   API
                                                                             |
- A library is a collection of code built to perform common tasks            |  - API is a part of library which defines how an application communicates with external code .
- Library is written in same language which in which it is used              |  - API can be written in any language
- Library code tends to be relatively stable and bug free.                   |  - APIs should be defined before the code implementing them is implemented. 
- Use of appropriate libraries can reduce the amount of code the need to be  |  - APIs should be stable, although portions of the API can be deprecated 
  written. It will tend to reduce line of code counts for an application     |  - The more broadly used the API the more difficult it is to change it.
  will increasing the rate at which functionality is delivered.              |  - e.g. Google Maps API for JavaScript, flickrj is API for Flickr in JAVA
- Usually, it's better to use a library routine than to write own code.      |         tweepy is an API for Twitter, spotipy is an API for Spotify
- e.g. Numpy is a library of Python for matrices & mathematical handling,    |  
       math is a library to handle numberal operations                       |
"""





#Q5. Access Spotify API & try to play some music & find some libraries



import spotipy
katyperry_uri = 'spotify:artist:6jJ0s89eD6GaHleKKya26X'
spotify = spotipy.Spotify()
results = spotify.artist_albums(katyperry_uri, album_type = 'album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])
for album in albums:
    print((album['name']))