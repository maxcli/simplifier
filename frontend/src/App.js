// src/App.js
import React from "react";
import {ThemeProvider, createTheme} from "@mui/material/styles";
import Typography from "@mui/material/Typography";
import Header from "./components/Header";
import Sidebar from "./components/Sidebar";
import TextViewer from "./components/TextViewer";

const theme = createTheme();

function App() {
  return (
    <ThemeProvider theme={theme}>
      <Header />
      <Typography variant="h1" component="h2">
        Hello, Simplifier!
      </Typography>
      <Sidebar />
      <TextViewer />
    </ThemeProvider>
  );
}

export default App;
