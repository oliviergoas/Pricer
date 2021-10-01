from contract import Contract

class Barrier(Contract):
    def __init__(self, type, asset, strike, matu, barrier, barrier_dir, barrier_type):
        super().__init__(type, asset, strike, matu)
        self.barrier = barrier
        self.barrier_dir = barrier_dir
        self.barrier_type = barrier_type
