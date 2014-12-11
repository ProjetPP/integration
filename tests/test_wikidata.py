import requests
from unittest import TestCase

from ppp_datamodel import Triple
from ppp_datamodel.communication import Response

class WikidataTestCase(TestCase):
    def testWikidataTriple(self):
        r = requests.post('http://ppp.pony.ovh:9000/core/', data='{"id": "", "language": "en", "trace": [], "measures": {}, "tree": {"type": "triple", "subject": {"type": "resource", "value": "Douglas Adams"}, "object": {"type": "missing"}, "predicate": {"type": "resource", "value": "birth date"}}}').json()
        r = list(filter(lambda x:not isinstance(x.tree, Triple),
                        map(Response.from_dict, r)))
        self.assertGreaterEqual(len(r), 1, r)
        for o in r:
            self.assertEqual(o.tree.type, 'resource')
            self.assertEqual(o.tree.value, '1952-03-11')

    def testWikidataSentence(self):
        r = requests.post('http://ppp.pony.ovh:9000/core/', data='{"id": "", "language": "en", "trace": [], "measures": {}, "tree": {"type": "sentence", "value": "Douglas Adams"}}').json()
        r = list(filter(lambda x:not isinstance(x.tree, Triple),
                        map(Response.from_dict, r)))
        self.assertGreaterEqual(len(r), 1, r)
        got_actual_answer = True
        for o in r:
            if o.tree.type == 'resource' and hasattr(o.tree, 'value_type') and o.tree.value_type == 'wikibase-entity' and o.tree.value == 'Douglas Adams':
                got_actual_answer = True
        self.assertTrue(got_actual_answer, r)