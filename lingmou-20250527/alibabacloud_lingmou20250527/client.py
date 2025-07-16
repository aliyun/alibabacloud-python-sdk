# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_lingmou20250527 import models as ling_mou_20250527_models
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
        self._endpoint = self.get_endpoint('lingmou', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_chat_session_with_options(
        self,
        id: str,
        request: ling_mou_20250527_models.CreateChatSessionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.CreateChatSessionResponse:
        """
        @summary 创建数字人会话
        
        @param request: CreateChatSessionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateChatSessionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.license):
            query['license'] = request.license
        if not UtilClient.is_unset(request.platform):
            query['platform'] = request.platform
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChatSession',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/chat/init/{OpenApiUtilClient.get_encode_param(id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.CreateChatSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chat_session_with_options_async(
        self,
        id: str,
        request: ling_mou_20250527_models.CreateChatSessionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.CreateChatSessionResponse:
        """
        @summary 创建数字人会话
        
        @param request: CreateChatSessionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateChatSessionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.license):
            query['license'] = request.license
        if not UtilClient.is_unset(request.platform):
            query['platform'] = request.platform
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChatSession',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/chat/init/{OpenApiUtilClient.get_encode_param(id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.CreateChatSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chat_session(
        self,
        id: str,
        request: ling_mou_20250527_models.CreateChatSessionRequest,
    ) -> ling_mou_20250527_models.CreateChatSessionResponse:
        """
        @summary 创建数字人会话
        
        @param request: CreateChatSessionRequest
        @return: CreateChatSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_chat_session_with_options(id, request, headers, runtime)

    async def create_chat_session_async(
        self,
        id: str,
        request: ling_mou_20250527_models.CreateChatSessionRequest,
    ) -> ling_mou_20250527_models.CreateChatSessionResponse:
        """
        @summary 创建数字人会话
        
        @param request: CreateChatSessionRequest
        @return: CreateChatSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_chat_session_with_options_async(id, request, headers, runtime)
