import streamlit as st 
import pandas as pd
st.title("Text input")
# it will give input option and then it will display
name=st.text_input("Enter your name")
if name:
    st.write(f"hello {name}")
    
age=st.slider("select your age",0,100,20)  # it will give slider
st.write(f"Your age is{age}.")

# options
options=["python","java","c++","js"]
choice=st.selectbox("choice your fav lang",options)
st.write(f"you selected {choice}")

db = pd.DataFrame({
    'num':[1,2,3,4],
    'name':["Rugved","atharva","tanmay","shivam"],
    'roll column':[10,20,30,40]
})
data=pd.DataFrame(db)
st.write(db)

uploaded_file=st.file_uploader("Choose a CSV file",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)