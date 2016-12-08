import unittest
#import copy # for deepcopy

def increment_dictionary_values(d, i):
  d = d.copy()
  for k,v in d.items():
    d[k] = v+i
  return d

class TestIncrementDictionaryValues(unittest.TestCase):

  def test_increment_dictionary_values(self):

    d = {'a': 1 }
    dd = increment_dictionary_values(d, 1)
    ddd = increment_dictionary_values(d, -1)
    self.assertEqual(dd['a'], 2)
    self.assertEqual(ddd['a'], 0)

if __name__ == '__main__':
  unittest.main()