import json
import unittest
from websocket import create_connection
import time

global ws
ws = create_connection("wss://ws.binaryws.com/websockets/v3?app_id=1089")

def send_and_receive_ws(json_data):

    autho = json.dumps({"authorize": "ei5EBsqQan230MG"})
    ws.send(autho)
    ws.recv()

    ws.send(json_data)
    result_str = ws.recv()

    result_js = json.loads(result_str)

    return result_js