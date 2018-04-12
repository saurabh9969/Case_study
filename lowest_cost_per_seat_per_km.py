# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 15:12:18 2018

@author: saurabh
"""

import numpy as np
import pandas as pd

import os

os.getcwd()

data=pd.read_csv("C:\\Users\\saurabh\\Downloads\\aircraftcost1.csv")

#we have to calculate lowest cost per km

#for flight type A320

A320cost_per_seat_per_km=data.no_of_seat.values[0]*data.avg_speed.values[0]/data.cost_per_flight_hours.values[0]

#for flight type A330

A330cost_per_seat_per_km=data.no_of_seat.values[1]*data.avg_speed.values[1]/data.cost_per_flight_hours.values[1]

#for flight type B737

B737cost_per_seat_per_km=data.no_of_seat.values[2]*data.avg_speed.values[2]/data.cost_per_flight_hours.values[2]

#for flight type B747

B747cost_per_seat_per_km=data.no_of_seat.values[3]*data.avg_speed.values[3]/data.cost_per_flight_hours.values[3]

#for flight type Q400

Q400cost_per_seat_per_km=data.no_of_seat.values[4]*data.avg_speed.values[4]/data.cost_per_flight_hours.values[4]


#for flight type ATR72

ATR72cost_per_seat_per_km=data.no_of_seat.values[5]*data.avg_speed.values[5]/data.cost_per_flight_hours.values[5]


print("A320 flight type have cost per seat per km is: ",A320cost_per_seat_per_km)
print("A330 flight type have cost per seat per km is: ",A330cost_per_seat_per_km)
print("B737 flight type have cost per seat per km is: ",B737cost_per_seat_per_km)
print("B747 flight type have cost per seat per km is: ",B747cost_per_seat_per_km)
print("Q400 flight type have cost per seat per km is: ",Q400cost_per_seat_per_km)
print("ATR72 flight type have cost per seat per km is: ",ATR72cost_per_seat_per_km)

print("According to the observation Flight type ATR72 has lowest cost per seat per km : " ,ATR72cost_per_seat_per_km)








