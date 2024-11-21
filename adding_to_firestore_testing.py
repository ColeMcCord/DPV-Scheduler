import firebase_config
class MyClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

# Create an instance of the class
obj = MyClass(name="Test Object", value=42)

# Convert to dictionary
data = obj.__dict__


firebase_config.initialize_firebase()
db = firebase_config.get_firestore_client()


# Define the Firestore collection and document
collection_name = "testing"
document_name = "my_document"

# Add the serialized object to Firestore
db.collection(collection_name).document(document_name).set(data)

