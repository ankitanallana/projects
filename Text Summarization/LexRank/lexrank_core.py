import os
import math
import numpy
from unicodedata import category
import codecs
import nltk
from collections import namedtuple
from operator import attrgetter

def getTermFrequencyVector(sentence, wordMap):

    words = sentence.split()

    tempDict = {}

    for w in words:
        if w in wordMap:
            count = wordMap[w] + 1
            wordMap[w] = count
        else:
            wordMap[w] = 1
        if w in tempDict:
            count = tempDict[w] + 1
            tempDict[w] = count
        else:
            tempDict[w] = 1

    return tempDict

def getAverageCosineValues(matrix):
    sum = 0.0
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]!= 0 and matrix[i][j]!=1:
                sum += matrix[i][j]
                count += 1

    average = float(sum)/count
    return average


def cosineSimilarity(sentence1, sentence2, tf1, tf2, idfMatrix):

    #print sentence1, sentence2

    s1 = sentence1.split()
    s2 = sentence2.split()

    set1 = set(s1)
    set2 = set(s2)

    unique_words = set1.intersection(set2)

    num = 0
    for word in unique_words:
        if word in tf1 and word in tf2 and word in idfMatrix:
            num += tf1[word] * tf2[word] * pow(idfMatrix[word], 2)

    sum1 = 0
    for i in tf1.keys():
        sum1 += pow(tf1[i]*idfMatrix[i], 2)

    sum2 = 0
    for i in tf2.keys():
        sum2 += pow(tf2[i]*idfMatrix[i], 2)

    if sum1 > 0 and sum2 > 0:
        denom = float(math.sqrt(sum1)) * math.sqrt(sum2)
        return float(num)/denom

    else:
        return 0.0

def computeLexRankScores(similarityMatrix, degree, threshold_value, typeS):

    for i in range(len(similarityMatrix)):
        for j in range(len(similarityMatrix[i])):
            if typeS is 'LexRank':
                if similarityMatrix[i][j] > threshold_value :
                    similarityMatrix[i][j] = 1
                    degree[i] += 1
                else:
                    similarityMatrix[i][j] = 0
            else:
                degree[i] += 1

    for i in range(len(similarityMatrix)):
        for j in range(len(similarityMatrix[i])):
            try:
                similarityMatrix[i][j] = float(similarityMatrix[i][j])/degree[i]
            except ZeroDivisionError:
                pass

    return similarityMatrix

def lexicalPageRank(matrix, n):
    transpose_matrix = zip(*matrix)

    lambda_value = 1.0
    e = 0.1

    vector_p = [(1.0 / n) for i in range(n)]

    while lambda_value > e:
        p_next = numpy.dot(transpose_matrix, vector_p)
        lambda_value = numpy.linalg.norm(numpy.subtract(p_next, vector_p))
        vector_p = p_next

   # print vector_p
    return vector_p

def getBestRankedSentences(sentencesArray, summarySize):
    sentence_desc = namedtuple("sentence_desc", ("sentence", "order", "p_rating"))

    sentence_list = []
    count = 0
    for s in sentencesArray:
        sen, score = s
        sentence_list.append(sentence_desc(sen, count, score))
        count += 1

    """ Get top ranked sentences """
    temp_list = sorted(sentence_list, key=attrgetter("p_rating"), reverse=True)
    if summarySize==0:
        summarySize = int(len(sentencesArray) * 0.41)

    temp_list = temp_list[:summarySize]

    """ Sort them by order """
    temp_list = sorted(temp_list, key=attrgetter("order"))
    return temp_list



def getDocumentContent(fileName):
    cwd = os.getcwd()
    import re
    newline_string = "\n+"

    content = codecs.open(cwd +"/articles/"+fileName, "r", encoding='utf8').read()
    content = re.sub(newline_string, ".\n", content)
    tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
    sentences = tokenizer.tokenize(content)

    sentences = [sentence.strip() for sentence in sentences]

    all_sentences = [sentence.split("\n") for sentence in sentences]
    sentences = [item for sublist in all_sentences for item in sublist]

    sentences = [''.join(ch for ch in sentence if category(ch)[0] != 'P') for sentence in sentences]
    sentences = [sentence for sentence in sentences if sentence.strip() is not ""]

    #print "number of sentences - ", len(sentences)
    return sentences

