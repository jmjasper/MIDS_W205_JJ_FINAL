from __future__ import absolute_import, print_function, unicode_literals

import itertools, time
import tweepy, copy 
import Queue, threading
import json

from streamparse.spout import Spout

#import psycopg2

################################################################################
# Twitter credentials
################################################################################
twitter_credentials = {
    "consumer_key"        :  "WuI1Wfos7MUzYFgUojNIbrQ1p",
    "consumer_secret"     :  "eD44zqpwbdPyAOztQRK2H7QkSCQnPxLQ2AnIiFAj0MzD1Zo2Vu",
    "access_token"        :  "4041131898-SZlgmPe3OdjN2HC8Lt4r7LfcnzwrkUsrXnCxOyS",
    "access_token_secret" :  "i5eQGhYOKZ0YRCluHgsgkCs20X9luV7jPYw0q6FiQW28N",
}

def auth_get(auth_key):
    if auth_key in twitter_credentials:
        return twitter_credentials[auth_key]
    return None

################################################################################
# Class to listen and act on the incoming tweets
################################################################################
class TweetStreamListener(tweepy.StreamListener):

    def __init__(self, listener):
        self.listener = listener
        super(self.__class__, self).__init__(listener.tweepy_api())

    def on_status(self, status):
        #Editted status.text to status for whole json object
        self.listener.queue().put(status, timeout = 0.01)
        return True
  
    def on_error(self, status_code):
        return True # keep stream alive
  
    def on_limit(self, track):
        return True # keep stream alive

class Tweets(Spout):

    def initialize(self, stormconf, context):
        self._queue = Queue.Queue(maxsize = 100)

        consumer_key = auth_get("consumer_key") 
        consumer_secret = auth_get("consumer_secret") 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        if auth_get("access_token") and auth_get("access_token_secret"):
            access_token = auth_get("access_token")
            access_token_secret = auth_get("access_token_secret")
            auth.set_access_token(access_token, access_token_secret)

        self._tweepy_api = tweepy.API(auth)

        # Create the listener for twitter stream
        listener = TweetStreamListener(self)

        # Create the stream and listen for english tweets add track to stream.filter to change what's being
        stream = tweepy.Stream(auth, listener, timeout=None)
        stream.filter(languages=["en"], track=["disney"], async=True)

    def queue(self):
        return self._queue

    def tweepy_api(self):
        return self._tweepy_api

    def next_tuple(self):
        try:
            #Read the queue
            tweet = self.queue().get(timeout = 0.1)
            
            #Text Componenets
            sentence = tweet.text
            created = tweet.created_at
            reply_user_id = tweet.in_reply_to_user_id
            reply_screename = tweet.in_reply_to_screen_name
            reply_status = tweet.in_reply_to_status_id
            retweeted = tweet.retweet_count

            #User Components
            user_id = tweet.user.id
            screen_name = tweet.user.screen_name
            name = tweet.user.name
            location = tweet.user.location
            lang = tweet.user.lang


            #hashtags = tweet.entities.hashtags

            if tweet:
                self.queue().task_done()
                try:
                    #Tweet
                    #self.log(tweet)

                	#Text
                    self.log(sentence)
	            self.log(created)
                    self.log(reply_user_id)
                    self.log(reply_screename)
                    self.log(reply_status)
                    self.log(retweeted)

                    #User_Id
                    self.log(user_id)
                    self.log(screen_name)
                    self.log(name)
                    self.log(location)
                    self.log(lang)

                    #Hashtags

                    self.emit([tweet])
                except:
                	#self.log("Unicode Error!")
                	pass
                
        except Queue.Empty:
            pass
            #self.log("Empty queue exception")
            time.sleep(0.1) 

    def ack(self, tup_id):
        pass  # if a tuple is processed properly, do nothing

    def fail(self, tup_id):
        pass  # if a tuple fails to process, do nothing
