// src/components/Sidebar.js
import React from "react";
import {
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Typography,
} from "@mui/material";

function Sidebar({
  tone,
  setTone,
  educationLevel,
  setEducationLevel,
  expertise,
  setExpertise,
}) {
  const handleLanguageChange = (event) => {
    setTone(event.target.value);
  };

  const handleEducationLevelChange = (event) => {
    setEducationLevel(event.target.value);
  };

  const handleExpertiseChange = (event) => {
    setExpertise(event.target.value);
  };

  return (
    <aside className="w-64 p-4 bg-gray-100">
      <Typography variant="h6" gutterBottom>
        Options
      </Typography>

      <FormControl fullWidth sx={{mt: 2}}>
        <InputLabel id="tone-select-label">Language</InputLabel>
        <Select
          labelId="language-select-label"
          id="language"
          value={tone}
          label="Language"
          onChange={handleLanguageChange}
        >
          <MenuItem value="formal">English</MenuItem>
          <MenuItem value="formal">Spanish</MenuItem>
          <MenuItem value="neutral">Chinese</MenuItem>
          <MenuItem value="casual">Punjabi</MenuItem>
          <MenuItem value="casual">Hindi</MenuItem>
          <MenuItem value="casual">French</MenuItem>
        </Select>
      </FormControl>

      <FormControl fullWidth sx={{mt: 2}}>
        <InputLabel id="education-level-select-label">
          Education Level
        </InputLabel>
        <Select
          labelId="education-level-select-label"
          id="education-level-select"
          value={educationLevel}
          label="Education Level"
          onChange={handleEducationLevelChange}
        >
          <MenuItem value="elementary">Elementary</MenuItem>
          <MenuItem value="middle_school">Middle School</MenuItem>
          <MenuItem value="high_school">High School</MenuItem>
          <MenuItem value="undergraduate">Undergraduate</MenuItem>
          <MenuItem value="graduate">Graduate</MenuItem>
          <MenuItem value="phd">PhD</MenuItem>
        </Select>
      </FormControl>

      <FormControl fullWidth sx={{mt: 2}}>
        <InputLabel id="expertise-select-label">Expertise</InputLabel>
        <Select
          labelId="expertise-select-label"
          id="expertise-select"
          value={expertise}
          label="Interests"
          onChange={handleExpertiseChange}
        >
          <MenuItem value="computer_science">Computer Science</MenuItem>
          <MenuItem value="biology">Biology</MenuItem>
          <MenuItem value="history">History</MenuItem>
          <MenuItem value="cinematics">Cinematics</MenuItem>
          <MenuItem value="sports">Sports</MenuItem>
        </Select>
      </FormControl>
    </aside>
  );
}

export default Sidebar;
