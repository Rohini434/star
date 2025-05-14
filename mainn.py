import streamlit as st
st.title("first app")
st.write("created streamlit library")
name=st.text_input("Enter your name: ")
if st.button("submit"):
  st.write(f"Hello, {name} Welcome to streamlit")
