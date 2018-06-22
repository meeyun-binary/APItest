import unittest
import test_utils as tu
import json


class TestLandingCompany(unittest.TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return

    def assert_landing_company(self, input, expected_data):
        landing_company_input = tu.send_and_receive_ws_x_authorize(input)
        expected_landing_company = tu.convert_py_json_output(expected_data)

        self.assertTrue(tu.compare_data(landing_company_input, expected_landing_company), "Unmatch result")

    def test_landing_company_indonesia(self):
        indonesia = json.dumps({
            "landing_company": "id"
        })

        self.assert_landing_company(indonesia, tu.expected_landing_company_id)

    def test_landing_company_uk(self):
        uk = json.dumps({
            "landing_company": "gb"
        })

        self.assert_landing_company(uk, tu.expected_landing_company_gb)

    def test_landing_company_be(self):
        belgium = json.dumps({
            "landing_company": "be"
        })

        self.assert_landing_company(belgium, tu.expected_landing_company_be)

    def test_landing_company_es(self):
        spain = json.dumps({
            "landing_company": "es"
        })

        self.assert_landing_company(spain, tu.expected_landing_company_es)

    def test_landing_company_china(self):
        china = json.dumps({
            "landing_company": "cn"
        })

        self.assert_landing_company(china, tu.expected_landing_company_cn)

    def test_landing_company_canada(self):
        canada = json.dumps({
            "landing_company": "ca"
        })

        self.assert_landing_company(canada, tu.expected_landing_company_ca)
