import React from 'react';
import './App.css';
import { subscribeToServer } from './api';
import { Button, Card } from 'react-materialize'
import Text from './screen/text'
import "materialize-css/dist/css/materialize.css"
import { handle } from './socketHandler'
import PartTable from './screen/table';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      view: ['MAIN'],
      notes: [],
      step: '0step',
      table: false,
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
    let index = this.state.notes.length-1
    this.setState({ notes: this.state.notes.slice(0, index).concat(str) })
  }

  render() {
    let elemArr = []
    const view = this.state.view[this.state.view.length - 1]
    if (view === 'NOTE') {
      elemArr.push(<div key='NOTE'><div style={{ margin: '10em 3em 0em 3em' }}>
        <Card>
        <Text displayStr={this.state.notes[this.state.notes.length-1]} change={this.changeDisplayString} />
        <Button waves="light" style={{ fontSize: '2em' }}>
          Save
      </Button>
        </Card>
      </div>
        </div>)
    }

    if (view === 'MAIN') {
      elemArr.push(
        <div className="center" key="MAIN">
          <h2 style={{color:'white'}}>Main View. What would you like to do?</h2>
          
         
        </div>
      )
    }
    else if (view === 'DIAG') {
      elemArr.push(
        

          this.state.table ? <div className="casual" style={{color:'black', margin:'0em 3em'}}>
          <Card>
            <h2 style={{fontSize:'2.56rem'}}>{this.state.step}</h2>
            <hr></hr>
            <h2>
              Running diagnostic
            </h2>

          </Card>
            <Card>
              <PartTable/>
            </Card>
          </div>
          : <div className="center" key="MAIN" style={{color:'black'}}>
          <Card>
            <h2 style={{fontSize:'2.56rem'}}>{this.state.step}</h2>
            <hr></hr>
            <h2>
              Running diagnostic
            </h2>

          </Card> </div>

      )
    }
    

    return (
      <div>
        {elemArr}


      </div>
    );
  }

}

export default App;
