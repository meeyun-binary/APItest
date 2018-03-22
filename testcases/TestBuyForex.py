import json
import unittest
import test_utils as tu





class TestBuyContractForex(unittest.TestCase):
    def setUp(self):
        # Skip testing on weekend as forex market is closed
        if not tu.trading_day():
            self.skipTest("Skipped test due to weekend")

        self.symbol = "frxAUDJPY"
        self.duration = 7
        self.end_date = tu.contract_end_date(self.duration)

    def tearDown(self):
        # selling contract to avoid hitting maximum number of open contract
        tu.sell_last_bought_contract()
        return

    def test_buy_call_contract(self):
        proposal = tu.proposal_call_put(symbol=self.symbol,
                                        contract_type="CALL",
                                        duration=self.duration,
                                        duration_unit="d")

        expected_longcode = 'Win payout if AUD/JPY is strictly higher than entry spot at close on ' \
                            '{}.'.format(self.end_date)

        tu.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_put_contract(self):
        proposal = tu.proposal_call_put(symbol=self.symbol,
                                        contract_type="PUT",
                                        duration=self.duration,
                                        duration_unit="d")

        expected_longcode = 'Win payout if AUD/JPY is strictly lower than entry spot at close on ' \
                            '{}.'.format(self.end_date)

        tu.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_lower_contract(self):
        current_spot = tu.find_latest_tick(self.symbol)
        current_spot_formatted = "{:.3f}".format(current_spot)

        # use current_spot as absolute barrier
        proposal = tu.proposal_higher_lower(symbol=self.symbol,
                                            contract_type="PUT",
                                            duration=self.duration,
                                            duration_unit="d",
                                            barrier=current_spot)

        expected_longcode = 'Win payout if AUD/JPY is strictly lower than {} at close on ' \
                            '{}.'.format(current_spot_formatted, self.end_date)

        tu.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_higher_contract(self):
        current_spot = tu.find_latest_tick(self.symbol)
        current_spot_formatted = "{:.3f}".format(current_spot)

        # use current_spot as absolute barrier
        proposal = tu.proposal_higher_lower(symbol=self.symbol,
                                            contract_type="CALL",
                                            duration=self.duration,
                                            duration_unit="d",
                                            barrier=current_spot)

        expected_longcode = 'Win payout if AUD/JPY is strictly higher than {} at close on ' \
                            '{}.'.format(current_spot_formatted, self.end_date)

        tu.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_touch_contract(self):
        current_spot = tu.find_latest_tick(self.symbol)
        barrier = tu.abs_higher_barrier(current_spot, 3.5, 3)

        proposal = tu.proposal_touch_no_touch(symbol=self.symbol,
                                              contract_type="ONETOUCH",
                                              duration=self.duration,
                                              duration_unit="d",
                                              barrier=barrier)

        expected_longcode = 'Win payout if AUD/JPY touches {} through close on ' \
                            '{}.'.format(barrier, self.end_date)

        tu.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_no_touch_contract(self):
        current_spot = tu.find_latest_tick(self.symbol)
        barrier = tu.abs_higher_barrier(current_spot, 0.5, 3)

        proposal = tu.proposal_touch_no_touch(symbol=self.symbol,
                                              contract_type="NOTOUCH",
                                              duration=self.duration,
                                              duration_unit="d",
                                              barrier=barrier)

        expected_longcode = 'Win payout if AUD/JPY does not touch {} through close on ' \
                            '{}.'.format(barrier, self.end_date)

        tu.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_end_between_contract(self):
        current_spot = tu.find_latest_tick(self.symbol)
        barrier = tu.abs_higher_barrier(current_spot, 0.5, 3)
        barrier2 = tu.abs_lower_barrier2(current_spot, 0.5, 3)

        proposal = tu.proposal_in_out(symbol=self.symbol,
                                      contract_type="EXPIRYRANGE",
                                      duration=self.duration,
                                      duration_unit="d",
                                      barrier=barrier,
                                      barrier2=barrier2)

        expected_longcode = 'Win payout if AUD/JPY ends strictly between {} to {} at close on ' \
                            '{}.'.format(barrier2, barrier, self.end_date)

        tu.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_end_out_contract(self):
        current_spot = tu.find_latest_tick(self.symbol)
        barrier = tu.abs_higher_barrier(current_spot, 0.5, 3)
        barrier2 = tu.abs_lower_barrier2(current_spot, 0.5, 3)

        proposal = tu.proposal_in_out(symbol=self.symbol,
                                      contract_type="EXPIRYMISS",
                                      duration=self.duration,
                                      duration_unit="d",
                                      barrier=barrier,
                                      barrier2=barrier2)

        expected_longcode = 'Win payout if AUD/JPY ends outside {} to {} at close on ' \
                            '{}.'.format(barrier2, barrier, self.end_date)

        tu.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_stay_between_contract(self):
        current_spot = tu.find_latest_tick(self.symbol)
        barrier = tu.abs_higher_barrier(current_spot, 0.5, 3)
        barrier2 = tu.abs_lower_barrier2(current_spot, 0.5, 3)

        proposal = tu.proposal_in_out(symbol=self.symbol,
                                      contract_type="RANGE",
                                      duration=self.duration,
                                      duration_unit="d",
                                      barrier=barrier,
                                      barrier2=barrier2)

        expected_longcode = 'Win payout if AUD/JPY stays between {} to {} through close on ' \
                            '{}.'.format(barrier2, barrier, self.end_date)

        tu.buy_and_compare_longcode(proposal, expected_longcode)

    def test_buy_goes_outside_contract(self):
        current_spot = tu.find_latest_tick(self.symbol)
        barrier = tu.abs_higher_barrier(current_spot, 23.4, 3)
        barrier2 = tu.abs_lower_barrier2(current_spot, 25.3, 3)

        proposal = tu.proposal_in_out(symbol=self.symbol,
                                      contract_type="UPORDOWN",
                                      duration=self.duration,
                                      duration_unit="d",
                                      barrier=barrier,
                                      barrier2=barrier2)

        expected_longcode = 'Win payout if AUD/JPY goes outside {} to {} through close on ' \
                            '{}.'.format(barrier2, barrier, self.end_date)

        tu.buy_and_compare_longcode(proposal, expected_longcode)


