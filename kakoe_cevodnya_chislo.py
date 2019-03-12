#!/usr/bin/python3

from datetime import date

def getWeekday(day):
	f = open("vocab/days.txt", "r")
	for i in range(7):
		line = f.readline()
		print(line)
		if i == day:
			return line

def main():
	today = str(date.today())
	#Weekdays start on 0 for Monday
	weekday = str(date.today().weekday())
	print("Сего́дня " + weekday + " " + today)
	print("Сего́дня " + getWeekday(date.today().weekday()))

if __name__ == "__main__":
	main()

