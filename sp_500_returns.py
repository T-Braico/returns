#!/usr/bin/env python

def input_or_default(message, value):
    user_input = input(message)
    try:
        return int(user_input)
    except ValueError:
        try:
            return float(user_input)
        except ValueError:
            return value

def main():
    annual_return = float(input_or_default('Yearly Appreciation: ', 0.07))  # percentage annual return
    monthly_investment = input_or_default('Monthly Investment: ', 500)
    initial_investment = input_or_default('Initial Investment: ', 80_000)  # funds after one year of college
    current_age = input_or_default('Starting Age: ', 18)
    selling_age = input_or_default('Selling Age: ', 65)

    # assuming equal returns m / m
    # (1 + monthly_return) ^ 12 = 1 + annual_return
    # 12 ln(1 + monthly_return) = ln(1 + annual_return)
    # ln(1 + monthly_return) = ln(1 + annual_return) / 12
    # 1 + monthly_return = (e ^ ln(1 + annual_return)) ^ (1 / 12)
    # 1 + monthly_return = (1 + annual_return) ^ 1 / 12
    # monthly_return = (1 + annual_return) ^ (1 / 12) - 1
    monthly_return = (1 + annual_return) ** (1 / 12) - 1

    balance = initial_investment
    total_return = 1
    for i in range(selling_age - current_age):
        for _ in range(12):
            balance *= (1 + monthly_return)
            total_return *= (1 + monthly_return)
            balance += monthly_investment

    annual_inflation = 0.02
    capital_gains_tax_rate = 0.20
    inflation_adjustment = (1 - annual_inflation) ** (selling_age - current_age)
    adjusted_equity = balance * (1 - capital_gains_tax_rate) * inflation_adjustment

    print(f'After {selling_age - current_age} years, equity is ${adjusted_equity:,.2f} after tax and adjusting for inflation')
    print(f'Total return is {total_return * 100:.2f}%')

if __name__ == '__main__':
    main()
