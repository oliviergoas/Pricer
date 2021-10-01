from put import Put
from call import Call

class Results:
    def __init__(self, contract, pricing_method, price, delta, gamma, vega, theta, rho):
        self.contract = contract
        self.pm = pricing_method
        self.price = price
        self.delta = delta
        self.gamma = gamma
        self.vega = vega
        self.theta = theta
        self.rho = rho

    def get_dictionary(self):
        return {
            "contract": self.contract.get_dictionary(),
            "pricing method": self.pm,
            "values": {
                "price": self.price,
                "delta": self.delta,
                "gamma": self.gamma,
                "vega": self.vega,
                "theta": self.theta,
                "rho": self.rho,
            }
        }

    def __str__(self):
        if isinstance(self.contract, Call):
            type = "Call"
        elif isinstance(self.contract, Put):
            type = "Put"
        return f"{self.contract.asset.name} {type} contract\nPricing method {self.pm}\nPrice (per $): {self.price}\nDelta (per $): {self.delta}\nGamma (per $ per $): {self.gamma}\nVega (per %): {self.vega}\nTheta (per %): {self.theta}\nRho (per %): {self.rho}\n"
