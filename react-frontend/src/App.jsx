import { Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import InputForm from "./components/Inputform";
import OutputPage from "./components/OutputPage";  // Ensure correct import

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/inputform" element={<InputForm />} />
      <Route path="/output" element={<OutputPage />} />
    </Routes>
  );
};

export default App;
