import re
import statistics


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
            self.age_range = None
            self.is_romantic = None
            self.num_identifiers = None
            self.age = None
            self.gender = None
            self.same_gender = None
            self.identifier_age_avg = None
        else:
            # If > 13, this row is already refined
            if len(row) > 13:
                self.author = row[0]
                self.created = row[1]
                self.flair = row[2]
                self.score = row[3]
                self.edited = row[4]
                self.locked = row[5]
                self.num_comments = row[6]
                self.num_awards = row[7]
                self.ups = row[8]
                self.downs = row[9]
                self.ratio = row[10]
                self.age_range = row[11]
                self.is_romantic = row[12]
                self.num_identifiers = row[13]
                self.age = row[14]
                self.gender = row[15]
                self.same_gender = row[16]
                self.identifier_age_avg = row[17]
            else:
                self.author = row[0]
                self.created = row[1]
                self.flair = row[2]
                self.title = row[3]
                self.text = row[4]
                self.score = row[5]
                self.edited = row[6]
                self.locked = row[7]
                self.num_comments = row[8]
                self.num_awards = row[9]
                self.ups = row[10]
                self.downs = row[11]
                self.ratio = row[12]
                self.age_range = self.getAgeRange()
                self.is_romantic = self.isRomantic()

                identifiers = self.getIdentifiers()
                self.num_identifiers = len(identifiers)
                self.same_gender = self.isSameGender()
                self.identifier_age_avg = self.getParticipantAgeAvg()

                ageGender = self.getPosterAgeGender()
                self.age = ageGender["age"]
                self.gender = ageGender["gender"]

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
            "gf",
            "bf",
        ]
        for word in romantic_words:
            if re.search(word, self.text, re.IGNORECASE):
                return True
        if re.search(r"SO", self.text):
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

    # Gets average age of detected participants
    def getParticipantAgeAvg(self):
        identifiers = self.getIdentifiers()
        # This only really matters if we have more than 1
        if len(identifiers) < 2:
            return "_"
        ages = []
        for participant in identifiers:
            age = re.search(r"\d{2}", participant)
            ages.append(int(age.group(0)))

        return statistics.mean(ages)

    # Sees if the gender of all participants is the same
    def isSameGender(self):
        identifiers = self.getIdentifiers()
        # This only really matters if we have more than 1
        if len(identifiers) < 2:
            return "_"
        for index, participant in enumerate(identifiers, start=1):
            gender = re.search(r"[MF]", participant, re.IGNORECASE)
            if not re.match(
                f"{gender.group(0)}", identifiers[index - 1], re.IGNORECASE
            ):
                return False
        return True

    # Tries to determine if the poster is male (M) or female (F)
    # Also tries to get their age
    def getPosterAgeGender(self) -> dict:
        result = dict()
        try:
            possibleIdentifier = re.search(
                r"(myself|I|me)\s*[\(\[\{](\d{2}[MF]|[MF]\d{2})",
                self.text,
                re.IGNORECASE,
            )
            justAge = re.search(r"\d{2}", possibleIdentifier.group(2))
            justGender = re.search(r"[mf]", possibleIdentifier.group(2), re.IGNORECASE)
            result["age"] = justAge.group(0)
            result["gender"] = str(justGender.group(0)).upper()
        except:
            result["age"] = "_"
            result["gender"] = "_"
        finally:
            return result

    # Prints out a row with all data
    def getRow(self) -> str:
        return (
            ",".join(
                [
                    self.author,
                    self.created,
                    self.flair,
                    self.score,
                    self.edited,
                    self.locked,
                    self.num_comments,
                    self.num_awards,
                    self.ups,
                    self.downs,
                    self.ratio,
                    str(self.age_range),
                    str(self.is_romantic),
                    str(self.num_identifiers),
                    str(self.age),
                    self.gender,
                    str(self.same_gender),
                    str(self.identifier_age_avg),
                ]
            )
            + "\n"
        )

    @staticmethod
    def getHeader() -> str:
        return (
            ",".join(
                [
                    "Author",
                    "Created",
                    "Flair",
                    "Score",
                    "Edited",
                    "Locked",
                    "NumComments",
                    "NumAwards",
                    "Ups",
                    "Downs",
                    "Ratio",
                    "AgeRange",
                    "IsRomantic",
                    "NumParticipants",
                    "Age",
                    "Gender",
                    "SameGender",
                    "ParticipantAvgAge",
                ]
            )
            + "\n"
        )
