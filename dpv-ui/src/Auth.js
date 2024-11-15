import React, { useState } from 'react';
import { auth } from './firebaseConfig';
import { createUserWithEmailAndPassword, signInWithEmailAndPassword } from 'firebase/auth';
import { getFirestore, doc, setDoc, getDoc } from 'firebase/firestore';
import { useNavigate } from 'react-router-dom'; // Import useNavigate for navigation
import './Auth.css';

const db = getFirestore();

function Auth() {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    role: 'Employee', // Default role for SignUp
  });
  const [isSignUp, setIsSignUp] = useState(true); // Toggle between Sign Up and Sign In
  const [error, setError] = useState('');
  const [message, setMessage] = useState('');
  const navigate = useNavigate(); // Hook to navigate

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setMessage('');
    try {
      if (isSignUp) {
        // Sign up logic
        const userCredential = await createUserWithEmailAndPassword(
          auth,
          formData.email,
          formData.password
        );

        // Store user role in Firestore
        const user = userCredential.user;
        await setDoc(doc(db, 'users', user.uid), {
          email: formData.email,
          role: formData.role,
        });

        setMessage('Account created successfully with role: ' + formData.role);
      } else {
        // Sign in logic
        const userCredential = await signInWithEmailAndPassword(
          auth,
          formData.email,
          formData.password
        );
        const user = userCredential.user;

        // Fetch user role from Firestore
        const userDoc = await getDoc(doc(db, 'users', user.uid));
        if (userDoc.exists()) {
          const userRole = userDoc.data().role;
          // Navigate based on role
          if (userRole === 'Manager') {
            navigate('/manager-dashboard');
          } else if (userRole === 'Employee') {
            navigate('/employee-dashboard');
          }
        }

        setMessage('Signed in successfully!');
      }
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <div className="auth-container">
      <div className="auth-form">
        <h2>{isSignUp ? 'Sign Up' : 'Sign In'}</h2>
        <form onSubmit={handleSubmit}>
          <div className="input-group">
            <label>Email:</label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              className="input-field"
              required
            />
          </div>
          <div className="input-group">
            <label>Password:</label>
            <input
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              className="input-field"
              required
            />
          </div>

          {isSignUp && (
            <div className="input-group">
              <label>Role:</label>
              <select
                name="role"
                value={formData.role}
                onChange={handleChange}
                className="input-field"
              >
                <option value="Admin">Admin</option>
                <option value="Manager">Manager</option>
                <option value="Employee">Employee</option>
              </select>
            </div>
          )}

          {error && <p className="error-message">{error}</p>}
          {message && <p className="success-message">{message}</p>}

          <button type="submit" className="submit-button">
            {isSignUp ? 'Sign Up' : 'Sign In'}
          </button>
        </form>

        <p>
          {isSignUp ? (
            <>
              Already have an account?{' '}
              <span className="toggle-link" onClick={() => setIsSignUp(false)}>
                Sign In
              </span>
            </>
          ) : (
            <>
              Don't have an account?{' '}
              <span className="toggle-link" onClick={() => setIsSignUp(true)}>
                Sign Up
              </span>
            </>
          )}
        </p>
      </div>
    </div>
  );
}

export default Auth;
