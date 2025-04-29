import streamlit as st
import joblib

model=joblib.load('placement.pkl')


def main():
    
    st.title("Welcome to My placement App")
    cgpa=st.slider('choose your packge from slider',min_value=0.0,max_value=10.0,step=0.1)
    st.write("cgpa is",cgpa)
       

    if st.button('Predict'):
        result=model.predict([[cgpa]])
        st.success(f'your package would be: {result} lpa')

if __name__ == "__main__":
    main()
    
