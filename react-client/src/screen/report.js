import React from 'react';
import {Collapsible, CollapsibleItem} from 'react-materialize'
import "materialize-css/dist/css/materialize.css"

class Report extends React.Component {
//   constructor(props) {
//     super(props);  
//   }



  render() {
    const jsxArr = this.props.arr.map((item)=>{
        return (<CollapsibleItem header={item}>
            {item}
        </CollapsibleItem>)
    })
    return (
      <div style={{color:'black'}}>
          <Collapsible>
            {jsxArr}
          </Collapsible>
      </div>
    );
  }

}

export default Report;

