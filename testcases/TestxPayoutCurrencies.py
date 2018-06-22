import unittest
import test_utils as tu
import json


class TestxPayoutCurrencies(unittest.TestCase):

    def setUp(self):
        tu.log_out()

    def tearDown(self):
        return

    def test_payout_currencies(self):
        expected_payout_currencies = [
            "AUD",
            "BCH",
            "BTC",
            "DAI",
            "ETH",
            "EUR",
            "GBP",
            "LTC",
            "USD"
        ]

        payout_currencies = json.dumps({
            "payout_currencies": 1
        })

        tu.log_out()  # log out so it will return full available payout currencies
        payout_currencies_reponse = tu.send_and_receive_ws_x_authorize(payout_currencies)

        payout_currencies_list = payout_currencies_reponse["payout_currencies"]

        self.assertTrue(set(expected_payout_currencies) == set(payout_currencies_list))
        self.assertTrue("error" not in payout_currencies_reponse)
