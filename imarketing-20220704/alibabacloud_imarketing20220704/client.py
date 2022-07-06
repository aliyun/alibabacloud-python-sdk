# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imarketing20220704 import models as imarketing_20220704_models
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
        self._endpoint = self.get_endpoint('imarketing', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_device_with_options(
        self,
        tmp_req: imarketing_20220704_models.CreateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imarketing_20220704_models.CreateDeviceResponse:
        UtilClient.validate_model(tmp_req)
        request = imarketing_20220704_models.CreateDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extra_map):
            request.extra_map_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra_map, 'ExtraMap', 'json')
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.city):
            body['City'] = request.city
        if not UtilClient.is_unset(request.device_model_number):
            body['DeviceModelNumber'] = request.device_model_number
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.district):
            body['District'] = request.district
        if not UtilClient.is_unset(request.extra_map_shrink):
            body['ExtraMap'] = request.extra_map_shrink
        if not UtilClient.is_unset(request.first_scene):
            body['FirstScene'] = request.first_scene
        if not UtilClient.is_unset(request.floor):
            body['Floor'] = request.floor
        if not UtilClient.is_unset(request.location_name):
            body['LocationName'] = request.location_name
        if not UtilClient.is_unset(request.media_id):
            body['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.outer_code):
            body['OuterCode'] = request.outer_code
        if not UtilClient.is_unset(request.province):
            body['Province'] = request.province
        if not UtilClient.is_unset(request.second_scene):
            body['SecondScene'] = request.second_scene
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDevice',
            version='2022-07-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imarketing_20220704_models.CreateDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_device_with_options_async(
        self,
        tmp_req: imarketing_20220704_models.CreateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imarketing_20220704_models.CreateDeviceResponse:
        UtilClient.validate_model(tmp_req)
        request = imarketing_20220704_models.CreateDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extra_map):
            request.extra_map_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra_map, 'ExtraMap', 'json')
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.city):
            body['City'] = request.city
        if not UtilClient.is_unset(request.device_model_number):
            body['DeviceModelNumber'] = request.device_model_number
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.district):
            body['District'] = request.district
        if not UtilClient.is_unset(request.extra_map_shrink):
            body['ExtraMap'] = request.extra_map_shrink
        if not UtilClient.is_unset(request.first_scene):
            body['FirstScene'] = request.first_scene
        if not UtilClient.is_unset(request.floor):
            body['Floor'] = request.floor
        if not UtilClient.is_unset(request.location_name):
            body['LocationName'] = request.location_name
        if not UtilClient.is_unset(request.media_id):
            body['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.outer_code):
            body['OuterCode'] = request.outer_code
        if not UtilClient.is_unset(request.province):
            body['Province'] = request.province
        if not UtilClient.is_unset(request.second_scene):
            body['SecondScene'] = request.second_scene
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDevice',
            version='2022-07-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imarketing_20220704_models.CreateDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_device(
        self,
        request: imarketing_20220704_models.CreateDeviceRequest,
    ) -> imarketing_20220704_models.CreateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_device_with_options(request, runtime)

    async def create_device_async(
        self,
        request: imarketing_20220704_models.CreateDeviceRequest,
    ) -> imarketing_20220704_models.CreateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_device_with_options_async(request, runtime)

    def get_user_finished_ad_with_options(
        self,
        request: imarketing_20220704_models.GetUserFinishedAdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imarketing_20220704_models.GetUserFinishedAdResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserFinishedAd',
            version='2022-07-04',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imarketing_20220704_models.GetUserFinishedAdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_finished_ad_with_options_async(
        self,
        request: imarketing_20220704_models.GetUserFinishedAdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imarketing_20220704_models.GetUserFinishedAdResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserFinishedAd',
            version='2022-07-04',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imarketing_20220704_models.GetUserFinishedAdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_finished_ad(
        self,
        request: imarketing_20220704_models.GetUserFinishedAdRequest,
    ) -> imarketing_20220704_models.GetUserFinishedAdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_finished_ad_with_options(request, runtime)

    async def get_user_finished_ad_async(
        self,
        request: imarketing_20220704_models.GetUserFinishedAdRequest,
    ) -> imarketing_20220704_models.GetUserFinishedAdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_finished_ad_with_options_async(request, runtime)

    def list_advertising_with_options(
        self,
        tmp_req: imarketing_20220704_models.ListAdvertisingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imarketing_20220704_models.ListAdvertisingResponse:
        UtilClient.validate_model(tmp_req)
        request = imarketing_20220704_models.ListAdvertisingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.app), 'App', 'json')
        if not UtilClient.is_unset(tmp_req.ext):
            request.ext_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext, 'Ext', 'json')
        if not UtilClient.is_unset(tmp_req.imp):
            request.imp_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.imp, 'Imp', 'json')
        if not UtilClient.is_unset(tmp_req.user):
            request.user_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user), 'User', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAdvertising',
            version='2022-07-04',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imarketing_20220704_models.ListAdvertisingResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_advertising_with_options_async(
        self,
        tmp_req: imarketing_20220704_models.ListAdvertisingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imarketing_20220704_models.ListAdvertisingResponse:
        UtilClient.validate_model(tmp_req)
        request = imarketing_20220704_models.ListAdvertisingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.app), 'App', 'json')
        if not UtilClient.is_unset(tmp_req.ext):
            request.ext_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext, 'Ext', 'json')
        if not UtilClient.is_unset(tmp_req.imp):
            request.imp_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.imp, 'Imp', 'json')
        if not UtilClient.is_unset(tmp_req.user):
            request.user_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user), 'User', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAdvertising',
            version='2022-07-04',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imarketing_20220704_models.ListAdvertisingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_advertising(
        self,
        request: imarketing_20220704_models.ListAdvertisingRequest,
    ) -> imarketing_20220704_models.ListAdvertisingResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_advertising_with_options(request, runtime)

    async def list_advertising_async(
        self,
        request: imarketing_20220704_models.ListAdvertisingRequest,
    ) -> imarketing_20220704_models.ListAdvertisingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_advertising_with_options_async(request, runtime)
