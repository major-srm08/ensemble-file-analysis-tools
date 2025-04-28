// src/components/Header.jsx
import React from "react";
import "./Header.css";

const Header = () => {
  return (
    <header className="header-container">

      <div className="flying-papers">
        <div className="paper paper1">📄</div>
        <div className="paper paper2">📄</div>
        <div className="paper paper3">📄</div>
        <div className="paper paper4">📄</div>
        <div className="paper paper5">📄</div>
      </div>  
      <div className="header-content">
        <img src="/icons/logo.png" alt="Logo" className="logo" />
        <h1 className="site-title">FILENOMICS</h1>
      </div>
    </header>
  );
};

export default Header;
