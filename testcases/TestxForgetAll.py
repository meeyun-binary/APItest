import json
import unittest
import test_utils as tu
import time


class TestxForgetAll(unittest.TestCase):

    def setUp(self):
        tu.log_out()
        # to forget all (this is needed in case some test cases are failing
        # and thus forgot is not done on the test cases)
        json_data = json.dumps({'forget_all': 'ticks'})
        tu.send_and_receive_ws_x_authorize(json_data)
        json_data = json.dumps({'forget_all': 'proposal'})
        tu.send_and_receive_ws_x_authorize(json_data)

    def tearDown(self):
        # to forget all (this is needed in case some test cases are failing
        # and thus forgot is not done on the test cases)
        json_data = json.dumps({'forget_all': 'ticks'})
        tu.send_and_receive_ws_x_authorize(json_data)
        json_data = json.dumps({'forget_all': 'proposal'})
        tu.send_and_receive_ws_x_authorize(json_data)

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

    def test_forget_all_ticks_without_subscribe(self):
        json_data = json.dumps({'forget_all': 'ticks'})
        result_js = tu.send_and_receive_ws_x_authorize(json_data)

        forget_all = result_js['forget_all']
        msg_type = result_js["msg_type"]

        expected_forget_all = []
        expected_msg_type = "forget_all"

        self.assertEqual(forget_all, expected_forget_all)
        self.assertEqual(msg_type, expected_msg_type)

    def assert_forget_all(self, data, forget_value, json_key):
        output = tu.send_and_receive_ws_x_authorize(data)
        output_id = output[json_key]["id"]

        # send forget all - tick
        forget_all = json.dumps({'forget_all': forget_value})
        forget_output = tu.send_and_receive_ws_x_authorize(forget_all)
        forget_output_id = forget_output["forget_all"][0]

        # the subscribe id and forget id should be the same
        self.assertEqual(output_id, forget_output_id)
        self.assertTrue('error' not in forget_output)

    def test_forget_all_proposal(self):
        # subscribe proposal API
        proposal_call = self.proposal_call_put_subscribe("R_100", "CALL", 5, "d")

        self.assert_forget_all(proposal_call, "proposal", "proposal")

    def test_forget_all_multiple_proposals(self):
        # subscribe multiple proposal API
        proposal_call = self.proposal_call_put_subscribe("R_100", "CALL", 5, "d")
        output_call = tu.send_and_receive_ws_x_authorize(proposal_call)
        proposal_put = self.proposal_call_put_subscribe("R_100", "PUT", 5, "d")
        output_put = tu.send_and_receive_ws_x_authorize(proposal_put)

        # save the both proposal id in the list
        output_id_list = []
        output_id_list.extend((output_call["proposal"]["id"], output_put["proposal"]["id"]))

        forget_all = json.dumps({'forget_all': "proposal"})
        forget_output = tu.send_and_receive_ws_x_authorize(forget_all)
        forget_output_id = forget_output["forget_all"]

        # output_id_list and forget_output_id should have same list
        same_forget_id = [item for item in output_id_list if item in forget_output_id]

        self.assertEqual(len(same_forget_id), 2)
        self.assertTrue('error' not in forget_output)
