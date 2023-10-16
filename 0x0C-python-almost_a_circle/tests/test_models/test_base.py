#!/usr/bin/python3
"""
#George Maroa <mgm.engineeringtie847@gmail.com>

#####################
module: base.py
#####################
"""


import sys
import unittest
import inspect
import io
import pep8
from contextlib import redirect_stdout
from models.base import Base


class TestSquare(unittest.TestCase):
    """tests Base class' methods"""

    @classmethod
    def setUpClass(cls):
        """for the doc tests"""
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_pep8_conformance_base(self):
        """Tests if the base.py file conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base(self):
        """Tests if test_base.py file conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests if module docstring documentation exists"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests if the class docstring documentation exist"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests if methods docstring documntation exist"""
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)
