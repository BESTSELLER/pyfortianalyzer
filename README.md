# pyfortianalyzer
Python API client library for Fortinet's [FortiAnalyzer](https://www.fortinet.com/products/management/fortianalyzer).

It does not provide all endpoints or functionality available. We encourage to make a pull request with needed missing endpoints.

> **Note:** This library has been built and tested for FortiAnalyzer v7.2.x.

## Installation
To install run `pip install pyfortianalyzer`.

Alternatively, you can clone the repo and run `python setup.py install`.

## Quick Start
To begin, import pyfortianalyzer and instantiate the API.

We need to provide the IP or FQDN to the FortiAnalyzer instance and a user with access to the API.
Optionally, its possible to set `adom` which defaults to `root` and `verify` which defaults to `True`.

**Code**
```
import pyfortianalyzer
fortianalyzer = pyfortianalyzer.api(
    host = "https://fortianalyzer.example.com",
    token = "<api_token_from_faz>"
)
```

## Examples
### List all FortiGates.
There is a ton of data for a single FortiGate. This code retrieves all of it, but only prints the name of the FortiGates.

**Code**
```
faz_fortigates = fortianalyzer.fortigates.all()
for faz_fortigate in faz_fortigates['data']:
    print(faz_fortigate['name'])
```

**Output**
```
FortiGate-VM64-1
FortiGate-VM64-2
FortiGate-VM64-3
```

### Status object.
You can use the status object to check if the request is a success or not, and retrieve the error message.

**Code**
```
faz_fortigate = fortianalyzer.fortigates.all(fortigate="FortiGate-VM64-4")
if faz_fortigate['status']['code'] == 0:
    print(faz_fortigate['data']['name'])
else:
    print(faz_fortigate['status'])
```

**Output**
```
"status": {
    "code": -3,
    "message": "Object does not exist"
}
```


### Custom API request.
Since FortiAnalyzer consists of a ton of API endpoints, not all are supported natively in this module.

You can however use the custom_request function in order to reach any API endpoint in FortiAnalyzer.

**Code**
```
faz_custom_request = fortianalyzer.system.custom_request(
    params={
        "url": "/dvmdb/adom/root/device",
        "option": [
            "get meta"
        ]
    },
    method="get"
)
print(json.dumps(faz_custom_request, indent=4))
```

### Adding a FortiGate
This adds a FortiGate in the Device Manager with the minimum required fields.

**Code**
```
faz_fortigate_add = fortianalyzer.fortigates.add(
    serial = "FGT60FTK1234ABCD"
)
print(faz_fortigate_add)
```

**Output**
```
{
    "data": {
        "device": {
            "beta": -1,
            "conn_mode": 1,
            "dev_status": 1,
            "flags": 67371008,
            "hostname": "FGT60FTK1234ABCD",
            "maxvdom": 10,
            "mgmt_id": 965165689,
            "mgmt_mode": 2,
            "mr": -1,
            "name": "FGT60FTK1234ABCD",
            "oid": 3999,
            "os_type": 0,
            "os_ver": -1,
            "patch": -1,
            "platform_id": 19,
            "platform_str": "FortiGate-60F",
            "sn": "FGT60FTK1234ABCD",
            "source": 1,
            "tab_status": "<unknown>"
        }
    },
    "status": {
        "code": 0,
        "message": "OK"
    },
    "url": "/dvm/cmd/add/device"
}
```

### Updating a FortiGate
This updates a FortiGate in the Device Manager.

**Code**
```
faz_fortigate_update = fortianalyzer.fortigates.update(
    fortigate = "FortiGate-VM64-1",
    description = "Test FortiGate"
)
print(faz_fortigate_update)
```

**Output**
```
{
    "data": {
        "name": "FortiGate-VM64-1"
    },
    "status": {
        "code": 0,
        "message": "OK"
    },
    "url": "/dvmdb/adom/root/device/FortiGate-VM64-1"
}
```

### Deleting a FortiGate
This deletes a FortiGate in the Device Manager.

**Code**
```
faz_fortigate_delete = fortianalyzer.fortigates.delete(
    fortigate = "FortiGate-VM64-1"
)
print(faz_fortigate_delete)
```

**Output**
```
{
    "status": {
        "code": 0,
        "message": "OK"
    },
    "url": "/dvm/cmd/del/device"
}
```