from call import Call
from put import Put
from barrierput import BarrierPut
from barriercall import BarrierCall
from portfolio import Portfolio
from results import Results

class Pricer:
    def __init__(self, pricing_method):
        self.pm = pricing_method

    def price(self, object):
        if isinstance(object, Call) or isinstance(object, Put) or isinstance(object, BarrierCall) or isinstance(object, BarrierPut):
            return self.price_contract(object)
        if isinstance(object, Portfolio):
            return self.price_portfolio(object)

    def price_contract(self, contract):
        price = self.pm.compute_price(contract)
        delta = self.pm.compute_delta(contract)
        gamma = self.pm.compute_gamma(contract)
        vega = self.pm.compute_vega(contract)
        theta = self.pm.compute_theta(contract)
        rho = self.pm.compute_rho(contract)
        return Results(contract, self.pm.method, price, delta, gamma, vega, theta, rho)

    def price_portfolio(self, portfolio):
        price = 0
        delta = 0
        for contract in portfolio.contracts:
            price += self.pm.compute_price(contract) * portfolio.contracts[contract]
            delta += self.pm.compute_delta(contract) * portfolio.contracts[contract]
        return [price, delta]

    def implied_volatility(self, contract, market_price):
        return self.pm.compute_implied_volatility(contract, market_price)

    def price_projection(self, contract, spots):
        price_projection = []
        spot = contract.asset.spot
        for i in spots:
            contract.asset.spot = i
            price_projection.append(self.pm.compute_price(contract))
        contract.asset.spot = spot
        return price_projection

    def delta_projection(self, contract, spots):
        delta_projection = []
        spot = contract.asset.spot
        for i in spots:
            contract.asset.spot = i
            delta_projection.append(self.pm.compute_delta(contract))
        contract.asset.spot = spot
        return delta_projection

    def gamma_projection(self, contract, spots):
        gamma_projection = []
        spot = contract.asset.spot
        for i in spots:
            contract.asset.spot = i
            gamma_projection.append(self.pm.compute_gamma(contract))
        contract.asset.spot = spot
        return gamma_projection

    def vega_projection(self, contract, spots):
        vega_projection = []
        spot = contract.asset.spot
        for i in spots:
            contract.asset.spot = i
            vega_projection.append(self.pm.compute_vega(contract))
        contract.asset.spot = spot
        return vega_projection

    def theta_projection(self, contract, spots):
        theta_projection = []
        spot = contract.asset.spot
        for i in spots:
            contract.asset.spot = i
            theta_projection.append(self.pm.compute_theta(contract))
        contract.asset.spot = spot
        return theta_projection

    def rho_projection(self, contract, spots):
        rho_projection = []
        spot = contract.asset.spot
        for i in spots:
            contract.asset.spot = i
            rho_projection.append(self.pm.compute_rho(contract))
        contract.asset.spot = spot
        return rho_projection
