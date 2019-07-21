

def food(): 
    pass


customers = [
    {
    "customer_id": 1
    "name": "John Smith",
    "phone": "3057854963",
    "customer_approval": True
    }
]

diagnostic = [
    {
    "diagnostic_id": 1, 
    "comment": "fix sink", 
    "timestamp": '01-02-2019',
    "status": "Not-Started",
    "fault-code": 209,
    "customer_id": 1
    }
]

diagnostic_log = [
    {
        "diagnostic_log_id":1
        "text":"Shut engine down"
        "arrtibute": "Yes"
        "diagnostic_id": 1 
    }
]

result_procedure = [
    {
        "result_procedure_id": 1, 
        "diagnostic_id": 1
    }
]

procedure_log = [
    {
        "procedure_log_id": 1, 
        "text": "Is pressure over 30psi", 
        "attribute": "27psi",
        "result_procedure_id": 1
    }
]

part = [
    {
        "part_id": 1, 
        "part_description": "Sink value 7B",
        "result_procedure_id":1
    }
]

warrenty = [
    {
        "warrenty_id":1
        "covered": False
        "timestamp": "02-17-2012"
        "part_id":1
    }
]