from preprocess import preprocess
features_train, features_test, labels_train, labels_test = preprocess()

scores=[]
import numpy
features= numpy.row_stack((features_train,features_test))
labels = numpy.array(labels_train+labels_test)

print "Baeye's Incoming"
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(features_train,labels_train)
clf.predict(features_test)
accuracy = clf.score(features_test,labels_test)
print accuracy

from sklearn.cross_validation import cross_val_score
scores=cross_val_score(clf,features,labels,cv=4)
print "accuracy is ", scores.mean(),"+-",scores.std()*2

print "SVM rocking"
from sklearn import svm
clf = svm.SVC(kernel='rbf',C=1000)
clf.fit(features_train,labels_train)
accuracy=clf.score(features_test,labels_test)
print accuracy

from sklearn.cross_validation import cross_val_score
scores=cross_val_score(clf,features,labels,cv=4)
print "accuracy is ", scores.mean(),"+-",scores.std()*2

pufeat=[]
for i in range(1,len(labels)):
    if labels[i]==0:
        pufeat.append(features[i])
pufeat=numpy.array(pufeat)
clf = svm.OneClassSVM(nu=0.1,kernel='rbf',gamma=0.1)
pufeat=pufeat[1:700]
clf.fit(pufeat)
ypred=clf.predict(features)
errors=ypred[ypred==-1].size
print errors