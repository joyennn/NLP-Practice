import nltk
from nltk.parse.generate import generate

productions = [
    "ROOT -> WORD [1.0]",
    "WORD -> P1 [0.25]",
    "WORD -> P1 P2 [0.25]",
    "WORD -> P1 P2 P3 [0.25]",
    "WORD -> P1 P2 P3 P4 [0.25]",
    "P1 -> 'A' [1.0]",
    "P2 -> 'B' [0.5]",
    "P2 -> 'C' [0.5]",
    "P3 -> 'D' [0.3]",
    "P3 -> 'E' [0.3]",
    "P3 -> 'F' [0.4]",
    "P4 -> 'G' [0.9]",
    "P4 -> 'H' [0.1]",
]

grammarString = "\n".join(productions)
grammar = nltk.PCFG.fromstring(grammarString)
for sentence in generate(grammar, n=10, depth=5):
    palindrome = "".join(sentence).replace(" ","")
    print("문자열 : {}, 크기 : {}".format(palindrome, len(palindrome)))