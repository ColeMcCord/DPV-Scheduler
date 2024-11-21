import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth, firestore
from backend import fetch_user_role_and_message  # Import the backend function

# Initialize Firebase only if it hasn't been initialized already
if not firebase_admin._apps:
    cred = credentials.Certificate('dpv-scheduler-firebase-adminsdk-1eo6j-197d820956.json')
    firebase_admin.initialize_app(cred)

# Streamlit app UI
st.set_page_config(page_title="Welcome to DPV Scheduler", page_icon="🔒", layout="centered")

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
            margin-bottom: 10px; /* Add spacing between buttons */
            width: 100%; /* Make buttons the same size */
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

# Title of the page (this title will always be visible when user is not signed in)
if "user" not in st.session_state:
    st.markdown("<h1 style='text-align: center;'>Welcome to DPV Scheduler</h1>", unsafe_allow_html=True)
else:
    st.markdown("<h1 style='text-align: center;'>Welcome to Your Dashboard</h1>", unsafe_allow_html=True)

# Check if the user is logged in
if "user" not in st.session_state:
    # Choose between sign-up or sign-in
    auth_option = st.radio("Select Option", ["Sign Up", "Sign In"], index=0)

    # Create the form fields for user inputs
    email = st.text_input("Email", placeholder="Enter your email")
    password = st.text_input("Password", type="password", placeholder="Enter your password")
    role = st.selectbox("Select Your Role", ["Employee", "Admin", "Manager"], key="role") if auth_option == "Sign Up" else None

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
                    st.session_state.user = user  # Store user in session state
                    st.success(f"Welcome back, {email}!")
                    st.rerun()  # Reload the page to go to the next screen
                else:
                    st.error("Invalid credentials.")
            else:
                st.warning("Please fill in all fields.")
else:
    # If the user is logged in, show the next page (dashboard)
    st.title("Welcome to Your Dashboard")

    # Fetch the user-specific task from Firestore
    user_id = st.session_state.user.uid  # Get the logged-in user's UID

    db = firestore.client()  # Initialize Firestore client
    user_doc = db.collection('users').document(user_id).get()  # Fetch user data
    if user_doc.exists:
        user_data = user_doc.to_dict()
        role = user_data.get('role')  # You can also fetch other data like role
        task = user_data.get('task', 'No task assigned')  # Replace 'task' with the field from Firestore if needed
    else:
        task = 'No task assigned'  # Default message if no task is assigned or user doesn't exist

    # Display the task assigned
    st.subheader(f"Your Current Task: {task}")
    
    # Create two columns: one for task details and one for the buttons
    col1, col2 = st.columns([2, 1])  # Adjust column width as needed

    with col1:
        # Display task details (if any)
        st.write(f"Task: {task}")  # You can add more details about the task here
    
    with col2:
        # Vertical buttons for the task actions with the same size
        st.button("Complete")
        st.button("Edit")
        st.button("Change")
        st.button("Remove")
        st.button("Get")
