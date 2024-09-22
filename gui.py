import streamlit as st
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier    


def app():
    st.title("Heart Disease Prediction")
    model = pickle.load(open("heart_disease_model.pkl","rb"))
        
    col1,col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        cp = st.number_input("Chest Pain Type", min_value=0, max_value=600, step=1)
        chol = st.number_input("Serum Cholesterol (mg/dL)", min_value=0, max_value=600, step=1)
        restecg = st.number_input("Resting Electrocardiographic Results", min_value=0, max_value=600, step=1)
        exang = st.number_input("Exercise Induced Angina", min_value=0, max_value=600, step=1)
        slope = st.number_input("Slope of the Peak Exercise ST Segment", min_value=0, max_value=600, step=1)
        thal = st.number_input("Thalassemia", min_value=0, max_value=600, step=1)

    
    with col2:
        sex = st.selectbox("Sex", options=["Male", "Female"])
        trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=250, step=1)
        fbs = st.number_input("Fasting Blood Sugar > 120 mg/dL", min_value=0, max_value=600, step=1)
        thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0, max_value=250, step=1)
        oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, step=0.1)
        ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy", min_value=0, max_value=600, step=1)
    
    if st.button("Predict"):
        # Do something with the input values
        # st.write("Age:", age)
        # st.write("Sex:", sex)
        # st.write("Chest Pain Type:", cp)
        # st.write("Resting Blood Pressure:", trestbps)
        # st.write("Serum Cholesterol:", chol)
        # st.write("Fasting Blood Sugar > 120 mg/dL:", fbs)
        # st.write("Resting Electrocardiographic Results:", restecg)
        # st.write("Maximum Heart Rate Achieved:", thalach)
        # st.write("Exercise Induced Angina:", exang)
        # st.write("ST Depression Induced by Exercise:", oldpeak)
        # st.write("Slope of the Peak Exercise ST Segment:", slope)
        # st.write("Number of Major Vessels Colored by Fluoroscopy:", ca)
        # st.write("Thalassemia:", thal)

        input_data = (age, 1  if sex == "Male" else 0,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        # input_data = (58,1,1,125,220,0,1,144,0,0.4,1,4,3)
        st.write(input_data)
        # change the input data to a numpy array
        input_data_as_numpy_array= np.asarray(input_data)

        # reshape the numpy array as we are predicting for only on instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        prediction = model.predict(input_data_reshaped)
        if (prediction[0]== 0):
            st.success("The Person does not have a Heart Disease")
            print('The Person does not have a Heart Disease')
        else:
            st.error("The Person has Heart Disease")
            print('The Person has Heart Disease')
if __name__ == "__main__":
    app()
