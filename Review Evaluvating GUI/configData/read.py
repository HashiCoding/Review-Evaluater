import sqlite3
import random
import sklearn as sl ###  tensorflow,Pytorch for nural network modles


class Sentiment:
	negative ="NEGATIVE"
	positive ="POSITIVE"


class Review:
    def __init__(self, text, score):
        self.text = text
        self.score = score
        self.sentiment = self.get_sentiment()

    def get_sentiment(self):
        if float(self.score) <= 2:
            return Sentiment.negative
        else:
            return Sentiment.positive
        

class ReviewContainer:
	def __init__(self, reviews):
		self.reviews = reviews

	def get_text(self):
		return [x.text for x in self.reviews]

	def get_sentiment(self):
		return [x.sentiment for x in self.reviews]
    

	def evenly_distribute(self):
		negative = list(filter(lambda x: x.sentiment == Sentiment.negative, self.reviews))
		positive = list(filter(lambda x: x.sentiment == Sentiment.positive, self.reviews))
        #print(len(negative),len(positive),len(nutral)) 
		positive_shrunk = positive[:len(negative)]
		self.reviews = positive_shrunk + negative 
		random.shuffle(self.reviews)
		#print(len(negative),(len(positive_shrunk)))


conn = sqlite3.connect('review.db')
cur = conn.cursor()
cur.execute(" SELECT * FROM reviews")
items = cur.fetchall()
reviews = []
for item in items:
    reviews.append(Review(item[1],(item[2])))
cur.close()


from sklearn.model_selection import train_test_split
training, test = train_test_split(reviews, test_size = 0.33, random_state=42)
train_containers = ReviewContainer(training)
test_containers = ReviewContainer(test)


train_containers.evenly_distribute()
train_x = train_containers.get_text()
train_y = train_containers.get_sentiment()


test_containers.evenly_distribute()
test_x =  test_containers.get_text()
test_y =  test_containers.get_sentiment()

# print(train_y.count(Sentiment.positive),train_y.count(Sentiment.negative))


from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
train_x_vectors = vectorizer.fit_transform(train_x)
test_x_vectors = vectorizer.transform(test_x)



# from sklearn import svm
# svm
# clf_svm = svm.SVC(kernel='linear')
# #print(test_x[0])
# #print(test_x_vectors)
# clf_svm.fit(train_x_vectors,train_y)
# p = clf_svm.predict(test_x_vectors[0])
# print(p)


# #decisiontree
# from sklearn.tree import DecisionTreeClassifier
# clf_dec =  DecisionTreeClassifier()
# clf_dec.fit(train_x_vectors,train_y)
# p1 = clf_dec.predict(test_x_vectors[0])
# print(p1)


# #naive bayes
# from sklearn.naive_bayes import GaussianNB 
# clf_gnb = DecisionTreeClassifier()
# clf_gnb.fit(train_x_vectors,train_y)
# p2 = clf_gnb.predict(test_x_vectors[0])
# print(p2)



#logistic regression
from sklearn.linear_model import LogisticRegression
clf_log = LogisticRegression()
clf_log.fit(train_x_vectors,train_y)
p3 = clf_log.predict(test_x_vectors[0])
#print(p3)




#############################  EVALUATION
#mean acuracy

# s1 = clf_svm.score(test_x_vectors,test_y)
# print(s1)

# s2 = clf_dec.score(test_x_vectors,test_y)
# print(s2)

# s3 = clf_gnb.score(test_x_vectors,test_y)
# print(s3)

s4 = clf_log.score(test_x_vectors,test_y)
#print(s4)






#F1 scores

from sklearn.metrics import f1_score

# F1 = f1_score(test_y, clf_svm.predict(test_x_vectors),average= None , labels= [Sentiment.positive,Sentiment.negative] ) 
# print(F1)

# F2 = f1_score(test_y, clf_dec.predict(test_x_vectors),average= None , labels= [Sentiment.positive,Sentiment.negative] ) 
# print(F2)

# F3 = f1_score(test_y, clf_gnb.predict(test_x_vectors),average= None , labels= [Sentiment.positive,Sentiment.negative]) 
# print(F3)

F4 = f1_score(test_y, clf_log.predict(test_x_vectors),average= None , labels= [Sentiment.positive,Sentiment.negative] ) 
#print(F4)



### input fileds
def prediction(comment):
	test_set = [f"{comment}"]
	new_test = vectorizer.transform(test_set)
	result = clf_log.predict(new_test)
	return(result)
    

# com = ["great"]
# print(prediction(com))
