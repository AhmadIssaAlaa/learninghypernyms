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

