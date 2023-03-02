# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_moguan_sdk20210415 import models as moguan_sdk_20210415_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('moguan-sdk', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def register_device_with_options(
        self,
        tmp_req: moguan_sdk_20210415_models.RegisterDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> moguan_sdk_20210415_models.RegisterDeviceResponse:
        UtilClient.validate_model(tmp_req)
        request = moguan_sdk_20210415_models.RegisterDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extend):
            request.extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extend, 'Extend', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.extend_shrink):
            body['Extend'] = request.extend_shrink
        if not UtilClient.is_unset(request.sdk_code):
            body['SdkCode'] = request.sdk_code
        if not UtilClient.is_unset(request.user_device_id):
            body['UserDeviceId'] = request.user_device_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegisterDevice',
            version='2021-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            moguan_sdk_20210415_models.RegisterDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_device_with_options_async(
        self,
        tmp_req: moguan_sdk_20210415_models.RegisterDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> moguan_sdk_20210415_models.RegisterDeviceResponse:
        UtilClient.validate_model(tmp_req)
        request = moguan_sdk_20210415_models.RegisterDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extend):
            request.extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extend, 'Extend', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.extend_shrink):
            body['Extend'] = request.extend_shrink
        if not UtilClient.is_unset(request.sdk_code):
            body['SdkCode'] = request.sdk_code
        if not UtilClient.is_unset(request.user_device_id):
            body['UserDeviceId'] = request.user_device_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegisterDevice',
            version='2021-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            moguan_sdk_20210415_models.RegisterDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_device(
        self,
        request: moguan_sdk_20210415_models.RegisterDeviceRequest,
    ) -> moguan_sdk_20210415_models.RegisterDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_device_with_options(request, runtime)

    async def register_device_async(
        self,
        request: moguan_sdk_20210415_models.RegisterDeviceRequest,
    ) -> moguan_sdk_20210415_models.RegisterDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_device_with_options_async(request, runtime)
