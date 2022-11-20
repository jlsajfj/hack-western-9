import './App.css';

import * as React from 'react';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';

import {toast} from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
toast.configure()

// maybe insert some logic that changes the text based on image displayed

function BodyData(props) {
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
            //notify()
          }}
        >Approve
        </Button>
        <Button variant="outlined" size="large"
          onClick={() => {
            fetch("http://100.126.117.114:5000/deny");
            //notify()
          }}>
          Deny
        </Button>
      </Stack>
    </header>
  );
}

function notify() {
  // Calling toast method by passing string
  toast('potatos')
}

function App() {
  return (
    <div className="App">
      <BodyData />
    </div>
  );
}

export default App;
