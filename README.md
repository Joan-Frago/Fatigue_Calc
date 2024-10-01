# FATIGUE CALCULATOR

- things to consider when calculating fatigue:
1. From the actual day:
```python
# Training kms
kms:float

# training avg HR
trAvgHr:int

# training highest HR
trHiHr:int

# user's actual energy level after training (0-10)
enrgyLev:int

# hours of sleep
hSlp:float

# HRV
hrv:int

# generate a float number to determine that day fatigue
dayIndex:float

# substract from that index the fully rested fatigue
dayIndex:float
```

2. Considering the last 30 days of training, give a fatigue index
````python
index:int
```