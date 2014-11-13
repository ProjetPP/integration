import requests
from unittest import TestCase

from ppp_datamodel import Triple
from ppp_datamodel.communication import Response

class WikidataTestCase(TestCase):
    def testWikidataAnswers(self):
        r = requests.post('http://ppp.pony.ovh:9000/core/', data='{"id": "", "language": "en", "trace": [], "measures": {}, "tree": {"type": "sentence", "value": "What is the birth date of George Washington?"}}').json()
        r = list(filter(lambda x:not isinstance(x.tree, Triple),
                        map(Response.from_dict, r)))
        self.assertGreaterEqual(len(r), 1, r)
        for o in r:
            self.assertEqual(o.tree.type, 'resource')
            self.assertIn(o.tree.value, {'1732-02-22', '22/2/1732'})
