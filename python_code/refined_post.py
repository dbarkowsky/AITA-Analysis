import re

class Refined_Post:
    def __init__(self) -> None:
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

    # Returns true if a word suggesting a romantic relationship is found
    def isRomantic(self) -> bool:
        romantic_words = ['partner', 'spouse', 'girlfriend', 'boyfriend', 'husband', 'wife', 'significant other', 'so']
        for word in romantic_words:
            if re.search(word, self.text, re.IGNORECASE):
                return True
        return False
    
    # Gets all the instances of age and gender
    def getIdentifiers(self) -> [str]:
        return re.findall(r'\d{2}[MF]|[MF]\d{2}', self.text, re.IGNORECASE)
        
    # Gets the age range between all detected participants
    def getAgeRange(self) -> int:
        identifiers = self.getIdentifiers()
        ages = [] # a list of just ages
        for identifier in identifiers:
            ages.append(int(re.findall(r'\d{2}', identifier)[0]))
        return max(ages) - min(ages)
