class Portfolio:
    def __init__(self, contracts, weights):
        if (sum(weights) != 1):
            print("Portfolio: weights must add up to 1")
            exit(1)
        if (len(contracts)) != len(weights):
            print("Portfolio: assets and weights must be of same length")
            exit(1)
        self.contracts = {}
        for contract, weight in zip(contracts, weights):
            self.contracts[contract] = weight
