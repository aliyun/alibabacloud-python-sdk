# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_push20160801 import models as push_20160801_models
from alibabacloud_tea_util import models as util_models


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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.BindAliasResponse().from_map(
            self.do_rpcrequest('BindAlias', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_alias_with_options_async(
        self,
        request: push_20160801_models.BindAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.BindAliasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.BindAliasResponse().from_map(
            await self.do_rpcrequest_async('BindAlias', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.BindPhoneResponse().from_map(
            self.do_rpcrequest('BindPhone', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_phone_with_options_async(
        self,
        request: push_20160801_models.BindPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.BindPhoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.BindPhoneResponse().from_map(
            await self.do_rpcrequest_async('BindPhone', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.BindTagResponse().from_map(
            self.do_rpcrequest('BindTag', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_tag_with_options_async(
        self,
        request: push_20160801_models.BindTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.BindTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.BindTagResponse().from_map(
            await self.do_rpcrequest_async('BindTag', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.CancelPushResponse().from_map(
            self.do_rpcrequest('CancelPush', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_push_with_options_async(
        self,
        request: push_20160801_models.CancelPushRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.CancelPushResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.CancelPushResponse().from_map(
            await self.do_rpcrequest_async('CancelPush', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def check_device_with_options(
        self,
        request: push_20160801_models.CheckDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.CheckDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.CheckDeviceResponse().from_map(
            self.do_rpcrequest('CheckDevice', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_device_with_options_async(
        self,
        request: push_20160801_models.CheckDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.CheckDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.CheckDeviceResponse().from_map(
            await self.do_rpcrequest_async('CheckDevice', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.CheckDevicesResponse().from_map(
            self.do_rpcrequest('CheckDevices', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_devices_with_options_async(
        self,
        request: push_20160801_models.CheckDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.CheckDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.CheckDevicesResponse().from_map(
            await self.do_rpcrequest_async('CheckDevices', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.CompleteContinuouslyPushResponse().from_map(
            self.do_rpcrequest('CompleteContinuouslyPush', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def complete_continuously_push_with_options_async(
        self,
        request: push_20160801_models.CompleteContinuouslyPushRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.CompleteContinuouslyPushResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.CompleteContinuouslyPushResponse().from_map(
            await self.do_rpcrequest_async('CompleteContinuouslyPush', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.ContinuouslyPushResponse().from_map(
            self.do_rpcrequest('ContinuouslyPush', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def continuously_push_with_options_async(
        self,
        request: push_20160801_models.ContinuouslyPushRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.ContinuouslyPushResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.ContinuouslyPushResponse().from_map(
            await self.do_rpcrequest_async('ContinuouslyPush', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return push_20160801_models.ListSummaryAppsResponse().from_map(
            self.do_rpcrequest('ListSummaryApps', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_summary_apps_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.ListSummaryAppsResponse:
        req = open_api_models.OpenApiRequest()
        return push_20160801_models.ListSummaryAppsResponse().from_map(
            await self.do_rpcrequest_async('ListSummaryApps', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.ListTagsResponse().from_map(
            self.do_rpcrequest('ListTags', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tags_with_options_async(
        self,
        request: push_20160801_models.ListTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.ListTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.ListTagsResponse().from_map(
            await self.do_rpcrequest_async('ListTags', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.MassPushResponse().from_map(
            self.do_rpcrequest('MassPush', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def mass_push_with_options_async(
        self,
        request: push_20160801_models.MassPushRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.MassPushResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.MassPushResponse().from_map(
            await self.do_rpcrequest_async('MassPush', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.PushResponse().from_map(
            self.do_rpcrequest('Push', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def push_with_options_async(
        self,
        request: push_20160801_models.PushRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.PushResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.PushResponse().from_map(
            await self.do_rpcrequest_async('Push', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.PushMessageToAndroidResponse().from_map(
            self.do_rpcrequest('PushMessageToAndroid', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def push_message_to_android_with_options_async(
        self,
        request: push_20160801_models.PushMessageToAndroidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.PushMessageToAndroidResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.PushMessageToAndroidResponse().from_map(
            await self.do_rpcrequest_async('PushMessageToAndroid', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.PushMessageToiOSResponse().from_map(
            self.do_rpcrequest('PushMessageToiOS', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def push_message_toi_oswith_options_async(
        self,
        request: push_20160801_models.PushMessageToiOSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.PushMessageToiOSResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.PushMessageToiOSResponse().from_map(
            await self.do_rpcrequest_async('PushMessageToiOS', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.PushNoticeToAndroidResponse().from_map(
            self.do_rpcrequest('PushNoticeToAndroid', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def push_notice_to_android_with_options_async(
        self,
        request: push_20160801_models.PushNoticeToAndroidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.PushNoticeToAndroidResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.PushNoticeToAndroidResponse().from_map(
            await self.do_rpcrequest_async('PushNoticeToAndroid', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.PushNoticeToiOSResponse().from_map(
            self.do_rpcrequest('PushNoticeToiOS', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def push_notice_toi_oswith_options_async(
        self,
        request: push_20160801_models.PushNoticeToiOSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.PushNoticeToiOSResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.PushNoticeToiOSResponse().from_map(
            await self.do_rpcrequest_async('PushNoticeToiOS', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.QueryAliasesResponse().from_map(
            self.do_rpcrequest('QueryAliases', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_aliases_with_options_async(
        self,
        request: push_20160801_models.QueryAliasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryAliasesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.QueryAliasesResponse().from_map(
            await self.do_rpcrequest_async('QueryAliases', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.QueryDeviceCountResponse().from_map(
            self.do_rpcrequest('QueryDeviceCount', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_count_with_options_async(
        self,
        request: push_20160801_models.QueryDeviceCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryDeviceCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.QueryDeviceCountResponse().from_map(
            await self.do_rpcrequest_async('QueryDeviceCount', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.QueryDeviceInfoResponse().from_map(
            self.do_rpcrequest('QueryDeviceInfo', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_info_with_options_async(
        self,
        request: push_20160801_models.QueryDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryDeviceInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.QueryDeviceInfoResponse().from_map(
            await self.do_rpcrequest_async('QueryDeviceInfo', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_devices_by_account_with_options(
        self,
        request: push_20160801_models.QueryDevicesByAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryDevicesByAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.QueryDevicesByAccountResponse().from_map(
            self.do_rpcrequest('QueryDevicesByAccount', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_devices_by_account_with_options_async(
        self,
        request: push_20160801_models.QueryDevicesByAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryDevicesByAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.QueryDevicesByAccountResponse().from_map(
            await self.do_rpcrequest_async('QueryDevicesByAccount', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.QueryDevicesByAliasResponse().from_map(
            self.do_rpcrequest('QueryDevicesByAlias', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_devices_by_alias_with_options_async(
        self,
        request: push_20160801_models.QueryDevicesByAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryDevicesByAliasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.QueryDevicesByAliasResponse().from_map(
            await self.do_rpcrequest_async('QueryDevicesByAlias', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_device_stat_with_options(
        self,
        request: push_20160801_models.QueryDeviceStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryDeviceStatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.QueryDeviceStatResponse().from_map(
            self.do_rpcrequest('QueryDeviceStat', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_stat_with_options_async(
        self,
        request: push_20160801_models.QueryDeviceStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryDeviceStatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.QueryDeviceStatResponse().from_map(
            await self.do_rpcrequest_async('QueryDeviceStat', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_push_records_with_options(
        self,
        request: push_20160801_models.QueryPushRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryPushRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.QueryPushRecordsResponse().from_map(
            self.do_rpcrequest('QueryPushRecords', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_push_records_with_options_async(
        self,
        request: push_20160801_models.QueryPushRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryPushRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.QueryPushRecordsResponse().from_map(
            await self.do_rpcrequest_async('QueryPushRecords', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.QueryPushStatByAppResponse().from_map(
            self.do_rpcrequest('QueryPushStatByApp', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_push_stat_by_app_with_options_async(
        self,
        request: push_20160801_models.QueryPushStatByAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryPushStatByAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.QueryPushStatByAppResponse().from_map(
            await self.do_rpcrequest_async('QueryPushStatByApp', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.QueryPushStatByMsgResponse().from_map(
            self.do_rpcrequest('QueryPushStatByMsg', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_push_stat_by_msg_with_options_async(
        self,
        request: push_20160801_models.QueryPushStatByMsgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryPushStatByMsgResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.QueryPushStatByMsgResponse().from_map(
            await self.do_rpcrequest_async('QueryPushStatByMsg', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.QueryTagsResponse().from_map(
            self.do_rpcrequest('QueryTags', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_tags_with_options_async(
        self,
        request: push_20160801_models.QueryTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.QueryTagsResponse().from_map(
            await self.do_rpcrequest_async('QueryTags', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.QueryUniqueDeviceStatResponse().from_map(
            self.do_rpcrequest('QueryUniqueDeviceStat', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_unique_device_stat_with_options_async(
        self,
        request: push_20160801_models.QueryUniqueDeviceStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.QueryUniqueDeviceStatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.QueryUniqueDeviceStatResponse().from_map(
            await self.do_rpcrequest_async('QueryUniqueDeviceStat', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.RemoveTagResponse().from_map(
            self.do_rpcrequest('RemoveTag', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_tag_with_options_async(
        self,
        request: push_20160801_models.RemoveTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.RemoveTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.RemoveTagResponse().from_map(
            await self.do_rpcrequest_async('RemoveTag', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.UnbindAliasResponse().from_map(
            self.do_rpcrequest('UnbindAlias', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_alias_with_options_async(
        self,
        request: push_20160801_models.UnbindAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.UnbindAliasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.UnbindAliasResponse().from_map(
            await self.do_rpcrequest_async('UnbindAlias', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.UnbindPhoneResponse().from_map(
            self.do_rpcrequest('UnbindPhone', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_phone_with_options_async(
        self,
        request: push_20160801_models.UnbindPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.UnbindPhoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.UnbindPhoneResponse().from_map(
            await self.do_rpcrequest_async('UnbindPhone', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.UnbindTagResponse().from_map(
            self.do_rpcrequest('UnbindTag', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_tag_with_options_async(
        self,
        request: push_20160801_models.UnbindTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> push_20160801_models.UnbindTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return push_20160801_models.UnbindTagResponse().from_map(
            await self.do_rpcrequest_async('UnbindTag', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
