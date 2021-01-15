#! /usr/bin/python3

import json, random, datetime, os

def getWeightsKey(pair):
	if len(pair) == 2:
		return pair[0] + ":" + pair[1];
	return pair[0] + "::"

def popRandom(aList):
	i = random.randint(0,len(aList) - 1 )
	result = aList[i]
	del aList[i]
	return result

def orderedPair(item1, item2):
	if item1 < item2:
		return [item1, item2]
	else:
		return [item2, item1]

def printPairs(pairs):
	date = str(datetime.datetime.now())
	result = date + "\n\n"
	for pair in pairs:
		if len(pair) == 2:
			result = result + ("@%s is paired with @%s" % (pair[0], pair[1]))
		else:
			result = result + ("@%s is the odd one out. We'll get you next time, @%s" % (pair[0], pair[0]))
		result = result + "\n"
	return result

def listContainsOnly(aList, aName):
	for name in aList:
		if name != aName:
			print('listContainsOnly false')
			return False
	print('listContainsOnly true')
	return True

def removeNonAscii(text):
	return ''.join([i if ord(i) < 128 else ' ' for i in text])

def getDataset():
	checkDataFolder()
	subfolders = [ f.path for f in os.scandir('./data') if f.is_dir() ]
	if len(subfolders) == 0:
		print('No Datasets available.  You must create one first...')
		createDataset()
	i = 1
	for path in subfolders:
		print('%d: %s' % (i, os.path.basename(path)))
		i = i + 1
	print('C: Create new dataset...')
	print('')
	datasetIndex = input('Which dataset do you want to generate matches for? ')
	if datasetIndex == 'c' or datasetIndex == 'C':
		createDataset()
	dataset = subfolders[int(datasetIndex) - 1]
	print('Generating matches for %s' % (dataset))
	return dataset

def checkDataFolder():
	if not os.path.isdir('data'):
		os.mkdir('data')

def createDataset():
	datasetName = input('What is the new dataset called? ')
	if not os.path.isdir('data/' + datasetName):
		os.mkdir('data/' + datasetName)
		with open('data/' + datasetName + '/participants.txt', 'w') as outfile:
			outfile.write('// List your participant slackIDs (without the @ symbol) in this file, one per line.\r// You can list both name and slack ID to help in keeping the file up-to-date.\r// Only the text found after the last colon is used, ie: "Simon Clark:sclark"\r// For folks who want multiple matches per round, add a repeat count: "* 3"\r// Lines starting two slashes are ignored.\r// -------------------------------------------------\rSimon Clark : siclark\rJen Patil:jpatil\rGreedy Clark : grclark * 2\rcococlark\r// Introvert Clark : noclark')
		with open('data/' + datasetName + '/matchWeights.json', 'w') as outfile:
			outfile.write('{}')
		print("Dataset has been created for %s. Please add participants to the file ./data/%s/participants.txt, then run this script again." % (datasetName, datasetName))
	else:
		print("Dataset already exists for %s" % (datasetName))
	exit()

