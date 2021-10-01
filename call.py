from contract import Contract

class Call(Contract):
    def __init__(self, asset, strike, matu):
        super().__init__("Call", asset, strike, matu)

    def expected_payoff(self):
        sT = self.asset.simul_path(self.matu)
        return max(sT - self.strike, 0)
