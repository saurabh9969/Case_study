# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 22:34:50 2018

@author: saurabh
"""

import numpy as np
import pandas as pd
import os

os.getcwd()

os.chdir("C:\\Users\\saurabh\\Downloads")

data=pd.read_csv("C:\\Users\\saurabh\\Downloads\\AirlinesA.csv")

data.columns=['aircraftname','aircrafttype','jan14','feb14','mar14','apr14','may14','jun14','jul14','aug14','sep14','oct14','nov14','dec14']

data.aircrafttype.value_counts()

#A330 flight type 
A330=data[data.aircrafttype == "A330"]

TotalhoursflownA330=A330['jan14'].sum()+A330['feb14'].sum()+A330['mar14'].sum()+A330['apr14'].sum()+A330['may14'].sum()+A330['jun14'].sum()+A330['jul14'].sum()+A330['aug14'].sum()+A330['sep14'].sum()+A330['oct14'].sum()+A330['nov14'].sum()+A330['dec14'].sum()

aircraftcost=pd.read_csv("C:\\Users\\saurabh\\Downloads\\aircraftcost1.csv")

aircraftcostA330=aircraftcost.cost_per_flight_hours.values[1]

totalcostA330=TotalhoursflownA330*aircraftcostA330

#A320

A320=data[data.aircrafttype == "A320"]

TotalhoursflownA320=A320['jan14'].sum()+A320['feb14'].sum()+A320['mar14'].sum()+A320['apr14'].sum()+A320['may14'].sum()+A320['jun14'].sum()+A320['jul14'].sum()+A320['aug14'].sum()+A320['sep14'].sum()+A320['oct14'].sum()+A320['nov14'].sum()+A320['dec14'].sum()

aircraftcostA320=aircraftcost.cost_per_flight_hours.values[0]

totalcostA320=TotalhoursflownA320*aircraftcostA320

#B737

B737=data[data.aircrafttype == "B737"]

TotalhoursflownB737=B737['jan14'].sum()+B737['feb14'].sum()+B737['mar14'].sum()+B737['apr14'].sum()+B737['may14'].sum()+B737['jun14'].sum()+B737['jul14'].sum()+B737['aug14'].sum()+B737['sep14'].sum()+B737['oct14'].sum()+B737['nov14'].sum()+B737['dec14'].sum()

aircraftcostB737=aircraftcost.cost_per_flight_hours.values[2]

totalcostB737=TotalhoursflownB737*aircraftcostB737

#Q400

Q400=data[data.aircrafttype == "Q400"]

TotalhoursflownQ400=Q400['jan14'].sum()+Q400['feb14'].sum()+Q400['mar14'].sum()+Q400['apr14'].sum()+Q400['may14'].sum()+Q400['jun14'].sum()+Q400['jul14'].sum()+Q400['aug14'].sum()+Q400['sep14'].sum()+Q400['oct14'].sum()+Q400['nov14'].sum()+Q400['dec14'].sum()

aircraftcostQ400=aircraftcost.cost_per_flight_hours.values[4]

totalcostQ400=TotalhoursflownQ400*aircraftcostQ400

#ATR72

ATR72=data[data.aircrafttype == "ATR72"]

TotalhoursflownATR72=ATR72['jan14'].sum()+ATR72['feb14'].sum()+ATR72['mar14'].sum()+ATR72['apr14'].sum()+ATR72['may14'].sum()+ATR72['jun14'].sum()+ATR72['jul14'].sum()+ATR72['aug14'].sum()+ATR72['sep14'].sum()+ATR72['oct14'].sum()+ATR72['nov14'].sum()+ATR72['dec14'].sum()

aircraftcostATR72=aircraftcost.cost_per_flight_hours.values[5]

totalcostATR72=TotalhoursflownATR72*aircraftcostATR72


#B747

B747=data[data.aircrafttype == "B747"]

TotalhoursflownB747=B747['jan14'].sum()+B747['feb14'].sum()+B747['mar14'].sum()+B747['apr14'].sum()+B747['may14'].sum()+B747['jun14'].sum()+B747['jul14'].sum()+B747['aug14'].sum()+B747['sep14'].sum()+B747['oct14'].sum()+B747['nov14'].sum()+B747['dec14'].sum()

aircraftcostB747=aircraftcost.cost_per_flight_hours.values[3]

totalcostB747=TotalhoursflownB747*aircraftcostB747


#print the total cost of the flight type 

print("Total cost for flight Type (A320) :",totalcostA320)
print("Total cost for flight Type (A330) :" ,totalcostA330)
print("Total cost for flight Type (ATR72) :",totalcostATR72)
print("Total cost for flight Type (B737) :",totalcostB737)
print("Total cost for flight Type (B747) :",totalcostB747)
print("Total cost for flight Type (Q400) :",totalcostQ400)