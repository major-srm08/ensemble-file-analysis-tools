import React from "react";
import "./Footer.css";

const Footer = () => {
  return (
    <footer className="footer-container">
      <div className="detective-section">
        <img 
          src="/icons/detective.gif" 
          alt="Detective Investigating" 
          className="detective-img"
        />
      </div>
      <div className="footer-text">
        <p>© 2025 Filenomics | First Step Towards Digital Investigation</p>
      </div>
    </footer>
  );
};

export default Footer;
