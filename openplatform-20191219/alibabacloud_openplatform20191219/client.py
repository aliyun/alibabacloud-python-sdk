# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_openplatform20191219 import models as open_platform_20191219_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('openplatform', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def authorize_file_upload_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return open_platform_20191219_models.AuthorizeFileUploadResponse().from_map(self.do_request('AuthorizeFileUpload', 'HTTPS', 'GET', '2019-12-19', 'AK', TeaCore.to_map(request), None, runtime))

    def authorize_file_upload(self, request):
        runtime = util_models.RuntimeOptions()
        return self.authorize_file_upload_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
