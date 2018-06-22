# remember to convert empty dict {} to None, else, result will fail ( {}!=None )

expected_landing_company_details_costarica = {
    "echo_req": {
        "landing_company_details": "costarica"
    },
    "landing_company_details": {
        "address": None,
        "country": "Costa Rica",
        "currency_config": {
            "commodities": {
                "AUD": {
                    "max_payout": 50000,
                    "min_stake": 0.5
                },
                "BCH": {
                    "max_payout": 5,
                    "min_stake": 0.001
                },
                "BTC": {
                    "max_payout": 5,
                    "min_stake": 0.0002
                },
                "DAI": {
                    "max_payout": 5000,
                    "min_stake": 0.5
                },
                "ETH": {
                    "max_payout": 10,
                    "min_stake": 0.002
                },
                "EUR": {
                    "max_payout": 50000,
                    "min_stake": 0.5
                },
                "GBP": {
                    "max_payout": 50000,
                    "min_stake": 0.5
                },
                "LTC": {
                    "max_payout": 50,
                    "min_stake": 0.01
                },
                "USD": {
                    "max_payout": 50000,
                    "min_stake": 0.5
                }
            },
            "forex": {
                "AUD": {
                    "max_payout": 50000,
                    "min_stake": 0.5
                },
                "BCH": {
                    "max_payout": 5,
                    "min_stake": 0.001
                },
                "BTC": {
                    "max_payout": 5,
                    "min_stake": 0.0002
                },
                "DAI": {
                    "max_payout": 5000,
                    "min_stake": 0.5
                },
                "ETH": {
                    "max_payout": 10,
                    "min_stake": 0.002
                },
                "EUR": {
                    "max_payout": 50000,
                    "min_stake": 0.5
                },
                "GBP": {
                    "max_payout": 50000,
                    "min_stake": 0.5
                },
                "LTC": {
                    "max_payout": 50,
                    "min_stake": 0.01
                },
                "USD": {
                    "max_payout": 50000,
                    "min_stake": 0.5
                }
            },
            "indices": {
                "AUD": {
                    "max_payout": 50000,
                    "min_stake": 0.5
                },
                "BCH": {
                    "max_payout": 5,
                    "min_stake": 0.001
                },
                "BTC": {
                    "max_payout": 5,
                    "min_stake": 0.0002
                },
                "DAI": {
                    "max_payout": 5000,
                    "min_stake": 0.5
                },
                "ETH": {
                    "max_payout": 10,
                    "min_stake": 0.002
                },
                "EUR": {
                    "max_payout": 50000,
                    "min_stake": 0.5
                },
                "GBP": {
                    "max_payout": 50000,
                    "min_stake": 0.5
                },
                "LTC": {
                    "max_payout": 50,
                    "min_stake": 0.01
                },
                "USD": {
                    "max_payout": 50000,
                    "min_stake": 0.5
                }
            },
            "volidx": {
                "AUD": {
                    "max_payout": 50000,
                    "min_stake": 0.35
                },
                "BCH": {
                    "max_payout": 5,
                    "min_stake": 0.001
                },
                "BTC": {
                    "max_payout": 5,
                    "min_stake": 0.0002
                },
                "DAI": {
                    "max_payout": 5000,
                    "min_stake": 0.5
                },
                "ETH": {
                    "max_payout": 10,
                    "min_stake": 0.002
                },
                "EUR": {
                    "max_payout": 50000,
                    "min_stake": 0.35
                },
                "GBP": {
                    "max_payout": 50000,
                    "min_stake": 0.35
                },
                "LTC": {
                    "max_payout": 50,
                    "min_stake": 0.01
                },
                "USD": {
                    "max_payout": 50000,
                    "min_stake": 0.35
                }
            }
        },
        "has_reality_check": 0,
        "legal_allowed_contract_categories": [
            "asian",
            "callput",
            "callputequal",
            "digits",
            "endsinout",
            "staysinout",
            "touchnotouch",
            "lookback",
            "highlowticks",
            "reset",
            "callputspread"
        ],
        "legal_allowed_currencies": [
            "AUD",
            "BCH",
            "BTC",
            "DAI",
            "ETH",
            "EUR",
            "GBP",
            "LTC",
            "USD"
        ],
        "legal_allowed_markets": [
            "commodities",
            "forex",
            "indices",
            "volidx"
        ],
        "legal_default_currency": "USD",
        "name": "Binary (C.R.) S.A.",
        "shortcode": "costarica"
    },
    "msg_type": "landing_company_details"
}

