from contract import Contract

class Put(Contract):
    def __init__(self, asset, strike, matu):
        super().__init__("Put", asset, strike, matu)

    def expected_payoff(self):
        sT = self.asset.simul_path(self.matu)
        return max(self.strike - sT, 0)
