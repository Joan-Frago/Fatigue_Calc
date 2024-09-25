#!/usr/bin/python3

import sys

class ActualDay:
	def __init__(self, kms:float, trAvgHr:int, trHiHr:int, enrgyLev:int, hSlp:float, hrv:int):
		self.kms = kms
		self.trAvgHr = trAvgHr
		self.trHiHr = trHiHr
		self.enrgyLev = enrgyLev
		self.hSlp = hSlp
		self.hrv = hrv

	def generateIndex(kms, trAvgHr, trHiHr, enrgyLev, hSlp, hrv) -> float:
		# calculate kms index
		if kms <= 5:
			index = 2
		elif kms > 5 <= 10:
			index = 4
		elif kms > 10 <= 15:
			index = 6
		elif kms > 15 <= 20:
			index = 8
		elif kms > 20 <= 25:
			index = 9
		elif kms > 25:
			index = 10

		# calculate trAvgHr index
		if trAvgHr >= trZones["Zone 1"][0] <= trZones["Zone 1"][1]:
			index = index + 2
		elif trAvgHr >= trZones["Zone 2"][0] <= trZones["Zone 2"][1]:
			index = index + 4
		elif trAvgHr >= trZones["Zone 3"][0] <= trZones["Zone 3"][1]:
			index = index + 6
		elif trAvgHr >= trZones["Zone 4"][0] <= trZones["Zone 4"][1]:
			index = index + 8
		elif trAvgHr >= trZones["Zone 5"][0] <= trZones["Zone 5"][1]:
			index = index + 10

		# calculate trHiHr
		if trHiHr <= trZones["Zone 2"][1]:
			index = index + 1
		elif trHiHr <= trZones["Zone 4"][1] > trZones["Zone 2"][1]:
			index = index + 3
		elif trHiHr <= trZones["Zone 5"][1] > trZones["Zone 4"][1]:
			index = index + 5

		# calculate energyLev
		if enrgyLev > 0 <= 2:
			index = index + 10
		elif enrgyLev > 2 <= 4:
			index = index + 8
		elif enrgyLev > 4 <= 6:
			index = index + 6
		elif enrgyLev > 6 <= 8:
			index = index + 4
		elif enrgyLev > 8 <= 9:
			index = index + 2
		elif enrgyLev == 10:
			index = index

		# calculate hSlp
		if hSlp <= 5:
			index = index + 8
		elif hSlp > 5 <= 6:
			index = index + 5
		elif hSlp > 6 <= 8:
			index = index + 3
		elif hSlp > 8 <= 10:
			index = index + 1
		elif hSlp > 10:
			index = index + 3

		# calculate hrv
		if hrv <= 100:
			index = index + 8
		elif hrv > 100 <= 118:
			index = index + 0
		elif hrv > 118:
			index = index + 8

		return index

def getIndexes(actDayIndex:float) -> list:
    # for the moment, I'm simulating the last 30 days list,
    # but the idea is to get it from a db or file or excel

    lst30dIndex = [ 30,22.1,42,33,32,51,11,32.7,32.1,48,
                    10,24.33,33,12.2,60,31,40,24,52,11,
                    42,42,27.3,39,9.1212,50,35,25,44]

    lst30dIndex.append(actDayIndex)
    return lst30dIndex

def subsRest(index:float) -> float:
    return index

def generateIndex(allindex:list) -> float:
    # depending on the last 30 days indexes, return the median
    # to be able to calculate this, I need this function to get a list with the last 30 days indexes
    index = 0
    lenIndex = len(allindex)
    for i in allindex:
        index += i

    # here I have to substract the resting
    index = subsRest(index)
    index = round(index)
    return index

if __name__ == '__main__':
    try:
	   trZones = {	"Zone 1":[0,132],
				    "Zone 2":[133,153],
				    "Zone 3":[154,169],
				    "Zone 4":[170,179],
				    "Zone 5":[180,192]}
	
        try:
	        #actDayIndex = ActualDay.generateIndex(15, 143, 162, 7, 5.5, 112)
	        actDayIndex = ActualDay.generateIndex(int(input("how many kms did you do today?: ")),
                                                    int(input("what was your avg HR?: ")),
                                                    int(input("what was your max HR?: ")),
                                                    int(input("what are your actual energy levels (0 - 10)?: ")),
                                                    float(input("how many hours did you sleep?: ")),
                                                    int(input("what was your HRV today?: ")))
	        allIndex = getIndexes(actDayIndex)
	        print(generateIndex(allIndex))

        except Exception as e:
            print(e)
    except KeyboardInterrupt:
        sys.exit()