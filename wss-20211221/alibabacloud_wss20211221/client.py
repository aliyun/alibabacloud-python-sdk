# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_wss20211221 import models as wss_20211221_models
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
        self._endpoint = self.get_endpoint('wss', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_multi_order_with_options(
        self,
        tmp_req: wss_20211221_models.CreateMultiOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wss_20211221_models.CreateMultiOrderResponse:
        """
        @summary 多商品组合下单
        
        @param tmp_req: CreateMultiOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMultiOrderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = wss_20211221_models.CreateMultiOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.properties):
            request.properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.properties, 'Properties', 'json')
        query = {}
        if not UtilClient.is_unset(request.order_items):
            query['OrderItems'] = request.order_items
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.properties_shrink):
            query['Properties'] = request.properties_shrink
        if not UtilClient.is_unset(request.reseller_owner_uid):
            query['ResellerOwnerUid'] = request.reseller_owner_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMultiOrder',
            version='2021-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wss_20211221_models.CreateMultiOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_multi_order_with_options_async(
        self,
        tmp_req: wss_20211221_models.CreateMultiOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wss_20211221_models.CreateMultiOrderResponse:
        """
        @summary 多商品组合下单
        
        @param tmp_req: CreateMultiOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMultiOrderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = wss_20211221_models.CreateMultiOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.properties):
            request.properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.properties, 'Properties', 'json')
        query = {}
        if not UtilClient.is_unset(request.order_items):
            query['OrderItems'] = request.order_items
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.properties_shrink):
            query['Properties'] = request.properties_shrink
        if not UtilClient.is_unset(request.reseller_owner_uid):
            query['ResellerOwnerUid'] = request.reseller_owner_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMultiOrder',
            version='2021-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wss_20211221_models.CreateMultiOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_multi_order(
        self,
        request: wss_20211221_models.CreateMultiOrderRequest,
    ) -> wss_20211221_models.CreateMultiOrderResponse:
        """
        @summary 多商品组合下单
        
        @param request: CreateMultiOrderRequest
        @return: CreateMultiOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_multi_order_with_options(request, runtime)

    async def create_multi_order_async(
        self,
        request: wss_20211221_models.CreateMultiOrderRequest,
    ) -> wss_20211221_models.CreateMultiOrderResponse:
        """
        @summary 多商品组合下单
        
        @param request: CreateMultiOrderRequest
        @return: CreateMultiOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_multi_order_with_options_async(request, runtime)

    def describe_delivery_address_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> wss_20211221_models.DescribeDeliveryAddressResponse:
        """
        @param request: DescribeDeliveryAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeliveryAddressResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeDeliveryAddress',
            version='2021-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wss_20211221_models.DescribeDeliveryAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_delivery_address_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> wss_20211221_models.DescribeDeliveryAddressResponse:
        """
        @param request: DescribeDeliveryAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeliveryAddressResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeDeliveryAddress',
            version='2021-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wss_20211221_models.DescribeDeliveryAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_delivery_address(self) -> wss_20211221_models.DescribeDeliveryAddressResponse:
        """
        @return: DescribeDeliveryAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_delivery_address_with_options(runtime)

    async def describe_delivery_address_async(self) -> wss_20211221_models.DescribeDeliveryAddressResponse:
        """
        @return: DescribeDeliveryAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_delivery_address_with_options_async(runtime)

    def describe_multi_price_with_options(
        self,
        request: wss_20211221_models.DescribeMultiPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wss_20211221_models.DescribeMultiPriceResponse:
        """
        @param request: DescribeMultiPriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMultiPriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_items):
            query['OrderItems'] = request.order_items
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.package_code):
            query['PackageCode'] = request.package_code
        if not UtilClient.is_unset(request.reseller_owner_uid):
            query['ResellerOwnerUid'] = request.reseller_owner_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMultiPrice',
            version='2021-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wss_20211221_models.DescribeMultiPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_multi_price_with_options_async(
        self,
        request: wss_20211221_models.DescribeMultiPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wss_20211221_models.DescribeMultiPriceResponse:
        """
        @param request: DescribeMultiPriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMultiPriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_items):
            query['OrderItems'] = request.order_items
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.package_code):
            query['PackageCode'] = request.package_code
        if not UtilClient.is_unset(request.reseller_owner_uid):
            query['ResellerOwnerUid'] = request.reseller_owner_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMultiPrice',
            version='2021-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wss_20211221_models.DescribeMultiPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_multi_price(
        self,
        request: wss_20211221_models.DescribeMultiPriceRequest,
    ) -> wss_20211221_models.DescribeMultiPriceResponse:
        """
        @param request: DescribeMultiPriceRequest
        @return: DescribeMultiPriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_multi_price_with_options(request, runtime)

    async def describe_multi_price_async(
        self,
        request: wss_20211221_models.DescribeMultiPriceRequest,
    ) -> wss_20211221_models.DescribeMultiPriceResponse:
        """
        @param request: DescribeMultiPriceRequest
        @return: DescribeMultiPriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_multi_price_with_options_async(request, runtime)

    def describe_package_deductions_with_options(
        self,
        request: wss_20211221_models.DescribePackageDeductionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wss_20211221_models.DescribePackageDeductionsResponse:
        """
        @summary 查询核时包抵扣明细
        
        @param request: DescribePackageDeductionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePackageDeductionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.package_ids):
            query['PackageIds'] = request.package_ids
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePackageDeductions',
            version='2021-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wss_20211221_models.DescribePackageDeductionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_package_deductions_with_options_async(
        self,
        request: wss_20211221_models.DescribePackageDeductionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wss_20211221_models.DescribePackageDeductionsResponse:
        """
        @summary 查询核时包抵扣明细
        
        @param request: DescribePackageDeductionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePackageDeductionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.package_ids):
            query['PackageIds'] = request.package_ids
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePackageDeductions',
            version='2021-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wss_20211221_models.DescribePackageDeductionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_package_deductions(
        self,
        request: wss_20211221_models.DescribePackageDeductionsRequest,
    ) -> wss_20211221_models.DescribePackageDeductionsResponse:
        """
        @summary 查询核时包抵扣明细
        
        @param request: DescribePackageDeductionsRequest
        @return: DescribePackageDeductionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_package_deductions_with_options(request, runtime)

    async def describe_package_deductions_async(
        self,
        request: wss_20211221_models.DescribePackageDeductionsRequest,
    ) -> wss_20211221_models.DescribePackageDeductionsResponse:
        """
        @summary 查询核时包抵扣明细
        
        @param request: DescribePackageDeductionsRequest
        @return: DescribePackageDeductionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_package_deductions_with_options_async(request, runtime)

    def modify_instance_properties_with_options(
        self,
        request: wss_20211221_models.ModifyInstancePropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wss_20211221_models.ModifyInstancePropertiesResponse:
        """
        @param request: ModifyInstancePropertiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstancePropertiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceProperties',
            version='2021-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wss_20211221_models.ModifyInstancePropertiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_properties_with_options_async(
        self,
        request: wss_20211221_models.ModifyInstancePropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wss_20211221_models.ModifyInstancePropertiesResponse:
        """
        @param request: ModifyInstancePropertiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstancePropertiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceProperties',
            version='2021-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wss_20211221_models.ModifyInstancePropertiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_properties(
        self,
        request: wss_20211221_models.ModifyInstancePropertiesRequest,
    ) -> wss_20211221_models.ModifyInstancePropertiesResponse:
        """
        @param request: ModifyInstancePropertiesRequest
        @return: ModifyInstancePropertiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_properties_with_options(request, runtime)

    async def modify_instance_properties_async(
        self,
        request: wss_20211221_models.ModifyInstancePropertiesRequest,
    ) -> wss_20211221_models.ModifyInstancePropertiesResponse:
        """
        @param request: ModifyInstancePropertiesRequest
        @return: ModifyInstancePropertiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_properties_with_options_async(request, runtime)
