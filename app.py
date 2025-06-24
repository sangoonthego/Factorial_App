import streamlit as st
from factorial import fact
import os

def load_users():
    try:
        if os.path.exists("users.txt"):
            with open("users.txt", "r", encoding="utf-8") as file:
                users =[line.strip() for line in file.readlines() if line.strip()]
                return users
        else:
            st.error("Error: File Not Exist!")
            return []
    except Exception as e:
        st.error(f"Error occur when reading file users.txt: {e}")
        return []
    
def login_page():
    st.title("Log in")
    username = st.text_input("Enter username: ")

    col1, col2 = st.columns([1, 1])
    with col1:
        signup_clicked = st.button("Sign up", use_container_width=True)
    with col2:
        login_clicked = st.button("Log in", use_container_width=True)

    if signup_clicked:
        if username:
            users = load_users()
            if username in users:
                st.warning("Username already exists!")
            else:
                try:
                    with open("users.txt", "a", encoding="utf-8") as file:
                        file.write(username + "\n")
                    st.success("Register successfully!!!")   
                except Exception as e:
                    st.error(f"Error when registering: {e}")
        else:
            st.warning("Please enter username!!!")

    if login_clicked:
        if username:
            users = load_users()
            if username in users:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                st.session_state.show_greeting = True
                st.session_state.username = username
                st.rerun()
        else:
            st.warning("Please enter username!!!")

def factorial_calculator():
    st.title("Factorial Calculator")
    st.write(f"Hello, {st.session_state.username}")

    if st.button("Log out"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    st.divider()

    number = st.number_input("Enter a number: ", min_value=0, step=1, format="%d")

    if st.button("Calculate"):
        try:
            result = fact(int(number))
            st.write(f"The factorial of {int(number)} is {result}")
        except Exception as e:
            st.error(f"Error: {e}")

def greeting_page():
    st.title("Welcome to my Application")
    st.write(f"Ohayou {st.session_state.username}")
    st.write("You have no permission to access factorial calculator function!")

    if st.button("Return Log in"):
        st.session_state.show_greeting = False
        st.session_state.username = ""
        st.rerun()

def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""
    if "show_greeting" not in st.session_state:
        st.session_state.show_greeting = False
    
    if st.session_state.logged_in:
        factorial_calculator()
    elif st.session_state.show_greeting:
        greeting_page()
    else:
        login_page()

if __name__ == "__main__":
    main()
    