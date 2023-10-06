import unittest
from src.circles import circle_area
from math import pi
#try to know, what might be happend by using circle_area
class TestCircleArea(unittest.TestCase):
  def test_area(self):
    # Test areas when radius >= 0
    self.assertAlmostEqual(circle_area(1), pi)
    self.assertAlmostEqual(circle_area(0), 0)
    self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)
    

  def test_values(self):
    # Make sure value errors are raised when necessary
    self.assertRaises(ValueError, circle_area, -2)

  def test_types(self):
    # Make sure type errors are raised when necessary
    self.assertRaises(TypeError, circle_area, 5 + 6j)
    self.assertRaises(TypeError, circle_area, "radius")
    
  def run_me():
    #run the class instead of executing with that ugly line...
    unittest.main(argv=[''], verbosity=2, exit=False) 
    


