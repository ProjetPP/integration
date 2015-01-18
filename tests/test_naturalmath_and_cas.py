import requests
from unittest import TestCase

from ppp_datamodel import Sentence, Resource, MathLatexResource
from ppp_datamodel.communication import Response

class NaturalmathAndCasTestCase(TestCase):
    def testNaturalmathAndCas(self):
        r = requests.post('http://localhost:9000/core/', data='{"id": "", "language": "en", "trace": [], "measures": {}, "tree": {"type": "sentence", "value": "derivate cos(x)"}}').json()
        r = [Response.from_dict(x) for x in r]
        self.assertIn(r'- \sin{\left (x \right )}',
                {x.tree.value for x in r if isinstance(x.tree, Resource)})
