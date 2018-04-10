import unittest
import test_utils as tu
import json
import time


class TestBuyContract(unittest.TestCase):

    def setUp(self):
        self.symbol = "R_100"
        self.duration = "3"
        self.duration_unit = "m"

        self.symbol_name = tu.vol[self.symbol]
        self.contract_duration = self.duration + " " + tu.duration[self.duration_unit]

    def tearDown(self):
        # selling contract to avoid hitting maximum number of open contract
        tu.sell_last_bought_contract()
        return

    def assert_longcode(self, proposal, expected_longcode):
        result_longcode = tu.buy(proposal)
        self.assertEqual(expected_longcode, result_longcode)

    def test_buy_call_contract(self):
        proposal = tu.proposal_call_put(symbol=self.symbol,
                                        contract_type="CALL",
                                        duration=self.duration,
                                        duration_unit=self.duration_unit)

        expected_longcode = 'Win payout if {0} is strictly higher than entry spot at {1} ' \
                            'after contract start time.' \
            .format(self.symbol_name, self.contract_duration)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_put_contract(self):
        proposal = tu.proposal_call_put(symbol=self.symbol,
                                        contract_type="PUT",
                                        duration=self.duration,
                                        duration_unit=self.duration_unit)
        expected_longcode = 'Win payout if {0} is strictly lower than entry spot at {1} ' \
                            'after contract start time.' \
            .format(self.symbol_name, self.contract_duration)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_lower_contract(self):
        current_spot = tu.find_latest_tick(self.symbol)
        current_spot_formatted = "{:.2f}".format(current_spot)

        # use current_spot as absolute barrier
        proposal = tu.proposal_higher_lower(symbol=self.symbol,
                                            contract_type="PUT",
                                            duration=self.duration,
                                            duration_unit=self.duration_unit,
                                            barrier=current_spot)
        expected_longcode = 'Win payout if {0} is strictly lower than {1} ' \
                            'at {2} after contract start time.' \
            .format(self.symbol_name, current_spot_formatted, self.contract_duration)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_higher_contract(self):
        current_spot = tu.find_latest_tick(self.symbol)
        current_spot_formatted = "{:.2f}".format(current_spot)

        # use current_spot as absolute barrier
        proposal = tu.proposal_higher_lower(symbol=self.symbol,
                                            contract_type="CALL",
                                            duration=self.duration,
                                            duration_unit=self.duration_unit,
                                            barrier=current_spot)
        expected_longcode = 'Win payout if {0} is strictly higher than {1} ' \
                            'at {2} after contract start time.' \
            .format(self.symbol_name, current_spot_formatted, self.contract_duration)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_touch_contract(self):
        current_spot = tu.find_latest_tick(self.symbol)
        abs_barrier = tu.abs_higher_barrier(current_spot, 23.50, 2)

        proposal = tu.proposal_touch_no_touch(symbol=self.symbol,
                                              contract_type="ONETOUCH",
                                              duration=self.duration,
                                              duration_unit=self.duration_unit,
                                              barrier=abs_barrier)
        expected_longcode = 'Win payout if {0} touches {1} through {2} after contract start time.' \
            .format(self.symbol_name, abs_barrier, self.contract_duration)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_no_touch_contract(self):
        current_spot = tu.find_latest_tick(self.symbol)
        abs_barrier = tu.abs_higher_barrier(current_spot, 5.50, 2)

        proposal = tu.proposal_touch_no_touch(symbol=self.symbol,
                                              contract_type="NOTOUCH",
                                              duration=self.duration,
                                              duration_unit=self.duration_unit,
                                              barrier=abs_barrier)

        expected_longcode = 'Win payout if {0} does not touch {1} through {2} after contract start time.' \
            .format(self.symbol_name, abs_barrier, self.contract_duration)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_end_between_contract(self):
        proposal = tu.proposal_in_out(symbol=self.symbol,
                                      contract_type="EXPIRYRANGE",
                                      duration=self.duration,
                                      duration_unit=self.duration_unit,
                                      barrier="+3.50",
                                      barrier2="-4.50")

        expected_longcode = 'Win payout if {0} ends strictly between entry spot minus 4.50 to ' \
                            'entry spot plus 3.50 at {1} after contract start time.' \
            .format(self.symbol_name, self.contract_duration)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_end_out_contract(self):
        proposal = tu.proposal_in_out(symbol=self.symbol,
                                      contract_type="EXPIRYMISS",
                                      duration=self.duration,
                                      duration_unit=self.duration_unit,
                                      barrier="+3.50",
                                      barrier2="-4.5")

        expected_longcode = 'Win payout if {0} ends outside entry spot minus 4.50 to entry spot ' \
                            'plus 3.50 at {1} after contract start time.' \
            .format(self.symbol_name, self.contract_duration)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_stay_between_contract(self):
        proposal = tu.proposal_in_out(symbol=self.symbol,
                                      contract_type="RANGE",
                                      duration=self.duration,
                                      duration_unit=self.duration_unit,
                                      barrier="+3.5",
                                      barrier2="-4.5")
        expected_longcode = 'Win payout if {0} stays between entry spot minus 4.50 and entry spot ' \
                            'plus 3.50 through {1} after contract start time.' \
            .format(self.symbol_name, self.contract_duration)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_goes_outside_contract(self):
        proposal = tu.proposal_in_out(symbol=self.symbol,
                                      contract_type="UPORDOWN",
                                      duration=self.duration,
                                      duration_unit=self.duration_unit,
                                      barrier="+23.4",
                                      barrier2="-25.6")
        expected_longcode = 'Win payout if {0} goes outside entry spot minus 25.60 and entry ' \
                            'spot plus 23.40 through {1} after contract start time.' \
            .format(self.symbol_name, self.contract_duration)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_asian_down_contract(self):
        proposal = tu.proposal_asian_up_down(self.symbol, "ASIAND")
        expected_longcode = 'Win payout if the last tick of {} is strictly lower than the ' \
                            'average of the 5 ticks.'.format(self.symbol_name)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_asian_up_contract(self):
        proposal = tu.proposal_asian_up_down(self.symbol, "ASIANU")
        expected_longcode = 'Win payout if the last tick of {} is strictly higher than the ' \
                            'average of the 5 ticks.'.format(self.symbol_name)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_digit_match_contract(self):
        proposal = tu.proposal_digit(self.symbol, "DIGITMATCH")
        expected_longcode = 'Win payout if the last digit of {} is 5 after 5 ticks.' \
            .format(self.symbol_name)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_digit_diff_contract(self):
        proposal = tu.proposal_digit(self.symbol, "DIGITDIFF")
        expected_longcode = 'Win payout if the last digit of {} is not 5 after 5 ticks.' \
            .format(self.symbol_name)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_digit_over_contract(self):
        proposal = tu.proposal_digit(self.symbol, "DIGITOVER")
        expected_longcode = 'Win payout if the last digit of {} is strictly higher than 5 ' \
                            'after 5 ticks.'.format(self.symbol_name)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_digit_under_contract(self):
        proposal = tu.proposal_digit(self.symbol, "DIGITUNDER")
        expected_longcode = 'Win payout if the last digit of {} is strictly lower than 5 ' \
                            'after 5 ticks.'.format(self.symbol_name)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_digit_even_contract(self):
        proposal = tu.proposal_digit_even_odd(self.symbol, "DIGITEVEN")
        expected_longcode = 'Win payout if the last digit of {} is even after 5 ticks.' \
            .format(self.symbol_name)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_digit_odd_contract(self):
        proposal = tu.proposal_digit_even_odd(self.symbol, "DIGITODD")
        expected_longcode = 'Win payout if the last digit of {} is odd after 5 ticks.' \
            .format(self.symbol_name)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_lookback_high_close_contract(self):
        proposal = tu.proposal_lookback(self.symbol, "LBFLOATPUT")
        expected_longcode = 'Win USD 1 times {}\'s high minus close over the next 1 minute.' \
            .format(self.symbol_name)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_lookback_close_low_contract(self):
        proposal = tu.proposal_lookback(self.symbol, "LBFLOATCALL")
        expected_longcode = 'Win USD 1 times {}\'s close minus low over the next 1 minute.' \
            .format(self.symbol_name)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_lookback_high_low_contract(self):
        proposal = tu.proposal_lookback(self.symbol, "LBHIGHLOW")
        expected_longcode = 'Win USD 1 times {}\'s high minus low over the next 1 minute.' \
            .format(self.symbol_name)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_reset_call_contract(self):
        # temporarily avoid rate limit
        time.sleep(6)
        # Reset contract is set as No business for now!
        contract_type = "RESETCALL"

        buy = json.dumps({"buy": "1",
                          "price": 100,
                          "parameters": {
                              "amount": 10,
                              "basis": "payout",
                              "currency": "USD",
                              "duration": 4,
                              "duration_unit": "t",
                              "contract_type": contract_type,
                              "symbol": self.symbol}
                          })
        buy_result_js = tu.send_and_receive_ws(buy)

        expected_error_message = 'This trade is temporarily unavailable.'
        error_message = buy_result_js['error']['message']

        self.assertEqual(error_message, expected_error_message)
