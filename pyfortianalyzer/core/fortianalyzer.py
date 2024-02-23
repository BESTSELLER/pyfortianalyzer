import requests


class FortiAnalyzer(object):
    """API class for FortiAnalyzer login management and post requests.
    """

    def __init__(self, api, **kwargs):
        self.api = api
        self.base_url = f"{self.api.host}/jsonrpc"

    def post(self, method: str, params: dict):
        """Sends a POST request to the FortiAnalyzer API.

        Args:
            method (str): get, exec, add, set, update, delete.
            params (dict): Payload data to send with the request.

        Returns:
            dict: JSON data.
        """

        headers = {
            "Authorization": f"Bearer {self.api.token}"
        }

        data = {
            "method": method,
            "params": [params]
        }

        response = requests.post(url=self.base_url, json=data, verify=self.api.verify, headers=headers)

        # HTTP 200 OK
        if response.status_code == 200:
            return response.json()['result'][0]