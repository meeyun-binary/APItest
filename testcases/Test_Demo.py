import unittest
import json
import test_utils as tu
from websocket import create_connection


class TestForgetAll(unittest.TestCase):

    def setUp(self):
        # test api
        self.input = json.dumps(
            {
                "forget_all": "ticks"
            }

        )

        self.output_dict = tu.send_and_receive_ws(self.input)

    def tearDown(self):
        return

    def test_forget_all_works(self):
        output = self.output_dict['msg_type']

        expected = "forget_all"

        self.assertEqual(output, expected)

    def test_forget_all_no_error(self):
        self.assertTrue('error' not in self.output_dict)
