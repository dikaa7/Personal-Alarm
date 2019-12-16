import time


class Time(object):
	""" docstring for Time"""
	""" hours = 0
	minutes = 0
	seconds = 0"""
	def __init__(self, hours=0, minutes=0, seconds=0):
		super(Time, self).__init__()
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds

	def clock(self):
		while True:
			print(str(self.hours).zfill(2) + ":" + str(self.minutes).zfill(2) + ":" + str(self.seconds).zfill(2))
			time.sleep(1)
			self.seconds += 1
			if not self.isSecondValid():
				self.seconds -= 60
				self.minutes += 1
			if not self.isMinutesValid():
				self.minutes -= 60
				self.hours += 1

	def timer(self):
		while True:
			if(self.isTimerOff()):
				print("Time Off")
				break
			else:
				print(str(self.hours).zfill(2) + ":" + str(self.minutes).zfill(2) + ":" + str(self.seconds).zfill(2))
				time.sleep(1)
				self.seconds -= 1
				if not self.isSecondValid():
					self.seconds += 60
					self.minutes -= 1
				if not self.isMinutesValid():
					self.minutes += 60
					self.hours -= 1

	def isTimerOff(self):
		return (self.hours == 0) and (self.minutes == 0) and (self.seconds == 0)

	def isSecondValid(self):
		return (self.seconds >= 0) and (self.seconds < 60)

	def isMinutesValid(self):
		return (self.minutes >= 0) and (self.minutes < 60)

	def isHoursValid(self):
		return (self.hours >= 0) and (self.hours < 24)

	def minutesToHours(self):
		self.hours = 0
		while(not self.isSecondValid()):
			self.hours += 1
			self.seconds -= 60
		return self.hours


clock = Time(0, 0, 0)
clock.timer()
print("Anda Keluar dari Timer")
