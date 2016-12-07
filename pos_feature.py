#!/usr/bin/env python3

import sys

# first, we need a feature extraction function
# this should return a dictionary, made of up attribute:value data

def pos_features(word, nf):
	features = {}

	# fill in the details for this line, so that last_letter contains the last letter of 'word'
	# hint: strings are lists; and you can access from the end of a list with negative values
	# add as many features as you like
	vowel = "уеыаоэиюөәү"
	features = {
		"nf": nf.lower(),
		"suffix3": word[-3:],
		"suffix2": word[-2:],
		"count": str(len(word)),
		"capital": str(word[0].islower()),
		"isupper": str(word.isupper()),
		"istitle": str(word.istitle()),
		"isdigit": str(word.isdigit()),
		# "vowel": str(word[-1] in vowel)
	}

	return features

for line in open(sys.argv[1]):
	line = line.strip() # remove newline from the end of the line

	if not len(line): #skip blank lines
		print()
		continue

	label, word, nf  = line.split("\t") # get the label and word out
	features = pos_features(word, nf) # do feature extraction

	# build a list of name:value strings, for the features
	crfsuite_features = []
	for feature_name in features:
		crfsuite_features.append(feature_name + '_' + features[feature_name])
	# output the label, a tab, and then all the features with tabs between them
	print(label + "\t" + "\t".join(crfsuite_features))