expected_landing_company_details_iom = {
    "echo_req": {
        "landing_company_details": "iom"
    },
    "landing_company_details": {
        "address": [
            "First Floor, Millennium House",
            "Victoria Road",
            "Douglas",
            "IM2 4RW",
            "Isle of Man",
            "British Isles"
        ],
        "country": "Isle of Man",
        "currency_config": {
            "volidx": {
                "GBP": {
                    "max_payout": 50000,
                    "min_stake": 0.35
                },
                "USD": {
                    "max_payout": 50000,
                    "min_stake": 0.35
                }
            }
        },
        "has_reality_check": 1,
        "legal_allowed_contract_categories": [
            "asian",
            "callput",
            "digits",
            "endsinout",
            "staysinout",
            "touchnotouch"
        ],
        "legal_allowed_currencies": [
            "GBP",
            "USD"
        ],
        "legal_allowed_markets": [
            "volidx"
        ],
        "legal_default_currency": "GBP",
        "name": "Binary (IOM) Ltd",
        "shortcode": "iom"
    },
    "msg_type": "landing_company_details"
}

expected_landing_company_details_malta = {
    "echo_req": {
        "landing_company_details": "malta"
    },
    "landing_company_details": {
        "address": [
            "Mompalao Building",
            "Suite 2",
            "Tower Road",
            "Msida MSD1825",
            "Malta"
        ],
        "country": "Malta",
        "currency_config": {
            "volidx": {
                "EUR": {
                    "max_payout": 50000,
                    "min_stake": 0.35
                },
                "GBP": {
                    "max_payout": 50000,
                    "min_stake": 0.35
                },
                "USD": {
                    "max_payout": 50000,
                    "min_stake": 0.35
                }
            }
        },
        "has_reality_check": 1,
        "legal_allowed_contract_categories": [
            "asian",
            "callput",
            "digits",
            "endsinout",
            "staysinout",
            "touchnotouch"
        ],
        "legal_allowed_currencies": [
            "EUR",
            "GBP",
            "USD"
        ],
        "legal_allowed_markets": [
            "volidx"
        ],
        "legal_default_currency": "EUR",
        "name": "Binary (Europe) Ltd",
        "shortcode": "malta"
    },
    "msg_type": "landing_company_details"
}

expected_landing_company_details_maltainvest = {
    "echo_req": {
        "landing_company_details": "maltainvest"
    },
    "landing_company_details": {
        "address": [
            "Mompalao Building",
            "Suite 2",
            "Tower Road",
            "Msida MSD1825",
            "Malta"
        ],
        "country": "Malta",
        "currency_config": {
            "commodities": {
                "EUR": {
                    "max_payout": 50000,
                    "min_stake": 5
                },
                "GBP": {
                    "max_payout": 50000,
                    "min_stake": 5
                },
                "USD": {
                    "max_payout": 50000,
                    "min_stake": 5
                }
            },
            "forex": {
                "EUR": {
                    "max_payout": 50000,
                    "min_stake": 5
                },
                "GBP": {
                    "max_payout": 50000,
                    "min_stake": 5
                },
                "USD": {
                    "max_payout": 50000,
                    "min_stake": 5
                }
            },
            "indices": {
                "EUR": {
                    "max_payout": 50000,
                    "min_stake": 5
                },
                "GBP": {
                    "max_payout": 50000,
                    "min_stake": 5
                },
                "USD": {
                    "max_payout": 50000,
                    "min_stake": 5
                }
            }
        },
        "has_reality_check": 1,
        "legal_allowed_contract_categories": [
            "asian",
            "callput",
            "callputequal",
            "digits",
            "endsinout",
            "staysinout",
            "touchnotouch"
        ],
        "legal_allowed_currencies": [
            "EUR",
            "GBP",
            "USD"
        ],
        "legal_allowed_markets": [
            "commodities",
            "forex",
            "indices"
        ],
        "legal_default_currency": "EUR",
        "name": "Binary Investments (Europe) Ltd",
        "shortcode": "maltainvest"
    },
    "msg_type": "landing_company_details"
}

expected_landing_company_details_virtual = {
    "echo_req": {
        "landing_company_details": "virtual"
    },
    "landing_company_details": {
        "address": None,
        "country": "Bahamas",
        "currency_config": {
            "commodities": {
                "USD": {
                    "max_payout": 50000,
                    "min_stake": 0.5
                }
            },
            "forex": {
                "USD": {
                    "max_payout": 50000,
                    "min_stake": 0.5
                }
            },
            "indices": {
                "USD": {
                    "max_payout": 50000,
                    "min_stake": 0.5
                }
            },
            "volidx": {
                "USD": {
                    "max_payout": 50000,
                    "min_stake": 0.35
                }
            }
        },
        "has_reality_check": 0,
        "legal_allowed_contract_categories": [
            "asian",
            "callput",
            "callputequal",
            "digits",
            "endsinout",
            "staysinout",
            "touchnotouch",
            "reset",
            "lookback",
            "highlowticks",
            "callputspread"
        ],
        "legal_allowed_currencies": [
            "USD"
        ],
        "legal_allowed_markets": [
            "commodities",
            "forex",
            "indices",
            "volidx"
        ],
        "legal_default_currency": "USD",
        "name": "Binary Ltd",
        "shortcode": "virtual"
    },
    "msg_type": "landing_company_details"
}

