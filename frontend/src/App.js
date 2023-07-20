import React from "react";
import InstructionPage from "./pages/Instruction/Instruction.jsx";
import { BrowserRouter, Routes, Route } from "react-router-dom";

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<InstructionPage />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;