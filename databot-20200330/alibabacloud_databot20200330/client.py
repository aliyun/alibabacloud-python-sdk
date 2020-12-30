# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_databot20200330 import models as databot_20200330_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('databot', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def query_databot_with_options(
        self,
        request: databot_20200330_models.QueryDatabotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> databot_20200330_models.QueryDatabotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return databot_20200330_models.QueryDatabotResponse().from_map(
            self.do_rpcrequest('QueryDatabot', '2020-03-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_databot_with_options_async(
        self,
        request: databot_20200330_models.QueryDatabotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> databot_20200330_models.QueryDatabotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return databot_20200330_models.QueryDatabotResponse().from_map(
            await self.do_rpcrequest_async('QueryDatabot', '2020-03-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_databot(
        self,
        request: databot_20200330_models.QueryDatabotRequest,
    ) -> databot_20200330_models.QueryDatabotResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_databot_with_options(request, runtime)

    async def query_databot_async(
        self,
        request: databot_20200330_models.QueryDatabotRequest,
    ) -> databot_20200330_models.QueryDatabotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_databot_with_options_async(request, runtime)
