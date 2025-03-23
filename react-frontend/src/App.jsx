import React from "react";
import { Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import InputForm from "./components/Inputform";

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/inputform" element={<InputForm />} />
    </Routes>
  );
};

export default App;
