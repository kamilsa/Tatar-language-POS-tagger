#!/bin/bash
python pos_feature.py train.conll > train.input;
python pos_feature.py test.conll > test.input;
crfsuite learn -m my.model -p feature.possible_states=1 -p c2=0.4  train.input
crfsuite tag -q -m my.model -t test.input
