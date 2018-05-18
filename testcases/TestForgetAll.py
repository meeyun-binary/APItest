import json
import unittest
import test_utils as tu

class TestForgetAll(unittest.TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return

    def test_forget_all(self):
        json_data = json.dumps({'forget_all': 'ticks'})
        result_js = tu.send_and_receive_ws(json_data)

        forget_all = result_js['forget_all']
        msg_type = result_js["msg_type"]

        expected_forget_all = []
        expected_msg_type = "forget_all"

        self.assertEqual(forget_all,expected_forget_all)
        self.assertEqual(msg_type, expected_msg_type)
