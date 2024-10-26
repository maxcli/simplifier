// src/components/Header.js
import React from "react";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";

function Header() {
  return (
    <AppBar position="static" className="bg-blue-600">
      <Toolbar className="px-4 flex items-center">
        <img
          src="/newlogo.png"
          alt="Logo"
          height={50}
          style={{ backgroundColor: "#1e3a8a", padding: "4px", borderRadius: "8px" }} // Match AppBar color
        />
        <Typography variant="h6" component="div" sx={{ flexGrow: 1, pl: 1 }}>
          Simplifier
        </Typography>
      </Toolbar>
    </AppBar>
  );
}

export default Header;
