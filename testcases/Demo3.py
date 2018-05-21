import json
import unittest
import test_utils as tu

class TestWithDictionaryStructure(unittest.TestCase):
    """This demo utilizes dictionary structure"""

    def setUp(self):
        return

    def tearDown(self):
        return

    def test_forget_all_3(self):
        json_data = json.dumps(
            {
                'forget_all': 'ticks'
            }
        )

        output = tu.send_and_receive_ws(json_data)
        msg_type = output["msg_type"]

        expected_msg_type = "forget_all"

        self.assertEqual(msg_type, expected_msg_type)
