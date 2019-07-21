smartList = [
{
'Step' : 0,
'Text' : "Finished with diagnostics. Continue?",
'YES'  : 0,
'NO'   : 0,
'Value-Required' : 'NO'

},

{
  'Step' : 1,
  'Text' : "This is the Wiring Harness Guided Diagnostic with fault code SPN 3563 / FMI 3",
  'YES'  : 2,
  'NO'   : 2,
  'Value-Required' : 'NO'

},

{
 'Step' : 2,
 'Text' : "Disconnect the intake manifold pressure/temperature sensor and inspect the harness side for bent, spread, or corroded terminals. Is any damage to the harness found?",
 'YES'  : 3,
 'NO'   : 4,
 'YES_STAT' : "Harness Damage Report: Damage to the harness was found. Please proceed to the appropriate repairs.",
 'NO_STAT' : "Harness Damage Report: Damage to the harness was not found. Pleace proceed to turn on the ignition.",
 'Value-Required' : 'YES'
},

{
  'Step' : 3,
  'Text' : "Repair the wiring harness as needed. Advance to TechLane for repair and SRT information.",
  'YES'  : 0,
  'NO'   : 0,
  'Value-Required' : 'NO'

},

{
  'Step' : 4,
  'Text' : "Ignition On",
  'YES'  : 5,
  'NO'   : 5,
  'Value-Required' : 'NO'

},

{
  'Step' : 5,
  'Text' : "Use the link below to determine the correct diagnostic probe part number for the Intake Manifold Pressure/Temperature Sensor. https://extranet-ddc.freightliner.com/Power_service/Literature/Content/13A/13A_0B_02_00.xml Measure the voltage between pin 1 of the intake manifold pressure/temperature sensor harness connector and ground. Enter the voltage below. Is the voltage less than or equal to 6 V?",
  'YES'  : 3,
  'NO'   : 6,
  'YES_STAT' : "Primary Voltage Status: Voltage is less than or equal to 6 V. Proceed to appropriate wiring harness repairs.",
  'NO_STAT' : "Primary Voltage Status: Voltage is greater than 6 V. Please proceed to secondary voltage check.",
  'Value-Required' : 'YES'

},

{
  'Step' : 6,
  'Text' : "Check for the presence of voltage between pins 2 and 4 on the intake manifold pressure/temperature sensor harness connector. Is voltage present?",
  'YES'  : 7,
  'NO'   : 3,
  'YES_STAT' : "Secondary Voltage Status: Voltage is present between the two connectors. Please proceed to the next component diagnostic test, if applicable.",
  'NO_STAT' : "Secondary Voltage Status: Voltage is not present between the two connectors. Please proceed to the appropriate wiring harness repairs.",
  'Value-Required' : 'YES'

},

{
  'Step' : 7,
  'Text' : "This component troubleshooting is complete with no trouble found. Go to the next component.",
  'YES'  : 0,
  'NO'   : 0,
  'Value-Required' : 'NO'

},
]

inventory = {
   "air bags" : 3
}

parts = {
"Repair-harness" : ["fuel shutoff valve", "fuel line pressure sensor", "fuel compensation pressure sensor", "intake throttle valve", "wastegate solenoid sensor", "intake air delta pressure", "intake manifold pressure/temp", "EGR valve", "brake gate solenoid", "turbo inlet temp"]
}
