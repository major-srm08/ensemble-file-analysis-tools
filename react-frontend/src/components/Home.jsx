import React from "react";
import { useNavigate } from "react-router-dom";
import { Carousel } from "react-responsive-carousel";
import "react-responsive-carousel/lib/styles/carousel.min.css";
import "./Home.css";

const fileData = [
  {
    type: "PDF",
    description: "PDF files are validated using python-magic, scanned with yara-python, and metadata is extracted using PyExifTool.",
    icon: "public/icons/Pdf.png",
  },
  {
    type: "DOCX",
    description: "DOCX analysis includes macro inspection with oletools, password checking with msoffcrypto-tool, and malware scanning with yara-python.",
    icon: "public/icons/docx.png",
  },
  {
    type: "EXE",
    description: "EXE files are inspected using yara-python for malware detection, python-magic for format validation, and pyClamd for antivirus scanning.",
    icon: "public/icons/exe.png",
  },
  {
    type: "XLSX",
    description: "XLSX files are analyzed for hidden macros with oletools, encryption with msoffcrypto-tool, and threats using yara-python.",
    icon: "public/icons/xlsx.png",
  },
  {
    type: "MP3",
    description: "MP3 analysis checks format with python-magic, metadata via PyExifTool, streams using ffmpeg-python, and hidden data with stegpy.",
    icon: "public/icons/mp3.png",
  },
  {
    type: "MP4",
    description: "MP4 files are analyzed for metadata (pymediainfo), frames (imageio, OpenCV), and hidden payloads (stegpy).",
    icon: "public/icons/mp4.png",
  },
  {
    type: "JPG",
    description: "JPG images are inspected using PyExifTool for metadata, OpenCV and scikit-image for image integrity, and stegpy for steganography detection.",
    icon: "public/icons/jpg.png",
  },
];

const Home = () => {
  const navigate = useNavigate();

  return (
    <div className="home-container">

      {/* Main Content */}
      <div className="main-content">
        {/* Sidebar */}
        <aside className="sidebar">
          <img src="/icons/search.png" alt="Search Icon" className="search-img" />
          <button className="try-now-btn" onClick={() => navigate("/inputform")}>
            Try It Now!
          </button>
        </aside>

        {/* About Section */}
        <section className="about-tool">
          <h2>Supported File Analysis</h2>
          <div className="carousel-container">
            <Carousel
              showArrows
              autoPlay
              infiniteLoop
              showThumbs={false}
              interval={4000}
              showStatus={false}
              emulateTouch
              swipeable
              dynamicHeight={false}
              stopOnHover
            >
              {fileData.map((file, index) => (
                <div className="carousel-slide" key={index}>
                  <img src={file.icon} alt={`${file.type} Icon`} className="file-icon" />
                  <h3>{file.type}</h3>
                  <p>{file.description}</p>
                </div>
              ))}
            </Carousel>
          </div>
        </section>
      </div>
    </div>
  );
};

export default Home;
