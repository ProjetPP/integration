import json
import requests
from unittest import TestCase

from ppp_datamodel import Triple
from ppp_datamodel.communication import Response

class WikidataTestCase(TestCase):
    def testWikidataAnswers(self):
        r = requests.post('http://askplatyp.us:9000/core/', data=json.dumps({"id": "", "language": "fr", "trace": [], "measures": {}, "tree": {"type": "sentence", "value": "Quelle est la date de naissance d’Obama ?"}})).json()
        r = list(filter(lambda x:not isinstance(x.tree, Triple),
                        map(Response.from_dict, r)))
        self.assertGreaterEqual(len(r), 1, r)
        got_answer = False
        for o in r:
            if o.tree.type == 'resource':
                self.assertEqual(o.tree.value, '1961-08-04')
                got_answer = True
        self.assertTrue(got_answer, r)
