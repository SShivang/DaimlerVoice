import React from 'react';
import './App.css';
import { subscribeToServer } from './api';
import { Button } from 'react-materialize'
import Text from './screen/text'
import "materialize-css/dist/css/materialize.css"
import { handle } from './socketHandler'

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      view: ['MAIN'],
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

  changeDisplayString(str) {
    this.setState({ noteStr: str })
  }

  render() {
    let elemArr = []
    const view = this.state.view[this.state.view.length-1]
    if(view === 'NOTE' ){
      elemArr.push(<div key='NOTE'><div style={{margin: '20em 3em 0em 3em'}}>
      <Text displayStr={this.state.noteStr} change={this.changeDisplayString} />
      </div>
      <Button waves="light">
        Save
      </Button></div>)
    }

    if(view === 'MAIN'){
      elemArr.push(
        <div className="center" key="MAIN">
          <h2>Main View. What would you like to do?</h2>
        </div>    
      )
    }

    return (
      <div className="App-center">
        {elemArr}


      </div>
    );
  }

}

export default App;
