import pytest
import unittest
from base.driver_config import DriverConfig

class RunCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       cls.driver =  DriverConfig().driver_init()
       # cls.login_page =

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def runCase(self):

