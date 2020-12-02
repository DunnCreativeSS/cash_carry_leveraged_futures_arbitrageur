from swaps.connection.restapi_sync_client import RestApiSyncClient
from swaps.constant.system import HttpMethod
from swaps.model.etf import *
from swaps.utils import *



class GetEtfSwapConfigService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/etf/swap/config"

        def parse(dict_data):
            data_info = dict_data.get("data", {})
            return default_parse(data_info, EtfSwapConfig, UnitPrice)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params, parse)






