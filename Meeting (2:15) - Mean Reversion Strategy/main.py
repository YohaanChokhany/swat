# region imports
from AlgorithmImports import *

# endregion


class CreativeTanFalcon(QCAlgorithm):

    def initialize(self):
        self.set_start_date(2023, 8, 12)
        self.set_cash(100000)
        self.spy = self.add_equity("SPY", Resolution.Daily).symbol
        self.sma = self.sma(self.spy, 20, Resolution.Daily)

    def on_data(self, data: Slice):
        if not self.sma.is_ready:
            return

        price = data[self.spy].close
        sma_value = self.sma.current.value

        if price < sma_value * 0.98 and not self.portfolio.invested:
            self.market_order(self.spy, 100)

        elif price > sma_value * 1.02 and self.portfolio.invested:
            self.liquidate(self.spy)
