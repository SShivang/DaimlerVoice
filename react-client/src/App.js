import React from 'react';
import logo from './logo.svg';
import './App.css';
import { subscribeToTimer } from './api';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state={
      displayStr: 'Default'
    }
    subscribeToTimer((err, timestamp) => { console.log('Heard somthing');
    console.log(timestamp);
    this.setState({displayStr: timestamp.data})});
  }

render(){
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Yeet: {this.state.displayStr}
        </p>
        
      </header>
    </div>
  );
}
  
}

export default App;
