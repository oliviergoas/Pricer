from portfolio import Portfolio
import pprint

from asset import Asset
from call import Call
from put import Put
from barriercall import BarrierCall
from barrierput import BarrierPut
from plotter import Plotter
from pricer import Pricer
from montecarlo import MonteCarlo
from blackscholes import BlackScholes
from gui import Gui

def test_plot(asset):
    plotter = Plotter()
    plotter.plot_time_series(asset.simul_time_series(1))
    call = Call(asset, 100, 1)
    put = Put(asset, 100, 1)
    plotter.plot_call_put_parity(call, put, 50, .1)
    plotter.plot_projections(call, 99, .1)

def test_price_vanilla(asset):
    pricer = Pricer(BlackScholes())
    res = pricer.price(Call(asset, 105, 1))
    pprint.PrettyPrinter(indent=2).pprint(res.get_dictionary())
    print()
    res = pricer.price(Put(asset, 105, 1))
    pprint.PrettyPrinter(indent=2).pprint(res.get_dictionary())

def test_price_barrier(asset):
    pricer = Pricer(MonteCarlo())
    res = pricer.price(BarrierCall(asset, 100, 21/252, 120, "up", "out"))
    pprint.PrettyPrinter(indent=2).pprint(res.get_dictionary())
    print()
    res = pricer.price(BarrierPut(asset, 100, 21/252, 120, "up", "out"))
    pprint.PrettyPrinter(indent=2).pprint(res.get_dictionary())

def test_portfolio(asset):
    pricer = Pricer(BlackScholes())
    res = pricer.price(Portfolio([Call(asset, 105, 1), Put(asset, 105, 1)], [.5, .5]))
    print(res)

def test_implied_volatility(asset):
    pricer = Pricer(BlackScholes())
    print(pricer.implied_volatility(Call(asset, 105, 1), 10)*100, "%")

def test_gui():
    Gui.show_gui()

def main():
    asset = Asset("STOCK", 100, .1, .4)
    # test_plot(asset)
    # test_price_vanilla(asset)
    # test_price_barrier(asset)
    # test_portfolio(asset)
    # test_implied_volatility(asset)
    test_gui()

if __name__ == "__main__":
    main()
