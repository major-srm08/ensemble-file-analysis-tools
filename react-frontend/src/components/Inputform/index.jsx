import React, { useState } from "react";
import { Toast, ToastContainer } from "react-bootstrap";
import "./index.css";
import { useNavigate } from "react-router-dom";
// Icons for file types
import pdfIcon from "/icons/Pdf.png";
import imageIcon from "/icons/jpg.png";
import docIcon from "/icons/docx.png";
import excelIcon from "/icons/xlsx.png";
import exeIcon from "/icons/exe.png";
import audioIcon from "/icons/mp3.png";
import videoIcon from "/icons/mp4.png";
import defaultIcon from "/icons/default.png"; // A default icon for unknown files

const InputForm = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [fileIcon, setFileIcon] = useState(defaultIcon);
  const [showToast, setShowToast] = useState(false);
  const [toastMessage, setToastMessage] = useState("");
  const [isDragOver, setIsDragOver] = useState(false);

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

  // Function to handle file validation
  const validateFile = (file) => {
    if (file) {
      const fileExtension = file.name.slice(file.name.lastIndexOf(".")).toLowerCase();

      if (supportedFormats[fileExtension]) {
        setSelectedFile(file);
        setFileIcon(supportedFormats[fileExtension]); // Set the correct icon
      } else {
        setToastMessage("Unsupported file format! Please select a valid file.");
        setShowToast(true);
        setSelectedFile(null);
        setFileIcon(defaultIcon);
      }
    }
  };

  // Handle file input change
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

  const navigate = useNavigate();

  return (
    <div className="file-upload-container">
      {/* Home Button */}
      <button className="home-btn" onClick={() => navigate("/")}>
        🏠 Home
      </button>
      {/* Custom Styled Select File Button */}
      <div className="file-selector">
        <label htmlFor="fileInput" className="custom-file-upload">
          Select file ▼
        </label>
        <input id="fileInput" type="file" onChange={handleFileChange} />
      </div>

      {/* Drag and Drop Box */}
      <div
        className={`upload-box ${isDragOver ? "drag-over" : ""}`}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
      >
        <img src={fileIcon} alt="File Type" className="upload-icon" />
      </div>

      <p className="drag-text">Drag and drop the file...</p>
      <p className="supported-formats">.pdf, .jpg/.png, .docx, .xlsx, .exe, .mp3, .mp4</p>

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
