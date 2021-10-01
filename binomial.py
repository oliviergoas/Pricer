from pricingmethod import PricingMethod

class Binomial(PricingMethod):
    def __init__(self):
        self.method = "Binomial"

    def compute_price(self, contract):
        return "not implemented"

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
