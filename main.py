import streamlit as st
import random
import time
from datetime import datetime


#######   MODEL ######

import random
import joblib

mod1 = joblib.load('model1.joblib')
mod2 = joblib.load('model2.joblib')

def custom_random(start, stop, step=0.01):
    return round(random.randint(0, int((stop - start) / step)) * step + start, 2)



def call():
    pressure = custom_random(27, 45)
    temp = custom_random(45, 90)
    vibe = custom_random(3.6, 7.3)
    flow = custom_random(10.8, 15)
    level = custom_random(18, 100)
    rpm =  custom_random(900, 1100)

    parameters = ["Pressure", "Temperature", "Vibration", "Flow", "Level", "RPM"]
    # printStr = "Pressure Temperature Vibration   Flow    Level    RPM   \n   "
    # printStr += str(pressure) + "    " + str(temp) + "       " + str(vibe) + "        " + str(flow) + "   " + str(level) + "    " + str(rpm) + "  \n   "
    current_time = datetime.now().strftime("%H:%M:%S")

    printStr = """

     Time : {}     \n    

    | Pressure | Temperature | Vibration | Flow | Level | RPM |
    |----------|-------------|-----------|------|-------|-----|
    | {}       | {}          | {}        | {}   | {}    | {}  |


         \n     



    """.format(current_time, pressure, temp, vibe, flow, level, rpm)


    predicted_value = mod1.predict([[pressure, temp, vibe, flow, level, rpm]])
    if predicted_value[0] == 0:
        predicted_value = mod2.predict([[pressure, temp, vibe, flow, level, rpm]])
        printStr += "Machine is likely to **FAIL** because of "
        predicted_list = predicted_value.tolist()[0]  # Convert to a list
        n = 0
        for i in predicted_list:
            n+=1
            if (i==0):
                # print(parameters[n-1], end=" ")
                printStr += parameters[n-1] + " "
        return printStr
    else:
        printStr += "Machine is likely to **WORK**."
        return printStr








# Streamlit UI
log_file = open('call_log.txt', 'a')

# Streamlit UI
st.title("Machine Failure Prediction")
st.write("*Instructions:*\n- *Press Start to start the program*   \n- *Press Stop at the top right corner to stop*")
st.write("Logs are saved in call_log.txt in the same directory")

# Create placeholders to display the random integers
random_int_placeholder = st.empty()

# Create a start button
start_button = st.button("Start")

if start_button:
    while True:
        output = call()
        random_int_placeholder.write(output)
        log_file.write(output)  # Write the output to the log file
        log_file.write('\n')  # Add a newline after each entry
        time.sleep(2)

# Close the log file when the program is stopped
log_file.close()
