# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_appflow20230904 import models as appflow_20230904_models
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
        self._endpoint = self.get_endpoint('appflow', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def generate_user_session_token_with_options(
        self,
        request: appflow_20230904_models.GenerateUserSessionTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appflow_20230904_models.GenerateUserSessionTokenResponse:
        """
        @summary Generate Login Session Token
        
        @param request: GenerateUserSessionTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateUserSessionTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chatbot_id):
            query['ChatbotId'] = request.chatbot_id
        if not UtilClient.is_unset(request.expire_second):
            query['ExpireSecond'] = request.expire_second
        if not UtilClient.is_unset(request.extra_info):
            query['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.integrate_id):
            query['IntegrateId'] = request.integrate_id
        if not UtilClient.is_unset(request.user_avatar):
            query['UserAvatar'] = request.user_avatar
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateUserSessionToken',
            version='2023-09-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appflow_20230904_models.GenerateUserSessionTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_user_session_token_with_options_async(
        self,
        request: appflow_20230904_models.GenerateUserSessionTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appflow_20230904_models.GenerateUserSessionTokenResponse:
        """
        @summary Generate Login Session Token
        
        @param request: GenerateUserSessionTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateUserSessionTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chatbot_id):
            query['ChatbotId'] = request.chatbot_id
        if not UtilClient.is_unset(request.expire_second):
            query['ExpireSecond'] = request.expire_second
        if not UtilClient.is_unset(request.extra_info):
            query['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.integrate_id):
            query['IntegrateId'] = request.integrate_id
        if not UtilClient.is_unset(request.user_avatar):
            query['UserAvatar'] = request.user_avatar
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateUserSessionToken',
            version='2023-09-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appflow_20230904_models.GenerateUserSessionTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_user_session_token(
        self,
        request: appflow_20230904_models.GenerateUserSessionTokenRequest,
    ) -> appflow_20230904_models.GenerateUserSessionTokenResponse:
        """
        @summary Generate Login Session Token
        
        @param request: GenerateUserSessionTokenRequest
        @return: GenerateUserSessionTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_user_session_token_with_options(request, runtime)

    async def generate_user_session_token_async(
        self,
        request: appflow_20230904_models.GenerateUserSessionTokenRequest,
    ) -> appflow_20230904_models.GenerateUserSessionTokenResponse:
        """
        @summary Generate Login Session Token
        
        @param request: GenerateUserSessionTokenRequest
        @return: GenerateUserSessionTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_user_session_token_with_options_async(request, runtime)
