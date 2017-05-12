import spidev
class SPI_access:
	def __init__(self, device, mode):
		self.spi = spidev.SpiDev()
		self.spi.open(0,device)#DAC bus and device
		self.spi.max_speed_hz = 100000
		self.spi.mode = mode#DAC working mode

	def set(self,input):
		msb = input >> 8
		msb = msb & 0xFF
		lsb = input & 0xFF
		data = self.spi.xfer([msb, lsb])
		return ((data[0] << 8) + data[1])

	def set32(self,input):
		msb2 = input >> 24
		msb = msb2 & 0xFF
		lsb2 = input >> 16
		lsb2 = lsb2 & 0xFF
		msb = input >> 8
		msb = msb & 0xFF
		lsb = input & 0xFF
		data = self.spi.xfer([msb2,lsb2, msb, lsb])
		#print "Faking SPI. msb %s, lsb %s", hex(msb), hex(lsb)
		#data = input
		return ((data[0] << 24) + (data[1] << 16) + (data[2] << 8) + data[3])

	def close():
		self.spi.close()
		print "Faking SPI. Close()"
