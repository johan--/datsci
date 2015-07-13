# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 21:56:02 2015

@author: alex
"""

# Exploring UN Security Council Resolutions with NLTK

import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = 'Desktop/datsci/UN/corpus/unscr/'
scrs = PlaintextCorpusReader(corpus_root, '.*')
scrs.fileids()

# plots conditional frequency distributions of words across years
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4]) # separates the years out of the filenames for the X axis
    for fileid in scrs.fileids()
    for w in scrs.words(fileid)
    for target in ['genocide', 'sad'] # also looked at "sad", "cost", "urge", "condemn"
    if w.lower().startswith(target))

cfd.plot()

# authorizing missions
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4]) # separates the years out of the filenames for the X axis
    for fileid in scrs.fileids()
    for w in scrs.words(fileid)
    for target in ['authorize', 'mission', 'deploy'] 
    if w.lower().startswith(target))

cfd.plot()

# feelings by year
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4]) # separates the years out of the filenames for the X axis
    for fileid in scrs.fileids()
    for w in scrs.words(fileid)
    for target in ['sad', 'deplor', 'condemn', 'express'] 
    if w.lower().startswith(target))

cfd.plot()



