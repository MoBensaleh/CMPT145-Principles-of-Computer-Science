# Mohamed Bensaleh
# CMPT 145 Assignment 3 question 4
# Mob127
# 11254030

import a3q3 as Experiment

dnaSequence = Experiment.create("sequences2.txt")
numSequences = Experiment.numSequences(dnaSequence)
averageGC = Experiment.averageGCcontent(dnaSequence)
seqLength = Experiment.averageLength(dnaSequence)
lengthDistrib = Experiment.lengthDistribution(dnaSequence)

minCutoff=int(input('Enter minCutoff: '))
maxCutoff = int(input('Enter maxCutoff: '))

print("Number of sequences:", numSequences)
print('Average GC content:', averageGC, '%')
print('Average Sequence Length:', seqLength)
print('Sequence Length Distributions:')
print('     Length: Number of Sequences','\n\r', lengthDistrib)
print('                                                         ')
print('Removing Sequences with GC content below', minCutoff, 'or above', maxCutoff)
print('Updated Statistics ------------------------')
Experiment.removeLowQuality(dnaSequence, minCutoff, maxCutoff)
print('Number of Sequences:', Experiment.numSequences(dnaSequence))
print('Average GC content:', Experiment.averageGCcontent(dnaSequence), '%')
print('Average Sequence Length:', Experiment.averageLength(dnaSequence))
print('Sequence Length Distributions:')
print('     Length: Number of Sequences','\n\r', Experiment.lengthDistribution(dnaSequence))







