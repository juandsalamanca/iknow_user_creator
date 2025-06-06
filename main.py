import streamlit as st
import requests

st.header("User creator")

user = st.text_input("Type here your username")
pwd = st.text_input("Type here your password")
email = st.text_input("Type here your email")

if user and pwd and email:
  submit = st.button("Submit")
  if submit:
    payload = {"username":user, "password":pwd, "email":email}
    response = requests.post("https://api.iknow.aidevlab.com/api/v1/auth/signup", json=payload)
    if response.status_code == 200 or response.status_code == 201:
      st.success("New user created!")
