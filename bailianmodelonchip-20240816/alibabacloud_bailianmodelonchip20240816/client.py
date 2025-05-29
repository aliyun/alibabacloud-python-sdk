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

    def create_channel_sign_with_options(
        self,
        request: bailian_model_on_chip_20240816_models.CreateChannelSignRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.CreateChannelSignResponse:
        """
        @summary 创建渠道签约申请
        
        @param request: CreateChannelSignRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateChannelSignResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_name):
            body['channelName'] = request.channel_name
        if not UtilClient.is_unset(request.contact):
            body['contact'] = request.contact
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateChannelSign',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/channel/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.CreateChannelSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_channel_sign_with_options_async(
        self,
        request: bailian_model_on_chip_20240816_models.CreateChannelSignRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.CreateChannelSignResponse:
        """
        @summary 创建渠道签约申请
        
        @param request: CreateChannelSignRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateChannelSignResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_name):
            body['channelName'] = request.channel_name
        if not UtilClient.is_unset(request.contact):
            body['contact'] = request.contact
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateChannelSign',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/channel/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.CreateChannelSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_channel_sign(
        self,
        request: bailian_model_on_chip_20240816_models.CreateChannelSignRequest,
    ) -> bailian_model_on_chip_20240816_models.CreateChannelSignResponse:
        """
        @summary 创建渠道签约申请
        
        @param request: CreateChannelSignRequest
        @return: CreateChannelSignResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_channel_sign_with_options(request, headers, runtime)

    async def create_channel_sign_async(
        self,
        request: bailian_model_on_chip_20240816_models.CreateChannelSignRequest,
    ) -> bailian_model_on_chip_20240816_models.CreateChannelSignResponse:
        """
        @summary 创建渠道签约申请
        
        @param request: CreateChannelSignRequest
        @return: CreateChannelSignResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_channel_sign_with_options_async(request, headers, runtime)

    def create_product_with_options(
        self,
        request: bailian_model_on_chip_20240816_models.CreateProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.CreateProductResponse:
        """
        @summary 创建产品
        
        @param request: CreateProductRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProductResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.euid):
            body['euid'] = request.euid
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProduct',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/product/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.CreateProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_product_with_options_async(
        self,
        request: bailian_model_on_chip_20240816_models.CreateProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.CreateProductResponse:
        """
        @summary 创建产品
        
        @param request: CreateProductRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProductResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.euid):
            body['euid'] = request.euid
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProduct',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/product/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.CreateProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_product(
        self,
        request: bailian_model_on_chip_20240816_models.CreateProductRequest,
    ) -> bailian_model_on_chip_20240816_models.CreateProductResponse:
        """
        @summary 创建产品
        
        @param request: CreateProductRequest
        @return: CreateProductResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_product_with_options(request, headers, runtime)

    async def create_product_async(
        self,
        request: bailian_model_on_chip_20240816_models.CreateProductRequest,
    ) -> bailian_model_on_chip_20240816_models.CreateProductResponse:
        """
        @summary 创建产品
        
        @param request: CreateProductRequest
        @return: CreateProductResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_product_with_options_async(request, headers, runtime)

    def delete_product_with_options(
        self,
        request: bailian_model_on_chip_20240816_models.DeleteProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.DeleteProductResponse:
        """
        @summary 删除产品
        
        @param request: DeleteProductRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProductResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProduct',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/product/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.DeleteProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_product_with_options_async(
        self,
        request: bailian_model_on_chip_20240816_models.DeleteProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.DeleteProductResponse:
        """
        @summary 删除产品
        
        @param request: DeleteProductRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProductResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProduct',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/product/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.DeleteProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_product(
        self,
        request: bailian_model_on_chip_20240816_models.DeleteProductRequest,
    ) -> bailian_model_on_chip_20240816_models.DeleteProductResponse:
        """
        @summary 删除产品
        
        @param request: DeleteProductRequest
        @return: DeleteProductResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_product_with_options(request, headers, runtime)

    async def delete_product_async(
        self,
        request: bailian_model_on_chip_20240816_models.DeleteProductRequest,
    ) -> bailian_model_on_chip_20240816_models.DeleteProductResponse:
        """
        @summary 删除产品
        
        @param request: DeleteProductRequest
        @return: DeleteProductResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_product_with_options_async(request, headers, runtime)

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
        query = {}
        if not UtilClient.is_unset(request.product_key):
            query['productKey'] = request.product_key
        if not UtilClient.is_unset(request.request_time):
            query['requestTime'] = request.request_time
        if not UtilClient.is_unset(request.signature):
            query['signature'] = request.signature
        body = {}
        if not UtilClient.is_unset(request.nonce):
            body['nonce'] = request.nonce
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
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
        query = {}
        if not UtilClient.is_unset(request.product_key):
            query['productKey'] = request.product_key
        if not UtilClient.is_unset(request.request_time):
            query['requestTime'] = request.request_time
        if not UtilClient.is_unset(request.signature):
            query['signature'] = request.signature
        body = {}
        if not UtilClient.is_unset(request.nonce):
            body['nonce'] = request.nonce
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
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

    def get_channel_sign_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.GetChannelSignResponse:
        """
        @summary 查询渠道签约申请
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChannelSignResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetChannelSign',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/channel/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.GetChannelSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_channel_sign_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.GetChannelSignResponse:
        """
        @summary 查询渠道签约申请
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChannelSignResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetChannelSign',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/channel/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.GetChannelSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_channel_sign(self) -> bailian_model_on_chip_20240816_models.GetChannelSignResponse:
        """
        @summary 查询渠道签约申请
        
        @return: GetChannelSignResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_channel_sign_with_options(headers, runtime)

    async def get_channel_sign_async(self) -> bailian_model_on_chip_20240816_models.GetChannelSignResponse:
        """
        @summary 查询渠道签约申请
        
        @return: GetChannelSignResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_channel_sign_with_options_async(headers, runtime)

    def get_quota_info_with_options(
        self,
        request: bailian_model_on_chip_20240816_models.GetQuotaInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.GetQuotaInfoResponse:
        """
        @summary 获取额度信息
        
        @param request: GetQuotaInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQuotaInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.record_id):
            body['recordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQuotaInfo',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/quota/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.GetQuotaInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_info_with_options_async(
        self,
        request: bailian_model_on_chip_20240816_models.GetQuotaInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.GetQuotaInfoResponse:
        """
        @summary 获取额度信息
        
        @param request: GetQuotaInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQuotaInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.record_id):
            body['recordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQuotaInfo',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/quota/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.GetQuotaInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota_info(
        self,
        request: bailian_model_on_chip_20240816_models.GetQuotaInfoRequest,
    ) -> bailian_model_on_chip_20240816_models.GetQuotaInfoResponse:
        """
        @summary 获取额度信息
        
        @param request: GetQuotaInfoRequest
        @return: GetQuotaInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_quota_info_with_options(request, headers, runtime)

    async def get_quota_info_async(
        self,
        request: bailian_model_on_chip_20240816_models.GetQuotaInfoRequest,
    ) -> bailian_model_on_chip_20240816_models.GetQuotaInfoResponse:
        """
        @summary 获取额度信息
        
        @param request: GetQuotaInfoRequest
        @return: GetQuotaInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_quota_info_with_options_async(request, headers, runtime)

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
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.nonce):
            body['nonce'] = request.nonce
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
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
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.nonce):
            body['nonce'] = request.nonce
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
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

    def half_llmapp_call_with_options(
        self,
        tmp_req: bailian_model_on_chip_20240816_models.HalfLLMAppCallRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.HalfLLMAppCallResponse:
        """
        @summary 半托管大模型应用请求
        
        @param tmp_req: HalfLLMAppCallRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: HalfLLMAppCallResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bailian_model_on_chip_20240816_models.HalfLLMAppCallShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_param):
            request.biz_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_param, 'bizParam', 'json')
        if not UtilClient.is_unset(tmp_req.model_type_list):
            request.model_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.model_type_list, 'modelTypeList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.biz_param_shrink):
            body['bizParam'] = request.biz_param_shrink
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.model_type_list_shrink):
            body['modelTypeList'] = request.model_type_list_shrink
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.text):
            body['text'] = request.text
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HalfLLMAppCall',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/device/v1/half/llm/app/call',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.HalfLLMAppCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def half_llmapp_call_with_options_async(
        self,
        tmp_req: bailian_model_on_chip_20240816_models.HalfLLMAppCallRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.HalfLLMAppCallResponse:
        """
        @summary 半托管大模型应用请求
        
        @param tmp_req: HalfLLMAppCallRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: HalfLLMAppCallResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bailian_model_on_chip_20240816_models.HalfLLMAppCallShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_param):
            request.biz_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_param, 'bizParam', 'json')
        if not UtilClient.is_unset(tmp_req.model_type_list):
            request.model_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.model_type_list, 'modelTypeList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.biz_param_shrink):
            body['bizParam'] = request.biz_param_shrink
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.model_type_list_shrink):
            body['modelTypeList'] = request.model_type_list_shrink
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.text):
            body['text'] = request.text
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HalfLLMAppCall',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/device/v1/half/llm/app/call',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.HalfLLMAppCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def half_llmapp_call(
        self,
        request: bailian_model_on_chip_20240816_models.HalfLLMAppCallRequest,
    ) -> bailian_model_on_chip_20240816_models.HalfLLMAppCallResponse:
        """
        @summary 半托管大模型应用请求
        
        @param request: HalfLLMAppCallRequest
        @return: HalfLLMAppCallResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.half_llmapp_call_with_options(request, headers, runtime)

    async def half_llmapp_call_async(
        self,
        request: bailian_model_on_chip_20240816_models.HalfLLMAppCallRequest,
    ) -> bailian_model_on_chip_20240816_models.HalfLLMAppCallResponse:
        """
        @summary 半托管大模型应用请求
        
        @param request: HalfLLMAppCallRequest
        @return: HalfLLMAppCallResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.half_llmapp_call_with_options_async(request, headers, runtime)

    def half_llmchat_with_options(
        self,
        request: bailian_model_on_chip_20240816_models.HalfLLMChatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.HalfLLMChatResponse:
        """
        @summary 半托管大模型流式文本对话
        
        @param request: HalfLLMChatRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: HalfLLMChatResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.enable_search):
            body['enableSearch'] = request.enable_search
        if not UtilClient.is_unset(request.input_text):
            body['inputText'] = request.input_text
        if not UtilClient.is_unset(request.model):
            body['model'] = request.model
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.stream):
            body['stream'] = request.stream
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HalfLLMChat',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/device/v1/half/llm/chat',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.HalfLLMChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def half_llmchat_with_options_async(
        self,
        request: bailian_model_on_chip_20240816_models.HalfLLMChatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.HalfLLMChatResponse:
        """
        @summary 半托管大模型流式文本对话
        
        @param request: HalfLLMChatRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: HalfLLMChatResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.enable_search):
            body['enableSearch'] = request.enable_search
        if not UtilClient.is_unset(request.input_text):
            body['inputText'] = request.input_text
        if not UtilClient.is_unset(request.model):
            body['model'] = request.model
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.stream):
            body['stream'] = request.stream
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HalfLLMChat',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/device/v1/half/llm/chat',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.HalfLLMChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def half_llmchat(
        self,
        request: bailian_model_on_chip_20240816_models.HalfLLMChatRequest,
    ) -> bailian_model_on_chip_20240816_models.HalfLLMChatResponse:
        """
        @summary 半托管大模型流式文本对话
        
        @param request: HalfLLMChatRequest
        @return: HalfLLMChatResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.half_llmchat_with_options(request, headers, runtime)

    async def half_llmchat_async(
        self,
        request: bailian_model_on_chip_20240816_models.HalfLLMChatRequest,
    ) -> bailian_model_on_chip_20240816_models.HalfLLMChatResponse:
        """
        @summary 半托管大模型流式文本对话
        
        @param request: HalfLLMChatRequest
        @return: HalfLLMChatResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.half_llmchat_with_options_async(request, headers, runtime)

    def half_llmimage_chat_with_options(
        self,
        request: bailian_model_on_chip_20240816_models.HalfLLMImageChatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.HalfLLMImageChatResponse:
        """
        @summary 半托管大模型文本合成语音
        
        @param request: HalfLLMImageChatRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: HalfLLMImageChatResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.enable_search):
            body['enableSearch'] = request.enable_search
        if not UtilClient.is_unset(request.image_url):
            body['imageUrl'] = request.image_url
        if not UtilClient.is_unset(request.input_text):
            body['inputText'] = request.input_text
        if not UtilClient.is_unset(request.model):
            body['model'] = request.model
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HalfLLMImageChat',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/device/v1/half/llm/image/chat',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.HalfLLMImageChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def half_llmimage_chat_with_options_async(
        self,
        request: bailian_model_on_chip_20240816_models.HalfLLMImageChatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.HalfLLMImageChatResponse:
        """
        @summary 半托管大模型文本合成语音
        
        @param request: HalfLLMImageChatRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: HalfLLMImageChatResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.enable_search):
            body['enableSearch'] = request.enable_search
        if not UtilClient.is_unset(request.image_url):
            body['imageUrl'] = request.image_url
        if not UtilClient.is_unset(request.input_text):
            body['inputText'] = request.input_text
        if not UtilClient.is_unset(request.model):
            body['model'] = request.model
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HalfLLMImageChat',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/device/v1/half/llm/image/chat',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.HalfLLMImageChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def half_llmimage_chat(
        self,
        request: bailian_model_on_chip_20240816_models.HalfLLMImageChatRequest,
    ) -> bailian_model_on_chip_20240816_models.HalfLLMImageChatResponse:
        """
        @summary 半托管大模型文本合成语音
        
        @param request: HalfLLMImageChatRequest
        @return: HalfLLMImageChatResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.half_llmimage_chat_with_options(request, headers, runtime)

    async def half_llmimage_chat_async(
        self,
        request: bailian_model_on_chip_20240816_models.HalfLLMImageChatRequest,
    ) -> bailian_model_on_chip_20240816_models.HalfLLMImageChatResponse:
        """
        @summary 半托管大模型文本合成语音
        
        @param request: HalfLLMImageChatRequest
        @return: HalfLLMImageChatResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.half_llmimage_chat_with_options_async(request, headers, runtime)

    def half_llmimage_ocr_with_options(
        self,
        request: bailian_model_on_chip_20240816_models.HalfLLMImageOcrRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.HalfLLMImageOcrResponse:
        """
        @summary 半托管大模型图片识别
        
        @param request: HalfLLMImageOcrRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: HalfLLMImageOcrResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.image_url):
            body['imageUrl'] = request.image_url
        if not UtilClient.is_unset(request.model):
            body['model'] = request.model
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HalfLLMImageOcr',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/device/v1/half/llm/image/ocr',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.HalfLLMImageOcrResponse(),
            self.call_api(params, req, runtime)
        )

    async def half_llmimage_ocr_with_options_async(
        self,
        request: bailian_model_on_chip_20240816_models.HalfLLMImageOcrRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.HalfLLMImageOcrResponse:
        """
        @summary 半托管大模型图片识别
        
        @param request: HalfLLMImageOcrRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: HalfLLMImageOcrResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.image_url):
            body['imageUrl'] = request.image_url
        if not UtilClient.is_unset(request.model):
            body['model'] = request.model
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HalfLLMImageOcr',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/device/v1/half/llm/image/ocr',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.HalfLLMImageOcrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def half_llmimage_ocr(
        self,
        request: bailian_model_on_chip_20240816_models.HalfLLMImageOcrRequest,
    ) -> bailian_model_on_chip_20240816_models.HalfLLMImageOcrResponse:
        """
        @summary 半托管大模型图片识别
        
        @param request: HalfLLMImageOcrRequest
        @return: HalfLLMImageOcrResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.half_llmimage_ocr_with_options(request, headers, runtime)

    async def half_llmimage_ocr_async(
        self,
        request: bailian_model_on_chip_20240816_models.HalfLLMImageOcrRequest,
    ) -> bailian_model_on_chip_20240816_models.HalfLLMImageOcrResponse:
        """
        @summary 半托管大模型图片识别
        
        @param request: HalfLLMImageOcrRequest
        @return: HalfLLMImageOcrResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.half_llmimage_ocr_with_options_async(request, headers, runtime)

    def half_llmttschat_with_options(
        self,
        request: bailian_model_on_chip_20240816_models.HalfLLMTTSChatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.HalfLLMTTSChatResponse:
        """
        @summary 半托管大模型文本合成语音
        
        @param request: HalfLLMTTSChatRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: HalfLLMTTSChatResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.enable_search):
            body['enableSearch'] = request.enable_search
        if not UtilClient.is_unset(request.format):
            body['format'] = request.format
        if not UtilClient.is_unset(request.model):
            body['model'] = request.model
        if not UtilClient.is_unset(request.pitch_rate):
            body['pitchRate'] = request.pitch_rate
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        if not UtilClient.is_unset(request.sample_rate):
            body['sampleRate'] = request.sample_rate
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.speech_rate):
            body['speechRate'] = request.speech_rate
        if not UtilClient.is_unset(request.stream):
            body['stream'] = request.stream
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.text):
            body['text'] = request.text
        if not UtilClient.is_unset(request.url):
            body['url'] = request.url
        if not UtilClient.is_unset(request.voice):
            body['voice'] = request.voice
        if not UtilClient.is_unset(request.volume):
            body['volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HalfLLMTTSChat',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/device/v1/half/llm/tts/chat',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.HalfLLMTTSChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def half_llmttschat_with_options_async(
        self,
        request: bailian_model_on_chip_20240816_models.HalfLLMTTSChatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.HalfLLMTTSChatResponse:
        """
        @summary 半托管大模型文本合成语音
        
        @param request: HalfLLMTTSChatRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: HalfLLMTTSChatResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.enable_search):
            body['enableSearch'] = request.enable_search
        if not UtilClient.is_unset(request.format):
            body['format'] = request.format
        if not UtilClient.is_unset(request.model):
            body['model'] = request.model
        if not UtilClient.is_unset(request.pitch_rate):
            body['pitchRate'] = request.pitch_rate
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        if not UtilClient.is_unset(request.sample_rate):
            body['sampleRate'] = request.sample_rate
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.speech_rate):
            body['speechRate'] = request.speech_rate
        if not UtilClient.is_unset(request.stream):
            body['stream'] = request.stream
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.text):
            body['text'] = request.text
        if not UtilClient.is_unset(request.url):
            body['url'] = request.url
        if not UtilClient.is_unset(request.voice):
            body['voice'] = request.voice
        if not UtilClient.is_unset(request.volume):
            body['volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HalfLLMTTSChat',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/device/v1/half/llm/tts/chat',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.HalfLLMTTSChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def half_llmttschat(
        self,
        request: bailian_model_on_chip_20240816_models.HalfLLMTTSChatRequest,
    ) -> bailian_model_on_chip_20240816_models.HalfLLMTTSChatResponse:
        """
        @summary 半托管大模型文本合成语音
        
        @param request: HalfLLMTTSChatRequest
        @return: HalfLLMTTSChatResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.half_llmttschat_with_options(request, headers, runtime)

    async def half_llmttschat_async(
        self,
        request: bailian_model_on_chip_20240816_models.HalfLLMTTSChatRequest,
    ) -> bailian_model_on_chip_20240816_models.HalfLLMTTSChatResponse:
        """
        @summary 半托管大模型文本合成语音
        
        @param request: HalfLLMTTSChatRequest
        @return: HalfLLMTTSChatResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.half_llmttschat_with_options_async(request, headers, runtime)

    def query_device_page_with_options(
        self,
        request: bailian_model_on_chip_20240816_models.QueryDevicePageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.QueryDevicePageResponse:
        """
        @summary 设备列表分页查询
        
        @param request: QueryDevicePageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDevicePageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.disable_status):
            body['disableStatus'] = request.disable_status
        if not UtilClient.is_unset(request.page_index):
            body['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDevicePage',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/device/v1/page',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.QueryDevicePageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_page_with_options_async(
        self,
        request: bailian_model_on_chip_20240816_models.QueryDevicePageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.QueryDevicePageResponse:
        """
        @summary 设备列表分页查询
        
        @param request: QueryDevicePageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDevicePageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.disable_status):
            body['disableStatus'] = request.disable_status
        if not UtilClient.is_unset(request.page_index):
            body['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDevicePage',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/device/v1/page',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.QueryDevicePageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_device_page(
        self,
        request: bailian_model_on_chip_20240816_models.QueryDevicePageRequest,
    ) -> bailian_model_on_chip_20240816_models.QueryDevicePageResponse:
        """
        @summary 设备列表分页查询
        
        @param request: QueryDevicePageRequest
        @return: QueryDevicePageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_device_page_with_options(request, headers, runtime)

    async def query_device_page_async(
        self,
        request: bailian_model_on_chip_20240816_models.QueryDevicePageRequest,
    ) -> bailian_model_on_chip_20240816_models.QueryDevicePageResponse:
        """
        @summary 设备列表分页查询
        
        @param request: QueryDevicePageRequest
        @return: QueryDevicePageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_device_page_with_options_async(request, headers, runtime)

    def query_product_page_with_options(
        self,
        request: bailian_model_on_chip_20240816_models.QueryProductPageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.QueryProductPageResponse:
        """
        @summary 分页查询产品
        
        @param request: QueryProductPageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryProductPageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_type):
            body['modelType'] = request.model_type
        if not UtilClient.is_unset(request.page_index):
            body['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryProductPage',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/product/page',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.QueryProductPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_product_page_with_options_async(
        self,
        request: bailian_model_on_chip_20240816_models.QueryProductPageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.QueryProductPageResponse:
        """
        @summary 分页查询产品
        
        @param request: QueryProductPageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryProductPageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_type):
            body['modelType'] = request.model_type
        if not UtilClient.is_unset(request.page_index):
            body['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryProductPage',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/product/page',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.QueryProductPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_product_page(
        self,
        request: bailian_model_on_chip_20240816_models.QueryProductPageRequest,
    ) -> bailian_model_on_chip_20240816_models.QueryProductPageResponse:
        """
        @summary 分页查询产品
        
        @param request: QueryProductPageRequest
        @return: QueryProductPageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_product_page_with_options(request, headers, runtime)

    async def query_product_page_async(
        self,
        request: bailian_model_on_chip_20240816_models.QueryProductPageRequest,
    ) -> bailian_model_on_chip_20240816_models.QueryProductPageResponse:
        """
        @summary 分页查询产品
        
        @param request: QueryProductPageRequest
        @return: QueryProductPageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_product_page_with_options_async(request, headers, runtime)

    def query_product_quota_page_with_options(
        self,
        request: bailian_model_on_chip_20240816_models.QueryProductQuotaPageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.QueryProductQuotaPageResponse:
        """
        @summary 分页查询产品额度
        
        @param request: QueryProductQuotaPageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryProductQuotaPageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_index):
            body['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.purchase_time_end):
            body['purchaseTimeEnd'] = request.purchase_time_end
        if not UtilClient.is_unset(request.purchase_time_start):
            body['purchaseTimeStart'] = request.purchase_time_start
        if not UtilClient.is_unset(request.purchase_type):
            body['purchaseType'] = request.purchase_type
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryProductQuotaPage',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/product/quotaPage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.QueryProductQuotaPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_product_quota_page_with_options_async(
        self,
        request: bailian_model_on_chip_20240816_models.QueryProductQuotaPageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.QueryProductQuotaPageResponse:
        """
        @summary 分页查询产品额度
        
        @param request: QueryProductQuotaPageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryProductQuotaPageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_index):
            body['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.purchase_time_end):
            body['purchaseTimeEnd'] = request.purchase_time_end
        if not UtilClient.is_unset(request.purchase_time_start):
            body['purchaseTimeStart'] = request.purchase_time_start
        if not UtilClient.is_unset(request.purchase_type):
            body['purchaseType'] = request.purchase_type
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryProductQuotaPage',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/product/quotaPage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.QueryProductQuotaPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_product_quota_page(
        self,
        request: bailian_model_on_chip_20240816_models.QueryProductQuotaPageRequest,
    ) -> bailian_model_on_chip_20240816_models.QueryProductQuotaPageResponse:
        """
        @summary 分页查询产品额度
        
        @param request: QueryProductQuotaPageRequest
        @return: QueryProductQuotaPageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_product_quota_page_with_options(request, headers, runtime)

    async def query_product_quota_page_async(
        self,
        request: bailian_model_on_chip_20240816_models.QueryProductQuotaPageRequest,
    ) -> bailian_model_on_chip_20240816_models.QueryProductQuotaPageResponse:
        """
        @summary 分页查询产品额度
        
        @param request: QueryProductQuotaPageRequest
        @return: QueryProductQuotaPageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_product_quota_page_with_options_async(request, headers, runtime)

    def query_token_usage_with_options(
        self,
        request: bailian_model_on_chip_20240816_models.QueryTokenUsageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.QueryTokenUsageResponse:
        """
        @summary 查询token使用量
        
        @param request: QueryTokenUsageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTokenUsageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_date):
            body['endDate'] = request.end_date
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.start_date):
            body['startDate'] = request.start_date
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryTokenUsage',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/token/usage/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.QueryTokenUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_token_usage_with_options_async(
        self,
        request: bailian_model_on_chip_20240816_models.QueryTokenUsageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.QueryTokenUsageResponse:
        """
        @summary 查询token使用量
        
        @param request: QueryTokenUsageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTokenUsageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_date):
            body['endDate'] = request.end_date
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.start_date):
            body['startDate'] = request.start_date
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryTokenUsage',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/token/usage/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.QueryTokenUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_token_usage(
        self,
        request: bailian_model_on_chip_20240816_models.QueryTokenUsageRequest,
    ) -> bailian_model_on_chip_20240816_models.QueryTokenUsageResponse:
        """
        @summary 查询token使用量
        
        @param request: QueryTokenUsageRequest
        @return: QueryTokenUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_token_usage_with_options(request, headers, runtime)

    async def query_token_usage_async(
        self,
        request: bailian_model_on_chip_20240816_models.QueryTokenUsageRequest,
    ) -> bailian_model_on_chip_20240816_models.QueryTokenUsageResponse:
        """
        @summary 查询token使用量
        
        @param request: QueryTokenUsageRequest
        @return: QueryTokenUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_token_usage_with_options_async(request, headers, runtime)

    def revoke_channel_sign_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.RevokeChannelSignResponse:
        """
        @summary 撤销渠道签约申请
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeChannelSignResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RevokeChannelSign',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/channel/revoke',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.RevokeChannelSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_channel_sign_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.RevokeChannelSignResponse:
        """
        @summary 撤销渠道签约申请
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeChannelSignResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RevokeChannelSign',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/channel/revoke',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.RevokeChannelSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_channel_sign(self) -> bailian_model_on_chip_20240816_models.RevokeChannelSignResponse:
        """
        @summary 撤销渠道签约申请
        
        @return: RevokeChannelSignResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.revoke_channel_sign_with_options(headers, runtime)

    async def revoke_channel_sign_async(self) -> bailian_model_on_chip_20240816_models.RevokeChannelSignResponse:
        """
        @summary 撤销渠道签约申请
        
        @return: RevokeChannelSignResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.revoke_channel_sign_with_options_async(headers, runtime)

    def update_device_status_with_options(
        self,
        request: bailian_model_on_chip_20240816_models.UpdateDeviceStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.UpdateDeviceStatusResponse:
        """
        @summary 修改设备状态
        
        @param request: UpdateDeviceStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDeviceStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDeviceStatus',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/device/v1/update/status',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.UpdateDeviceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_device_status_with_options_async(
        self,
        request: bailian_model_on_chip_20240816_models.UpdateDeviceStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.UpdateDeviceStatusResponse:
        """
        @summary 修改设备状态
        
        @param request: UpdateDeviceStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDeviceStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDeviceStatus',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/device/v1/update/status',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.UpdateDeviceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_device_status(
        self,
        request: bailian_model_on_chip_20240816_models.UpdateDeviceStatusRequest,
    ) -> bailian_model_on_chip_20240816_models.UpdateDeviceStatusResponse:
        """
        @summary 修改设备状态
        
        @param request: UpdateDeviceStatusRequest
        @return: UpdateDeviceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_device_status_with_options(request, headers, runtime)

    async def update_device_status_async(
        self,
        request: bailian_model_on_chip_20240816_models.UpdateDeviceStatusRequest,
    ) -> bailian_model_on_chip_20240816_models.UpdateDeviceStatusResponse:
        """
        @summary 修改设备状态
        
        @param request: UpdateDeviceStatusRequest
        @return: UpdateDeviceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_device_status_with_options_async(request, headers, runtime)

    def update_image_quota_with_options(
        self,
        request: bailian_model_on_chip_20240816_models.UpdateImageQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.UpdateImageQuotaResponse:
        """
        @summary 修改图片模型额度
        
        @param request: UpdateImageQuotaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateImageQuotaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.duration):
            body['duration'] = request.duration
        if not UtilClient.is_unset(request.duration_type):
            body['durationType'] = request.duration_type
        if not UtilClient.is_unset(request.image_count):
            body['imageCount'] = request.image_count
        if not UtilClient.is_unset(request.license_count):
            body['licenseCount'] = request.license_count
        if not UtilClient.is_unset(request.package_type):
            body['packageType'] = request.package_type
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.purchase_type):
            body['purchaseType'] = request.purchase_type
        if not UtilClient.is_unset(request.record_id):
            body['recordId'] = request.record_id
        if not UtilClient.is_unset(request.settlement_amount):
            body['settlementAmount'] = request.settlement_amount
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.unit_price):
            body['unitPrice'] = request.unit_price
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateImageQuota',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/quota/update/image',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.UpdateImageQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_image_quota_with_options_async(
        self,
        request: bailian_model_on_chip_20240816_models.UpdateImageQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.UpdateImageQuotaResponse:
        """
        @summary 修改图片模型额度
        
        @param request: UpdateImageQuotaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateImageQuotaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.duration):
            body['duration'] = request.duration
        if not UtilClient.is_unset(request.duration_type):
            body['durationType'] = request.duration_type
        if not UtilClient.is_unset(request.image_count):
            body['imageCount'] = request.image_count
        if not UtilClient.is_unset(request.license_count):
            body['licenseCount'] = request.license_count
        if not UtilClient.is_unset(request.package_type):
            body['packageType'] = request.package_type
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.purchase_type):
            body['purchaseType'] = request.purchase_type
        if not UtilClient.is_unset(request.record_id):
            body['recordId'] = request.record_id
        if not UtilClient.is_unset(request.settlement_amount):
            body['settlementAmount'] = request.settlement_amount
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.unit_price):
            body['unitPrice'] = request.unit_price
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateImageQuota',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/quota/update/image',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.UpdateImageQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_image_quota(
        self,
        request: bailian_model_on_chip_20240816_models.UpdateImageQuotaRequest,
    ) -> bailian_model_on_chip_20240816_models.UpdateImageQuotaResponse:
        """
        @summary 修改图片模型额度
        
        @param request: UpdateImageQuotaRequest
        @return: UpdateImageQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_image_quota_with_options(request, headers, runtime)

    async def update_image_quota_async(
        self,
        request: bailian_model_on_chip_20240816_models.UpdateImageQuotaRequest,
    ) -> bailian_model_on_chip_20240816_models.UpdateImageQuotaResponse:
        """
        @summary 修改图片模型额度
        
        @param request: UpdateImageQuotaRequest
        @return: UpdateImageQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_image_quota_with_options_async(request, headers, runtime)

    def update_quota_with_options(
        self,
        request: bailian_model_on_chip_20240816_models.UpdateQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.UpdateQuotaResponse:
        """
        @summary 修改额度
        
        @param request: UpdateQuotaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateQuotaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.duration):
            body['duration'] = request.duration
        if not UtilClient.is_unset(request.duration_type):
            body['durationType'] = request.duration_type
        if not UtilClient.is_unset(request.license_count):
            body['licenseCount'] = request.license_count
        if not UtilClient.is_unset(request.max_qps):
            body['maxQps'] = request.max_qps
        if not UtilClient.is_unset(request.package_type):
            body['packageType'] = request.package_type
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.purchase_type):
            body['purchaseType'] = request.purchase_type
        if not UtilClient.is_unset(request.record_id):
            body['recordId'] = request.record_id
        if not UtilClient.is_unset(request.settlement_amount):
            body['settlementAmount'] = request.settlement_amount
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.token_number):
            body['tokenNumber'] = request.token_number
        if not UtilClient.is_unset(request.unit_price):
            body['unitPrice'] = request.unit_price
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateQuota',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/quota/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.UpdateQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_quota_with_options_async(
        self,
        request: bailian_model_on_chip_20240816_models.UpdateQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_model_on_chip_20240816_models.UpdateQuotaResponse:
        """
        @summary 修改额度
        
        @param request: UpdateQuotaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateQuotaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.duration):
            body['duration'] = request.duration
        if not UtilClient.is_unset(request.duration_type):
            body['durationType'] = request.duration_type
        if not UtilClient.is_unset(request.license_count):
            body['licenseCount'] = request.license_count
        if not UtilClient.is_unset(request.max_qps):
            body['maxQps'] = request.max_qps
        if not UtilClient.is_unset(request.package_type):
            body['packageType'] = request.package_type
        if not UtilClient.is_unset(request.product_key):
            body['productKey'] = request.product_key
        if not UtilClient.is_unset(request.purchase_type):
            body['purchaseType'] = request.purchase_type
        if not UtilClient.is_unset(request.record_id):
            body['recordId'] = request.record_id
        if not UtilClient.is_unset(request.settlement_amount):
            body['settlementAmount'] = request.settlement_amount
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.token_number):
            body['tokenNumber'] = request.token_number
        if not UtilClient.is_unset(request.unit_price):
            body['unitPrice'] = request.unit_price
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateQuota',
            version='2024-08-16',
            protocol='HTTPS',
            pathname=f'/open/api/v1/quota/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_model_on_chip_20240816_models.UpdateQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_quota(
        self,
        request: bailian_model_on_chip_20240816_models.UpdateQuotaRequest,
    ) -> bailian_model_on_chip_20240816_models.UpdateQuotaResponse:
        """
        @summary 修改额度
        
        @param request: UpdateQuotaRequest
        @return: UpdateQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_quota_with_options(request, headers, runtime)

    async def update_quota_async(
        self,
        request: bailian_model_on_chip_20240816_models.UpdateQuotaRequest,
    ) -> bailian_model_on_chip_20240816_models.UpdateQuotaResponse:
        """
        @summary 修改额度
        
        @param request: UpdateQuotaRequest
        @return: UpdateQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_quota_with_options_async(request, headers, runtime)
