def evaluatePrecision(summaryExtracts, referenceExtracts):

    summaryExtracts = frozenset(summaryExtracts)
    referenceExtracts = frozenset(referenceExtracts)
    commonSentences = summaryExtracts & referenceExtracts

    if len(commonSentences) == 0:
        return 0

    return float(len(commonSentences))*100 / len(summaryExtracts)


def evaluateRecall(summaryExtracts, referenceExtracts):
    summaryExtracts = frozenset(summaryExtracts)
    referenceExtracts = frozenset(referenceExtracts)
    commonSentences = summaryExtracts & referenceExtracts

    if len(commonSentences) == 0:
        return 0

    return float(len(commonSentences))*100 / len(referenceExtracts)
