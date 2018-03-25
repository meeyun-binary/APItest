import json
from websocket import create_connection
import time
import setting
import datetime


ws = create_connection("wss://{}/websockets/v3?app_id={}".format(setting.args.server, setting.args.app_id))


def send_and_receive_ws(json_data):
    autho = json.dumps({"authorize": "{}".format(setting.args.token)})

    ws.send(autho)
    ws.recv()

    ws.send(json_data)
    result_str = ws.recv()

    # convert to dictionary structure
    result_js = json.loads(result_str)

    return result_js

# decorator to avoid hitting rate limit
def rate_limited(max_per_second):
    min_interval = 1.0 / float(max_per_second)

    def decorate(func):
        last_time_called = [0.0]

        def rate_limited_function(*args, **kargs):
            elapsed = time.clock() - last_time_called[0]
            left_to_wait = min_interval - elapsed
            if left_to_wait > 0:
                time.sleep(left_to_wait)
            ret = func(*args, **kargs)
            last_time_called[0] = time.clock()
            return ret

        return rate_limited_function

    return decorate



def trading_day(symbol):
    # if symbol is not Volatility, check if today is trading day
    if "R_" not in symbol:
        check_trading_day = datetime.datetime.today().weekday()

        if check_trading_day < 5:
            is_trading_day = True
        else:
            is_trading_day = False

    else:
        is_trading_day = True

        return is_trading_day


def contract_end_date(duration):
    today = datetime.datetime.today()
    end_date_time = today + datetime.timedelta(days=duration)
    end_date = end_date_time.strftime('%Y-%m-%d')
    return end_date
