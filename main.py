from firebase_config import initialize_firebase, get_firestore_client

# Initialize Firebase app
initialize_firebase()

# Function to list all users in the 'users' collection
def list_all_users():
    db = get_firestore_client()
    users_ref = db.collection('users')
    docs = users_ref.stream()

    print("All Users in Firestore:")
    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")

# Call the function to list all users
list_all_users()
