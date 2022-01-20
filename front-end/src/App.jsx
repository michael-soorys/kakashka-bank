import React, { useEffect, useState } from 'react';
import './App.css';

const App = () => {
  const [currentTime, setCurrentTime] = useState(0);

  const fetchData = async () => {
    const res = await fetch('/time');
    console.log(res);
    const data = await res.json();
    setCurrentTime(data.time);

    return function cleanup() {
      console.log('dead');
    };
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <p>The current time is {currentTime}.</p>
      </header>
    </div>
  );
};

export default App;
