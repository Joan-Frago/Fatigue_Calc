#!/usr/bin/python3

import sys
import insertDB
import actDay

def getIndexes(actDayIndex:float, afile:str) -> list:
    """
    This function receives the actual day index and the file where all the days indexes are stored
    It creates a list with all of those indexes and returns the last 30 indexes
    """
    try:
        lst = []
        lst30dIndex = []
        # for the moment, I'm simulating the last 30 days list,
        # but the idea is to get it from a db or file or excel


        # from db file
        with open(afile) as file:
            for i in file:
                lst.append(i)

        lst = [ 30,22.1,42,33,32,51,11,32.7,32.1,48,
                10,24.33,33,12.2,60,31,40,24,52,11,
                42,42,27.3,39,9.1212,50,35,25,44]

        lst.append(actDayIndex)
        # reverse lst
        lst = lst.reverse()
        # create list with 30 first elements, which are 30 last elements
        for i in lst:
            while i <= 30:
                lst30dIndex.append(i)

        return lst30dIndex
    except Exception as e:
        print(e)

def subsRest(index:float, userQuest:list) -> float:
    try:
        """
        This function should get the actual day index and substract
        from it depending on the rest from the last 30 days.
        """
        # this is going to get all the questions too

        print("------------- userQuest in subsRest -------------")
        print(userQuest)
        index = round(index)
        return index
    except Exception as e:
        print(e)

def generateIndex(allindex:list) -> float:
    try:
        """
        This function gets the last 30 indexes and sums them
        It returns the sum of the last 30 indexes
        """
        index = 0
        
        for i in allindex:
            index += i

        return index
    except Exception as e:
        print(e)

if __name__ == '__main__':
    try:
        try:
            # path to db file
            ifile = "./DB/db.txt"

            #actDayIndex = ActualDay.generateIndex(15, 143, 162, 7, 5.5, 112)
            userQuest = [int(input("how many kms did you do today?: ")),
                        int(input("what was your avg HR?: ")),
                        int(input("what was your max HR?: ")),
                        int(input("what are your actual energy levels (0 - 10)?: ")),
                        float(input("how many hours did you sleep?: ")),
                        int(input("what was your HRV today?: "))]
            trZones = { "Zone 1":[0,132],
                        "Zone 2":[133,153],
                        "Zone 3":[154,169],
                        "Zone 4":[170,179],
                        "Zone 5":[180,192]}
            actDayIndex = actDay.ActualDay.genIndex(userQuest[0],
                                                    userQuest[1],
                                                    userQuest[2],
                                                    userQuest[3],
                                                    userQuest[4],
                                                    userQuest[5])
            
            
            allIndex = getIndexes(actDayIndex, ifile)
            finalIndex = generateIndex(allIndex)
            finalIndex = subsRest(finalIndex, userQuest)
            print(finalIndex)

            #insertDB.insert(round(index))

        except Exception as e:
            print(e)
    except KeyboardInterrupt:
        sys.exit("\n")