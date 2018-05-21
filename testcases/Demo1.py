import json
import unittest
from websocket import create_connection

# import test_utils as tu

class TestSimplest(unittest.TestCase):
    """Simplest test case"""

    def setUp(self):
        return

    def tearDown(self):
        return

    def test_forget_all_1(self):

        # define your websocket
        ws = create_connection("wss://ws.binaryws.com/websockets/v3?app_id=1089")

        # authorise API token
        authorise = json.dumps(
            {
                "authorize": "ei5EBsqQan230MG"
            }
        )

        # authorize
        ws.send(authorise)
        ws.recv()


        # json.dumps: python dict => json string
        json_data = json.dumps(
            {
                'forget_all': 'ticks'
            }
        )


        ws.send(json_data)
        result_str = ws.recv() # return output in string format
        output = json.loads(result_str) # convert string to dictionary structure

        expected_output ={"echo_req":{"forget_all":"ticks"},"forget_all":[],"msg_type":"forget_all"}

        self.assertEqual(output, expected_output)