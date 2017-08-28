import math
import os
import re
import pickle
from collections import Counter
import string
import nltk

""" Helper Functions """

""" Function to read all comedies """
def getComedies():
    comedies = []
    fileNames = []
    comediesDict = {}
    for filename in os.listdir('./shakespeare/comedies/'):
        theFile = open('./shakespeare/comedies/' + filename).read().lower()
        #print "read " + filename
        fileNames.append(theFile)
        comedies.append(filename)
        comediesDict[filename] = theFile
    pickle.dump(comediesDict, open("./comediesDict.p","wb"))
    return comediesDict

""" Function to read all comedies """
def getTragedies():
    tragedies = []
    fileNames = []
    tragediesDict = {}
    for filename in os.listdir('./shakespeare/tragedies/'):
        theFile = open('./shakespeare/tragedies/' + filename).read().lower()
        #print "read " + filename
        fileNames.append(theFile)
        tragedies.append(filename)
        tragediesDict[filename] = theFile
    pickle.dump(tragediesDict, open("./tragediesDict.p", "wb"))
    return tragediesDict

""" Function to obtain frequency of a word from a particular class"""
def getFeatureFrequencyByClass(feature, FILE, allFeaturesDict, classTracker, dclass):
    sumOfFrequency = 0
    for f in classTracker.keys():
        """ The following IF condition handles the case that we are not going to read from the test document"""
        if f != FILE:
            if classTracker[f]==dclass:
                tempDict = allFeaturesDict[f]
                featureFreq = tempDict[feature]
                if featureFreq!=None:
                    sumOfFrequency += featureFreq
    return sumOfFrequency

""" Function to obtain all Features in a particular class """
def getAllFeaturesCountByClass(FILE, allFeaturesDict, classTracker, dclass):
    sumOfAllFeatures = 0
    for f in classTracker.keys():
        """ The following IF condition handles the case that we are not going to read from the test document"""
        if f != FILE :
            if classTracker[f] == dclass :
                getData = sum(allFeaturesDict[f].values())
                if getData!= None:
                    sumOfAllFeatures += getData
    return sumOfAllFeatures

""" Main program execution begins from here """

lists = os.listdir("./")
pickleComediesDict = "comediesDict.p"
pickleTragediesDict = "tragediesDict.p"

""" Corpus from comedy & tragedy classes being retrieved from pickle files (if they exist)"""

if pickleComediesDict not in lists:
    comediesDict = getComedies()
else:
    comediesDict = pickle.load(open("./"+pickleComediesDict, "rb"))

if pickleTragediesDict not in lists:
    tragediesDict = getTragedies()
else:
    tragediesDict = pickle.load(open("./"+pickleTragediesDict, "rb"))

allFileNames = {}

""" classTracker keeps track of files and which class they belong to i.e. comedy or tragedy """
classTracker = {}

""" allFeaturesDict maintains the features and their frequencies document wise """
allFeaturesDict = {}
exclude = string.punctuation

for c in comediesDict.keys():
    """ Cleaning the data - removing punctuation, lower case conversion, etc """
    content = comediesDict[c]
    classTracker[c] = "comedy"
    content = re.sub(r"\n", " ", content)
    content = ''.join(ch for ch in content if ch not in exclude).lower()

    """ All features have been extracted from the document """
    content = nltk.word_tokenize(content)

    """ Frequencies of all features have been computed """
    tempDict = Counter(content)

    """ Features and their corresponding frequencies have been added to a dictionary
    with the document name """
    allFeaturesDict[c] = tempDict

for c in tragediesDict.keys():
    """ Cleaning the data - removing punctuation, lower case conversion, etc """
    content = tragediesDict[c]
    classTracker[c] = "tragedy"
    content = re.sub(r"\n", " ", content)
    content = ''.join(ch for ch in content if ch not in exclude).lower()

    """ All features have been extracted from the document """
    content = nltk.word_tokenize(content)

    """ Frequencies of all features have been computed """
    tempDict = Counter(content)

    """ Features and their corresponding frequencies have been added to a dictionary
    with the document name"""
    allFeaturesDict[c] = tempDict

