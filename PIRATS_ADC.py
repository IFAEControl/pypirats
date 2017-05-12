import PIRATS_SPI as Pspi
import PIRATS_ADC_def as Pdef
import time

class ADC:
	def __init__(self):
		self.spiADC = Pspi.SPI_access(0,1)#device, mode
		self.command_config = self.spiADC.set32(0x54835481)
		print hex(self.command_config)
		self.command_config = self.command_config & 0xFFFF
		print "Initial command_config: ",hex(self.command_config)

	def set_diferential_channel(self,channel):
		"""channel 0 it means pin 0 and 1, channel 1 pin 2 and 3, channel 2 pin 0 and 3, channel 3 pin 1 and 3"""
		if channel == 0 :
			self.command_config = ((self.command_config & Pdef.MASKS.CHANNEL) | Pdef.DIFERENTIAL.CH_0_1)
		elif channel == 1 :
			self.command_config = ((self.command_config & Pdef.MASKS.CHANNEL) | Pdef.DIFERENTIAL.CH_2_3)
		elif channel == 2 :
			self.command_config = ((self.command_config & Pdef.MASKS.CHANNEL) | Pdef.DIFERENTIAL.CH_0_3)
		elif channel == 3 :
			self.command_config = ((self.command_config & Pdef.MASKS.CHANNEL) | Pdef.DIFERENTIAL.CH_1_3)
		else:
			print "set_diferential_channel: Channel value not valid"

	def set_single_ended_channel(self,channel):
		"""channel 0 to 3"""
		if channel == 0 :
			self.command_config = ((self.command_config & Pdef.MASKS.CHANNEL) | Pdef.SINGLE_ENDED.CH_0)
		elif channel == 1 :
			self.command_config = ((self.command_config & Pdef.MASKS.CHANNEL) | Pdef.SINGLE_ENDED.CH_1)
		elif channel == 2 :
			self.command_config = ((self.command_config & Pdef.MASKS.CHANNEL) | Pdef.SINGLE_ENDED.CH_2)
		elif channel == 3 :
			self.command_config = ((self.command_config & Pdef.MASKS.CHANNEL) | Pdef.SINGLE_ENDED.CH_3)
		else:
			print "set_single_ended_channel: Channel value not valid"

	def start_single_conversion(self,start):
		""" Start single conversion. Check operation mode"""
		if start == 1:
			self.command_config = ((self.command_config & Pdef.MASKS.SINGLE_CONVERSION) | Pdef.SINGLE_CONVERSION.ON)
		elif start == 0:
			self.command_config = ((self.command_config & Pdef.MASKS.SINGLE_CONVERSION) | Pdef.SINGLE_CONVERSION.OFF)
		else:
			print "start_single_conversion: Value to start not valid"

	def set_programable_gain(self,gain):
		"""Programable FSR (V). 0 = 6.144V, 1 = 4.096 V, 2 = 2048 V (default), 3 = 1.024 V, 4 = 0.512 V, 5 = 0.256 V. Take of the electrical limints"""
		if gain == 0:
			 self.command_config = ((self.command_config & Pdef.MASKS.PROGRAMABLE_GAIN) | Pdef.PROGRAMABLE_GAIN.G6144)
		elif gain == 1:
 			 self.command_config = ((self.command_config & Pdef.MASKS.PROGRAMABLE_GAIN) | Pdef.PROGRAMABLE_GAIN.G4096)
		elif gain == 2:
 			 self.command_config = ((self.command_config & Pdef.MASKS.PROGRAMABLE_GAIN) | Pdef.PROGRAMABLE_GAIN.G2048)
		elif gain == 3:
			 self.command_config = ((self.command_config & Pdef.MASKS.PROGRAMABLE_GAIN) | Pdef.PROGRAMABLE_GAIN.G1024)
		elif gain == 4:
			 self.command_config = ((self.command_config & Pdef.MASKS.PROGRAMABLE_GAIN) | Pdef.PROGRAMABLE_GAIN.G0512)
		elif gain == 5:
			 self.command_config = ((self.command_config & Pdef.MASKS.PROGRAMABLE_GAIN) | Pdef.PROGRAMABLE_GAIN.G0256)
		else:
			print "set_programable_gain: Gain value not valid"

	def set_mode(self,mode):
		""" O = continuous working mode. 1 = Power down single conversion working mode"""
		if mode == 1:
			self.command_config = ((self.command_config & Pdef.MASKS.MODE) | Pdef.MODE.POWER_DOWN)
		elif mode == 0:
			self.command_config = ((self.command_config & Pdef.MASKS.MODE) | Pdef.MODE.CONTINUOUS)
		else:
			print "set_mode: Not valid mode"

	def set_data_rate(self,data_rate):
		"""Programable data rate. 0 = 128 SPS, 1 = 250 SPS, 2 = 490 SPS, 3 = 920 SPS, 4 = 1600 SPS (default), 5 = 2400 SPS, 6 = 3300 SPS"""
		if data_rate == 0:
			 self.command_config = ((self.command_config & Pdef.MASKS.DATA_RATE) | Pdef.DATA_RATE.DR0128)
		elif data_rate == 1:
 			 self.command_config = ((self.command_config & Pdef.MASKS.DATA_RATE) | Pdef.DATA_RATE.DR0250)
		elif data_rate == 2:
 			 self.command_config = ((self.command_config & Pdef.MASKS.DATA_RATE) | Pdef.DATA_RATE.DR0490)
		elif data_rate == 3:
			 self.command_config = ((self.command_config & Pdef.MASKS.DATA_RATE) | Pdef.DATA_RATE.DR0920)
		elif data_rate == 4:
			 self.command_config = ((self.command_config & Pdef.MASKS.DATA_RATE) | Pdef.DATA_RATE.DR1600)
		elif data_rate == 5:
			 self.command_config = ((self.command_config & Pdef.MASKS.DATA_RATE) | Pdef.DATA_RATE.DR2400)
		elif data_rate == 6:
			 self.command_config = ((self.command_config & Pdef.MASKS.DATA_RATE) | Pdef.DATA_RATE.DR3300)
		else:
			print "set_data_rate: Data rate not valid"

	def set_ts_mode(self,ts_mode):
		""" O = OFF temperature sensor mode, ON ADC mode.
		    1 = ON temperature mode, OFF ADC mode"""
		if ts_mode == 1:
			self.command_config = ((self.command_config & Pdef.MASKS.TS_MODE) | Pdef.TS_MODE.ON)
		elif ts_mode == 0:
			self.command_config = ((self.command_config & Pdef.MASKS.TS_MODE) | Pdef.TS_MODE.OFF)
		else:
			print "set_ts_mode: Not valid temperature sensor mode"

	def set_pull_up(self,pull_up):
		""" O = disable pull up resistor for DOUT/DRY. 1 = enable it"""
		if pull_up == 1:
			self.command_config = ((self.command_config & Pdef.MASKS.PULL_UP) | Pdef.PULL_UP.ON)
		elif pull_up == 0:
			self.command_config = ((self.command_config & Pdef.MASKS.PULL_UP) | Pdef.PULL_UP.OFF)
		else:
			print "set_putll_up: Not valid pull_up on/off value"

	def set_nop(self,nop):
		""" O = Not operation, not actualize config register.
		    1 = Valid operation, actualize register """
		if nop == 1:
			self.command_config = ((self.command_config & Pdef.MASKS.NOP) | Pdef.NOP.VALID)
		elif nop == 0:
			self.command_config = ((self.command_config & Pdef.MASKS.NOP) | Pdef.NOP.NOT_VALID)
		else:
			print "set_nop: Not valid data valid"

	def set_command_config(self):
		""" Send the config comand by SPI to the ADC"""
		self.command_config = self.command_config | 0x0001#last bit always has to be 1
		self.spiADC.set(self.command_config)

	def get_data(self):
		dada = self.spiADC.set(0x0001)#any number
		return dada

	def print_command_config(self):
		print "print_command_config (hex): ",hex(self.command_config)

if __name__ == '__main__':
	print "If you are using PIRATS V0, remember to remove MISO as output from PWM. Enjoy!!!"
	adc = ADC() #Initialize configuration word.
	adc.print_command_config() #print command config value
	adc.set_single_ended_channel(0) #Channel 1 selected
	adc.set_programable_gain(2) # FSR 2.048 V
	adc.set_mode(0)#continuso working mode
	adc.set_ts_mode(0)#ADC mode
	adc.set_pull_up(0)#No pull up resistor
	adc.set_nop(1)#Data to send valid
	adc.set_data_rate(4)
	adc.set_command_config() #Write command config to ADC
	adc.print_command_config() #print command config value
	adc.print_command_config() #print command config value
	adc.print_command_config() #print command config value
	adc.print_command_config() #print command config value
	while True:
		try:
			dada = adc.get_data()
			time.sleep(0.1)
			print "dada: ", hex(dada)

		except KeyboardInterrupt:
			print "Program has gone"
			break
