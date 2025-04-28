import React from "react";
import "./OutputTable.css";

const OutputTable = ({ analysisResult }) => {
  if (!analysisResult) {
    return <p className="no-data">No analysis data available.</p>;
  }

  return (
    <div className="output-container">
      <h2 className="output-title">Analysis Report</h2>
      <table className="table table-striped table-bordered">
        <thead className="table-dark">
          <tr>
            <th>Attribute</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          {Object.entries(analysisResult).map(([key, value]) => (
            <tr key={key}>
              <td>{key.replace(/_/g, " ")}</td>
              <td>{typeof value === "object" ? JSON.stringify(value, null, 2) : value}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default OutputTable;
