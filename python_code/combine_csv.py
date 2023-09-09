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
                ageGender = post.getPosterAgeGender()
                if isRomantic:
                    romantic_records += 1
                posts.append(
                    f"{post.author},{post.created},{post.flair},{post.score},{post.edited},{post.locked},{post.num_comments},{post.num_awards},{post.ups},{post.downs},{post.ratio},{post.getAgeRange()},{isRomantic},{len(post.getIdentifiers())},{ageGender['age']},{ageGender['gender']}\n"
                )
    return posts


timestamp = datetime.now()
total_records = 0
romantic_records = 0

with open(f"./combined_posts.csv", "w", encoding="utf-8") as file:
    file.write(
        "Author,Created,Flair,Score,Edited,Locked,NumComments,NumAwards,Ups,Downs,Ratio,Range,IsRomantic,NumParticipants,Age,Gender\n"
    )
with open(f"./combined_posts.csv", "a", encoding="utf-8") as file:
    post_list = get_all_posts()
    for post in post_list:
        file.write(post)
    print("Done combining posts.")
    print(f"Total Records: {total_records}")
    print(f"Total Romantic: {romantic_records}")
