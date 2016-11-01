#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
import sys
import jsonpickle
import os
from pymongo import MongoClient

consumer_key = "JOXnfbeaHIwNfBqKNpsHWiv50"
consumer_secret = "JDHoT7iZisUiybSFPn7FmuiwK8gXUWseh7BVJ6HkYdh6HNjAU8"

access_token = "789152547449733120-n1dU0fUg1HwTA7ymAY8l1J0K1A5o1YF"
access_token_secret = "5v08p8n75bxNfKxP8M3s0mH8smFviNzNNK5z4VBDY1n48"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

fName = 'tweets.txt'

i=0

menu = {}
menu['1']="#SYRIZA tweet finder"
menu['2']="Negative emoticon"
menu['3']="Positive emoticon"

menu['4']="Exit"

while True:
  options=menu.keys()
  options.sort()

  for option in options:
      print option, menu[option]

  selection=raw_input("Please Select:")
  if selection =='1':
      i=0
      with open(fName, 'w') as f:
          for tweet in tweepy.Cursor(api.search,q="#SYRIZA",count=100).items():
              i=i+1
              print tweet.created_at, tweet.text
              f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                              '\n')
          print  "I found " , i , " tweets! Your results are on tweets.txt\n"

  elif selection == '2':
      con = MongoClient()
      db=con.test
      collection=db.test
      #print db.command("import -d test -c test tweets.txt")

      print db.test.find({'text': { '$regex' : 'δρόμο'}}).count()


  elif selection == '3':
      con = MongoClient()
      db=con.test
      collection=db.test
      print db.test.find({'text': { '$regex' : 'Μπράβο'}}).count()


  elif selection == '4':
      break
  else:
      print "Unknown Option Selected!"
