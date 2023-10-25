from requests.adapters import HTTPAdapter, Retry
import requests
import atexit


class FortiAnalyzer(object):
    """API class for FortiAnalyzer login management and post requests.
    """

    def __init__(self, api):
        self.api = api
        self.base_url = f"{self.api.host}/jsonrpc"
        self.session = None
        self.sessionid = None
        self.max_retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
        atexit.register(self.logout)

    def login(self):
        """Logs in to the FortiAnalyzer API.

        Returns:
            dict: JSON data.
        """

        # Only log in, if we don't have a session stored in memory.
        if self.session is None or self.sessionid is None:
            self.session = requests.session()

            data = {
                "method": "exec",
                "params": [
                    {
                        "data": {
                            "passwd": self.api.password,
                            "user": self.api.username
                        },
                        "url": "/sys/login/user"
                    }
                ],
                "session": self.sessionid
            }

            self.session.mount("http://", HTTPAdapter(max_retries=self.max_retries))
            response = self.session.post(url=self.base_url, json=data, verify=self.api.verify)

            # HTTP 200 OK
            if response.status_code == 200:

                # Check if the FortiAnalyzer request is successful
                if response.json()['result'][0]['status']['code'] == 0:
                    self.sessionid = response.json()['session']

                return response.json()

    def logout(self):
        """Logs out of the FortiAnalyzer API.

        Returns:
            dict: JSON data.
        """

        # Only log out, if we have a session stored in-memory.
        if self.session:
            data = {
                "method": "exec",
                "params": [
                    {
                        "url": "/sys/logout"
                    }
                ],
                "session": self.sessionid
            }

            self.session.mount("http://", HTTPAdapter(max_retries=self.max_retries))
            response = self.session.post(url=self.base_url, json=data, verify=self.api.verify)

            # HTTP 200 OK
            if response.status_code == 200:
                self.session = None
                self.sessionid = None

    def login_check(self):
        """Checks if we have a valid login session.
        """

        # Check if we have a session in-memory
        if self.session:

            # Use the sys_status endpoint as a test to see if our session is valid
            data = {
                "method": "get",
                "params": [
                    {
                        "url": "/sys/status"
                    }
                ],
                "session": self.sessionid
            }

            self.session.mount("http://", HTTPAdapter(max_retries=self.max_retries))
            sys_status = self.session.post(url=self.base_url, json=data, verify=self.api.verify)

            # HTTP 200 OK
            if sys_status.status_code == 200:

                # If the FortiAnalyzer request is unsuccessful, then we log out and log in again.
                if sys_status.json()['result'][0]['status']['code'] != 0:
                    self.logout()
                    self.login()

        # Otherwise, log in again.
        else:
            self.login()

    def post(self, method: str, params: dict):
        """Sends a POST request to the FortiAnalyzer API.

        Args:
            method (str): get, exec, add, set, update, delete.
            params (dict): Payload data to send with the request.

        Returns:
            dict: JSON data.
        """

        self.login_check()

        data = {
            "method": method,
            "params": [params],
            "session": self.sessionid
        }

        self.session.mount("http://", HTTPAdapter(max_retries=self.max_retries))
        response = self.session.post(url=self.base_url, json=data, verify=self.api.verify)

        # HTTP 200 OK
        if response.status_code == 200:
            return response.json()['result'][0]