expected_landing_company_details_japan = {
    "echo_req": {
        "landing_company_details": "japan"
    },
    "landing_company_details": {
        "address": [
            "Hiroo Miyata Bldg 3F",
            "1-9-16 Hiroo",
            "Shibuya-ku",
            "Tokyo 150-0012",
            "Japan"
        ],
        "country": "Japan",
        "currency_config": {
            "forex": {
                "JPY": {
                    "max_payout": 5000000,
                    "min_stake": 35
                }
            }
        },
        "has_reality_check": 0,
        "legal_allowed_contract_categories": [
            "callput",
            "callputequal",
            "endsinout",
            "staysinout",
            "touchnotouch"
        ],
        "legal_allowed_currencies": [
            "JPY"
        ],
        "legal_allowed_markets": [
            "forex"
        ],
        "legal_default_currency": "JPY",
        "name": "Binary KK",
        "shortcode": "japan"
    },
    "msg_type": "landing_company_details"
}

expected_landing_company_details_japan_virtual = {
    "echo_req": {
        "landing_company_details": "japan-virtual"
    },
    "landing_company_details": {
        "address": None,
        "country": "Japan",
        "currency_config": {
            "forex": {
                "JPY": {
                    "max_payout": 5000000,
                    "min_stake": 35
                }
            }
        },
        "has_reality_check": 0,
        "legal_allowed_contract_categories": [
            "callput",
            "callputequal",
            "endsinout",
            "staysinout",
            "touchnotouch"
        ],
        "legal_allowed_currencies": [
            "JPY"
        ],
        "legal_allowed_markets": [
            "forex"
        ],
        "legal_default_currency": "JPY",
        "name": "Binary Virtual Japan",
        "shortcode": "japan-virtual"
    },
    "msg_type": "landing_company_details"
}

expected_landing_company_details_vanuatu = {
    "echo_req": {
        "landing_company_details": "vanuatu"
    },
    "landing_company_details": {
        "address": [
            "Govant Building",
            "Port Vila",
            "P.O. Box 1276",
            "Vanuatu",
            "Republic of Vanuatu"
        ],
        "country": "Republic of Vanuatu",
        "currency_config": {
            "forex": {
                "USD": {
                    "max_payout": 50000,
                    "min_stake": 0.5
                }
            }
        },
        "has_reality_check": 0,
        "legal_allowed_contract_categories": [
            "callput"
        ],
        "legal_allowed_currencies": [
            "USD"
        ],
        "legal_allowed_markets": [
            "forex"
        ],
        "legal_default_currency": "USD",
        "name": "Binary (V) Ltd",
        "shortcode": "vanuatu"
    },
    "msg_type": "landing_company_details"
}

expected_landing_company_details_champion = {
    "echo_req": {
        "landing_company_details": "champion"
    },
    "landing_company_details": {
        "address": [
            "Govant Building",
            "Port Vila",
            "P.O. Box 1276",
            "Vanuatu",
            "Republic of Vanuatu"
        ],
        "country": "Republic of Vanuatu",
        "currency_config": {
            "commodities": {
                "USD": {
                    "max_payout": 50000,
                    "min_stake": 0.5
                }
            },
            "forex": {
                "USD": {
                    "max_payout": 50000,
                    "min_stake": 0.5
                }
            },
            "indices": {
                "USD": {
                    "max_payout": 50000,
                    "min_stake": 0.5
                }
            }
        },
        "has_reality_check": 0,
        "legal_allowed_contract_categories": [
            "callput",
            "endsinout",
            "staysinout",
            "touchnotouch"
        ],
        "legal_allowed_currencies": [
            "USD"
        ],
        "legal_allowed_markets": [
            "commodities",
            "forex",
            "indices"
        ],
        "legal_default_currency": "USD",
        "name": "Champion Group Ltd",
        "shortcode": "champion"
    },
    "msg_type": "landing_company_details"
}

expected_landing_company_details_champion_virtual = {
    "echo_req": {
        "landing_company_details": "champion-virtual"
    },
    "landing_company_details": {
        "address": None,
        "country": "Republic of Vanuatu",
        "currency_config": {
            "commodities": {
                "USD": {
                    "max_payout": 50000,
                    "min_stake": 0.5
                }
            },
            "forex": {
                "USD": {
                    "max_payout": 50000,
                    "min_stake": 0.5
                }
            },
            "indices": {
                "USD": {
                    "max_payout": 50000,
                    "min_stake": 0.5
                }
            }
        },
        "has_reality_check": 0,
        "legal_allowed_contract_categories": [
            "callput",
            "endsinout",
            "staysinout",
            "touchnotouch"
        ],
        "legal_allowed_currencies": [
            "USD"
        ],
        "legal_allowed_markets": [
            "commodities",
            "forex",
            "indices"
        ],
        "legal_default_currency": "USD",
        "name": "Champion Virtual",
        "shortcode": "champion-virtual"
    },
    "msg_type": "landing_company_details"
}
