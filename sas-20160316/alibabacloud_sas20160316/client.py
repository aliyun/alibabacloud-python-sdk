# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_sas20160316 import models as sas_20160316_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "central"
        self._endpoint_map = {
            "cn-hangzhou": "tds.aliyuncs.com",
            "ap-southeast-3": "tds.ap-southeast-3.aliyuncs.com",
            "cn-shanghai-et2-b01": "tds.cn-shanghai-et2-b01.aliyuncs.com"
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint("sas", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def is_sas_service_opening_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return sas_20160316_models.IsSasServiceOpeningResponse().from_map(self.do_request("IsSasServiceOpening", "HTTPS", "POST", "2016-03-16", "AK", None, request.to_map(), runtime))

    def is_sas_service_opening(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.is_sas_service_opening_with_options(request, runtime)

    def get_events_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return sas_20160316_models.GetEventsCountResponse().from_map(self.do_request("GetEventsCount", "HTTPS", "POST", "2016-03-16", "AK", None, request.to_map(), runtime))

    def get_events_count(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_events_count_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
