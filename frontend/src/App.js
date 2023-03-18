import './App.css';
import InputPage from './components/InputPage/InputPage';
import { Routes, Route } from 'react-router-dom';

import Hero from './components/Hero/Hero';

function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Hero />} />
        <Route path="/input" element={<InputPage />} />
      </Routes>
    </>
    
  );
}

export default App;
