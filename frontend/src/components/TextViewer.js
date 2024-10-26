// src/components/TextViewer.js
import React, {useState} from "react";
import {
  Box,
  Button,
  TextField,
  Typography,
  CircularProgress,
  Card,
  CardContent,
} from "@mui/material";
import axios from "axios";

function TextViewer({language, educationLevel, expertise}) {
  const [inputText, setInputText] = useState("");
  const [simplifiedText, setSimplifiedText] = useState("");
  const [summaryText, setSummaryText] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    console.log({inputText});
    setLoading(true);
    try {
      const response = await axios.post(`http://127.0.0.1:5000/analyze_text`, {
        sample_text: inputText,
        education_level: educationLevel,
        expertise: expertise,
      });
      console.log({response});
      setSimplifiedText(response.data.text);
      setSummaryText(response.data.summary);
    } catch (error) {
      console.error("Error analyzing text:", error);
      setSimplifiedText("An error occurred while analyzing the text.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box>
      {/* Input Section */}
      <TextField
        label="Enter Text to Analyze"
        multiline
        rows={4}
        fullWidth
        variant="outlined"
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        sx={{marginBottom: 2}}
      />
      <Button
        variant="contained"
        color="primary"
        onClick={handleAnalyze}
        disabled={loading}
        sx={{marginBottom: 4}}
      >
        {loading ? <CircularProgress size={24} /> : "Analyze"}
      </Button>

      {/* Results Section */}
      {(summaryText || simplifiedText) && (
        <Box sx={{display: 'flex', flexDirection: 'column', gap: 4}}>
          {/* Summary Section */}
          {summaryText && (
            <Card sx={{backgroundColor: "#f3f4f6"}}>
              <CardContent>
                <Typography variant="h5" color="primary" gutterBottom>
                  Summary
                </Typography>
                {summaryText.split('\n').filter(point => point.trim() !== '' && point.trim() !== '-').map((point, index) => (
                  <Typography key={index} variant="body1" paragraph sx={{marginBottom: 1}}>
                    {point.trim().startsWith('-') ? point.trim() : `- ${point.trim()}`}
                  </Typography>
                ))}
              </CardContent>
            </Card>
          )}

          {/* Simplified Text Section */}
          {simplifiedText && (
            <Card sx={{backgroundColor: "#f3f4f6"}}>
              <CardContent>
                <Typography variant="h5" color="primary" gutterBottom>
                  Simplified Text
                </Typography>
                <Typography variant="body1">{simplifiedText}</Typography>
              </CardContent>
            </Card>
          )}
        </Box>
      )}
    </Box>
  );
}

export default TextViewer;
