import json
import unittest
import test_utils as tu
import time


class TestxLandingCompanyDetails(unittest.TestCase):

    def setUp(self):
        # self.skipTest("-----")
        return

    def tearDown(self):
        return

    def get_prod_output(self, input):
        # prod
        tu.prod_ws.send(input)
        result_str = tu.prod_ws.recv()
        prod_output = json.loads(result_str)

        return prod_output

    def assert_landing_company_details(self, input, expected_data):
        landing_company_details = tu.send_and_receive_ws_x_authorize(input)
        expected_landing_company_details = self.get_prod_output(input)

        self.assertTrue(tu.compare_data(landing_company_details, expected_landing_company_details), "Unmatch result")

    # test landing company details - CR
    def test_landing_company_details_costarica(self):
        costarica = json.dumps({
            "landing_company_details": "costarica"

        })

        self.assert_landing_company_details(costarica, tu.expected_landing_company_details_costarica)

    # test landing company details - MX
    def test_landing_company_details_iom(self):
        iom = json.dumps({
            "landing_company_details": "iom"

        })

        self.assert_landing_company_details(iom, tu.expected_landing_company_details_iom)

    # test landing company details - MLT
    def test_landing_company_details_malta(self):
        malta = json.dumps({
            "landing_company_details": "malta"

        })

        self.assert_landing_company_details(malta, tu.expected_landing_company_details_malta)

    # test landing company details - MF
    def test_landing_company_details_maltainvest(self):
        maltainvest = json.dumps({
            "landing_company_details": "maltainvest"

        })

        self.assert_landing_company_details(maltainvest, tu.expected_landing_company_details_maltainvest)

    # test landing company details - virtual
    def test_landing_company_details_virtual(self):
        virtual = json.dumps({
            "landing_company_details": "virtual"

        })

        self.assert_landing_company_details(virtual, tu.expected_landing_company_details_virtual)

    # test landing company details - Japan
    def test_landing_company_details_japan(self):
        japan = json.dumps({
            "landing_company_details": "japan"

        })

        self.assert_landing_company_details(japan, tu.expected_landing_company_details_japan)

    # test landing company details - Japan virtual
    def test_landing_company_details_japan_virtual(self):
        japan_virtual = json.dumps({
            "landing_company_details": "japan-virtual"

        })

        self.assert_landing_company_details(japan_virtual, tu.expected_landing_company_details_japan_virtual)

    # test landing company details - vanuatu
    def test_landing_company_details_vanuatu(self):
        vanuatu = json.dumps({
            "landing_company_details": "vanuatu"

        })

        self.assert_landing_company_details(vanuatu, tu.expected_landing_company_details_vanuatu)

    # test landing company details - Champion
    def test_landing_company_details_champion(self):
        champion = json.dumps({
            "landing_company_details": "champion"

        })

        self.assert_landing_company_details(champion, tu.expected_landing_company_details_champion)

    # test landing company details - Champion virtual
    def test_landing_company_details_champion_virtual(self):
        champion_virtual = json.dumps({
            "landing_company_details": "champion-virtual"

        })

        self.assert_landing_company_details(champion_virtual, tu.expected_landing_company_details_champion_virtual)

    # test invalid landing company details should raise error
    def test_landing_company_details_invalid(self):
        landing_company_details = json.dumps({
            "landing_company_details": "invalid"

        })

        landing_company_details_invalid = tu.send_and_receive_ws_x_authorize(landing_company_details)

        self.assertTrue('error' in landing_company_details_invalid)
        self.assertTrue(
            'Input validation failed: landing_company_details' in landing_company_details_invalid['error']['message'])
