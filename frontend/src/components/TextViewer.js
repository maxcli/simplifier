// src/components/TextViewer.js
import React from "react";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";

function TextViewer() {
  return (
    <main className="flex-grow p-4">
      <Card className="mb-4 shadow-lg">
        <CardContent>
          <Typography variant="h5" component="div">
            Document Viewer
          </Typography>
          <Typography variant="body2" color="text.secondary">
            Upload a document to start.
          </Typography>
        </CardContent>
      </Card>
    </main>
  );
}

export default TextViewer;
