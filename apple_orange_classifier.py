from sklearn import tree
#program to classify apple from oranges
# feature is smooth,0 vs bumpy,1
# feature is weight of the fruit, oranges tend to be heavier
features=[[140,0],[130,0],[150,1],[170,1]]
#values corresponding to above data, 0-apple, 1-orange
lables=[0,0,1,1]

#pick a classifier
classifier=tree.DecisionTreeClassifier()

#train classifier with data
classifier=classifier.fit(features, lables)

#checking the result of prediction

print classifier.predict([[160,1]])

