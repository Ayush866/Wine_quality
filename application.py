import streamlit as st
import pickle

scaler = pickle.load(open("standard_scaler.pkl","rb"))
model = pickle.load(open("model1.pkl",'rb'))

st.title("Wine quality predection")


fixed_acidity = st.text_input("Enter the value of fixed acidity")
volatile_acidity = st.text_input("Enter the value of fvolatile acidity")
citric_acid = st.text_input("Enter the value of citric acid")
residual_sugar = st.text_input("Enter the value of residual sugar")
chlorides=st.text_input("Enter the value of chlorides")
free_sulfur_dioxide = st.text_input("Enter the value of free sulfur dioxide")
total_sulfur_dioxide=st.text_input("Enter the value of total sulfur dioxide")
density = st.text_input("Enter the value of density")
pH = st.text_input("Enter the value of pH")
sulphates=st.text_input("Enter the value of sulphates")
alcohol=st.text_input("Enter the value of alcohol")


if st.button('predict'):
    result = model.predict(scaler.transform([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                                              chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,
                                              pH, sulphates, alcohol]]))


    if result[0] == 1:
        st.header("Good Quality")
    else:
        st.header("Bad Quality")