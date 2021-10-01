from barrier import Barrier

class BarrierPut(Barrier):
    def __init__(self, asset, strike, matu, barrier, barrier_dir, barrier_type):
        barrier_dir = barrier_dir.lower()
        barrier_type = barrier_type.lower()
        super().__init__(f"Barrier Put {barrier_dir} and {barrier_type}", asset, strike, matu, barrier, barrier_dir, barrier_type)

    def expected_payoff(self):
        values = self.asset.simul_time_series(self.matu)
        if self.barrier_dir == "up":
            crossed = not all(i < self.barrier for i in values)
        elif self.barrier_dir == "down":
            crossed = not all(i > self.barrier for i in values)
        if (self.barrier_type == "in" and crossed is False) or (self.barrier_type == "out" and crossed is True):
            return 0
        return max(self.strike - values[-1], 0)
