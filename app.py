import streamlit as st
import datetime as dt
import pickle
import numpy as np  
import pandas as pd



def show_page():

    

    st.title("DSS Software")
    dislay_text = "time of Check-up"
    now = dt.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    date = st.write(f"{now} is your {dislay_text}")

    title = st.text_input('Patients name', ' ')
    number = st.number_input("Patients age")
    height = st.number_input("Patients height")
    weight = st.number_input("Patients weight")
    bp = st.number_input("Patients blood pressure")

    

    
    #Load the pretrained model
    with open('rfdssmodel.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    # Replace 'your_dataset.csv' with the actual file name/path
    your_dataset = pd.read_csv('disease\Testing.csv')

    # Get the list of symptoms from the dataset
    symptoms = your_dataset.columns[:-1]
           
    
    selected_symptom = st.multiselect("Select the patient's symptoms", symptoms)
    st.write(f"These are your symtomps {selected_symptom}")
    
    # Get user input for symptoms
    user_input = [1 if symptom in selected_symptom else 0 for symptom in symptoms]

    # Reshape the input for model prediction
    user_input = pd.DataFrame([user_input])



    # Make prediction
    prediction = model.predict(user_input)[0]

    doc_note = st.text_area("Doctor's note")
    
    symptoms_str = ', '.join(selected_symptom)
    record = (
        f"{now} is the Patient's {dislay_text}\n"
        f"Patient's Name: {title}\n"
        f"Patient's Age: {number}\n"
        f"Patient's Height: {height}\n"
        f"Patient's Weight: {weight}\n"
        f"Patient's Blood Pressure: {bp}\n"
        f"Selected Symptoms: {symptoms_str}\n"
        f"The predicted prognosis is {prediction}\n"
        f"Doctor's note: {doc_note}"
    )



    st.download_button('Download Prognosis', record, file_name='prognosis_record.txt')

    # Display prediction result
    predict = st.button('Predict Prognosis')
    if predict:
        st.subheader(f"Patient most likely has: {prediction}")

    
show_page()