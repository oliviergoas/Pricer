import tkinter as tk
import tkinter.ttk as ttk

from asset import Asset
from call import Call
from put import Put
from barriercall import BarrierCall
from barrierput import BarrierPut
from pricer import Pricer
from montecarlo import MonteCarlo
from blackscholes import BlackScholes

class Gui:
    @staticmethod
    def show_gui():
        window = tk.Tk()

        window.title("Options Valuation and Risk Measures")
        window.rowconfigure([0,1,2,3,4,5,6,7,8,9,10,11,12], minsize=50, weight=1)
        window.columnconfigure([0,1,2,3,4,5,6,7,8,9], minsize=120, weight=1)

        lbl_input = tk.Label(master=window, text="Input Data", fg="white", bg="#204468")
        lbl_input.grid(row=0, column=0, sticky="snew")

        lbl_model = tk.Label(master=window, text="Pricing Method")
        lbl_model.grid(row=1, column=0)
        cbx_model = ttk.Combobox(master=window, values=["Black Scholes", "Monte Carlo"])
        cbx_model.current(0)
        cbx_model.grid(row=1, column=1)

        lbl_spot = tk.Label(master=window, text="Asset Price")
        lbl_spot.grid(row=2, column=0)
        sbx_spot = tk.Spinbox(master=window, from_=0.0, to=9999.0)
        sbx_spot.grid(row=2, column=1)

        lbl_rf = tk.Label(master=window, text="Risk-free Rate (% per year)")
        lbl_rf.grid(row=3, column=0)
        sbx_rf = tk.Spinbox(master=window, from_=0.0, to=100.0)
        sbx_rf.grid(row=3, column=1)

        lbl_vol = tk.Label(master=window, text="Volatility (% per year)")
        lbl_vol.grid(row=4, column=0)
        sbx_vol = tk.Spinbox(master=window, from_=0.0, to=100.0)
        sbx_vol.grid(row=4, column=1)

        lbl_matu = tk.Label(master=window, text="Time to Maturity (days)")
        lbl_matu.grid(row=5, column=0)
        sbx_matu = tk.Spinbox(master=window, from_=0.0, to=9999.0)
        sbx_matu.grid(row=5, column=1)

        lbl_strike = tk.Label(master=window, text="Excercise Price")
        lbl_strike.grid(row=6, column=0)
        sbx_strike = tk.Spinbox(master=window, from_=0.0, to=9999.0)
        sbx_strike.grid(row=6, column=1)

        lbl_barrier_price = tk.Label(master=window, text="Barrier Price")
        lbl_barrier_price.grid(row=8, column=0)
        sbx_barrier_price = tk.Spinbox(master=window, from_=0.0, to=9999.0)
        sbx_barrier_price.grid(row=8, column=1)

        lbl_barrier_dir = tk.Label(master=window, text="Barrier Direction")
        lbl_barrier_dir.grid(row=9, column=0)
        cbx_barrier_dir = ttk.Combobox(master=window, values=["Up", "Down"])
        cbx_barrier_dir.current(0)
        cbx_barrier_dir.grid(row=9, column=1)

        lbl_barrier_type = tk.Label(master=window, text="Barrier Type")
        lbl_barrier_type.grid(row=10, column=0)
        cbx_barrier_type = ttk.Combobox(master=window, values=["In", "Out"])
        cbx_barrier_type.current(0)
        cbx_barrier_type.grid(row=10, column=1)



        lbl_results = tk.Label(master=window, text="Results", fg="white", bg="#204468")
        lbl_results.grid(row=0, column=3, sticky="snew")

        lbl_price = tk.Label(master=window, text="Price")
        lbl_price.grid(row=2, column=3)

        lbl_delta = tk.Label(master=window, text="Delta")
        lbl_delta.grid(row=3, column=3)

        lbl_gamma = tk.Label(master=window, text="Gamma")
        lbl_gamma.grid(row=4, column=3)

        lbl_vega = tk.Label(master=window, text="Vega")
        lbl_vega.grid(row=5, column=3)

        lbl_theta = tk.Label(master=window, text="Theta")
        lbl_theta.grid(row=6, column=3)

        lbl_rho = tk.Label(master=window, text="Rho")
        lbl_rho.grid(row=7, column=3)



        lbl_call = tk.Label(master=window, text="Call", font="Helvetica 14 bold")
        lbl_call.grid(row=1, column=4)
        
        lbl_price_call = tk.Label(master=window, bg="white", anchor="e")
        lbl_price_call.grid(row=2, column=4, sticky="ew")

        lbl_delta_call = tk.Label(master=window, bg="white", anchor="e")
        lbl_delta_call.grid(row=3, column=4, sticky="ew")

        lbl_gamma_call = tk.Label(master=window, bg="white", anchor="e")
        lbl_gamma_call.grid(row=4, column=4, sticky="ew")

        lbl_vega_call = tk.Label(master=window, bg="white", anchor="e")
        lbl_vega_call.grid(row=5, column=4, sticky="ew")

        lbl_theta_call = tk.Label(master=window, bg="white", anchor="e")
        lbl_theta_call.grid(row=6, column=4, sticky="ew")

        lbl_rho_call = tk.Label(master=window, bg="white", anchor="e")
        lbl_rho_call.grid(row=7, column=4, sticky="ew")



        lbl_put = tk.Label(master=window, text="Put", font="Helvetica 14 bold")
        lbl_put.grid(row=1, column=5)

        lbl_price_put = tk.Label(master=window, bg="white", anchor="e")
        lbl_price_put.grid(row=2, column=5, sticky="ew")
        
        lbl_delta_put = tk.Label(master=window, bg="white", anchor="e")
        lbl_delta_put.grid(row=3, column=5, sticky="ew")
        
        lbl_gamma_put = tk.Label(master=window, bg="white", anchor="e")
        lbl_gamma_put.grid(row=4, column=5, sticky="ew")
        
        lbl_vega_put = tk.Label(master=window, bg="white", anchor="e")
        lbl_vega_put.grid(row=5, column=5, sticky="ew")
        
        lbl_theta_put = tk.Label(master=window, bg="white", anchor="e")
        lbl_theta_put.grid(row=6, column=5, sticky="ew")
        
        lbl_rho_put = tk.Label(master=window, bg="white", anchor="e")
        lbl_rho_put.grid(row=7, column=5, sticky="ew")



        lbl_barrier_call = tk.Label(master=window, text="Barrier Call", font="Helvetica 14 bold")
        lbl_barrier_call.grid(row=1, column=7)

        lbl_barrier_price_call = tk.Label(master=window, bg="white", anchor="e")
        lbl_barrier_price_call.grid(row=2, column=7, sticky="ew")

        lbl_barrier_delta_call = tk.Label(master=window, bg="white", anchor="e")
        lbl_barrier_delta_call.grid(row=3, column=7, sticky="ew")

        lbl_barrier_gamma_call = tk.Label(master=window, bg="white", anchor="e")
        lbl_barrier_gamma_call.grid(row=4, column=7, sticky="ew")

        lbl_barrier_vega_call = tk.Label(master=window, bg="white", anchor="e")
        lbl_barrier_vega_call.grid(row=5, column=7, sticky="ew")

        lbl_barrier_theta_call = tk.Label(master=window, bg="white", anchor="e")
        lbl_barrier_theta_call.grid(row=6, column=7, sticky="ew")

        lbl_barrier_rho_call = tk.Label(master=window, bg="white", anchor="e")
        lbl_barrier_rho_call.grid(row=7, column=7, sticky="ew")



        lbl_barrier_put = tk.Label(master=window, text="Barrier Put", font="Helvetica 14 bold")
        lbl_barrier_put.grid(row=1, column=8)
        
        lbl_barrier_price_put = tk.Label(master=window, bg="white", anchor="e")
        lbl_barrier_price_put.grid(row=2, column=8, sticky="ew")
        
        lbl_barrier_delta_put = tk.Label(master=window, bg="white", anchor="e")
        lbl_barrier_delta_put.grid(row=3, column=8, sticky="ew")
        
        lbl_barrier_gamma_put = tk.Label(master=window, bg="white", anchor="e")
        lbl_barrier_gamma_put.grid(row=4, column=8, sticky="ew")

        lbl_barrier_vega_put = tk.Label(master=window, bg="white", anchor="e")
        lbl_barrier_vega_put.grid(row=5, column=8, sticky="ew")
        
        lbl_barrier_theta_put = tk.Label(master=window, bg="white", anchor="e")
        lbl_barrier_theta_put.grid(row=6, column=8, sticky="ew")

        lbl_barrier_rho_put = tk.Label(master=window, bg="white", anchor="e")
        lbl_barrier_rho_put.grid(row=7, column=8, sticky="ew")



        def price_and_display_vanilla():
            pricer = None
            if cbx_model.get() == "Black Scholes":
                pricer = Pricer(BlackScholes())
            elif cbx_model.get() == "Monte Carlo":
                pricer = Pricer(MonteCarlo())
            if pricer is None:
                print("Wrong input: please select revelant pricing method")
                return
            asset = Asset("stock", float(sbx_spot.get()), float(sbx_rf.get())/100.0, float(sbx_vol.get())/100.0)

            res = pricer.price(Call(asset, float(sbx_strike.get()), float(sbx_matu.get())/252))
            if res.price < 0:
                lbl_price_call.config(fg= "red")
            lbl_price_call["text"] = res.price
            if res.delta < 0:
                lbl_delta_call.config(fg= "red")
            lbl_delta_call["text"] = res.delta
            if res.gamma < 0:
                lbl_gamma_call.config(fg= "red")
            lbl_gamma_call["text"] = res.gamma
            if res.vega < 0:
                lbl_vega_call.config(fg= "red")
            lbl_vega_call["text"] = res.vega
            if res.theta < 0:
                lbl_theta_call.config(fg= "red")
            lbl_theta_call["text"] = res.theta
            if res.rho < 0:
                lbl_rho_call.config(fg= "red")
            lbl_rho_call["text"] = res.rho

            res = pricer.price(Put(asset, float(sbx_strike.get()), float(sbx_matu.get())/252))
            if res.price < 0:
                lbl_price_put.config(fg= "red")
            lbl_price_put["text"] = res.price
            if res.delta < 0:
                lbl_delta_put.config(fg= "red")
            lbl_delta_put["text"] = res.delta
            if res.gamma < 0:
                lbl_gamma_put.config(fg= "red")
            lbl_gamma_put["text"] = res.gamma
            if res.vega < 0:
                lbl_vega_put.config(fg= "red")
            lbl_vega_put["text"] = res.vega
            if res.theta < 0:
                lbl_theta_put.config(fg= "red")
            lbl_theta_put["text"] = res.theta
            if res.rho < 0:
                lbl_rho_put.config(fg= "red")
            lbl_rho_put["text"] = res.rho



        def price_and_display_barrier():
            pricer = None
            if cbx_model.get() == "Monte Carlo":
                pricer = Pricer(MonteCarlo())
            if pricer is None:
                print("Wrong input: please select revelant pricing method")
                return
            asset = Asset("stock", float(sbx_spot.get()), float(sbx_rf.get())/100.0, float(sbx_vol.get())/100.0)

            res = pricer.price(BarrierCall(asset, float(sbx_strike.get()), float(sbx_matu.get())/252, float(sbx_barrier_price.get()), cbx_barrier_dir.get(), cbx_barrier_type.get()))
            if res.price < 0:
                lbl_barrier_price_call.config(fg= "red")
            lbl_barrier_price_call["text"] = res.price

            res = pricer.price(BarrierPut(asset, float(sbx_strike.get()), float(sbx_matu.get())/252, float(sbx_barrier_price.get()), cbx_barrier_dir.get(), cbx_barrier_type.get()))
            if res.price < 0:
                lbl_barrier_price_put.config(fg= "red")
            lbl_barrier_price_put["text"] = res.price



        btn_price_vanilla = ttk.Button(window, text="Price Vanilla", command=price_and_display_vanilla)
        btn_price_vanilla.grid(row=7, column=1)

        btn_price_barrier = ttk.Button(window, text="Price Barrier", command=price_and_display_barrier)
        btn_price_barrier.grid(row=11, column=1)

        window.mainloop()
