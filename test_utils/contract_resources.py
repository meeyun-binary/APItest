import json
import unittest
import test_utils as tu

from websocket import create_connection

def find_latest_tick(symbol):
    # use tick_history API to get current spot
    spot = json.dumps({"ticks_history": symbol,
                       "end": "latest",
                       "start": 1,
                       "style": "ticks",
                       "adjust_start_time": 1,
                       "count": 1
                       })

    result_spot = tu.send_and_receive_ws(spot)
    current_spot = result_spot['history']['prices'][0]

    return current_spot

def proposal_call_put(symbol, contract_type):
    proposal = json.dumps({"proposal": 1,
                           "amount": "10",
                           "basis": "payout",
                           "contract_type": contract_type,
                           "currency": "USD",
                           "duration": "1",
                           "duration_unit": "m",
                           "symbol": symbol})

    proposal_result_js = tu.send_and_receive_ws(proposal)

    return proposal_result_js

def proposal_higher_lower(symbol, contract_type, barrier):
    proposal = json.dumps({"proposal": 1,
                           "amount": "10",
                           "basis": "payout",
                           "contract_type": contract_type,
                           "currency": "USD",
                           "duration": "1",
                           "duration_unit": "m",
                           "barrier": barrier,
                           "symbol": symbol})

    proposal_result_js = tu.send_and_receive_ws(proposal)

    return proposal_result_js

def proposal_touch_no_touch(symbol, contract_type, barrier):
    proposal = json.dumps({"proposal": 1,
                           "amount": "100",
                           "basis": "payout",
                           "contract_type": contract_type,
                           "currency": "USD",
                           "duration": "3",
                           "duration_unit": "m",
                           "barrier": barrier,
                           "symbol": symbol
                           })

    proposal_result_js = tu.send_and_receive_ws(proposal)

    return proposal_result_js

def proposal_in_out(symbol, contract_type, barrier, barrier2):
    proposal = json.dumps({"proposal": 1,
                           "amount": "100",
                           "basis": "payout",
                           "contract_type": contract_type,
                           "currency": "USD",
                           "duration": "3",
                           "duration_unit": "m",
                           "barrier": barrier,
                           "barrier2": barrier2,
                           "symbol": symbol
                           })

    proposal_result_js = tu.send_and_receive_ws(proposal)

    return proposal_result_js

def proposal_asian_up_down(symbol, contract_type):
    proposal = json.dumps({"proposal": 1,
                           "amount": "10",
                           "basis": "payout",
                           "contract_type": contract_type,
                           "currency": "USD",
                           "duration": 5,
                           "duration_unit": "t",
                           "symbol": symbol})

    proposal_result_js = tu.send_and_receive_ws(proposal)

    return proposal_result_js

def proposal_digit(symbol, contract_type):
    proposal = json.dumps({"proposal": 1,
                           "amount": "10",
                           "basis": "payout",
                           "contract_type": contract_type,
                           "currency": "USD",
                           "duration": 5,
                           "duration_unit": "t",
                           "barrier": 5,
                           "symbol": symbol})

    proposal_result_js = tu.send_and_receive_ws(proposal)

    return proposal_result_js

def proposal_digit_even_odd(symbol, contract_type):
    proposal = json.dumps({"proposal": 1,
                           "amount": "10",
                           "basis": "payout",
                           "contract_type": contract_type,
                           "currency": "USD",
                           "duration": 5,
                           "duration_unit": "t",
                           "symbol": symbol})

    proposal_result_js = tu.send_and_receive_ws(proposal)

    return proposal_result_js

def proposal_lookback(symbol, contract_type):
    proposal = json.dumps({"proposal": 1,
                           "amount": "1",
                           "basis": "multiplier",
                           "contract_type": contract_type,
                           "currency": "USD",
                           "duration": "1",
                           "duration_unit": "m",
                           "symbol": symbol})

    proposal_result_js = tu.send_and_receive_ws(proposal)

    return proposal_result_js


def sell_last_bought_contract():
    json_contract_id = json.dumps({"portfolio": 1})
    result_contract_id = tu.send_and_receive_ws(json_contract_id)

    num_open_contract = len(result_contract_id['portfolio']['contracts'])

    if(num_open_contract!=0):
        # get the contract id of last purchase contract
        contract_id = result_contract_id['portfolio']['contracts'][-1]['contract_id']

        # sell it
        json_sell_contract = json.dumps({"sell": contract_id,
                                         "price": 0
                                         })

        result_sell_contract = tu.send_and_receive_ws(json_sell_contract)

    else:
        result_sell_contract = "No open contract. Skipped selling contract"
        print (result_sell_contract)


    return result_sell_contract
