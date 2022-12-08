import pickle

import numpy as np
import streamlit as st
model = pickle.load(open('model.pkl','rb'))
st.title("Traffic severity prediction")
st.header('Predict the severity ')
time = st.number_input('Enter the time', min_value=0, value=1, step=1)
st.text("")

st.text('Lighting conditions in which the accident occurred')
st.text( '1 - Full day')
st.text('2 - Twilight or dawn')
st.text('3 - Night without public lighting')
st.text( '4 - Night with public lighting not lit')
st.text('5 - Night with public lighting on')
lum = st.number_input( 'Enter the lighting conditions',min_value=0, value=1, step=1)
st.text("")

st.text('Type of Intersection')
st.text( '1 - Out of intersection')
st.text('2 - Intersection in X')
st.text('3 - Intersection in T')
st.text( '4 - Intersection in Y')
st.text('5 - Intersection with more than 4 branches')
st.text( '6 - Giratory')
st.text('7 - Place')
st.text('8 - Level crossing')
st.text( '9 - Other intersection')
int1 = st.number_input( 'Enter the type of intersection',min_value=0, value=1, step=1)
st.text("")

st.text('Atmospheric conditions')
st.text( '1 - Normal')
st.text('2 - Light rain')
st.text('3 - Heavy rain')
st.text( '4 - Snow - hail')
st.text('5 - Fog - smoke')
st.text( '6 - Strong wind - storm')
st.text('7 - Dazzling weather')
st.text('8 - Cloudy weather')
st.text( '9 - Other')
atm = st.number_input( 'Enter the Atmospheric condition:',min_value=0, value=1, step=1)
st.text("")

st.text('Type of Collision')
st.text( '1 - Two vehicles - frontal')
st.text('2 - Two vehicles - from the rear')
st.text('3 - Two vehicles - by the side')
st.text( '4 - Three vehicles and more - in chain')
st.text('5 - Three or more vehicles - multiple collisions')
st.text( '6 - Other collision')
st.text('7 - Without collision')
col = st.number_input('Enter the Type of Collision', min_value=0, value=1, step=1)
st.text("")

st.text('Category of Road')
st.text( '1 - Highway')
st.text('2 - National Road')
st.text('3 - Departmental Road')
st.text( '4 - Communal Way')
st.text('5 - Off public network')
st.text( '6 - Parking lot open to public traffic')
st.text('9 - other')
road_cat = st.number_input('Enter the Category of the Road', min_value=0, value=1, step=1)
st.text("")

st.text('Traffic Regime')
st.text('1 - One way')
st.text('2 - Bidirectional')
st.text('3 - Separated carriageways')
st.text( '4 - With variable assignment channels')
traf_reg = st.number_input('Enter the Traffic Regime', min_value=0, value=1, step=1)
st.text("")


st.text('Longitudinal profile describes the gradient of the road at the accident site')
st.text('1 - Dish')
st.text('2 - Slope')
st.text('3 - Hilltop')
st.text( '4- Hill bottom')
long_pro=st.number_input('Enter the Longitudinal profile of the road', min_value=0, value=1, step=1)
st.text("")

st.text('Road Shape')
st.text('1 - Straight part')
st.text('2 - Curved on the left')
st.text('3 - Curved right')
st.text( '4 - In "S"')
shape=st.number_input('Enter the shape of the Road', min_value=0, value=1, step=1)
st.text("")

st.text('Surface Conditions')
st.text( '1 - normal')
st.text('2 - wet')
st.text('3 - puddles')
st.text( '4 - flooded')
st.text('5 - snow')
st.text( '6 - mud')
st.text('7 - icy')
st.text('8 - fat - oil')
st.text( '9 - Other')
surf = st.number_input('Enter the surface conditions:', min_value=0, value=1, step=1)
st.text("")

dead_pred=st.number_input('Whether there are any Senior citizen involved in the accident or not.(0-NO/1-YES)', min_value=0, value=1, step=1)
st.text("")


st.text("")
x = np.zeros(11)
x[0]=time
x[1]=lum
x[2]=int1
x[3]=atm
x[4]=col
x[5]=road_cat
x[6]=traf_reg
x[7]=long_pro
x[8]=shape
x[9]=surf
x[10]=dead_pred

yhat = model.predict([x])[0]
if (yhat == 1):
    acc_pred = 'The Accident is Severe'
else:
    acc_pred = 'The Accident is not Severe'

st.success(acc_pred)



