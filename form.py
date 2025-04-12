import streamlit as st 


st.title("💼 Job Application Form")

#input field 
first_name=st.text_input("First name")

last_name=st.text_input("Last name")

email=st.text_input("Email address")

phone=st.text_input("Phone number")

address=st.text_area("Address")

education=st.selectbox("Education",["select","Under graduate", "Postgraduated"])

stream=st.selectbox("Stream",["select","CSE","IT","ECE","MECH","EEE"])

passed_out=st.text_input("Year of passed out")

resume=st.file_uploader("Upload CV/Resume",type=["pdf","doc"])

st.checkbox("Agree to terms and conditions")

if st.button("Submit"):
    if not all([first_name,last_name,email,phone,address,education!="select",stream!="select",passed_out,resume]):
        st.error("❌ Please fill all the required fields")
    
    else:
        st.success("✅ Form submitted successfully")
        st.balloons()

