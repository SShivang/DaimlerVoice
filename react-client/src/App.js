import React from 'react';
import './App.css';
import { subscribeToServer } from './api';
import { Button } from 'react-materialize'
import Text from './screen/text'
import "materialize-css/dist/css/materialize.css"
import {handle} from './socketHandler'

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      view: 'Main',
      noteStr: 'Default'
    }
    this.changeDisplayString = this.changeDisplayString.bind(this)
    subscribeToServer((obj) => {
      this.setState(
        handle(this.state, obj)
      )
      console.log('State is now: ')
      console.log(this.state)
    });
  }

  changeDisplayString(str){
    this.setState({noteStr: str})
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <p>
            {this.state.noteStr}
          </p>
          <Button waves="light" style={{ marginRight: '5px' }}>
            button
        </Button>
          <Text displayStr={this.state.noteStr} change={this.changeDisplayString}/>


        </header>
      </div>
    );
  }

}

export default App;
