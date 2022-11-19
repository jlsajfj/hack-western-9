import doggo_placeholder from './placeholder.jpeg';
import './App.css';

import * as React from 'react';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';

// maybe insert some logic that changes the text based on image displayed

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={doggo_placeholder} className="doggo" alt="doggo" />
        <p>
          A potential entry in your backyard has been detected.
        </p>
        <Stack spacing={2} direction="row">
          <Button variant="contained" size="large">Approve</Button>
          <Button variant="outlined" size="large">Deny</Button>
        </Stack>
      </header>
    </div>
  );
}

export default App;
