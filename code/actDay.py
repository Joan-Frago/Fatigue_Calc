#!/usr/bin/python3

class ActualDay:
    def __init__(self, kms:float, trAvgHr:int, trHiHr:int, enrgyLev:int, hSlp:float, hrv:int):
        self.kms = kms
        self.trAvgHr = trAvgHr
        self.trHiHr = trHiHr
        self.enrgyLev = enrgyLev
        self.hSlp = hSlp
        self.hrv = hrv

    def genIndex(kms, trAvgHr, trHiHr, enrgyLev, hSlp, hrv) -> float:
        try:
            # have to reduce this
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
        
        except Exception as e:
            print(e)