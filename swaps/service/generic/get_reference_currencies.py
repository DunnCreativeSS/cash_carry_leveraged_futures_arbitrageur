from swaps.connection.restapi_sync_client import RestApiSyncClient
from swaps.constant.system import HttpMethod
from swaps.model.generic import *
from swaps.utils import *



class GetReferenceCurrenciesService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/reference/currencies"

        def parse(dict_data):
            ret_list = []
            data_list = dict_data.get("data", [])
            if data_list and len(data_list):
                for reference_currency in data_list:
                    reference_currency_obj = default_parse(reference_currency, ReferenceCurrency, Chain)
                    ret_list.append(reference_currency_obj)
            return ret_list

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params, parse)






