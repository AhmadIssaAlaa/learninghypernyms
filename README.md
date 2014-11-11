*Bismillahi-r-Rahmani-r-Rahim*

In the Name of God, the Merciful, the Compassionate

Learning to Distinguish Hypernyms and Co-Hyponyms
=================================================

This repository contains code used in the COLING paper with the above
title. The purpose is to attempt to learn relationships between words,
for example that *animal* is a hypernym of *cat*. This repository
allows you to run experiments for both supervised and unsupervised
approaches to this task.

Datasets
--------

The repository also contains the datasets used in our experiments, in
JSON format. These are in the data folder.

The datafiles created from the BLESS dataset are BLESS_coord.json and BLESS_ent-pairs.json - coord refers to pairs where existence of a coordinate relationship in BLESS is labelled 1 and existence of some other relationship (hyponymy, hypernymy, meronymy, random) is labelled 0.  In ent-pairs a hypernym relationship e.g. robin ISA bird is labelled 1 [robin,bird,1] whereas existence of some other relationship (hyponymy, co-hyponymy, meronymy, random) is labelled 0

The other datafiles are created from WordNet.  All of the words also occur in our dump of wikipedia over 100 times.  Each word is only allowed to occur once in each position (left/right) of a relationship.

In entpairs, a direct hypernym relationship is labelled 1 whereas other relationships (hyponymy and co-hyponymy) are labelled 0.  In coordpairs, a co-hyponym relationship is labelled 1 whereas other realtionships (direct hyponymy and direct hypernymy) are labelled 0.

However, the results reported in our experiments were actually using entpairs2_wiki100 and coordpairs2_wiki100.  In these sets, indirect hypernymy (i.e., any entailment) is included in hypernymy and indirect hyponymy is included in hyponymy.  In other words [robin,animal,1] may exist in the entpairs2_wiki100 set.  One of [robin,animal,0] or [animal,robin,0] may exist in the coordpairs2_wiki100 set.  However, none of these pairings/labellings will exist in entpairs_wiki100 or coordpairs_wiki10  One of [robin,animal,0] or [animal,robin,0] may exist in the coordpairs2_wiki100 set.  However, none of these pairings/labellings will exist in entpairs_wiki100 or coordpairs_wiki100.

All of the datasets are balanced so that there are the same number of positive and negative examples of each relationship.  Where more than 1 relationship is included in the negative examples, these examples are also balanced between the different relationships.  


Getting Started
---------------

Download the code or clone the git repository:

    git clone https://github.com/SussexCompSem/confusionmetrics.git

Install dependencies (Numpy, Scipy and our confusionmetrics module):

    sudo apt-get install -qq python-numpy python-scipy
    sudo pip install -U pytest scikit-learn
    sudo pip install -r requirements.txt

Check that the installation is working by running the tests:

    python setup.py test

Experiments are configured by editing the file `entailment.cfg`. An
example experiment is provided in the unit test data folder. To run
experiments:

    python -m coneexperiment.EntailmentSuite test_data/entailment.cfg

Running this creates a file `test_data/unittest/analysis.csv`
containing results of the experiment.

Word vectors are contained in a file whose format should match that of
`test_data/nouns-deps-small-head.mi`: each line is of format

    word/POS_TAG f1 n1 f2 n2 ...

where each `fi` is a feature name (string) and each `ni` is a count
for that feature.

