import React from 'react';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
// auth
import Auth from './components/auth/Auth'
// user
import UserProfile from './components/UserProfile';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
          <Routes>
            <Route path='/' element={<Auth />}></Route>
            <Route path='/home' element={<UserProfile />}></Route>
          </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;