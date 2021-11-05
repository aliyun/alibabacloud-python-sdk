# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_rmc20211104 import models as rmc20211104_models
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
        self._endpoint = self.get_endpoint('rmc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def search_resources_with_options(
        self,
        request: rmc20211104_models.SearchResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rmc20211104_models.SearchResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rmc20211104_models.SearchResourcesResponse(),
            self.do_rpcrequest('SearchResources', '2021-11-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_resources_with_options_async(
        self,
        request: rmc20211104_models.SearchResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rmc20211104_models.SearchResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rmc20211104_models.SearchResourcesResponse(),
            await self.do_rpcrequest_async('SearchResources', '2021-11-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_resources(
        self,
        request: rmc20211104_models.SearchResourcesRequest,
    ) -> rmc20211104_models.SearchResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_resources_with_options(request, runtime)

    async def search_resources_async(
        self,
        request: rmc20211104_models.SearchResourcesRequest,
    ) -> rmc20211104_models.SearchResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_resources_with_options_async(request, runtime)
