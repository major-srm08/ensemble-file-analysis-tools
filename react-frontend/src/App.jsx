// src/App.jsx
import { Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import Home from "./components/Home";
import InputForm from "./components/Inputform";
import OutputPage from "./components/OutputPage";

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="inputform" element={<InputForm />} />
        <Route path="output" element={<OutputPage />} />
      </Route>
    </Routes>
  );
};

export default App;
