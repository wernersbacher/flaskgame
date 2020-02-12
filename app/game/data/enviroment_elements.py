class Undergrounds:

	def __init__(self, id, name, abrasion, **kwargs):
		self.id = id
		self.name = name
		self.abrasion = abrasion
		self.props = kwargs

class Tyre:

	def __init__(self, id, name, distance, **kwargs):
		self.id = id
		self.name = name
		self.distance = distance
		self.props = kwargs

	def getTyrePerformance(self, underground, etap_length):
		performance_bonus = 0
		# calc performance for normal use
		for prop, val in underground.props.items():
			if prop not in self.props:
				performance_bonus -= val
			else:
				performance_bonus += self.props[prop] - val

		# calc the abrasion in meters done
		lost_tyre_meters = underground.abrasion * etap_length

		return performance_bonus, lost_tyre_meters

class Track:

	def __init__(self, id, undergroundDict, length, straights, corners):
		self.name = id
		self.undergroundDict = undergroundDict
		self.length = length

		self.straights = straights
		self.corners = corners

	def getTyrePerformance(self, tyre):
		if not isinstance(tyre, Tyre):
			raise BaseException("No tyre given")

		summed_performance_bonus = 0
		summed_tyre_meters_lost = 0

		for underground, percent in self.undergroundDict.items():
			etap_multi, lost_tyre_meters = tyre.getTyrePerformance(underground, etap_length=self.length*percent)
			summed_tyre_meters_lost += lost_tyre_meters
			summed_performance_bonus += percent * etap_multi



		tyre_stress = summed_tyre_meters_lost/tyre.distance
		#print(f"performance without stressed tyres is {1+summed_performance_bonus}")
		# if tyre got broken, add negative bonus
		if tyre_stress > 1:
			summed_performance_bonus -= 0.25
		if tyre_stress > 2:
			summed_performance_bonus -= 0.25
		if tyre_stress > 3:
			summed_performance_bonus -= 0.4

		return 1+summed_performance_bonus, tyre_stress

	def getCarPerformance(self, car):

		straight_performance = self.straights * car.getStraightPerformance()
		corner_performance = self.corners * car.getCornerPerformance()

		return (corner_performance+straight_performance)/2

	def getTimeBase(self):
		SPEED_SLOW = 30 #m/s
		SPEED_FAST = 100
		speed_abs = self.corners * SPEED_SLOW + self.straights * SPEED_FAST
		return self.length/speed_abs