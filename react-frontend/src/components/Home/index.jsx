import React from "react";
import { useNavigate } from "react-router-dom";
import "./index.css"; // Ensure you have the updated styles

const Home = () => {
  const navigate = useNavigate();

  return (
    <div className="home-container">
      {/* Header Section */}
      <header className="header">
        <img src="/icons/logo.png" alt="Logo" className="logo" />
        <h1 className="title">Ensemble File Analysis Tool</h1>
      </header>

      {/* Main Content Section */}
      <div className="main-content">
        {/* Left Section - Sidebar */}
        <aside className="sidebar">
          <img src="/icons/search.png" alt="Search Icon" className="search-img" />
          <button className="try-now-btn" onClick={() => navigate("/inputform")}>
            Try It Now!
          </button>
        </aside>

        {/* Right Section - About the Tool */}
        <section className="about-tool">
          <h2>About the Tool</h2>
          <div className="file-grid">
            <div className="file-box">PDF</div>
            <div className="file-box">DOCX</div>
            <div className="file-box">XLSX</div>
            <div className="file-box">MP3</div>
            <div className="file-box">MP4</div>
            <div className="file-box">JPG</div>
            <div className="file-box">EXE</div>
          </div>
        </section>
      </div>
    </div>
  );
};

export default Home;
