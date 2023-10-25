from pyfortianalyzer.core.fortianalyzer import FortiAnalyzer


class ADOMs(FortiAnalyzer):
    """API class for ADOM management.
    """

    def __init__(self, **kwargs):
        super(ADOMs, self).__init__(**kwargs)

    def all(self, name: str=None):
        """Retrieves all ADOMs or a single ADOM.

        Args:
            name (str): Name of a ADOM.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": "/dvmdb/adom"
        }

        # Retrieve a specific ADOM
        if name:
            params['url'] += f"/{name}"

        return self.post(method="get", params=params)