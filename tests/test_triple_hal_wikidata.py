import requests
from unittest import TestCase

from ppp_datamodel import Triple, Missing, Resource
from ppp_datamodel.communication import Response

class TripleHalWikidataTestCase(TestCase):
    def testTripleHalWikidata(self):
        r = requests.post('http://askplatyp.us:9000/core/', data='{"id": "", "language": "en", "trace": [], "measures": {}, "tree": {"type": "sentence", "value": "((The first cycles in an evolving graph, author, ?), birth date, ?)"}}').json()
        r = list(map(Response.from_dict, r))
        self.assertGreaterEqual(len(r), 2, r)
        got_actual_answer = False
        for o in r:
            if o.tree.type == 'resource':
                self.assertEqual(o.tree.value, '1938-01-10')
                got_actual_answer = True
            elif o.tree.type == 'list':
                self.assertIn('1938-01-10',
                        (x.value for x in o.tree.list))
                got_actual_answer = True
        self.assertTrue(got_actual_answer, r)

