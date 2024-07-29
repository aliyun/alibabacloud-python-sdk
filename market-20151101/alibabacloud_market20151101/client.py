# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_market20151101 import models as market_20151101_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-hangzhou': 'market.aliyuncs.com',
            'ap-northeast-1': 'market.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'market.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'market.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'market.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'market.ap-southeast-1.aliyuncs.com',
            'cn-beijing': 'market.aliyuncs.com',
            'cn-chengdu': 'market.aliyuncs.com',
            'cn-hongkong': 'market.aliyuncs.com',
            'cn-huhehaote': 'market.aliyuncs.com',
            'cn-qingdao': 'market.aliyuncs.com',
            'cn-shanghai': 'market.aliyuncs.com',
            'cn-shenzhen': 'market.aliyuncs.com',
            'cn-zhangjiakou': 'market.aliyuncs.com',
            'eu-central-1': 'market.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'market.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'market.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'market.ap-southeast-1.aliyuncs.com',
            'us-west-1': 'market.ap-southeast-1.aliyuncs.com',
            'cn-hangzhou-finance': 'market.aliyuncs.com',
            'cn-shenzhen-finance-1': 'market.aliyuncs.com',
            'cn-shanghai-finance-1': 'market.aliyuncs.com',
            'cn-north-2-gov-1': 'market.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('market', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def activate_license_with_options(
        self,
        request: market_20151101_models.ActivateLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.ActivateLicenseResponse:
        """
        @summary 增加STS支持
        
        @param request: ActivateLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActivateLicenseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identification):
            query['Identification'] = request.identification
        if not UtilClient.is_unset(request.license_code):
            query['LicenseCode'] = request.license_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateLicense',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.ActivateLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_license_with_options_async(
        self,
        request: market_20151101_models.ActivateLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.ActivateLicenseResponse:
        """
        @summary 增加STS支持
        
        @param request: ActivateLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActivateLicenseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identification):
            query['Identification'] = request.identification
        if not UtilClient.is_unset(request.license_code):
            query['LicenseCode'] = request.license_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateLicense',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.ActivateLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def activate_license(
        self,
        request: market_20151101_models.ActivateLicenseRequest,
    ) -> market_20151101_models.ActivateLicenseResponse:
        """
        @summary 增加STS支持
        
        @param request: ActivateLicenseRequest
        @return: ActivateLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.activate_license_with_options(request, runtime)

    async def activate_license_async(
        self,
        request: market_20151101_models.ActivateLicenseRequest,
    ) -> market_20151101_models.ActivateLicenseResponse:
        """
        @summary 增加STS支持
        
        @param request: ActivateLicenseRequest
        @return: ActivateLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.activate_license_with_options_async(request, runtime)

    def auto_renew_instance_with_options(
        self,
        request: market_20151101_models.AutoRenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.AutoRenewInstanceResponse:
        """
        @param request: AutoRenewInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AutoRenewInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_renew_cycle):
            body['AutoRenewCycle'] = request.auto_renew_cycle
        if not UtilClient.is_unset(request.auto_renew_duration):
            body['AutoRenewDuration'] = request.auto_renew_duration
        if not UtilClient.is_unset(request.order_biz_id):
            body['OrderBizId'] = request.order_biz_id
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AutoRenewInstance',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.AutoRenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def auto_renew_instance_with_options_async(
        self,
        request: market_20151101_models.AutoRenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.AutoRenewInstanceResponse:
        """
        @param request: AutoRenewInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AutoRenewInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_renew_cycle):
            body['AutoRenewCycle'] = request.auto_renew_cycle
        if not UtilClient.is_unset(request.auto_renew_duration):
            body['AutoRenewDuration'] = request.auto_renew_duration
        if not UtilClient.is_unset(request.order_biz_id):
            body['OrderBizId'] = request.order_biz_id
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AutoRenewInstance',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.AutoRenewInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def auto_renew_instance(
        self,
        request: market_20151101_models.AutoRenewInstanceRequest,
    ) -> market_20151101_models.AutoRenewInstanceResponse:
        """
        @param request: AutoRenewInstanceRequest
        @return: AutoRenewInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.auto_renew_instance_with_options(request, runtime)

    async def auto_renew_instance_async(
        self,
        request: market_20151101_models.AutoRenewInstanceRequest,
    ) -> market_20151101_models.AutoRenewInstanceResponse:
        """
        @param request: AutoRenewInstanceRequest
        @return: AutoRenewInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.auto_renew_instance_with_options_async(request, runtime)

    def create_order_with_options(
        self,
        request: market_20151101_models.CreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.CreateOrderResponse:
        """
        @param request: CreateOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity):
            query['Commodity'] = request.commodity
        if not UtilClient.is_unset(request.order_souce):
            query['OrderSouce'] = request.order_souce
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrder',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.CreateOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_order_with_options_async(
        self,
        request: market_20151101_models.CreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.CreateOrderResponse:
        """
        @param request: CreateOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity):
            query['Commodity'] = request.commodity
        if not UtilClient.is_unset(request.order_souce):
            query['OrderSouce'] = request.order_souce
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrder',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.CreateOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_order(
        self,
        request: market_20151101_models.CreateOrderRequest,
    ) -> market_20151101_models.CreateOrderResponse:
        """
        @param request: CreateOrderRequest
        @return: CreateOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_order_with_options(request, runtime)

    async def create_order_async(
        self,
        request: market_20151101_models.CreateOrderRequest,
    ) -> market_20151101_models.CreateOrderResponse:
        """
        @param request: CreateOrderRequest
        @return: CreateOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_order_with_options_async(request, runtime)

    def cross_account_verify_token_with_options(
        self,
        request: market_20151101_models.CrossAccountVerifyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.CrossAccountVerifyTokenResponse:
        """
        @param request: CrossAccountVerifyTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CrossAccountVerifyTokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CrossAccountVerifyToken',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.CrossAccountVerifyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def cross_account_verify_token_with_options_async(
        self,
        request: market_20151101_models.CrossAccountVerifyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.CrossAccountVerifyTokenResponse:
        """
        @param request: CrossAccountVerifyTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CrossAccountVerifyTokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CrossAccountVerifyToken',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.CrossAccountVerifyTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cross_account_verify_token(
        self,
        request: market_20151101_models.CrossAccountVerifyTokenRequest,
    ) -> market_20151101_models.CrossAccountVerifyTokenResponse:
        """
        @param request: CrossAccountVerifyTokenRequest
        @return: CrossAccountVerifyTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cross_account_verify_token_with_options(request, runtime)

    async def cross_account_verify_token_async(
        self,
        request: market_20151101_models.CrossAccountVerifyTokenRequest,
    ) -> market_20151101_models.CrossAccountVerifyTokenResponse:
        """
        @param request: CrossAccountVerifyTokenRequest
        @return: CrossAccountVerifyTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cross_account_verify_token_with_options_async(request, runtime)

    def describe_api_metering_with_options(
        self,
        request: market_20151101_models.DescribeApiMeteringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeApiMeteringResponse:
        """
        @summary 查询API用量
        
        @param request: DescribeApiMeteringRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApiMeteringResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiMetering',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeApiMeteringResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_metering_with_options_async(
        self,
        request: market_20151101_models.DescribeApiMeteringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeApiMeteringResponse:
        """
        @summary 查询API用量
        
        @param request: DescribeApiMeteringRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApiMeteringResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiMetering',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeApiMeteringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_metering(
        self,
        request: market_20151101_models.DescribeApiMeteringRequest,
    ) -> market_20151101_models.DescribeApiMeteringResponse:
        """
        @summary 查询API用量
        
        @param request: DescribeApiMeteringRequest
        @return: DescribeApiMeteringResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_api_metering_with_options(request, runtime)

    async def describe_api_metering_async(
        self,
        request: market_20151101_models.DescribeApiMeteringRequest,
    ) -> market_20151101_models.DescribeApiMeteringResponse:
        """
        @summary 查询API用量
        
        @param request: DescribeApiMeteringRequest
        @return: DescribeApiMeteringResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_metering_with_options_async(request, runtime)

    def describe_current_node_info_with_options(
        self,
        request: market_20151101_models.DescribeCurrentNodeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeCurrentNodeInfoResponse:
        """
        @param request: DescribeCurrentNodeInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCurrentNodeInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCurrentNodeInfo',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeCurrentNodeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_current_node_info_with_options_async(
        self,
        request: market_20151101_models.DescribeCurrentNodeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeCurrentNodeInfoResponse:
        """
        @param request: DescribeCurrentNodeInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCurrentNodeInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCurrentNodeInfo',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeCurrentNodeInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_current_node_info(
        self,
        request: market_20151101_models.DescribeCurrentNodeInfoRequest,
    ) -> market_20151101_models.DescribeCurrentNodeInfoResponse:
        """
        @param request: DescribeCurrentNodeInfoRequest
        @return: DescribeCurrentNodeInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_current_node_info_with_options(request, runtime)

    async def describe_current_node_info_async(
        self,
        request: market_20151101_models.DescribeCurrentNodeInfoRequest,
    ) -> market_20151101_models.DescribeCurrentNodeInfoResponse:
        """
        @param request: DescribeCurrentNodeInfoRequest
        @return: DescribeCurrentNodeInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_current_node_info_with_options_async(request, runtime)

    def describe_distribution_products_with_options(
        self,
        request: market_20151101_models.DescribeDistributionProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeDistributionProductsResponse:
        """
        @summary 分页获取推广商品
        
        @param request: DescribeDistributionProductsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDistributionProductsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDistributionProducts',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeDistributionProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_distribution_products_with_options_async(
        self,
        request: market_20151101_models.DescribeDistributionProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeDistributionProductsResponse:
        """
        @summary 分页获取推广商品
        
        @param request: DescribeDistributionProductsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDistributionProductsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDistributionProducts',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeDistributionProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_distribution_products(
        self,
        request: market_20151101_models.DescribeDistributionProductsRequest,
    ) -> market_20151101_models.DescribeDistributionProductsResponse:
        """
        @summary 分页获取推广商品
        
        @param request: DescribeDistributionProductsRequest
        @return: DescribeDistributionProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_distribution_products_with_options(request, runtime)

    async def describe_distribution_products_async(
        self,
        request: market_20151101_models.DescribeDistributionProductsRequest,
    ) -> market_20151101_models.DescribeDistributionProductsResponse:
        """
        @summary 分页获取推广商品
        
        @param request: DescribeDistributionProductsRequest
        @return: DescribeDistributionProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_distribution_products_with_options_async(request, runtime)

    def describe_distribution_products_link_with_options(
        self,
        tmp_req: market_20151101_models.DescribeDistributionProductsLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeDistributionProductsLinkResponse:
        """
        @summary 获取并生成推广商品-链接
        
        @param tmp_req: DescribeDistributionProductsLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDistributionProductsLinkResponse
        """
        UtilClient.validate_model(tmp_req)
        request = market_20151101_models.DescribeDistributionProductsLinkShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.codes):
            request.codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.codes, 'Codes', 'json')
        query = {}
        if not UtilClient.is_unset(request.codes_shrink):
            query['Codes'] = request.codes_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDistributionProductsLink',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeDistributionProductsLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_distribution_products_link_with_options_async(
        self,
        tmp_req: market_20151101_models.DescribeDistributionProductsLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeDistributionProductsLinkResponse:
        """
        @summary 获取并生成推广商品-链接
        
        @param tmp_req: DescribeDistributionProductsLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDistributionProductsLinkResponse
        """
        UtilClient.validate_model(tmp_req)
        request = market_20151101_models.DescribeDistributionProductsLinkShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.codes):
            request.codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.codes, 'Codes', 'json')
        query = {}
        if not UtilClient.is_unset(request.codes_shrink):
            query['Codes'] = request.codes_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDistributionProductsLink',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeDistributionProductsLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_distribution_products_link(
        self,
        request: market_20151101_models.DescribeDistributionProductsLinkRequest,
    ) -> market_20151101_models.DescribeDistributionProductsLinkResponse:
        """
        @summary 获取并生成推广商品-链接
        
        @param request: DescribeDistributionProductsLinkRequest
        @return: DescribeDistributionProductsLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_distribution_products_link_with_options(request, runtime)

    async def describe_distribution_products_link_async(
        self,
        request: market_20151101_models.DescribeDistributionProductsLinkRequest,
    ) -> market_20151101_models.DescribeDistributionProductsLinkResponse:
        """
        @summary 获取并生成推广商品-链接
        
        @param request: DescribeDistributionProductsLinkRequest
        @return: DescribeDistributionProductsLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_distribution_products_link_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: market_20151101_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeInstanceResponse:
        """
        @param request: DescribeInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        request: market_20151101_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeInstanceResponse:
        """
        @param request: DescribeInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance(
        self,
        request: market_20151101_models.DescribeInstanceRequest,
    ) -> market_20151101_models.DescribeInstanceResponse:
        """
        @param request: DescribeInstanceRequest
        @return: DescribeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: market_20151101_models.DescribeInstanceRequest,
    ) -> market_20151101_models.DescribeInstanceResponse:
        """
        @param request: DescribeInstanceRequest
        @return: DescribeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: market_20151101_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeInstancesResponse:
        """
        @param request: DescribeInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.codes):
            query['Codes'] = request.codes
        if not UtilClient.is_unset(request.except_codes):
            query['ExceptCodes'] = request.except_codes
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: market_20151101_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeInstancesResponse:
        """
        @param request: DescribeInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.codes):
            query['Codes'] = request.codes
        if not UtilClient.is_unset(request.except_codes):
            query['ExceptCodes'] = request.except_codes
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instances(
        self,
        request: market_20151101_models.DescribeInstancesRequest,
    ) -> market_20151101_models.DescribeInstancesResponse:
        """
        @param request: DescribeInstancesRequest
        @return: DescribeInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: market_20151101_models.DescribeInstancesRequest,
    ) -> market_20151101_models.DescribeInstancesResponse:
        """
        @param request: DescribeInstancesRequest
        @return: DescribeInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_license_with_options(
        self,
        request: market_20151101_models.DescribeLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeLicenseResponse:
        """
        @summary 获取License
        
        @param request: DescribeLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLicenseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.license_code):
            query['LicenseCode'] = request.license_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLicense',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_license_with_options_async(
        self,
        request: market_20151101_models.DescribeLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeLicenseResponse:
        """
        @summary 获取License
        
        @param request: DescribeLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLicenseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.license_code):
            query['LicenseCode'] = request.license_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLicense',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_license(
        self,
        request: market_20151101_models.DescribeLicenseRequest,
    ) -> market_20151101_models.DescribeLicenseResponse:
        """
        @summary 获取License
        
        @param request: DescribeLicenseRequest
        @return: DescribeLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_license_with_options(request, runtime)

    async def describe_license_async(
        self,
        request: market_20151101_models.DescribeLicenseRequest,
    ) -> market_20151101_models.DescribeLicenseResponse:
        """
        @summary 获取License
        
        @param request: DescribeLicenseRequest
        @return: DescribeLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_license_with_options_async(request, runtime)

    def describe_order_with_options(
        self,
        request: market_20151101_models.DescribeOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeOrderResponse:
        """
        @param request: DescribeOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOrder',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_order_with_options_async(
        self,
        request: market_20151101_models.DescribeOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeOrderResponse:
        """
        @param request: DescribeOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOrder',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_order(
        self,
        request: market_20151101_models.DescribeOrderRequest,
    ) -> market_20151101_models.DescribeOrderResponse:
        """
        @param request: DescribeOrderRequest
        @return: DescribeOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_order_with_options(request, runtime)

    async def describe_order_async(
        self,
        request: market_20151101_models.DescribeOrderRequest,
    ) -> market_20151101_models.DescribeOrderResponse:
        """
        @param request: DescribeOrderRequest
        @return: DescribeOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_order_with_options_async(request, runtime)

    def describe_price_with_options(
        self,
        request: market_20151101_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribePriceResponse:
        """
        @param request: DescribePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity):
            query['Commodity'] = request.commodity
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrice',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_price_with_options_async(
        self,
        request: market_20151101_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribePriceResponse:
        """
        @param request: DescribePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity):
            query['Commodity'] = request.commodity
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrice',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_price(
        self,
        request: market_20151101_models.DescribePriceRequest,
    ) -> market_20151101_models.DescribePriceResponse:
        """
        @param request: DescribePriceRequest
        @return: DescribePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    async def describe_price_async(
        self,
        request: market_20151101_models.DescribePriceRequest,
    ) -> market_20151101_models.DescribePriceResponse:
        """
        @param request: DescribePriceRequest
        @return: DescribePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_price_with_options_async(request, runtime)

    def describe_product_with_options(
        self,
        request: market_20151101_models.DescribeProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeProductResponse:
        """
        @param request: DescribeProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.query_draft):
            query['QueryDraft'] = request.query_draft
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProduct',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_product_with_options_async(
        self,
        request: market_20151101_models.DescribeProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeProductResponse:
        """
        @param request: DescribeProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.query_draft):
            query['QueryDraft'] = request.query_draft
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProduct',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_product(
        self,
        request: market_20151101_models.DescribeProductRequest,
    ) -> market_20151101_models.DescribeProductResponse:
        """
        @param request: DescribeProductRequest
        @return: DescribeProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_product_with_options(request, runtime)

    async def describe_product_async(
        self,
        request: market_20151101_models.DescribeProductRequest,
    ) -> market_20151101_models.DescribeProductResponse:
        """
        @param request: DescribeProductRequest
        @return: DescribeProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_product_with_options_async(request, runtime)

    def describe_products_with_options(
        self,
        request: market_20151101_models.DescribeProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeProductsResponse:
        """
        @param request: DescribeProductsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProductsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_term):
            query['SearchTerm'] = request.search_term
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProducts',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_products_with_options_async(
        self,
        request: market_20151101_models.DescribeProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeProductsResponse:
        """
        @param request: DescribeProductsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProductsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_term):
            query['SearchTerm'] = request.search_term
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProducts',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_products(
        self,
        request: market_20151101_models.DescribeProductsRequest,
    ) -> market_20151101_models.DescribeProductsResponse:
        """
        @param request: DescribeProductsRequest
        @return: DescribeProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_products_with_options(request, runtime)

    async def describe_products_async(
        self,
        request: market_20151101_models.DescribeProductsRequest,
    ) -> market_20151101_models.DescribeProductsResponse:
        """
        @param request: DescribeProductsRequest
        @return: DescribeProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_products_with_options_async(request, runtime)

    def describe_project_attachments_with_options(
        self,
        request: market_20151101_models.DescribeProjectAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeProjectAttachmentsResponse:
        """
        @param request: DescribeProjectAttachmentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectAttachmentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProjectAttachments',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeProjectAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_project_attachments_with_options_async(
        self,
        request: market_20151101_models.DescribeProjectAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeProjectAttachmentsResponse:
        """
        @param request: DescribeProjectAttachmentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectAttachmentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProjectAttachments',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeProjectAttachmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_project_attachments(
        self,
        request: market_20151101_models.DescribeProjectAttachmentsRequest,
    ) -> market_20151101_models.DescribeProjectAttachmentsResponse:
        """
        @param request: DescribeProjectAttachmentsRequest
        @return: DescribeProjectAttachmentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_project_attachments_with_options(request, runtime)

    async def describe_project_attachments_async(
        self,
        request: market_20151101_models.DescribeProjectAttachmentsRequest,
    ) -> market_20151101_models.DescribeProjectAttachmentsResponse:
        """
        @param request: DescribeProjectAttachmentsRequest
        @return: DescribeProjectAttachmentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_attachments_with_options_async(request, runtime)

    def describe_project_info_with_options(
        self,
        request: market_20151101_models.DescribeProjectInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeProjectInfoResponse:
        """
        @param request: DescribeProjectInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProjectInfo',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeProjectInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_project_info_with_options_async(
        self,
        request: market_20151101_models.DescribeProjectInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeProjectInfoResponse:
        """
        @param request: DescribeProjectInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProjectInfo',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeProjectInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_project_info(
        self,
        request: market_20151101_models.DescribeProjectInfoRequest,
    ) -> market_20151101_models.DescribeProjectInfoResponse:
        """
        @param request: DescribeProjectInfoRequest
        @return: DescribeProjectInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_project_info_with_options(request, runtime)

    async def describe_project_info_async(
        self,
        request: market_20151101_models.DescribeProjectInfoRequest,
    ) -> market_20151101_models.DescribeProjectInfoResponse:
        """
        @param request: DescribeProjectInfoRequest
        @return: DescribeProjectInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_info_with_options_async(request, runtime)

    def describe_project_messages_with_options(
        self,
        request: market_20151101_models.DescribeProjectMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeProjectMessagesResponse:
        """
        @param request: DescribeProjectMessagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectMessagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProjectMessages',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeProjectMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_project_messages_with_options_async(
        self,
        request: market_20151101_models.DescribeProjectMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeProjectMessagesResponse:
        """
        @param request: DescribeProjectMessagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectMessagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProjectMessages',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeProjectMessagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_project_messages(
        self,
        request: market_20151101_models.DescribeProjectMessagesRequest,
    ) -> market_20151101_models.DescribeProjectMessagesResponse:
        """
        @param request: DescribeProjectMessagesRequest
        @return: DescribeProjectMessagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_project_messages_with_options(request, runtime)

    async def describe_project_messages_async(
        self,
        request: market_20151101_models.DescribeProjectMessagesRequest,
    ) -> market_20151101_models.DescribeProjectMessagesResponse:
        """
        @param request: DescribeProjectMessagesRequest
        @return: DescribeProjectMessagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_messages_with_options_async(request, runtime)

    def describe_project_nodes_with_options(
        self,
        request: market_20151101_models.DescribeProjectNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeProjectNodesResponse:
        """
        @description *\
        *\
        
        @param request: DescribeProjectNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProjectNodes',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeProjectNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_project_nodes_with_options_async(
        self,
        request: market_20151101_models.DescribeProjectNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeProjectNodesResponse:
        """
        @description *\
        *\
        
        @param request: DescribeProjectNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProjectNodes',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeProjectNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_project_nodes(
        self,
        request: market_20151101_models.DescribeProjectNodesRequest,
    ) -> market_20151101_models.DescribeProjectNodesResponse:
        """
        @description *\
        *\
        
        @param request: DescribeProjectNodesRequest
        @return: DescribeProjectNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_project_nodes_with_options(request, runtime)

    async def describe_project_nodes_async(
        self,
        request: market_20151101_models.DescribeProjectNodesRequest,
    ) -> market_20151101_models.DescribeProjectNodesResponse:
        """
        @description *\
        *\
        
        @param request: DescribeProjectNodesRequest
        @return: DescribeProjectNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_nodes_with_options_async(request, runtime)

    def describe_project_operate_logs_with_options(
        self,
        request: market_20151101_models.DescribeProjectOperateLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeProjectOperateLogsResponse:
        """
        @param request: DescribeProjectOperateLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectOperateLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProjectOperateLogs',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeProjectOperateLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_project_operate_logs_with_options_async(
        self,
        request: market_20151101_models.DescribeProjectOperateLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeProjectOperateLogsResponse:
        """
        @param request: DescribeProjectOperateLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectOperateLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProjectOperateLogs',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.DescribeProjectOperateLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_project_operate_logs(
        self,
        request: market_20151101_models.DescribeProjectOperateLogsRequest,
    ) -> market_20151101_models.DescribeProjectOperateLogsResponse:
        """
        @param request: DescribeProjectOperateLogsRequest
        @return: DescribeProjectOperateLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_project_operate_logs_with_options(request, runtime)

    async def describe_project_operate_logs_async(
        self,
        request: market_20151101_models.DescribeProjectOperateLogsRequest,
    ) -> market_20151101_models.DescribeProjectOperateLogsResponse:
        """
        @param request: DescribeProjectOperateLogsRequest
        @return: DescribeProjectOperateLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_operate_logs_with_options_async(request, runtime)

    def finish_current_project_node_with_options(
        self,
        request: market_20151101_models.FinishCurrentProjectNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.FinishCurrentProjectNodeResponse:
        """
        @param request: FinishCurrentProjectNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FinishCurrentProjectNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.template_form):
            query['TemplateForm'] = request.template_form
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FinishCurrentProjectNode',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.FinishCurrentProjectNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def finish_current_project_node_with_options_async(
        self,
        request: market_20151101_models.FinishCurrentProjectNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.FinishCurrentProjectNodeResponse:
        """
        @param request: FinishCurrentProjectNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FinishCurrentProjectNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.template_form):
            query['TemplateForm'] = request.template_form
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FinishCurrentProjectNode',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.FinishCurrentProjectNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def finish_current_project_node(
        self,
        request: market_20151101_models.FinishCurrentProjectNodeRequest,
    ) -> market_20151101_models.FinishCurrentProjectNodeResponse:
        """
        @param request: FinishCurrentProjectNodeRequest
        @return: FinishCurrentProjectNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.finish_current_project_node_with_options(request, runtime)

    async def finish_current_project_node_async(
        self,
        request: market_20151101_models.FinishCurrentProjectNodeRequest,
    ) -> market_20151101_models.FinishCurrentProjectNodeResponse:
        """
        @param request: FinishCurrentProjectNodeRequest
        @return: FinishCurrentProjectNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.finish_current_project_node_with_options_async(request, runtime)

    def pause_project_with_options(
        self,
        request: market_20151101_models.PauseProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.PauseProjectResponse:
        """
        @param request: PauseProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PauseProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PauseProject',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.PauseProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_project_with_options_async(
        self,
        request: market_20151101_models.PauseProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.PauseProjectResponse:
        """
        @param request: PauseProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PauseProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PauseProject',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.PauseProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_project(
        self,
        request: market_20151101_models.PauseProjectRequest,
    ) -> market_20151101_models.PauseProjectResponse:
        """
        @param request: PauseProjectRequest
        @return: PauseProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.pause_project_with_options(request, runtime)

    async def pause_project_async(
        self,
        request: market_20151101_models.PauseProjectRequest,
    ) -> market_20151101_models.PauseProjectResponse:
        """
        @param request: PauseProjectRequest
        @return: PauseProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.pause_project_with_options_async(request, runtime)

    def push_metering_data_with_options(
        self,
        request: market_20151101_models.PushMeteringDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.PushMeteringDataResponse:
        """
        @param request: PushMeteringDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushMeteringDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.metering):
            query['Metering'] = request.metering
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushMeteringData',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.PushMeteringDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_metering_data_with_options_async(
        self,
        request: market_20151101_models.PushMeteringDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.PushMeteringDataResponse:
        """
        @param request: PushMeteringDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushMeteringDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.metering):
            query['Metering'] = request.metering
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushMeteringData',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.PushMeteringDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_metering_data(
        self,
        request: market_20151101_models.PushMeteringDataRequest,
    ) -> market_20151101_models.PushMeteringDataResponse:
        """
        @param request: PushMeteringDataRequest
        @return: PushMeteringDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.push_metering_data_with_options(request, runtime)

    async def push_metering_data_async(
        self,
        request: market_20151101_models.PushMeteringDataRequest,
    ) -> market_20151101_models.PushMeteringDataResponse:
        """
        @param request: PushMeteringDataRequest
        @return: PushMeteringDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.push_metering_data_with_options_async(request, runtime)

    def resume_project_with_options(
        self,
        request: market_20151101_models.ResumeProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.ResumeProjectResponse:
        """
        @param request: ResumeProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeProject',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.ResumeProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_project_with_options_async(
        self,
        request: market_20151101_models.ResumeProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.ResumeProjectResponse:
        """
        @param request: ResumeProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeProject',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.ResumeProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_project(
        self,
        request: market_20151101_models.ResumeProjectRequest,
    ) -> market_20151101_models.ResumeProjectResponse:
        """
        @param request: ResumeProjectRequest
        @return: ResumeProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resume_project_with_options(request, runtime)

    async def resume_project_async(
        self,
        request: market_20151101_models.ResumeProjectRequest,
    ) -> market_20151101_models.ResumeProjectResponse:
        """
        @param request: ResumeProjectRequest
        @return: ResumeProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.resume_project_with_options_async(request, runtime)

    def rollback_current_project_node_with_options(
        self,
        request: market_20151101_models.RollbackCurrentProjectNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.RollbackCurrentProjectNodeResponse:
        """
        @param request: RollbackCurrentProjectNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RollbackCurrentProjectNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackCurrentProjectNode',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.RollbackCurrentProjectNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_current_project_node_with_options_async(
        self,
        request: market_20151101_models.RollbackCurrentProjectNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.RollbackCurrentProjectNodeResponse:
        """
        @param request: RollbackCurrentProjectNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RollbackCurrentProjectNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackCurrentProjectNode',
            version='2015-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            market_20151101_models.RollbackCurrentProjectNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_current_project_node(
        self,
        request: market_20151101_models.RollbackCurrentProjectNodeRequest,
    ) -> market_20151101_models.RollbackCurrentProjectNodeResponse:
        """
        @param request: RollbackCurrentProjectNodeRequest
        @return: RollbackCurrentProjectNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rollback_current_project_node_with_options(request, runtime)

    async def rollback_current_project_node_async(
        self,
        request: market_20151101_models.RollbackCurrentProjectNodeRequest,
    ) -> market_20151101_models.RollbackCurrentProjectNodeResponse:
        """
        @param request: RollbackCurrentProjectNodeRequest
        @return: RollbackCurrentProjectNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rollback_current_project_node_with_options_async(request, runtime)
