import requests
from unittest import TestCase

from ppp_datamodel import Triple, Missing, Resource
from ppp_datamodel.communication import Response

class TripleWikidataTestCase(TestCase):
    def testTripleWikidata(self):
        r = requests.post('http://ppp.pony.ovh:9000/core/', data='{"id": "", "language": "en", "trace": [], "measures": {}, "tree": {"type": "sentence", "value": "(Douglas Adams, birth date, ?)"}}').json()
        r = list(filter(lambda x:not isinstance(x.tree, Triple),
                        map(Response.from_dict, r)))
        self.assertGreaterEqual(len(r), 2, r)
        got_actual_answer = False
        for o in r:
            self.assertIn(o.tree.type, {'resource', 'triple'})
            if o.tree.type == 'resource':
                self.assertEqual(o.tree.value, '1952-03-11')
                got_actual_answer = True
            else:
                self.assertEqual(o.tree, Triple(
                    Resource('Douglas Adams'),
                    Resource('birth date'),
                    Missing()))
        self.assertTrue(got_actual_answer, r)
