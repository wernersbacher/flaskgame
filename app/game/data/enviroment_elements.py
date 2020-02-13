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

			if prop not in self.props: # if not there, is 0, so the difference must be -val
				performance_bonus -= val
			else:
				performance_bonus += self.props[prop] - val
			#print(prop, performance_bonus)

		# calc the abrasion in meters done
		lost_tyre_meters = underground.abrasion * etap_length

		#print(f"for {underground.name}: {performance_bonus}")

		return performance_bonus, lost_tyre_meters

class Track:

	def __init__(self, id, name, undergroundDict, length, straights, corners, testOnly=False):
		self.id = id
		self.name = name
		self.testOnly = testOnly
		self.undergroundDict = undergroundDict
		self.length = length

		self.straights = straights
		self.corners = corners

	def getUndergroundDescription(self):
		undergroundStrings = []
		for underground, percent in self.undergroundDict.items():
			undergroundStrings.append(f"{percent*100:.0f}% {underground.name}")

		return ", ".join(undergroundStrings)

	def getCharacter(self):
		""" describe the track character"""

		if self.straights > 0.9:
			return "Very straight"
		if self.straights > 0.65:
			return "Mostly straight with a few corners"
		if self.straights > 0.4:
			return "Equally as much corners as straights"
		if self.straights > 0.2:
			return "Mostly corners with a few straights"
		return "Almost only corners"

	def getDescription(self):
		underground_desc = self.getUndergroundDescription()
		caracter_desc = self.getCharacter()
		return f"{self.name}: {underground_desc} <br/> {self.length} meters long <br/> {caracter_desc} "

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
			summed_performance_bonus -= 0.35
		if tyre_stress > 2:
			summed_performance_bonus -= 0.35
		if tyre_stress > 3:
			summed_performance_bonus -= 0.5

		return 1+2*summed_performance_bonus, tyre_stress

	def getCarPerformance(self, car):

		straight_performance = self.straights * car.getStraightPerformance()
		corner_performance = self.corners * car.getCornerPerformance()

		return (corner_performance+straight_performance)/2

	def getTimeBase(self):
		SPEED_SLOW = 30 #m/s
		SPEED_FAST = 100
		speed_avg = self.corners * SPEED_SLOW + self.straights * SPEED_FAST

		abrasion_avg = 0
		for underground, percent in self.undergroundDict.items():
			abrasion_avg += percent * underground.abrasion

		# the higher the abrasion, the slower the speed
		speed_avg *= 1/abrasion_avg

		return self.length/speed_avg
