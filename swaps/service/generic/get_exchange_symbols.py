from swaps.connection.restapi_sync_client import RestApiSyncClient
from swaps.constant.system import HttpMethod
from swaps.model.generic import *
from swaps.utils import *


class GetExchangeSymbolsService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/common/symbols"

        def parse(dict_data):
            data_list = dict_data.get("data", [])
            return default_parse_list_dict(data_list, Symbol, [])

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params, parse)
