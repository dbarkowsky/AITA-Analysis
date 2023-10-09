import csv
from stats_bundler import StatsBundler
from refined_post import Refined_Post
from chart_builder import ChartBuilder

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
        # K Question
        if post.is_romantic == "True" and post.is_oldest == "True":
            stats.increment_k_question(post.flair, post.age_range)
        # Add number of comments to list
        stats.append_comments_count(post.flair, post.num_comments)

# Find top 10 (11 including deleted) posters
stats.top_10_posters()

# How many of each flair?
stats.flair_totals()
# Median and Mean of each flair
stats.flair_medians()
flair_means = stats.flair_means()

# Mean of comments counts
comment_means = stats.comments_means()

# Print A-hole count
# stats.pretty_print_ahole_count()
stats.age_object_to_percentages("k_question")

# Chart Building

# Count posts per Flair
ChartBuilder.bar(
    chart_title="Count of Post by Flair",
    series_titles=list(stats.ahole_count.keys()),
    series_data=[
        stats.ahole_count["Not the A-hole"]["count"],
        stats.ahole_count["Asshole"]["count"],
        stats.ahole_count["No A-holes here"]["count"],
        stats.ahole_count["Everyone Sucks"]["count"],
    ],
)

# Average Score per Flair
ChartBuilder.bar(
    chart_title="Average Post Score per Flair",
    series_titles=list(stats.ahole_count.keys()),
    series_data=[
        flair_means["Not the A-hole"],
        flair_means["Asshole"],
        flair_means["No A-holes here"],
        flair_means["Everyone Sucks"],
    ],
)

# Average Number of Comments per Flair
ChartBuilder.bar(
    chart_title="Average Number of Comments per Flair",
    series_titles=list(stats.ahole_count.keys()),
    series_data=[
        comment_means["Not the A-hole"],
        comment_means["Asshole"],
        comment_means["No A-holes here"],
        comment_means["Everyone Sucks"],
    ],
)


def dictValuesToTuple(dict):
    return [(val) for val in dict.values()]


def filterKeysLessThan(dict, value):
    return {k: v for k, v in dict.items() if int(k) <= value}


# Age Range Per Flair
age_cutoff = 50
age_range_data = [
    dictValuesToTuple(
        filterKeysLessThan(stats.ahole_count["Not the A-hole"]["age_range"], age_cutoff)
    ),
    dictValuesToTuple(
        filterKeysLessThan(stats.ahole_count["Asshole"]["age_range"], age_cutoff)
    ),
    dictValuesToTuple(
        filterKeysLessThan(
            stats.ahole_count["No A-holes here"]["age_range"], age_cutoff
        )
    ),
    dictValuesToTuple(
        filterKeysLessThan(stats.ahole_count["Everyone Sucks"]["age_range"], age_cutoff)
    ),
]
ChartBuilder.pyramid(
    chart_title="Count of Age Range per Flair",
    series_data=age_range_data,
    series_titles=list(stats.ahole_count.keys()),
    x_labels=map(str, range(age_cutoff + 1)),
    y_title="Age Difference (Years)",
)
