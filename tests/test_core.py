import unittest,copy,json
from sqlite_collation_collision import run
DEMO={'keys': ['A', 'a', 'A ', 'é', 'É', None, None]}
class DomainTests(unittest.TestCase):
 def test_ascii_and_unicode(self):
  x=run(DEMO)['collations'];self.assertEqual(x['NOCASE']['rejected_indices'],[1]);self.assertEqual(x['RTRIM']['rejected_indices'],[2])
 def test_null_is_not_unique_key(self):
  x=run({'keys':[None,None]});self.assertEqual(x['collations']['BINARY']['accepted_indices'],[0,1])
 def test_no_trim_in_binary(self):
  self.assertEqual(run(DEMO)['collations']['BINARY']['rejected_indices'],[])
