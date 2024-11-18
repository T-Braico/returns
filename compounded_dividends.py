#!/usr/bin/env python

from sp_500_returns import input_or_default
from average_dividend import average_dividend
from frequencies import compounds

symbol = input('Ticker: ')
dividend, freq, _, _ = average_dividend(symbol)
initial_investment = input_or_default('Initial Investment: ', 5_000)
cost_basis = input_or_default('Cost Basis (Price of Instrument): ', 50)
shares = initial_investment / cost_basis

def compounded_yield(n_compounds):
    global shares
    d_yield = 0
    for _ in range(n_compounds):
        d_yield += shares * dividend
        shares += (shares * dividend) / cost_basis
    return d_yield

print(f'You would earn ${compounded_yield(compounds[freq]):,.2f} in dividends one year')
