# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_btripopen20220520 import models as btrip_open_20220520_models
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
        self._signature_algorithm = 'v2'
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('btripopen', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def access_token(
        self,
        request: btrip_open_20220520_models.AccessTokenRequest,
    ) -> btrip_open_20220520_models.AccessTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.access_token_with_options(request, headers, runtime)

    async def access_token_async(
        self,
        request: btrip_open_20220520_models.AccessTokenRequest,
    ) -> btrip_open_20220520_models.AccessTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.access_token_with_options_async(request, headers, runtime)

    def access_token_with_options(
        self,
        request: btrip_open_20220520_models.AccessTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.AccessTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['app_key'] = request.app_key
        if not UtilClient.is_unset(request.app_secret):
            query['app_secret'] = request.app_secret
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AccessToken',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/btrip-open-auth/v1/access-token/action/take',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.AccessTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def access_token_with_options_async(
        self,
        request: btrip_open_20220520_models.AccessTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> btrip_open_20220520_models.AccessTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['app_key'] = request.app_key
        if not UtilClient.is_unset(request.app_secret):
            query['app_secret'] = request.app_secret
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AccessToken',
            version='2022-05-20',
            protocol='HTTPS',
            pathname=f'/btrip-open-auth/v1/access-token/action/take',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            btrip_open_20220520_models.AccessTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )
