import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP | NP VP Conj NP VP | NP VP Conj VP
VP -> V | V NP | V P NP | Adv V NP | V NP Adv | V Adv
NP -> NP P NP
NP -> N | Det N | Adj N | Det Adj N | Det Adj Adj Adj N | Det N Adv
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    def count_letters(s):
        return sum([1 for i in s if i.isalpha()])
    
    words = nltk.word_tokenize(sentence)
    words = [word.lower() for word in words]
    words = [word for word in words if count_letters(word) >= 1]
    return words
        

def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    # res = []
    # paths = []

    # def search(t, path):
    #     path = path.copy()
    #     path.append(t)
    #     if t.height() == 2:
    #         paths.append(path)
    #     else:
    #         sons = len(t)
    #         for i in range(sons):
    #             search(t[i], path)
    
    # search(tree, [])
    # print(len(paths))
    
    # for path in paths:
    #     if path[-1].label() == 'P':
    #         continue
    #     for chunk in reversed(path):
    #         if chunk.label() == 'NP':
    #             if chunk not in res:
    #                 res.append(chunk)
    #             break
    # return res

    np_chunks = []
    for subtree in tree.subtrees():
        if subtree.label() == 'NP':
            if all( ssub.label() != 'NP' for ssub in subtree.subtrees(lambda s: s != subtree)):
                np_chunks.append(subtree)
    return np_chunks



if __name__ == "__main__":
    main()
