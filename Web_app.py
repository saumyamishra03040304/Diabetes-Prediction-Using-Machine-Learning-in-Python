import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model=pickle.load(open(r"C:\Users\msaum\OneDrive\Desktop\Diabetes prediction app\trained_model.sav",'rb'))

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)



    prediction = loaded_model.predict(input_data_reshaped)
  

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'


def main():

    # giving title
    st.title("Diabetes Prediction Web App")

    # ,,DiabetesPedigreeFunction,Age
    # getting input data from user
    Pregnancies=st.text_input("No of Pregnancies:")
    Glucose=st.text_input("Glucose level:")
    BloodPressure=st.text_input("Blood Pressure value:")
    SkinThickness=st.text_input("Skin Thickness value:")
    Insulin=st.text_input("Insulin value:")
    BMI=st.text_input("Body Mass Index(BMI):")
    DiabetesPedigreeFunction=st.text_input("Diabetes Pedigree Function:")
    Age=st.text_input("Age:")

    # code for prediction
    diagnosis=''

    # creating a button
    if st.button("Diabetes Test Result"):   # if button clicked
        diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)  # it will give output

if __name__ == '__main__':
    main()