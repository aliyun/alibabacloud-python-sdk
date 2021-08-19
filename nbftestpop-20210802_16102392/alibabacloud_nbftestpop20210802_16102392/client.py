# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_nbftestpop20210802_16102392 import models as nbf_test_pop_20210802__16102392_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


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
        self._endpoint = self.get_endpoint('nbftestpop', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add(
        self,
        request: nbf_test_pop_20210802__16102392_models.AddRequest,
    ) -> nbf_test_pop_20210802__16102392_models.AddResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_with_options(request, headers, runtime)

    async def add_async(
        self,
        request: nbf_test_pop_20210802__16102392_models.AddRequest,
    ) -> nbf_test_pop_20210802__16102392_models.AddResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_with_options_async(request, headers, runtime)

    def add_with_options(
        self,
        request: nbf_test_pop_20210802__16102392_models.AddRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nbf_test_pop_20210802__16102392_models.AddResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.x):
            query['x'] = request.x
        if not UtilClient.is_unset(request.y):
            query['y'] = request.y
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            nbf_test_pop_20210802__16102392_models.AddResponse(),
            self.do_roarequest('Add', '2021-08-02_16-10-23-92', 'HTTP', 'GET', 'AK', f'/kxThree/headerTest', 'json', req, runtime)
        )

    async def add_with_options_async(
        self,
        request: nbf_test_pop_20210802__16102392_models.AddRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nbf_test_pop_20210802__16102392_models.AddResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.x):
            query['x'] = request.x
        if not UtilClient.is_unset(request.y):
            query['y'] = request.y
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            nbf_test_pop_20210802__16102392_models.AddResponse(),
            await self.do_roarequest_async('Add', '2021-08-02_16-10-23-92', 'HTTP', 'GET', 'AK', f'/kxThree/headerTest', 'json', req, runtime)
        )
