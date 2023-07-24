import React from "react";
import InstructionPage from "./pages/Instruction/Instruction.jsx";
import HomePage from "./pages/Home/Home.jsx";
import TestPage from "./pages/Test/Test.jsx"; 
import { BrowserRouter, Routes, Route } from "react-router-dom";

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/instruction" element={<InstructionPage />} />
        <Route
          path="/test/:testID/attempt/:attemptID/question/:questionNo"
          element={<TestPage />}
        />
      </Routes>
    </BrowserRouter>
  );
};

export default App;