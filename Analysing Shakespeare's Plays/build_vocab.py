import math
import os
import re
import pickle
import string

""" Helper Functions """

""" Function to read all comedies """
def getComedies():

    comedies = []
    fileNames = []
    for filename in os.listdir('./shakespeare/comedies/'):
        theFile = open('./shakespeare/comedies/'+filename).read().lower()
        print "read "+filename
        fileNames.append(theFile)
        comedies.append(filename)

    return comedies, fileNames

""" Function to read all tragedies """
def getTragedies():

    tragedies = []
    fileNames = []
    for filename in os.listdir('./shakespeare/tragedies/'):
        theFile = open('./shakespeare/tragedies/'+filename).read().lower()
        print "read " + filename
        fileNames.append(theFile)
        tragedies.append(filename)

    return tragedies, fileNames

""" Function to return frequency of word belonging to class comedy and tragedy """
def getCountsPerClass(wordDict, fileNames, fileNamesT):
    sumC = 0
    sumT = 0
    allFileNames = wordDict.keys()
    for fileName in allFileNames:
        if fileName in fileNames:
            sumC += wordDict[fileName]
        elif fileName in fileNamesT:
            sumT += wordDict[fileName]

    return sumC, sumT

""" Main program execution starts from here """

fileNames, comedies = getComedies()
fileNamesT, tragedies = getTragedies()
wordsInPlayComedies = []
wordsInPlayTragedies = []

i = 0

wordsInPlayDict = {}

pickleFileName = "corpus_shkspr.p"

exclude = string.punctuation

lists = os.listdir("./")

""" The data from the corpus i.e. words and their frequencies file-wise are stored as a pickle file(a dictionary), if not found - create a pickle file
This speeds up execution for subsequent runs of the programs. """

if pickleFileName not in lists:
    print "Reading all comedies : "
    for c in comedies:
        comedies[i] = re.sub(r"/n", " ", comedies[i])
        comedies[i] = ''.join(ch for ch in comedies[i] if ch not in exclude).lower()
        comedies[i] = comedies[i].split(" ")
        currentFile = fileNames[i]
        for word in comedies[i]:
            if word not in wordsInPlayDict.keys():
                wordsInPlayDict[word] = {currentFile: 1}
            else:
                tempDict = wordsInPlayDict[word]
                if currentFile in tempDict.keys():
                    tempDict[currentFile] += 1
                else:
                    tempDict[currentFile] = 1
                wordsInPlayDict[word] = tempDict

        i += 1

    i = 0

    print len(wordsInPlayDict)

    print "Reading all tragedies : "

    for t in tragedies:
        tragedies[i] = re.sub(r"/n", " ", tragedies[i])
        tragedies[i] = ''.join(ch for ch in tragedies[i] if ch not in exclude).lower()
        tragedies[i] = tragedies[i].split(" ")
        currentFile = fileNamesT[i]
        for word in tragedies[i]:
            if word not in wordsInPlayDict.keys():
                wordsInPlayDict[word] = {currentFile: 1}
            else:
                tempDict = wordsInPlayDict[word]
                if currentFile in tempDict.keys():
                    tempDict[currentFile] += 1
                else:
                    tempDict[currentFile] = 1
                wordsInPlayDict[word] = tempDict

        i += 1

    

    """ If not found, create the pickle file """
    pickle.dump(wordsInPlayDict, open(pickleFileName, "wb"))
    vocabFile = open("vocab.txt", "w")
    vocabFile.write(str(wordsInPlayDict.keys()))
    vocabFile.close()
    print "pickle dump done"

    """ If pickle file exists """
else:
    wordsInPlayDict = pickle.load(open("./"+pickleFileName, "rb"))
    
sumOfCounts = 0
wordOccurranceDict = {}
featureLikelihoods = {}

""" wordsInPlayDict.keys() essentially returns the vocab set """
for word in wordsInPlayDict.keys():
    sumOfCounts = len(wordsInPlayDict.get(word).keys())

    """ If the word appears in only ONE file, DELETE the word entry """
    if sumOfCounts == 1:
        del wordsInPlayDict[word]
        """ If the word appears in multiple files but total count of those frequencies is less than 5, DELETE the word entry """
    elif sum(wordsInPlayDict.get(word).values()) < 5:
        del wordsInPlayDict[word]
        
    else:

        
        comedyCount, tragedyCount = getCountsPerClass(wordsInPlayDict[word], fileNames, fileNamesT)

        """ totalCount is the total number of times the feature occurs in our corpus """
        totalCount = comedyCount + tragedyCount
        wordOccurranceDict[word] = {"comedyFreq":comedyCount, "tragedyFreq":tragedyCount, "totalCount": totalCount}

        """ Store the comedy & tragedy probabilities of the feature (with lambda smoothing of 0.1)"""
        featureLikelihoods[word] = {"comedy":(float(comedyCount)+0.1/float(totalCount)),
                                            "tragedy":(float(tragedyCount)+0.1/float(totalCount))}

vocabFile = open("word_freq.txt", "w")
del wordOccurranceDict['']
vocabFile.write(str(wordOccurranceDict))
vocabFile.close()

""" Vocabulary extracted has been written to a file called vocab.txt """
vocabFile1 = open("vocab.txt", "w")
vocabFile1.write(str(featureLikelihoods.keys()))
vocabFile1.close()

""" Word Frequencies stored in a pickle file """
pickle.dump(wordOccurranceDict, open("word_freq.p", "wb"))

featureWiseLikelihood = {}

for feature in featureLikelihoods.keys():
    """ The likelihood is computed as P(comedy|feature)/P(tragedy|feature) """
    """ Since the values are small, they have been converted to LOG base 2 and subtracted
    i.e. equivalent to division """    
    featureWiseLikelihood[feature] = math.log(featureLikelihoods[feature].get("comedy"), 2) - \
                                                 math.log(featureLikelihoods[feature].get("tragedy"), 2)

""" The features have been sorted by their log likelihood values """
logLikelihoodFeatures = sorted(featureWiseLikelihood.items(), key=lambda x: x[1], reverse=True)

print "\n20 Most comic features : \n"
for (k, v) in logLikelihoodFeatures[0:20] : 
    print k ,"  -->  ", v

end = len(logLikelihoodFeatures) - 1

print "\n20 Most tragic features : \n"
for (k, v) in logLikelihoodFeatures[end-20:end]:
    print k, "  -->  ", v











