# firebase_operations.py

from firebase_config import initialize_firebase, get_firestore_client, get_realtime_db_reference

# Initialize Firebase when this module is imported
initialize_firebase()

### Realtime Database Operations ###

# Write data to Realtime Database
def write_realtime_data(path, data):
    ref = get_realtime_db_reference(path)
    ref.set(data)

# Read data from Realtime Database
def read_realtime_data(path):
    ref = get_realtime_db_reference(path)
    return ref.get()

# Update data in Realtime Database
def update_realtime_data(path, data):
    ref = get_realtime_db_reference(path)
    ref.update(data)

# Delete data in Realtime Database
def delete_realtime_data(path):
    ref = get_realtime_db_reference(path)
    ref.delete()

### Firestore Operations ###

# Write data to Firestore
def write_firestore_data(collection, document, data):
    db = get_firestore_client()
    doc_ref = db.collection(collection).document(document)
    doc_ref.set(data)

# Read data from Firestore
def read_firestore_data(collection, document):
    db = get_firestore_client()
    doc_ref = db.collection(collection).document(document)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    return None

# Update data in Firestore
def update_firestore_data(collection, document, data):
    db = get_firestore_client()
    doc_ref = db.collection(collection).document(document)
    doc_ref.update(data)

# Delete data in Firestore
def delete_firestore_data(collection, document):
    db = get_firestore_client()
    doc_ref = db.collection(collection).document(document)
    doc_ref.delete()
