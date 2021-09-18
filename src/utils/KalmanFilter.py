# This is a working prototype. DO NOT USE IT IN LIVE PROJECTS

class KalmanFilter:
	def __init__(self, r, q, a=1, b=0, c=1):
		# R models the process noise and describes how noisy a system internally is.
		# How much noise can be expected from the system itself?
		# When a system is constant R can be set to a (very) low value.
		self.R = r

		# Q resembles the measurement noise.
		# How much noise is caused by the measurements?
		# When it's expected that the measurements will contain most of the noise,
		# it makes sense to set this parameter to a high number (especially in comparison to the process noise).
		self.Q = q

		# Usually you make an estimate of R and Q based on measurements or domain knowledge.
		
		self.A = a # State vector
		self.B = b # Control vector
		self.C = c # Measurement vector

		self.x = float('nan') # estimated signal without noise
		self.cov = 0.0

	# Predict next value
	def __predict(self, u = 0):
		return (self.A * self.x) + (self.B * u)

	# uncertainty of filter
	def __uncertainty(self):
		return (square(self.A) * self.cov) + self.R

	def filter(self, signal, u=0):
		if isNaN(self.x):
			self.x = (1 / self.C) * signal
			self.cov = square(1 / self.C) * self.Q
		else:
			prediction = self.__predict(u)
			uncertainty = self.__uncertainty()

			# Kalman gain
			k_gain = uncertainty * self.C * (1 / ((square(self.C) * uncertainty) + self.Q))

			# correction
			self.x = prediction + k_gain * (signal - (self.C * prediction))
			self.cov = uncertainty - (k_gain * self.C * uncertainty)

		return self.x

def square(x):
	return x * x

def isNaN(num):
	return num != num
