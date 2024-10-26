// src/App.js
import React, {useState} from "react";
import {ThemeProvider, createTheme} from "@mui/material/styles";
import {Box, Container, Grid, Typography} from "@mui/material";
import Header from "./components/Header";
import Sidebar from "./components/Sidebar";
import TextViewer from "./components/TextViewer";

const theme = createTheme();

function App() {
  const [language, setLanguage] = useState("");
  const [educationLevel, setEducationLevel] = useState("");
  const [expertise, setExpertise] = useState("");

  return (
    <ThemeProvider theme={theme}>
      <Box sx={{flexGrow: 1}}>
        <Header />
        <Box sx={{ py: 4, backgroundColor: "grey.100", textAlign: "center" }}>
          <Container maxWidth="md">
            <Typography variant="h4" component="h1" gutterBottom>
              Welcome to Simplifier
            </Typography>
            <Typography variant="body1" color="textSecondary">
              Your personalized tool to explore content based on language, education level, and area of expertise. Select your preferences and see tailored content that suits your needs.
            </Typography>
          </Container>
        </Box>
        <Container maxWidth="lg" sx={{pt: 4}}>
          <Grid container spacing={3}>
            <Grid item xs={12} md={3}>
              <Sidebar
                language={language}
                setLanguage={setLanguage}
                educationLevel={educationLevel}
                setEducationLevel={setEducationLevel}
                expertise={expertise}
                setExpertise={setExpertise}
              />
            </Grid>
            <Grid item xs={12} md={9}>
              <TextViewer
                language={language}
                educationLevel={educationLevel}
                expertise={expertise}
              />
            </Grid>
          </Grid>
        </Container>
      </Box>
    </ThemeProvider>
  );
}

export default App;
