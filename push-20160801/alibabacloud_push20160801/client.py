# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_push20160801 import models as main_models
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
            'ap-northeast-1': 'cloudpush.aliyuncs.com',
            'ap-northeast-2-pop': 'cloudpush.aliyuncs.com',
            'ap-south-1': 'cloudpush.aliyuncs.com',
            'ap-southeast-1': 'cloudpush.aliyuncs.com',
            'ap-southeast-2': 'cloudpush.aliyuncs.com',
            'ap-southeast-3': 'cloudpush.aliyuncs.com',
            'ap-southeast-5': 'cloudpush.aliyuncs.com',
            'cn-beijing': 'cloudpush.aliyuncs.com',
            'cn-beijing-finance-1': 'cloudpush.aliyuncs.com',
            'cn-beijing-finance-pop': 'cloudpush.aliyuncs.com',
            'cn-beijing-gov-1': 'cloudpush.aliyuncs.com',
            'cn-beijing-nu16-b01': 'cloudpush.aliyuncs.com',
            'cn-chengdu': 'cloudpush.aliyuncs.com',
            'cn-edge-1': 'cloudpush.aliyuncs.com',
            'cn-fujian': 'cloudpush.aliyuncs.com',
            'cn-haidian-cm12-c01': 'cloudpush.aliyuncs.com',
            'cn-hangzhou': 'cloudpush.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'cloudpush.aliyuncs.com',
            'cn-hangzhou-finance': 'cloudpush.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'cloudpush.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'cloudpush.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'cloudpush.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'cloudpush.aliyuncs.com',
            'cn-hangzhou-test-306': 'cloudpush.aliyuncs.com',
            'cn-hongkong': 'cloudpush.aliyuncs.com',
            'cn-hongkong-finance-pop': 'cloudpush.aliyuncs.com',
            'cn-huhehaote': 'cloudpush.aliyuncs.com',
            'cn-north-2-gov-1': 'cloudpush.aliyuncs.com',
            'cn-qingdao': 'cloudpush.aliyuncs.com',
            'cn-qingdao-nebula': 'cloudpush.aliyuncs.com',
            'cn-shanghai': 'cloudpush.aliyuncs.com',
            'cn-shanghai-et15-b01': 'cloudpush.aliyuncs.com',
            'cn-shanghai-et2-b01': 'cloudpush.aliyuncs.com',
            'cn-shanghai-finance-1': 'cloudpush.aliyuncs.com',
            'cn-shanghai-inner': 'cloudpush.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'cloudpush.aliyuncs.com',
            'cn-shenzhen': 'cloudpush.aliyuncs.com',
            'cn-shenzhen-finance-1': 'cloudpush.aliyuncs.com',
            'cn-shenzhen-inner': 'cloudpush.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'cloudpush.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'cloudpush.aliyuncs.com',
            'cn-wuhan': 'cloudpush.aliyuncs.com',
            'cn-yushanfang': 'cloudpush.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'cloudpush.aliyuncs.com',
            'cn-zhangjiakou': 'cloudpush.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'cloudpush.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'cloudpush.aliyuncs.com',
            'eu-central-1': 'cloudpush.aliyuncs.com',
            'eu-west-1': 'cloudpush.aliyuncs.com',
            'eu-west-1-oxs': 'cloudpush.aliyuncs.com',
            'me-east-1': 'cloudpush.aliyuncs.com',
            'rus-west-1-pop': 'cloudpush.aliyuncs.com',
            'us-east-1': 'cloudpush.aliyuncs.com',
            'us-west-1': 'cloudpush.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('push', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def bind_alias_with_options(
        self,
        request: main_models.BindAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAliasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias_name):
            query['AliasName'] = request.alias_name
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAlias',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_alias_with_options_async(
        self,
        request: main_models.BindAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAliasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias_name):
            query['AliasName'] = request.alias_name
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAlias',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_alias(
        self,
        request: main_models.BindAliasRequest,
    ) -> main_models.BindAliasResponse:
        runtime = RuntimeOptions()
        return self.bind_alias_with_options(request, runtime)

    async def bind_alias_async(
        self,
        request: main_models.BindAliasRequest,
    ) -> main_models.BindAliasResponse:
        runtime = RuntimeOptions()
        return await self.bind_alias_with_options_async(request, runtime)

    def bind_phone_with_options(
        self,
        request: main_models.BindPhoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindPhoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindPhone',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindPhoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_phone_with_options_async(
        self,
        request: main_models.BindPhoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindPhoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindPhone',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindPhoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_phone(
        self,
        request: main_models.BindPhoneRequest,
    ) -> main_models.BindPhoneResponse:
        runtime = RuntimeOptions()
        return self.bind_phone_with_options(request, runtime)

    async def bind_phone_async(
        self,
        request: main_models.BindPhoneRequest,
    ) -> main_models.BindPhoneResponse:
        runtime = RuntimeOptions()
        return await self.bind_phone_with_options_async(request, runtime)

    def bind_tag_with_options(
        self,
        request: main_models.BindTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.client_key):
            query['ClientKey'] = request.client_key
        if not DaraCore.is_null(request.key_type):
            query['KeyType'] = request.key_type
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindTag',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_tag_with_options_async(
        self,
        request: main_models.BindTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.client_key):
            query['ClientKey'] = request.client_key
        if not DaraCore.is_null(request.key_type):
            query['KeyType'] = request.key_type
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindTag',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_tag(
        self,
        request: main_models.BindTagRequest,
    ) -> main_models.BindTagResponse:
        runtime = RuntimeOptions()
        return self.bind_tag_with_options(request, runtime)

    async def bind_tag_async(
        self,
        request: main_models.BindTagRequest,
    ) -> main_models.BindTagResponse:
        runtime = RuntimeOptions()
        return await self.bind_tag_with_options_async(request, runtime)

    def cancel_push_with_options(
        self,
        request: main_models.CancelPushRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelPushResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelPush',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelPushResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_push_with_options_async(
        self,
        request: main_models.CancelPushRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelPushResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelPush',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelPushResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_push(
        self,
        request: main_models.CancelPushRequest,
    ) -> main_models.CancelPushResponse:
        runtime = RuntimeOptions()
        return self.cancel_push_with_options(request, runtime)

    async def cancel_push_async(
        self,
        request: main_models.CancelPushRequest,
    ) -> main_models.CancelPushResponse:
        runtime = RuntimeOptions()
        return await self.cancel_push_with_options_async(request, runtime)

    def check_certificate_with_options(
        self,
        request: main_models.CheckCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckCertificate',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_certificate_with_options_async(
        self,
        request: main_models.CheckCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckCertificate',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_certificate(
        self,
        request: main_models.CheckCertificateRequest,
    ) -> main_models.CheckCertificateResponse:
        runtime = RuntimeOptions()
        return self.check_certificate_with_options(request, runtime)

    async def check_certificate_async(
        self,
        request: main_models.CheckCertificateRequest,
    ) -> main_models.CheckCertificateResponse:
        runtime = RuntimeOptions()
        return await self.check_certificate_with_options_async(request, runtime)

    def check_device_with_options(
        self,
        request: main_models.CheckDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDevice',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_device_with_options_async(
        self,
        request: main_models.CheckDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDevice',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_device(
        self,
        request: main_models.CheckDeviceRequest,
    ) -> main_models.CheckDeviceResponse:
        runtime = RuntimeOptions()
        return self.check_device_with_options(request, runtime)

    async def check_device_async(
        self,
        request: main_models.CheckDeviceRequest,
    ) -> main_models.CheckDeviceResponse:
        runtime = RuntimeOptions()
        return await self.check_device_with_options_async(request, runtime)

    def check_devices_with_options(
        self,
        request: main_models.CheckDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.device_ids):
            query['DeviceIds'] = request.device_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDevices',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_devices_with_options_async(
        self,
        request: main_models.CheckDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.device_ids):
            query['DeviceIds'] = request.device_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDevices',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_devices(
        self,
        request: main_models.CheckDevicesRequest,
    ) -> main_models.CheckDevicesResponse:
        runtime = RuntimeOptions()
        return self.check_devices_with_options(request, runtime)

    async def check_devices_async(
        self,
        request: main_models.CheckDevicesRequest,
    ) -> main_models.CheckDevicesResponse:
        runtime = RuntimeOptions()
        return await self.check_devices_with_options_async(request, runtime)

    def complete_continuously_push_with_options(
        self,
        request: main_models.CompleteContinuouslyPushRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompleteContinuouslyPushResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CompleteContinuouslyPush',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompleteContinuouslyPushResponse(),
            self.call_api(params, req, runtime)
        )

    async def complete_continuously_push_with_options_async(
        self,
        request: main_models.CompleteContinuouslyPushRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompleteContinuouslyPushResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CompleteContinuouslyPush',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompleteContinuouslyPushResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def complete_continuously_push(
        self,
        request: main_models.CompleteContinuouslyPushRequest,
    ) -> main_models.CompleteContinuouslyPushResponse:
        runtime = RuntimeOptions()
        return self.complete_continuously_push_with_options(request, runtime)

    async def complete_continuously_push_async(
        self,
        request: main_models.CompleteContinuouslyPushRequest,
    ) -> main_models.CompleteContinuouslyPushResponse:
        runtime = RuntimeOptions()
        return await self.complete_continuously_push_with_options_async(request, runtime)

    def continuously_push_with_options(
        self,
        request: main_models.ContinuouslyPushRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ContinuouslyPushResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        if not DaraCore.is_null(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ContinuouslyPush',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContinuouslyPushResponse(),
            self.call_api(params, req, runtime)
        )

    async def continuously_push_with_options_async(
        self,
        request: main_models.ContinuouslyPushRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ContinuouslyPushResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        if not DaraCore.is_null(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ContinuouslyPush',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContinuouslyPushResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def continuously_push(
        self,
        request: main_models.ContinuouslyPushRequest,
    ) -> main_models.ContinuouslyPushResponse:
        runtime = RuntimeOptions()
        return self.continuously_push_with_options(request, runtime)

    async def continuously_push_async(
        self,
        request: main_models.ContinuouslyPushRequest,
    ) -> main_models.ContinuouslyPushResponse:
        runtime = RuntimeOptions()
        return await self.continuously_push_with_options_async(request, runtime)

    def list_summary_apps_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListSummaryAppsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListSummaryApps',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSummaryAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_summary_apps_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListSummaryAppsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListSummaryApps',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSummaryAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_summary_apps(self) -> main_models.ListSummaryAppsResponse:
        runtime = RuntimeOptions()
        return self.list_summary_apps_with_options(runtime)

    async def list_summary_apps_async(self) -> main_models.ListSummaryAppsResponse:
        runtime = RuntimeOptions()
        return await self.list_summary_apps_with_options_async(runtime)

    def list_tags_with_options(
        self,
        request: main_models.ListTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTags',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tags_with_options_async(
        self,
        request: main_models.ListTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTags',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tags(
        self,
        request: main_models.ListTagsRequest,
    ) -> main_models.ListTagsResponse:
        runtime = RuntimeOptions()
        return self.list_tags_with_options(request, runtime)

    async def list_tags_async(
        self,
        request: main_models.ListTagsRequest,
    ) -> main_models.ListTagsResponse:
        runtime = RuntimeOptions()
        return await self.list_tags_with_options_async(request, runtime)

    def mass_push_with_options(
        self,
        request: main_models.MassPushRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MassPushResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.idempotent_token):
            query['IdempotentToken'] = request.idempotent_token
        body = {}
        if not DaraCore.is_null(request.push_task):
            body['PushTask'] = request.push_task
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MassPush',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MassPushResponse(),
            self.call_api(params, req, runtime)
        )

    async def mass_push_with_options_async(
        self,
        request: main_models.MassPushRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MassPushResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.idempotent_token):
            query['IdempotentToken'] = request.idempotent_token
        body = {}
        if not DaraCore.is_null(request.push_task):
            body['PushTask'] = request.push_task
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MassPush',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MassPushResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mass_push(
        self,
        request: main_models.MassPushRequest,
    ) -> main_models.MassPushResponse:
        runtime = RuntimeOptions()
        return self.mass_push_with_options(request, runtime)

    async def mass_push_async(
        self,
        request: main_models.MassPushRequest,
    ) -> main_models.MassPushResponse:
        runtime = RuntimeOptions()
        return await self.mass_push_with_options_async(request, runtime)

    def mass_push_v2with_options(
        self,
        tmp_req: main_models.MassPushV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.MassPushV2Response:
        tmp_req.validate()
        request = main_models.MassPushV2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.push_tasks):
            request.push_tasks_shrink = Utils.array_to_string_with_specified_style(tmp_req.push_tasks, 'PushTasks', 'json')
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.idempotent_token):
            query['IdempotentToken'] = request.idempotent_token
        if not DaraCore.is_null(request.push_tasks_shrink):
            query['PushTasks'] = request.push_tasks_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MassPushV2',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MassPushV2Response(),
            self.call_api(params, req, runtime)
        )

    async def mass_push_v2with_options_async(
        self,
        tmp_req: main_models.MassPushV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.MassPushV2Response:
        tmp_req.validate()
        request = main_models.MassPushV2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.push_tasks):
            request.push_tasks_shrink = Utils.array_to_string_with_specified_style(tmp_req.push_tasks, 'PushTasks', 'json')
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.idempotent_token):
            query['IdempotentToken'] = request.idempotent_token
        if not DaraCore.is_null(request.push_tasks_shrink):
            query['PushTasks'] = request.push_tasks_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MassPushV2',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MassPushV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def mass_push_v2(
        self,
        request: main_models.MassPushV2Request,
    ) -> main_models.MassPushV2Response:
        runtime = RuntimeOptions()
        return self.mass_push_v2with_options(request, runtime)

    async def mass_push_v2_async(
        self,
        request: main_models.MassPushV2Request,
    ) -> main_models.MassPushV2Response:
        runtime = RuntimeOptions()
        return await self.mass_push_v2with_options_async(request, runtime)

    def push_with_options(
        self,
        tmp_req: main_models.PushRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushResponse:
        tmp_req.validate()
        request = main_models.PushShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.android_oppo_private_content_parameters):
            request.android_oppo_private_content_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_oppo_private_content_parameters, 'AndroidOppoPrivateContentParameters', 'json')
        if not DaraCore.is_null(tmp_req.android_oppo_private_title_parameters):
            request.android_oppo_private_title_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_oppo_private_title_parameters, 'AndroidOppoPrivateTitleParameters', 'json')
        query = {}
        if not DaraCore.is_null(request.android_activity):
            query['AndroidActivity'] = request.android_activity
        if not DaraCore.is_null(request.android_badge_add_num):
            query['AndroidBadgeAddNum'] = request.android_badge_add_num
        if not DaraCore.is_null(request.android_badge_class):
            query['AndroidBadgeClass'] = request.android_badge_class
        if not DaraCore.is_null(request.android_badge_set_num):
            query['AndroidBadgeSetNum'] = request.android_badge_set_num
        if not DaraCore.is_null(request.android_big_body):
            query['AndroidBigBody'] = request.android_big_body
        if not DaraCore.is_null(request.android_big_picture_url):
            query['AndroidBigPictureUrl'] = request.android_big_picture_url
        if not DaraCore.is_null(request.android_big_title):
            query['AndroidBigTitle'] = request.android_big_title
        if not DaraCore.is_null(request.android_ext_parameters):
            query['AndroidExtParameters'] = request.android_ext_parameters
        if not DaraCore.is_null(request.android_honor_target_user_type):
            query['AndroidHonorTargetUserType'] = request.android_honor_target_user_type
        if not DaraCore.is_null(request.android_huawei_live_notification_payload):
            query['AndroidHuaweiLiveNotificationPayload'] = request.android_huawei_live_notification_payload
        if not DaraCore.is_null(request.android_huawei_receipt_id):
            query['AndroidHuaweiReceiptId'] = request.android_huawei_receipt_id
        if not DaraCore.is_null(request.android_huawei_target_user_type):
            query['AndroidHuaweiTargetUserType'] = request.android_huawei_target_user_type
        if not DaraCore.is_null(request.android_image_url):
            query['AndroidImageUrl'] = request.android_image_url
        if not DaraCore.is_null(request.android_inbox_body):
            query['AndroidInboxBody'] = request.android_inbox_body
        if not DaraCore.is_null(request.android_meizu_notice_msg_type):
            query['AndroidMeizuNoticeMsgType'] = request.android_meizu_notice_msg_type
        if not DaraCore.is_null(request.android_message_huawei_category):
            query['AndroidMessageHuaweiCategory'] = request.android_message_huawei_category
        if not DaraCore.is_null(request.android_message_huawei_urgency):
            query['AndroidMessageHuaweiUrgency'] = request.android_message_huawei_urgency
        if not DaraCore.is_null(request.android_message_oppo_category):
            query['AndroidMessageOppoCategory'] = request.android_message_oppo_category
        if not DaraCore.is_null(request.android_message_oppo_notify_level):
            query['AndroidMessageOppoNotifyLevel'] = request.android_message_oppo_notify_level
        if not DaraCore.is_null(request.android_message_vivo_category):
            query['AndroidMessageVivoCategory'] = request.android_message_vivo_category
        if not DaraCore.is_null(request.android_music):
            query['AndroidMusic'] = request.android_music
        if not DaraCore.is_null(request.android_notification_bar_priority):
            query['AndroidNotificationBarPriority'] = request.android_notification_bar_priority
        if not DaraCore.is_null(request.android_notification_bar_type):
            query['AndroidNotificationBarType'] = request.android_notification_bar_type
        if not DaraCore.is_null(request.android_notification_channel):
            query['AndroidNotificationChannel'] = request.android_notification_channel
        if not DaraCore.is_null(request.android_notification_group):
            query['AndroidNotificationGroup'] = request.android_notification_group
        if not DaraCore.is_null(request.android_notification_honor_channel):
            query['AndroidNotificationHonorChannel'] = request.android_notification_honor_channel
        if not DaraCore.is_null(request.android_notification_huawei_channel):
            query['AndroidNotificationHuaweiChannel'] = request.android_notification_huawei_channel
        if not DaraCore.is_null(request.android_notification_notify_id):
            query['AndroidNotificationNotifyId'] = request.android_notification_notify_id
        if not DaraCore.is_null(request.android_notification_thread_id):
            query['AndroidNotificationThreadId'] = request.android_notification_thread_id
        if not DaraCore.is_null(request.android_notification_vivo_channel):
            query['AndroidNotificationVivoChannel'] = request.android_notification_vivo_channel
        if not DaraCore.is_null(request.android_notification_xiaomi_channel):
            query['AndroidNotificationXiaomiChannel'] = request.android_notification_xiaomi_channel
        if not DaraCore.is_null(request.android_notify_type):
            query['AndroidNotifyType'] = request.android_notify_type
        if not DaraCore.is_null(request.android_open_type):
            query['AndroidOpenType'] = request.android_open_type
        if not DaraCore.is_null(request.android_open_url):
            query['AndroidOpenUrl'] = request.android_open_url
        if not DaraCore.is_null(request.android_oppo_delete_intent_data):
            query['AndroidOppoDeleteIntentData'] = request.android_oppo_delete_intent_data
        if not DaraCore.is_null(request.android_oppo_intelligent_intent):
            query['AndroidOppoIntelligentIntent'] = request.android_oppo_intelligent_intent
        if not DaraCore.is_null(request.android_oppo_intent_env):
            query['AndroidOppoIntentEnv'] = request.android_oppo_intent_env
        if not DaraCore.is_null(request.android_oppo_private_content_parameters_shrink):
            query['AndroidOppoPrivateContentParameters'] = request.android_oppo_private_content_parameters_shrink
        if not DaraCore.is_null(request.android_oppo_private_msg_template_id):
            query['AndroidOppoPrivateMsgTemplateId'] = request.android_oppo_private_msg_template_id
        if not DaraCore.is_null(request.android_oppo_private_title_parameters_shrink):
            query['AndroidOppoPrivateTitleParameters'] = request.android_oppo_private_title_parameters_shrink
        if not DaraCore.is_null(request.android_popup_activity):
            query['AndroidPopupActivity'] = request.android_popup_activity
        if not DaraCore.is_null(request.android_popup_body):
            query['AndroidPopupBody'] = request.android_popup_body
        if not DaraCore.is_null(request.android_popup_title):
            query['AndroidPopupTitle'] = request.android_popup_title
        if not DaraCore.is_null(request.android_remind):
            query['AndroidRemind'] = request.android_remind
        if not DaraCore.is_null(request.android_render_style):
            query['AndroidRenderStyle'] = request.android_render_style
        if not DaraCore.is_null(request.android_target_user_type):
            query['AndroidTargetUserType'] = request.android_target_user_type
        if not DaraCore.is_null(request.android_vivo_push_mode):
            query['AndroidVivoPushMode'] = request.android_vivo_push_mode
        if not DaraCore.is_null(request.android_vivo_receipt_id):
            query['AndroidVivoReceiptId'] = request.android_vivo_receipt_id
        if not DaraCore.is_null(request.android_xiao_mi_activity):
            query['AndroidXiaoMiActivity'] = request.android_xiao_mi_activity
        if not DaraCore.is_null(request.android_xiao_mi_notify_body):
            query['AndroidXiaoMiNotifyBody'] = request.android_xiao_mi_notify_body
        if not DaraCore.is_null(request.android_xiao_mi_notify_title):
            query['AndroidXiaoMiNotifyTitle'] = request.android_xiao_mi_notify_title
        if not DaraCore.is_null(request.android_xiaomi_big_picture_url):
            query['AndroidXiaomiBigPictureUrl'] = request.android_xiaomi_big_picture_url
        if not DaraCore.is_null(request.android_xiaomi_image_url):
            query['AndroidXiaomiImageUrl'] = request.android_xiaomi_image_url
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.body):
            query['Body'] = request.body
        if not DaraCore.is_null(request.device_type):
            query['DeviceType'] = request.device_type
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.harmony_action):
            query['HarmonyAction'] = request.harmony_action
        if not DaraCore.is_null(request.harmony_action_type):
            query['HarmonyActionType'] = request.harmony_action_type
        if not DaraCore.is_null(request.harmony_badge_add_num):
            query['HarmonyBadgeAddNum'] = request.harmony_badge_add_num
        if not DaraCore.is_null(request.harmony_badge_set_num):
            query['HarmonyBadgeSetNum'] = request.harmony_badge_set_num
        if not DaraCore.is_null(request.harmony_category):
            query['HarmonyCategory'] = request.harmony_category
        if not DaraCore.is_null(request.harmony_ext_parameters):
            query['HarmonyExtParameters'] = request.harmony_ext_parameters
        if not DaraCore.is_null(request.harmony_extension_extra_data):
            query['HarmonyExtensionExtraData'] = request.harmony_extension_extra_data
        if not DaraCore.is_null(request.harmony_extension_push):
            query['HarmonyExtensionPush'] = request.harmony_extension_push
        if not DaraCore.is_null(request.harmony_image_url):
            query['HarmonyImageUrl'] = request.harmony_image_url
        if not DaraCore.is_null(request.harmony_inbox_content):
            query['HarmonyInboxContent'] = request.harmony_inbox_content
        if not DaraCore.is_null(request.harmony_live_view_payload):
            query['HarmonyLiveViewPayload'] = request.harmony_live_view_payload
        if not DaraCore.is_null(request.harmony_notification_slot_type):
            query['HarmonyNotificationSlotType'] = request.harmony_notification_slot_type
        if not DaraCore.is_null(request.harmony_notify_id):
            query['HarmonyNotifyId'] = request.harmony_notify_id
        if not DaraCore.is_null(request.harmony_receipt_id):
            query['HarmonyReceiptId'] = request.harmony_receipt_id
        if not DaraCore.is_null(request.harmony_remind):
            query['HarmonyRemind'] = request.harmony_remind
        if not DaraCore.is_null(request.harmony_remind_body):
            query['HarmonyRemindBody'] = request.harmony_remind_body
        if not DaraCore.is_null(request.harmony_remind_title):
            query['HarmonyRemindTitle'] = request.harmony_remind_title
        if not DaraCore.is_null(request.harmony_render_style):
            query['HarmonyRenderStyle'] = request.harmony_render_style
        if not DaraCore.is_null(request.harmony_test_message):
            query['HarmonyTestMessage'] = request.harmony_test_message
        if not DaraCore.is_null(request.harmony_uri):
            query['HarmonyUri'] = request.harmony_uri
        if not DaraCore.is_null(request.idempotent_token):
            query['IdempotentToken'] = request.idempotent_token
        if not DaraCore.is_null(request.job_key):
            query['JobKey'] = request.job_key
        if not DaraCore.is_null(request.push_time):
            query['PushTime'] = request.push_time
        if not DaraCore.is_null(request.push_type):
            query['PushType'] = request.push_type
        if not DaraCore.is_null(request.send_channels):
            query['SendChannels'] = request.send_channels
        if not DaraCore.is_null(request.send_speed):
            query['SendSpeed'] = request.send_speed
        if not DaraCore.is_null(request.sms_delay_secs):
            query['SmsDelaySecs'] = request.sms_delay_secs
        if not DaraCore.is_null(request.sms_params):
            query['SmsParams'] = request.sms_params
        if not DaraCore.is_null(request.sms_send_policy):
            query['SmsSendPolicy'] = request.sms_send_policy
        if not DaraCore.is_null(request.sms_sign_name):
            query['SmsSignName'] = request.sms_sign_name
        if not DaraCore.is_null(request.sms_template_name):
            query['SmsTemplateName'] = request.sms_template_name
        if not DaraCore.is_null(request.store_offline):
            query['StoreOffline'] = request.store_offline
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        if not DaraCore.is_null(request.target_value):
            query['TargetValue'] = request.target_value
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.trim):
            query['Trim'] = request.trim
        if not DaraCore.is_null(request.i_osapns_env):
            query['iOSApnsEnv'] = request.i_osapns_env
        if not DaraCore.is_null(request.i_osbadge):
            query['iOSBadge'] = request.i_osbadge
        if not DaraCore.is_null(request.i_osbadge_auto_increment):
            query['iOSBadgeAutoIncrement'] = request.i_osbadge_auto_increment
        if not DaraCore.is_null(request.i_osext_parameters):
            query['iOSExtParameters'] = request.i_osext_parameters
        if not DaraCore.is_null(request.i_osinterruption_level):
            query['iOSInterruptionLevel'] = request.i_osinterruption_level
        if not DaraCore.is_null(request.i_oslive_activity_attributes):
            query['iOSLiveActivityAttributes'] = request.i_oslive_activity_attributes
        if not DaraCore.is_null(request.i_oslive_activity_attributes_type):
            query['iOSLiveActivityAttributesType'] = request.i_oslive_activity_attributes_type
        if not DaraCore.is_null(request.i_oslive_activity_content_state):
            query['iOSLiveActivityContentState'] = request.i_oslive_activity_content_state
        if not DaraCore.is_null(request.i_oslive_activity_dismissal_date):
            query['iOSLiveActivityDismissalDate'] = request.i_oslive_activity_dismissal_date
        if not DaraCore.is_null(request.i_oslive_activity_event):
            query['iOSLiveActivityEvent'] = request.i_oslive_activity_event
        if not DaraCore.is_null(request.i_oslive_activity_id):
            query['iOSLiveActivityId'] = request.i_oslive_activity_id
        if not DaraCore.is_null(request.i_oslive_activity_stale_date):
            query['iOSLiveActivityStaleDate'] = request.i_oslive_activity_stale_date
        if not DaraCore.is_null(request.i_osmusic):
            query['iOSMusic'] = request.i_osmusic
        if not DaraCore.is_null(request.i_osmutable_content):
            query['iOSMutableContent'] = request.i_osmutable_content
        if not DaraCore.is_null(request.i_osnotification_category):
            query['iOSNotificationCategory'] = request.i_osnotification_category
        if not DaraCore.is_null(request.i_osnotification_collapse_id):
            query['iOSNotificationCollapseId'] = request.i_osnotification_collapse_id
        if not DaraCore.is_null(request.i_osnotification_thread_id):
            query['iOSNotificationThreadId'] = request.i_osnotification_thread_id
        if not DaraCore.is_null(request.i_osrelevance_score):
            query['iOSRelevanceScore'] = request.i_osrelevance_score
        if not DaraCore.is_null(request.i_osremind):
            query['iOSRemind'] = request.i_osremind
        if not DaraCore.is_null(request.i_osremind_body):
            query['iOSRemindBody'] = request.i_osremind_body
        if not DaraCore.is_null(request.i_ossilent_notification):
            query['iOSSilentNotification'] = request.i_ossilent_notification
        if not DaraCore.is_null(request.i_ossubtitle):
            query['iOSSubtitle'] = request.i_ossubtitle
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Push',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_with_options_async(
        self,
        tmp_req: main_models.PushRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushResponse:
        tmp_req.validate()
        request = main_models.PushShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.android_oppo_private_content_parameters):
            request.android_oppo_private_content_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_oppo_private_content_parameters, 'AndroidOppoPrivateContentParameters', 'json')
        if not DaraCore.is_null(tmp_req.android_oppo_private_title_parameters):
            request.android_oppo_private_title_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_oppo_private_title_parameters, 'AndroidOppoPrivateTitleParameters', 'json')
        query = {}
        if not DaraCore.is_null(request.android_activity):
            query['AndroidActivity'] = request.android_activity
        if not DaraCore.is_null(request.android_badge_add_num):
            query['AndroidBadgeAddNum'] = request.android_badge_add_num
        if not DaraCore.is_null(request.android_badge_class):
            query['AndroidBadgeClass'] = request.android_badge_class
        if not DaraCore.is_null(request.android_badge_set_num):
            query['AndroidBadgeSetNum'] = request.android_badge_set_num
        if not DaraCore.is_null(request.android_big_body):
            query['AndroidBigBody'] = request.android_big_body
        if not DaraCore.is_null(request.android_big_picture_url):
            query['AndroidBigPictureUrl'] = request.android_big_picture_url
        if not DaraCore.is_null(request.android_big_title):
            query['AndroidBigTitle'] = request.android_big_title
        if not DaraCore.is_null(request.android_ext_parameters):
            query['AndroidExtParameters'] = request.android_ext_parameters
        if not DaraCore.is_null(request.android_honor_target_user_type):
            query['AndroidHonorTargetUserType'] = request.android_honor_target_user_type
        if not DaraCore.is_null(request.android_huawei_live_notification_payload):
            query['AndroidHuaweiLiveNotificationPayload'] = request.android_huawei_live_notification_payload
        if not DaraCore.is_null(request.android_huawei_receipt_id):
            query['AndroidHuaweiReceiptId'] = request.android_huawei_receipt_id
        if not DaraCore.is_null(request.android_huawei_target_user_type):
            query['AndroidHuaweiTargetUserType'] = request.android_huawei_target_user_type
        if not DaraCore.is_null(request.android_image_url):
            query['AndroidImageUrl'] = request.android_image_url
        if not DaraCore.is_null(request.android_inbox_body):
            query['AndroidInboxBody'] = request.android_inbox_body
        if not DaraCore.is_null(request.android_meizu_notice_msg_type):
            query['AndroidMeizuNoticeMsgType'] = request.android_meizu_notice_msg_type
        if not DaraCore.is_null(request.android_message_huawei_category):
            query['AndroidMessageHuaweiCategory'] = request.android_message_huawei_category
        if not DaraCore.is_null(request.android_message_huawei_urgency):
            query['AndroidMessageHuaweiUrgency'] = request.android_message_huawei_urgency
        if not DaraCore.is_null(request.android_message_oppo_category):
            query['AndroidMessageOppoCategory'] = request.android_message_oppo_category
        if not DaraCore.is_null(request.android_message_oppo_notify_level):
            query['AndroidMessageOppoNotifyLevel'] = request.android_message_oppo_notify_level
        if not DaraCore.is_null(request.android_message_vivo_category):
            query['AndroidMessageVivoCategory'] = request.android_message_vivo_category
        if not DaraCore.is_null(request.android_music):
            query['AndroidMusic'] = request.android_music
        if not DaraCore.is_null(request.android_notification_bar_priority):
            query['AndroidNotificationBarPriority'] = request.android_notification_bar_priority
        if not DaraCore.is_null(request.android_notification_bar_type):
            query['AndroidNotificationBarType'] = request.android_notification_bar_type
        if not DaraCore.is_null(request.android_notification_channel):
            query['AndroidNotificationChannel'] = request.android_notification_channel
        if not DaraCore.is_null(request.android_notification_group):
            query['AndroidNotificationGroup'] = request.android_notification_group
        if not DaraCore.is_null(request.android_notification_honor_channel):
            query['AndroidNotificationHonorChannel'] = request.android_notification_honor_channel
        if not DaraCore.is_null(request.android_notification_huawei_channel):
            query['AndroidNotificationHuaweiChannel'] = request.android_notification_huawei_channel
        if not DaraCore.is_null(request.android_notification_notify_id):
            query['AndroidNotificationNotifyId'] = request.android_notification_notify_id
        if not DaraCore.is_null(request.android_notification_thread_id):
            query['AndroidNotificationThreadId'] = request.android_notification_thread_id
        if not DaraCore.is_null(request.android_notification_vivo_channel):
            query['AndroidNotificationVivoChannel'] = request.android_notification_vivo_channel
        if not DaraCore.is_null(request.android_notification_xiaomi_channel):
            query['AndroidNotificationXiaomiChannel'] = request.android_notification_xiaomi_channel
        if not DaraCore.is_null(request.android_notify_type):
            query['AndroidNotifyType'] = request.android_notify_type
        if not DaraCore.is_null(request.android_open_type):
            query['AndroidOpenType'] = request.android_open_type
        if not DaraCore.is_null(request.android_open_url):
            query['AndroidOpenUrl'] = request.android_open_url
        if not DaraCore.is_null(request.android_oppo_delete_intent_data):
            query['AndroidOppoDeleteIntentData'] = request.android_oppo_delete_intent_data
        if not DaraCore.is_null(request.android_oppo_intelligent_intent):
            query['AndroidOppoIntelligentIntent'] = request.android_oppo_intelligent_intent
        if not DaraCore.is_null(request.android_oppo_intent_env):
            query['AndroidOppoIntentEnv'] = request.android_oppo_intent_env
        if not DaraCore.is_null(request.android_oppo_private_content_parameters_shrink):
            query['AndroidOppoPrivateContentParameters'] = request.android_oppo_private_content_parameters_shrink
        if not DaraCore.is_null(request.android_oppo_private_msg_template_id):
            query['AndroidOppoPrivateMsgTemplateId'] = request.android_oppo_private_msg_template_id
        if not DaraCore.is_null(request.android_oppo_private_title_parameters_shrink):
            query['AndroidOppoPrivateTitleParameters'] = request.android_oppo_private_title_parameters_shrink
        if not DaraCore.is_null(request.android_popup_activity):
            query['AndroidPopupActivity'] = request.android_popup_activity
        if not DaraCore.is_null(request.android_popup_body):
            query['AndroidPopupBody'] = request.android_popup_body
        if not DaraCore.is_null(request.android_popup_title):
            query['AndroidPopupTitle'] = request.android_popup_title
        if not DaraCore.is_null(request.android_remind):
            query['AndroidRemind'] = request.android_remind
        if not DaraCore.is_null(request.android_render_style):
            query['AndroidRenderStyle'] = request.android_render_style
        if not DaraCore.is_null(request.android_target_user_type):
            query['AndroidTargetUserType'] = request.android_target_user_type
        if not DaraCore.is_null(request.android_vivo_push_mode):
            query['AndroidVivoPushMode'] = request.android_vivo_push_mode
        if not DaraCore.is_null(request.android_vivo_receipt_id):
            query['AndroidVivoReceiptId'] = request.android_vivo_receipt_id
        if not DaraCore.is_null(request.android_xiao_mi_activity):
            query['AndroidXiaoMiActivity'] = request.android_xiao_mi_activity
        if not DaraCore.is_null(request.android_xiao_mi_notify_body):
            query['AndroidXiaoMiNotifyBody'] = request.android_xiao_mi_notify_body
        if not DaraCore.is_null(request.android_xiao_mi_notify_title):
            query['AndroidXiaoMiNotifyTitle'] = request.android_xiao_mi_notify_title
        if not DaraCore.is_null(request.android_xiaomi_big_picture_url):
            query['AndroidXiaomiBigPictureUrl'] = request.android_xiaomi_big_picture_url
        if not DaraCore.is_null(request.android_xiaomi_image_url):
            query['AndroidXiaomiImageUrl'] = request.android_xiaomi_image_url
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.body):
            query['Body'] = request.body
        if not DaraCore.is_null(request.device_type):
            query['DeviceType'] = request.device_type
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.harmony_action):
            query['HarmonyAction'] = request.harmony_action
        if not DaraCore.is_null(request.harmony_action_type):
            query['HarmonyActionType'] = request.harmony_action_type
        if not DaraCore.is_null(request.harmony_badge_add_num):
            query['HarmonyBadgeAddNum'] = request.harmony_badge_add_num
        if not DaraCore.is_null(request.harmony_badge_set_num):
            query['HarmonyBadgeSetNum'] = request.harmony_badge_set_num
        if not DaraCore.is_null(request.harmony_category):
            query['HarmonyCategory'] = request.harmony_category
        if not DaraCore.is_null(request.harmony_ext_parameters):
            query['HarmonyExtParameters'] = request.harmony_ext_parameters
        if not DaraCore.is_null(request.harmony_extension_extra_data):
            query['HarmonyExtensionExtraData'] = request.harmony_extension_extra_data
        if not DaraCore.is_null(request.harmony_extension_push):
            query['HarmonyExtensionPush'] = request.harmony_extension_push
        if not DaraCore.is_null(request.harmony_image_url):
            query['HarmonyImageUrl'] = request.harmony_image_url
        if not DaraCore.is_null(request.harmony_inbox_content):
            query['HarmonyInboxContent'] = request.harmony_inbox_content
        if not DaraCore.is_null(request.harmony_live_view_payload):
            query['HarmonyLiveViewPayload'] = request.harmony_live_view_payload
        if not DaraCore.is_null(request.harmony_notification_slot_type):
            query['HarmonyNotificationSlotType'] = request.harmony_notification_slot_type
        if not DaraCore.is_null(request.harmony_notify_id):
            query['HarmonyNotifyId'] = request.harmony_notify_id
        if not DaraCore.is_null(request.harmony_receipt_id):
            query['HarmonyReceiptId'] = request.harmony_receipt_id
        if not DaraCore.is_null(request.harmony_remind):
            query['HarmonyRemind'] = request.harmony_remind
        if not DaraCore.is_null(request.harmony_remind_body):
            query['HarmonyRemindBody'] = request.harmony_remind_body
        if not DaraCore.is_null(request.harmony_remind_title):
            query['HarmonyRemindTitle'] = request.harmony_remind_title
        if not DaraCore.is_null(request.harmony_render_style):
            query['HarmonyRenderStyle'] = request.harmony_render_style
        if not DaraCore.is_null(request.harmony_test_message):
            query['HarmonyTestMessage'] = request.harmony_test_message
        if not DaraCore.is_null(request.harmony_uri):
            query['HarmonyUri'] = request.harmony_uri
        if not DaraCore.is_null(request.idempotent_token):
            query['IdempotentToken'] = request.idempotent_token
        if not DaraCore.is_null(request.job_key):
            query['JobKey'] = request.job_key
        if not DaraCore.is_null(request.push_time):
            query['PushTime'] = request.push_time
        if not DaraCore.is_null(request.push_type):
            query['PushType'] = request.push_type
        if not DaraCore.is_null(request.send_channels):
            query['SendChannels'] = request.send_channels
        if not DaraCore.is_null(request.send_speed):
            query['SendSpeed'] = request.send_speed
        if not DaraCore.is_null(request.sms_delay_secs):
            query['SmsDelaySecs'] = request.sms_delay_secs
        if not DaraCore.is_null(request.sms_params):
            query['SmsParams'] = request.sms_params
        if not DaraCore.is_null(request.sms_send_policy):
            query['SmsSendPolicy'] = request.sms_send_policy
        if not DaraCore.is_null(request.sms_sign_name):
            query['SmsSignName'] = request.sms_sign_name
        if not DaraCore.is_null(request.sms_template_name):
            query['SmsTemplateName'] = request.sms_template_name
        if not DaraCore.is_null(request.store_offline):
            query['StoreOffline'] = request.store_offline
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        if not DaraCore.is_null(request.target_value):
            query['TargetValue'] = request.target_value
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.trim):
            query['Trim'] = request.trim
        if not DaraCore.is_null(request.i_osapns_env):
            query['iOSApnsEnv'] = request.i_osapns_env
        if not DaraCore.is_null(request.i_osbadge):
            query['iOSBadge'] = request.i_osbadge
        if not DaraCore.is_null(request.i_osbadge_auto_increment):
            query['iOSBadgeAutoIncrement'] = request.i_osbadge_auto_increment
        if not DaraCore.is_null(request.i_osext_parameters):
            query['iOSExtParameters'] = request.i_osext_parameters
        if not DaraCore.is_null(request.i_osinterruption_level):
            query['iOSInterruptionLevel'] = request.i_osinterruption_level
        if not DaraCore.is_null(request.i_oslive_activity_attributes):
            query['iOSLiveActivityAttributes'] = request.i_oslive_activity_attributes
        if not DaraCore.is_null(request.i_oslive_activity_attributes_type):
            query['iOSLiveActivityAttributesType'] = request.i_oslive_activity_attributes_type
        if not DaraCore.is_null(request.i_oslive_activity_content_state):
            query['iOSLiveActivityContentState'] = request.i_oslive_activity_content_state
        if not DaraCore.is_null(request.i_oslive_activity_dismissal_date):
            query['iOSLiveActivityDismissalDate'] = request.i_oslive_activity_dismissal_date
        if not DaraCore.is_null(request.i_oslive_activity_event):
            query['iOSLiveActivityEvent'] = request.i_oslive_activity_event
        if not DaraCore.is_null(request.i_oslive_activity_id):
            query['iOSLiveActivityId'] = request.i_oslive_activity_id
        if not DaraCore.is_null(request.i_oslive_activity_stale_date):
            query['iOSLiveActivityStaleDate'] = request.i_oslive_activity_stale_date
        if not DaraCore.is_null(request.i_osmusic):
            query['iOSMusic'] = request.i_osmusic
        if not DaraCore.is_null(request.i_osmutable_content):
            query['iOSMutableContent'] = request.i_osmutable_content
        if not DaraCore.is_null(request.i_osnotification_category):
            query['iOSNotificationCategory'] = request.i_osnotification_category
        if not DaraCore.is_null(request.i_osnotification_collapse_id):
            query['iOSNotificationCollapseId'] = request.i_osnotification_collapse_id
        if not DaraCore.is_null(request.i_osnotification_thread_id):
            query['iOSNotificationThreadId'] = request.i_osnotification_thread_id
        if not DaraCore.is_null(request.i_osrelevance_score):
            query['iOSRelevanceScore'] = request.i_osrelevance_score
        if not DaraCore.is_null(request.i_osremind):
            query['iOSRemind'] = request.i_osremind
        if not DaraCore.is_null(request.i_osremind_body):
            query['iOSRemindBody'] = request.i_osremind_body
        if not DaraCore.is_null(request.i_ossilent_notification):
            query['iOSSilentNotification'] = request.i_ossilent_notification
        if not DaraCore.is_null(request.i_ossubtitle):
            query['iOSSubtitle'] = request.i_ossubtitle
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Push',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push(
        self,
        request: main_models.PushRequest,
    ) -> main_models.PushResponse:
        runtime = RuntimeOptions()
        return self.push_with_options(request, runtime)

    async def push_async(
        self,
        request: main_models.PushRequest,
    ) -> main_models.PushResponse:
        runtime = RuntimeOptions()
        return await self.push_with_options_async(request, runtime)

    def push_message_to_android_with_options(
        self,
        request: main_models.PushMessageToAndroidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushMessageToAndroidResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.body):
            query['Body'] = request.body
        if not DaraCore.is_null(request.job_key):
            query['JobKey'] = request.job_key
        if not DaraCore.is_null(request.store_offline):
            query['StoreOffline'] = request.store_offline
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        if not DaraCore.is_null(request.target_value):
            query['TargetValue'] = request.target_value
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushMessageToAndroid',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushMessageToAndroidResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_message_to_android_with_options_async(
        self,
        request: main_models.PushMessageToAndroidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushMessageToAndroidResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.body):
            query['Body'] = request.body
        if not DaraCore.is_null(request.job_key):
            query['JobKey'] = request.job_key
        if not DaraCore.is_null(request.store_offline):
            query['StoreOffline'] = request.store_offline
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        if not DaraCore.is_null(request.target_value):
            query['TargetValue'] = request.target_value
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushMessageToAndroid',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushMessageToAndroidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_message_to_android(
        self,
        request: main_models.PushMessageToAndroidRequest,
    ) -> main_models.PushMessageToAndroidResponse:
        runtime = RuntimeOptions()
        return self.push_message_to_android_with_options(request, runtime)

    async def push_message_to_android_async(
        self,
        request: main_models.PushMessageToAndroidRequest,
    ) -> main_models.PushMessageToAndroidResponse:
        runtime = RuntimeOptions()
        return await self.push_message_to_android_with_options_async(request, runtime)

    def push_message_toi_oswith_options(
        self,
        request: main_models.PushMessageToiOSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushMessageToiOSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.body):
            query['Body'] = request.body
        if not DaraCore.is_null(request.job_key):
            query['JobKey'] = request.job_key
        if not DaraCore.is_null(request.store_offline):
            query['StoreOffline'] = request.store_offline
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        if not DaraCore.is_null(request.target_value):
            query['TargetValue'] = request.target_value
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushMessageToiOS',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushMessageToiOSResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_message_toi_oswith_options_async(
        self,
        request: main_models.PushMessageToiOSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushMessageToiOSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.body):
            query['Body'] = request.body
        if not DaraCore.is_null(request.job_key):
            query['JobKey'] = request.job_key
        if not DaraCore.is_null(request.store_offline):
            query['StoreOffline'] = request.store_offline
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        if not DaraCore.is_null(request.target_value):
            query['TargetValue'] = request.target_value
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushMessageToiOS',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushMessageToiOSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_message_toi_os(
        self,
        request: main_models.PushMessageToiOSRequest,
    ) -> main_models.PushMessageToiOSResponse:
        runtime = RuntimeOptions()
        return self.push_message_toi_oswith_options(request, runtime)

    async def push_message_toi_os_async(
        self,
        request: main_models.PushMessageToiOSRequest,
    ) -> main_models.PushMessageToiOSResponse:
        runtime = RuntimeOptions()
        return await self.push_message_toi_oswith_options_async(request, runtime)

    def push_notice_to_android_with_options(
        self,
        request: main_models.PushNoticeToAndroidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushNoticeToAndroidResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.body):
            query['Body'] = request.body
        if not DaraCore.is_null(request.ext_parameters):
            query['ExtParameters'] = request.ext_parameters
        if not DaraCore.is_null(request.job_key):
            query['JobKey'] = request.job_key
        if not DaraCore.is_null(request.store_offline):
            query['StoreOffline'] = request.store_offline
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        if not DaraCore.is_null(request.target_value):
            query['TargetValue'] = request.target_value
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushNoticeToAndroid',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushNoticeToAndroidResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_notice_to_android_with_options_async(
        self,
        request: main_models.PushNoticeToAndroidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushNoticeToAndroidResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.body):
            query['Body'] = request.body
        if not DaraCore.is_null(request.ext_parameters):
            query['ExtParameters'] = request.ext_parameters
        if not DaraCore.is_null(request.job_key):
            query['JobKey'] = request.job_key
        if not DaraCore.is_null(request.store_offline):
            query['StoreOffline'] = request.store_offline
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        if not DaraCore.is_null(request.target_value):
            query['TargetValue'] = request.target_value
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushNoticeToAndroid',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushNoticeToAndroidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_notice_to_android(
        self,
        request: main_models.PushNoticeToAndroidRequest,
    ) -> main_models.PushNoticeToAndroidResponse:
        runtime = RuntimeOptions()
        return self.push_notice_to_android_with_options(request, runtime)

    async def push_notice_to_android_async(
        self,
        request: main_models.PushNoticeToAndroidRequest,
    ) -> main_models.PushNoticeToAndroidResponse:
        runtime = RuntimeOptions()
        return await self.push_notice_to_android_with_options_async(request, runtime)

    def push_notice_toi_oswith_options(
        self,
        request: main_models.PushNoticeToiOSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushNoticeToiOSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apns_env):
            query['ApnsEnv'] = request.apns_env
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.body):
            query['Body'] = request.body
        if not DaraCore.is_null(request.ext_parameters):
            query['ExtParameters'] = request.ext_parameters
        if not DaraCore.is_null(request.job_key):
            query['JobKey'] = request.job_key
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        if not DaraCore.is_null(request.target_value):
            query['TargetValue'] = request.target_value
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushNoticeToiOS',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushNoticeToiOSResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_notice_toi_oswith_options_async(
        self,
        request: main_models.PushNoticeToiOSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushNoticeToiOSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apns_env):
            query['ApnsEnv'] = request.apns_env
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.body):
            query['Body'] = request.body
        if not DaraCore.is_null(request.ext_parameters):
            query['ExtParameters'] = request.ext_parameters
        if not DaraCore.is_null(request.job_key):
            query['JobKey'] = request.job_key
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        if not DaraCore.is_null(request.target_value):
            query['TargetValue'] = request.target_value
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushNoticeToiOS',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushNoticeToiOSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_notice_toi_os(
        self,
        request: main_models.PushNoticeToiOSRequest,
    ) -> main_models.PushNoticeToiOSResponse:
        runtime = RuntimeOptions()
        return self.push_notice_toi_oswith_options(request, runtime)

    async def push_notice_toi_os_async(
        self,
        request: main_models.PushNoticeToiOSRequest,
    ) -> main_models.PushNoticeToiOSResponse:
        runtime = RuntimeOptions()
        return await self.push_notice_toi_oswith_options_async(request, runtime)

    def push_v2with_options(
        self,
        tmp_req: main_models.PushV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.PushV2Response:
        tmp_req.validate()
        request = main_models.PushV2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.push_task):
            request.push_task_shrink = Utils.array_to_string_with_specified_style(tmp_req.push_task, 'PushTask', 'json')
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.idempotent_token):
            query['IdempotentToken'] = request.idempotent_token
        if not DaraCore.is_null(request.push_task_shrink):
            query['PushTask'] = request.push_task_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushV2',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushV2Response(),
            self.call_api(params, req, runtime)
        )

    async def push_v2with_options_async(
        self,
        tmp_req: main_models.PushV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.PushV2Response:
        tmp_req.validate()
        request = main_models.PushV2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.push_task):
            request.push_task_shrink = Utils.array_to_string_with_specified_style(tmp_req.push_task, 'PushTask', 'json')
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.idempotent_token):
            query['IdempotentToken'] = request.idempotent_token
        if not DaraCore.is_null(request.push_task_shrink):
            query['PushTask'] = request.push_task_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushV2',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def push_v2(
        self,
        request: main_models.PushV2Request,
    ) -> main_models.PushV2Response:
        runtime = RuntimeOptions()
        return self.push_v2with_options(request, runtime)

    async def push_v2_async(
        self,
        request: main_models.PushV2Request,
    ) -> main_models.PushV2Response:
        runtime = RuntimeOptions()
        return await self.push_v2with_options_async(request, runtime)

    def query_aliases_with_options(
        self,
        request: main_models.QueryAliasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAliasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAliases',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAliasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_aliases_with_options_async(
        self,
        request: main_models.QueryAliasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAliasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAliases',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAliasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_aliases(
        self,
        request: main_models.QueryAliasesRequest,
    ) -> main_models.QueryAliasesResponse:
        runtime = RuntimeOptions()
        return self.query_aliases_with_options(request, runtime)

    async def query_aliases_async(
        self,
        request: main_models.QueryAliasesRequest,
    ) -> main_models.QueryAliasesResponse:
        runtime = RuntimeOptions()
        return await self.query_aliases_with_options_async(request, runtime)

    def query_device_info_with_options(
        self,
        request: main_models.QueryDeviceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDeviceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDeviceInfo',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_info_with_options_async(
        self,
        request: main_models.QueryDeviceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDeviceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDeviceInfo',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_device_info(
        self,
        request: main_models.QueryDeviceInfoRequest,
    ) -> main_models.QueryDeviceInfoResponse:
        runtime = RuntimeOptions()
        return self.query_device_info_with_options(request, runtime)

    async def query_device_info_async(
        self,
        request: main_models.QueryDeviceInfoRequest,
    ) -> main_models.QueryDeviceInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_device_info_with_options_async(request, runtime)

    def query_device_stat_with_options(
        self,
        request: main_models.QueryDeviceStatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDeviceStatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.device_type):
            query['DeviceType'] = request.device_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDeviceStat',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDeviceStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_stat_with_options_async(
        self,
        request: main_models.QueryDeviceStatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDeviceStatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.device_type):
            query['DeviceType'] = request.device_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDeviceStat',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDeviceStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_device_stat(
        self,
        request: main_models.QueryDeviceStatRequest,
    ) -> main_models.QueryDeviceStatResponse:
        runtime = RuntimeOptions()
        return self.query_device_stat_with_options(request, runtime)

    async def query_device_stat_async(
        self,
        request: main_models.QueryDeviceStatRequest,
    ) -> main_models.QueryDeviceStatResponse:
        runtime = RuntimeOptions()
        return await self.query_device_stat_with_options_async(request, runtime)

    def query_devices_by_account_with_options(
        self,
        request: main_models.QueryDevicesByAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDevicesByAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDevicesByAccount',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDevicesByAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_devices_by_account_with_options_async(
        self,
        request: main_models.QueryDevicesByAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDevicesByAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDevicesByAccount',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDevicesByAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_devices_by_account(
        self,
        request: main_models.QueryDevicesByAccountRequest,
    ) -> main_models.QueryDevicesByAccountResponse:
        runtime = RuntimeOptions()
        return self.query_devices_by_account_with_options(request, runtime)

    async def query_devices_by_account_async(
        self,
        request: main_models.QueryDevicesByAccountRequest,
    ) -> main_models.QueryDevicesByAccountResponse:
        runtime = RuntimeOptions()
        return await self.query_devices_by_account_with_options_async(request, runtime)

    def query_devices_by_alias_with_options(
        self,
        request: main_models.QueryDevicesByAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDevicesByAliasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias):
            query['Alias'] = request.alias
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDevicesByAlias',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDevicesByAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_devices_by_alias_with_options_async(
        self,
        request: main_models.QueryDevicesByAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDevicesByAliasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias):
            query['Alias'] = request.alias
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDevicesByAlias',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDevicesByAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_devices_by_alias(
        self,
        request: main_models.QueryDevicesByAliasRequest,
    ) -> main_models.QueryDevicesByAliasResponse:
        runtime = RuntimeOptions()
        return self.query_devices_by_alias_with_options(request, runtime)

    async def query_devices_by_alias_async(
        self,
        request: main_models.QueryDevicesByAliasRequest,
    ) -> main_models.QueryDevicesByAliasResponse:
        runtime = RuntimeOptions()
        return await self.query_devices_by_alias_with_options_async(request, runtime)

    def query_push_records_with_options(
        self,
        request: main_models.QueryPushRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPushRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.push_type):
            query['PushType'] = request.push_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPushRecords',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPushRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_push_records_with_options_async(
        self,
        request: main_models.QueryPushRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPushRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.push_type):
            query['PushType'] = request.push_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPushRecords',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPushRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_push_records(
        self,
        request: main_models.QueryPushRecordsRequest,
    ) -> main_models.QueryPushRecordsResponse:
        runtime = RuntimeOptions()
        return self.query_push_records_with_options(request, runtime)

    async def query_push_records_async(
        self,
        request: main_models.QueryPushRecordsRequest,
    ) -> main_models.QueryPushRecordsResponse:
        runtime = RuntimeOptions()
        return await self.query_push_records_with_options_async(request, runtime)

    def query_push_stat_by_app_with_options(
        self,
        request: main_models.QueryPushStatByAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPushStatByAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPushStatByApp',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPushStatByAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_push_stat_by_app_with_options_async(
        self,
        request: main_models.QueryPushStatByAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPushStatByAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPushStatByApp',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPushStatByAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_push_stat_by_app(
        self,
        request: main_models.QueryPushStatByAppRequest,
    ) -> main_models.QueryPushStatByAppResponse:
        runtime = RuntimeOptions()
        return self.query_push_stat_by_app_with_options(request, runtime)

    async def query_push_stat_by_app_async(
        self,
        request: main_models.QueryPushStatByAppRequest,
    ) -> main_models.QueryPushStatByAppResponse:
        runtime = RuntimeOptions()
        return await self.query_push_stat_by_app_with_options_async(request, runtime)

    def query_push_stat_by_msg_with_options(
        self,
        request: main_models.QueryPushStatByMsgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPushStatByMsgResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPushStatByMsg',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPushStatByMsgResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_push_stat_by_msg_with_options_async(
        self,
        request: main_models.QueryPushStatByMsgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPushStatByMsgResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPushStatByMsg',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPushStatByMsgResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_push_stat_by_msg(
        self,
        request: main_models.QueryPushStatByMsgRequest,
    ) -> main_models.QueryPushStatByMsgResponse:
        runtime = RuntimeOptions()
        return self.query_push_stat_by_msg_with_options(request, runtime)

    async def query_push_stat_by_msg_async(
        self,
        request: main_models.QueryPushStatByMsgRequest,
    ) -> main_models.QueryPushStatByMsgResponse:
        runtime = RuntimeOptions()
        return await self.query_push_stat_by_msg_with_options_async(request, runtime)

    def query_tags_with_options(
        self,
        request: main_models.QueryTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.client_key):
            query['ClientKey'] = request.client_key
        if not DaraCore.is_null(request.key_type):
            query['KeyType'] = request.key_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTags',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tags_with_options_async(
        self,
        request: main_models.QueryTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.client_key):
            query['ClientKey'] = request.client_key
        if not DaraCore.is_null(request.key_type):
            query['KeyType'] = request.key_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTags',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_tags(
        self,
        request: main_models.QueryTagsRequest,
    ) -> main_models.QueryTagsResponse:
        runtime = RuntimeOptions()
        return self.query_tags_with_options(request, runtime)

    async def query_tags_async(
        self,
        request: main_models.QueryTagsRequest,
    ) -> main_models.QueryTagsResponse:
        runtime = RuntimeOptions()
        return await self.query_tags_with_options_async(request, runtime)

    def query_unique_device_stat_with_options(
        self,
        request: main_models.QueryUniqueDeviceStatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUniqueDeviceStatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUniqueDeviceStat',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUniqueDeviceStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_unique_device_stat_with_options_async(
        self,
        request: main_models.QueryUniqueDeviceStatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUniqueDeviceStatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUniqueDeviceStat',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUniqueDeviceStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_unique_device_stat(
        self,
        request: main_models.QueryUniqueDeviceStatRequest,
    ) -> main_models.QueryUniqueDeviceStatResponse:
        runtime = RuntimeOptions()
        return self.query_unique_device_stat_with_options(request, runtime)

    async def query_unique_device_stat_async(
        self,
        request: main_models.QueryUniqueDeviceStatRequest,
    ) -> main_models.QueryUniqueDeviceStatResponse:
        runtime = RuntimeOptions()
        return await self.query_unique_device_stat_with_options_async(request, runtime)

    def remove_tag_with_options(
        self,
        request: main_models.RemoveTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveTag',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_tag_with_options_async(
        self,
        request: main_models.RemoveTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveTag',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_tag(
        self,
        request: main_models.RemoveTagRequest,
    ) -> main_models.RemoveTagResponse:
        runtime = RuntimeOptions()
        return self.remove_tag_with_options(request, runtime)

    async def remove_tag_async(
        self,
        request: main_models.RemoveTagRequest,
    ) -> main_models.RemoveTagResponse:
        runtime = RuntimeOptions()
        return await self.remove_tag_with_options_async(request, runtime)

    def unbind_alias_with_options(
        self,
        request: main_models.UnbindAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindAliasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias_name):
            query['AliasName'] = request.alias_name
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.unbind_all):
            query['UnbindAll'] = request.unbind_all
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindAlias',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_alias_with_options_async(
        self,
        request: main_models.UnbindAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindAliasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias_name):
            query['AliasName'] = request.alias_name
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.unbind_all):
            query['UnbindAll'] = request.unbind_all
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindAlias',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_alias(
        self,
        request: main_models.UnbindAliasRequest,
    ) -> main_models.UnbindAliasResponse:
        runtime = RuntimeOptions()
        return self.unbind_alias_with_options(request, runtime)

    async def unbind_alias_async(
        self,
        request: main_models.UnbindAliasRequest,
    ) -> main_models.UnbindAliasResponse:
        runtime = RuntimeOptions()
        return await self.unbind_alias_with_options_async(request, runtime)

    def unbind_phone_with_options(
        self,
        request: main_models.UnbindPhoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindPhoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindPhone',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindPhoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_phone_with_options_async(
        self,
        request: main_models.UnbindPhoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindPhoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindPhone',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindPhoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_phone(
        self,
        request: main_models.UnbindPhoneRequest,
    ) -> main_models.UnbindPhoneResponse:
        runtime = RuntimeOptions()
        return self.unbind_phone_with_options(request, runtime)

    async def unbind_phone_async(
        self,
        request: main_models.UnbindPhoneRequest,
    ) -> main_models.UnbindPhoneResponse:
        runtime = RuntimeOptions()
        return await self.unbind_phone_with_options_async(request, runtime)

    def unbind_tag_with_options(
        self,
        request: main_models.UnbindTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.client_key):
            query['ClientKey'] = request.client_key
        if not DaraCore.is_null(request.key_type):
            query['KeyType'] = request.key_type
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindTag',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_tag_with_options_async(
        self,
        request: main_models.UnbindTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.client_key):
            query['ClientKey'] = request.client_key
        if not DaraCore.is_null(request.key_type):
            query['KeyType'] = request.key_type
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindTag',
            version = '2016-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_tag(
        self,
        request: main_models.UnbindTagRequest,
    ) -> main_models.UnbindTagResponse:
        runtime = RuntimeOptions()
        return self.unbind_tag_with_options(request, runtime)

    async def unbind_tag_async(
        self,
        request: main_models.UnbindTagRequest,
    ) -> main_models.UnbindTagResponse:
        runtime = RuntimeOptions()
        return await self.unbind_tag_with_options_async(request, runtime)
