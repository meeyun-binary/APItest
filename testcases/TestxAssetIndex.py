import json
import unittest
import test_utils as tu


class TestAssetIndex(unittest.TestCase):
    """Compare the Asset Index result with Production"""

    def setUp(self):
        return

    def tearDown(self):
        return

    def compare(self, input):
        # prod
        json_data = json.dumps(input)
        tu.prod_ws.send(json_data)
        result_str = tu.prod_ws.recv()
        result_prod = json.loads(result_str)

        # qa
        json_data = json.dumps(input)
        result_qa = tu.send_and_receive_ws_x_authorize(json_data)

        self.assertEqual(result_qa, result_prod)

    def test_asset_index(self):
        input = {
            "asset_index": 1
        }

        self.compare(input)

    # test asset index for MX
    def test_asset_index_iom(self):
        input = {
            "asset_index": 1,
            "landing_company": "iom"

        }

        self.compare(input)

    # test asset index for MLT
    def test_asset_index_malta(self):
        input = {
            "asset_index": 1,
            "landing_company": "malta"

        }

        self.compare(input)

    # test asset index for MF
    def test_asset_index_maltainvest(self):
        input = {
            "asset_index": 1,
            "landing_company": "maltainvest"

        }

        self.compare(input)

    # test asset index for CR
    def test_asset_index_costarica(self):
        input = {
            "asset_index": 1,
            "landing_company": "costarica"

        }

        self.compare(input)

    # test asset index for virtual account
    def test_asset_index_virtual(self):
        input = {
            "asset_index": 1,
            "landing_company": "virtual"

        }

        self.compare(input)

    # test asset index for Japan
    def test_asset_index_japan(self):
        input = {
            "asset_index": 1,
            "landing_company": "japan"

        }

        self.compare(input)

    # test asset index for Japan virtual account
    def test_asset_index_japan_virtual(self):
        input = {
            "asset_index": 1,
            "landing_company": "japan-virtual"

        }

        self.compare(input)

    # test asset index for vanuatu
    def test_asset_index_vanuatu(self):
        input = {
            "asset_index": 1,
            "landing_company": "vanuatu"

        }

        self.compare(input)

    # test asset index for Champion
    def test_asset_index_champion(self):
        input = {
            "asset_index": 1,
            "landing_company": "champion"

        }

        self.compare(input)

    # test asset index for Champion virtual
    def test_asset_index_champion_virtual(self):
        input = {
            "asset_index": 1,
            "landing_company": "champion-virtual"

        }

        self.compare(input)

    # test invalid landing company should raise error
    def test_asset_index_invalid_landing_company(self):
        asset_index = json.dumps({
            "asset_index": 1,
            "landing_company": "invalid"

        })

        asset_index_invalid = tu.send_and_receive_ws_x_authorize(asset_index)

        self.assertTrue('error' in asset_index_invalid)
        self.assertTrue('Input validation failed: landing_company' in asset_index_invalid['error']['message'])
