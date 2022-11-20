import './App.css';

import * as React from 'react';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';

// maybe insert some logic that changes the text based on image displayed

function Main(props) {
  return (
    <header className="App-header">
      <img src={"http://100.126.117.114:5000/photo"} className="doggo" alt="doggo" />
      <p>
        A potential entry in your backyard has been detected.
      </p>
      <Stack spacing={2} direction="row">
        <Button variant="contained" size="large"
          onClick={() => {
            fetch("http://100.126.117.114:5000/approve");
          }}
        >Approve
        </Button>
        <Button variant="outlined" size="large"
          onClick={() => {
            fetch("http://100.126.117.114:5000/deny");
          }}>
          Deny
        </Button>
      </Stack>
    </header>
  );
}

function App() {
  return (
    <div className="App">
      <Main />
    </div>
  );
}

export default App;
