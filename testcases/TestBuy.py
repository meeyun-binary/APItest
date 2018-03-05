import json
import unittest
import test_utils as tu
import time
from websocket import create_connection

ws = create_connection("wss://ws.binaryws.com/websockets/v3?app_id=1089")


class TestBuyContract(unittest.TestCase):

    def setUp(self):
        return
        # json.dumps({"authorize": "ei5EBsqQan230MG"})

    def tearDown(self):
        return

    def proposal_call_put(self, contract_type):
        proposal = json.dumps({"proposal": 1,
                               "amount": "10",
                               "basis": "payout",
                               "contract_type": contract_type,
                               "currency": "USD",
                               "duration": "9",
                               "duration_unit": "m",
                               "symbol": "R_100"})

        proposal_result_js = tu.send_and_receive_ws(proposal)

        return proposal_result_js

    def test_call_contract(self):
        proposal = self.proposal_call_put("CALL")
        contract_id = proposal['proposal']['id']

        json_buy = json.dumps({"buy": contract_id,
                               "price": 100
                               })
        result_buy = tu.send_and_receive_ws(json_buy)

        longcode = result_buy['buy']['longcode']
        expected_longcode = 'Win payout if Volatility 100 Index is strictly higher than entry spot at 9 minutes after contract start time.'

        self.assertEqual(longcode, expected_longcode)

    def test_put_contract(self):
        proposal = self.proposal_call_put("PUT")
        contract_id = proposal['proposal']['id']

        json_buy = json.dumps({"buy": contract_id,
                               "price": 100
                               })
        result_buy = tu.send_and_receive_ws(json_buy)

        longcode = result_buy['buy']['longcode']
        expected_longcode = 'Win payout if Volatility 100 Index is strictly lower than entry spot at 9 minutes after contract start time.'

        self.assertEqual(longcode, expected_longcode)


    # todo test call hl
    # todo test put hl
    # todo test touches
    # todo test no touches
    # todo test end between
    # todo test end out
    # todo test asian put
    # todo test asian down
