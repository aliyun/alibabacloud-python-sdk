# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_saf20170331 import models as saf_20170331_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-hangzhou': 'saf.cn-shanghai.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('saf', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def execute_request_with_options(
        self,
        request: saf_20170331_models.ExecuteRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> saf_20170331_models.ExecuteRequestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return saf_20170331_models.ExecuteRequestResponse().from_map(
            self.do_rpcrequest('ExecuteRequest', '2017-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def execute_request_with_options_async(
        self,
        request: saf_20170331_models.ExecuteRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> saf_20170331_models.ExecuteRequestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return saf_20170331_models.ExecuteRequestResponse().from_map(
            await self.do_rpcrequest_async('ExecuteRequest', '2017-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_request(
        self,
        request: saf_20170331_models.ExecuteRequestRequest,
    ) -> saf_20170331_models.ExecuteRequestResponse:
        runtime = util_models.RuntimeOptions()
        return self.execute_request_with_options(request, runtime)

    async def execute_request_async(
        self,
        request: saf_20170331_models.ExecuteRequestRequest,
    ) -> saf_20170331_models.ExecuteRequestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_request_with_options_async(request, runtime)
