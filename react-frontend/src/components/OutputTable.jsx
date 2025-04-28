import React from "react";
import "./OutputTable.css";

const OutputTable = ({ analysisResult }) => {
  if (!analysisResult) {
    return <p className="no-data">No analysis data available.</p>;
  }

  const renderDetails = (details) => {
    if (Array.isArray(details)) {
      return (
        <ul className="list-group">
          {details.map((item, index) => (
            <li key={index} className="list-group-item">{item}</li>
          ))}
        </ul>
      );
    } else if (typeof details === "object") {
      return (
        <pre className="json-data">{JSON.stringify(details, null, 2)}</pre>
      );
    }
    return details;
  };

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
          <tr>
            <td>File Type</td>
            <td>{analysisResult.file_type || "N/A"}</td>
          </tr>
          <tr>
            <td>Status</td>
            <td>{analysisResult.status || "N/A"}</td>
          </tr>

          {analysisResult.tool_insights &&
            Object.entries(analysisResult.tool_insights).map(([key, value]) => (
              <React.Fragment key={key}>
                <tr className="table-primary">
                  <td colSpan="2"><strong>{key.replace(/_/g, " ")}</strong></td>
                </tr>
                <tr>
                  <td>Status</td>
                  <td>{value.status || "N/A"}</td>
                </tr>
                {value.details && (
                  <tr>
                    <td>Details</td>
                    <td>{renderDetails(value.details)}</td>
                  </tr>
                )}
                {value.recommendation && (
                  <tr>
                    <td>Recommendation</td>
                    <td>{value.recommendation || "N/A"}</td>
                  </tr>
                )}
              </React.Fragment>
            ))}

          {analysisResult.verdict && (
            <tr>
              <td>Verdict</td>
              <td><strong className={analysisResult.verdict === "SUSPICIOUS" ? "text-danger" : "text-success"}>{analysisResult.verdict}</strong></td>
            </tr>
          )}
          {analysisResult.reason && (
            <tr>
              <td>Reason</td>
              <td>{analysisResult.reason}</td>
            </tr>
          )}
          {analysisResult.suggested_action && (
            <tr>
              <td>Suggested Action</td>
              <td>{analysisResult.suggested_action}</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
};

export default OutputTable;
