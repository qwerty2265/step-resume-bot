from src import bot
from database import sqlite_db
from tests import test_utils
import unittest

if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.loadTestsFromTestCase(test_utils.TestFunctions)
    test_runner = unittest.TextTestRunner(verbosity=1)
    test_result = test_runner.run(test_suite)

    if test_result.wasSuccessful():
        try:
            sqlite_db.sqlite_start()
            bot.start_bot()
        except Exception as ex:
            print(ex)