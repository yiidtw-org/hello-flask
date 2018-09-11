# -*- coding: utf-8 -*-
import unittest
from app import * 

class TestHello(unittest.TestCase):
    def test_hello(self):
       self.assertEqual("Hello DevOpsDay", hello()) 

if __name__ == '__main__':
    unittest.main()
