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
        runtime = util_models.RuntimeOptions()
        return self.activate_license_with_options(request, runtime)

    async def activate_license_async(
        self,
        request: market_20151101_models.ActivateLicenseRequest,
    ) -> market_20151101_models.ActivateLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.activate_license_with_options_async(request, runtime)

    def bind_image_package_with_options(
        self,
        request: market_20151101_models.BindImagePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.BindImagePackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not UtilClient.is_unset(request.image_package_instance_id):
            query['ImagePackageInstanceId'] = request.image_package_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindImagePackage',
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
            market_20151101_models.BindImagePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_image_package_with_options_async(
        self,
        request: market_20151101_models.BindImagePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.BindImagePackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not UtilClient.is_unset(request.image_package_instance_id):
            query['ImagePackageInstanceId'] = request.image_package_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindImagePackage',
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
            market_20151101_models.BindImagePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_image_package(
        self,
        request: market_20151101_models.BindImagePackageRequest,
    ) -> market_20151101_models.BindImagePackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_image_package_with_options(request, runtime)

    async def bind_image_package_async(
        self,
        request: market_20151101_models.BindImagePackageRequest,
    ) -> market_20151101_models.BindImagePackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_image_package_with_options_async(request, runtime)

    def create_commodity_with_options(
        self,
        request: market_20151101_models.CreateCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.CreateCommodityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCommodity',
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
            market_20151101_models.CreateCommodityResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_commodity_with_options_async(
        self,
        request: market_20151101_models.CreateCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.CreateCommodityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCommodity',
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
            market_20151101_models.CreateCommodityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_commodity(
        self,
        request: market_20151101_models.CreateCommodityRequest,
    ) -> market_20151101_models.CreateCommodityResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_commodity_with_options(request, runtime)

    async def create_commodity_async(
        self,
        request: market_20151101_models.CreateCommodityRequest,
    ) -> market_20151101_models.CreateCommodityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_commodity_with_options_async(request, runtime)

    def create_order_with_options(
        self,
        request: market_20151101_models.CreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.CreateOrderResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.create_order_with_options(request, runtime)

    async def create_order_async(
        self,
        request: market_20151101_models.CreateOrderRequest,
    ) -> market_20151101_models.CreateOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_order_with_options_async(request, runtime)

    def create_rate_with_options(
        self,
        request: market_20151101_models.CreateRateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.CreateRateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.customer_labels):
            query['CustomerLabels'] = request.customer_labels
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.score):
            query['Score'] = request.score
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRate',
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
            market_20151101_models.CreateRateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rate_with_options_async(
        self,
        request: market_20151101_models.CreateRateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.CreateRateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.customer_labels):
            query['CustomerLabels'] = request.customer_labels
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.score):
            query['Score'] = request.score
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRate',
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
            market_20151101_models.CreateRateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rate(
        self,
        request: market_20151101_models.CreateRateRequest,
    ) -> market_20151101_models.CreateRateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_rate_with_options(request, runtime)

    async def create_rate_async(
        self,
        request: market_20151101_models.CreateRateRequest,
    ) -> market_20151101_models.CreateRateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_rate_with_options_async(request, runtime)

    def delete_commodity_with_options(
        self,
        request: market_20151101_models.DeleteCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DeleteCommodityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_id):
            query['CommodityId'] = request.commodity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCommodity',
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
            market_20151101_models.DeleteCommodityResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_commodity_with_options_async(
        self,
        request: market_20151101_models.DeleteCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DeleteCommodityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_id):
            query['CommodityId'] = request.commodity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCommodity',
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
            market_20151101_models.DeleteCommodityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_commodity(
        self,
        request: market_20151101_models.DeleteCommodityRequest,
    ) -> market_20151101_models.DeleteCommodityResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_commodity_with_options(request, runtime)

    async def delete_commodity_async(
        self,
        request: market_20151101_models.DeleteCommodityRequest,
    ) -> market_20151101_models.DeleteCommodityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_commodity_with_options_async(request, runtime)

    def describe_commodities_with_options(
        self,
        request: market_20151101_models.DescribeCommoditiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeCommoditiesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCommodities',
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
            market_20151101_models.DescribeCommoditiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_commodities_with_options_async(
        self,
        request: market_20151101_models.DescribeCommoditiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeCommoditiesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCommodities',
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
            market_20151101_models.DescribeCommoditiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_commodities(
        self,
        request: market_20151101_models.DescribeCommoditiesRequest,
    ) -> market_20151101_models.DescribeCommoditiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_commodities_with_options(request, runtime)

    async def describe_commodities_async(
        self,
        request: market_20151101_models.DescribeCommoditiesRequest,
    ) -> market_20151101_models.DescribeCommoditiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_commodities_with_options_async(request, runtime)

    def describe_commodity_with_options(
        self,
        request: market_20151101_models.DescribeCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeCommodityResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCommodity',
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
            market_20151101_models.DescribeCommodityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_commodity_with_options_async(
        self,
        request: market_20151101_models.DescribeCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeCommodityResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCommodity',
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
            market_20151101_models.DescribeCommodityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_commodity(
        self,
        request: market_20151101_models.DescribeCommodityRequest,
    ) -> market_20151101_models.DescribeCommodityResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_commodity_with_options(request, runtime)

    async def describe_commodity_async(
        self,
        request: market_20151101_models.DescribeCommodityRequest,
    ) -> market_20151101_models.DescribeCommodityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_commodity_with_options_async(request, runtime)

    def describe_current_node_info_with_options(
        self,
        request: market_20151101_models.DescribeCurrentNodeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeCurrentNodeInfoResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_current_node_info_with_options(request, runtime)

    async def describe_current_node_info_async(
        self,
        request: market_20151101_models.DescribeCurrentNodeInfoRequest,
    ) -> market_20151101_models.DescribeCurrentNodeInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_current_node_info_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: market_20151101_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeInstanceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: market_20151101_models.DescribeInstanceRequest,
    ) -> market_20151101_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: market_20151101_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeInstancesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: market_20151101_models.DescribeInstancesRequest,
    ) -> market_20151101_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_license_with_options(
        self,
        request: market_20151101_models.DescribeLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeLicenseResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_license_with_options(request, runtime)

    async def describe_license_async(
        self,
        request: market_20151101_models.DescribeLicenseRequest,
    ) -> market_20151101_models.DescribeLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_license_with_options_async(request, runtime)

    def describe_order_with_options(
        self,
        request: market_20151101_models.DescribeOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeOrderResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_order_with_options(request, runtime)

    async def describe_order_async(
        self,
        request: market_20151101_models.DescribeOrderRequest,
    ) -> market_20151101_models.DescribeOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_order_with_options_async(request, runtime)

    def describe_price_with_options(
        self,
        request: market_20151101_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribePriceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    async def describe_price_async(
        self,
        request: market_20151101_models.DescribePriceRequest,
    ) -> market_20151101_models.DescribePriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_price_with_options_async(request, runtime)

    def describe_product_with_options(
        self,
        request: market_20151101_models.DescribeProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeProductResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_product_with_options(request, runtime)

    async def describe_product_async(
        self,
        request: market_20151101_models.DescribeProductRequest,
    ) -> market_20151101_models.DescribeProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_product_with_options_async(request, runtime)

    def describe_products_with_options(
        self,
        request: market_20151101_models.DescribeProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeProductsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_products_with_options(request, runtime)

    async def describe_products_async(
        self,
        request: market_20151101_models.DescribeProductsRequest,
    ) -> market_20151101_models.DescribeProductsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_products_with_options_async(request, runtime)

    def describe_project_attachments_with_options(
        self,
        request: market_20151101_models.DescribeProjectAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeProjectAttachmentsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_project_attachments_with_options(request, runtime)

    async def describe_project_attachments_async(
        self,
        request: market_20151101_models.DescribeProjectAttachmentsRequest,
    ) -> market_20151101_models.DescribeProjectAttachmentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_attachments_with_options_async(request, runtime)

    def describe_project_info_with_options(
        self,
        request: market_20151101_models.DescribeProjectInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeProjectInfoResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_project_info_with_options(request, runtime)

    async def describe_project_info_async(
        self,
        request: market_20151101_models.DescribeProjectInfoRequest,
    ) -> market_20151101_models.DescribeProjectInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_info_with_options_async(request, runtime)

    def describe_project_messages_with_options(
        self,
        request: market_20151101_models.DescribeProjectMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeProjectMessagesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_project_messages_with_options(request, runtime)

    async def describe_project_messages_async(
        self,
        request: market_20151101_models.DescribeProjectMessagesRequest,
    ) -> market_20151101_models.DescribeProjectMessagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_messages_with_options_async(request, runtime)

    def describe_project_nodes_with_options(
        self,
        request: market_20151101_models.DescribeProjectNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeProjectNodesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_project_nodes_with_options(request, runtime)

    async def describe_project_nodes_async(
        self,
        request: market_20151101_models.DescribeProjectNodesRequest,
    ) -> market_20151101_models.DescribeProjectNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_nodes_with_options_async(request, runtime)

    def describe_project_operate_logs_with_options(
        self,
        request: market_20151101_models.DescribeProjectOperateLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeProjectOperateLogsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_project_operate_logs_with_options(request, runtime)

    async def describe_project_operate_logs_async(
        self,
        request: market_20151101_models.DescribeProjectOperateLogsRequest,
    ) -> market_20151101_models.DescribeProjectOperateLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_operate_logs_with_options_async(request, runtime)

    def describe_rate_with_options(
        self,
        request: market_20151101_models.DescribeRateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeRateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRate',
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
            market_20151101_models.DescribeRateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rate_with_options_async(
        self,
        request: market_20151101_models.DescribeRateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.DescribeRateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRate',
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
            market_20151101_models.DescribeRateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rate(
        self,
        request: market_20151101_models.DescribeRateRequest,
    ) -> market_20151101_models.DescribeRateResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rate_with_options(request, runtime)

    async def describe_rate_async(
        self,
        request: market_20151101_models.DescribeRateRequest,
    ) -> market_20151101_models.DescribeRateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rate_with_options_async(request, runtime)

    def finish_current_project_node_with_options(
        self,
        request: market_20151101_models.FinishCurrentProjectNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.FinishCurrentProjectNodeResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.finish_current_project_node_with_options(request, runtime)

    async def finish_current_project_node_async(
        self,
        request: market_20151101_models.FinishCurrentProjectNodeRequest,
    ) -> market_20151101_models.FinishCurrentProjectNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.finish_current_project_node_with_options_async(request, runtime)

    def notify_contract_event_with_options(
        self,
        request: market_20151101_models.NotifyContractEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.NotifyContractEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_message):
            query['EventMessage'] = request.event_message
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NotifyContractEvent',
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
            market_20151101_models.NotifyContractEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def notify_contract_event_with_options_async(
        self,
        request: market_20151101_models.NotifyContractEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.NotifyContractEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_message):
            query['EventMessage'] = request.event_message
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NotifyContractEvent',
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
            market_20151101_models.NotifyContractEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def notify_contract_event(
        self,
        request: market_20151101_models.NotifyContractEventRequest,
    ) -> market_20151101_models.NotifyContractEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.notify_contract_event_with_options(request, runtime)

    async def notify_contract_event_async(
        self,
        request: market_20151101_models.NotifyContractEventRequest,
    ) -> market_20151101_models.NotifyContractEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.notify_contract_event_with_options_async(request, runtime)

    def pause_project_with_options(
        self,
        request: market_20151101_models.PauseProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.PauseProjectResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.pause_project_with_options(request, runtime)

    async def pause_project_async(
        self,
        request: market_20151101_models.PauseProjectRequest,
    ) -> market_20151101_models.PauseProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pause_project_with_options_async(request, runtime)

    def push_metering_data_with_options(
        self,
        request: market_20151101_models.PushMeteringDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.PushMeteringDataResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.push_metering_data_with_options(request, runtime)

    async def push_metering_data_async(
        self,
        request: market_20151101_models.PushMeteringDataRequest,
    ) -> market_20151101_models.PushMeteringDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.push_metering_data_with_options_async(request, runtime)

    def query_market_categories_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.QueryMarketCategoriesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryMarketCategories',
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
            market_20151101_models.QueryMarketCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_market_categories_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.QueryMarketCategoriesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryMarketCategories',
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
            market_20151101_models.QueryMarketCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_market_categories(self) -> market_20151101_models.QueryMarketCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_market_categories_with_options(runtime)

    async def query_market_categories_async(self) -> market_20151101_models.QueryMarketCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_market_categories_with_options_async(runtime)

    def query_market_images_with_options(
        self,
        request: market_20151101_models.QueryMarketImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.QueryMarketImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMarketImages',
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
            market_20151101_models.QueryMarketImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_market_images_with_options_async(
        self,
        request: market_20151101_models.QueryMarketImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.QueryMarketImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMarketImages',
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
            market_20151101_models.QueryMarketImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_market_images(
        self,
        request: market_20151101_models.QueryMarketImagesRequest,
    ) -> market_20151101_models.QueryMarketImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_market_images_with_options(request, runtime)

    async def query_market_images_async(
        self,
        request: market_20151101_models.QueryMarketImagesRequest,
    ) -> market_20151101_models.QueryMarketImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_market_images_with_options_async(request, runtime)

    def resume_project_with_options(
        self,
        request: market_20151101_models.ResumeProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.ResumeProjectResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.resume_project_with_options(request, runtime)

    async def resume_project_async(
        self,
        request: market_20151101_models.ResumeProjectRequest,
    ) -> market_20151101_models.ResumeProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_project_with_options_async(request, runtime)

    def rollback_current_project_node_with_options(
        self,
        request: market_20151101_models.RollbackCurrentProjectNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.RollbackCurrentProjectNodeResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.rollback_current_project_node_with_options(request, runtime)

    async def rollback_current_project_node_async(
        self,
        request: market_20151101_models.RollbackCurrentProjectNodeRequest,
    ) -> market_20151101_models.RollbackCurrentProjectNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rollback_current_project_node_with_options_async(request, runtime)

    def update_commodity_with_options(
        self,
        request: market_20151101_models.UpdateCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.UpdateCommodityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_id):
            query['CommodityId'] = request.commodity_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCommodity',
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
            market_20151101_models.UpdateCommodityResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_commodity_with_options_async(
        self,
        request: market_20151101_models.UpdateCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.UpdateCommodityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_id):
            query['CommodityId'] = request.commodity_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCommodity',
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
            market_20151101_models.UpdateCommodityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_commodity(
        self,
        request: market_20151101_models.UpdateCommodityRequest,
    ) -> market_20151101_models.UpdateCommodityResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_commodity_with_options(request, runtime)

    async def update_commodity_async(
        self,
        request: market_20151101_models.UpdateCommodityRequest,
    ) -> market_20151101_models.UpdateCommodityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_commodity_with_options_async(request, runtime)

    def upload_commodity_file_with_options(
        self,
        request: market_20151101_models.UploadCommodityFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.UploadCommodityFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_content_type):
            query['FileContentType'] = request.file_content_type
        if not UtilClient.is_unset(request.file_resource):
            query['FileResource'] = request.file_resource
        if not UtilClient.is_unset(request.file_resource_type):
            query['FileResourceType'] = request.file_resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadCommodityFile',
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
            market_20151101_models.UploadCommodityFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_commodity_file_with_options_async(
        self,
        request: market_20151101_models.UploadCommodityFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> market_20151101_models.UploadCommodityFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_content_type):
            query['FileContentType'] = request.file_content_type
        if not UtilClient.is_unset(request.file_resource):
            query['FileResource'] = request.file_resource
        if not UtilClient.is_unset(request.file_resource_type):
            query['FileResourceType'] = request.file_resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadCommodityFile',
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
            market_20151101_models.UploadCommodityFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_commodity_file(
        self,
        request: market_20151101_models.UploadCommodityFileRequest,
    ) -> market_20151101_models.UploadCommodityFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_commodity_file_with_options(request, runtime)

    async def upload_commodity_file_async(
        self,
        request: market_20151101_models.UploadCommodityFileRequest,
    ) -> market_20151101_models.UploadCommodityFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_commodity_file_with_options_async(request, runtime)
