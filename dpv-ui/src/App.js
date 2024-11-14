import React from 'react';
import './App.css';
import Signup from './Signup'; // Import the Signup component

function App() {
  return (
    <div className="App">
      <h1>Welcome to My Website</h1>
      <Signup />  {/* Render the Signup component */}
    </div>
  );
}

export default App;
