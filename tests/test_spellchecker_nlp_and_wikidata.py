import requests
from unittest import TestCase

from ppp_datamodel import Triple
from ppp_datamodel.communication import Response

class SpellCheckerNlpWikidataTestCase(TestCase):
    def testSpellCheckerNlpWikidata(self):
        r = requests.post('http://askplatyp.us:9000/core/', data='{"id": "", "language": "en", "trace": [], "measures": {}, "tree": {"type": "sentence", "value": "What is the birth daet of Douglas Adams?"}}').json()
        r = list(filter(lambda x:not isinstance(x.tree, Triple),
                        map(Response.from_dict, r)))
        self.assertGreaterEqual(len(r), 1, r)
        got_actual_answer = False
        for o in r:
            self.assertIn(o.tree.type, {'resource', 'sentence'})
            if o.tree.type == 'resource':
                self.assertEqual(o.tree.value, '1952-03-11')
                got_actual_answer = True
            else:
                self.assertEqual(o.tree.value,
                        'What is the birth date of Douglas Adams?')
        self.assertTrue(got_actual_answer, r)
