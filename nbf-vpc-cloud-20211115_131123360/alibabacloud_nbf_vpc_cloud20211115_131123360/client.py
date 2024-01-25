# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_nbf_vpc_cloud20211115_131123360 import models as nbf__vpc__cloud_20211115__131123360_models


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
        self._endpoint = self.get_endpoint('nbf-vpc-cloud', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def adada_awith_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nbf__vpc__cloud_20211115__131123360_models.AdadaAResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='AdadaA',
            version='2021-11-15_13-11-23-360',
            protocol='HTTP',
            pathname=f'/caihe_cloud_product_1/1_0_0/adadaA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nbf__vpc__cloud_20211115__131123360_models.AdadaAResponse(),
            self.call_api(params, req, runtime)
        )

    async def adada_awith_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nbf__vpc__cloud_20211115__131123360_models.AdadaAResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='AdadaA',
            version='2021-11-15_13-11-23-360',
            protocol='HTTP',
            pathname=f'/caihe_cloud_product_1/1_0_0/adadaA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nbf__vpc__cloud_20211115__131123360_models.AdadaAResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def adada_a(self) -> nbf__vpc__cloud_20211115__131123360_models.AdadaAResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.adada_awith_options(headers, runtime)

    async def adada_a_async(self) -> nbf__vpc__cloud_20211115__131123360_models.AdadaAResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.adada_awith_options_async(headers, runtime)

    def yx_test_api_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nbf__vpc__cloud_20211115__131123360_models.YxTestApiResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='YxTestApi',
            version='2021-11-15_13-11-23-360',
            protocol='HTTPS',
            pathname=f'/caihe_cloud_product_1/1_0_0/yxTestApi',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nbf__vpc__cloud_20211115__131123360_models.YxTestApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def yx_test_api_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nbf__vpc__cloud_20211115__131123360_models.YxTestApiResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='YxTestApi',
            version='2021-11-15_13-11-23-360',
            protocol='HTTPS',
            pathname=f'/caihe_cloud_product_1/1_0_0/yxTestApi',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nbf__vpc__cloud_20211115__131123360_models.YxTestApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def yx_test_api(self) -> nbf__vpc__cloud_20211115__131123360_models.YxTestApiResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.yx_test_api_with_options(headers, runtime)

    async def yx_test_api_async(self) -> nbf__vpc__cloud_20211115__131123360_models.YxTestApiResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.yx_test_api_with_options_async(headers, runtime)
