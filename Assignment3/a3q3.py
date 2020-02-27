# Mohamed Bensaleh
# CMPT 145 Assignment 3 Question 3
# Mob127
# 11254030

from collections import Counter

def create(filename):
    """
        Purpose:  creates an empty list to store allowed strings from experimental data
        Pre-conditions:
            :param filename: experimental data (input file)
        Post-conditions: None
        Return
            :return an empty list to store experimental data
        """
    f = open(filename, 'r')
    dnaSequence = []
    for line in f:
        if line[0] == '>':
            dnaSequence.append('')
        else:
            for i in line:
                if i in 'ATCG':
                    dnaSequence[-1] += i
    f.close()
    return dnaSequence


# Display each sequences one by one
def display(dnaSequence):
    """
    Purpose: Displays each sequence as a string
    Pre-conditions:
        :param dnaSequence: strings representing data stored within Experiment ADT
    Post-conditions: None
    Return:
        :return Each sequence one by one from input file
        """
    for sequence in dnaSequence:
        return sequence


# Get the number of sequences present in the list
def numSequences(dnaSequence):
    """
    Purpose: Returns the number of sequences in the Experiment ADT
    Pre-conditions:
        :param dnaSequence: strings representing data stored within Experiment ADT
    Post-conditions: None
    Return:
        :return The number of sequences stored in Experiment ADT
        """
    return len(dnaSequence)


# Get average length all sequences
def averageLength(dnaSequence):
    """
    Purpose: Returns the average length of the sequences in the Experiment ADT
    Pre-conditions:
        :param dnaSequence: strings representing data stored within Experiment ADT
    Post-conditions: None
    Return:
        :return The average length of the sequences stored in Experiment ADT
            """
    avg = 0
    for sequence in dnaSequence:
        avg += len(sequence)
    return int(avg / len(dnaSequence))


# Get length distribution based dictionary
# Keys are length
# Values are sequences in same length
def lengthDistribution(dnaSequence):
    """
    Purpose: Returns a dictionary where keys are unique sequence length and values are integer counts of the number of
    sequences with that length.
    Pre-conditions:
        :param dnaSequence: strings representing data stored within Experiment ADT
    Post-conditions: None
    Return:
        :return Dictionary where keys are length and values are counts of sequences with that length
                """
    dictSequence = Counter(map(len, dnaSequence))
    return dictSequence


# Get overall average GC count
def averageGCcontent(dnaSequence):
    """
    Purpose:
    Pre-conditions: Calculates and returns the average GC content  of the sequences stored in the Experiment ADT
        :param dnaSequence: strings representing data stored within Experiment ADT
    Post-conditions: None
    Return:
        :return Average GC content of the sequences stored in the Experiment ADT
                    """
    total = 0
    gcTotal = 0
    for sequence in dnaSequence:
        total += len(sequence)
        for ch in sequence:
            if ch == 'G' or ch == 'C':
                gcTotal += 1
    try:
        z = (gcTotal / total) * 100
    except ZeroDivisionError:
        z = 0
    return z

# Remove all low quality sequences from the list
def removeLowQuality(dnaSequence, minCutoff, maxCutoff):
    """
    Purpose: Removes sequences stored in the Experiment ADT that have a GC content below minCutoff or above maxCutoff.
    Pre-conditions:
        :param dnaSequence: strings representing data stored within Experiment ADT
        :param minCutoff: Number representing minimum GC content
        :param maxCutoff: Number representing maximum GC content
    Post-condtions:
        The number of sequences stored in the Experiment ADT decreases in size
    Return:
        :return: None
    """
    for sequence in dnaSequence:
        gcTotal = 0
        for ch in sequence:
            if (ch == 'G' or ch == 'C'):
                gcTotal += 1

            if (gcTotal > minCutoff or gcTotal < maxCutoff):
                while True:
                    try:
                        dnaSequence.remove(sequence)
                    except:
                        break
                    while ('' in dnaSequence):
                        dnaSequence.remove('')
    return dnaSequence





