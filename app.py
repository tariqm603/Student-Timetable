import streamlit as st
import pandas as pd

# Title and description
st.title("Student Day Timetable Planner")
st.write("Create and manage your daily schedule with ease.")

# Input for task details
st.header("Add a New Task")
task_name = st.text_input("Task Name")
start_time = st.time_input("Start Time")
end_time = st.time_input("End Time")

# Initialize session state to store tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Button to add task
if st.button("Add Task"):
    if task_name and start_time < end_time:
        st.session_state.tasks.append({"Task": task_name, "Start Time": start_time, "End Time": end_time})
        st.success(f"Task '{task_name}' added.")
    else:
        st.error("Please enter a valid task name and ensure the start time is before the end time.")

# Display current timetable
st.header("Your Timetable")
if st.session_state.tasks:
    timetable_df = pd.DataFrame(st.session_state.tasks)
    st.table(timetable_df)
else:
    st.info("No tasks added yet.")

# Clear timetable option
if st.button("Clear Timetable"):
    st.session_state.tasks = []
    st.success("Timetable cleared.")
