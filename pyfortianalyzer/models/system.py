from pyfortianalyzer.core.fortianalyzer import FortiAnalyzer


class System(FortiAnalyzer):
    """API class for the FortiAnalyzer system.
    """

    def __init__(self, **kwargs):
        super(System, self).__init__(**kwargs)

    def custom_request(self, params: dict = None, method: str = "get"):
        """Send a custom request to the FortiManager API.

        Args:
            params (dict): Payload parameters to send with the request.
            method (str): get, exec, add, set, update, delete. Default is get.

        Returns:
            dict: JSON data.
        """

        params = params

        return self.post(method=method, params=params)

    def ha(self):
        """Obtain FortiAnalyzer HA information and status of the system.

        Returns:
            dict: JSON data.
        """
   
        params = {
            "url": "/sys/ha/status"
        }

        return self.post(method="get", params=params)
 
    def reboot(self, message: str=None):
        """Reboots the FortiAnalyzer.

        Args:
            message (str, optional): Optional message to be stored in the event log.

        Returns:
            dict: JSON data.
        """
   
        params = {
            "url": "/sys/reboot",
            "data": {
                "message": message
            }
        }

        return self.post(method="exec", params=params)

    def status(self):
        """Retrieves the FortiAnalyzer system status.

        Returns:
            dict: JSON data.
        """
   
        params = {
            "url": "/sys/status"
        }

        return self.post(method="get", params=params)

    def tasks(self, task:int=None, filter: list=None, loadsub: int=0):
        """Retrieves all FortiAnalyzer tasks or a single task.

        Args:
            task (int): ID of a specific task.
            filter (list): Filter the result according to a set of criteria. example: List [ "{attribute}", "==", "{value}" ]
            loadsub (int): Enable or disable the return of any sub-objects.

        Returns:
            dict: JSON data.
        """
   
        params = {
            "url": "/task/task",
            "filter": filter,
            "loadsub": loadsub
        }

        # Retrieve a single task
        if task:
            params['url'] = f"/task/task/{task}/line"

        return self.post(method="get", params=params)