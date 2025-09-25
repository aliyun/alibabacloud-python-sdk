# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_bailianchatbot20241105 import models as bailian_chat_bot_20241105_models
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
        self._endpoint = self.get_endpoint('bailianchatbot', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def sse_chat_with_options(
        self,
        request: bailian_chat_bot_20241105_models.SseChatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_chat_bot_20241105_models.SseChatResponse:
        """
        @summary SSE问答接口
        
        @param request: SseChatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SseChatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.sender_id):
            query['SenderId'] = request.sender_id
        if not UtilClient.is_unset(request.sender_nick):
            query['SenderNick'] = request.sender_nick
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.utterance):
            query['Utterance'] = request.utterance
        if not UtilClient.is_unset(request.vendor_param):
            query['VendorParam'] = request.vendor_param
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SseChat',
            version='2024-11-05',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_chat_bot_20241105_models.SseChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def sse_chat_with_options_async(
        self,
        request: bailian_chat_bot_20241105_models.SseChatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_chat_bot_20241105_models.SseChatResponse:
        """
        @summary SSE问答接口
        
        @param request: SseChatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SseChatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.sender_id):
            query['SenderId'] = request.sender_id
        if not UtilClient.is_unset(request.sender_nick):
            query['SenderNick'] = request.sender_nick
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.utterance):
            query['Utterance'] = request.utterance
        if not UtilClient.is_unset(request.vendor_param):
            query['VendorParam'] = request.vendor_param
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SseChat',
            version='2024-11-05',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_chat_bot_20241105_models.SseChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sse_chat(
        self,
        request: bailian_chat_bot_20241105_models.SseChatRequest,
    ) -> bailian_chat_bot_20241105_models.SseChatResponse:
        """
        @summary SSE问答接口
        
        @param request: SseChatRequest
        @return: SseChatResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.sse_chat_with_options(request, runtime)

    async def sse_chat_async(
        self,
        request: bailian_chat_bot_20241105_models.SseChatRequest,
    ) -> bailian_chat_bot_20241105_models.SseChatResponse:
        """
        @summary SSE问答接口
        
        @param request: SseChatRequest
        @return: SseChatResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.sse_chat_with_options_async(request, runtime)
