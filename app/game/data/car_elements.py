class Car:

	def __init__(self, id, name, handling, brakes, accel, speed):
		self.id = id
		self.name = name

		self.handling = handling
		self.brakes = brakes
		self.accel = accel
		self.speed = speed

	def getPerformanceDesc(self):
		return f"Acceleration: {self.accel*100:.2f}% | Topspeed: {self.speed*100:.2f}% | Handling: {self.handling*100:.2f}% | Brakes: {self.brakes*100:.2f}%"

	def getCompleteDesc(self):
		return f"\"{self.name}\", Performance Rating: <br/> {self.getPerformanceDesc()}"

	def getCornerPerformance(self):
		return (4 * self.handling + 2 * self.brakes + 1 * self.accel) / 7

	def getStraightPerformance(self):
		return (4 * self.speed + 1 * self.brakes + 2 * self.accel) / 7
