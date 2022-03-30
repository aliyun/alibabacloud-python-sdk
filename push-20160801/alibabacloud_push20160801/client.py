# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_push20160801 import models as push_20160801_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def bind_alias_with_options(
        self,
        request: push_20160801_models.BindAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.BindAliasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindAlias',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.BindAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_alias_with_options_async(
        self,
        request: push_20160801_models.BindAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.BindAliasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindAlias',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.BindAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_alias(
        self,
        request: push_20160801_models.BindAliasRequest,
    ) -> push_20160801_models.BindAliasResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_alias_with_options(request, runtime)

    async def bind_alias_async(
        self,
        request: push_20160801_models.BindAliasRequest,
    ) -> push_20160801_models.BindAliasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_alias_with_options_async(request, runtime)

    def bind_phone_with_options(
        self,
        request: push_20160801_models.BindPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.BindPhoneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindPhone',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.BindPhoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_phone_with_options_async(
        self,
        request: push_20160801_models.BindPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.BindPhoneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindPhone',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.BindPhoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_phone(
        self,
        request: push_20160801_models.BindPhoneRequest,
    ) -> push_20160801_models.BindPhoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_phone_with_options(request, runtime)

    async def bind_phone_async(
        self,
        request: push_20160801_models.BindPhoneRequest,
    ) -> push_20160801_models.BindPhoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_phone_with_options_async(request, runtime)

    def bind_tag_with_options(
        self,
        request: push_20160801_models.BindTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.BindTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.client_key):
            query['ClientKey'] = request.client_key
        if not UtilClient.is_unset(request.key_type):
            query['KeyType'] = request.key_type
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindTag',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.BindTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_tag_with_options_async(
        self,
        request: push_20160801_models.BindTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.BindTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.client_key):
            query['ClientKey'] = request.client_key
        if not UtilClient.is_unset(request.key_type):
            query['KeyType'] = request.key_type
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindTag',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.BindTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_tag(
        self,
        request: push_20160801_models.BindTagRequest,
    ) -> push_20160801_models.BindTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_tag_with_options(request, runtime)

    async def bind_tag_async(
        self,
        request: push_20160801_models.BindTagRequest,
    ) -> push_20160801_models.BindTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_tag_with_options_async(request, runtime)

    def cancel_push_with_options(
        self,
        request: push_20160801_models.CancelPushRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.CancelPushResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelPush',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.CancelPushResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_push_with_options_async(
        self,
        request: push_20160801_models.CancelPushRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.CancelPushResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelPush',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.CancelPushResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_push(
        self,
        request: push_20160801_models.CancelPushRequest,
    ) -> push_20160801_models.CancelPushResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_push_with_options(request, runtime)

    async def cancel_push_async(
        self,
        request: push_20160801_models.CancelPushRequest,
    ) -> push_20160801_models.CancelPushResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_push_with_options_async(request, runtime)

    def check_certificate_with_options(
        self,
        request: push_20160801_models.CheckCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.CheckCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCertificate',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.CheckCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_certificate_with_options_async(
        self,
        request: push_20160801_models.CheckCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.CheckCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCertificate',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.CheckCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_certificate(
        self,
        request: push_20160801_models.CheckCertificateRequest,
    ) -> push_20160801_models.CheckCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_certificate_with_options(request, runtime)

    async def check_certificate_async(
        self,
        request: push_20160801_models.CheckCertificateRequest,
    ) -> push_20160801_models.CheckCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_certificate_with_options_async(request, runtime)

    def check_device_with_options(
        self,
        request: push_20160801_models.CheckDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.CheckDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDevice',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.CheckDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_device_with_options_async(
        self,
        request: push_20160801_models.CheckDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.CheckDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDevice',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.CheckDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_device(
        self,
        request: push_20160801_models.CheckDeviceRequest,
    ) -> push_20160801_models.CheckDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_device_with_options(request, runtime)

    async def check_device_async(
        self,
        request: push_20160801_models.CheckDeviceRequest,
    ) -> push_20160801_models.CheckDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_device_with_options_async(request, runtime)

    def check_devices_with_options(
        self,
        request: push_20160801_models.CheckDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.CheckDevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_ids):
            query['DeviceIds'] = request.device_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDevices',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.CheckDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_devices_with_options_async(
        self,
        request: push_20160801_models.CheckDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.CheckDevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_ids):
            query['DeviceIds'] = request.device_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDevices',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.CheckDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_devices(
        self,
        request: push_20160801_models.CheckDevicesRequest,
    ) -> push_20160801_models.CheckDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_devices_with_options(request, runtime)

    async def check_devices_async(
        self,
        request: push_20160801_models.CheckDevicesRequest,
    ) -> push_20160801_models.CheckDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_devices_with_options_async(request, runtime)

    def complete_continuously_push_with_options(
        self,
        request: push_20160801_models.CompleteContinuouslyPushRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.CompleteContinuouslyPushResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompleteContinuouslyPush',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.CompleteContinuouslyPushResponse(),
            self.call_api(params, req, runtime)
        )

    async def complete_continuously_push_with_options_async(
        self,
        request: push_20160801_models.CompleteContinuouslyPushRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.CompleteContinuouslyPushResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompleteContinuouslyPush',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.CompleteContinuouslyPushResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def complete_continuously_push(
        self,
        request: push_20160801_models.CompleteContinuouslyPushRequest,
    ) -> push_20160801_models.CompleteContinuouslyPushResponse:
        runtime = util_models.RuntimeOptions()
        return self.complete_continuously_push_with_options(request, runtime)

    async def complete_continuously_push_async(
        self,
        request: push_20160801_models.CompleteContinuouslyPushRequest,
    ) -> push_20160801_models.CompleteContinuouslyPushResponse:
        runtime = util_models.RuntimeOptions()
        return await self.complete_continuously_push_with_options_async(request, runtime)

    def continuously_push_with_options(
        self,
        request: push_20160801_models.ContinuouslyPushRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.ContinuouslyPushResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ContinuouslyPush',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.ContinuouslyPushResponse(),
            self.call_api(params, req, runtime)
        )

    async def continuously_push_with_options_async(
        self,
        request: push_20160801_models.ContinuouslyPushRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.ContinuouslyPushResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ContinuouslyPush',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.ContinuouslyPushResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def continuously_push(
        self,
        request: push_20160801_models.ContinuouslyPushRequest,
    ) -> push_20160801_models.ContinuouslyPushResponse:
        runtime = util_models.RuntimeOptions()
        return self.continuously_push_with_options(request, runtime)

    async def continuously_push_async(
        self,
        request: push_20160801_models.ContinuouslyPushRequest,
    ) -> push_20160801_models.ContinuouslyPushResponse:
        runtime = util_models.RuntimeOptions()
        return await self.continuously_push_with_options_async(request, runtime)

    def list_summary_apps_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.ListSummaryAppsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListSummaryApps',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.ListSummaryAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_summary_apps_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.ListSummaryAppsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListSummaryApps',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.ListSummaryAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_summary_apps(self) -> push_20160801_models.ListSummaryAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_summary_apps_with_options(runtime)

    async def list_summary_apps_async(self) -> push_20160801_models.ListSummaryAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_summary_apps_with_options_async(runtime)

    def list_tags_with_options(
        self,
        request: push_20160801_models.ListTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.ListTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTags',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.ListTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tags_with_options_async(
        self,
        request: push_20160801_models.ListTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.ListTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTags',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.ListTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tags(
        self,
        request: push_20160801_models.ListTagsRequest,
    ) -> push_20160801_models.ListTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tags_with_options(request, runtime)

    async def list_tags_async(
        self,
        request: push_20160801_models.ListTagsRequest,
    ) -> push_20160801_models.ListTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tags_with_options_async(request, runtime)

    def mass_push_with_options(
        self,
        request: push_20160801_models.MassPushRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.MassPushResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        body = {}
        if not UtilClient.is_unset(request.push_task):
            body['PushTask'] = request.push_task
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MassPush',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.MassPushResponse(),
            self.call_api(params, req, runtime)
        )

    async def mass_push_with_options_async(
        self,
        request: push_20160801_models.MassPushRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.MassPushResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        body = {}
        if not UtilClient.is_unset(request.push_task):
            body['PushTask'] = request.push_task
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MassPush',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.MassPushResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mass_push(
        self,
        request: push_20160801_models.MassPushRequest,
    ) -> push_20160801_models.MassPushResponse:
        runtime = util_models.RuntimeOptions()
        return self.mass_push_with_options(request, runtime)

    async def mass_push_async(
        self,
        request: push_20160801_models.MassPushRequest,
    ) -> push_20160801_models.MassPushResponse:
        runtime = util_models.RuntimeOptions()
        return await self.mass_push_with_options_async(request, runtime)

    def push_with_options(
        self,
        request: push_20160801_models.PushRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.PushResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_activity):
            query['AndroidActivity'] = request.android_activity
        if not UtilClient.is_unset(request.android_big_body):
            query['AndroidBigBody'] = request.android_big_body
        if not UtilClient.is_unset(request.android_big_picture_url):
            query['AndroidBigPictureUrl'] = request.android_big_picture_url
        if not UtilClient.is_unset(request.android_big_title):
            query['AndroidBigTitle'] = request.android_big_title
        if not UtilClient.is_unset(request.android_ext_parameters):
            query['AndroidExtParameters'] = request.android_ext_parameters
        if not UtilClient.is_unset(request.android_image_url):
            query['AndroidImageUrl'] = request.android_image_url
        if not UtilClient.is_unset(request.android_inbox_body):
            query['AndroidInboxBody'] = request.android_inbox_body
        if not UtilClient.is_unset(request.android_message_huawei_category):
            query['AndroidMessageHuaweiCategory'] = request.android_message_huawei_category
        if not UtilClient.is_unset(request.android_message_huawei_urgency):
            query['AndroidMessageHuaweiUrgency'] = request.android_message_huawei_urgency
        if not UtilClient.is_unset(request.android_music):
            query['AndroidMusic'] = request.android_music
        if not UtilClient.is_unset(request.android_notification_bar_priority):
            query['AndroidNotificationBarPriority'] = request.android_notification_bar_priority
        if not UtilClient.is_unset(request.android_notification_bar_type):
            query['AndroidNotificationBarType'] = request.android_notification_bar_type
        if not UtilClient.is_unset(request.android_notification_channel):
            query['AndroidNotificationChannel'] = request.android_notification_channel
        if not UtilClient.is_unset(request.android_notification_huawei_channel):
            query['AndroidNotificationHuaweiChannel'] = request.android_notification_huawei_channel
        if not UtilClient.is_unset(request.android_notification_notify_id):
            query['AndroidNotificationNotifyId'] = request.android_notification_notify_id
        if not UtilClient.is_unset(request.android_notification_vivo_channel):
            query['AndroidNotificationVivoChannel'] = request.android_notification_vivo_channel
        if not UtilClient.is_unset(request.android_notification_xiaomi_channel):
            query['AndroidNotificationXiaomiChannel'] = request.android_notification_xiaomi_channel
        if not UtilClient.is_unset(request.android_notify_type):
            query['AndroidNotifyType'] = request.android_notify_type
        if not UtilClient.is_unset(request.android_open_type):
            query['AndroidOpenType'] = request.android_open_type
        if not UtilClient.is_unset(request.android_open_url):
            query['AndroidOpenUrl'] = request.android_open_url
        if not UtilClient.is_unset(request.android_popup_activity):
            query['AndroidPopupActivity'] = request.android_popup_activity
        if not UtilClient.is_unset(request.android_popup_body):
            query['AndroidPopupBody'] = request.android_popup_body
        if not UtilClient.is_unset(request.android_popup_title):
            query['AndroidPopupTitle'] = request.android_popup_title
        if not UtilClient.is_unset(request.android_remind):
            query['AndroidRemind'] = request.android_remind
        if not UtilClient.is_unset(request.android_render_style):
            query['AndroidRenderStyle'] = request.android_render_style
        if not UtilClient.is_unset(request.android_vivo_push_mode):
            query['AndroidVivoPushMode'] = request.android_vivo_push_mode
        if not UtilClient.is_unset(request.android_xiao_mi_activity):
            query['AndroidXiaoMiActivity'] = request.android_xiao_mi_activity
        if not UtilClient.is_unset(request.android_xiao_mi_notify_body):
            query['AndroidXiaoMiNotifyBody'] = request.android_xiao_mi_notify_body
        if not UtilClient.is_unset(request.android_xiao_mi_notify_title):
            query['AndroidXiaoMiNotifyTitle'] = request.android_xiao_mi_notify_title
        if not UtilClient.is_unset(request.android_xiaomi_big_picture_url):
            query['AndroidXiaomiBigPictureUrl'] = request.android_xiaomi_big_picture_url
        if not UtilClient.is_unset(request.android_xiaomi_image_url):
            query['AndroidXiaomiImageUrl'] = request.android_xiaomi_image_url
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.device_type):
            query['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.job_key):
            query['JobKey'] = request.job_key
        if not UtilClient.is_unset(request.push_time):
            query['PushTime'] = request.push_time
        if not UtilClient.is_unset(request.push_type):
            query['PushType'] = request.push_type
        if not UtilClient.is_unset(request.send_channels):
            query['SendChannels'] = request.send_channels
        if not UtilClient.is_unset(request.send_speed):
            query['SendSpeed'] = request.send_speed
        if not UtilClient.is_unset(request.sms_delay_secs):
            query['SmsDelaySecs'] = request.sms_delay_secs
        if not UtilClient.is_unset(request.sms_params):
            query['SmsParams'] = request.sms_params
        if not UtilClient.is_unset(request.sms_send_policy):
            query['SmsSendPolicy'] = request.sms_send_policy
        if not UtilClient.is_unset(request.sms_sign_name):
            query['SmsSignName'] = request.sms_sign_name
        if not UtilClient.is_unset(request.sms_template_name):
            query['SmsTemplateName'] = request.sms_template_name
        if not UtilClient.is_unset(request.store_offline):
            query['StoreOffline'] = request.store_offline
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.trim):
            query['Trim'] = request.trim
        if not UtilClient.is_unset(request.i_osapns_env):
            query['iOSApnsEnv'] = request.i_osapns_env
        if not UtilClient.is_unset(request.i_osbadge):
            query['iOSBadge'] = request.i_osbadge
        if not UtilClient.is_unset(request.i_osbadge_auto_increment):
            query['iOSBadgeAutoIncrement'] = request.i_osbadge_auto_increment
        if not UtilClient.is_unset(request.i_osext_parameters):
            query['iOSExtParameters'] = request.i_osext_parameters
        if not UtilClient.is_unset(request.i_osinterruption_level):
            query['iOSInterruptionLevel'] = request.i_osinterruption_level
        if not UtilClient.is_unset(request.i_osmusic):
            query['iOSMusic'] = request.i_osmusic
        if not UtilClient.is_unset(request.i_osmutable_content):
            query['iOSMutableContent'] = request.i_osmutable_content
        if not UtilClient.is_unset(request.i_osnotification_category):
            query['iOSNotificationCategory'] = request.i_osnotification_category
        if not UtilClient.is_unset(request.i_osnotification_collapse_id):
            query['iOSNotificationCollapseId'] = request.i_osnotification_collapse_id
        if not UtilClient.is_unset(request.i_osnotification_thread_id):
            query['iOSNotificationThreadId'] = request.i_osnotification_thread_id
        if not UtilClient.is_unset(request.i_osrelevance_score):
            query['iOSRelevanceScore'] = request.i_osrelevance_score
        if not UtilClient.is_unset(request.i_osremind):
            query['iOSRemind'] = request.i_osremind
        if not UtilClient.is_unset(request.i_osremind_body):
            query['iOSRemindBody'] = request.i_osremind_body
        if not UtilClient.is_unset(request.i_ossilent_notification):
            query['iOSSilentNotification'] = request.i_ossilent_notification
        if not UtilClient.is_unset(request.i_ossubtitle):
            query['iOSSubtitle'] = request.i_ossubtitle
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Push',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.PushResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_with_options_async(
        self,
        request: push_20160801_models.PushRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.PushResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_activity):
            query['AndroidActivity'] = request.android_activity
        if not UtilClient.is_unset(request.android_big_body):
            query['AndroidBigBody'] = request.android_big_body
        if not UtilClient.is_unset(request.android_big_picture_url):
            query['AndroidBigPictureUrl'] = request.android_big_picture_url
        if not UtilClient.is_unset(request.android_big_title):
            query['AndroidBigTitle'] = request.android_big_title
        if not UtilClient.is_unset(request.android_ext_parameters):
            query['AndroidExtParameters'] = request.android_ext_parameters
        if not UtilClient.is_unset(request.android_image_url):
            query['AndroidImageUrl'] = request.android_image_url
        if not UtilClient.is_unset(request.android_inbox_body):
            query['AndroidInboxBody'] = request.android_inbox_body
        if not UtilClient.is_unset(request.android_message_huawei_category):
            query['AndroidMessageHuaweiCategory'] = request.android_message_huawei_category
        if not UtilClient.is_unset(request.android_message_huawei_urgency):
            query['AndroidMessageHuaweiUrgency'] = request.android_message_huawei_urgency
        if not UtilClient.is_unset(request.android_music):
            query['AndroidMusic'] = request.android_music
        if not UtilClient.is_unset(request.android_notification_bar_priority):
            query['AndroidNotificationBarPriority'] = request.android_notification_bar_priority
        if not UtilClient.is_unset(request.android_notification_bar_type):
            query['AndroidNotificationBarType'] = request.android_notification_bar_type
        if not UtilClient.is_unset(request.android_notification_channel):
            query['AndroidNotificationChannel'] = request.android_notification_channel
        if not UtilClient.is_unset(request.android_notification_huawei_channel):
            query['AndroidNotificationHuaweiChannel'] = request.android_notification_huawei_channel
        if not UtilClient.is_unset(request.android_notification_notify_id):
            query['AndroidNotificationNotifyId'] = request.android_notification_notify_id
        if not UtilClient.is_unset(request.android_notification_vivo_channel):
            query['AndroidNotificationVivoChannel'] = request.android_notification_vivo_channel
        if not UtilClient.is_unset(request.android_notification_xiaomi_channel):
            query['AndroidNotificationXiaomiChannel'] = request.android_notification_xiaomi_channel
        if not UtilClient.is_unset(request.android_notify_type):
            query['AndroidNotifyType'] = request.android_notify_type
        if not UtilClient.is_unset(request.android_open_type):
            query['AndroidOpenType'] = request.android_open_type
        if not UtilClient.is_unset(request.android_open_url):
            query['AndroidOpenUrl'] = request.android_open_url
        if not UtilClient.is_unset(request.android_popup_activity):
            query['AndroidPopupActivity'] = request.android_popup_activity
        if not UtilClient.is_unset(request.android_popup_body):
            query['AndroidPopupBody'] = request.android_popup_body
        if not UtilClient.is_unset(request.android_popup_title):
            query['AndroidPopupTitle'] = request.android_popup_title
        if not UtilClient.is_unset(request.android_remind):
            query['AndroidRemind'] = request.android_remind
        if not UtilClient.is_unset(request.android_render_style):
            query['AndroidRenderStyle'] = request.android_render_style
        if not UtilClient.is_unset(request.android_vivo_push_mode):
            query['AndroidVivoPushMode'] = request.android_vivo_push_mode
        if not UtilClient.is_unset(request.android_xiao_mi_activity):
            query['AndroidXiaoMiActivity'] = request.android_xiao_mi_activity
        if not UtilClient.is_unset(request.android_xiao_mi_notify_body):
            query['AndroidXiaoMiNotifyBody'] = request.android_xiao_mi_notify_body
        if not UtilClient.is_unset(request.android_xiao_mi_notify_title):
            query['AndroidXiaoMiNotifyTitle'] = request.android_xiao_mi_notify_title
        if not UtilClient.is_unset(request.android_xiaomi_big_picture_url):
            query['AndroidXiaomiBigPictureUrl'] = request.android_xiaomi_big_picture_url
        if not UtilClient.is_unset(request.android_xiaomi_image_url):
            query['AndroidXiaomiImageUrl'] = request.android_xiaomi_image_url
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.device_type):
            query['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.job_key):
            query['JobKey'] = request.job_key
        if not UtilClient.is_unset(request.push_time):
            query['PushTime'] = request.push_time
        if not UtilClient.is_unset(request.push_type):
            query['PushType'] = request.push_type
        if not UtilClient.is_unset(request.send_channels):
            query['SendChannels'] = request.send_channels
        if not UtilClient.is_unset(request.send_speed):
            query['SendSpeed'] = request.send_speed
        if not UtilClient.is_unset(request.sms_delay_secs):
            query['SmsDelaySecs'] = request.sms_delay_secs
        if not UtilClient.is_unset(request.sms_params):
            query['SmsParams'] = request.sms_params
        if not UtilClient.is_unset(request.sms_send_policy):
            query['SmsSendPolicy'] = request.sms_send_policy
        if not UtilClient.is_unset(request.sms_sign_name):
            query['SmsSignName'] = request.sms_sign_name
        if not UtilClient.is_unset(request.sms_template_name):
            query['SmsTemplateName'] = request.sms_template_name
        if not UtilClient.is_unset(request.store_offline):
            query['StoreOffline'] = request.store_offline
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.trim):
            query['Trim'] = request.trim
        if not UtilClient.is_unset(request.i_osapns_env):
            query['iOSApnsEnv'] = request.i_osapns_env
        if not UtilClient.is_unset(request.i_osbadge):
            query['iOSBadge'] = request.i_osbadge
        if not UtilClient.is_unset(request.i_osbadge_auto_increment):
            query['iOSBadgeAutoIncrement'] = request.i_osbadge_auto_increment
        if not UtilClient.is_unset(request.i_osext_parameters):
            query['iOSExtParameters'] = request.i_osext_parameters
        if not UtilClient.is_unset(request.i_osinterruption_level):
            query['iOSInterruptionLevel'] = request.i_osinterruption_level
        if not UtilClient.is_unset(request.i_osmusic):
            query['iOSMusic'] = request.i_osmusic
        if not UtilClient.is_unset(request.i_osmutable_content):
            query['iOSMutableContent'] = request.i_osmutable_content
        if not UtilClient.is_unset(request.i_osnotification_category):
            query['iOSNotificationCategory'] = request.i_osnotification_category
        if not UtilClient.is_unset(request.i_osnotification_collapse_id):
            query['iOSNotificationCollapseId'] = request.i_osnotification_collapse_id
        if not UtilClient.is_unset(request.i_osnotification_thread_id):
            query['iOSNotificationThreadId'] = request.i_osnotification_thread_id
        if not UtilClient.is_unset(request.i_osrelevance_score):
            query['iOSRelevanceScore'] = request.i_osrelevance_score
        if not UtilClient.is_unset(request.i_osremind):
            query['iOSRemind'] = request.i_osremind
        if not UtilClient.is_unset(request.i_osremind_body):
            query['iOSRemindBody'] = request.i_osremind_body
        if not UtilClient.is_unset(request.i_ossilent_notification):
            query['iOSSilentNotification'] = request.i_ossilent_notification
        if not UtilClient.is_unset(request.i_ossubtitle):
            query['iOSSubtitle'] = request.i_ossubtitle
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Push',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.PushResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push(
        self,
        request: push_20160801_models.PushRequest,
    ) -> push_20160801_models.PushResponse:
        runtime = util_models.RuntimeOptions()
        return self.push_with_options(request, runtime)

    async def push_async(
        self,
        request: push_20160801_models.PushRequest,
    ) -> push_20160801_models.PushResponse:
        runtime = util_models.RuntimeOptions()
        return await self.push_with_options_async(request, runtime)

    def push_message_to_android_with_options(
        self,
        request: push_20160801_models.PushMessageToAndroidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.PushMessageToAndroidResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.job_key):
            query['JobKey'] = request.job_key
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushMessageToAndroid',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.PushMessageToAndroidResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_message_to_android_with_options_async(
        self,
        request: push_20160801_models.PushMessageToAndroidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.PushMessageToAndroidResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.job_key):
            query['JobKey'] = request.job_key
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushMessageToAndroid',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.PushMessageToAndroidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_message_to_android(
        self,
        request: push_20160801_models.PushMessageToAndroidRequest,
    ) -> push_20160801_models.PushMessageToAndroidResponse:
        runtime = util_models.RuntimeOptions()
        return self.push_message_to_android_with_options(request, runtime)

    async def push_message_to_android_async(
        self,
        request: push_20160801_models.PushMessageToAndroidRequest,
    ) -> push_20160801_models.PushMessageToAndroidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.push_message_to_android_with_options_async(request, runtime)

    def push_message_toi_oswith_options(
        self,
        request: push_20160801_models.PushMessageToiOSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.PushMessageToiOSResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.job_key):
            query['JobKey'] = request.job_key
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushMessageToiOS',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.PushMessageToiOSResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_message_toi_oswith_options_async(
        self,
        request: push_20160801_models.PushMessageToiOSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.PushMessageToiOSResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.job_key):
            query['JobKey'] = request.job_key
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushMessageToiOS',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.PushMessageToiOSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_message_toi_os(
        self,
        request: push_20160801_models.PushMessageToiOSRequest,
    ) -> push_20160801_models.PushMessageToiOSResponse:
        runtime = util_models.RuntimeOptions()
        return self.push_message_toi_oswith_options(request, runtime)

    async def push_message_toi_os_async(
        self,
        request: push_20160801_models.PushMessageToiOSRequest,
    ) -> push_20160801_models.PushMessageToiOSResponse:
        runtime = util_models.RuntimeOptions()
        return await self.push_message_toi_oswith_options_async(request, runtime)

    def push_notice_to_android_with_options(
        self,
        request: push_20160801_models.PushNoticeToAndroidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.PushNoticeToAndroidResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.ext_parameters):
            query['ExtParameters'] = request.ext_parameters
        if not UtilClient.is_unset(request.job_key):
            query['JobKey'] = request.job_key
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushNoticeToAndroid',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.PushNoticeToAndroidResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_notice_to_android_with_options_async(
        self,
        request: push_20160801_models.PushNoticeToAndroidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.PushNoticeToAndroidResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.ext_parameters):
            query['ExtParameters'] = request.ext_parameters
        if not UtilClient.is_unset(request.job_key):
            query['JobKey'] = request.job_key
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushNoticeToAndroid',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.PushNoticeToAndroidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_notice_to_android(
        self,
        request: push_20160801_models.PushNoticeToAndroidRequest,
    ) -> push_20160801_models.PushNoticeToAndroidResponse:
        runtime = util_models.RuntimeOptions()
        return self.push_notice_to_android_with_options(request, runtime)

    async def push_notice_to_android_async(
        self,
        request: push_20160801_models.PushNoticeToAndroidRequest,
    ) -> push_20160801_models.PushNoticeToAndroidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.push_notice_to_android_with_options_async(request, runtime)

    def push_notice_toi_oswith_options(
        self,
        request: push_20160801_models.PushNoticeToiOSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.PushNoticeToiOSResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apns_env):
            query['ApnsEnv'] = request.apns_env
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.ext_parameters):
            query['ExtParameters'] = request.ext_parameters
        if not UtilClient.is_unset(request.job_key):
            query['JobKey'] = request.job_key
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushNoticeToiOS',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.PushNoticeToiOSResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_notice_toi_oswith_options_async(
        self,
        request: push_20160801_models.PushNoticeToiOSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.PushNoticeToiOSResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apns_env):
            query['ApnsEnv'] = request.apns_env
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.ext_parameters):
            query['ExtParameters'] = request.ext_parameters
        if not UtilClient.is_unset(request.job_key):
            query['JobKey'] = request.job_key
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushNoticeToiOS',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.PushNoticeToiOSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_notice_toi_os(
        self,
        request: push_20160801_models.PushNoticeToiOSRequest,
    ) -> push_20160801_models.PushNoticeToiOSResponse:
        runtime = util_models.RuntimeOptions()
        return self.push_notice_toi_oswith_options(request, runtime)

    async def push_notice_toi_os_async(
        self,
        request: push_20160801_models.PushNoticeToiOSRequest,
    ) -> push_20160801_models.PushNoticeToiOSResponse:
        runtime = util_models.RuntimeOptions()
        return await self.push_notice_toi_oswith_options_async(request, runtime)

    def query_aliases_with_options(
        self,
        request: push_20160801_models.QueryAliasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryAliasesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAliases',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryAliasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_aliases_with_options_async(
        self,
        request: push_20160801_models.QueryAliasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryAliasesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAliases',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryAliasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_aliases(
        self,
        request: push_20160801_models.QueryAliasesRequest,
    ) -> push_20160801_models.QueryAliasesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_aliases_with_options(request, runtime)

    async def query_aliases_async(
        self,
        request: push_20160801_models.QueryAliasesRequest,
    ) -> push_20160801_models.QueryAliasesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_aliases_with_options_async(request, runtime)

    def query_device_count_with_options(
        self,
        request: push_20160801_models.QueryDeviceCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryDeviceCountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceCount',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryDeviceCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_count_with_options_async(
        self,
        request: push_20160801_models.QueryDeviceCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryDeviceCountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceCount',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryDeviceCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_device_count(
        self,
        request: push_20160801_models.QueryDeviceCountRequest,
    ) -> push_20160801_models.QueryDeviceCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_count_with_options(request, runtime)

    async def query_device_count_async(
        self,
        request: push_20160801_models.QueryDeviceCountRequest,
    ) -> push_20160801_models.QueryDeviceCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_count_with_options_async(request, runtime)

    def query_device_info_with_options(
        self,
        request: push_20160801_models.QueryDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryDeviceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceInfo',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_info_with_options_async(
        self,
        request: push_20160801_models.QueryDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryDeviceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceInfo',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_device_info(
        self,
        request: push_20160801_models.QueryDeviceInfoRequest,
    ) -> push_20160801_models.QueryDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_info_with_options(request, runtime)

    async def query_device_info_async(
        self,
        request: push_20160801_models.QueryDeviceInfoRequest,
    ) -> push_20160801_models.QueryDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_info_with_options_async(request, runtime)

    def query_device_stat_with_options(
        self,
        request: push_20160801_models.QueryDeviceStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryDeviceStatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_type):
            query['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceStat',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryDeviceStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_stat_with_options_async(
        self,
        request: push_20160801_models.QueryDeviceStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryDeviceStatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_type):
            query['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceStat',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryDeviceStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_device_stat(
        self,
        request: push_20160801_models.QueryDeviceStatRequest,
    ) -> push_20160801_models.QueryDeviceStatResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_stat_with_options(request, runtime)

    async def query_device_stat_async(
        self,
        request: push_20160801_models.QueryDeviceStatRequest,
    ) -> push_20160801_models.QueryDeviceStatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_stat_with_options_async(request, runtime)

    def query_devices_by_account_with_options(
        self,
        request: push_20160801_models.QueryDevicesByAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryDevicesByAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDevicesByAccount',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryDevicesByAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_devices_by_account_with_options_async(
        self,
        request: push_20160801_models.QueryDevicesByAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryDevicesByAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDevicesByAccount',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryDevicesByAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_devices_by_account(
        self,
        request: push_20160801_models.QueryDevicesByAccountRequest,
    ) -> push_20160801_models.QueryDevicesByAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_devices_by_account_with_options(request, runtime)

    async def query_devices_by_account_async(
        self,
        request: push_20160801_models.QueryDevicesByAccountRequest,
    ) -> push_20160801_models.QueryDevicesByAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_devices_by_account_with_options_async(request, runtime)

    def query_devices_by_alias_with_options(
        self,
        request: push_20160801_models.QueryDevicesByAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryDevicesByAliasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias):
            query['Alias'] = request.alias
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDevicesByAlias',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryDevicesByAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_devices_by_alias_with_options_async(
        self,
        request: push_20160801_models.QueryDevicesByAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryDevicesByAliasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias):
            query['Alias'] = request.alias
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDevicesByAlias',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryDevicesByAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_devices_by_alias(
        self,
        request: push_20160801_models.QueryDevicesByAliasRequest,
    ) -> push_20160801_models.QueryDevicesByAliasResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_devices_by_alias_with_options(request, runtime)

    async def query_devices_by_alias_async(
        self,
        request: push_20160801_models.QueryDevicesByAliasRequest,
    ) -> push_20160801_models.QueryDevicesByAliasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_devices_by_alias_with_options_async(request, runtime)

    def query_push_records_with_options(
        self,
        request: push_20160801_models.QueryPushRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryPushRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.push_type):
            query['PushType'] = request.push_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPushRecords',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryPushRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_push_records_with_options_async(
        self,
        request: push_20160801_models.QueryPushRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryPushRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.push_type):
            query['PushType'] = request.push_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPushRecords',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryPushRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_push_records(
        self,
        request: push_20160801_models.QueryPushRecordsRequest,
    ) -> push_20160801_models.QueryPushRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_push_records_with_options(request, runtime)

    async def query_push_records_async(
        self,
        request: push_20160801_models.QueryPushRecordsRequest,
    ) -> push_20160801_models.QueryPushRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_push_records_with_options_async(request, runtime)

    def query_push_stat_by_app_with_options(
        self,
        request: push_20160801_models.QueryPushStatByAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryPushStatByAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPushStatByApp',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryPushStatByAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_push_stat_by_app_with_options_async(
        self,
        request: push_20160801_models.QueryPushStatByAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryPushStatByAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPushStatByApp',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryPushStatByAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_push_stat_by_app(
        self,
        request: push_20160801_models.QueryPushStatByAppRequest,
    ) -> push_20160801_models.QueryPushStatByAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_push_stat_by_app_with_options(request, runtime)

    async def query_push_stat_by_app_async(
        self,
        request: push_20160801_models.QueryPushStatByAppRequest,
    ) -> push_20160801_models.QueryPushStatByAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_push_stat_by_app_with_options_async(request, runtime)

    def query_push_stat_by_msg_with_options(
        self,
        request: push_20160801_models.QueryPushStatByMsgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryPushStatByMsgResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPushStatByMsg',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryPushStatByMsgResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_push_stat_by_msg_with_options_async(
        self,
        request: push_20160801_models.QueryPushStatByMsgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryPushStatByMsgResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPushStatByMsg',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryPushStatByMsgResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_push_stat_by_msg(
        self,
        request: push_20160801_models.QueryPushStatByMsgRequest,
    ) -> push_20160801_models.QueryPushStatByMsgResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_push_stat_by_msg_with_options(request, runtime)

    async def query_push_stat_by_msg_async(
        self,
        request: push_20160801_models.QueryPushStatByMsgRequest,
    ) -> push_20160801_models.QueryPushStatByMsgResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_push_stat_by_msg_with_options_async(request, runtime)

    def query_tags_with_options(
        self,
        request: push_20160801_models.QueryTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.client_key):
            query['ClientKey'] = request.client_key
        if not UtilClient.is_unset(request.key_type):
            query['KeyType'] = request.key_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTags',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tags_with_options_async(
        self,
        request: push_20160801_models.QueryTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.client_key):
            query['ClientKey'] = request.client_key
        if not UtilClient.is_unset(request.key_type):
            query['KeyType'] = request.key_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTags',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_tags(
        self,
        request: push_20160801_models.QueryTagsRequest,
    ) -> push_20160801_models.QueryTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_tags_with_options(request, runtime)

    async def query_tags_async(
        self,
        request: push_20160801_models.QueryTagsRequest,
    ) -> push_20160801_models.QueryTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_tags_with_options_async(request, runtime)

    def query_unique_device_stat_with_options(
        self,
        request: push_20160801_models.QueryUniqueDeviceStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryUniqueDeviceStatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUniqueDeviceStat',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryUniqueDeviceStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_unique_device_stat_with_options_async(
        self,
        request: push_20160801_models.QueryUniqueDeviceStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryUniqueDeviceStatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUniqueDeviceStat',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryUniqueDeviceStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_unique_device_stat(
        self,
        request: push_20160801_models.QueryUniqueDeviceStatRequest,
    ) -> push_20160801_models.QueryUniqueDeviceStatResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_unique_device_stat_with_options(request, runtime)

    async def query_unique_device_stat_async(
        self,
        request: push_20160801_models.QueryUniqueDeviceStatRequest,
    ) -> push_20160801_models.QueryUniqueDeviceStatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_unique_device_stat_with_options_async(request, runtime)

    def remove_tag_with_options(
        self,
        request: push_20160801_models.RemoveTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.RemoveTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTag',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.RemoveTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_tag_with_options_async(
        self,
        request: push_20160801_models.RemoveTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.RemoveTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTag',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.RemoveTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_tag(
        self,
        request: push_20160801_models.RemoveTagRequest,
    ) -> push_20160801_models.RemoveTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_tag_with_options(request, runtime)

    async def remove_tag_async(
        self,
        request: push_20160801_models.RemoveTagRequest,
    ) -> push_20160801_models.RemoveTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_tag_with_options_async(request, runtime)

    def unbind_alias_with_options(
        self,
        request: push_20160801_models.UnbindAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.UnbindAliasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.unbind_all):
            query['UnbindAll'] = request.unbind_all
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindAlias',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.UnbindAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_alias_with_options_async(
        self,
        request: push_20160801_models.UnbindAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.UnbindAliasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.unbind_all):
            query['UnbindAll'] = request.unbind_all
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindAlias',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.UnbindAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_alias(
        self,
        request: push_20160801_models.UnbindAliasRequest,
    ) -> push_20160801_models.UnbindAliasResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_alias_with_options(request, runtime)

    async def unbind_alias_async(
        self,
        request: push_20160801_models.UnbindAliasRequest,
    ) -> push_20160801_models.UnbindAliasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_alias_with_options_async(request, runtime)

    def unbind_phone_with_options(
        self,
        request: push_20160801_models.UnbindPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.UnbindPhoneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindPhone',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.UnbindPhoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_phone_with_options_async(
        self,
        request: push_20160801_models.UnbindPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.UnbindPhoneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindPhone',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.UnbindPhoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_phone(
        self,
        request: push_20160801_models.UnbindPhoneRequest,
    ) -> push_20160801_models.UnbindPhoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_phone_with_options(request, runtime)

    async def unbind_phone_async(
        self,
        request: push_20160801_models.UnbindPhoneRequest,
    ) -> push_20160801_models.UnbindPhoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_phone_with_options_async(request, runtime)

    def unbind_tag_with_options(
        self,
        request: push_20160801_models.UnbindTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.UnbindTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.client_key):
            query['ClientKey'] = request.client_key
        if not UtilClient.is_unset(request.key_type):
            query['KeyType'] = request.key_type
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindTag',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.UnbindTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_tag_with_options_async(
        self,
        request: push_20160801_models.UnbindTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.UnbindTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.client_key):
            query['ClientKey'] = request.client_key
        if not UtilClient.is_unset(request.key_type):
            query['KeyType'] = request.key_type
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindTag',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.UnbindTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_tag(
        self,
        request: push_20160801_models.UnbindTagRequest,
    ) -> push_20160801_models.UnbindTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_tag_with_options(request, runtime)

    async def unbind_tag_async(
        self,
        request: push_20160801_models.UnbindTagRequest,
    ) -> push_20160801_models.UnbindTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_tag_with_options_async(request, runtime)
