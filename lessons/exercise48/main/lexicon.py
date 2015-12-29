class lexicon(object):
    def __init__(self):
        self.words = []

    def __isDirection__(self, word):
        """
            Check if the given word is a direction. Return True in case it is together with the tuple('direction', value)
        :param word:
        :returns tuple('direction', value) as first parameter followed by the second parameter boolean True/False
        based on the word type.
        """
        self.directions = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
        for direction in self.directions:
            if direction == word:
                return ('direction', word), True
        return None, False

    def __isVerb__(self, word):
        """
            Check if the given word is a verb. Return True in case it is together with the tuple('verb', value)
        :param word:
        :returns tuple('verb', value) as first parameter followed by the second parameter boolean True/False
        based on the word type.
        """
        self.verbs = ('go', 'stop', 'kill', 'eat')
        for verb in self.verbs:
            if verb == word:
                return ('verb', word), True
        return None, False

    def __isStopWord__(self, word):
        """
            Check if the given word is a stop word. Return True in case it is together with the tuple('stop', value)
        :param word:
        :returns tuple('stop', value) as first parameter followed by the second parameter boolean True/False
        based on the word type.
        """
        self.stopWords = ('the', 'in', 'of', 'from', 'at', 'it')
        for stopWord in self.stopWords:
            if stopWord == word:
                return ('stop', word), True
        return None, False

    def __isNoun__(self, word):
        """
            Check if the given word is a noun. Return True in case it is together with the tuple('noun', value)
        :param word:
        :returns tuple('noun', value) as first parameter followed by the second parameter boolean True/False
        based on the word type.
        """
        self.nouns = ('door', 'bear', 'princess', 'cabinet')
        for noun in self.nouns:
            if noun == word:
                return ('noun', word), True
        return None, False

    def __isNumber__(self, word):
        """
            Check if the given word is a number. Return True in case it is together with the tuple('number', value)
        :param word:
        :returns tuple('number', value) as first parameter followed by the second parameter boolean True/False
        based on the word type.
        """
        try:
            return ('number', int(word)), True
        except ValueError:
            return None, False

    def __check_word__(self, word):
        """
            Check if the word is a direction, verb, stop word, noun or number and return the correct tuple (Type, Value)
        :param word:
        :return:
        """
        self.directionValue, self.isDirection = self.__isDirection__(word.lower())
        self.verbValue, self.isVerb = self.__isVerb__(word.lower())
        self.stopValue, self.isStop = self.__isStopWord__(word.lower())
        self.nounValue, self.isNoun = self.__isNoun__(word.lower())
        self.numberValue, self.isNumber = self.__isNumber__(word.lower())

        if self.isDirection:
            return self.directionValue
        elif self.isVerb:
            return self.verbValue
        elif self.isStop:
            return self.stopValue
        elif self.isNoun:
            return self.nounValue
        elif self.isNumber:
            return self.numberValue
        else:
            return ('error', word)

    def scan(self, message):
        """
            Split the given message into words. Return an array of tuples with (TYPE, WORD)
        :param message:
        :return tuple [(TYPE, WORD),(TYPE, WORD)]:
        """
        words = message.split(" ")
        for word in words:
            self.words.append(self.__check_word__(word))
        return self.words

def scan(message):
    """
        function that uses object lexicon
    :param message:
    :return:
    """
    analyze = lexicon()
    return analyze.scan(message=message)

# ----------------------- option 2 with no classes ---------------------------------------------
def isNumber(word):
    """
        function that checks if a word is a number or not
    :param word:
    :return:
    """
    try:
        int(word)
        return True
    except ValueError:
        return False

def getType(word):
    """
        Function that checks the type of a word based on a dictionary
    :param word:
    :return:
    """
    rules = {
        'direction': ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'],
        'verb': ['go', 'stop', 'kill', 'eat'],
        'stop': ['the', 'in', 'of', 'from', 'at', 'it'],
        'noun': ['door', 'bear', 'princess', 'cabinet']
    }
    if isNumber(word):
        return 'number'

    for rule, rule_list in rules.items():
        if word in rule_list:
            return rule

    return 'error'

def scan_dictionary_option(message):
    """
        A second version of scan function that uses a dictionary to determine the type
    :param message:
    :return:
    """
    returnValue = []

    words = message.split(' ')
    for word in words:
        type = getType(word.lower())
        returnValue.append((type, word))

    return returnValue