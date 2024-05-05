import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

// auth
import Auth from './components/auth/Auth'
// user
import Home from './components/Home';
// ProtectedRoutes
import ProtectedRoutes from './components/ProtectedRoutes';

const App = () => (
  <Router>
    <Routes>
      <Route path="/" element={<Auth />} />
      <Route path="/home" element={<ProtectedRoutes><Home /></ProtectedRoutes>} />
    </Routes>
  </Router>
);

export default App;