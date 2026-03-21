# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_wss20211221 import models as main_models
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_multi_order_with_options(
        self,
        tmp_req: main_models.CreateMultiOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMultiOrderResponse:
        tmp_req.validate()
        request = main_models.CreateMultiOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.properties):
            request.properties_shrink = Utils.array_to_string_with_specified_style(tmp_req.properties, 'Properties', 'json')
        query = {}
        if not DaraCore.is_null(request.order_items):
            query['OrderItems'] = request.order_items
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.properties_shrink):
            query['Properties'] = request.properties_shrink
        if not DaraCore.is_null(request.reseller_owner_uid):
            query['ResellerOwnerUid'] = request.reseller_owner_uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMultiOrder',
            version = '2021-12-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMultiOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_multi_order_with_options_async(
        self,
        tmp_req: main_models.CreateMultiOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMultiOrderResponse:
        tmp_req.validate()
        request = main_models.CreateMultiOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.properties):
            request.properties_shrink = Utils.array_to_string_with_specified_style(tmp_req.properties, 'Properties', 'json')
        query = {}
        if not DaraCore.is_null(request.order_items):
            query['OrderItems'] = request.order_items
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.properties_shrink):
            query['Properties'] = request.properties_shrink
        if not DaraCore.is_null(request.reseller_owner_uid):
            query['ResellerOwnerUid'] = request.reseller_owner_uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMultiOrder',
            version = '2021-12-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMultiOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_multi_order(
        self,
        request: main_models.CreateMultiOrderRequest,
    ) -> main_models.CreateMultiOrderResponse:
        runtime = RuntimeOptions()
        return self.create_multi_order_with_options(request, runtime)

    async def create_multi_order_async(
        self,
        request: main_models.CreateMultiOrderRequest,
    ) -> main_models.CreateMultiOrderResponse:
        runtime = RuntimeOptions()
        return await self.create_multi_order_with_options_async(request, runtime)

    def describe_delivery_address_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeliveryAddressResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDeliveryAddress',
            version = '2021-12-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeliveryAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_delivery_address_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeliveryAddressResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDeliveryAddress',
            version = '2021-12-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeliveryAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_delivery_address(self) -> main_models.DescribeDeliveryAddressResponse:
        runtime = RuntimeOptions()
        return self.describe_delivery_address_with_options(runtime)

    async def describe_delivery_address_async(self) -> main_models.DescribeDeliveryAddressResponse:
        runtime = RuntimeOptions()
        return await self.describe_delivery_address_with_options_async(runtime)

    def describe_multi_price_with_options(
        self,
        request: main_models.DescribeMultiPriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMultiPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_items):
            query['OrderItems'] = request.order_items
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.package_code):
            query['PackageCode'] = request.package_code
        if not DaraCore.is_null(request.reseller_owner_uid):
            query['ResellerOwnerUid'] = request.reseller_owner_uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMultiPrice',
            version = '2021-12-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMultiPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_multi_price_with_options_async(
        self,
        request: main_models.DescribeMultiPriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMultiPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_items):
            query['OrderItems'] = request.order_items
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.package_code):
            query['PackageCode'] = request.package_code
        if not DaraCore.is_null(request.reseller_owner_uid):
            query['ResellerOwnerUid'] = request.reseller_owner_uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMultiPrice',
            version = '2021-12-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMultiPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_multi_price(
        self,
        request: main_models.DescribeMultiPriceRequest,
    ) -> main_models.DescribeMultiPriceResponse:
        runtime = RuntimeOptions()
        return self.describe_multi_price_with_options(request, runtime)

    async def describe_multi_price_async(
        self,
        request: main_models.DescribeMultiPriceRequest,
    ) -> main_models.DescribeMultiPriceResponse:
        runtime = RuntimeOptions()
        return await self.describe_multi_price_with_options_async(request, runtime)

    def describe_package_deductions_with_options(
        self,
        request: main_models.DescribePackageDeductionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePackageDeductionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.package_ids):
            query['PackageIds'] = request.package_ids
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePackageDeductions',
            version = '2021-12-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePackageDeductionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_package_deductions_with_options_async(
        self,
        request: main_models.DescribePackageDeductionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePackageDeductionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.package_ids):
            query['PackageIds'] = request.package_ids
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePackageDeductions',
            version = '2021-12-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePackageDeductionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_package_deductions(
        self,
        request: main_models.DescribePackageDeductionsRequest,
    ) -> main_models.DescribePackageDeductionsResponse:
        runtime = RuntimeOptions()
        return self.describe_package_deductions_with_options(request, runtime)

    async def describe_package_deductions_async(
        self,
        request: main_models.DescribePackageDeductionsRequest,
    ) -> main_models.DescribePackageDeductionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_package_deductions_with_options_async(request, runtime)

    def modify_instance_properties_with_options(
        self,
        request: main_models.ModifyInstancePropertiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstancePropertiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceProperties',
            version = '2021-12-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstancePropertiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_properties_with_options_async(
        self,
        request: main_models.ModifyInstancePropertiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstancePropertiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceProperties',
            version = '2021-12-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstancePropertiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_properties(
        self,
        request: main_models.ModifyInstancePropertiesRequest,
    ) -> main_models.ModifyInstancePropertiesResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_properties_with_options(request, runtime)

    async def modify_instance_properties_async(
        self,
        request: main_models.ModifyInstancePropertiesRequest,
    ) -> main_models.ModifyInstancePropertiesResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_properties_with_options_async(request, runtime)
