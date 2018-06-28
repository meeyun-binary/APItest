import unittest
import test_utils as tu
import json
import pprint


class TestxContractFor(unittest.TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return

    def remove_non_deterministic_element(self, data):
        barrier_list = ['barrier', 'high_barrier', 'low_barrier']
        forward_start_list = ['close', 'date', 'open']
        contracts_for_list = ['close', 'hit_count', 'open', 'spot']

        for available_item in range(len(data['contracts_for']['available'])):
            # to remove barrier
            for bl in barrier_list:
                if bl in data['contracts_for']['available'][available_item]:
                    data['contracts_for']['available'][available_item].pop(bl, None)

            # to remove element in forward_starting_options
            if 'forward_starting_options' in data['contracts_for']['available'][available_item]:
                for item_forward in range(
                        len(data['contracts_for']['available'][available_item]['forward_starting_options'])):
                    for fsl in forward_start_list:
                        data['contracts_for']['available'][available_item]['forward_starting_options'][
                            item_forward].pop(fsl, None)

        for cfl in contracts_for_list:
            data['contracts_for'].pop(cfl, None)

        return data

    def remove_multibarrier_non_deterministic_element(self, data):
        trading_period_list = ['epoch', 'date']
        contracts_for_list = ['close', 'hit_count', 'open', 'spot']

        for available_item in range(len(data['contracts_for']['available'])):
            # to remove available_barriers
            data['contracts_for']['available'][available_item].pop('available_barriers', None)

            # to remove element in trading_period
            for tpl in trading_period_list:
                # print(available_item)
                # print(len(data['contracts_for']['available']))
                # print(data['contracts_for']['available'][0]['trading_period']['date_expiry'])

                data['contracts_for']['available'][available_item]['trading_period']['date_expiry'].pop(tpl, None)
                data['contracts_for']['available'][available_item]['trading_period']['date_start'].pop(tpl, None)

        for cfl in contracts_for_list:
            data['contracts_for'].pop(cfl, None)

        return data

    def assert_contracts_for(self, input, expected):
        output = tu.send_and_receive_ws_x_authorize(input)
        processed_output = self.remove_non_deterministic_element(output)

        self.assertTrue(tu.compare_data(processed_output, expected))

    # test CR contracts_for - vol
    def test_contracts_for_vol_cr(self):
        input = json.dumps({
            "contracts_for": "R_50",
            "currency": "USD",
            "product_type": "basic",
            "landing_company": "costarica"
        })

        expected = tu.convert_py_json_output(tu.expected_contracts_for_vol_cr)
        processed_expected = self.remove_non_deterministic_element(expected)
        self.assert_contracts_for(input, processed_expected)

    # test CR contracts_for - forex
    def test_contracts_for_forex_cr(self):
        input = json.dumps({
            "contracts_for": "frxAUDJPY",
            "currency": "USD",
            "product_type": "basic",
            "landing_company": "costarica"
        })

        expected = tu.convert_py_json_output(tu.expected_contracts_for_forex_cr)
        processed_expected = self.remove_non_deterministic_element(expected)
        self.assert_contracts_for(input, processed_expected)

    # test mx contracts_for - vol
    def test_contracts_for_vol_iom(self):
        input = json.dumps({
            "contracts_for": "R_100",
            "currency": "USD",
            "product_type": "basic",
            "landing_company": "iom"
        })

        expected = tu.convert_py_json_output(tu.expected_contracts_for_vol_iom)
        processed_expected = self.remove_non_deterministic_element(expected)
        self.assert_contracts_for(input, processed_expected)

    # test mx contracts_for - forex
    def test_contracts_for_forex_iom(self):
        input = json.dumps({
            "contracts_for": "frxAUDJPY",
            "currency": "USD",
            "product_type": "basic",
            "landing_company": "iom"
        })

        output = tu.send_and_receive_ws_x_authorize(input)

        self.assertTrue('error' in output)
        self.assertEqual(output['error']['message'], 'Offering is unavailable on this symbol.')

    # test mlt contracts_for - vol
    def test_contracts_for_vol_malta(self):
        input = json.dumps({
            "contracts_for": "R_100",
            "currency": "USD",
            "product_type": "basic",
            "landing_company": "malta"
        })

        expected = tu.convert_py_json_output(tu.expected_contracts_for_vol_malta)
        processed_expected = self.remove_non_deterministic_element(expected)
        self.assert_contracts_for(input, processed_expected)

    # test mlt contracts_for - forex
    def test_contracts_for_forex_malta(self):
        input = json.dumps({
            "contracts_for": "frxAUDJPY",
            "currency": "USD",
            "product_type": "basic",
            "landing_company": "malta"
        })

        output = tu.send_and_receive_ws_x_authorize(input)

        self.assertTrue('error' in output)
        self.assertEqual(output['error']['message'], 'Offering is unavailable on this symbol.')

    # test mf contracts_for - forex
    def test_contracts_for_forex_maltainvest(self):
        input = json.dumps({
            "contracts_for": "frxAUDJPY",
            "currency": "USD",
            "product_type": "basic",
            "landing_company": "maltainvest"
        })

        expected = tu.convert_py_json_output(tu.expected_contracts_for_forex_maltainvest)
        processed_expected = self.remove_non_deterministic_element(expected)
        self.assert_contracts_for(input, processed_expected)

    # test mlt contracts_for - vol
    def test_contracts_for_vol_maltainvest(self):
        input = json.dumps({
            "contracts_for": "R_100",
            "currency": "USD",
            "product_type": "basic",
            "landing_company": "maltainvest"
        })

        output = tu.send_and_receive_ws_x_authorize(input)

        self.assertTrue('error' in output)
        self.assertEqual(output['error']['message'], 'Offering is unavailable on this symbol.')

    # test virtual contracts_for - forex
    def test_contracts_for_forex_virtual(self):
        input = json.dumps({
            "contracts_for": "frxAUDJPY",
            "currency": "USD",
            "product_type": "basic",
            "landing_company": "virtual"
        })

        expected = tu.convert_py_json_output(tu.expected_contracts_for_forex_virtual)
        processed_expected = self.remove_non_deterministic_element(expected)
        self.assert_contracts_for(input, processed_expected)

    # test vanuatu contracts_for - forex
    def test_contracts_for_forex_vanuatu(self):
        input = json.dumps({
            "contracts_for": "frxAUDJPY",
            "currency": "USD",
            "product_type": "basic",
            "landing_company": "vanuatu"
        })

        expected = tu.convert_py_json_output(tu.expected_contracts_for_forex_vanuatu)
        processed_expected = self.remove_non_deterministic_element(expected)
        self.assert_contracts_for(input, processed_expected)

    # test vanuatu contracts_for - vol
    def test_contracts_for_vol_vanuatu(self):
        input = json.dumps({
            "contracts_for": "R_100",
            "currency": "USD",
            "product_type": "basic",
            "landing_company": "vanuatu"
        })

        output = tu.send_and_receive_ws_x_authorize(input)

        self.assertTrue('error' in output)
        self.assertEqual(output['error']['message'], 'Offering is unavailable on this symbol.')

    # test contracts_for - multibarrier forex cr
    def test_contracts_for_forex_cr_multibarrier(self):
        input = json.dumps({
            "contracts_for": "frxAUDJPY",
            "currency": "USD",
            "product_type": "multi_barrier",
            "landing_company": "costarica"
        })

        output = tu.send_and_receive_ws_x_authorize(input)
        processed_output = self.remove_multibarrier_non_deterministic_element(output)

        expected = tu.convert_py_json_output(tu.expected_contracts_for_mb_forex_cr)
        processed_expected = self.remove_multibarrier_non_deterministic_element(expected)
        self.assertTrue(tu.compare_data(processed_output, processed_expected))

    # test contracts_for - multibarrier vol cr
    def test_contracts_for_vol_cr_multibarrier(self):
        input = json.dumps({
            "contracts_for": "R_100",
            "currency": "USD",
            "product_type": "multi_barrier",
            "landing_company": "costarica"
        })

        output = tu.send_and_receive_ws_x_authorize(input)

        self.assertTrue('error' in output)
        self.assertEqual(output['error']['message'], 'Offering is unavailable on this symbol.')

    # test contracts_for - multibarrier vol mx
    def test_contracts_for_vol_iom_multibarrier(self):
        input = json.dumps({
            "contracts_for": "R_100",
            "currency": "USD",
            "product_type": "multi_barrier",
            "landing_company": "iom"
        })

        output = tu.send_and_receive_ws_x_authorize(input)

        self.assertTrue('error' in output)
        self.assertEqual(output['error']['message'], 'Offering is unavailable on this symbol.')

    # test contracts_for - multibarrier forex mf
    def test_contracts_for_forex_mf_multibarrier(self):
        input = json.dumps({
            "contracts_for": "frxAUDJPY",
            "currency": "USD",
            "product_type": "multi_barrier",
            "landing_company": "maltainvest"
        })

        output = tu.send_and_receive_ws_x_authorize(input)
        processed_output = self.remove_multibarrier_non_deterministic_element(output)

        expected = tu.convert_py_json_output(tu.expected_contracts_for_mb_forex_mf)
        processed_expected = self.remove_multibarrier_non_deterministic_element(expected)
        self.assertTrue(tu.compare_data(processed_output, processed_expected))
