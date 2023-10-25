from pyfortianalyzer.core.fortianalyzer import FortiAnalyzer


class FortiGates(FortiAnalyzer):
    """API class for FortiGates.
    """

    def __init__(self, **kwargs):
        super(FortiGates, self).__init__(**kwargs)

    def all(self, fortigate: str=None, adom: str=None):
        """Retrieves all FortiGates or a single FortiGate.

        Args:
            name (str): Name of a specific FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/dvmdb/adom/{adom or self.api.adom}/device",
            "option": [
                "get meta"
            ]
        }

        # Retrieve a single FortiGate
        if fortigate:
            params['url'] += f"/{fortigate}"

        return self.post(method="get", params=params)

    def add(self, serial: str, name: str=None, mgmt_mode: str="fmgfaz", adm_usr: str=None, adm_pass: str=None, description: str=None, meta_fields: dict=None, adom: str=None):
        """Adds a new FortiGate in FortiAnalyzer.

        Args:
            name (str): Name of the FortiGate. Default is serial number.
            serial (str): Serial number of the FortiGate.
            mgmt_mode (str): unreg, fmg, faz, fmgfaz. Default is fmgfaz.
            adm_usr (str, optional): Default admin username.
            adm_pass (str, optional): Default admin password.
            description (str, optional): Description of the FortiGate.
            meta_fields (dict, optional): Meta fields for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": "/dvm/cmd/add/device",
            "data": {
                "adom": adom or self.api.adom,
                "device": {
                    "mgmt_mode": mgmt_mode,
                    "device action": "add_model",
                    "name": name or serial,
                    "sn": serial
                }
            }
        }

        # Optional fields
        if adm_usr:
            params['data']['device']['adm_usr'] = adm_usr

        if adm_pass:
            params['data']['device']['adm_pass'] = adm_pass

        if description:
            params['data']['device']['desc'] = description

        if meta_fields:
            params['data']['device']['meta fields'] = meta_fields

        return self.post(method="exec", params=params)
    
    def update(self, fortigate: str, meta_fields: dict=None, adm_pass: str=None, adm_usr: str=None, description: str=None, ip: str=None, latitude: float=None, longitude: float=None, name: str=None, adom: str=None):
        """Updates a FortiGate.

        Args:
            fortigate (str): Name of the FortiGate to update.
            meta_fields (dict): All meta fields in a dict.
            adm_pass (str, optional): Admin password.
            adm_usr (str, optional): Admin username.
            description (str, optional): Description of the FortiGate.
            ip (str, optional): Public IP address of the FortiGate.
            latitude (float, optional): GPS latitude coordinates.
            longitude (float, optional): GPS longitude coordinates.
            name (str, optional): Name of the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/dvmdb/adom/{adom or self.api.adom}/device/{fortigate}",
            "data": {}
        }

        # Update optional fields
        if adm_pass:
            params['data']['adm_pass'] = adm_pass

        if adm_usr:
            params['data']['adm_usr'] = adm_usr

        if description:
            params['data']['desc'] = description

        if ip:
            params['data']['ip'] = ip

        if latitude:
            params['data']['latitude'] = latitude

        if longitude:
            params['data']['longitude'] = longitude

        if name:
            params['data']['name'] = name

        if meta_fields:
            params['data']['meta fields'] = meta_fields

        return self.post(method="update", params=params)
    
    def delete(self, fortigate: str, adom:str=None):
        """Deletes a FortiGate.

        Args:
            fortigate (str): Name of the FortiGate to delete.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": "/dvm/cmd/del/device",
            "data": {
                "adom": adom or self.api.adom,
                "device": fortigate
            }
        }

        return self.post(method="exec", params=params)