import React from 'react';
import {TextInput } from 'react-materialize'
import "materialize-css/dist/css/materialize.css"

class Text extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      displayStr: 'Default'

    }
    this.onChange = this.onChange.bind(this)
  
  }

  onChange(event){
    event.persist()  
    console.log('Changed to be ')
    console.log(event.target.value)
    this.props.change(event.target.value)
  }

  render() {
    return (
      <div>
          <TextInput value={this.props.displayStr} onChange={this.onChange}/>
      </div>
    );
  }

}

export default Text;
