import twitter_credentials
from tweepy import API
from tweepy import OAuthHandler
from tweepy import Cursor
import pandas as pd
import numpy as np
import time
import csv

auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

api = API(auth)

form tweepy import Cursor  
friends_ids = []  
for page in Cursor(api.friends_ids, screen_name='wadu_hek').pages(): #Enter the user's screen name here
  friends_ids.extend(page)
  time.sleep(60)

screen_names = []
num_statuses = [] 

for id in friends_ids:
  u = api.get_user(id)
  screen_names.append(u.screen_name)
  num_statuses.append(u.statuses_count)
  
def get_all_tweets(screen_name):
  alltweets = []  
  new_tweets = api.user_timeline(screen_name=screen_name, count=200)  
  alltweets.extend(new_tweets)    
  oldest = alltweets[-1].id - 1    
  while len(new_tweets) > 0:  
    new_tweets = api.user_timeline(screen_name=screen_name, count=200,  max_id=oldest)        
    alltweets.extend(new_tweets)        
    if len(alltweets) > 500:            
      break        
    oldest = alltweets[-1].id - 1        
    print('%d tweets downloaded so far' % len(alltweets))    
    out_tweets = [[tweet.id_str, tweet.created_at,  tweet.text.encode("utf-8")] for tweet in alltweets]  
    with open('%s_tweets.csv' % screen_name, 'w') as f:    
      writer = csv.writer(f)    
      writer.writerow(['id', 'created_at', 'text'])    
      writer.writerows(out_tweets)    
 
for name in screen_names:  
  get_all_tweets(name) 
  
# write a function: Input: tweet files, output: dataframe[timestamp, tweet, sentiment]

