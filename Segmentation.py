import nltk

def featureExtractor(words, i):
    return ({'current-word': words[i], 'next-is-upper':
             words[i+1][0].isupper()}, words[i+1][0].isupper())

def getFeaturesets(sentence):
    words = nltk.word_tokenize(sentence)
    featuresets = [featureExtractor(words, i) for i in range(1, len(words) - 1) if words[i] == '.']
    return featuresets

def segmentTextAndPrintSentences(data):
    words = nltk.word_tokenize(data)
    for i in range(0, len(words) - 1):
        if words[i] == '.':
            if classifier.classify(featureExtractor(words, i)[0]) == True:
                print(".")
            else:
                print(words[i], end='')
        else:
            print("{} ".format(words[i]), end='')
    print(words[-1])

traindata = "India, officially the Republic of India (Hindi: Bhārat Gaṇarājya),[24] is a country in South Asia. It is the seventh-largest country by area, the second-most populous country, and the most populous democracy in the world. Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west;[f] China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives; its Andaman and Nicobar Islands share a maritime border with Thailand, Myanmar and Indonesia."
testdata = "India has been a federal republic since 1950, governed in a democratic parliamentary system. It is a pluralistic, multilingual and multi-ethnic society. India's population grew from 361 million in 1951 to 1.211 billion in 2011.[54] During the same time, its nominal per capita income increased from US$64 annually to US$1,498, and its literacy rate from 16.6% to 74%. From being a comparatively destitute country in 1951,[55] India has become a fast-growing major economy and a hub for information technology services, with an expanding middle class.[56] It has a space programme which includes several planned or completed extraterrestrial missions. Indian movies, music, and spiritual teachings play an increasing role in global culture.[57] India has substantially reduced its rate of poverty, though at the cost of increasing economic inequality.[58] India is a nuclear-weapon state, which ranks high in military expenditure. It has disputes over Kashmir with its neighbours, Pakistan and China, unresolved since the mid-20th century.[59] Among the socio-economic challenges India faces are gender inequality, child malnutrition,[60] and rising levels of air pollution.[61] India's land is megadiverse, with four biodiversity hotspots.[62] Its forest cover comprises 21.7% of its area.[63] India's wildlife, which has traditionally been viewed with tolerance in India's culture,[64] is supported among these forests, and elsewhere, in protected habitats."

traindataset = getFeaturesets(traindata)
classifier = nltk.NaiveBayesClassifier.train(traindataset)
segmentTextAndPrintSentences(testdata)
