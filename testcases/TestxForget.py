import json
import unittest
import test_utils as tu


class TestxForget(unittest.TestCase):

    def setUp(self):
        tu.log_out()
        return

    def tearDown(self):
        # to forget all (this is needed in case some test cases are failing
        # and thus forgot is not done on the test cases)
        json_data = json.dumps({'forget_all': 'proposal'})
        tu.send_and_receive_ws_x_authorize(json_data)
        return

    def proposal_call_put_subscribe(self, symbol, contract_type, duration, duration_unit):
        proposal = json.dumps({"proposal": 1,
                               "amount": "10",
                               "basis": "payout",
                               "contract_type": contract_type,
                               "currency": "USD",
                               "duration": duration,
                               "duration_unit": duration_unit,
                               "symbol": symbol,
                               "subscribe": 1})

        return proposal

    def test_forget_proposal(self):
        # subscribe proposal API
        proposal_call = self.proposal_call_put_subscribe("R_100", "CALL", 5, "d")
        output_call = tu.send_and_receive_ws_x_authorize(proposal_call)
        proposal_id = output_call["proposal"]["id"]

        forget = json.dumps({'forget': proposal_id})
        forget_output = tu.send_and_receive_ws_x_authorize(forget)

        self.assertEqual(forget_output["forget"], 1)
        self.assertTrue('error' not in forget_output)
