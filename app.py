import streamlit as st
import pandas as pd
st.title("Student Management System")

if "students" not in st.session_state:
    st.session_state.students = []

st.header("Add Student")

name = st.text_input("Student Name")
roll = st.text_input("Roll Number")
course = st.text_input("Course")

if st.button("Add Student"):
    if name and roll and course:
        st.session_state.students.append({
            "Name": name,
            "Roll": roll,
            "Course": course
        })
        st.success("Student added successfully!")
    else:
        st.warning("Please fill all fields")


st.header(" Delete Student")

roll_to_delete = st.text_input("Enter Roll Number to Delete")

if st.button("Delete Student"):
    found = False
    for student in st.session_state.students:
        if student["Roll"] == roll_to_delete:
            st.session_state.students.remove(student)
            st.success("Student deleted successfully!")

            
            found = True
            break
    if not found:
        st.error("Student not found")


st.header(" Student List")

if st.session_state.students:
    st.table(st.session_state.students)
else:
    st.info("No students added yet")
