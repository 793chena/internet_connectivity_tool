from .types import *
from .dns_connectivity import DNSConnectivity
from .http_connectivity import HTTPConnectivity
from .https_connectivity import HTTPSConnectivity

class TestFactory:
    def create_test(type, properties):
        if type == DNS_CONNECTIVITY:
            return DNSConnectivity(properties["address"])
        elif type == HTTP_CONNECTIVITY:
            return HTTPConnectivity(properties["address"], properties["method"], properties["attributes"])
        elif type == HTTPS_CONNECTIVITY:
            return HTTPSConnectivity(properties["address"], properties["method"], properties["attributes"])
        else:
            raise NameError('Test type not found')