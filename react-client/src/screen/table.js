import React from 'react';
import { Table } from 'react-materialize'
import "materialize-css/dist/css/materialize.css"

class PartTable extends React.Component {
    // constructor(props) {
    //     super(props);


    // }



    render() {
        return (
            <div style={{margin:'3em 3em'}}>
                <Table>
  <thead>
<tr>
<th>HD DD MCM Sensor</th>
<th>Wire / Shrink Tube Color</th>
<th>Probe Part #</th>
<th>Replacement Pigtail Part #</th>
<th>Sensor Location / Section Reference</th>
</tr>
</thead>
<tbody>
<tr>
<td>Crankshaft Position Sensor</td>
<td>Red/Red</td>
<td>  DKI470E16022-37</td>
<td>  A0001506136</td>
<td>

<img src="https://extranet-ddc.freightliner.com/Power_service/Literature/Graphics/d010178.png" width="468" height="288" alt="d140582"/>
{/* <a href="../157/157_08_01_0C.xml#v2678953" target="_blank">Refer to section "Removal of the Crankshaft Position Sensor"</a> */}
</td>
</tr>
<tr>
<td> Intake Manifold Temperature Sensor DD13, DD15 and DD16</td>
<td>Red/Red</td>
<td> DKI470E16022-37</td>
<td> A0001506136</td>
<td>
<img src="https://extranet-ddc.freightliner.com/Power_service/Literature/Graphics/d140582.png" width="468" height="288" alt="d140582" onClick="ShowImage('d140582.png', 'd140582')"/>
{/* <a href="../157/157_08_01_0C.xml#v2678953" target="_blank">Refer to section "Removal of the Crankshaft Position Sensor"</a> */}
</td>
</tr>
<tr>
<td> Turbocharger Speed Sensor</td>
<td>Red/Red</td>
<td>DKI470E16022-37</td>
<td> N/A</td>
<td>
<img src="https://extranet-ddc.freightliner.com/Power_service/Literature/Graphics/d090140.png" width="468" height="288" alt="d090140" onClick="ShowImage('d090140.png', 'd090140')"/>
{/* <a href="../157/157_08_01_34.xml#v2679926" target="_blank">Refer to section "Removal of the Turbocharger Speed Sensor"</a> */}
</td>
</tr>
<tr>
<td> Water Pump Speed Sensor</td>
<td>Red/Red</td>
<td>DKI470E16022-37</td>
<td> A0001506336</td>
<td>
<img src="https://extranet-ddc.freightliner.com/Power_service/Literature/Graphics/d200067.png" width="144" height="79" alt="d200067" onClick="ShowImage('d200067.png', 'd200067')"/>
{/* <a href="../157/157_06_0B_02.xml#v2622507" target="_blank">Refer to section "Removal of the Variable Speed Water Pump"</a> */}
</td>
</tr>
</tbody>

                </Table>
            </div>
        );
    }

}

export default PartTable;


