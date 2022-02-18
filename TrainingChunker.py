import nltk
from nltk.corpus import conll2000
from nltk.corpus import treebank_chunk

def mySimpleChunker():
    grammar = 'NP: {<NNP>+}'
    return nltk.RegexpParser(grammar)

def test_nothing(data):
    cp = nltk.RegexpParser("")
    print(cp.evaluate(data))

def test_mysimplechunker(data):
    schunker = mySimpleChunker()
    print(schunker.evaluate(data))

datasets = [conll2000.chunked_sents('test.txt', chunk_types=['NP']),
            treebank_chunk.chunked_sents()
            ]

print(datasets)

for dataset in datasets:
    test_nothing(dataset[:50])
    test_mysimplechunker(dataset[:50])

