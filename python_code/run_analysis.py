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


# Make sure all age dicts are sorted by key's numerical value
# Takes (key, value) pair and returns key as int
def sortAsInt(keyValuePair):
    return int(keyValuePair[0])


for flair in stats.ahole_count.keys():
    stats.ahole_count[flair]["age"] = dict(
        sorted(stats.ahole_count[flair]["age"].items(), key=sortAsInt)
    )
    stats.ahole_count[flair]["avg_age"] = dict(
        sorted(stats.ahole_count[flair]["avg_age"].items(), key=sortAsInt)
    )
    stats.ahole_count[flair]["age_range"] = dict(
        sorted(stats.ahole_count[flair]["age_range"].items(), key=sortAsInt)
    )
    stats.ahole_count[flair]["k_question"] = dict(
        sorted(stats.ahole_count[flair]["k_question"].items(), key=sortAsInt)
    )


# How many of each flair?
stats.flair_totals()
# Median and Mean of each flair
stats.flair_medians()
flair_means = stats.flair_means()

# Mean of comments counts
comment_means = stats.comments_means()

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


def dictKeyValueToTuple(dict):
    result = []
    for key in dict.keys():
        result.append((int(key), float(dict[key])))
    return result


def filterKeysLessThan(dict, value):
    return {k: v for k, v in dict.items() if int(k) < value}


# Age Gap/Range Per Flair
age_cutoff = 50
age_difference_data = []
for flair in stats.ahole_count.keys():
    age_difference_data.append(
        dictValuesToTuple(
            filterKeysLessThan(stats.ahole_count[flair]["age_range"], age_cutoff)
        )
    )
ChartBuilder.pyramid(
    chart_title="Count of Age Difference per Flair",
    series_data=age_difference_data,
    series_titles=list(stats.ahole_count.keys()),
    x_labels=map(str, range(age_cutoff + 1)),
    y_title="Age Difference (Years)",
)

# Scatterplot to show likelihood of asshole based on age gap
# Seemingly consistent
percentage_age_difference_data = []
for flair in stats.ahole_count.keys():
    percentage_age_difference_data.append(
        dictKeyValueToTuple(stats.age_object_to_percentages("age_range")[flair])
    )
ChartBuilder.scatterplot(
    chart_title="Likelihood of Asshole by Age Gap",
    series_data=percentage_age_difference_data,
    series_titles=["Not the A-hole", "Asshole"],
    x_title="Age Gap between Poster and Other Participant",
)

# Bar chart for Age Bracket/Range per Flair
age_range_data = []
for flair in stats.ahole_count.keys():
    age_range_data.append(dictValuesToTuple(stats.ahole_count[flair]["age_chunk"]))
ChartBuilder.bar(
    chart_title="Count of Posts per Age Bracket per Flair",
    series_titles=list(stats.ahole_count.keys()),
    series_data=age_range_data,
    x_labels=list(stats.ahole_count["Asshole"]["age_chunk"].keys()),
)
# Stacked Bar for Ratio of the Same thing
normalized_age_range_data = []
for flair in stats.ahole_count.keys():
    normalized_age_range_data.append(
        dictValuesToTuple(stats.age_object_to_percentages("age_chunk")[flair])
    )
ChartBuilder.stacked_bar(
    chart_title="Ratio of Posts per Age Bracket per Flair",
    series_titles=list(stats.ahole_count.keys()),
    series_data=normalized_age_range_data,
    x_labels=list(stats.ahole_count["Asshole"]["age_chunk"].keys()),
)

# Scatterplot for K Question
k_question_data = []
for flair in stats.ahole_count.keys():
    k_question_data.append(
        dictKeyValueToTuple(stats.age_object_to_percentages("k_question")[flair])
    )
ChartBuilder.scatterplot(
    chart_title="Likelihood of Asshole if Romantic and Older by Age Difference",
    series_data=k_question_data,
    series_titles=["Not the A-hole", "Asshole"],
    x_title="Age Difference Between Participants",
)

# Bar for Age of Posters
age_cutoff = 60
age_data = []
for flair in stats.ahole_count.keys():
    age_data.append(
        dictValuesToTuple(
            filterKeysLessThan(stats.ahole_count[flair]["age"], age_cutoff)
        )
    )
ChartBuilder.stacked_bar(
    chart_title="Count of Age of Posters",
    series_data=age_data,
    series_titles=list(stats.ahole_count.keys()),
    x_labels=map(str, range(13, age_cutoff + 1)),
)

# Scatterplot - Likelihood by Age of Poster
percentage_age_data = []
for flair in stats.ahole_count.keys():
    percentage_age_data.append(
        dictKeyValueToTuple(stats.age_object_to_percentages("age")[flair])
    )
ChartBuilder.scatterplot(
    chart_title="Likelihood of Asshole by Age",
    series_data=percentage_age_data,
    series_titles=["Not the A-hole", "Asshole"],
    x_title="Age of Poster",
)

# Stacked Bar for Romantic
romantic_data = []
for flair in stats.ahole_count.keys():
    romantic_data.append(
        (
            stats.ahole_count[flair]["romantic"],
            (stats.ahole_count[flair]["count"] - stats.ahole_count[flair]["romantic"]),
        )
    )
ChartBuilder.bar(
    chart_title="Distribution of Flairs by Romantic Status",
    series_titles=list(stats.ahole_count.keys()),
    series_data=romantic_data,
    x_labels=["Romantic", "Not Romantic"],
)

# Stacked Bar for Edited
edited_data = []
for flair in stats.ahole_count.keys():
    edited_data.append(
        (
            stats.ahole_count[flair]["edited"],
            (stats.ahole_count[flair]["count"] - stats.ahole_count[flair]["edited"]),
        )
    )
ChartBuilder.bar(
    chart_title="Distribution of Flairs by Edited Status",
    series_titles=list(stats.ahole_count.keys()),
    series_data=edited_data,
    x_labels=["Edited", "Not Edited"],
)

# Top 10 posters -> horizontal bar
# Find top 10 (11 including deleted) posters
top_10 = stats.top_10_posters()
top_10_data = []
for user in top_10:
    top_10_data.append(stats.frequent_posters[user])
ChartBuilder.horizontal_bar(
    chart_title="Top 10 Most Frequent Posters",
    series_titles=top_10,
    series_data=top_10_data,
)


# Bar Chart showing gender distribution per flair
gender_data = []
for flair in stats.ahole_count.keys():
    gender_data.append(dictValuesToTuple(stats.ahole_count[flair]["gender"]))
ChartBuilder.bar(
    chart_title="Gender Trends by Count",
    series_data=gender_data,
    series_titles=list(stats.ahole_count.keys()),
    x_labels=["Male", "Female", "Same Gender", "Different Gender"],
)
# Stacked Bar for Ratio of the Same thing
normalized_gender_data = []
for flair in stats.ahole_count.keys():
    normalized_gender_data.append(
        [
            stats.ahole_count[flair]["gender"]["M"],
            stats.ahole_count[flair]["gender"]["F"],
            stats.ahole_count[flair]["gender"]["same"],
            stats.ahole_count[flair]["gender"]["different"],
        ]
    )
ChartBuilder.stacked_bar(
    chart_title="Gender Trends by Ratio of Posts",
    series_titles=list(stats.ahole_count.keys()),
    series_data=normalized_gender_data,
    x_labels=["Male", "Female", "Same Gender", "Different Gender"],
)
