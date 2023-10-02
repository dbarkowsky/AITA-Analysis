import statistics
from collections import defaultdict
import copy
import json


class StatsBundler:
    def __init__(self):
        default_dict = {
            "count": 0,
            "score_list": [],
            "gender": {"M": 0, "F": 0, "same": 0, "different": 0},
            "edited": 0,
            "age_chunk": {"<19": 0, "19-25": 0, "26-35": 0, "36-45": 0, ">45": 0},
            "age": {},
            "age_range": {},  # difference between youngest and oldest
            "avg_age": {},  # count avg age between all participants in one post
            "romantic": 0,
            "num_comments_list": [],
        }
        self.frequent_posters = dict()
        self.ahole_count = {
            "Not the A-hole": copy.deepcopy(default_dict),
            "Asshole": copy.deepcopy(default_dict),
            "No A-holes here": copy.deepcopy(default_dict),
            "Everyone Sucks": copy.deepcopy(default_dict),
        }

    # Modifications
    def increment_poster(self, poster):
        self.frequent_posters[poster] = self.frequent_posters.get(poster, 0) + 1

    def increment_flair(self, flair):
        self.ahole_count[flair]["count"] += 1

    def append_score(self, flair, score):
        self.ahole_count[flair]["score_list"].append(int(score))

    def increment_gender(self, flair, gender):
        if ["M", "F"].__contains__(gender):
            self.ahole_count[flair]["gender"][gender] += 1

    def increment_same_different_gender(self, flair, isSame):
        if isSame == "True":
            self.ahole_count[flair]["gender"]["same"] += 1
        else:
            self.ahole_count[flair]["gender"]["different"] += 1

    def increment_edited(self, flair):
        self.ahole_count[flair]["edited"] += 1

    def increment_age_chunk(self, flair, age):
        int_age = int(age)
        match int_age:
            case _ if int_age < 19:
                self.ahole_count[flair]["age_chunk"]["<19"] += 1
            case _ if int_age >= 19 and int_age <= 25:
                self.ahole_count[flair]["age_chunk"]["19-25"] += 1
            case _ if int_age >= 26 and int_age <= 35:
                self.ahole_count[flair]["age_chunk"]["26-35"] += 1
            case _ if int_age >= 36 and int_age <= 45:
                self.ahole_count[flair]["age_chunk"]["36-45"] += 1
            case _ if int_age >= 45:
                self.ahole_count[flair]["age_chunk"][">45"] += 1

    def increment_age(self, flair, age):
        self.ahole_count[flair]["age"][str(age)] = (
            self.ahole_count[flair]["age"].get(str(age), 0) + 1
        )

    def increment_age_range(self, flair, range):
        self.ahole_count[flair]["age_range"][str(range)] = (
            self.ahole_count[flair]["age_range"].get(str(range), 0) + 1
        )

    def increment_avg_age(self, flair, age):
        self.ahole_count[flair]["avg_age"][str(age)] = (
            self.ahole_count[flair]["avg_age"].get(str(age), 0) + 1
        )

    def increment_romantic(self, flair):
        self.ahole_count[flair]["romantic"] += 1

    def append_comments_count(self, flair, comments_count):
        self.ahole_count[flair]["num_comments_list"].append(int(comments_count))

    # Calculations
    def top_10_posters(self):
        top_10 = sorted(
            self.frequent_posters, key=self.frequent_posters.get, reverse=True
        )[:11]
        top_10.pop(0)  # Removing "[deleted]" users
        print("Top 10 Posters by Amount:")
        for poster in top_10:
            print(f"{poster}: {self.frequent_posters[poster]}")
        print()

    def flair_totals(self):
        print("Total of each Flair:")
        for flair in self.ahole_count.keys():
            print(f"{flair}: {self.ahole_count[flair]['count']}")
        print()

    def flair_medians(self):
        print("Median Score per Flair:")
        for flair in self.ahole_count.keys():
            print(
                f"{flair}: {statistics.median(self.ahole_count[flair]['score_list'])}"
            )
        print()

    def flair_means(self):
        print("Mean Score per Flair:")
        for flair in self.ahole_count.keys():
            print(
                f"{flair}: {round(statistics.mean(self.ahole_count[flair]['score_list']), 2)}"
            )
        print()

    def comments_means(self):
        print("Mean Number of Comments per Flair:")
        for flair in self.ahole_count.keys():
            print(
                f"{flair}: {round(statistics.mean(self.ahole_count[flair]['num_comments_list']), 2)}"
            )
        print()

    # Utilities
    def pretty_print_ahole_count(self):
        print(json.dumps(self.ahole_count, sort_keys=True, indent=2))
