import unittest
import json
import test_utils as tu

class TestWithTestFixture(unittest.TestCase):
    """This demo utilizes test fixture"""

    def setUp(self):
        # test forget_all API
        self.input = json.dumps({
            "forget_all": "ticks"
        })

        self.output = tu.send_and_receive_ws(self.input)

    def test_forget_all_msg(self):
        output_msg_type = self.output['msg_type']
        expected = "forget_all"

        self.assertEqual(expected, output_msg_type)

    def test_forget_all_has_no_error(self):
        self.assertTrue('error' not in self.output)

