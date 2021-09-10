# https://blog.mapbox.com/fast-geodesic-approximations-with-cheap-ruler-106f229ad016
import math
import pandas as pd

RE = 6378.137 # equatorial radius
FE = 1 / 298.257223563 # flattening

PI = 3.14
E2 = FE * (2 - FE)
RAD = math.pi / 180

# df = pd.read_csv('1.csv')
def wrap(deg):
	while(deg < -180): deg += 360
	while (deg > 180): deg -= 360

	return deg


class CheapRule:
	def __init__(self, lat, df):
		units = 1000
		coslat = math.cos(lat * RAD)
		m = RAD * RE * units
		w2 = 1 / (1 - E2 * (1 - coslat * coslat))
		w = math.sqrt(w2)

		self.kx = m * w * coslat
		self.ky = m * w * w2 * (1 - E2)

		self.df = df
	

	def distance(self, a, b):
		dx = wrap(a[0] - b[0]) * self.kx
		dy = (a[1] - b[1]) * self.ky
		return math.sqrt(dx * dx + dy * dy)

	def default_callback(self, x, thresold=1.0, mcc=[]):
		# thresold_in_km
		# return 1 and 1
		# medan = [3.5952, 98.672226]
		# mcc = medan
		lat_index = 1
		lng_index = 2
		xx =  x[lat_index] < mcc[0] -thresold  or mcc[0] + thresold > x[lat_index]
		yy = x[lng_index] < mcc[1] -thresold or mcc[1] + thresold > x[lng_index]
		
		return xx and yy

	def addition(self, x=[], to=[]):
		result = self.distance(to, [x[1], x[2]])
		# print(x[0])
		return [x[0], result]
		
	def filter(self, mc=[]):
		less_than_zero = list(filter(lambda x: self.default_callback(x, thresold=1.0, mcc=mc), self.df.values))
		# print(a)
		result = map(lambda x: self.addition(x, mc), less_than_zero)
		r = sorted(result, key=lambda x: x[1])

		# print(r)

		if len(r) < 1:
			return ""

		return r[0][0]


# medan = [3.5952, 98.672226]
# bandung = [-6.914744, 107.609810]
# bekasi = [-6.241586, 106.992416]
# bogor = [-6.586520, 106.808339]

# mcc = medan
# p1 = CheapRule(mcc[0])


# areas = [medan, bandung, bekasi, bogor]

# # 1 degre = 111 km
# def callback(x, thresold=1.0):
# 	# thresold_in_km
# 	lat_index = 1
# 	lng_index = 2
# 	xx =  x[lat_index] < mcc[0] -thresold  or mcc[0] + thresold > x[lat_index]
# 	yy = x[lng_index] < mcc[1] -thresold or mcc[1] + thresold > x[lng_index]
	
# 	return xx and yy


# less_than_zero = list(filter(lambda x: callback(x, thresold=1), df.values))

# def addition(x):
# 	result = p1.distance(medan, [x[1], x[2]])
# 	return [x[0], result]

# result = map(addition, less_than_zero)

# r = sorted(result, key=lambda x: x[1])

# # print(r)
