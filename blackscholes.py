import numpy as np
import scipy.stats as si

from put import Put
from call import Call

class BlackScholes():
    def __init__(self):
        self.method = "Black Scholes"

    def d1(self, S, r, v, K, T):
        return (np.log(S / K) + (r + .5 * v ** 2) * T) / (v * np.sqrt(T))

    def d2(self, S, r, v, K, T):
        return self.d1(S, r, v, K, T) - v * np.sqrt(T)

    def compute_price(self, contract):
        # Price Black Scholes per $
        S = contract.asset.spot
        r = contract.asset.rf
        v = contract.asset.vol
        K = contract.strike
        T = contract.matu
        if isinstance(contract, Call):
            return S * si.norm.cdf(self.d1(S, r, v, K, T)) - K * np.exp(-r * T) * si.norm.cdf(self.d2(S, r, v, K, T))
        elif isinstance(contract, Put):
            return K * np.exp(-r * T) * si.norm.cdf(-self.d2(S, r, v, K, T)) - S * si.norm.cdf(-self.d1(S, r, v, K, T))

    def compute_delta(self, contract):
        # Delta Black Scholes per $
        S = contract.asset.spot
        r = contract.asset.rf
        v = contract.asset.vol
        K = contract.strike
        T = contract.matu
        if isinstance(contract, Call):
            return si.norm.cdf(self.d1(S, r, v, K, T))
        elif isinstance(contract, Put):
            return -si.norm.cdf(-self.d1(S, r, v, K, T))

    def compute_gamma(self, contract):
        # Gamma Black Scholes per $
        S = contract.asset.spot
        r = contract.asset.rf
        v = contract.asset.vol
        K = contract.strike
        T = contract.matu
        if isinstance(contract, Call) or isinstance(contract, Put):
            return si.norm.pdf(self.d1(S, r, v, K, T)) / (S * v * np.sqrt(T))

    def compute_vega(self, contract):
        # Vega Black Scholes per %
        S = contract.asset.spot
        r = contract.asset.rf
        v = contract.asset.vol
        K = contract.strike
        T = contract.matu
        if isinstance(contract, Call) or isinstance(contract, Put):
            return .01 * (S * si.norm.pdf(self.d1(S, r, v, K, T)) * np.sqrt(T))

    def compute_theta(self, contract):
        # Theta Black Scholes per %
        S = contract.asset.spot
        r = contract.asset.rf
        v = contract.asset.vol
        K = contract.strike
        T = contract.matu
        if isinstance(contract, Call):
            return .01 * (-(S * si.norm.pdf(self.d1(S, r, v, K, T)) * v) / (2 * np.sqrt(T)) - r * K * np.exp(-r * T) * si.norm.cdf(self.d2(S, r, v, K, T)))
        elif isinstance(contract, Put):
            return .01 * (-(S * si.norm.pdf(self.d1(S, r, v, K, T)) * v) / (2 * np.sqrt(T)) + r * K * np.exp(-r * T) * si.norm.cdf(-self.d2(S, r, v, K, T)))

    def compute_rho(self, contract):
        # Rho Black Scholes per %
        S = contract.asset.spot
        r = contract.asset.rf
        v = contract.asset.vol
        K = contract.strike
        T = contract.matu
        if isinstance(contract, Call):
            return .01 * (K * T * np.exp(-r * T) * si.norm.cdf(self.d2(S, r, v, K, T)))
        elif isinstance(contract, Put):
            return .01 * (-K * T * np.exp(-r * T) * si.norm.cdf(-self.d2(S, r, v, K, T)))

    def compute_implied_volatility(self, contract, price):
        # Implied volatility Back Scholes per %
        S = contract.asset.spot
        r = contract.asset.rf
        K = contract.strike
        T = contract.matu
        sigma = .001
        while sigma < 1:
            if isinstance(contract, Call):
                implied_price = S * si.norm.cdf(self.d1(S, r, sigma, K, T)) - K * np.exp(-r * T) * si.norm.cdf(self.d2(S, r, sigma, K, T))
            elif isinstance(contract, Put):
                implied_price = K * np.exp(-r * T) * si.norm.cdf(-self.d2(S, r, sigma, K, T)) - S * si.norm.cdf(-self.d1(S, r, sigma, K, T))
            if price - implied_price < .001:
                return sigma
            sigma += .001
        return "no implied volatility found"
