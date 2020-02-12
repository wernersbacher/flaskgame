class Car:

	def __init__(self, id, name, handling, brakes, accel, speed):
		self.id = id
		self.name = name

		self.handling = handling
		self.brakes = brakes
		self.accel = accel
		self.speed = speed

	def getCornerPerformance(self):
		return (4 * self.handling + 2 * self.brakes + 1 * self.accel) / 7

	def getStraightPerformance(self):
		return (4 * self.speed + 1 * self.brakes + 2 * self.accel) / 7
