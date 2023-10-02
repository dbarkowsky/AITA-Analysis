# Questions to ask
# 1. Are there frequent posters? Top 5? 10?
# 3. What are the totals of each flair?
# 4a. More likely to be the a-hole if edited?
# 4b. Or are people editing their posts if flaired a-holes?
# 6. More likely to be a-hole if high comments? -> shows engagement
# 7a. Are the a-holes more upvoted?
# 7b. Are they getting more votes in general?
# 8. Is it more likely to be the a-hole if the age range is large? (original question)
# 9. More likely to be a-hole if possibly romantic issue?
# 10. More likely to be a-hole based on num of participants? 2, 3, 4+
# 11. More likely to be a-hole based on age range? <18, 19-25, 26-40, 41+
# 12. More likely to be a-hole based on gender?
# 13. If only 2 participants, compare same vs different gender. For M and F.

# Questions that might be out...
# 2a. Most like to be the a-hole if posted at certain times of day? Morning, Afternoon, Evening, Night?
# 2b. Maybe can't tell that considering that we don't know their timezones.
# 5. More likely to be locked if a-hole?
# 5a. Too few locked posts to tell...
# 7c. Do a-holes get downvoted more (despite not the intent of the downvote)?
# 7d. Seems like downvotes don't get captured

import csv
from stats_bundler import StatsBundler
from refined_post import Refined_Post

stats = StatsBundler()

with open(f"./combined_posts.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    # Skip first line (header)
    reader.__next__()
    for x in reader:
        post = Refined_Post(x)
        # Count how many times they've posted
        stats.increment_poster(post.author)
        # Count number of each flair
        stats.increment_flair(post.flair)
        # Sum of score for each flair
        stats.append_score(post.flair, post.score)
        # Count genders per flair
        stats.increment_gender(post.flair, post.gender)
        # Count if same or different gender
        if post.same_gender == "True" or post.same_gender == "False":
            stats.increment_same_different_gender(post.flair, post.same_gender)
        # Count if edited (will be a number representing date, otherwise False string)
        if post.edited != "False":
            stats.increment_edited(post.flair)
        # Count that age
        if str(post.age).isdigit():
            stats.increment_age_chunk(post.flair, post.age)
            stats.increment_age(post.flair, post.age)
        # Count age ranges
        if str(post.age_range).isdigit():
            stats.increment_age_range(post.flair, post.age_range)
        # Count avg age brackets
        if str(post.identifier_age_avg).isdigit():
            stats.increment_avg_age(post.flair, post.identifier_age_avg)
        # Count if romantic
        if post.is_romantic == "True":
            stats.increment_romantic(post.flair)
        # Add number of comments to list
        stats.append_comments_count(post.flair, post.num_comments)

# Find top 10 (11 including deleted) posters
stats.top_10_posters()

# How many of each flair?
stats.flair_totals()
# Median and Mean of each flair
stats.flair_medians()
stats.flair_means()

# Mean of comments counts
stats.comments_means()

# Print A-hole count
stats.pretty_print_ahole_count()
