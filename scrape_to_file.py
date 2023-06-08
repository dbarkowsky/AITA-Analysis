import requests
from refined_post import Refined_Post
import time
import os
from datetime import datetime

# Writes a list of posts to a csv file
def append_to_file(post_list, timestamp):
  with open(f'filtered_posts_{timestamp.date()}.csv', 'a', encoding='utf-8') as file:
    for post in post_list:
      text = str(post.text).replace(",", "").replace("\n", " ").replace("\r", "")
      title = str(post.title).replace(",", "")
      file.write(f'{post.author},{post.created},{post.flair},{title},{text},{post.score},{post.edited},{post.locked},{post.num_comments},{post.num_awards},{post.ups},{post.downs},{post.ratio}\n')

max_posts = 1000
time_between_scrapes = 0.2
limit = 100
good_record_count = 0
desired_flairs = ['Not the A-hole', 'Asshole', 'No A-holes here', 'Everyone Sucks']
last_post = ''
number_of_calls = 0
timestamp = datetime.now()

# Does file already exist? If not make file with headers
if (not os.path.isfile(f'filtered_posts_{timestamp.date()}.csv')):
  with open(f'filtered_posts_{timestamp.date()}.csv', 'a', encoding='utf-8') as file:
    file.write('Author,Created,Flair,Title,Text,Score,Edited,Locked,NumComments,NumAwards,Ups,Downs,Ratio\n')

# Collect posts
while good_record_count < max_posts:
  response = requests.get(f'https://www.reddit.com/r/AmItheAsshole/new.json?limit={limit}&t=all&after={last_post}', headers = {'User-agent': 'AITA Scraper'})
  print(response.status_code)
  number_of_calls += 1
  print(f'Call number {number_of_calls}')

  dictionary_posts = response.json() # type is dictionary
  posts_list = dictionary_posts['data']['children'] # convert to list of posts
  if len(posts_list) > 0:
    last_post = posts_list[-1]['data']['name']
    refined_posts_list = []
    for post in posts_list:
      if post['data']['link_flair_text'] in desired_flairs:
        refined_post = Refined_Post()
        refined_post.author = post['data']['author']
        refined_post.created = post['data']['created']
        refined_post.downs = post['data']['downs']
        refined_post.edited = post['data']['edited']
        refined_post.flair = post['data']['link_flair_text']
        refined_post.locked = post['data']['locked']
        refined_post.num_comments = post['data']['num_comments']
        refined_post.score = post['data']['score']
        refined_post.text = post['data']['selftext']
        refined_post.title = post['data']['title']
        refined_post.num_awards = post['data']['total_awards_received']
        refined_post.ups = post['data']['ups']
        refined_post.ratio = post['data']['upvote_ratio']
        good_record_count += 1
        refined_posts_list.append(refined_post)
    append_to_file(refined_posts_list, timestamp)
    print(f'Records saved so far: {good_record_count}')
    time.sleep(time_between_scrapes) # To avoid rate limiter
  else:
    break
