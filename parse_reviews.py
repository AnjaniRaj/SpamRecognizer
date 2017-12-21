from nltk.stem.snowball import SnowballStemmer
import string

def parseText(f):

    f.seek(0)
    all_text=f.read()
    content = all_text.split()
    words=""

    if len(content)>1:
        wordslist = [''.join(c for c in s if c not in string.punctuation) for s in content]
       # wordslist = text_string.split()
        words=""
        stemmer = SnowballStemmer("english")
        for word in wordslist:
            words=words+" "+stemmer.stem(word)
        words = words.lstrip()


    return words
