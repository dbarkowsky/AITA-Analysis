import os
import csv
from refined_post import Refined_Post
from datetime import datetime


def get_all_posts():
    global total_records
    global romantic_records
    posts = []
    files = os.listdir("./csvFiles")
    for current_file in files:
        with open(f"./csvFiles/{current_file}", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            # Skip first line
            reader.__next__()
            for row in reader:
                total_records += 1
                post = Refined_Post(row)
                isRomantic = post.isRomantic()
                if isRomantic:
                    romantic_records += 1
                posts.append(
                    f"{','.join(row)},{post.getAgeRange()},{isRomantic},{len(post.getIdentifiers())}\n"
                )
    return posts


timestamp = datetime.now()
total_records = 0
romantic_records = 0

with open(f"./combined_posts_{timestamp.date()}.csv", "w", encoding="utf-8") as file:
    file.write(
        "Author,Created,Flair,Title,Text,Score,Edited,Locked,NumComments,NumAwards,Ups,Downs,Ratio,Range,IsRomantic,NumParticipants\n"
    )
with open(f"./combined_posts_{timestamp.date()}.csv", "a", encoding="utf-8") as file:
    post_list = get_all_posts()
    for post in post_list:
        file.write(post)
    print("Done combining posts.")
    print(f"Total Records: {total_records}")
    print(f"Total Romantic: {romantic_records}")
