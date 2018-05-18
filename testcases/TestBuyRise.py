import unittest
import test_utils as tu
import json
import copy

test_data = \
    {
        "valid_parameter": [
            # Volatility indices
            ("R_10", "CALL", 5, "t"),
            ("R_25", "CALL", 15, "s"),
            ("R_50", "CALL", 2, "m"),
            ("R_75", "CALL", 3, "h"),
            ("R_100", "CALL", 1, "d"),
            # Major pairs
            ("frxAUDJPY", "CALL", 5, "t"),
            ("frxAUDUSD", "CALL", 15, "m"),
            ("frxEURAUD", "CALL", 3, "h"),
            ("frxEURCAD", "CALL", 7, "d"),
            # Minor pairs
            ("frxAUDCAD", "CALL", 3, "m"),
            ("frxAUDCHF", "CALL", 3, "h"),
            ("frxEURNZD", "CALL", 7, "d"),
        ],

        "invalid_parameter": [
            # Volatility indices
            ("R_10", "CALL", 4, "t", "OfferingsValidationError"),
            # Major pairs
            ("frxAUDJPY", "CALL", 1, "m", "OfferingsValidationError"),
            # Minor pairs
            ("frxAUDCAD", "CALL", 15, "s", "OfferingsValidationError")

        ],

    }

missing_parameter_message = \
    {"amount": "Input validation failed: amount",
     "basis": "Input validation failed: basis",
     "contract_type": "Input validation failed: contract_type",
     "currency": "Input validation failed: currency",
     "duration": "Missing required contract parameters (date_expiry or duration).",
     "duration_unit": "Trading is not offered for this duration.",
     "proposal": "Unrecognised request",
     "symbol": "Input validation failed: symbol"

     }

complete_rise_proposal = {"proposal": 1,
                          "amount": "10",
                          "basis": "payout",
                          "contract_type": "CALL",
                          "currency": "USD",
                          "duration": 5,
                          "duration_unit": "m",
                          "symbol": "R_100"}


def rise_test_template(*args):
    def rise_valid_proposal(self):
        self.assert_valid_proposal(*args)

    return rise_valid_proposal


def rise_test_invalid_template(*args):
    def rise_invalid_assert(self):
        self.assert_invalid_parameter(*args)

    return rise_invalid_assert


def rise_test_missing_template(*args):
    def rise_missing_assert(self):
        self.assert_missing_parameter(*args)

    return rise_missing_assert


class TestProposalRise(unittest.TestCase):

    def assert_valid_proposal(self, symbol, contract_type, duration, duration_unit):
        if not tu.trading_day(symbol):
            self.skipTest("Skipped test due to weekend")
        else:
            proposal = tu.proposal_call_put(symbol=symbol,
                                        contract_type=contract_type,
                                        duration=duration,
                                        duration_unit=duration_unit)

            tu.print_if_error(proposal)
            self.assertTrue('error' not in proposal)

    def assert_invalid_parameter(self, symbol, contract_type, duration, duration_unit, error_code):
        if not tu.trading_day(symbol):
            self.skipTest("Skipped test due to weekend")
        else:
            proposal = tu.proposal_call_put(symbol=symbol,
                                            contract_type=contract_type,
                                            duration=duration,
                                            duration_unit=duration_unit)

            self.assertTrue('error' in proposal)

            if error_code != proposal["error"]["code"]:
                tu.print_if_error(proposal)
            self.assertEqual(error_code, proposal["error"]["code"])

    def assert_missing_parameter(self, parameter_name):
        temp_complete_proposal = copy.deepcopy(complete_rise_proposal)
        temp_complete_proposal.pop(parameter_name)
        proposal = json.dumps(temp_complete_proposal)
        proposal_result = tu.send_and_receive_ws(proposal)
        self.assertEqual(missing_parameter_message[parameter_name], proposal_result["error"]["message"])


for scenario, test_cases in test_data.items():
    if scenario == "valid_parameter":
        for each_test_case_data in test_cases:
            symbol_d, contract_type_d, duration_d, duration_unit_d = each_test_case_data
            test_name = "test_{0}_{1}_{2}_{3}_{4}".format(scenario, symbol_d, contract_type_d, duration_d,
                                                          duration_unit_d)
            rise_test_case = rise_test_template(*each_test_case_data)
            setattr(TestProposalRise, test_name, rise_test_case)

    elif scenario == "invalid_parameter":
        for each_test_case_data in test_cases:
            symbol_d, contract_type_d, duration_d, duration_unit_d, error_code = each_test_case_data
            test_name = "test_{0}_{1}_{2}_{3}_{4}".format(scenario, symbol_d, contract_type_d, duration_d,
                                                          duration_unit_d)
            rise_invalid_test_case = rise_test_invalid_template(*each_test_case_data)
            setattr(TestProposalRise, test_name, rise_invalid_test_case)


for each_parameter in complete_rise_proposal:
    test_name = "test_missing_{0}_parameter".format(each_parameter)
    rise_missing_test_case = rise_test_missing_template(each_parameter)
    setattr(TestProposalRise, test_name, rise_missing_test_case)
