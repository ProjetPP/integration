import requests
from unittest import TestCase

from ppp_datamodel import Triple
from ppp_datamodel.communication import Response

class OracleTestCase(TestCase):
    def testOracleAnswers(self):
        r = requests.post('http://askplatyp.us:9000/core/', data='{"id": "", "language": "en", "trace": [], "measures": {}, "tree": {"type": "sentence", "value": "What is your website?"}}').json()
        r = list(filter(lambda x:not isinstance(x.tree, Resource),
                        map(Response.from_dict, r)))
        self.assertGreaterEqual(len(r), 1, r)
        for o in r:
            self.assertEqual(o.tree.type, 'http://projetpp.github.io/')
