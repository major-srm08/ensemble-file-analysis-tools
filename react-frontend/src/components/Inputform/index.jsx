import React, { useState } from "react";
import { Toast, ToastContainer } from "react-bootstrap";
import "./index.css";
import { useNavigate } from "react-router-dom";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrash } from "@fortawesome/free-solid-svg-icons"; // Import FontAwesome trash icon

// Icons for file types
import pdfIcon from "/icons/Pdf.png";
import imageIcon from "/icons/jpg.png";
import docIcon from "/icons/docx.png";
import excelIcon from "/icons/xlsx.png";
import exeIcon from "/icons/exe.png";
import audioIcon from "/icons/mp3.png";
import videoIcon from "/icons/mp4.png";
import defaultIcon from "/icons/default.png"; // Default icon for unknown files

import OutputTable from "../OutputTable";

const InputForm = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [fileIcon, setFileIcon] = useState(defaultIcon);
  const [isValidFile, setIsValidFile] = useState(false);
  const [showToast, setShowToast] = useState(false);
  const [toastMessage, setToastMessage] = useState("");
  const [isDragOver, setIsDragOver] = useState(false);
  const [analysisResult, setAnalysisResult] = useState(null);
  const [loading, setLoading] = useState(false);  // New state for loading

  const supportedFormats = {
    ".pdf": pdfIcon,
    ".jpg": imageIcon,
    ".png": imageIcon,
    ".docx": docIcon,
    ".xlsx": excelIcon,
    ".exe": exeIcon,
    ".mp3": audioIcon,
    ".mp4": videoIcon,
  };

  // Function to handle file validation (for both input and drag-drop)
  const validateFile = (file) => {
    if (file) {
      const fileExtension = file.name.slice(file.name.lastIndexOf(".")).toLowerCase();

      if (supportedFormats[fileExtension]) {
        setSelectedFile(file);
        setFileIcon(supportedFormats[fileExtension]); // Set correct icon
        setIsValidFile(true); // Valid file
      } else {
        setToastMessage("Unsupported file format! Please select a valid file.");
        setShowToast(true);
        setSelectedFile(file); // Show file name even if invalid
        setFileIcon(defaultIcon);
        setIsValidFile(false); // Invalid file
      }
    }
  };

  // Handle file input change (when using select button)
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    validateFile(file);
  };

  // Handle drag & drop
  const handleDragOver = (event) => {
    event.preventDefault();
    setIsDragOver(true);
  };

  const handleDragLeave = () => {
    setIsDragOver(false);
  };

  const handleDrop = (event) => {
    event.preventDefault();
    setIsDragOver(false);

    const file = event.dataTransfer.files[0];
    validateFile(file);
  };

  // Handle file delete
  const deleteFile = () => {
    setSelectedFile(null);
    setFileIcon(defaultIcon);
    setIsValidFile(false);
  };

  const submitForm = async (event) => {
    event.preventDefault();

    if (!selectedFile) {
        setToastMessage("Please select a file before submitting.");
        setShowToast(true);
        return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);
    
    setLoading(true);  // Show loader when submission starts

    try {
        const uploadResponse = await fetch("http://127.0.0.1:8000/upload/", {
            method: "POST",
            body: formData,
        });

        const uploadResult = await uploadResponse.json();

        if (!uploadResponse.ok) {
            setToastMessage(`Upload failed: ${uploadResult.detail}`);
            setShowToast(true);
            setLoading(false);
            return;
        }

        console.log("✅ File uploaded successfully:", uploadResult);

        // Extract the uploaded file path
        const filePath = uploadResult.path;
        const fileExt = selectedFile.name.split('.').pop().toLowerCase();

        // Map extensions to API endpoints
        const analysisEndpoints = {
            "docx": "/analyze/docx",
            "xlsx": "/analyze/xlsx",
            "exe": "/analyze/exe",
            "jpg": "/analyze/image",
            "mp4": "/analyze/video",
            "mp3": "/analyze/mp3",
            "pdf": "/analyze/pdf",
        };

        const analysisEndpoint = analysisEndpoints[fileExt];

        if (!analysisEndpoint) {
            setToastMessage("Analysis not available for this file type.");
            setShowToast(true);
            setLoading(false);
            return;
        }

        console.log(`🔍 Triggering analysis for: ${fileExt} at ${analysisEndpoint}`);

        // Call the appropriate analysis API
        const analysisResponse = await fetch(`http://127.0.0.1:8000${analysisEndpoint}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ file_path: filePath }),
        });

        const analysisResult = await analysisResponse.json();

        if (!analysisResponse.ok) {
            setToastMessage(`Analysis failed: ${analysisResult.detail}`);
            setShowToast(true);
            setLoading(false);
            return;
        }

        console.log("✅ Analysis completed:", analysisResult);

        // Navigate to Output page with analysis result
        setTimeout(() => {
            setLoading(false);
            navigate("/output", { state: { analysisResult: analysisResult.analysis_result } });
        }, 1000);

    } catch (error) {
        setToastMessage("Error processing file.");
        setShowToast(true);
        setLoading(false);
    }
};


  const navigate = useNavigate();

  return (
    <div className="file-upload-container">

            {/* Show Loader if Analysis is Running */}
{loading && (
  <div className="loader-container">
    <div className="spinner"></div>
    <p>Analyzing file... Please wait</p>
  </div>
)}

      {/* Home Button */}
      <button className="home-btn" onClick={() => navigate("/")}>
        🏠 Home
      </button>

      {/* Form for file selection and submission */}
      <form onSubmit={submitForm} className="form-container">
        {/* Custom Styled Select File Button */}
        <div className="file-selector">
          <label htmlFor="fileInput" className="custom-file-upload">
            Select file ▼
          </label>
          <input id="fileInput" type="file" onChange={handleFileChange} />
        </div>

        {/* Analyse Button */}
        <button type="submit" className="custom-file-upload">
          Analyse
        </button>
      </form>

      {/* Drag and Drop Box */}
      <div
        className={`upload-box ${isDragOver ? "drag-over" : ""}`}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
      >
        <img src={fileIcon} alt="File Type" className="upload-icon" />
      </div>

      {/* File Name Display with Delete Option */}
      {selectedFile && (
        <div className="file-info">
          <p className={`file-name ${isValidFile ? "valid-file" : "invalid-file"}`}>
            {selectedFile.name} {isValidFile ? "✅" : "❌"}
          </p>
          <button className="delete-btn" onClick={deleteFile}>
            <FontAwesomeIcon icon={faTrash} />
          </button>
        </div>
      )}

      <p className="drag-text">Drop Your File Here Or Select Manually</p>
      <p className="supported-formats">.PDF, .JPG, .DOCX, .XLSX, .EXE, .MP3, .MP4</p>
      
      {/* Add OutputTable below the file input */}
      {analysisResult && <OutputTable analysisResult={analysisResult} />}
      
      {/* Toast Notification */}
      <ToastContainer position="top-end" className="p-3">
        <Toast
          onClose={() => setShowToast(false)}
          show={showToast}
          delay={3000}
          autohide
          className="custom-toast"
        >
          <Toast.Body>{toastMessage}</Toast.Body>
        </Toast>
      </ToastContainer>
    </div>
  );
};

export default InputForm;
