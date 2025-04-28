// src/components/Layout.jsx
import React from "react";
import Header from "./Header";
import Footer from "./Footer";
import { Outlet } from "react-router-dom";

const Layout = () => {
  return (
    <>
      <Header />
      <main>
        <Outlet /> {/* Render dynamic pages here */}
      </main>
      <Footer />
    </>
  );
};

export default Layout;
