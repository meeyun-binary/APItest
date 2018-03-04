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

    def proposal_R_100_touches_contract(self):
        json_data = json.dumps({"proposal": 1,
                                "amount": "100",
                                "basis": "payout",
                                "contract_type": "ONETOUCH",
                                "currency": "USD",
                                "duration": "2",
                                "duration_unit": "m",
                                "barrier": "+3.50",
                                "symbol": "R_100"})

        proposal_result_js = tu.send_and_receive_ws(json_data)

        return proposal_result_js

    def test_proposal_R_100_touches_contract(self):
        longcode = self.proposal_R_100_touches_contract()['proposal']['longcode']
        expected_longcode = 'lWin payout if Volatility 100 Index touches entry spot plus 3.50 through 2 minutes after ' \
                            'contract start time.'

        self.assertEqual(longcode, expected_longcode)

    # def test_proposal_and_buy_R_100_touches_contract(self):

    # ---------------------------------------------------
    # autho = json.dumps({"authorize": "ei5EBsqQan230MG"})
    # ws.send(autho)
    # result_autho = ws.recv()
    # # print(result_autho)
    #
    # json_data = json.dumps({
    #     "buy": "1",
    #     "price": 100,
    #     "parameters": {
    #         "amount": 10,
    #         "basis": "payout",
    #         "currency": "USD",
    #         "duration": 5,
    #         "duration_unit": "m",
    #         "contract_type": "CALL",
    #         "symbol": "R_100"
    #     }
    # })
    #
    # ws.send(json_data)
    # result_buy = ws.recv()
    # print(result_buy)

    # ---------------------------------------------------

    # autho = json.dumps({"authorize": "ei5EBsqQan230MG"})
    # ws.send(autho)
    # ws.recv()
    #
    # json_proposal = json.dumps({"proposal": 1,
    #                         "amount": "10",
    #                         "basis": "payout",
    #                         "contract_type": "CALL",
    #                         "currency": "USD",
    #                         "duration": "9",
    #                         "duration_unit": "m",
    #                         "symbol": "R_100"})
    #
    # print(json_proposal)
    #
    # ws.send(json_proposal)
    # result_proposal = ws.recv()
    #
    # print(result_proposal)
    #
    # result_js = json.loads(result_proposal)
    #
    # contract_id = result_js['proposal']['id']
    #
    # json_buy = json.dumps({"buy": contract_id,
    #                     "price": 100
    #                     })
    #
    # ws.send(json_buy)
    # result_buy_proposal = ws.recv()
    #
    # print(result_buy_proposal)

    # ---------------------------------------------------

    # json_proposal = json.dumps({"proposal": 1,
    #                             "amount": "10",
    #                             "basis": "payout",
    #                             "contract_type": "CALL",
    #                             "currency": "USD",
    #                             "duration": "12",
    #                             "duration_unit": "m",
    #                             "symbol": "R_100"})
    #
    # # result_proposal = self.snr(json_proposal)
    # result_proposal = tu.send_and_receive_ws(json_proposal)
    #
    #
    #
    # contract_id = result_proposal['proposal']['id']
    #
    # json_buy = json.dumps({"buy": contract_id,
    #                        "price": 100
    #                        })
    #
    # # result_buy_proposal = self.snr(json_buy)
    # result_buy_proposal = tu.send_and_receive_ws(json_buy)
    #
    #
    #
    # print(result_buy_proposal)

    # ----------------------

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

    # todo test call

    # todo test put

    # todo test call hl
    # todo test put hl
    # todo test touches
    # todo test no touches
    # todo test end between
    # todo test end out
    # todo test asian put
    # todo test asian down
