#!/usr/bin/env python

import yfinance as yf
import pandas as pd
from datetime import timedelta
from frequencies import Frequency
from enum import Enum
from sp_500_returns import input_or_default

def default_or_input(message, default=None):
    if default is not None:
        return default
    else:
        return input_or_default(message, None)

def format_date(d):
    return d.strftime('%m/%d/%Y')

def about_equals(td: timedelta, target: Enum, threshold=72):
    # threshold is in hours
    h = td.total_seconds() // 3600
    return abs(h - target.value) < threshold

def average_dividend(symbol):
    ticker = yf.Ticker(symbol)
    current_price = ticker.info['previousClose']
    data = ticker.history(interval='1d', period='max').loc[ticker.dividends.index].rename(columns=str.lower)
    avg_cost_per_dividend = data['close'].div(data['dividend'])

    payment_dates = pd.Series(data.index)
    first_date = payment_dates.iloc[0]
    last_date = payment_dates.iloc[-1]

    avg_freq = payment_dates.diff().mean()
    freq = None
    for f in Frequency:
        if about_equals(avg_freq, f):
            freq = f
    if freq is None:
        raise ValueError(f'No frequency matched for average payment time of {avg_freq}')

    return avg_cost_per_dividend, freq, first_date, last_date, current_price

if __name__ == '__main__':
    while True:
        try:
            symbol = input('Ticker: ')
            cost_per_dividend, f, first, last, cost_basis = average_dividend(symbol)
            print(f'\tCost Basis for $1 Dividend payment for {symbol} ({format_date(first)} - {format_date(last)})')
            print(f'\t${cost_per_dividend:.2f}')
            print(f'\tPayed out {f.name}')
        except Exception:
            print('Try again, lil bro.')
