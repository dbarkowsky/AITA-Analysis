import os
import csv
from refined_post import Refined_Post
from datetime import datetime

timestamp = datetime.now()
total_records = 0
romantic_records = 0

# Write headers to CSV
with open(f"./combined_posts.csv", "w", encoding="utf-8") as file:
    file.write(Refined_Post.getHeader())

# Collect rows from raw collected data
files = os.listdir("./csvFiles")
posts = []
for current_file in files:
    with open(f"./csvFiles/{current_file}", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        # Skip first line
        reader.__next__()
        for row in reader:
            total_records += 1
            post = Refined_Post(row)
            posts.append(post.getRow())

# Append to CSV
with open(f"./combined_posts.csv", "a", encoding="utf-8") as file:
    for post in posts:
        file.write(post)
    print("Done combining posts.")
    print(f"Total Records: {total_records}")
