import json
import unittest
import test_utils as tu
import datetime
import operator
import time
from numpy import isclose as isclose


class TestxExchangeRate(unittest.TestCase):

    def setUp(self):
        # list all the available currencies
        self.expected_target_currencies = ["USD", "AUD", "BCH", "BTC", "DAI", "ETH", "EUR", "GBP", "JPY", "LTC"]
        return

    def tearDown(self):
        return

    def send_and_receive_exchange(self, base_currency):
        input = json.dumps({
            "exchange_rates": 1,
            "base_currency": base_currency

        })

        usd_exchange = tu.send_and_receive_ws_x_authorize(input)

        return usd_exchange

    def assert_exchange_rate_API(self, base_currency):
        # remove base currency from self.expected_target_currencies
        self.expected_target_currencies.remove(base_currency)

        usd_exchange = self.send_and_receive_exchange(base_currency)

        target_currencies = list(usd_exchange["exchange_rates"]["rates"])

        # make sure base currency is return correctly
        self.assertEqual(usd_exchange["exchange_rates"]["base_currency"], base_currency)

        # make sure base to all other currencies are returned
        self.assertTrue(set(target_currencies) == set(self.expected_target_currencies))

        # make sure no error returned
        self.assertTrue('error' not in usd_exchange)

    # test exchange currency by using USD as base currency
    def test_exchange_rate_base_USD(self):
        base_currency = "USD"
        self.assert_exchange_rate_API(base_currency)

    # test exchange currency by using AUD as base currency
    def test_exchange_rate_base_AUD(self):
        base_currency = "AUD"
        self.assert_exchange_rate_API(base_currency)

    # test exchange currency by using BCH as base currency
    def test_exchange_rate_base_BCH(self):
        base_currency = "BCH"
        self.assert_exchange_rate_API(base_currency)

    # test exchange currency by using BTC as base currency
    def test_exchange_rate_base_BTC(self):
        base_currency = "BTC"
        self.assert_exchange_rate_API(base_currency)

    # test exchange currency by using DAI as base currency
    def test_exchange_rate_base_DAI(self):
        base_currency = "DAI"
        self.assert_exchange_rate_API(base_currency)

    # test exchange currency by using ETH as base currency
    def test_exchange_rate_base_ETH(self):
        base_currency = "ETH"
        self.assert_exchange_rate_API(base_currency)

    # test exchange currency by using EUR as base currency
    def test_exchange_rate_base_EUR(self):
        base_currency = "EUR"
        self.assert_exchange_rate_API(base_currency)

    # test exchange currency by using GBP as base currency
    def test_exchange_rate_base_GBP(self):
        base_currency = "GBP"
        self.assert_exchange_rate_API(base_currency)

    # test exchange currency by using JPY as base currency
    def test_exchange_rate_base_JPY(self):
        base_currency = "JPY"
        self.assert_exchange_rate_API(base_currency)

    # test exchange currency by using LTC as base currency
    def test_exchange_rate_base_LTC(self):
        base_currency = "LTC"
        self.assert_exchange_rate_API(base_currency)

    def check_rate_changes(self, base_currency):
        first_output = self.send_and_receive_exchange(base_currency)
        time.sleep(2)
        second_output = self.send_and_receive_exchange(base_currency)

        first_output_rates = first_output["exchange_rates"]["rates"]
        sorted_first_output = sorted(first_output_rates.items(), key=operator.itemgetter(1))

        second_output_rates = second_output["exchange_rates"]["rates"]
        sorted_second_output = sorted(second_output_rates.items(), key=operator.itemgetter(1))

        return (sorted_first_output, sorted_second_output)

    def filter_currency(self, data):
        # use these currency because they are frequently change
        currencies_to_keep = ("BTC", "BCH", "ETH", "LTC")
        item_list = [e for e in data]
        new_list = []
        for item in currencies_to_keep:
            new = [x for x in item_list if item in x]
            new_list.append(new)

        return new_list

    # test exchange rate should change during weekdays
    def test_exchange_rate_keep_changing(self):
        base_currency = "USD"
        first_output, second_output = self.check_rate_changes(base_currency)
        check_trading_day = datetime.datetime.today().weekday()
        if check_trading_day > 4:
            #TODO exclude japan
            # self.assertTrue(tu.compare_data(first_output, second_output), "Exchange rates should not change")
            print("skip test due to weekend")

        else:
            filtered_first_output = self.filter_currency(first_output)
            filtered_second_output = self.filter_currency(second_output)

            # create a list to store the value when currencies do not change
            same_rates = [item for item in filtered_first_output if item in filtered_second_output]

            # repeat five times if the rate is not changing
            try_times = 1
            while len(same_rates) == 4 and try_times <= 5:
                print("Retry number: ", try_times)
                first_output, second_output = self.check_rate_changes(base_currency)
                filtered_first_output = self.filter_currency(first_output)
                filtered_second_output = self.filter_currency(second_output)

                same_rates = [item for item in filtered_first_output if item in filtered_second_output]
                print(same_rates)
                print(len(same_rates))
                try_times += 1

            # there should be at least one currency has changing rate
            self.assertTrue(len(same_rates) < 4, "Rates do not change, please check")

    # test the returned rate must be accurate
    def test_exchange_rate_accuracy(self):
        # hard code exchange rates
        expected_rates = [
            ["BTC", "0.00015438"],
            ["BCH", "0.00118947"],
            ["ETH", "0.00200894"],
            ["LTC", "0.01053601"],
            ["GBP", "0.75"],
            ["EUR", "0.86"],
            ["DAI", "1.01"],
            ["AUD", "1.34"],
            ["JPY", "110.00"]
        ]

        first_output = self.send_and_receive_exchange("USD")
        first_output_rates = first_output["exchange_rates"]["rates"]
        sorted_first_output = sorted(first_output_rates.items(), key=operator.itemgetter(1))

        # if exchange rate difference is >20%, the currency will be added to the list
        possible_inaccurate_rate = [a for [a, b], [x, y] in zip(expected_rates, sorted_first_output) if
                                    not isclose(float(b), float(y), rtol=0.2)]

        self.assertEqual(len(possible_inaccurate_rate), 0)
        # print the currencies which is possibly has incorrect exchange rate (<20% difference)
        if len(possible_inaccurate_rate) != 0:
            print("Possible inaccurate rate: ", possible_inaccurate_rate)
