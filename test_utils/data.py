frx={
    # Major pairs
    'frxAUDJPY': 'AUD/JPY',
    'frxAUDUSD': 'AUD/USD',
    'frxEURAUD': 'EUR/AUD',
    'frxEURCAD': 'EUR/CAD',
    'frxEURCHF': 'EUR/CHF',
    'frxEURGBP': 'EUR/GBP',
    'frxEURJPY': 'EUR/JPY',
    'frxEURUSD': 'EUR/USD',
    'frxGBPAUD': 'GBP/AUD',
    'frxGBPJPY': 'GBP/JPY',
    'frxGBPUSD': 'GBP/USD',
    'frxUSDCAD': 'USD/CAD',
    'frxUSDCHF': 'USD/CHF',
    'frxUSDJPY': 'USD/JPY',

    # Minor pairs
    'frxAUDCAD': 'AUD/CAD',
    'frxAUDCHF': 'AUD/CHF',
    'frxAUDNZD': 'AUD/NZD',
    'frxAUDPLN': 'AUD/PLN',
    'frxEURNZD': 'EUR/NZD',
    'frxGBPCAD': 'GBP/CAD',
    'frxGBPCHF': 'GBP/CHF',
    'frxGBPNOK': 'GBP/NOK',
    'frxGBPNZD': 'GBP/NZD',
    'frxGBPPLN': 'GBP/PLN',
    'frxNZDJPY': 'NZD/JPY',
    'frxNZDUSD': 'NZD/USD',
    'frxUSDMXN': 'USD/MXN',
    'frxUSDNOK': 'USD/NOK',
    'frxUSDPLN': 'USD/PLN',
    'frxUSDSEK': 'USD/SEK',

}

vol={
    'R_10': 'Volatility 10 Index',
    'R_25': 'Volatility 25 Index',
    'R_50': 'Volatility 50 Index',
    'R_75': 'Volatility 75 Index',
    'R_100': 'Volatility 100 Index'
}


combined = dict(frx, **vol); combined.update(vol)


duration={
    't': 'ticks',
    's': 'seconds',
    'm': 'minutes',
    'h': 'hours',
    'd': 'days',

}

