import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    """
    1st-order sigma-delta modulator (1-bit)
    """
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='sdm1',
            in_sig=[np.float32],
            out_sig=[np.float32],
        )
        self.acc = 0.0

    def work(self, input_items, output_items):
        x = input_items[0]
        y = output_items[0]

        for n in range(len(x)):
            bit = 1.0 if self.acc >= 0.0 else 0.0
            self.acc += float(x[n]) - bit
            y[n] = bit

        return len(y)
