import React from 'react';
import './App.css';
import { subscribeToServer } from './api';
import { Button, Card, Chip, Icon } from 'react-materialize'
import Text from './screen/text'
import "materialize-css/dist/css/materialize.css"
import { handle } from './socketHandler'
import PartTable from './screen/table';
import Report from './screen/report'

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      view: ['MAIN'],
      notes: [],
      step: '0step',
      table: false,
      report: []
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
        <div>
            <span>
              <Chip style={{color:'white', margin: '1em .5em', backgroundColor:'#60bfbf', display: 'inline-flex' ,verticalAlign:'middle', padding:'.1em 1em'}}>
              <Icon>insert_chart</Icon>
              <div style={{padding:'0em .8em'}}>
              View Report

              </div>
            </Chip>
            </span>
            <span >
              <Chip style={{color:'white', margin: '1em .5em', backgroundColor:'#60bfbf', display: 'inline-flex' ,verticalAlign:'middle', padding:'.1em 1em'}}>
                <Icon>face</Icon>
                <div style={{padding:'0em .8em'}}>

                Contact Customer
                </div>
            </Chip>
            </span>
          </div>
      </div>
        </div>)
    }

    if (view === 'MAIN') {
      elemArr.push(
        <div className="center" key="MAIN">
          <Card>

          <h2>Welcome to Spaceship! </h2>
          <hr></hr>
          <h5>...your end-to-end voice solution for technical repairs.</h5>
          <p>Try one of the commands below</p>
          
          </Card>
          
          <div>
            <span>
              <Chip style={{color:'white', margin: '1em .5em', backgroundColor:'#60bfbf', display: 'inline-flex' ,verticalAlign:'middle', padding:'.1em 1em'}}>
              <Icon>insert_chart</Icon>
              <div style={{padding:'0em .8em'}}>
              View Report

              </div>
            </Chip>
            </span>
            <span>
              <Chip style={{color:'white', margin: '1em .5em', backgroundColor:'#60bfbf', display: 'inline-flex' ,verticalAlign:'middle', padding:'.1em 1em'}}>
              <Icon>aspect_ratio</Icon>
              <div style={{padding:'0em .8em'}}>
                Start Diagnostics
                </div>
            </Chip>
            </span>
            <span >
              <Chip style={{color:'white', margin: '1em .5em', backgroundColor:'#60bfbf', display: 'inline-flex' ,verticalAlign:'middle', padding:'.1em 1em'}}>
                <Icon>face</Icon>
                <div style={{padding:'0em .8em'}}>

                Contact Customer
                </div>
            </Chip>
            </span>
          </div>
         
        </div>
      )
    }
    else if (view === 'DIAG') {
      elemArr.push(
        

          this.state.table ? <div className="casual" style={{color:'black', margin:'0em 3em'}}>
          <Card>
            <h2 style={{fontSize:'2.56rem'}}>{this.state.step}</h2>
            <hr></hr>
            <h1>
              Running diagnostic
            </h1>

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
    else if(view === 'REPORT'){
      elemArr.push(
        <div style={{margin:'3em 3em', color:'white'}}>
          <h1>Report</h1>
          <h3> Diagnostic Status </h3>
          <Report arr={this.state.report} style={{color: 'black'}}/>
          <h3 style={{marginTop:'3em'}}>Notes</h3 >
          <Report arr={this.state.notes} style={{color: 'black'}}/>
          <div>
            <span>
              <Chip style={{color:'white', margin: '1em .5em', backgroundColor:'#60bfbf', display: 'inline-flex' ,verticalAlign:'middle', padding:'.1em 1em'}}>
              <Icon>insert_chart</Icon>
              <div style={{padding:'0em .8em'}}>
              View Report

              </div>
            </Chip>
            </span>
            <span >
              <Chip style={{color:'white', margin: '1em .5em', backgroundColor:'#60bfbf', display: 'inline-flex' ,verticalAlign:'middle', padding:'.1em 1em'}}>
                <Icon>face</Icon>
                <div style={{padding:'0em .8em'}}>

                Contact Customer
                </div>
            </Chip>
            </span>
          </div>
        </div>
        
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
