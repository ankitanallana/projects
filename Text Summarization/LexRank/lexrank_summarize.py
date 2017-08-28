import lexrank_core
import math

def summarize(sentences, threshold_value, summarySize, method):

    num_sentences = len(sentences)
    original_sentences = sentences
    N = 0

    for s in sentences:
        for term in s.split():
             N += 1


    similarityMatrix = [[0 for x in range(num_sentences)] for y in range(num_sentences)]
    termFrequencyMatrix = [[] for y in range(num_sentences)]
    idfMatrix = {}

    i=0
    wordMap = {}

    """ CALCULATE TF VECTORS PER SENTENCE """
    for s in sentences:
        termFrequencyMatrix[i] = lexrank_core.getTermFrequencyVector(s, wordMap)
        i += 1

    """ CALCULATE IDF PER WORD """
    for w in wordMap.keys():
        if w not in idfMatrix:
            idfMatrix[w] = math.log(N/wordMap[w], 2)


    """ BUILD SIMILARITY MATRIX """
    for i in range(num_sentences):
        for j in range(num_sentences):
            if i==j:
                similarityMatrix[i][j] = 1
            else:
                similarityMatrix[i][j] = lexrank_core.cosineSimilarity(sentences[i], sentences[j], termFrequencyMatrix[i],
                                                      termFrequencyMatrix[j], idfMatrix)


    """ COMPUTE LEXRANK SCORES """

    degree = [0 for i in range(len(similarityMatrix))]

    lexRankScoresMatrix = lexrank_core.computeLexRankScores(similarityMatrix, degree, threshold_value, method)


    similarSentencesMatrix = []

    for i in range(len(lexRankScoresMatrix)):
        similarSentencesMatrix.append([])
        for j in range(len(lexRankScoresMatrix)):
            if(i!=j):
                if lexRankScoresMatrix[i][j] > 0:
                    similarSentencesMatrix[i].append(j)

    """ RANK SENTENCES USING PAGE RANK """

    vector_p = lexrank_core.lexicalPageRank(lexRankScoresMatrix, len(sentences))

    sentencesArray = ['' for i in range(len(sentences))]
    count = 0
    for s in sentences:
        sentencesArray[count] = (s, vector_p[count])
        count += 1


    """ GET TOP N RANKED SENTENCES """

    summarySentences = lexrank_core.getBestRankedSentences(sentencesArray, summarySize)

    return summarySentences, original_sentences

