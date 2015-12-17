import requests
from unittest import TestCase

from ppp_datamodel import Triple
from ppp_datamodel.communication import Response

class WikidataTestCase(TestCase):
    def testWikidataAnswers(self):
        r = requests.post('http://askplatyp.us:9000/core/', data='{"id": "", "language": "en", "trace": [], "measures": {}, "tree": {"type": "sentence", "value": "What is the birth date of Douglas Adams?"}}').json()
        r = list(filter(lambda x:not isinstance(x.tree, Triple),
                        map(Response.from_dict, r)))
        self.assertGreaterEqual(len(r), 1, r)
        got_actual_answer = False
        for o in r:
            if o.tree.type == 'list':
                for resource in o.tree.list:
                    if resource.type == 'resource' and resource.value == '1952-03-11':
                        got_actual_answer = True
        self.assertTrue(got_actual_answer, r)
