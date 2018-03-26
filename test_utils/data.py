frx={
    'frxAUDJPY': 'AUD/JPY',
    'frxEURJPY': 'EUR/JPY',
    'frxAUDCAD': 'AUD/CAD',

}

vol={
    'R_100': 'Volatility 100 Index',
    'R_10': 'Volatility 10 Index',
}


combined = dict(frx, **vol); combined.update(vol)


duration={
    't': 'ticks',
    'm': 'minutes',
    'h': 'hours'

}