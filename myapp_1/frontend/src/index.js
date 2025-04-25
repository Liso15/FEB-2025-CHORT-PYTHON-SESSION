import React, { useState, useEffect } from 'react';
import axios from 'axios';

const myapp = () => {
  const [myapp, setWeather] = useState(null);
  const [city, setCity] = useState('London');

  const fetchWeather = async () => {
    const response = await axios.get(`http://localhost:8000/api/weather/?city=${city}`);
    setWeather(response.data);
  };

  return (
    <div>
      <input 
        type="text" 
        value={city} 
        onChange={(e) => setCity(e.target.value)} 
      />
      <button onClick={fetchWeather}>Get Weather</button>
      {weather && (
        <div>
          <h2>{weather.name}</h2>
          <p>Temperature: {weather.main.temp}°C</p>
        </div>
      )}
    </div>
  );
};

export default myapp;
// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
