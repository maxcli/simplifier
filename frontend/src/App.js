// src/App.js
import React, {useState} from "react";
import {ThemeProvider, createTheme} from "@mui/material/styles";
import {Box, Container, Grid} from "@mui/material";
import Header from "./components/Header";
import Sidebar from "./components/Sidebar";
import TextViewer from "./components/TextViewer";

const theme = createTheme();

function App() {
  const [language, setLanguage] = useState("english");
  const [educationLevel, setEducationLevel] = useState("");
  const [expertise, setExpertise] = useState("");

  return (
    <ThemeProvider theme={theme}>
      <Box sx={{flexGrow: 1}}>
        <Header />
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
