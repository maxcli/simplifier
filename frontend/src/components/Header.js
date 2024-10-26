// src/components/Header.js
import React from "react";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";

function Header() {
  return (
    <AppBar position="static">
      <Toolbar className="px-4">
        <Typography variant="h6" component="div" sx={{flexGrow: 1}}>
          Simplifier
        </Typography>
      </Toolbar>
    </AppBar>
  );
}

export default Header;
