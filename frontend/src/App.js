import './App.css';
import React from 'react';
import Login from './components/Login';
import Home from './components/Home';
import Schedule from './components/Schedule';
import ReactDOM from 'react-dom/client';
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <header>
        <h1>Venmo Scheduler</h1>
      </header>
      {/* <div>
        { props.children }
      </div> */}
      <Routes>
        <Route path="/" >
          <Route index element={<Home />} />
          <Route path="login" element={<Login />} />
          <Route path="schedule" element={<Schedule />} />
        </Route>
      </Routes>
    </div>
  );
}

export default App;
