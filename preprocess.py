import pickle
import cPickle
import numpy

from sklearn import cross_validation
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif


def preprocess(word_file="C:/Users/Pc/Desktop/op_spam_v1.4/SpamRecognizer/reviews_word_data.pkl",
               label_file="C:/Users/Pc/Desktop/op_spam_v1.4/SpamRecognizer/labels_of_reviews.pkl"):
    labels_file_handler = open(label_file, "r")
    labels = pickle.load(labels_file_handler)
    labels_file_handler.close()

    words_file_handler = open(word_file, "r")
    word_data = pickle.load(words_file_handler)
    words_file_handler.close()

    features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, labels,
                                                                                                 test_size=0.25,
                                                                                                 random_state=42)
    vectorizer = TfidfVectorizer(sublinear_tf=False,stop_words='english',ngram_range=(1,2))
    features_train_transformed = vectorizer.fit_transform(features_train)
    features_test_transformed = vectorizer.transform(features_test)

    selector = SelectPercentile(f_classif, percentile=1)
    selector.fit(features_train_transformed, labels_train)
    features_train_transformed = selector.transform(features_train_transformed).toarray()
    features_test_transformed = selector.transform(features_test_transformed).toarray()

    print "spam is ", sum(labels_train)
    print "not spam is ", len(labels_train)-sum(labels_train)
    print "training set length is ", len(labels_train)
    return features_train_transformed,features_test_transformed,labels_train,labels_test
