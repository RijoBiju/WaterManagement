from source.water import Water
from source.calculations import get_ratio_total, get_ratio_of_number, income_tax_calculation
from source.allot import Allot
from source.apartment import Apartment
import unittest

class TestCases(unittest.TestCase):

    def test_water_used(self):
        water_usage = Water.water_used(3, 10)
        self.assertEqual(water_usage, 900)

    def test_water_cost(self):
        water_cost = Water.water_cost('270.0', '1')
        self.assertEqual(water_cost, 270)

    def test_get_ratio_total(self):
        self.assertEqual(get_ratio_total('3:7'), (10, ['3', '7']))

    def test_get_ratio_of_number(self):
        self.assertEqual(get_ratio_of_number('900', '3:7'), ['270.0', '630.0'])

    def test_income_tax_calculation(self):
        self.assertEqual(income_tax_calculation(1500, [(2, 500), (3, 1000), (5, 1500), (8, 3000)]), 4000)

    def test_categorize(self):
        allot = Allot()
        self.assertEqual(allot.categorize(['ALLOT_WATER', '2', '3:7']), ('GUEST', 3, '3:7'))

if __name__=='__main__':
    unittest.main()