
#ADC definitions masks
class DIFERENTIAL:
	"""CH_X_Y. Channel between pin X and Y"""
	CH_0_1 = 0x0000
	CH_0_3 = 0x1000
	CH_1_3 = 0x2000
	CH_2_3 = 0x3000

class SINGLE_ENDED:
	"""CH_X. Channel in pin X"""
	CH_0 = 0x4000
	CH_1 = 0x5000
	CH_2 = 0x6000
	CH_3 = 0x7000

class SINGLE_CONVERSION:
	"""Start single shot conversion. Check pin 8 from config word."""
	ON = 0x8000
	OFF = 0x0000

class PROGRAMABLE_GAIN:
	"""Programable FSR (V) gain"""
	G6144 = 0x0000
	G4096 = 0x0200
	G2048 = 0x0400
	G1024 = 0x0600
	G0512 = 0x0800
	G0256 = 0x0A00

class MODE:
	"""Device operation mode. 0 = continuous-conversion mode. 1 = Power-down and single-shot mode (default) """
	CONTINUOUS = 0x0000
	POWER_DOWN = 0x0100

class DATA_RATE:
	"""Data rate setting. DRxxx where xxx is SPS data rate"""
	DR0128 = 0x0000
	DR0250 = 0x0020
	DR0490 = 0x0040
	DR0920 = 0x0060
	DR1600 = 0x0080
	DR2400 = 0x00C0
	DR3300 = 0x00E0

class TS_MODE:
	"""Temperature sensor mode"""
	ON = 0x0010
	OFF = 0x0000
class PULL_UP:
	"""Pullup resistor enable on DOUT/DRDY"""
	ON = 0x0008
	OFF = 0x0000

class NOP:
	"""No operation. Data are written to th e config resgister or not"""
	VALID = 0x0002
	NOT_VALID = 0x0000
class MASKS:
	"""Mask to reset the values to change"""
	CHANNEL = 0x8FFF
	SINGLE_CONVERSION = 0x7FFF
	PROGRAMABLE_GAIN = 0xF1FF
	MODE = 0xFEFF
	DATA_RATE = 0xFF1F
	TS_MODE = 0xFFEF
	PULL_UP = 0xFFF7
	NOP = 0xFFF9
