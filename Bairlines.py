# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 17:11:03 2018

@author: saurabh
"""

import numpy as np
import pandas as pd
import os

os.getcwd()

data=pd.read_csv("C:\\Users\\saurabh\\Downloads\\aircraftcost1.csv")

data2=pd.read_csv("C:\\Users\\saurabh\\Downloads\\AirlinesB.csv")

#for AA to BB network

print("passanger demand for AA to BB network will be: ",data2['pass.Demand'].values[0])

print("distance required to travelled : ",data2['destination'].values[0])


#so we required 420 passengers

B747seats=data.no_of_seat.values[3]
ATR72seats=data.no_of_seat.values[5]
A320seats=data.no_of_seat.values[0]
A330seats=data.no_of_seat.values[1]
B737seats=data.no_of_seat.values[2]
Q400seats=data.no_of_seat.values[4]

#so no of seats required for passanger in AA to BB network is 420


total_seats_for_AA_to_BB=B747seats+ATR72seats

seats_required=data2['pass.Demand'].values[0]

print("the aircraft type required for AA to BB network is , B747 and ATR72",total_seats_for_AA_to_BB)

# so no of seats required for passanger in BB to CC network is 450

total_seats_for_BB_to_CC=B747seats+B737seats

seat_required1=data2['pass.Demand'].values[1]

print("total no of seats required for passanger in BB to CC network is: ",seat_required1)

print("aircraft type required for BB to CC network is ,B747 and B737 and total available seats are : ",total_seats_for_BB_to_CC)

# so no of seats required for pasanger in CC to AA network is 300

total_seats_for_CC_to_AA=A320seats+B737seats

seat_required2=data2['pass.Demand'].values[2]

print("total no of seats required for passanger in CC to AA network is: ",seat_required2)

print("aircraft type required for CC to AA network is ,A320 and B737 and total available seats are : ",total_seats_for_CC_to_AA)

# so no of seats required for passenger in AA to DD network is 300

total_seats_for_AA_to_DD=A320seats+B737seats

seat_required3=data2['pass.Demand'].values[3]

print("total no of seats required for passanger in AA to DD network is: ",seat_required3)

print("aircraft type required for AA to DD network is ,A320 and B737 and total available seats are : ",total_seats_for_AA_to_DD)













