import unittest
import test_utils as tu
import json


class TestLandingCompany(unittest.TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return

    def test_indonesia(self):
        indonesia = json.dumps({
            "landing_company": "id"
        })
        landing_company_id = tu.send_and_receive_ws(indonesia)

        # remember to convert empty dict {} to None, else, result will fail ( {}!=None )
        expected_id = {
            "echo_req": {
                "landing_company": "id"
            },
            "landing_company": {
                "financial_company": {
                    "address": None,
                    "country": "Costa Rica",
                    "has_reality_check": 0,
                    "legal_allowed_contract_categories": [
                        "asian",
                        "callput",
                        "digits",
                        "endsinout",
                        "staysinout",
                        "touchnotouch",
                        "lookback",
                        "highlowticks",
                        "reset"
                    ],
                    "legal_allowed_currencies": [
                        "AUD",
                        "BCH",
                        "BTC",
                        "ETH",
                        "EUR",
                        "GBP",
                        "LTC",
                        "USD"
                    ],
                    "legal_allowed_markets": [
                        "commodities",
                        "forex",
                        "indices",
                        # "stocks",
                        "volidx"
                    ],
                    "legal_default_currency": "USD",
                    "name": "Binary (C.R.) S.A.",
                    "shortcode": "costarica"
                },
                "gaming_company": {
                    "address": None,
                    "country": "Costa Rica",
                    "has_reality_check": 0,
                    "legal_allowed_contract_categories": [
                        "asian",
                        "callput",
                        "digits",
                        "endsinout",
                        "staysinout",
                        "touchnotouch",
                        "lookback",
                        "highlowticks",
                        "reset"
                    ],
                    "legal_allowed_currencies": [
                        "AUD",
                        "BCH",
                        "BTC",
                        "ETH",
                        "EUR",
                        "GBP",
                        "LTC",
                        "USD"
                    ],
                    "legal_allowed_markets": [
                        "commodities",
                        "forex",
                        "indices",
                        # "stocks",
                        "volidx"
                    ],
                    "legal_default_currency": "USD",
                    "name": "Binary (C.R.) S.A.",
                    "shortcode": "costarica"
                },
                "id": "id",
                "mt_financial_company": {
                    "address": [
                        "Govant Building",
                        "Port Vila",
                        "P.O. Box 1276",
                        "Vanuatu",
                        "Republic of Vanuatu"
                    ],
                    "country": "Republic of Vanuatu",
                    "has_reality_check": 0,
                    "legal_allowed_contract_categories": [
                        "callput"
                    ],
                    "legal_allowed_currencies": [
                        "USD"
                    ],
                    "legal_allowed_markets": [
                        "forex"
                    ],
                    "legal_default_currency": "USD",
                    "name": "Binary (V) Ltd",
                    "shortcode": "vanuatu"
                },
                "mt_gaming_company": {
                    # "address": {},
                    "address": None,
                    "country": "Costa Rica",
                    "has_reality_check": 0,
                    "legal_allowed_contract_categories": [
                        "asian",
                        "callput",
                        "digits",
                        "endsinout",
                        "staysinout",
                        "touchnotouch",
                        "lookback",
                        "highlowticks",
                        "reset"
                    ],
                    "legal_allowed_currencies": [
                        "AUD",
                        "BCH",
                        "BTC",
                        "ETH",
                        "EUR",
                        "GBP",
                        "LTC",
                        "USD"
                    ],
                    "legal_allowed_markets": [
                        "commodities",
                        "forex",
                        "indices",
                        # "stocks",
                        "volidx"
                    ],
                    "legal_default_currency": "USD",
                    "name": "Binary (C.R.) S.A.",
                    "shortcode": "costarica"
                },
                "name": "Indonesia",
                "virtual_company": "virtual"
            },
            "msg_type": "landing_company"
        }

        # to convert python structure same as json output
        expected_id_ = json.dumps(expected_id)
        expected_landing_company_id = json.loads(expected_id_)

        self.assertTrue(tu.compare_data(landing_company_id, expected_landing_company_id), "Unmatch result")
