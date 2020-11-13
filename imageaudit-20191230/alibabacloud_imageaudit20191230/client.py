# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_imageaudit20191230 import models as imageaudit_20191230_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "regional"
        self.check_config(config)
        self._endpoint = self.get_endpoint("imageaudit", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def scan_text_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return imageaudit_20191230_models.ScanTextResponse().from_map(self.do_request("ScanText", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def scan_text(self, request):
        runtime = util_models.RuntimeOptions()
        return self.scan_text_with_options(request, runtime)

    def scan_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return imageaudit_20191230_models.ScanImageResponse().from_map(self.do_request("ScanImage", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def scan_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.scan_image_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
