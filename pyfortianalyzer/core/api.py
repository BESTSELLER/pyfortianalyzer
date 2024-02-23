from pyfortianalyzer.models.adoms import ADOMs
from pyfortianalyzer.models.fortigates import FortiGates
from pyfortianalyzer.models.system import System


class Api(object):
    """Base API class.
    """

    def __init__(self, host: str, token: str, adom: str="root", verify: bool=True, **kwargs):
        self.host = host
        self.token = token
        self.adom = adom
        self.verify = verify
        self.session = None
        self.sessionid = None

    @property
    def adoms(self):
        """Endpoints related to ADOM management.
        """
        return ADOMs(api=self)

    @property
    def fortigates(self):
        """Endpoints related to FortiGate management.
        """
        return FortiGates(api=self)

    @property
    def system(self):
        """Endpoints related to the FortiAnalyzer system.
        """
        return System(api=self)