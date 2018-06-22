import unittest
import test_utils as tu


class TestBuyContractForex(unittest.TestCase):

    def setUp(self):
        # Duration:7d to make sure contract is sell-able and its end date is on trading day
        self.symbol = "frxEURJPY"
        self.symbol_name = tu.frx[self.symbol]
        self.duration = 7
        self.duration_unit = "d"
        self.end_date = tu.contract_end_date(self.duration)

        # Skip testing on weekend as forex market is closed
        if not tu.trading_day(self.symbol):
            self.skipTest("Skipped test due to weekend")

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

        expected_longcode = 'Win payout if {0} is strictly higher than entry spot at close on {1}.' \
            .format(self.symbol_name, self.end_date)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_put_contract(self):
        proposal = tu.proposal_call_put(symbol=self.symbol,
                                        contract_type="PUT",
                                        duration=self.duration,
                                        duration_unit=self.duration_unit)

        expected_longcode = 'Win payout if {0} is strictly lower than entry spot at close on {1}.' \
            .format(self.symbol_name, self.end_date)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_lower_contract(self):
        current_spot = tu.find_latest_tick(self.symbol)
        current_spot_formatted = "{:.3f}".format(current_spot)

        # use current_spot as absolute barrier
        proposal = tu.proposal_higher_lower(symbol=self.symbol,
                                            contract_type="PUT",
                                            duration=self.duration,
                                            duration_unit=self.duration_unit,
                                            barrier=current_spot)

        expected_longcode = 'Win payout if {0} is strictly lower than {1} at close on {2}.' \
            .format(self.symbol_name, current_spot_formatted, self.end_date)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_higher_contract(self):
        current_spot = tu.find_latest_tick(self.symbol)
        current_spot_formatted = "{:.3f}".format(current_spot)

        # use current_spot as absolute barrier
        proposal = tu.proposal_higher_lower(symbol=self.symbol,
                                            contract_type="CALL",
                                            duration=self.duration,
                                            duration_unit=self.duration_unit,
                                            barrier=current_spot)

        expected_longcode = 'Win payout if {0} is strictly higher than {1} at close on {2}.' \
            .format(self.symbol_name, current_spot_formatted, self.end_date)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_touch_contract(self):
        current_spot = tu.find_latest_tick(self.symbol)
        barrier = tu.abs_higher_barrier(current_spot, 3.5, 3)

        proposal = tu.proposal_touch_no_touch(symbol=self.symbol,
                                              contract_type="ONETOUCH",
                                              duration=self.duration,
                                              duration_unit=self.duration_unit,
                                              barrier=barrier)

        expected_longcode = 'Win payout if {0} touches {1} through close on {2}.' \
            .format(self.symbol_name, barrier, self.end_date)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_no_touch_contract(self):
        current_spot = tu.find_latest_tick(self.symbol)
        barrier = tu.abs_higher_barrier(current_spot, 0.5, 3)

        proposal = tu.proposal_touch_no_touch(symbol=self.symbol,
                                              contract_type="NOTOUCH",
                                              duration=self.duration,
                                              duration_unit=self.duration_unit,
                                              barrier=barrier)

        expected_longcode = 'Win payout if {0} does not touch {1} through close on {2}.' \
            .format(self.symbol_name, barrier, self.end_date)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_end_between_contract(self):
        current_spot = tu.find_latest_tick(self.symbol)
        barrier = tu.abs_higher_barrier(current_spot, 0.5, 3)
        barrier2 = tu.abs_lower_barrier2(current_spot, 0.5, 3)

        proposal = tu.proposal_in_out(symbol=self.symbol,
                                      contract_type="EXPIRYRANGE",
                                      duration=self.duration,
                                      duration_unit=self.duration_unit,
                                      barrier=barrier,
                                      barrier2=barrier2)

        expected_longcode = 'Win payout if {0} ends strictly between {1} to {2} at close on {3}.' \
            .format(self.symbol_name, barrier2, barrier, self.end_date)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_end_out_contract(self):
        current_spot = tu.find_latest_tick(self.symbol)
        barrier = tu.abs_higher_barrier(current_spot, 0.5, 3)
        barrier2 = tu.abs_lower_barrier2(current_spot, 0.5, 3)

        proposal = tu.proposal_in_out(symbol=self.symbol,
                                      contract_type="EXPIRYMISS",
                                      duration=self.duration,
                                      duration_unit=self.duration_unit,
                                      barrier=barrier,
                                      barrier2=barrier2)

        expected_longcode = 'Win payout if {0} ends outside {1} to {2} at close on {3}.' \
            .format(self.symbol_name, barrier2, barrier, self.end_date)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_stay_between_contract(self):
        current_spot = tu.find_latest_tick(self.symbol)
        barrier = tu.abs_higher_barrier(current_spot, 0.5, 3)
        barrier2 = tu.abs_lower_barrier2(current_spot, 0.5, 3)

        proposal = tu.proposal_in_out(symbol=self.symbol,
                                      contract_type="RANGE",
                                      duration=self.duration,
                                      duration_unit=self.duration_unit,
                                      barrier=barrier,
                                      barrier2=barrier2)

        expected_longcode = 'Win payout if {0} stays between {1} to {2} through close on {3}.' \
            .format(self.symbol_name, barrier2, barrier, self.end_date)

        self.assert_longcode(proposal, expected_longcode)

    def test_buy_goes_outside_contract(self):
        current_spot = tu.find_latest_tick(self.symbol)
        barrier = tu.abs_higher_barrier(current_spot, 23.4, 3)
        barrier2 = tu.abs_lower_barrier2(current_spot, 25.3, 3)

        proposal = tu.proposal_in_out(symbol=self.symbol,
                                      contract_type="UPORDOWN",
                                      duration=self.duration,
                                      duration_unit=self.duration_unit,
                                      barrier=barrier,
                                      barrier2=barrier2)

        expected_longcode = 'Win payout if {0} goes outside {1} to {2} through close on {3}.' \
            .format(self.symbol_name, barrier2, barrier, self.end_date)

        self.assert_longcode(proposal, expected_longcode)
