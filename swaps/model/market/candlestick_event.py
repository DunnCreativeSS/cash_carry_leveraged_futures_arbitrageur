from swaps.constant import *
from swaps.model.market import *


class CandlestickEvent:
    """
    The candlestick/kline data received by subscription of candlestick/kline.

    :member
        ch: the topic you subscribed
        ts: the UNIX formatted timestamp generated by server in UTC.
        tick: the data of candlestick/kline.
    """

    def __init__(self):
        self.ch = ""
        self.ts = 0
        self.tick = Candlestick()


    def print_object(self, format_data=""):
        from swaps.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.ts, format_data + "Unix Time")
        PrintBasic.print_basic(self.ch, format_data + "Channel")
        if self.tick:
            self.tick.print_object()