allFiles = allFeaturesDict.keys()

""" vocab being loaded from a pickle file generated from part 1 """
vocab = pickle.load(open("word_freq.p", "rb"))
totalP = 1
documentClasses = ["comedy", "tragedy"]
i = 0

""" resultdata stores probabilities of the document per class """
resultdata = {}
vocabList = vocab.keys()

""" We will now proceed to calculate P(feature|class) for
every feature present (from our test document) in our vocab for every class

To calculate the Probability that a document D belongs to a class C, we calculate
all probabilities of the document belonging to every class C and finally assign it the class
which returns with the highest probability.

More formally:

P(C|D) = MAX (for all C, P(C|D))

To calculate the Probability of an unknown document D belonging to class C, we know that :

P(C|D) = P(D|C) * P(C) / P(D)

Since P(D) would be the same for all terms, we can choose to ignore it

A Document is made up of set of features X = {x1, x2 ... xn}

so P(D|C) = P(x1, x2, ... xn | C)
or (since we're assuming independence of the features here
P(D|C) = P(x1|C) * P(x2|C) * ... P(xn|C)

where P(xn|C) = frequency of feature xn in class C / frequency of all features in class C
P(C) has been fixed at 0.5 (comedy/tragedy prior probabilities)

"""

for FILE in allFiles:
    for dclass in documentClasses:

        """ Obtain all features from test doc """
        testDocFeatures = allFeaturesDict[FILE]
        totalP = 0
        p_feature = 1

        """ Obtain frequencies of all features belonging to a class"""
        dr = getAllFeaturesCountByClass(FILE, allFeaturesDict, classTracker, dclass)

        """ for every feature in test document """
        for feature in testDocFeatures.keys():
            if feature in vocabList:
                nr = getFeatureFrequencyByClass(feature, FILE, allFeaturesDict, classTracker, dclass)
                p_feature = (float(nr) + 0.1)/(float(dr) + 0.1 * len(vocabList))
                totalP += float(math.log(p_feature, 2))

        if resultdata.get(FILE) is None:
                    resultdata[FILE] = {dclass: (float(totalP) + math.log(0.5, 2))} #comedy/tragedy prior fixed at 0.5
        else:
                tempDict = {dclass: totalP}
                resultdata[FILE].update(tempDict)

res = {}

""" Here we assign the class which returned the highest probability of the document """
for f in allFiles:
    maximum = float('-inf')
    tempDict = resultdata[f]
    for x in tempDict:
        if tempDict[x] > maximum:
            maximum = tempDict[x]
            res[f] = x

misses = 0
total = 0

details = open("./results.txt", "wb")
differenceList = {}

print "\n"

""" Loop that prints the predictions that weren't correctly classified"""
for k in classTracker.keys():
    total += 1
    tempDict = resultdata[k]

    if res[k] != classTracker[k]:
        misses += 1
        print k, " is a ", classTracker[k], " - Predicted as ", res[k]
        differenceList[k] = tempDict["comedy"] - tempDict["tragedy"]

    details.write("\n\n======For FILE "+k+" ======\n")
    details.write(k+" is a "+classTracker[k]+" - Predicted as "+res[k]+"\n")

    """ Calculating the log likelihood ratio of comedy/tragedy per file """
    logLkhd = float(tempDict["comedy"]) / float(tempDict["tragedy"])
    details.write("log likelihood ratio (comedy/tragedy) : "+str(logLkhd))

print "\nAccuracy - ", (float(total-misses)/total)*100, "%\n\nTotal incorrect classifications - ", misses

""" The list of incorrect classifications """
sortedList = sorted(differenceList.items(), key=lambda x: x[1], reverse=True)
details.write("\n=====================================\n")
print "\n\nTragedy most similar to comedy - ", sortedList[0][0]
print "\n\nComedy most similar to tragedy - ", sortedList[len(sortedList)-1][0]
details.write("\n\nTragedy most similar to comedy - "+ sortedList[0][0])
details.write("\n\nComedy most similar to tragedy - "+ sortedList[len(sortedList)-1][0])
print "\n\n"
details.close()







