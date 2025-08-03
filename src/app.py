import os
import streamlit as st
from utils.helpers import calculate_average

# Render.com sets PORT as an environment variable
port = int(os.environ.get("PORT", 8080))

# These options ensure Streamlit listens on the correct port/address for Render
st.set_option('server.port', port)
st.set_option('server.address', '0.0.0.0')

def main():
    st.title("My Streamlit App")
    
    # Sidebar for user input
    st.sidebar.header("User Input")
    user_input = st.sidebar.text_input("Enter something:")
    
    if st.sidebar.button("Submit"):
        processed_data = calculate_average(user_input)
        st.write("Processed Data:", processed_data)

    # Main content
    st.header("Welcome to My Streamlit App")
    st.write("This is a simple Streamlit application.")

if __name__ == "__main__":
    main()