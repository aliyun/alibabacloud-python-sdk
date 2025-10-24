# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_bailianmodelonchip20240816 import models as bailian_model_on_chip_20240816_models
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
        self._endpoint = self.get_endpoint('bailianmodelonchip', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def active_interaction_create_with_options(
        self,
        request: bailian_model_on_chip_20240816_models.ActiveInteractionCreateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.ActiveInteractionCreateResponse:
        """
        @summary 主动交互消息传递
        
        @param request: ActiveInteractionCreateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActiveInteractionCreateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image):
            body['image'] = request.image
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ActiveInteractionCreate',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/active/interaction/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.ActiveInteractionCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def active_interaction_create_with_options_async(
        self,
        request: bailian_model_on_chip_20240816_models.ActiveInteractionCreateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.ActiveInteractionCreateResponse:
        """
        @summary 主动交互消息传递
        
        @param request: ActiveInteractionCreateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActiveInteractionCreateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image):
            body['image'] = request.image
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ActiveInteractionCreate',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/active/interaction/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.ActiveInteractionCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def active_interaction_create(
        self,
        request: bailian_model_on_chip_20240816_models.ActiveInteractionCreateRequest,
    ) -> bailian_model_on_chip_20240816_models.ActiveInteractionCreateResponse:
        """
        @summary 主动交互消息传递
        
        @param request: ActiveInteractionCreateRequest
        @return: ActiveInteractionCreateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.active_interaction_create_with_options(request, headers, runtime)

    async def active_interaction_create_async(
        self,
        request: bailian_model_on_chip_20240816_models.ActiveInteractionCreateRequest,
    ) -> bailian_model_on_chip_20240816_models.ActiveInteractionCreateResponse:
        """
        @summary 主动交互消息传递
        
        @param request: ActiveInteractionCreateRequest
        @return: ActiveInteractionCreateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.active_interaction_create_with_options_async(request, headers, runtime)

    def device_register_with_options(
        self,
        request: bailian_model_on_chip_20240816_models.DeviceRegisterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.DeviceRegisterResponse:
        """
        @summary 设备注册
        
        @param request: DeviceRegisterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeviceRegisterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.nonce):
            body['nonce'] = request.nonce
        if not UtilClient.is_unset(request.request_time):
            body['requestTime'] = request.request_time
        if not UtilClient.is_unset(request.signature):
            body['signature'] = request.signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeviceRegister',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/device/v1/register',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.DeviceRegisterResponse(),
            self.call_api(params, req, runtime)
        )

    async def device_register_with_options_async(
        self,
        request: bailian_model_on_chip_20240816_models.DeviceRegisterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.DeviceRegisterResponse:
        """
        @summary 设备注册
        
        @param request: DeviceRegisterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeviceRegisterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.nonce):
            body['nonce'] = request.nonce
        if not UtilClient.is_unset(request.request_time):
            body['requestTime'] = request.request_time
        if not UtilClient.is_unset(request.signature):
            body['signature'] = request.signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeviceRegister',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/device/v1/register',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.DeviceRegisterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def device_register(
        self,
        request: bailian_model_on_chip_20240816_models.DeviceRegisterRequest,
    ) -> bailian_model_on_chip_20240816_models.DeviceRegisterResponse:
        """
        @summary 设备注册
        
        @param request: DeviceRegisterRequest
        @return: DeviceRegisterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.device_register_with_options(request, headers, runtime)

    async def device_register_async(
        self,
        request: bailian_model_on_chip_20240816_models.DeviceRegisterRequest,
    ) -> bailian_model_on_chip_20240816_models.DeviceRegisterResponse:
        """
        @summary 设备注册
        
        @param request: DeviceRegisterRequest
        @return: DeviceRegisterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.device_register_with_options_async(request, headers, runtime)

    def get_token_with_options(
        self,
        request: bailian_model_on_chip_20240816_models.GetTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.GetTokenResponse:
        """
        @summary 获取网关校验Token
        
        @param request: GetTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.nonce):
            body['nonce'] = request.nonce
        if not UtilClient.is_unset(request.request_time):
            body['requestTime'] = request.request_time
        if not UtilClient.is_unset(request.signature):
            body['signature'] = request.signature
        if not UtilClient.is_unset(request.token_key):
            body['tokenKey'] = request.token_key
        if not UtilClient.is_unset(request.token_type):
            body['tokenType'] = request.token_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetToken',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/auth/v1/token/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.GetTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_token_with_options_async(
        self,
        request: bailian_model_on_chip_20240816_models.GetTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.GetTokenResponse:
        """
        @summary 获取网关校验Token
        
        @param request: GetTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.nonce):
            body['nonce'] = request.nonce
        if not UtilClient.is_unset(request.request_time):
            body['requestTime'] = request.request_time
        if not UtilClient.is_unset(request.signature):
            body['signature'] = request.signature
        if not UtilClient.is_unset(request.token_key):
            body['tokenKey'] = request.token_key
        if not UtilClient.is_unset(request.token_type):
            body['tokenType'] = request.token_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetToken',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/auth/v1/token/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.GetTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_token(
        self,
        request: bailian_model_on_chip_20240816_models.GetTokenRequest,
    ) -> bailian_model_on_chip_20240816_models.GetTokenResponse:
        """
        @summary 获取网关校验Token
        
        @param request: GetTokenRequest
        @return: GetTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_token_with_options(request, headers, runtime)

    async def get_token_async(
        self,
        request: bailian_model_on_chip_20240816_models.GetTokenRequest,
    ) -> bailian_model_on_chip_20240816_models.GetTokenResponse:
        """
        @summary 获取网关校验Token
        
        @param request: GetTokenRequest
        @return: GetTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_token_with_options_async(request, headers, runtime)
