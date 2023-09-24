import statistics
from collections import defaultdict


class StatsBundler:
    def __init__(self):
        self.frequent_posters = dict()
        self.flair_count = dict()
        self.flair_score_lists = defaultdict(list)

    # Modifications
    def increment_poster(self, poster):
        self.frequent_posters[poster] = self.frequent_posters.get(poster, 0) + 1

    def increment_flair(self, flair):
        self.flair_count[flair] = self.flair_count.get(flair, 0) + 1

    def append_score(self, flair, score):
        self.flair_score_lists[flair].append(int(score))

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
        for key in self.flair_count.keys():
            print(f"{key}: {self.flair_count[key]}")
        print()

    def flair_medians(self):
        print("Median Score per Flair:")
        for flair in self.flair_score_lists.keys():
            print(f"{flair}: {statistics.median(self.flair_score_lists[flair])}")
        print()

    def flair_means(self):
        print("Mean Score per Flair:")
        for flair in self.flair_score_lists.keys():
            print(
                f"{flair}: {round(statistics.mean(self.flair_score_lists[flair]), 2)}"
            )
        print()
