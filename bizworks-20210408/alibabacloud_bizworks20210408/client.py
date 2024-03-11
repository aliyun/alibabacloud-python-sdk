# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_bizworks20210408 import models as biz_works_20210408_models


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
        self._endpoint = self.get_endpoint('bizworks', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def query_usage_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> biz_works_20210408_models.QueryUsageResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryUsage',
            version='2021-04-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            biz_works_20210408_models.QueryUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_usage_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> biz_works_20210408_models.QueryUsageResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryUsage',
            version='2021-04-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            biz_works_20210408_models.QueryUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_usage(self) -> biz_works_20210408_models.QueryUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_usage_with_options(runtime)

    async def query_usage_async(self) -> biz_works_20210408_models.QueryUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_usage_with_options_async(runtime)
