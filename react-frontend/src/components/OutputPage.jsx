import React from "react";
import { useLocation, useNavigate } from "react-router-dom";
import OutputTable from "./OutputTable";
import "./OutputPage.css";

const OutputPage = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const analysisResult = location.state?.analysisResult; // Get data from state

  return (
    <div className="output-page">
      <button className="btn btn-primary back-btn" onClick={() => navigate("/inputform")}>
        ⬅ Back to Upload
      </button>

      {analysisResult ? (
        <OutputTable analysisResult={analysisResult} />
      ) : (
        <p className="no-data">No analysis data found.</p>
      )}
    </div>
  );
};

export default OutputPage;
