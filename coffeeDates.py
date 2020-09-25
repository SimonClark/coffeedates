#! /usr/bin/python3

import json, random
import cdUtils
import os

print('')
dataset = cdUtils.getDataset()

with open(dataset + '/matchWeights.json') as json_file:
    matchWeights = json.load(json_file)

# Scrub the participants list html for display names and match them with slack IDs
fread = open(dataset + '/participants.txt','r')
participants = []

for line in fread:
	if not line.startswith('//'):
		parts = line.split(':')
		name = parts[-1]
		participants.append(name.strip())

print ("%d Participants found." % (len(participants)))

# Make up to 50000 sets of random pairs and find the one with the lowest recent meeting weighting
lowestTotal = 1000000

for counter in range(1, 50000):
	pairs = []
	totalMatchWeight = 0.0;
	participantsPool = list(participants)
	while len(participantsPool) > 1:
		p1 = cdUtils.popRandom(participantsPool)
		p2 = cdUtils.popRandom(participantsPool)
		pair = cdUtils.orderedPair(p1, p2)

		weightsKey = cdUtils.getWeightsKey(pair)
		if weightsKey in matchWeights:
			totalMatchWeight = totalMatchWeight + matchWeights[weightsKey]
		pairs.append(pair)

	if len(participantsPool) == 1:
		weightsKey = cdUtils.getWeightsKey(participantsPool)
		if weightsKey in matchWeights:
			totalMatchWeight = totalMatchWeight + matchWeights[weightsKey]
		pairs.append([participantsPool[0]])

	if totalMatchWeight < lowestTotal:
		approvedPairs = list(pairs)
		lowestTotal = totalMatchWeight
		if lowestTotal == 0:
			break

prettyOutput = cdUtils.printPairs(approvedPairs)
print (prettyOutput)
print ("Weighting: %f" % (lowestTotal))

proceed = input("Do you wish to proceed? (Y/N) ")
if not (proceed == "Y" or proceed == "y"):
	exit()

# Update the recent weightings, and save them and the output
print ("Commiting matches")
for key in matchWeights:
	matchWeights[key] = matchWeights[key] / 2
for pair in approvedPairs:
	matchWeights[cdUtils.getWeightsKey(pair)] = 1.0;
with open(dataset + '/matchWeights.json', 'w') as outfile:
	json.dump(matchWeights, outfile)
with open(dataset + '/output.txt', "w") as outfile:
	outfile.write(prettyOutput)
