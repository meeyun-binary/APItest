import json
import unittest
import test_utils as tu
import time
import datetime


class TestxTickHistory(unittest.TestCase):

    def setUp(self):
        tu.log_out()
        # to forget all (this is needed in case some test cases are failing
        # and thus forgot is not done on the test cases)
        json_data = json.dumps({'forget_all': 'ticks'})
        tu.send_and_receive_ws_x_authorize(json_data)

    def tearDown(self):
        # to forget all (this is needed in case some test cases are failing
        # and thus forgot is not done on the test cases)
        json_data = json.dumps({'forget_all': 'ticks'})
        tu.send_and_receive_ws_x_authorize(json_data)
        return

    def test_tick_history_vol(self):
        input1 = json.dumps(
            {
                "ticks_history": "R_50",
                "end": "latest",
                "start": 1,
                "style": "ticks",
                "adjust_start_time": 1,
                "count": 10
            }
        )

        tick_history_output1 = tu.send_and_receive_ws_x_authorize(input1)
        last_tick_time1 = tick_history_output1["history"]["times"][-1]

        time.sleep(2)

        input2 = json.dumps(
            {
                "ticks_history": "R_50",
                "end": "latest",
                "start": 1,
                "style": "ticks",
                "adjust_start_time": 1,
                "count": 10
            }
        )

        tick_history_output2 = tu.send_and_receive_ws_x_authorize(input2)

        last_tick_time2 = tick_history_output2["history"]["times"][-1]

        # make sure last tick is the latest
        self.assertTrue(last_tick_time2 > last_tick_time1)

        # make sure it returns 10 history
        self.assertTrue(len(tick_history_output2["history"]["times"]), 10)
        self.assertTrue(len(tick_history_output2["history"]["prices"]), 10)
        self.assertTrue('error' not in tick_history_output2)

    def test_tick_history_custom_start_end(self):
        # get the current epoch time
        end = int(time.time())

        # get the time in ten minutes ago
        current_time = datetime.datetime.now()  # use datetime.datetime.utcnow() for UTC time
        ten_minutes_ago = current_time - datetime.timedelta(minutes=10)

        start = int(ten_minutes_ago.timestamp())  # convert to epoch time

        input = json.dumps(
            {
                "ticks_history": "R_50",
                "end": end,
                "start": start,
                "style": "ticks",
                "adjust_start_time": 1
            }
        )

        tick_history_output = tu.send_and_receive_ws_x_authorize(input)

        for item in tick_history_output["history"]["times"]:
            # convert unicode to int
            item = int(item)
            self.assertTrue(end >= item >= start)

        self.assertTrue(len(tick_history_output["history"]["times"]) != 0)

    def test_tick_history_forex(self):
        input1 = json.dumps(
            {
                "ticks_history": "frxAUDJPY",
                "end": "latest",
                "start": 1,
                "style": "ticks",
                "adjust_start_time": 1,
                "count": 10
            }
        )

        tick_history_output1 = tu.send_and_receive_ws_x_authorize(input1)
        last_tick_time1 = tick_history_output1["history"]["times"][-1]

        time.sleep(2)

        input2 = json.dumps(
            {
                "ticks_history": "R_50",
                "end": "latest",
                "start": 1,
                "style": "ticks",
                "adjust_start_time": 1,
                "count": 10
            }
        )

        tick_history_output2 = tu.send_and_receive_ws_x_authorize(input2)

        last_tick_time2 = tick_history_output2["history"]["times"][-1]

        # make sure last tick is the latest
        self.assertTrue(last_tick_time2 > last_tick_time1)

        # make sure it returns 10 history
        self.assertTrue(len(tick_history_output2["history"]["times"]), 10)
        self.assertTrue(len(tick_history_output2["history"]["prices"]), 10)
        self.assertTrue('error' not in tick_history_output2)

    @unittest.skip("enable after bug fix")
    def test_tick_history_candle_future_date(self):
        # get the time in ten minutes ago
        current_time = datetime.datetime.now()  # use datetime.datetime.utcnow() for UTC time
        five_years_future = current_time + datetime.timedelta(days=1825)

        end = int(five_years_future.timestamp())  # convert to epoch time

        input = json.dumps(
            {
                "ticks_history": "R_50",
                "end": end,
                "start": 1,
                "style": "candles",
                "adjust_start_time": 1,
                "count": 10
            }
        )

        tick_history_output = tu.send_and_receive_ws_x_authorize(input)

        self.assertTrue('error' not in tick_history_output)
        # make sure it returns 10 candles
        self.assertTrue(len(tick_history_output["candles"]), 10)
