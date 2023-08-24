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

    def isRomantic(self) -> bool:
        romantic_words = ['partner', 'spouse', 'girlfriend', 'boyfriend', 'husband', 'wife', 'significant other', 'so']
        for word in romantic_words:
            if re.search(word, self.text, re.IGNORECASE):
                return True
        return False
    
    def getIdentifiers(self) -> [str]:
        return re.findall(r'\d{2}[MF]|[MF]\d{2}', self.text, re.IGNORECASE)
        
