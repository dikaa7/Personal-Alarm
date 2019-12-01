import time
import tkinter
seconds = 55
minutes = 45
hours = 2


def clock(hours, minutes, seconds):
	while True:
		print(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2))
		time.sleep(1)

		seconds += 1
		if not isSecondValid(seconds):
			seconds -= 60
			minutes += 1
		if not isMinutesValid(minutes):
			minutes -= 60
			hours += 1

def  isSecondValid(seconds):
	return (seconds < 60)

def  isMinutesValid(minutes):
	return (minutes < 60)

def isHoursValid(hours):
	return (hours < 24)

def minutesToHours(seconds):
	hours = 0
	while(not isSecondValid(seconds)):
		hours += 1
		seconds -= 60
	return hours


window = tkinter.Tk()
window.title("My clock")

window.mainloop()