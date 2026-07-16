# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_market20151101 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def activate_license_with_options(
        self,
        request: main_models.ActivateLicenseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActivateLicenseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identification):
            query['Identification'] = request.identification
        if not DaraCore.is_null(request.license_code):
            query['LicenseCode'] = request.license_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ActivateLicense',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActivateLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_license_with_options_async(
        self,
        request: main_models.ActivateLicenseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActivateLicenseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identification):
            query['Identification'] = request.identification
        if not DaraCore.is_null(request.license_code):
            query['LicenseCode'] = request.license_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ActivateLicense',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActivateLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def activate_license(
        self,
        request: main_models.ActivateLicenseRequest,
    ) -> main_models.ActivateLicenseResponse:
        runtime = RuntimeOptions()
        return self.activate_license_with_options(request, runtime)

    async def activate_license_async(
        self,
        request: main_models.ActivateLicenseRequest,
    ) -> main_models.ActivateLicenseResponse:
        runtime = RuntimeOptions()
        return await self.activate_license_with_options_async(request, runtime)

    def auto_renew_instance_with_options(
        self,
        request: main_models.AutoRenewInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AutoRenewInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_renew_cycle):
            body['AutoRenewCycle'] = request.auto_renew_cycle
        if not DaraCore.is_null(request.auto_renew_duration):
            body['AutoRenewDuration'] = request.auto_renew_duration
        if not DaraCore.is_null(request.order_biz_id):
            body['OrderBizId'] = request.order_biz_id
        if not DaraCore.is_null(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AutoRenewInstance',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AutoRenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def auto_renew_instance_with_options_async(
        self,
        request: main_models.AutoRenewInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AutoRenewInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_renew_cycle):
            body['AutoRenewCycle'] = request.auto_renew_cycle
        if not DaraCore.is_null(request.auto_renew_duration):
            body['AutoRenewDuration'] = request.auto_renew_duration
        if not DaraCore.is_null(request.order_biz_id):
            body['OrderBizId'] = request.order_biz_id
        if not DaraCore.is_null(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AutoRenewInstance',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AutoRenewInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def auto_renew_instance(
        self,
        request: main_models.AutoRenewInstanceRequest,
    ) -> main_models.AutoRenewInstanceResponse:
        runtime = RuntimeOptions()
        return self.auto_renew_instance_with_options(request, runtime)

    async def auto_renew_instance_async(
        self,
        request: main_models.AutoRenewInstanceRequest,
    ) -> main_models.AutoRenewInstanceResponse:
        runtime = RuntimeOptions()
        return await self.auto_renew_instance_with_options_async(request, runtime)

    def confirm_notification_with_options(
        self,
        request: main_models.ConfirmNotificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfirmNotificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.notification_request_id):
            query['NotificationRequestId'] = request.notification_request_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfirmNotification',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfirmNotificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_notification_with_options_async(
        self,
        request: main_models.ConfirmNotificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfirmNotificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.notification_request_id):
            query['NotificationRequestId'] = request.notification_request_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfirmNotification',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfirmNotificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_notification(
        self,
        request: main_models.ConfirmNotificationRequest,
    ) -> main_models.ConfirmNotificationResponse:
        runtime = RuntimeOptions()
        return self.confirm_notification_with_options(request, runtime)

    async def confirm_notification_async(
        self,
        request: main_models.ConfirmNotificationRequest,
    ) -> main_models.ConfirmNotificationResponse:
        runtime = RuntimeOptions()
        return await self.confirm_notification_with_options_async(request, runtime)

    def create_order_with_options(
        self,
        request: main_models.CreateOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.commodity):
            query['Commodity'] = request.commodity
        if not DaraCore.is_null(request.order_souce):
            query['OrderSouce'] = request.order_souce
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrder',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_order_with_options_async(
        self,
        request: main_models.CreateOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.commodity):
            query['Commodity'] = request.commodity
        if not DaraCore.is_null(request.order_souce):
            query['OrderSouce'] = request.order_souce
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrder',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_order(
        self,
        request: main_models.CreateOrderRequest,
    ) -> main_models.CreateOrderResponse:
        runtime = RuntimeOptions()
        return self.create_order_with_options(request, runtime)

    async def create_order_async(
        self,
        request: main_models.CreateOrderRequest,
    ) -> main_models.CreateOrderResponse:
        runtime = RuntimeOptions()
        return await self.create_order_with_options_async(request, runtime)

    def cross_account_verify_token_with_options(
        self,
        request: main_models.CrossAccountVerifyTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CrossAccountVerifyTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.token):
            body['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CrossAccountVerifyToken',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CrossAccountVerifyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def cross_account_verify_token_with_options_async(
        self,
        request: main_models.CrossAccountVerifyTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CrossAccountVerifyTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.token):
            body['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CrossAccountVerifyToken',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CrossAccountVerifyTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cross_account_verify_token(
        self,
        request: main_models.CrossAccountVerifyTokenRequest,
    ) -> main_models.CrossAccountVerifyTokenResponse:
        runtime = RuntimeOptions()
        return self.cross_account_verify_token_with_options(request, runtime)

    async def cross_account_verify_token_async(
        self,
        request: main_models.CrossAccountVerifyTokenRequest,
    ) -> main_models.CrossAccountVerifyTokenResponse:
        runtime = RuntimeOptions()
        return await self.cross_account_verify_token_with_options_async(request, runtime)

    def describe_api_metering_with_options(
        self,
        request: main_models.DescribeApiMeteringRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiMeteringResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiMetering',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiMeteringResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_metering_with_options_async(
        self,
        request: main_models.DescribeApiMeteringRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiMeteringResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiMetering',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiMeteringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_metering(
        self,
        request: main_models.DescribeApiMeteringRequest,
    ) -> main_models.DescribeApiMeteringResponse:
        runtime = RuntimeOptions()
        return self.describe_api_metering_with_options(request, runtime)

    async def describe_api_metering_async(
        self,
        request: main_models.DescribeApiMeteringRequest,
    ) -> main_models.DescribeApiMeteringResponse:
        runtime = RuntimeOptions()
        return await self.describe_api_metering_with_options_async(request, runtime)

    def describe_current_node_info_with_options(
        self,
        request: main_models.DescribeCurrentNodeInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCurrentNodeInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCurrentNodeInfo',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCurrentNodeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_current_node_info_with_options_async(
        self,
        request: main_models.DescribeCurrentNodeInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCurrentNodeInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCurrentNodeInfo',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCurrentNodeInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_current_node_info(
        self,
        request: main_models.DescribeCurrentNodeInfoRequest,
    ) -> main_models.DescribeCurrentNodeInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_current_node_info_with_options(request, runtime)

    async def describe_current_node_info_async(
        self,
        request: main_models.DescribeCurrentNodeInfoRequest,
    ) -> main_models.DescribeCurrentNodeInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_current_node_info_with_options_async(request, runtime)

    def describe_distribution_products_with_options(
        self,
        request: main_models.DescribeDistributionProductsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDistributionProductsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDistributionProducts',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDistributionProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_distribution_products_with_options_async(
        self,
        request: main_models.DescribeDistributionProductsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDistributionProductsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDistributionProducts',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDistributionProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_distribution_products(
        self,
        request: main_models.DescribeDistributionProductsRequest,
    ) -> main_models.DescribeDistributionProductsResponse:
        runtime = RuntimeOptions()
        return self.describe_distribution_products_with_options(request, runtime)

    async def describe_distribution_products_async(
        self,
        request: main_models.DescribeDistributionProductsRequest,
    ) -> main_models.DescribeDistributionProductsResponse:
        runtime = RuntimeOptions()
        return await self.describe_distribution_products_with_options_async(request, runtime)

    def describe_distribution_products_link_with_options(
        self,
        tmp_req: main_models.DescribeDistributionProductsLinkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDistributionProductsLinkResponse:
        tmp_req.validate()
        request = main_models.DescribeDistributionProductsLinkShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.codes):
            request.codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.codes, 'Codes', 'json')
        query = {}
        if not DaraCore.is_null(request.codes_shrink):
            query['Codes'] = request.codes_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDistributionProductsLink',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDistributionProductsLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_distribution_products_link_with_options_async(
        self,
        tmp_req: main_models.DescribeDistributionProductsLinkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDistributionProductsLinkResponse:
        tmp_req.validate()
        request = main_models.DescribeDistributionProductsLinkShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.codes):
            request.codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.codes, 'Codes', 'json')
        query = {}
        if not DaraCore.is_null(request.codes_shrink):
            query['Codes'] = request.codes_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDistributionProductsLink',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDistributionProductsLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_distribution_products_link(
        self,
        request: main_models.DescribeDistributionProductsLinkRequest,
    ) -> main_models.DescribeDistributionProductsLinkResponse:
        runtime = RuntimeOptions()
        return self.describe_distribution_products_link_with_options(request, runtime)

    async def describe_distribution_products_link_async(
        self,
        request: main_models.DescribeDistributionProductsLinkRequest,
    ) -> main_models.DescribeDistributionProductsLinkResponse:
        runtime = RuntimeOptions()
        return await self.describe_distribution_products_link_with_options_async(request, runtime)

    def describe_failed_notifications_with_options(
        self,
        request: main_models.DescribeFailedNotificationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFailedNotificationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFailedNotifications',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFailedNotificationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_failed_notifications_with_options_async(
        self,
        request: main_models.DescribeFailedNotificationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFailedNotificationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFailedNotifications',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFailedNotificationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_failed_notifications(
        self,
        request: main_models.DescribeFailedNotificationsRequest,
    ) -> main_models.DescribeFailedNotificationsResponse:
        runtime = RuntimeOptions()
        return self.describe_failed_notifications_with_options(request, runtime)

    async def describe_failed_notifications_async(
        self,
        request: main_models.DescribeFailedNotificationsRequest,
    ) -> main_models.DescribeFailedNotificationsResponse:
        runtime = RuntimeOptions()
        return await self.describe_failed_notifications_with_options_async(request, runtime)

    def describe_image_instance_for_isv_with_options(
        self,
        request: main_models.DescribeImageInstanceForIsvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeImageInstanceForIsvResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_pk):
            query['CustomerPk'] = request.customer_pk
        if not DaraCore.is_null(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeImageInstanceForIsv',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeImageInstanceForIsvResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_instance_for_isv_with_options_async(
        self,
        request: main_models.DescribeImageInstanceForIsvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeImageInstanceForIsvResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_pk):
            query['CustomerPk'] = request.customer_pk
        if not DaraCore.is_null(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeImageInstanceForIsv',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeImageInstanceForIsvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_instance_for_isv(
        self,
        request: main_models.DescribeImageInstanceForIsvRequest,
    ) -> main_models.DescribeImageInstanceForIsvResponse:
        runtime = RuntimeOptions()
        return self.describe_image_instance_for_isv_with_options(request, runtime)

    async def describe_image_instance_for_isv_async(
        self,
        request: main_models.DescribeImageInstanceForIsvRequest,
    ) -> main_models.DescribeImageInstanceForIsvResponse:
        runtime = RuntimeOptions()
        return await self.describe_image_instance_for_isv_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: main_models.DescribeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstance',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        request: main_models.DescribeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstance',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance(
        self,
        request: main_models.DescribeInstanceRequest,
    ) -> main_models.DescribeInstanceResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: main_models.DescribeInstanceRequest,
    ) -> main_models.DescribeInstanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def describe_instance_for_isv_with_options(
        self,
        request: main_models.DescribeInstanceForIsvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceForIsvResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceForIsv',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceForIsvResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_for_isv_with_options_async(
        self,
        request: main_models.DescribeInstanceForIsvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceForIsvResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceForIsv',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceForIsvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_for_isv(
        self,
        request: main_models.DescribeInstanceForIsvRequest,
    ) -> main_models.DescribeInstanceForIsvResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_for_isv_with_options(request, runtime)

    async def describe_instance_for_isv_async(
        self,
        request: main_models.DescribeInstanceForIsvRequest,
    ) -> main_models.DescribeInstanceForIsvResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_for_isv_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: main_models.DescribeInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.codes):
            query['Codes'] = request.codes
        if not DaraCore.is_null(request.except_codes):
            query['ExceptCodes'] = request.except_codes
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstances',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: main_models.DescribeInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.codes):
            query['Codes'] = request.codes
        if not DaraCore.is_null(request.except_codes):
            query['ExceptCodes'] = request.except_codes
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstances',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instances(
        self,
        request: main_models.DescribeInstancesRequest,
    ) -> main_models.DescribeInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: main_models.DescribeInstancesRequest,
    ) -> main_models.DescribeInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_invoice_for_isv_with_options(
        self,
        request: main_models.DescribeInvoiceForIsvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInvoiceForIsvResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.invoice_id):
            query['InvoiceId'] = request.invoice_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInvoiceForIsv',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInvoiceForIsvResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_invoice_for_isv_with_options_async(
        self,
        request: main_models.DescribeInvoiceForIsvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInvoiceForIsvResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.invoice_id):
            query['InvoiceId'] = request.invoice_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInvoiceForIsv',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInvoiceForIsvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_invoice_for_isv(
        self,
        request: main_models.DescribeInvoiceForIsvRequest,
    ) -> main_models.DescribeInvoiceForIsvResponse:
        runtime = RuntimeOptions()
        return self.describe_invoice_for_isv_with_options(request, runtime)

    async def describe_invoice_for_isv_async(
        self,
        request: main_models.DescribeInvoiceForIsvRequest,
    ) -> main_models.DescribeInvoiceForIsvResponse:
        runtime = RuntimeOptions()
        return await self.describe_invoice_for_isv_with_options_async(request, runtime)

    def describe_license_with_options(
        self,
        request: main_models.DescribeLicenseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLicenseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.license_code):
            query['LicenseCode'] = request.license_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLicense',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_license_with_options_async(
        self,
        request: main_models.DescribeLicenseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLicenseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.license_code):
            query['LicenseCode'] = request.license_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLicense',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_license(
        self,
        request: main_models.DescribeLicenseRequest,
    ) -> main_models.DescribeLicenseResponse:
        runtime = RuntimeOptions()
        return self.describe_license_with_options(request, runtime)

    async def describe_license_async(
        self,
        request: main_models.DescribeLicenseRequest,
    ) -> main_models.DescribeLicenseResponse:
        runtime = RuntimeOptions()
        return await self.describe_license_with_options_async(request, runtime)

    def describe_order_with_options(
        self,
        request: main_models.DescribeOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOrder',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_order_with_options_async(
        self,
        request: main_models.DescribeOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOrder',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_order(
        self,
        request: main_models.DescribeOrderRequest,
    ) -> main_models.DescribeOrderResponse:
        runtime = RuntimeOptions()
        return self.describe_order_with_options(request, runtime)

    async def describe_order_async(
        self,
        request: main_models.DescribeOrderRequest,
    ) -> main_models.DescribeOrderResponse:
        runtime = RuntimeOptions()
        return await self.describe_order_with_options_async(request, runtime)

    def describe_order_for_isv_with_options(
        self,
        request: main_models.DescribeOrderForIsvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOrderForIsvResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOrderForIsv',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOrderForIsvResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_order_for_isv_with_options_async(
        self,
        request: main_models.DescribeOrderForIsvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOrderForIsvResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOrderForIsv',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOrderForIsvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_order_for_isv(
        self,
        request: main_models.DescribeOrderForIsvRequest,
    ) -> main_models.DescribeOrderForIsvResponse:
        runtime = RuntimeOptions()
        return self.describe_order_for_isv_with_options(request, runtime)

    async def describe_order_for_isv_async(
        self,
        request: main_models.DescribeOrderForIsvRequest,
    ) -> main_models.DescribeOrderForIsvResponse:
        runtime = RuntimeOptions()
        return await self.describe_order_for_isv_with_options_async(request, runtime)

    def describe_price_with_options(
        self,
        request: main_models.DescribePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.commodity):
            query['Commodity'] = request.commodity
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrice',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_price_with_options_async(
        self,
        request: main_models.DescribePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.commodity):
            query['Commodity'] = request.commodity
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrice',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_price(
        self,
        request: main_models.DescribePriceRequest,
    ) -> main_models.DescribePriceResponse:
        runtime = RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    async def describe_price_async(
        self,
        request: main_models.DescribePriceRequest,
    ) -> main_models.DescribePriceResponse:
        runtime = RuntimeOptions()
        return await self.describe_price_with_options_async(request, runtime)

    def describe_product_with_options(
        self,
        request: main_models.DescribeProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.query_draft):
            query['QueryDraft'] = request.query_draft
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProduct',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_product_with_options_async(
        self,
        request: main_models.DescribeProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.query_draft):
            query['QueryDraft'] = request.query_draft
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProduct',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_product(
        self,
        request: main_models.DescribeProductRequest,
    ) -> main_models.DescribeProductResponse:
        runtime = RuntimeOptions()
        return self.describe_product_with_options(request, runtime)

    async def describe_product_async(
        self,
        request: main_models.DescribeProductRequest,
    ) -> main_models.DescribeProductResponse:
        runtime = RuntimeOptions()
        return await self.describe_product_with_options_async(request, runtime)

    def describe_products_with_options(
        self,
        request: main_models.DescribeProductsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProductsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_term):
            query['SearchTerm'] = request.search_term
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProducts',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_products_with_options_async(
        self,
        request: main_models.DescribeProductsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProductsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_term):
            query['SearchTerm'] = request.search_term
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProducts',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_products(
        self,
        request: main_models.DescribeProductsRequest,
    ) -> main_models.DescribeProductsResponse:
        runtime = RuntimeOptions()
        return self.describe_products_with_options(request, runtime)

    async def describe_products_async(
        self,
        request: main_models.DescribeProductsRequest,
    ) -> main_models.DescribeProductsResponse:
        runtime = RuntimeOptions()
        return await self.describe_products_with_options_async(request, runtime)

    def describe_project_attachments_with_options(
        self,
        request: main_models.DescribeProjectAttachmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProjectAttachmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProjectAttachments',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProjectAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_project_attachments_with_options_async(
        self,
        request: main_models.DescribeProjectAttachmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProjectAttachmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProjectAttachments',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProjectAttachmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_project_attachments(
        self,
        request: main_models.DescribeProjectAttachmentsRequest,
    ) -> main_models.DescribeProjectAttachmentsResponse:
        runtime = RuntimeOptions()
        return self.describe_project_attachments_with_options(request, runtime)

    async def describe_project_attachments_async(
        self,
        request: main_models.DescribeProjectAttachmentsRequest,
    ) -> main_models.DescribeProjectAttachmentsResponse:
        runtime = RuntimeOptions()
        return await self.describe_project_attachments_with_options_async(request, runtime)

    def describe_project_info_with_options(
        self,
        request: main_models.DescribeProjectInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProjectInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProjectInfo',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProjectInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_project_info_with_options_async(
        self,
        request: main_models.DescribeProjectInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProjectInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProjectInfo',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProjectInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_project_info(
        self,
        request: main_models.DescribeProjectInfoRequest,
    ) -> main_models.DescribeProjectInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_project_info_with_options(request, runtime)

    async def describe_project_info_async(
        self,
        request: main_models.DescribeProjectInfoRequest,
    ) -> main_models.DescribeProjectInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_project_info_with_options_async(request, runtime)

    def describe_project_messages_with_options(
        self,
        request: main_models.DescribeProjectMessagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProjectMessagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProjectMessages',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProjectMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_project_messages_with_options_async(
        self,
        request: main_models.DescribeProjectMessagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProjectMessagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProjectMessages',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProjectMessagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_project_messages(
        self,
        request: main_models.DescribeProjectMessagesRequest,
    ) -> main_models.DescribeProjectMessagesResponse:
        runtime = RuntimeOptions()
        return self.describe_project_messages_with_options(request, runtime)

    async def describe_project_messages_async(
        self,
        request: main_models.DescribeProjectMessagesRequest,
    ) -> main_models.DescribeProjectMessagesResponse:
        runtime = RuntimeOptions()
        return await self.describe_project_messages_with_options_async(request, runtime)

    def describe_project_nodes_with_options(
        self,
        request: main_models.DescribeProjectNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProjectNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProjectNodes',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProjectNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_project_nodes_with_options_async(
        self,
        request: main_models.DescribeProjectNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProjectNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProjectNodes',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProjectNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_project_nodes(
        self,
        request: main_models.DescribeProjectNodesRequest,
    ) -> main_models.DescribeProjectNodesResponse:
        runtime = RuntimeOptions()
        return self.describe_project_nodes_with_options(request, runtime)

    async def describe_project_nodes_async(
        self,
        request: main_models.DescribeProjectNodesRequest,
    ) -> main_models.DescribeProjectNodesResponse:
        runtime = RuntimeOptions()
        return await self.describe_project_nodes_with_options_async(request, runtime)

    def describe_project_operate_logs_with_options(
        self,
        request: main_models.DescribeProjectOperateLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProjectOperateLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProjectOperateLogs',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProjectOperateLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_project_operate_logs_with_options_async(
        self,
        request: main_models.DescribeProjectOperateLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProjectOperateLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProjectOperateLogs',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProjectOperateLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_project_operate_logs(
        self,
        request: main_models.DescribeProjectOperateLogsRequest,
    ) -> main_models.DescribeProjectOperateLogsResponse:
        runtime = RuntimeOptions()
        return self.describe_project_operate_logs_with_options(request, runtime)

    async def describe_project_operate_logs_async(
        self,
        request: main_models.DescribeProjectOperateLogsRequest,
    ) -> main_models.DescribeProjectOperateLogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_project_operate_logs_with_options_async(request, runtime)

    def finish_current_project_node_with_options(
        self,
        request: main_models.FinishCurrentProjectNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FinishCurrentProjectNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.template_form):
            query['TemplateForm'] = request.template_form
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FinishCurrentProjectNode',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FinishCurrentProjectNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def finish_current_project_node_with_options_async(
        self,
        request: main_models.FinishCurrentProjectNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FinishCurrentProjectNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.template_form):
            query['TemplateForm'] = request.template_form
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FinishCurrentProjectNode',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FinishCurrentProjectNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def finish_current_project_node(
        self,
        request: main_models.FinishCurrentProjectNodeRequest,
    ) -> main_models.FinishCurrentProjectNodeResponse:
        runtime = RuntimeOptions()
        return self.finish_current_project_node_with_options(request, runtime)

    async def finish_current_project_node_async(
        self,
        request: main_models.FinishCurrentProjectNodeRequest,
    ) -> main_models.FinishCurrentProjectNodeResponse:
        runtime = RuntimeOptions()
        return await self.finish_current_project_node_with_options_async(request, runtime)

    def modify_invoice_for_isv_with_options(
        self,
        request: main_models.ModifyInvoiceForIsvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInvoiceForIsvResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_notice):
            query['CheckNotice'] = request.check_notice
        if not DaraCore.is_null(request.electron_url):
            query['ElectronUrl'] = request.electron_url
        if not DaraCore.is_null(request.invoice_id):
            query['InvoiceId'] = request.invoice_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInvoiceForIsv',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInvoiceForIsvResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_invoice_for_isv_with_options_async(
        self,
        request: main_models.ModifyInvoiceForIsvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInvoiceForIsvResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_notice):
            query['CheckNotice'] = request.check_notice
        if not DaraCore.is_null(request.electron_url):
            query['ElectronUrl'] = request.electron_url
        if not DaraCore.is_null(request.invoice_id):
            query['InvoiceId'] = request.invoice_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInvoiceForIsv',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInvoiceForIsvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_invoice_for_isv(
        self,
        request: main_models.ModifyInvoiceForIsvRequest,
    ) -> main_models.ModifyInvoiceForIsvResponse:
        runtime = RuntimeOptions()
        return self.modify_invoice_for_isv_with_options(request, runtime)

    async def modify_invoice_for_isv_async(
        self,
        request: main_models.ModifyInvoiceForIsvRequest,
    ) -> main_models.ModifyInvoiceForIsvResponse:
        runtime = RuntimeOptions()
        return await self.modify_invoice_for_isv_with_options_async(request, runtime)

    def pause_project_with_options(
        self,
        request: main_models.PauseProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PauseProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PauseProject',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PauseProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_project_with_options_async(
        self,
        request: main_models.PauseProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PauseProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PauseProject',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PauseProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_project(
        self,
        request: main_models.PauseProjectRequest,
    ) -> main_models.PauseProjectResponse:
        runtime = RuntimeOptions()
        return self.pause_project_with_options(request, runtime)

    async def pause_project_async(
        self,
        request: main_models.PauseProjectRequest,
    ) -> main_models.PauseProjectResponse:
        runtime = RuntimeOptions()
        return await self.pause_project_with_options_async(request, runtime)

    def push_metering_data_with_options(
        self,
        request: main_models.PushMeteringDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushMeteringDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.metering):
            query['Metering'] = request.metering
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushMeteringData',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushMeteringDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_metering_data_with_options_async(
        self,
        request: main_models.PushMeteringDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushMeteringDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.metering):
            query['Metering'] = request.metering
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushMeteringData',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushMeteringDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_metering_data(
        self,
        request: main_models.PushMeteringDataRequest,
    ) -> main_models.PushMeteringDataResponse:
        runtime = RuntimeOptions()
        return self.push_metering_data_with_options(request, runtime)

    async def push_metering_data_async(
        self,
        request: main_models.PushMeteringDataRequest,
    ) -> main_models.PushMeteringDataResponse:
        runtime = RuntimeOptions()
        return await self.push_metering_data_with_options_async(request, runtime)

    def push_times_usage_with_options(
        self,
        request: main_models.PushTimesUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushTimesUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.times):
            query['Times'] = request.times
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushTimesUsage',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushTimesUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_times_usage_with_options_async(
        self,
        request: main_models.PushTimesUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushTimesUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.times):
            query['Times'] = request.times
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushTimesUsage',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushTimesUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_times_usage(
        self,
        request: main_models.PushTimesUsageRequest,
    ) -> main_models.PushTimesUsageResponse:
        runtime = RuntimeOptions()
        return self.push_times_usage_with_options(request, runtime)

    async def push_times_usage_async(
        self,
        request: main_models.PushTimesUsageRequest,
    ) -> main_models.PushTimesUsageResponse:
        runtime = RuntimeOptions()
        return await self.push_times_usage_with_options_async(request, runtime)

    def resume_project_with_options(
        self,
        request: main_models.ResumeProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeProject',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_project_with_options_async(
        self,
        request: main_models.ResumeProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeProject',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_project(
        self,
        request: main_models.ResumeProjectRequest,
    ) -> main_models.ResumeProjectResponse:
        runtime = RuntimeOptions()
        return self.resume_project_with_options(request, runtime)

    async def resume_project_async(
        self,
        request: main_models.ResumeProjectRequest,
    ) -> main_models.ResumeProjectResponse:
        runtime = RuntimeOptions()
        return await self.resume_project_with_options_async(request, runtime)

    def rollback_current_project_node_with_options(
        self,
        request: main_models.RollbackCurrentProjectNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RollbackCurrentProjectNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackCurrentProjectNode',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackCurrentProjectNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_current_project_node_with_options_async(
        self,
        request: main_models.RollbackCurrentProjectNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RollbackCurrentProjectNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackCurrentProjectNode',
            version = '2015-11-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackCurrentProjectNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_current_project_node(
        self,
        request: main_models.RollbackCurrentProjectNodeRequest,
    ) -> main_models.RollbackCurrentProjectNodeResponse:
        runtime = RuntimeOptions()
        return self.rollback_current_project_node_with_options(request, runtime)

    async def rollback_current_project_node_async(
        self,
        request: main_models.RollbackCurrentProjectNodeRequest,
    ) -> main_models.RollbackCurrentProjectNodeResponse:
        runtime = RuntimeOptions()
        return await self.rollback_current_project_node_with_options_async(request, runtime)
