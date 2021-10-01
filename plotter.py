import numpy as np
import matplotlib.pyplot as plt

from pricer import Pricer
from blackscholes import BlackScholes

class Plotter:
    def plot_time_series(self, values):
        plt.plot([i+1 for i in range(252)], values, 'b')
        plt.xlabel("Time (per day)")
        plt.ylabel("Value (per $)")
        plt.show()

    def plot_call_put_parity(self, call, put, n, p):
        pricer = Pricer(BlackScholes())
        beg = max(call.strike - n, 0)
        end = call.strike + n
        spots = np.arange(beg, end, p)
        plt.plot(spots, pricer.price_projection(call, spots), 'y', label="Call value")
        plt.plot(spots, pricer.price_projection(put, spots), 'b', label="Put value")
        plt.xlabel("Spot (per $)")
        plt.ylabel("Contract price (per $)")
        plt.legend()
        plt.show()

    def plot_projections(self, contract, n, p):
        pricer = Pricer(BlackScholes())
        beg = max(contract.strike - n, 1)
        end = contract.strike + n
        spots = np.arange(beg, end, p)
        fig, axs = plt.subplots(3, 2)
        axs[0, 0].plot(spots, pricer.price_projection(contract, spots), 'b')
        axs[0, 0].set_title("Price")
        axs[0, 1].plot(spots, pricer.delta_projection(contract, spots), 'b')
        axs[0, 1].set_title("Delta")
        axs[1, 0].plot(spots, pricer.gamma_projection(contract, spots), 'b')
        axs[1, 0].set_title("Gamma")
        axs[1, 1].plot(spots, pricer.vega_projection(contract, spots), 'b')
        axs[1, 1].set_title("Vega")
        axs[2, 0].plot(spots, pricer.theta_projection(contract, spots), 'b')
        axs[2, 0].set_title("Theta")
        axs[2, 1].plot(spots, pricer.rho_projection(contract, spots), 'b')
        axs[2, 1].set_title("Rho")
        fig.tight_layout()
        plt.show()

    def plot_price_projection(self, contract, n, p):
        pricer = Pricer(BlackScholes())
        beg = max(contract.strike - n, 0)
        end = contract.strike + n
        spots = np.arange(beg, end, p)
        plt.plot(spots, pricer.price_projection(contract, spots), 'b')
        plt.xlabel("Spot (per $)")
        plt.ylabel("Contract price (per $)")
        plt.legend()
        plt.show()

    def plot_delta_projection(self, contract, n, p):
        pricer = Pricer(BlackScholes())
        beg = max(contract.strike - n, 0)
        end = contract.strike + n
        spots = np.arange(beg, end, p)
        plt.plot(spots, pricer.delta_projection(contract, spots), 'b')
        plt.xlabel("Spot (per $)")
        plt.ylabel("Delta (per $)")
        plt.show()

    def plot_gamma_projection(self, contract, n, p):
        pricer = Pricer(BlackScholes())
        beg = max(contract.strike - n, 0)
        end = contract.strike + n
        spots = np.arange(beg, end, p)
        plt.plot(spots, pricer.gamma_projection(contract, spots), 'b')
        plt.xlabel("Spot (per $)")
        plt.ylabel("Gamma (per $ per $)")
        plt.show()

    def plot_vega_projection(self, contract, n, p):
        pricer = Pricer(BlackScholes())
        beg = max(contract.strike - n, 0)
        end = contract.strike + n
        spots = np.arange(beg, end, p)
        plt.plot(spots, pricer.vega_projection(contract, spots), 'b')
        plt.xlabel("Spot (per $)")
        plt.ylabel("Vega (per %)")
        plt.show()

    def plot_theta_projection(self, contract, n, p):
        pricer = Pricer(BlackScholes())
        beg = max(contract.strike - n, 0)
        end = contract.strike + n
        spots = np.arange(beg, end, p)
        plt.plot(spots, pricer.theta_projection(contract, spots), 'b')
        plt.xlabel("Spot (per $)")
        plt.ylabel("Theta (per %)")
        plt.show()

    def plot_rho_projection(self, contract, n, p):
        pricer = Pricer(BlackScholes())
        beg = max(contract.strike - n, 0)
        end = contract.strike + n
        spots = np.arange(beg, end, p)
        plt.plot(spots, pricer.rho_projection(contract, spots), 'b')
        plt.xlabel("Spot (per $)")
        plt.ylabel("Rho (per %)")
        plt.show()
