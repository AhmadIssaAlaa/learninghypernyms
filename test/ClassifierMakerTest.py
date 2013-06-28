# Bismilllahi-r-Rahmani-r-Rahim

import unittest
import numpy as np
from numpy import random
from StringIO import StringIO
from utils import testData

from coneexperiment.ClassifierMaker import ClassifierMaker

class ClassifierMakerTestCase(unittest.TestCase):
    def setUp(self):
        random.seed(1001)

    def testClassifierMakerNames(self):
        data, test_data, vectors = testData()
        maker = ClassifierMaker(vectors)
        names = maker.get_names()
        self.assertGreater(len(names), 0,
                           "Maker should have more than one classifier")

    def testClassifierMakerClassifiers(self):
        "Check that all classifiers that can be made are valid."
        data, test_data, vectors = testData()
        class_values = set(x[2] for x in data)

        maker = ClassifierMaker(vectors)
        names = maker.get_names()

        for name in names:
            classifier = maker.make(name)
            classifier.fit(data)
            results = classifier.predict(test_data)
            
            self.assertEqual(len(results), len(test_data))
            self.assertTrue(set(results) <= class_values)

            
