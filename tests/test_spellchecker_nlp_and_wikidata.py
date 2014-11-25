import requests
from unittest import TestCase

from ppp_datamodel import Triple
from ppp_datamodel.communication import Response

class SpellCheckerNlpWikidataTestCase(TestCase):
    def testSpellCheckerNlpWikidata(self):
        r = requests.post('http://ppp.pony.ovh:9000/core/', data='{"id": "", "language": "en", "trace": [], "measures": {}, "tree": {"type": "sentence", "value": "What is the birth daet of George Washington?"}}').json()
        r = list(filter(lambda x:not isinstance(x.tree, Triple),
                        map(Response.from_dict, r)))
        self.assertGreaterEqual(len(r), 1, r)
        got_actual_answer = False
        for o in r:
            self.assertEqual(o.tree.type, 'resource')
            self.assertIn(o.tree.value,
                    {'What is the birth date of George Washington',
                     '1732-02-22', '22/2/1732'})
            if o.tree.value in {'1732-02-22', '22/2/1732'}:
                got_actual_answer = True
        self.assertTrue(got_actual_answer, r)

