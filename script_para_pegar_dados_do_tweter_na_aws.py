import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
job.commit()


import tweepy
import re
import json
import boto3

from tweepy import OAuthHandler

twitter_keys = {
    'consumer_key': 'eGyhuOTefIGDR86YnnJ6zHFwd',
    'consumer_secret': '8NTDVDA1nePi8C7Wt8YpOk0ps0FLSUQCAWQTjl1ntiaLarcgHH',
    'access_token_key': '709521801748070400-C00ITmfQE9o30yNo4DddjZ6XBxtYq0j',
    'access_token_secret': '80e7uMQ8WP8BVz3ZWlA3sCcyOqIz8LO73p7RTVC2dexkv'

}

# Configura acesso a API
auth = tweepy.OAuthHandler(
    twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(
    twitter_keys['access_token_key'], twitter_keys['access_token_secret'])

api = tweepy.API(auth)


# Post a tweet from Python
# api.update_status("Look, I'm tweeting from #Python in my #earthanalytics class! @EarthLabCU")
# Your tweet has been posted!


# Define the search term and the date_since date as variables

# Condição que filtra exatamente as palavras colocadas ex presidente bolsonaro ou os simbolos de sentimento
# search_words = "(presidente OR bolsonaro) AND (:( OR :{ OR :[ OR :) OR :D OR :])"


# search_words = "presidente OR bolsonaro OR ELEIÇÕES OR (:( OR :{ OR :[ OR :) OR :D OR :])lang:pt"

search_words = "(presidente OR bolsonaro) AND (:( OR :{ OR :[ OR :) OR :D OR :])"

# Collect tweets
tweets = tweepy.Cursor(api.search_tweets,
                       q=search_words,
                       lang="pt-br",
                       count=100,
                       result_type ='recent',
                       tweet_mode='extended' 
                       ).items(100)

my_json_list = []
# Iterate and print tweets
for tweet in tweets:
    my_json_list.append({
        "id": tweet.id,
        "full_text": tweet.full_text,
        "created_at": tweet.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "source": tweet.source,
        "retweet_count": tweet.retweet_count,
    })
    # print(tweet)

    # print(my_json_list)

    # file_name_save = re.sub(":", "-", my_json_list[0]['created_at'])
    # with open("./output/data_{}.json".format(file_name_save), 'w', encoding='utf-8') as f:
    #     json.dump(my_json_list, f, ensure_ascii=False, indent=4)

    file_name_save = re.sub(":", "-", my_json_list[0]['created_at'])

    # with open("s3://raw-zoni/data_{}.json".format(file_name_save), 'w', encoding='utf-8') as f:
    #     json.dump(my_json_list, f, ensure_ascii=False, indent=4)

    
    # Method 1: Object.put()
    s3 = boto3.resource('s3')
    object = s3.Object("raw-zoni", "brutos/data_{}.json".format(file_name_save))
    object.put(Body=json.dumps(my_json_list, ensure_ascii=False, indent=4))

    # with open("s3://raw-zoni/data.json".format(file_name_save), 'w', encoding='utf-8') as f:
    #     json.dump(my_json_list, f, ensure_ascii=False, indent=4)

    # Comando para usar no CRON "0/15 * ? * * *" para executar o script a cada 15 minutos