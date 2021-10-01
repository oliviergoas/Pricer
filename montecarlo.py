import numpy as np

class MonteCarlo():
    def __init__(self):
        self.method = "Monte Carlo"

    def compute_price(self, contract):
        # Price Monte Carlo per $
        n = 100000
        r = contract.asset.rf
        T = contract.matu
        sum_payoff = 0
        for _ in range(n):
            sum_payoff += contract.expected_payoff() * np.exp(-r * T)
        return sum_payoff / n

    def compute_delta(self, contract):
        return "not implemented"

    def compute_gamma(self, contract):
        return "not implemented"

    def compute_vega(self, contract):
        return "not implemented"

    def compute_theta(self, contract):
        return "not implemented"

    def compute_rho(self, contract):
        return "not implemented"

    def compute_implied_volatility(self, contract, price):
        return "not implemented"
