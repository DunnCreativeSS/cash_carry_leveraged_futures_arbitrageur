from swaps.connection.restapi_sync_client import RestApiSyncClient
from swaps.constant import *
from swaps.model.wallet import *
from swaps.utils import *


class GetAccountWithdrawAddressService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/account/withdraw/address"

        def parse(dict_data):
            data_list = dict_data.get("data", [])
            return default_parse_list_dict(data_list, ChainWithdrawAddress)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)






