#!/usr/bin/env python

import json
import yfinance as yf

# must have portfolio.json file to run this script
with open('portfolio.json', 'r') as f:
    portfolio_data = json.load(f)

value = 0
for ticker, quantity in portfolio_data.items():
    data = yf.Ticker(ticker).info
    if 'bid' in data.keys():
        value += data['bid'] * quantity
    else:
        value += data['previousClose'] * quantity

print(f'Current portfolio value is ${value:,.2f}')
