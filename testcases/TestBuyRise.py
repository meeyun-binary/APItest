import unittest
import test_utils as tu

test_data = \
    {"valid_proposal":       [("R_100", "CALL", 5, "t"),
                              ("R_100", "CALL", 15, "s"),
                              ("R_100", "CALL", 2, "m"),
                              ("R_100", "CALL", 3, "h"),
                              ("R_100", "CALL", 1, "d"),
                              ("frxAUDJPY", "CALL", 5, "t"),
                              ("frxAUDJPY", "CALL", 15, "m"),
                              ("frxAUDJPY", "CALL", 3, "h"),
                              ("frxAUDJPY", "CALL", 7, "d"),
                              ],
     }


def rise_test_template(*args):
    def foo(self):
        self.assert_proposal(*args)
    return foo


class TestBuyRise(unittest.TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return

    def assert_proposal(self, symbol, contract_type, duration, duration_unit):
        # Skip testing on weekend as forex market is closed
        if not tu.trading_day(symbol):
            self.skipTest("Skipped test due to weekend")
        else:
            proposal = tu.proposal_call_put(symbol=symbol,
                                            contract_type=contract_type,
                                            duration=duration,
                                            duration_unit=duration_unit)

            self.assertTrue('error' not in proposal)


for market, test_cases in test_data.items():
    for each_test_case_data in test_cases:
        symbol_d, contract_type_d, duration_d, duration_unit_d = each_test_case_data
        test_name = "test_{0}_{1}_{2}_{3}".format(symbol_d, contract_type_d, duration_d, duration_unit_d)
        rise_test_case = rise_test_template(*each_test_case_data)
        setattr(TestBuyRise, test_name, rise_test_case)