import json
import unittest
import test_utils as tu

class TestWithTestUtils(unittest.TestCase):
    """This demo includes test_utils"""

    def setUp(self):
        return

    def tearDown(self):
        return

    def test_forget_all_2(self):
        # json.dumps: python dict => json string
        json_data = json.dumps(
            {
                'forget_all': 'ticks'
            }
        )

        # ws.send(json_data)
        output = tu.send_and_receive_ws(json_data)  # return output in string format

        expected_output = {"echo_req": {"forget_all": "ticks"}, "forget_all": [], "msg_type": "forget_all"}

        self.assertEqual(output, expected_output)