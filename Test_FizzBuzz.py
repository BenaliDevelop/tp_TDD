import unittest
from fizzbuzz import *

class Test_FizzBuzz (unittest.TestCase):

    def setUp(self):
        self.instance=fizzbuzz()

    def test_affiche_sans_param(self):
        self.assertEqual(self.instance.affiche(), "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee1617Fizz.....9798FizzBuzz")