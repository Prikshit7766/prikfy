import unittest
from cnt_code_to_name import sym_to_name
from data import sym_cnt_dict as data_dict


class TestCCnt(unittest.TestCase):

    def test_sym_to_name(self):
        self.assertIn('GB', data_dict)
        self.assertIn('PL', data_dict)
        self.assertIn('AU', data_dict)
        self.assertIn('BM', data_dict)
        self.assertNotIn('wrong-symbol', data_dict)
        self.assertEqual(sym_to_name('GB'), 'United Kingdom')
        self.assertEqual(sym_to_name('pl'), 'Poland')
        self.assertEqual(sym_to_name('Au'), 'Australia')
        self.assertEqual(sym_to_name('bM'), 'Bermuda')
        self.assertIsNone(sym_to_name('wrong-symbol'))
        with self.assertRaises(ValueError):
            sym_to_name(1)
        with self.assertRaises(ValueError):
            sym_to_name(['a', 'b', 'c'])


if __name__ == '__main__':
    unittest.main()
