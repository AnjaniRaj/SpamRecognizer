import os
import cPickle
import pickle

from parse_reviews import parseText
negative=open("deceptive.txt","r")
positive=open("truthful.txt",'r')
word_data=[]
label_data=[]
false=[]
true=[]

for s, review_path in [("spam",negative),("notspam",positive)]:
    for path in review_path:
        path = os.path.join('..',path[:-1])
        review = open(path,"r")
        review_parsed = parseText(review)
        word_data.append(review_parsed)
        if s == "spam":
            label_data.append(1)
            false.append(review_parsed)
        else:
            label_data.append(0)
            true.append(review_parsed)
        review.close()

positive.close()
negative.close()

pickle.dump(true,open("true_reviews.pkl","w"))
pickle.dump(false,open("false_reviews.pkl","w"))
pickle.dump(word_data,open("reviews_word_data.pkl","w"))
pickle.dump(label_data,open("labels_of_reviews.pkl","w"))

#from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.feature_extraction import text
#stopwords= text.ENGLISH_STOP_WORDS.union()
#vectorizer = TfidfVectorizer(sublinear_tf=True,stop_words='english')
#vectorizer.fit_transform(word_data)
#vocab_list = vectorizer.get_feature_names()
#print len(vocab_list)