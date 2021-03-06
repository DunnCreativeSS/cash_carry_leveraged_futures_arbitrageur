from swaps.connection.restapi_sync_client import RestApiSyncClient
from swaps.constant import *
from swaps.utils.json_parser import *
from swaps.model.algo import *


class GetOrderHistoryService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/algo-orders/history"

        def parse(dict_data):
            data = dict_data.get("data", {})
            return default_parse_list_dict(data, OrderHistoryItem)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)
