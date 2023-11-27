import streamlit as st


# l2 and u1 are the lower and upper bounds of the range of values

def enm(l2, u1):
    l1 = 0.9*l2
    u2 = 1.1*u1
    iter = 100000
    val = l1

    good = []
    bad  = []
    while True:
        if l1 <= val < l2:
            bad.append(val)
            val += (l2-l1)/(iter/2)

        elif l2 <= val <= u1:
            good.append(val)
            val += (u1-l2)/iter

        elif u1 < val < u2:
            bad.append(val)
            val += (u2-u1)/(iter/2)

        if val > u2:
            break


    while (len(good) != len(bad)):
        if len(good) > len(bad):
            good.pop()
        elif len(bad) > len(good):
            bad.pop()
    return good, bad

import pandas as pd

good_pressure, bad_pressure = enm(30, 40)
good_temp, bad_temp = enm(50, 80)
good_vibe, bad_vibe = enm(4, 6.5)
good_flow, bad_flow = enm(12, 14)
good_level, bad_level = enm(20, 90)
good_rpm, bad_rpm = enm(900, 1000)  


min_length = min(len(good_pressure), len(bad_pressure), len(good_temp), len(bad_temp), len(good_vibe), len(bad_vibe), len(good_flow), len(bad_flow), len(good_level), len(bad_level), len(good_rpm), len(bad_rpm))

# Truncate all lists to the minimum length
good_pressure = good_pressure[:min_length]
bad_pressure = bad_pressure[:min_length]
good_temp = good_temp[:min_length]
bad_temp = bad_temp[:min_length]
good_vibe = good_vibe[:min_length]
bad_vibe = bad_vibe[:min_length]
good_flow = good_flow[:min_length]
bad_flow = bad_flow[:min_length]
good_level = good_level[:min_length]
bad_level = bad_level[:min_length]
good_rpm = good_rpm[:min_length]
bad_rpm = bad_rpm[:min_length]



df = pd.DataFrame({'good_pressure': good_pressure, 'bad_pressure': bad_pressure, 'good_temp': good_temp, 'bad_temp': bad_temp, 'good_vibe': good_vibe, 'bad_vibe': bad_vibe, 'good_flow': good_flow, 'bad_flow': bad_flow, 'good_level': good_level, 'bad_level': bad_level, 'good_rpm': good_rpm, 'bad_rpm': bad_rpm})
df.to_csv('raw.csv', index=False)
