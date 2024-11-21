import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth, firestore
from backend import fetch_user_role_and_message  # Import the backend function

# Initialize Firebase only if it hasn't been initialized already
if not firebase_admin._apps:
    cred = credentials.Certificate('dpv-scheduler-firebase-adminsdk-1eo6j-197d820956.json')
    firebase_admin.initialize_app(cred)

# Streamlit app UI
st.set_page_config(page_title="Sign In / Sign Up", page_icon="🔒", layout="centered")

# Add a custom header and background styling
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            font-family: 'Arial', sans-serif;
            color: #3c3c3c;
        }
        .stTextInput>div>div>input {
            background-color: #fff;
            border-radius: 8px;
            padding: 12px;
            font-size: 16px;
            border: 1px solid #ccc;
        }
        .stButton>button {
            background-color: #3b8d99;
            color: white;
            font-size: 16px;
            padding: 12px 20px;
            border-radius: 8px;
            border: none;
            transition: background-color 0.3s;
        }
        .stButton>button:hover {
            background-color: #257d87;
        }
        .dropdown select {
            background-color: #fff;
            padding: 10px;
            font-size: 16px;
            border-radius: 8px;
            border: 1px solid #ccc;
        }
    </style>
""", unsafe_allow_html=True)

# Title of the page
st.markdown("<h1 style='text-align: center;'>Sign Up / Sign In</h1>", unsafe_allow_html=True)

# Choose between sign-up or sign-in
auth_option = st.radio("Select Option", ["Sign Up", "Sign In"], index=0)

# Create the form fields for user inputs
email = st.text_input("Email", placeholder="Enter your email")
password = st.text_input("Password", type="password", placeholder="Enter your password")
role = st.selectbox("Select Your Role", ["Employee", "Admin", "Manager"],
                    key="role") if auth_option == "Sign Up" else None


# Firebase authentication functions
def sign_up(email, password, role):
    try:
        # Create Firebase user
        user = auth.create_user(email=email, password=password)

        # Store the role in Firestore under the user document
        db = firestore.client()
        db.collection('users').document(user.uid).set({
            'email': email,
            'role': role
        })

        return user
    except Exception as e:
        st.error(f"Error creating user: {e}")
        return None


def sign_in(email, password):
    try:
        user = auth.get_user_by_email(email)
        # Implement password verification here (not shown)
        return user
    except Exception as e:
        st.error(f"Error signing in: {e}")
        return None


# Form actions
if auth_option == "Sign Up":
    if st.button("Sign Up"):
        if email and password and role:
            user = sign_up(email, password, role)
            if user:
                st.success(f"Account created successfully! Welcome, {role}.")
            else:
                st.error("Failed to create account.")
        else:
            st.warning("Please fill in all fields.")

elif auth_option == "Sign In":
    if st.button("Sign In"):
        if email and password:
            user = sign_in(email, password)
            if user:
                st.success(f"Welcome back, {email}!")
                message = fetch_user_role_and_message(email)  # Call backend function
                st.write(message)  # Display the message from the backend function
            else:
                st.error("Invalid credentials.")
        else:
            st.warning("Please fill in all fields.")