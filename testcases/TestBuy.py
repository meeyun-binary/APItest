import json
import unittest
import test_utils as tu
import time


class TestBuyContract(unittest.TestCase):
    def setUp(self):
        self.symbol = "R_100"
        # add sleep time to avoid hitting rate limit
        time.sleep(4)

    def tearDown(self):
        # selling contract to avoid hitting maximum number of open contract
        tu.sell_last_bought_contract()

    def buy_and_compare_longcode(self, proposal, expected_longcode):
        print(proposal)
        id = proposal['proposal']['id']

        json_buy = json.dumps({"buy": id,
                               "price": 100
                               })
        result_buy = tu.send_and_receive_ws(json_buy)
        print(result_buy)
        longcode = result_buy['buy']['longcode']

        self.assertEqual(longcode, expected_longcode)

    def test_buy_call_contract(self):
        proposal = tu.proposal_call_put(self.symbol, "CALL")
        expected_longcode = 'Win payout if Volatility 100 Index is strictly higher than entry spot at 1 minute after ' \
                            'contract start time.'

        self.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_put_contract(self):
        proposal = tu.proposal_call_put(self.symbol, "PUT")
        expected_longcode = 'Win payout if Volatility 100 Index is strictly lower than entry spot at 1 minute after ' \
                            'contract start time.'

        self.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_lower_contract(self):
        current_spot = tu.find_latest_tick(self.symbol)

        # use current_spot as absolute barrier
        proposal = tu.proposal_higher_lower(self.symbol, "PUT", current_spot)
        expected_longcode = 'Win payout if Volatility 100 Index is strictly lower than %s at 1 minute after contract' \
                            ' start time.' % current_spot

        self.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_higher_contract(self):
        current_spot = tu.find_latest_tick(self.symbol)

        # use current_spot as absolute barrier
        proposal = tu.proposal_higher_lower(self.symbol, "CALL", current_spot)
        expected_longcode = 'Win payout if Volatility 100 Index is strictly higher than %s at 1 minute after ' \
                            'contract start time.' % current_spot

        self.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_touch_contract(self):
        proposal = tu.proposal_touch_no_touch(self.symbol, "ONETOUCH", "+3.5")
        expected_longcode = 'Win payout if Volatility 100 Index touches entry spot plus 3.50 through 3 minutes ' \
                            'after contract start time.'

        self.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_no_touch_contract(self):
        proposal = tu.proposal_touch_no_touch(self.symbol, "NOTOUCH", "+3.5")
        expected_longcode = 'Win payout if Volatility 100 Index does not touch entry spot plus 3.50 through 3 ' \
                            'minutes after contract start time.'

        self.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_end_between_contract(self):
        proposal = tu.proposal_in_out(self.symbol, "EXPIRYRANGE", "+3.5", "-4.5")
        expected_longcode = 'Win payout if Volatility 100 Index ends strictly between entry spot minus 4.50 to ' \
                            'entry spot plus 3.50 at 3 minutes after contract start time.'

        self.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_end_out_contract(self):
        proposal = tu.proposal_in_out(self.symbol, "EXPIRYMISS", "+3.5", "-4.5")
        expected_longcode = 'Win payout if Volatility 100 Index ends outside entry spot minus 4.50 to entry spot ' \
                            'plus 3.50 at 3 minutes after contract start time.'

        self.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_stay_between_contract(self):
        proposal = tu.proposal_in_out(self.symbol, "RANGE", "+3.5", "-4.5")
        expected_longcode = 'Win payout if Volatility 100 Index stays between entry spot minus 4.50 and entry spot ' \
                            'plus 3.50 through 3 minutes after contract start time.'

        self.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_goes_outside_contract(self):
        proposal = tu.proposal_in_out(self.symbol, "UPORDOWN", "+23.4", "-25.6")
        expected_longcode = 'Win payout if Volatility 100 Index goes outside entry spot minus 25.60 and entry ' \
                            'spot plus 23.40 through 3 minutes after contract start time.'

        self.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_asian_down_contract(self):
        proposal = tu.proposal_asian_up_down(self.symbol, "ASIAND")
        expected_longcode = 'Win payout if the last tick of Volatility 100 Index is strictly lower than the ' \
                            'average of the 5 ticks.'

        self.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_asian_up_contract(self):
        proposal = tu.proposal_asian_up_down(self.symbol, "ASIANU")
        expected_longcode = 'Win payout if the last tick of Volatility 100 Index is strictly higher than the ' \
                            'average of the 5 ticks.'

        self.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_digit_match_contract(self):
        proposal = tu.proposal_digit(self.symbol, "DIGITMATCH")
        expected_longcode = 'Win payout if the last digit of Volatility 100 Index is 5 after 5 ticks.'

        self.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_digit_diff_contract(self):
        proposal = tu.proposal_digit(self.symbol, "DIGITDIFF")
        expected_longcode = 'Win payout if the last digit of Volatility 100 Index is not 5 after 5 ticks.'

        self.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_digit_over_contract(self):
        proposal = tu.proposal_digit(self.symbol, "DIGITOVER")
        expected_longcode = 'Win payout if the last digit of Volatility 100 Index is strictly higher than 5 ' \
                            'after 5 ticks.'

        self.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_digit_under_contract(self):
        proposal = tu.proposal_digit(self.symbol, "DIGITUNDER")
        expected_longcode = 'Win payout if the last digit of Volatility 100 Index is strictly lower than 5 ' \
                            'after 5 ticks.'

        self.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_digit_even_contract(self):
        proposal = tu.proposal_digit_even_odd(self.symbol, "DIGITEVEN")
        expected_longcode = 'Win payout if the last digit of Volatility 100 Index is even after 5 ticks.'

        self.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_digit_odd_contract(self):
        proposal = tu.proposal_digit_even_odd(self.symbol, "DIGITODD")
        expected_longcode = 'Win payout if the last digit of Volatility 100 Index is odd after 5 ticks.'

        self.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_lookback_high_close_contract(self):
        proposal = tu.proposal_lookback(self.symbol, "LBFLOATPUT")
        expected_longcode = 'Win USD 1 times Volatility 100 Index\'s high minus close over the next 1 minute.'

        self.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_lookback_close_low_contract(self):
        proposal = tu.proposal_lookback(self.symbol, "LBFLOATCALL")
        expected_longcode = 'Win USD 1 times Volatility 100 Index\'s close minus low over the next 1 minute.'

        self.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_lookback_high_low_contract(self):
        proposal = tu.proposal_lookback(self.symbol, "LBHIGHLOW")
        expected_longcode = 'Win USD 1 times Volatility 100 Index\'s high minus low over the next 1 minute.'

        self.buy_and_compare_longcode(proposal, expected_longcode)
