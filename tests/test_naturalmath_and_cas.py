import requests
from unittest import TestCase

from ppp_datamodel import Sentence, Resource
from ppp_datamodel.communication import Response

class NaturalmathAndCasTestCase(TestCase):
    def testNaturalmathAndCas(self):
        r = requests.post('http://askplatyp.us:9000/core/', data='{"id": "", "language": "en", "trace": [], "measures": {}, "tree": {"type": "sentence", "value": "derivate cos(x)"}}').json()
        self.assertIn(Resource('-sin(x)'), (x.tree for x in r))
