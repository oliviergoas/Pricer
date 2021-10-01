class Contract:
    def __init__(self, type, asset, strike, matu):
        self.type = type
        self.asset = asset
        self.strike = strike
        self.matu = matu

    def get_dictionary(self):
        return {
            "type": self.type,
            "asset": self.asset.get_dictionary(),
            "strike": self.strike,
            "matu": self.matu
        }
