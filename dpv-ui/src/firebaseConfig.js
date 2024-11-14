// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";  // Import getAuth for authentication

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDQGoWyDgxMyXksGskDtUgMltU5ETRqAdw",
  authDomain: "dpv-scheduler.firebaseapp.com",
  databaseURL: "https://dpv-scheduler-default-rtdb.firebaseio.com",
  projectId: "dpv-scheduler",
  storageBucket: "dpv-scheduler.firebasestorage.app",
  messagingSenderId: "730189052301",
  appId: "1:730189052301:web:d36eeeba67af005ca5e5c4",
  measurementId: "G-NP2WD1HPT7"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
export const auth = getAuth(app);  // Initialize and export auth for use in signup