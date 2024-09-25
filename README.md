# FATIGUE CALCULATOR

- things to consider when calculating fatigue:
1. actual day
2. training kms -- kms -- float
3. training avg HR -- trAvgHr -- int
4. training highest HR -- trHiHr -- int
5. user's actual energy level after training (0-10) -- enrgyLev -- int
6. hours of sleep -- hSlp -- float
7. HRV -- hrv -- int

8. generate a float number to determine that day fatigue -- dayIndex

- -------------------- done until here -----------------------

9. Considering the last 30 days of training, give a fatigue index
10. substract from that index the fully rested fatigue