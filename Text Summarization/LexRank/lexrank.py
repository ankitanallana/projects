import evaluation
import lexrank_core
import lexrank_summarize
import os


""" Driver Program """
def summarizeDocuments(fileNames, summarySize):


    for fileName in fileNames:
        summFlag = True

        print "\n---------------", fileName, "------------------\n"
        summaryFileName = fileName.split(".")[0]+"_summ.txt"
        try:
            referenceSummaryExtracts = lexrank_core.getDocumentContent(summaryFileName)
        except IOError:
            summFlag = False
            pass

        print "\n------ LexRank 0.1 ------\n"
        threshold = 0.1
        summaryExtracts = []
        summarySentencesLexRank, original_sentencesLexRank = lexrank_summarize.summarize(lexrank_core.getDocumentContent(fileName),
                                                                                         threshold,
                                                                                         summarySize,
                                                                                         'LexRank')
        for i in summarySentencesLexRank:
            summaryExtracts.append(original_sentencesLexRank[i.order])

        for s in summaryExtracts:
            print s

        """ Precision & Recall - LexRank """
        if summFlag :

            precisionScore = evaluation.evaluatePrecision(summaryExtracts, referenceSummaryExtracts)
            recallScore = evaluation.evaluateRecall(summaryExtracts, referenceSummaryExtracts)

            print "\n"
            print "Precision : ", precisionScore
            print "Recall : ", recallScore
            print "\n"

        print "\n------ LexRank 0.2 ------\n"

        threshold = 0.2

        summaryExtracts = []

        summarySentencesLexRank, original_sentencesLexRank = lexrank_summarize.summarize(
            lexrank_core.getDocumentContent(fileName),
            threshold,
            summarySize,
            'LexRank')
        for i in summarySentencesLexRank:
            summaryExtracts.append(original_sentencesLexRank[i.order])

        for s in summaryExtracts:
            print s

        if summFlag:

            """ Precision & Recall - LexRank """
            precisionScore = evaluation.evaluatePrecision(summaryExtracts, referenceSummaryExtracts)
            recallScore = evaluation.evaluateRecall(summaryExtracts, referenceSummaryExtracts)

            print "\n"
            print "Precision : ", precisionScore
            print "Recall : ", recallScore
            print "\n"

        """ cLexRank """

        print "\n------ c-LexRank ------\n"

        summarySentencesLexRank, original_sentencesLexRank = lexrank_summarize.summarize(lexrank_core.getDocumentContent(fileName),
                                                                                         threshold,
                                                                                         summarySize,
                                                                                         'cLexRank')
        summaryExtracts = []
        for i in summarySentencesLexRank:
            summaryExtracts.append(original_sentencesLexRank[i.order])

        for s in summaryExtracts:
            print s

        if summFlag:

            """ Precision & Recall - cLexRank """
            precisionScore = evaluation.evaluatePrecision(summaryExtracts, referenceSummaryExtracts)
            recallScore = evaluation.evaluateRecall(summaryExtracts, referenceSummaryExtracts)

            print "\n"
            print "Precision : ", precisionScore
            print "Recall : ", recallScore
            print "\n"


"""

All files in the articles directory whose summaries can be generated - the array of file names is given
below. Some of them have a corresponding summary file. If the program finds it, it computes and displays the precision
and recall scores. Else it displays the generated summaries.

Three kinds of summaries are generated per file - one using LexRank with threshold value = 0.1,
one using LexRank with threshold value = 0.2 and one using continuous LexRank.

If the threshold value needs to be modified, on Line 23 of this file, change the value of the
variable named threshold

fileNames = ['014.txt', '015.txt', '016.txt', '017.txt', '018.txt',  '020.txt', '025.txt',
                      '033.txt',  '037.txt',  '051.txt',  '058.txt',
                     '068.txt',  '077.txt', '080.txt', '081.txt', '082.txt', '083.txt', '084.txt', '085.txt',
                     '096.txt',  '104.txt',  '124.txt',  '145.txt',  '161.txt',
                      '167.txt',  '258.txt', '270.txt', '277.txt', '282.txt',  '289.txt', '305.txt',
                     '318.txt',  'reut1.txt', 'reut2.txt', 'reut3.txt', 'reut4.txt', 'sumx.txt']"""


fileNames = ["reut1.txt", "096.txt", "reut3.txt", "018.txt"]
summarySize = 0

summarizeDocuments(fileNames, summarySize)

