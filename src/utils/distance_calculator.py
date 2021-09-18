class Calculadora_distancia():
	def __init__(self, measuredPower, N):
		self.measuredPower=measuredPower
		self.N=N
	def distancia(self, rssi):
		return 10 ** ((self.measuredPower - rssi) / (10 * self.N))

