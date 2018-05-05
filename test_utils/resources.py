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


# -------------------
# compare dictionary
# -------------------

def id_dict(obj):
    return obj.__class__.__name__ == 'dict'


def contains_key_rec(v_key, v_dict):
    for curKey in v_dict:
        if curKey == v_key or (id_dict(v_dict[curKey]) and contains_key_rec(v_key, v_dict[curKey])):
            return True
    return False

def get_value_rec(v_key, v_dict):
    for curKey in v_dict:
        if curKey == v_key:
            return v_dict[curKey]
        elif id_dict(v_dict[curKey]) and get_value_rec(v_key, v_dict[curKey]):
            return contains_key_rec(v_key, v_dict[curKey])

def compare_dict(d1, d2):
    for key in d1:
     if contains_key_rec(key, d2):
         d2_value = get_value_rec(key, d2)
         if d1[key] == d2_value:
             # print("values are equal, d1: " + str(d1[key]) + ", d2: " + str(d2_value))
             pass
         else:
             print("values are not equal:\n"
                   "list1: " + str(d1[key]) + "\n" +
                   "list2: " + str(d2_value))

     else:
         print("dict d2 does not contain key: " + key)

    for key in d2:
     if not contains_key_rec(key, d1):
         print("dict d1 does not contain key: " + key)

# --------------------------
# end of compare dictionary
# --------------------------

def compare_data(source_data_a, source_data_b):
    def compare(data_a, data_b):
        # type=list
        if (type(data_a) is list):
            # is [data_b] a list and of same length as [data_a]?
            if (
                    (type(data_b) != list) or
                    (len(data_a) != len(data_b))
            ):
                print("List 1 is not a list or not of same length as List 2")
                return False

            # iterate over list items
            for list_index, list_item in enumerate(data_a):
                # compare [data_a] list item against [data_b] at index
                if (not compare(list_item, data_b[list_index])):
                    print("{0} and {1} are not identical".format(list_item, data_b[list_index]))

                    return False

            # list identical
            return True

        # type=dictionary
        if (type(data_a) is dict):
            # is [data_b] a dictionary?
            if (type(data_b) != dict):
                print("Input is not a dictionary")
                return False

            # iterate over dictionary keys
            for dict_key, dict_value in data_a.items():
                # key exists in [data_b] dictionary, and same value?
                if (
                        (dict_key not in data_b) or
                        (not compare(dict_value, data_b[dict_key]))
                ):
                    print(dict_value)
                    print(data_b[dict_key])
                    # print("'{0}: {1}' should exists/correct in dict 2".format(dict_key, dict_value))

                    return False

            # dictionary identical
            return True

        # simple value - compare both value and type for equality
        return (
                (data_a == data_b) and
                (type(data_a) is type(data_b))
        )

    # compare a to b, then b to a
    return (
            compare(source_data_a, source_data_b) and
            compare(source_data_b, source_data_a)
    )