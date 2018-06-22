import unittest
import test_utils as tu
import json


class TestxPing(unittest.TestCase):

    def setUp(self):
        tu.log_out()
        return

    def tearDown(self):
        return

    def test_ping(self):
        ping = json.dumps({
            "ping": 1
        })

        ping_reponse = tu.send_and_receive_ws_x_authorize(ping)

        # remember to convert empty dict {} to None, else, result will fail ( {}!=None )
        expected_ping = {
            "echo_req": {
                "ping": 1
            },
            "msg_type": "ping",
            "ping": "pong"
        }

        # to convert python structure same as json output
        expected_ping_ = json.dumps(expected_ping)
        expected_ping_reponse = json.loads(expected_ping_)

        self.assertTrue(tu.compare_data(ping_reponse, expected_ping_reponse))
