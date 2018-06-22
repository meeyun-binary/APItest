import unittest
import test_utils as tu
import json


class TestxAssetIndex(unittest.TestCase):

    def setUp(self):
        tu.log_out()
        return

    def tearDown(self):
        return

    def assert_asset_index(self, input, expected_output_):
        output = tu.send_and_receive_ws_x_authorize(input)

        # to convert python structure same as json output
        expected_output = tu.convert_py_json_output(expected_output_)

        self.assertTrue(tu.compare_data(expected_output, output))

    # test asset index without defining landing company
    def test_asset_index(self):
        asset_index = json.dumps({
            "asset_index": 1
        })

        self.assert_asset_index(asset_index, tu.expected_asset_index)

    # test asset index for MX
    def test_asset_index_iom(self):
        asset_index = json.dumps({
            "asset_index": 1,
            "landing_company": "iom"

        })

        self.assert_asset_index(asset_index, tu.expected_asset_index_iom)
    
    # test asset index for MLT
    def test_asset_index_malta(self):
        asset_index = json.dumps({
            "asset_index": 1,
            "landing_company": "malta"

        })

        self.assert_asset_index(asset_index, tu.expected_asset_index_malta)

    # test asset index for MF
    def test_asset_index_maltainvest(self):
        asset_index = json.dumps({
            "asset_index": 1,
            "landing_company": "maltainvest"

        })

        self.assert_asset_index(asset_index, tu.expected_asset_index_maltainvest)

    # test asset index for CR
    def test_asset_index_costarica(self):
        asset_index = json.dumps({
            "asset_index": 1,
            "landing_company": "costarica"

        })

        self.assert_asset_index(asset_index, tu.expected_asset_index_costarica)
   
    # test asset index for virtual account
    def test_asset_index_virtual(self):
        asset_index = json.dumps({
            "asset_index": 1,
            "landing_company": "virtual"

        })

        self.assert_asset_index(asset_index, tu.expected_asset_index_virtual)

    # test asset index for Japan
    def test_asset_index_japan(self):
        asset_index = json.dumps({
            "asset_index": 1,
            "landing_company": "japan"

        })

        self.assert_asset_index(asset_index, tu.expected_asset_index_japan)

    # test asset index for Japan virtual account
    def test_asset_index_japan_virtual(self):
        asset_index = json.dumps({
            "asset_index": 1,
            "landing_company": "japan-virtual"

        })

        self.assert_asset_index(asset_index, tu.expected_asset_index_japan_virtual)

    # test asset index for vanuatu
    def test_asset_index_vanuatu(self):
        asset_index = json.dumps({
            "asset_index": 1,
            "landing_company": "vanuatu"

        })

        self.assert_asset_index(asset_index, tu.expected_asset_index_vanuatu)

    # test asset index for Champion
    def test_asset_index_champion(self):
        asset_index = json.dumps({
            "asset_index": 1,
            "landing_company": "champion"

        })

        self.assert_asset_index(asset_index, tu.expected_asset_index_champion)

    # test asset index for Champion virtual
    def test_asset_index_champion_virtual(self):
        asset_index = json.dumps({
            "asset_index": 1,
            "landing_company": "champion-virtual"

        })

        self.assert_asset_index(asset_index, tu.expected_asset_index_champion_virtual)

    # test invalid landing company should raise error
    def test_asset_index_invalid_landing_company(self):
        asset_index = json.dumps({
            "asset_index": 1,
            "landing_company": "invalid"

        })

        asset_index_invalid = tu.send_and_receive_ws_x_authorize(asset_index)

        self.assertTrue('error' in asset_index_invalid)
        self.assertTrue('Input validation failed: landing_company' in asset_index_invalid['error']['message'])
