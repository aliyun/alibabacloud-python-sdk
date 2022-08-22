# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aligenieip_1_0 import models as ali_genieip__1__0_models
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
        self._endpoint = self.get_endpoint('aligenie', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def device_control(
        self,
        request: ali_genieip__1__0_models.DeviceControlRequest,
    ) -> ali_genieip__1__0_models.DeviceControlResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeviceControlHeaders()
        return self.device_control_with_options(request, headers, runtime)

    async def device_control_async(
        self,
        request: ali_genieip__1__0_models.DeviceControlRequest,
    ) -> ali_genieip__1__0_models.DeviceControlResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeviceControlHeaders()
        return await self.device_control_with_options_async(request, headers, runtime)

    def device_control_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.DeviceControlRequest,
        headers: ali_genieip__1__0_models.DeviceControlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.DeviceControlResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.DeviceControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeviceControl',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/deviceControl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.DeviceControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def device_control_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.DeviceControlRequest,
        headers: ali_genieip__1__0_models.DeviceControlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.DeviceControlResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.DeviceControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeviceControl',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/deviceControl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.DeviceControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotel_home_back_image_and_modes(
        self,
        request: ali_genieip__1__0_models.GetHotelHomeBackImageAndModesRequest,
    ) -> ali_genieip__1__0_models.GetHotelHomeBackImageAndModesResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelHomeBackImageAndModesHeaders()
        return self.get_hotel_home_back_image_and_modes_with_options(request, headers, runtime)

    async def get_hotel_home_back_image_and_modes_async(
        self,
        request: ali_genieip__1__0_models.GetHotelHomeBackImageAndModesRequest,
    ) -> ali_genieip__1__0_models.GetHotelHomeBackImageAndModesResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelHomeBackImageAndModesHeaders()
        return await self.get_hotel_home_back_image_and_modes_with_options_async(request, headers, runtime)

    def get_hotel_home_back_image_and_modes_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelHomeBackImageAndModesRequest,
        headers: ali_genieip__1__0_models.GetHotelHomeBackImageAndModesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelHomeBackImageAndModesResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelHomeBackImageAndModesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelHomeBackImageAndModes',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelHomeBackImageAndModes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelHomeBackImageAndModesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotel_home_back_image_and_modes_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelHomeBackImageAndModesRequest,
        headers: ali_genieip__1__0_models.GetHotelHomeBackImageAndModesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelHomeBackImageAndModesResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelHomeBackImageAndModesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelHomeBackImageAndModes',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelHomeBackImageAndModes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelHomeBackImageAndModesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotel_order_detail(
        self,
        request: ali_genieip__1__0_models.GetHotelOrderDetailRequest,
    ) -> ali_genieip__1__0_models.GetHotelOrderDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelOrderDetailHeaders()
        return self.get_hotel_order_detail_with_options(request, headers, runtime)

    async def get_hotel_order_detail_async(
        self,
        request: ali_genieip__1__0_models.GetHotelOrderDetailRequest,
    ) -> ali_genieip__1__0_models.GetHotelOrderDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelOrderDetailHeaders()
        return await self.get_hotel_order_detail_with_options_async(request, headers, runtime)

    def get_hotel_order_detail_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelOrderDetailRequest,
        headers: ali_genieip__1__0_models.GetHotelOrderDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelOrderDetailResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelOrderDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelOrderDetail',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelOrderDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelOrderDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotel_order_detail_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelOrderDetailRequest,
        headers: ali_genieip__1__0_models.GetHotelOrderDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelOrderDetailResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelOrderDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelOrderDetail',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelOrderDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelOrderDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotel_sample_utterances(
        self,
        request: ali_genieip__1__0_models.GetHotelSampleUtterancesRequest,
    ) -> ali_genieip__1__0_models.GetHotelSampleUtterancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelSampleUtterancesHeaders()
        return self.get_hotel_sample_utterances_with_options(request, headers, runtime)

    async def get_hotel_sample_utterances_async(
        self,
        request: ali_genieip__1__0_models.GetHotelSampleUtterancesRequest,
    ) -> ali_genieip__1__0_models.GetHotelSampleUtterancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelSampleUtterancesHeaders()
        return await self.get_hotel_sample_utterances_with_options_async(request, headers, runtime)

    def get_hotel_sample_utterances_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelSampleUtterancesRequest,
        headers: ali_genieip__1__0_models.GetHotelSampleUtterancesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelSampleUtterancesResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelSampleUtterancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelSampleUtterances',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelSampleUtterances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelSampleUtterancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotel_sample_utterances_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelSampleUtterancesRequest,
        headers: ali_genieip__1__0_models.GetHotelSampleUtterancesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelSampleUtterancesResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelSampleUtterancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelSampleUtterances',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelSampleUtterances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelSampleUtterancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotel_screen_saver(
        self,
        request: ali_genieip__1__0_models.GetHotelScreenSaverRequest,
    ) -> ali_genieip__1__0_models.GetHotelScreenSaverResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelScreenSaverHeaders()
        return self.get_hotel_screen_saver_with_options(request, headers, runtime)

    async def get_hotel_screen_saver_async(
        self,
        request: ali_genieip__1__0_models.GetHotelScreenSaverRequest,
    ) -> ali_genieip__1__0_models.GetHotelScreenSaverResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelScreenSaverHeaders()
        return await self.get_hotel_screen_saver_with_options_async(request, headers, runtime)

    def get_hotel_screen_saver_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelScreenSaverRequest,
        headers: ali_genieip__1__0_models.GetHotelScreenSaverHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelScreenSaverResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelScreenSaverShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelScreenSaver',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelScreenSaver',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelScreenSaverResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotel_screen_saver_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelScreenSaverRequest,
        headers: ali_genieip__1__0_models.GetHotelScreenSaverHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelScreenSaverResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelScreenSaverShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelScreenSaver',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelScreenSaver',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelScreenSaverResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotel_control_device(
        self,
        request: ali_genieip__1__0_models.ListHotelControlDeviceRequest,
    ) -> ali_genieip__1__0_models.ListHotelControlDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelControlDeviceHeaders()
        return self.list_hotel_control_device_with_options(request, headers, runtime)

    async def list_hotel_control_device_async(
        self,
        request: ali_genieip__1__0_models.ListHotelControlDeviceRequest,
    ) -> ali_genieip__1__0_models.ListHotelControlDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelControlDeviceHeaders()
        return await self.list_hotel_control_device_with_options_async(request, headers, runtime)

    def list_hotel_control_device_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelControlDeviceRequest,
        headers: ali_genieip__1__0_models.ListHotelControlDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelControlDeviceResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelControlDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotelControlDevice',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelControlDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelControlDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotel_control_device_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelControlDeviceRequest,
        headers: ali_genieip__1__0_models.ListHotelControlDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelControlDeviceResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelControlDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotelControlDevice',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelControlDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelControlDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotel_order(
        self,
        request: ali_genieip__1__0_models.ListHotelOrderRequest,
    ) -> ali_genieip__1__0_models.ListHotelOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelOrderHeaders()
        return self.list_hotel_order_with_options(request, headers, runtime)

    async def list_hotel_order_async(
        self,
        request: ali_genieip__1__0_models.ListHotelOrderRequest,
    ) -> ali_genieip__1__0_models.ListHotelOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelOrderHeaders()
        return await self.list_hotel_order_with_options_async(request, headers, runtime)

    def list_hotel_order_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelOrderRequest,
        headers: ali_genieip__1__0_models.ListHotelOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotelOrder',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelOrder',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotel_order_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelOrderRequest,
        headers: ali_genieip__1__0_models.ListHotelOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotelOrder',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelOrder',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotel_scene_item(
        self,
        request: ali_genieip__1__0_models.ListHotelSceneItemRequest,
    ) -> ali_genieip__1__0_models.ListHotelSceneItemResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelSceneItemHeaders()
        return self.list_hotel_scene_item_with_options(request, headers, runtime)

    async def list_hotel_scene_item_async(
        self,
        request: ali_genieip__1__0_models.ListHotelSceneItemRequest,
    ) -> ali_genieip__1__0_models.ListHotelSceneItemResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelSceneItemHeaders()
        return await self.list_hotel_scene_item_with_options_async(request, headers, runtime)

    def list_hotel_scene_item_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelSceneItemRequest,
        headers: ali_genieip__1__0_models.ListHotelSceneItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelSceneItemResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelSceneItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotelSceneItem',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelSceneItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelSceneItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotel_scene_item_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelSceneItemRequest,
        headers: ali_genieip__1__0_models.ListHotelSceneItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelSceneItemResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelSceneItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotelSceneItem',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelSceneItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelSceneItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotel_service_category(
        self,
        request: ali_genieip__1__0_models.ListHotelServiceCategoryRequest,
    ) -> ali_genieip__1__0_models.ListHotelServiceCategoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelServiceCategoryHeaders()
        return self.list_hotel_service_category_with_options(request, headers, runtime)

    async def list_hotel_service_category_async(
        self,
        request: ali_genieip__1__0_models.ListHotelServiceCategoryRequest,
    ) -> ali_genieip__1__0_models.ListHotelServiceCategoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelServiceCategoryHeaders()
        return await self.list_hotel_service_category_with_options_async(request, headers, runtime)

    def list_hotel_service_category_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelServiceCategoryRequest,
        headers: ali_genieip__1__0_models.ListHotelServiceCategoryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelServiceCategoryResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelServiceCategoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotelServiceCategory',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelServiceCategory',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelServiceCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotel_service_category_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelServiceCategoryRequest,
        headers: ali_genieip__1__0_models.ListHotelServiceCategoryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelServiceCategoryResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelServiceCategoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotelServiceCategory',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelServiceCategory',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelServiceCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_device_status(
        self,
        request: ali_genieip__1__0_models.QueryDeviceStatusRequest,
    ) -> ali_genieip__1__0_models.QueryDeviceStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.QueryDeviceStatusHeaders()
        return self.query_device_status_with_options(request, headers, runtime)

    async def query_device_status_async(
        self,
        request: ali_genieip__1__0_models.QueryDeviceStatusRequest,
    ) -> ali_genieip__1__0_models.QueryDeviceStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.QueryDeviceStatusHeaders()
        return await self.query_device_status_with_options_async(request, headers, runtime)

    def query_device_status_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.QueryDeviceStatusRequest,
        headers: ali_genieip__1__0_models.QueryDeviceStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.QueryDeviceStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.QueryDeviceStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceStatus',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/queryDeviceStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.QueryDeviceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_status_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.QueryDeviceStatusRequest,
        headers: ali_genieip__1__0_models.QueryDeviceStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.QueryDeviceStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.QueryDeviceStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceStatus',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/queryDeviceStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.QueryDeviceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_hotel_product(
        self,
        request: ali_genieip__1__0_models.QueryHotelProductRequest,
    ) -> ali_genieip__1__0_models.QueryHotelProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.QueryHotelProductHeaders()
        return self.query_hotel_product_with_options(request, headers, runtime)

    async def query_hotel_product_async(
        self,
        request: ali_genieip__1__0_models.QueryHotelProductRequest,
    ) -> ali_genieip__1__0_models.QueryHotelProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.QueryHotelProductHeaders()
        return await self.query_hotel_product_with_options_async(request, headers, runtime)

    def query_hotel_product_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.QueryHotelProductRequest,
        headers: ali_genieip__1__0_models.QueryHotelProductHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.QueryHotelProductResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.QueryHotelProductShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryHotelProduct',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/queryHotelProduct',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.QueryHotelProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_hotel_product_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.QueryHotelProductRequest,
        headers: ali_genieip__1__0_models.QueryHotelProductHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.QueryHotelProductResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.QueryHotelProductShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryHotelProduct',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/queryHotelProduct',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.QueryHotelProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def room_check_out(
        self,
        request: ali_genieip__1__0_models.RoomCheckOutRequest,
    ) -> ali_genieip__1__0_models.RoomCheckOutResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.RoomCheckOutHeaders()
        return self.room_check_out_with_options(request, headers, runtime)

    async def room_check_out_async(
        self,
        request: ali_genieip__1__0_models.RoomCheckOutRequest,
    ) -> ali_genieip__1__0_models.RoomCheckOutResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.RoomCheckOutHeaders()
        return await self.room_check_out_with_options_async(request, headers, runtime)

    def room_check_out_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.RoomCheckOutRequest,
        headers: ali_genieip__1__0_models.RoomCheckOutHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.RoomCheckOutResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.RoomCheckOutShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RoomCheckOut',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/roomCheckOut',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.RoomCheckOutResponse(),
            self.call_api(params, req, runtime)
        )

    async def room_check_out_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.RoomCheckOutRequest,
        headers: ali_genieip__1__0_models.RoomCheckOutHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.RoomCheckOutResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.RoomCheckOutShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RoomCheckOut',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/roomCheckOut',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.RoomCheckOutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_hotel_order(
        self,
        request: ali_genieip__1__0_models.SubmitHotelOrderRequest,
    ) -> ali_genieip__1__0_models.SubmitHotelOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.SubmitHotelOrderHeaders()
        return self.submit_hotel_order_with_options(request, headers, runtime)

    async def submit_hotel_order_async(
        self,
        request: ali_genieip__1__0_models.SubmitHotelOrderRequest,
    ) -> ali_genieip__1__0_models.SubmitHotelOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.SubmitHotelOrderHeaders()
        return await self.submit_hotel_order_with_options_async(request, headers, runtime)

    def submit_hotel_order_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.SubmitHotelOrderRequest,
        headers: ali_genieip__1__0_models.SubmitHotelOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.SubmitHotelOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.SubmitHotelOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitHotelOrder',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/submitHotelOrder',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.SubmitHotelOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_hotel_order_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.SubmitHotelOrderRequest,
        headers: ali_genieip__1__0_models.SubmitHotelOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.SubmitHotelOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.SubmitHotelOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitHotelOrder',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/submitHotelOrder',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.SubmitHotelOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )
