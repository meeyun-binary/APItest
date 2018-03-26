import json
import test_utils as tu
import pytest


# from websocket import create_connection


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
    current_spot = float(current_spot)

    # note the current spot is float type.
    return current_spot


def proposal_call_put(symbol, contract_type, duration, duration_unit):
    proposal = json.dumps({"proposal": 1,
                           "amount": "10",
                           "basis": "payout",
                           "contract_type": contract_type,
                           "currency": "USD",
                           "duration": duration,
                           "duration_unit": duration_unit,
                           "symbol": symbol})

    proposal_result_js = tu.send_and_receive_ws(proposal)

    return proposal_result_js


def proposal_higher_lower(symbol, contract_type, barrier, duration, duration_unit):
    proposal = json.dumps({"proposal": 1,
                           "amount": "10",
                           "basis": "payout",
                           "contract_type": contract_type,
                           "currency": "USD",
                           "duration": duration,
                           "duration_unit": duration_unit,
                           "barrier": barrier,
                           "symbol": symbol})

    proposal_result_js = tu.send_and_receive_ws(proposal)

    return proposal_result_js


def proposal_touch_no_touch(symbol, contract_type, barrier, duration, duration_unit):
    proposal = json.dumps({"proposal": 1,
                           "amount": "100",
                           "basis": "payout",
                           "contract_type": contract_type,
                           "currency": "USD",
                           "duration": duration,
                           "duration_unit": duration_unit,
                           "barrier": barrier,
                           "symbol": symbol
                           })

    proposal_result_js = tu.send_and_receive_ws(proposal)

    return proposal_result_js


def proposal_in_out(symbol, contract_type, barrier, barrier2, duration, duration_unit):
    proposal = json.dumps({"proposal": 1,
                           "amount": "100",
                           "basis": "payout",
                           "contract_type": contract_type,
                           "currency": "USD",
                           "duration": duration,
                           "duration_unit": duration_unit,
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

    if num_open_contract != 0:
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


def abs_higher_barrier(current_spot, barrier, decimal_places):
    # create absolute barriers
    abs_barrier = current_spot + barrier
    abs_barrier_formatted = '{0:.{1}f}'.format(abs_barrier, decimal_places)

    return abs_barrier_formatted


def abs_lower_barrier2(current_spot, barrier2, decimal_places):
    # create absolute barriers
    abs_barrier2 = current_spot - barrier2
    abs_barrier_formatted2 = '{0:.{1}f}'.format(abs_barrier2, decimal_places)

    return abs_barrier_formatted2


@tu.rate_limited(0.20)
def buy(proposal):
    print_if_error(proposal)
    id = proposal['proposal']['id']

    json_buy = json.dumps({"buy": id,
                           "price": 100
                           })
    result_buy = tu.send_and_receive_ws(json_buy)

    print_if_error(result_buy)

    result_longcode = result_buy['buy']['longcode']

    return result_longcode


def print_if_error(call):
    if 'error' in call:
        print("{} error! \n {}".format(call['msg_type'], call))
