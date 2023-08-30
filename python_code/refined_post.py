import re


class Refined_Post:
    def __init__(self, row=None):
        if row == None:
            self.author = None
            self.created = None
            self.downs = None
            self.edited = None
            self.flair = None
            self.locked = None
            self.num_comments = None
            self.score = None
            self.text = None
            self.title = None
            self.num_awards = None
            self.ups = None
            self.ratio = None
        else:
            self.author = row[0]
            self.created = row[1]
            self.flair = row[2]
            self.title = row[3]
            self.text = row[4]
            self.score = row[4]
            self.edited = row[6]
            self.locked = row[7]
            self.num_comments = row[8]
            self.num_awards = row[9]
            self.ups = row[10]
            self.downs = row[11]
            self.ratio = row[12]

    # Returns true if a word suggesting a romantic relationship is found
    def isRomantic(self) -> bool:
        romantic_words = [
            "partner",
            "spouse",
            "girlfriend",
            "boyfriend",
            "husband",
            "wife",
            "significant other",
            "so",
            "gf",
            "bf",
        ]
        for word in romantic_words:
            if re.search(word, self.text, re.IGNORECASE):
                return True
        return False

    # Gets all the instances of age and gender
    def getIdentifiers(self) -> [str]:
        return re.findall(r"\d{2}[MF]|[MF]\d{2}", self.text, re.IGNORECASE)

    # Gets the age range between all detected participants
    def getAgeRange(self) -> int:
        identifiers = self.getIdentifiers()
        ages = []  # a list of just ages
        for identifier in identifiers:
            ages.append(int(re.findall(r"\d{2}", identifier)[0]))
        if len(ages) > 1:
            return max(ages) - min(ages)
        else:
            return "_"
