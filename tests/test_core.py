import unittest
from cgpa_calculator.cgpa_calc import CGPACalculator

class TestCGPACalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = CGPACalculator()

    def test_add_course(self):
        self.calculator.add_course("CSE110", 4.0, 3)
        self.assertEqual(len(self.calculator.courses), 1)

    def test_calculate_cgpa(self):
        self.calculator.add_course("CSE110", 4.0, 3)
        self.calculator.add_course("CSE370", 3.7, 3)
        self.assertAlmostEqual(self.calculator.calculate_cgpa(), 3.85, places=2)

if __name__ == "__main__":
    unittest.main()
