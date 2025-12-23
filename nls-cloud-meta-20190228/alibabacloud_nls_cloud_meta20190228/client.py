# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_nls_cloud_meta20190228 import models as nls_cloud_meta_20190228_models


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
        self._endpoint = self.get_endpoint('nls-cloud-meta', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_token_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> nls_cloud_meta_20190228_models.CreateTokenResponse:
        """
        @summary 创建鉴权Token
        
        @param request: CreateTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTokenResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='CreateToken',
            version='2019-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nls_cloud_meta_20190228_models.CreateTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_token_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> nls_cloud_meta_20190228_models.CreateTokenResponse:
        """
        @summary 创建鉴权Token
        
        @param request: CreateTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTokenResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='CreateToken',
            version='2019-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nls_cloud_meta_20190228_models.CreateTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_token(self) -> nls_cloud_meta_20190228_models.CreateTokenResponse:
        """
        @summary 创建鉴权Token
        
        @return: CreateTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_token_with_options(runtime)

    async def create_token_async(self) -> nls_cloud_meta_20190228_models.CreateTokenResponse:
        """
        @summary 创建鉴权Token
        
        @return: CreateTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_token_with_options_async(runtime)
