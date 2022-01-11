from gpiozero import PWMLED
from .chips.ADC120 import *
from .chips.MAX31856 import *
import spilite.spi as spi
from spilite.cs.decoders import AddressDecoder, ChipSelectDecoder
from spilite.cs.pins import ChipSelectPin, ActiveHighPin
from time import sleep

class Controller:
    def __init__(self, T_channels=[i for i in range(8)], spi_bus_speed_hz=2000000):
        self.status_leds = [PWMLED(i) for i in range(22,26)]
        addr_demux = AddressDecoder([5,6,12], ActiveHighPin(13))
        self.probe_T = [MAX31856(spi.Port(
            cs=ChipSelectDecoder(i,addr_demux),
            max_speed_hz=spi_bus_speed_hz,
            mode=0b11)) for i in T_channels]
        cs_ADC = ChipSelectPin(21)
        cs_ADC.unselect()
        self.probe_P = ADC120(spi.Port(
            cs=cs_ADC,
            max_speed_hz=spi_bus_speed_hz,
            mode=0b11))

    def blink_start(self):
        for d in self.status_leds:
            d.value = 0.4
            sleep(0.25)
    
        for d in self.status_leds:
            d.value = 0
    
    def read_P(self, ch, oversample=3):
        ch = self._validate_ch(ch)  # raises RuntimeError if out of range
        P_ch = []
        for i in ch:
            P_ch.extend([i]*oversample)
        raw_P = self.probe_P.readn(ch=P_ch)
        result = [(ch[i], raw_P[oversample*(i+1)-1]) for i in range(len(ch))]
        return result
        
    def read_T(self, ch):
        ch = self._validate_ch(ch)  # raises RuntimeError if out of range
        result = []
        for i in ch:
            status = self.probe_T[i].faults()
            ch_faults = [k for k,v in status.items() if v]
            ch_T = round(self.probe_T[i].temperature,2)
            result.append((i, ch_T, ch_faults))
        return result
       
    def _validate_ch(self,ch):  
        if isinstance(ch,int):
            ch = [ch]
        if any([i < 0 or i >= 8 for i in ch]):
            raise RuntimeError("Pressure channel index out of range")
        return ch
