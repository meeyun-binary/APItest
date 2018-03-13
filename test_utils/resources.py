import json
from websocket import create_connection
import time
import setting

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
def RateLimited(max_per_second):
    minInterval = 1.0 / float(max_per_second)

    def decorate(func):
        lastTimeCalled = [0.0]

        def rateLimitedFunction(*args, **kargs):
            elapsed = time.clock() - lastTimeCalled[0]
            leftToWait = minInterval - elapsed
            if leftToWait > 0:
                time.sleep(leftToWait)
            ret = func(*args, **kargs)
            lastTimeCalled[0] = time.clock()
            return ret

        return rateLimitedFunction

    return decorate
