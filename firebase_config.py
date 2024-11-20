# firebase_config.py

import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase app with credentials
def initialize_firebase():
    cred = credentials.Certificate("dpv-scheduler-firebase-adminsdk-1eo6j-197d820956.json")  # Use your actual credentials filename
    firebase_admin.initialize_app(cred)

# Firestore client
def get_firestore_client():
    return firestore.client()
