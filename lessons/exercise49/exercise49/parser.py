class ParserError(Exception):
    pass

class Sentence(object):
    def __init__(self, subject, verb, obj):
        """
            The method will receive the a tuple (TYPE, WORD) as input for each parameter
        :param subject:
        :param verb:
        :param obj:
        :return:
        """
        self.subject = subject[1]
        self.verb = verb[1]
        self.obj = obj[1]


def peek(word_list):
    """
        Take a look on the next word and return what type of word it is
    :param word_list:
    :return:
    """
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


def match(word_list, expecting):
    """
        Consume a word, it will confirm that the expected word is the right type, take it from the list and return
    the word
    :param word_list:
    :param expecting:
    :return:
    """
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    """
        A way to skip words that are not useful like stop words (type), "the", "and", "a"
    :param word_list:
    :param word_type:
    :return:
    """
    while peek(word_list) == word_type:
        match(word_list,word_type)

def parse_verb(word_list):
    """
        Skip any stop words, then peek ahead to make sure the next word is a "verb" type. If it's not then raise the
    ParserError to say why. If it is a "verb" then match it, which takes it off the list
    :param word_list:
    :return:
    """
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError('Expected a verb next')


def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")


def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")


def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)


x = parse_sentence([('verb', 'run'), ('direction', 'north')])
print(x.subject)
print(x.verb)
print(x.obj)

x = parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])
print(x.subject)
print(x.verb)
print(x.obj)