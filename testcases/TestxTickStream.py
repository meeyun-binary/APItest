import json
import unittest
import test_utils as tu
import time
import datetime


class TestxTickStream(unittest.TestCase):

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

    # def test_stream_debug(self):
    #     json_data = json.dumps({
    #                 "ticks": "frxAUDJPY",
    #                 "subscribe": 1
    #             })
    #     tu.send_and_receive_ws_x_authorize(json_data)
    #
    #     # while True:
    #     output = tu.ws.recv()
    #     print(output)

    # def test_tick_stream_vol(self):
    #
    #     json_data = json.dumps({
    #         "ticks": "R_100",
    #         "subscribe": 1
    #     })
    #     result_js = tu.send_and_receive_ws_x_authorize(json_data)
    #
    #     count = 1
    #     result = []
    #
    #     while 'error' not in result_js and count <= 5:
    #         print("Stream tick number ", count)
    #         output = tu.ws.recv()
    #         # print(output)
    #         result.append(output)
    #         count += 1
    #
    #     self.assertTrue('error' not in result_js)
    #     self.assertEqual(count, 6, "Tick is less than 5 in 30 seconds")
    #     if count == 1:
    #         print("Tick is not streaming at all")

    def test_tick_stream_forex(self):
        check_trading_day = datetime.datetime.today().weekday()

        if check_trading_day < 5:
            json_data = json.dumps({
                "ticks": "frxAUDJPY",
                "subscribe": 1
            })
            result_js = tu.send_and_receive_ws_x_authorize(json_data)

            count = 1
            result = []

            # while 'error' not in result_js:
            while 'error' not in result_js and count <= 5:
                print("Stream tick number ", count)
                output = tu.ws.recv()
                result.append(output)
                count += 1

            self.assertTrue('error' not in result_js)
            self.assertEqual(count, 6, "Tick is less than 5 in 30 seconds")

        else:

            print("Skipped test due to weekend")

    # TODO skip this chunk because timeout decorator is giving error. If no response, websocket will timeout and
    # causing the subsequent test fail
    # # @tu.timeout(30)
    # def test_tick_stream_vol(self):
    #     try:
    #         json_data = json.dumps({
    #             "ticks": "R_100",
    #             "subscribe": 1
    #         })
    #         result_js = tu.send_and_receive_ws_x_authorize(json_data)
    #
    #         count = 1
    #         result = []
    #
    #
    #         while 'error' not in result_js and count <= 5:
    #             print("Stream tick number ", count)
    #             output = tu.ws.recv()
    #             # print(output)
    #             result.append(output)
    #             count += 1
    #
    #         self.assertTrue('error' not in result_js)
    #         self.assertEqual(count, 6, "Tick is less than 5 in 30 seconds")
    #         if count == 1:
    #             print("Tick is not streaming at all")
    #
    #     #TODO find a better way to handle when there is no streaming at all
    #     # current using timeout decorator
    #     except NameError as e:
    #         self.assertFalse("Tick is not streaming")
    #
    # # @tu.timeout(30)
    # def test_tick_stream_forex(self):
    #     check_trading_day = datetime.datetime.today().weekday()
    #
    #     try:
    #         if check_trading_day < 5:
    #             json_data = json.dumps({
    #                 "ticks": "frxAUDJPY",
    #                 "subscribe": 1
    #             })
    #             result_js = tu.send_and_receive_ws_x_authorize(json_data)
    #
    #             count = 1
    #             result = []
    #
    #             while 'error' not in result_js and count <= 5:
    #                 print("Stream tick number ", count)
    #                 output = tu.ws.recv()
    #                 result.append(output)
    #                 count += 1
    #
    #             self.assertTrue('error' not in result_js)
    #             self.assertEqual(count, 6, "Tick is less than 5 in 30 seconds")
    #
    #         else:
    #             print("Skipped test due to weekend")
    #
    #     #TODO find a better way to handle when there is no streaming at all
    #     # current using timeout decorator
    #     except NameError as e:
    #         self.assertFalse("Tick is not streaming")
    #
