import nltk

def learnDefaultTagger(simpleSentence):
    wordsInSentence = nltk.word_tokenize(simpleSentence)
    tagger = nltk.DefaultTagger("NN")
    posEnabledTags = tagger.tag(wordsInSentence)
    print(posEnabledTags)

def learnRETageer(simpleSentence):
    customPatterns = [
        (r'.*ing$', 'ADJECTIVE'),
        (r'.*ly$', 'ADVERB'),
        (r'.*ion$', 'NOUN'),
        (r'(.*ate|.*en|is)$', 'VERB'),
        (r'^an$', 'INDEFINITE-ARTICLE'),
        (r'^(with|on|at)$', 'PREPOSITION'),
        (r'^\-?[0-9]+(\.[0-9]+)$', 'NUMBER'),
        (r'.*$', None),
    ]
    tagger = nltk.RegexpTagger(customPatterns)
    wordsInSentence = nltk.word_tokenize(simpleSentence)
    posEnabledTags = tagger.tag(wordsInSentence)
    print(posEnabledTags)

def learnLookupTagger(simpleSentence):
    mapping = {
        '.': '.', 'place': 'NN', 'on': 'IN',
        'earth': 'NN', 'Rey': 'NNP', 'is':'VBZ',
        'an': 'DT', 'amazing': 'JJ'
    }
    tagger = nltk.UnigramTagger(model=mapping)
    wordsInSentence = nltk.word_tokenize(simpleSentence)
    posEnabledTags = tagger.tag(wordsInSentence)
    print(posEnabledTags)




testSentence = "Rey is an amazing place on earth. I have visited Rey 10 times."
learnDefaultTagger(testSentence)
learnRETageer(testSentence)
learnLookupTagger(testSentence)