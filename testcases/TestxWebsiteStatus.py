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

    def get_prod_output(self, input):
        # prod
        tu.prod_ws.send(input)
        result_str = tu.prod_ws.recv()
        prod_output = json.loads(result_str)

        return prod_output

    @unittest.skip("skip this as travis detected country as 'us'")
    def test_website_status(self):
        tu.log_out()  # log out so it will return client country as my

        input = json.dumps({
            "website_status": 1
        })

        website_status_response = tu.send_and_receive_ws_x_authorize(input)

        prod_output = self.get_prod_output(input)

        # to convert python structure same as json output
        expected_website_status = tu.convert_py_json_output(prod_output)

        # Without authenticate token, it will return clients_country: my, or else, follow the account country
        self.assertTrue(tu.compare_data(website_status_response, expected_website_status))
        self.assertTrue('error' not in website_status_response)
