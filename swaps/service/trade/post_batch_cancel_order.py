from swaps.connection.restapi_sync_client import RestApiSyncClient
from swaps.constant import *
from swaps.utils import *
from swaps.model.trade import *

class PostBatchCancelOrderService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/order/orders/batchcancel"

        def parse(dict_data):
            data = dict_data.get("data", {})
            return default_parse_fill_directly(data, BatchCancelResult)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)






