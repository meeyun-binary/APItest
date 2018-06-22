import json
import unittest
import test_utils as tu
import datetime
import time


class TestxWebsiteStatus(unittest.TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return

    def test_website_status(self):
        tu.log_out()  # log out so it will return client country as my

        input = json.dumps({
            "website_status": 1
        })

        website_status_response = tu.send_and_receive_ws_x_authorize(input)

        expected_website_status = {
            "echo_req": {
                "website_status": 1
            },
            "msg_type": "website_status",
            "website_status": {
                "api_call_limits": {
                    "max_proposal_subscription": {
                        "applies_to": "subscribing to proposal concurrently",
                        "max": 5
                    },
                    "max_requestes_general": {
                        "applies_to": "rest of calls",
                        "hourly": 14400,
                        "minutely": 180
                    },
                    "max_requests_outcome": {
                        "applies_to": "portfolio, statement and proposal",
                        "hourly": 1500,
                        "minutely": 25
                    },
                    "max_requests_pricing": {
                        "applies_to": "proposal and proposal_open_contract",
                        "hourly": 3600,
                        "minutely": 80
                    }
                },
                "clients_country": "my",
                "currencies_config": {
                    "AUD": {
                        "fractional_digits": 2,
                        "stake_default": 10,
                        "type": "fiat"
                    },
                    "BCH": {
                        "fractional_digits": 8,
                        "stake_default": 0.03,
                        "type": "crypto"
                    },
                    "BTC": {
                        "fractional_digits": 8,
                        "stake_default": 0.003,
                        "type": "crypto"
                    },
                    "DAI": {
                        "fractional_digits": 2,
                        "stake_default": 10,
                        "type": "crypto"
                    },
                    "ETH": {
                        "fractional_digits": 8,
                        "stake_default": 0.05,
                        "type": "crypto"
                    },
                    "EUR": {
                        "fractional_digits": 2,
                        "stake_default": 10,
                        "type": "fiat"
                    },
                    "GBP": {
                        "fractional_digits": 2,
                        "stake_default": 10,
                        "type": "fiat"
                    },
                    "LTC": {
                        "fractional_digits": 8,
                        "stake_default": 0.25,
                        "type": "crypto"
                    },
                    "USD": {
                        "fractional_digits": 2,
                        "stake_default": 10,
                        "type": "fiat"
                    }
                },
                "site_status": "up",
                "supported_languages": [
                    "EN",
                    "ID",
                    "RU",
                    "ES",
                    "FR",
                    "IT",
                    "PT",
                    "PL",
                    "DE",
                    "JA",
                    "ZH_CN",
                    "VI",
                    "ZH_TW",
                    "TH"
                ],
                "terms_conditions_version": "Version 45 2018-05-21"
            }
        }

        # to convert python structure same as json output
        expected_website_status = tu.convert_py_json_output(expected_website_status)

        # Without authenticate token, it will return clients_country: my, or else, follow the account country
        self.assertTrue(tu.compare_data(website_status_response, expected_website_status))
        self.assertTrue('error' not in website_status_response)
