import React, { useEffect, useState } from 'react';
import './App.css';

const App = () => {
  const [currentBalance, setCurrentBalance] = useState(0);

  const getBalance = async () => {
    const res = await fetch('/balance', { method: 'GET' });
    console.log(res);
    const data = await res.json();
    setCurrentBalance(data.time);

    return function cleanup() {
      console.log('dead');
    };
  };

  useEffect(() => {
    getBalance();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <p>The current balance is {currentBalance}.</p>
      </header>
    </div>
  );
};

export default App;
