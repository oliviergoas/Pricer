import numpy as np

class Asset:
    def __init__(self, name, spot, rf, vol):
        self.name = name
        self.spot = spot
        self.rf = rf
        self.vol = vol

    def simul_path(self, years):
        drift = (self.rf - self.vol ** 2 / 2) * years
        alea = self.vol * np.random.normal(0,1) * np.sqrt(years)
        return self.spot * np.exp(drift + alea)

    def simul_time_series(self, years):
        day = 1/252
        spot = self.spot
        values = [spot]
        for _ in np.arange(2*day, years, day):
            drift = (self.rf - self.vol ** 2 / 2) * day
            alea = self.vol * np.random.normal(0,1) * np.sqrt(day)
            spot = spot * np.exp(drift + alea)
            values.append(spot)
        return values

    def get_dictionary(self):
        return {
            "name": self.name,
            "spot": self.spot,
            "risk-free rate": self.rf,
            "volatility": self.vol
        }
