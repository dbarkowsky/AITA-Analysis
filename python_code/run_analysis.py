# Questions to ask
# 1. Are there frequent posters? Top 5? 10?
# 2a. Most like to be the a-hole if posted at certain times of day? Morning, Afternoon, Evening, Night?
# 2b. Maybe can't tell that considering that we don't know their timezones.
# 3. What are the totals of each flair?
# 4a. More likely to be the a-hole if edited?
# 4b. Or are people editing their posts if flaired a-holes?
# 5. More likely to be locked if a-hole?
# 6. More likely to be a-hole if high comments? -> shows engagement
# 7a. Are the a-holes more upvoted?
# 7b. Are they getting more votes in general?
# 7c. Do a-holes get downvoted more (despite not the intent of the downvote)?
# 8. Is it more likely to be the a-hole if the age range is large? (original question)
# 9. More likely to be a-hole if possibly romantic issue?
# 10. More likely to be a-hole based on num of participants? 2, 3, 4+
# 11. More likely to be a-hole based on age range? <18, 19-25, 26-40, 41+
# 12. More likely to be a-hole based on gender?
# 13. If only 2 participants, compare same vs different gender. For M and F.

import csv
from stats_bundler import StatsBundler


class Combined_Row:
    def __init__(self, row):
        self.author = row[0]
        self.created = row[1]
        self.edited = row[4]
        self.flair = row[2]
        self.locked = row[5]
        self.num_comments = row[6]
        self.score = row[3]
        self.num_awards = row[7]
        self.ups = row[8]
        self.downs = row[9]
        self.ratio = row[10]
        self.age_range = row[11]
        self.is_romantic = row[12]
        self.num_identifiers = row[13]
        self.age = row[14]
        self.gender = row[15]


stats = StatsBundler()

with open(f"./combined_posts.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    # Skip first line (header)
    reader.__next__()
    for x in reader:
        row = Combined_Row(x)
        # Count how many times they've posted
        stats.increment_poster(row.author)
        # Count number of each flair
        stats.increment_flair(row.flair)
        # Sum of score for each flair
        stats.append_score(row.flair, row.score)

    # Find top 10 (11 including deleted) posters
    stats.top_10_posters()

    # How many of each flair?
    stats.flair_totals()
    # Median and Mean of each flair
    stats.flair_medians()
    stats.flair_means()