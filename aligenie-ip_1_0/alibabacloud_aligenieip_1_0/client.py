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

    def add_message_template(
        self,
        request: ali_genieip__1__0_models.AddMessageTemplateRequest,
    ) -> ali_genieip__1__0_models.AddMessageTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddMessageTemplateHeaders()
        return self.add_message_template_with_options(request, headers, runtime)

    async def add_message_template_async(
        self,
        request: ali_genieip__1__0_models.AddMessageTemplateRequest,
    ) -> ali_genieip__1__0_models.AddMessageTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddMessageTemplateHeaders()
        return await self.add_message_template_with_options_async(request, headers, runtime)

    def add_message_template_with_options(
        self,
        request: ali_genieip__1__0_models.AddMessageTemplateRequest,
        headers: ali_genieip__1__0_models.AddMessageTemplateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.AddMessageTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_detail):
            body['TemplateDetail'] = request.template_detail
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddMessageTemplate',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/addMessageTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.AddMessageTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_message_template_with_options_async(
        self,
        request: ali_genieip__1__0_models.AddMessageTemplateRequest,
        headers: ali_genieip__1__0_models.AddMessageTemplateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.AddMessageTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_detail):
            body['TemplateDetail'] = request.template_detail
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddMessageTemplate',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/addMessageTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.AddMessageTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_add_hotel_room(
        self,
        request: ali_genieip__1__0_models.BatchAddHotelRoomRequest,
    ) -> ali_genieip__1__0_models.BatchAddHotelRoomResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.BatchAddHotelRoomHeaders()
        return self.batch_add_hotel_room_with_options(request, headers, runtime)

    async def batch_add_hotel_room_async(
        self,
        request: ali_genieip__1__0_models.BatchAddHotelRoomRequest,
    ) -> ali_genieip__1__0_models.BatchAddHotelRoomResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.BatchAddHotelRoomHeaders()
        return await self.batch_add_hotel_room_with_options_async(request, headers, runtime)

    def batch_add_hotel_room_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.BatchAddHotelRoomRequest,
        headers: ali_genieip__1__0_models.BatchAddHotelRoomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.BatchAddHotelRoomResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.BatchAddHotelRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.room_no_list):
            request.room_no_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_no_list, 'RoomNoList', 'simple')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no_list_shrink):
            body['RoomNoList'] = request.room_no_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchAddHotelRoom',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/batchAddHotelRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.BatchAddHotelRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_add_hotel_room_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.BatchAddHotelRoomRequest,
        headers: ali_genieip__1__0_models.BatchAddHotelRoomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.BatchAddHotelRoomResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.BatchAddHotelRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.room_no_list):
            request.room_no_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_no_list, 'RoomNoList', 'simple')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no_list_shrink):
            body['RoomNoList'] = request.room_no_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchAddHotelRoom',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/batchAddHotelRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.BatchAddHotelRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_hotel_room(
        self,
        request: ali_genieip__1__0_models.BatchDeleteHotelRoomRequest,
    ) -> ali_genieip__1__0_models.BatchDeleteHotelRoomResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.BatchDeleteHotelRoomHeaders()
        return self.batch_delete_hotel_room_with_options(request, headers, runtime)

    async def batch_delete_hotel_room_async(
        self,
        request: ali_genieip__1__0_models.BatchDeleteHotelRoomRequest,
    ) -> ali_genieip__1__0_models.BatchDeleteHotelRoomResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.BatchDeleteHotelRoomHeaders()
        return await self.batch_delete_hotel_room_with_options_async(request, headers, runtime)

    def batch_delete_hotel_room_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.BatchDeleteHotelRoomRequest,
        headers: ali_genieip__1__0_models.BatchDeleteHotelRoomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.BatchDeleteHotelRoomResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.BatchDeleteHotelRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.room_no_list):
            request.room_no_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_no_list, 'RoomNoList', 'simple')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no_list_shrink):
            body['RoomNoList'] = request.room_no_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteHotelRoom',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/batchDeleteHotelRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.BatchDeleteHotelRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_hotel_room_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.BatchDeleteHotelRoomRequest,
        headers: ali_genieip__1__0_models.BatchDeleteHotelRoomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.BatchDeleteHotelRoomResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.BatchDeleteHotelRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.room_no_list):
            request.room_no_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_no_list, 'RoomNoList', 'simple')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no_list_shrink):
            body['RoomNoList'] = request.room_no_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteHotelRoom',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/batchDeleteHotelRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.BatchDeleteHotelRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hotel_alarm(
        self,
        request: ali_genieip__1__0_models.CreateHotelAlarmRequest,
    ) -> ali_genieip__1__0_models.CreateHotelAlarmResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.CreateHotelAlarmHeaders()
        return self.create_hotel_alarm_with_options(request, headers, runtime)

    async def create_hotel_alarm_async(
        self,
        request: ali_genieip__1__0_models.CreateHotelAlarmRequest,
    ) -> ali_genieip__1__0_models.CreateHotelAlarmResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.CreateHotelAlarmHeaders()
        return await self.create_hotel_alarm_with_options_async(request, headers, runtime)

    def create_hotel_alarm_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.CreateHotelAlarmRequest,
        headers: ali_genieip__1__0_models.CreateHotelAlarmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.CreateHotelAlarmResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.CreateHotelAlarmShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rooms):
            request.rooms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rooms, 'Rooms', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_info):
            request.schedule_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.schedule_info), 'ScheduleInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.music_type):
            body['MusicType'] = request.music_type
        if not UtilClient.is_unset(request.rooms_shrink):
            body['Rooms'] = request.rooms_shrink
        if not UtilClient.is_unset(request.schedule_info_shrink):
            body['ScheduleInfo'] = request.schedule_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHotelAlarm',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/createHotelAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.CreateHotelAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hotel_alarm_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.CreateHotelAlarmRequest,
        headers: ali_genieip__1__0_models.CreateHotelAlarmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.CreateHotelAlarmResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.CreateHotelAlarmShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rooms):
            request.rooms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rooms, 'Rooms', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_info):
            request.schedule_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.schedule_info), 'ScheduleInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.music_type):
            body['MusicType'] = request.music_type
        if not UtilClient.is_unset(request.rooms_shrink):
            body['Rooms'] = request.rooms_shrink
        if not UtilClient.is_unset(request.schedule_info_shrink):
            body['ScheduleInfo'] = request.schedule_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHotelAlarm',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/createHotelAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.CreateHotelAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hotel_alarm(
        self,
        request: ali_genieip__1__0_models.DeleteHotelAlarmRequest,
    ) -> ali_genieip__1__0_models.DeleteHotelAlarmResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeleteHotelAlarmHeaders()
        return self.delete_hotel_alarm_with_options(request, headers, runtime)

    async def delete_hotel_alarm_async(
        self,
        request: ali_genieip__1__0_models.DeleteHotelAlarmRequest,
    ) -> ali_genieip__1__0_models.DeleteHotelAlarmResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeleteHotelAlarmHeaders()
        return await self.delete_hotel_alarm_with_options_async(request, headers, runtime)

    def delete_hotel_alarm_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.DeleteHotelAlarmRequest,
        headers: ali_genieip__1__0_models.DeleteHotelAlarmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.DeleteHotelAlarmResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.DeleteHotelAlarmShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alarms):
            request.alarms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alarms, 'Alarms', 'json')
        body = {}
        if not UtilClient.is_unset(request.alarms_shrink):
            body['Alarms'] = request.alarms_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteHotelAlarm',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/deleteHotelAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.DeleteHotelAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hotel_alarm_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.DeleteHotelAlarmRequest,
        headers: ali_genieip__1__0_models.DeleteHotelAlarmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.DeleteHotelAlarmResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.DeleteHotelAlarmShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alarms):
            request.alarms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alarms, 'Alarms', 'json')
        body = {}
        if not UtilClient.is_unset(request.alarms_shrink):
            body['Alarms'] = request.alarms_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteHotelAlarm',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/deleteHotelAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.DeleteHotelAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

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

    def get_hotel_notice(
        self,
        request: ali_genieip__1__0_models.GetHotelNoticeRequest,
    ) -> ali_genieip__1__0_models.GetHotelNoticeResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelNoticeHeaders()
        return self.get_hotel_notice_with_options(request, headers, runtime)

    async def get_hotel_notice_async(
        self,
        request: ali_genieip__1__0_models.GetHotelNoticeRequest,
    ) -> ali_genieip__1__0_models.GetHotelNoticeResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelNoticeHeaders()
        return await self.get_hotel_notice_with_options_async(request, headers, runtime)

    def get_hotel_notice_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelNoticeRequest,
        headers: ali_genieip__1__0_models.GetHotelNoticeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelNoticeResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelNoticeShrinkRequest()
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
            action='GetHotelNotice',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelNotice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelNoticeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotel_notice_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelNoticeRequest,
        headers: ali_genieip__1__0_models.GetHotelNoticeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelNoticeResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelNoticeShrinkRequest()
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
            action='GetHotelNotice',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelNotice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelNoticeResponse(),
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

    def get_hotel_room_device(
        self,
        request: ali_genieip__1__0_models.GetHotelRoomDeviceRequest,
    ) -> ali_genieip__1__0_models.GetHotelRoomDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelRoomDeviceHeaders()
        return self.get_hotel_room_device_with_options(request, headers, runtime)

    async def get_hotel_room_device_async(
        self,
        request: ali_genieip__1__0_models.GetHotelRoomDeviceRequest,
    ) -> ali_genieip__1__0_models.GetHotelRoomDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelRoomDeviceHeaders()
        return await self.get_hotel_room_device_with_options_async(request, headers, runtime)

    def get_hotel_room_device_with_options(
        self,
        request: ali_genieip__1__0_models.GetHotelRoomDeviceRequest,
        headers: ali_genieip__1__0_models.GetHotelRoomDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelRoomDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hotel_id):
            query['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            query['RoomNo'] = request.room_no
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
            action='GetHotelRoomDevice',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelRoomDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelRoomDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotel_room_device_with_options_async(
        self,
        request: ali_genieip__1__0_models.GetHotelRoomDeviceRequest,
        headers: ali_genieip__1__0_models.GetHotelRoomDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelRoomDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hotel_id):
            query['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            query['RoomNo'] = request.room_no
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
            action='GetHotelRoomDevice',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelRoomDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelRoomDeviceResponse(),
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

    def import_room_control_devices(
        self,
        request: ali_genieip__1__0_models.ImportRoomControlDevicesRequest,
    ) -> ali_genieip__1__0_models.ImportRoomControlDevicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ImportRoomControlDevicesHeaders()
        return self.import_room_control_devices_with_options(request, headers, runtime)

    async def import_room_control_devices_async(
        self,
        request: ali_genieip__1__0_models.ImportRoomControlDevicesRequest,
    ) -> ali_genieip__1__0_models.ImportRoomControlDevicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ImportRoomControlDevicesHeaders()
        return await self.import_room_control_devices_with_options_async(request, headers, runtime)

    def import_room_control_devices_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.ImportRoomControlDevicesRequest,
        headers: ali_genieip__1__0_models.ImportRoomControlDevicesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ImportRoomControlDevicesResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ImportRoomControlDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.location_devices):
            request.location_devices_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_devices, 'LocationDevices', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.location_devices_shrink):
            body['LocationDevices'] = request.location_devices_shrink
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportRoomControlDevices',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/importRoomControlDevices',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ImportRoomControlDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_room_control_devices_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.ImportRoomControlDevicesRequest,
        headers: ali_genieip__1__0_models.ImportRoomControlDevicesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ImportRoomControlDevicesResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ImportRoomControlDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.location_devices):
            request.location_devices_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_devices, 'LocationDevices', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.location_devices_shrink):
            body['LocationDevices'] = request.location_devices_shrink
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportRoomControlDevices',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/importRoomControlDevices',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ImportRoomControlDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotel_alarm(
        self,
        request: ali_genieip__1__0_models.ListHotelAlarmRequest,
    ) -> ali_genieip__1__0_models.ListHotelAlarmResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelAlarmHeaders()
        return self.list_hotel_alarm_with_options(request, headers, runtime)

    async def list_hotel_alarm_async(
        self,
        request: ali_genieip__1__0_models.ListHotelAlarmRequest,
    ) -> ali_genieip__1__0_models.ListHotelAlarmResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelAlarmHeaders()
        return await self.list_hotel_alarm_with_options_async(request, headers, runtime)

    def list_hotel_alarm_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelAlarmRequest,
        headers: ali_genieip__1__0_models.ListHotelAlarmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelAlarmResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelAlarmShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rooms):
            request.rooms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rooms, 'Rooms', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.rooms_shrink):
            body['Rooms'] = request.rooms_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotelAlarm',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelAlarmList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotel_alarm_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelAlarmRequest,
        headers: ali_genieip__1__0_models.ListHotelAlarmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelAlarmResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelAlarmShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rooms):
            request.rooms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rooms, 'Rooms', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.rooms_shrink):
            body['Rooms'] = request.rooms_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotelAlarm',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelAlarmList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelAlarmResponse(),
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

    def list_hotel_info(self) -> ali_genieip__1__0_models.ListHotelInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelInfoHeaders()
        return self.list_hotel_info_with_options(headers, runtime)

    async def list_hotel_info_async(self) -> ali_genieip__1__0_models.ListHotelInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelInfoHeaders()
        return await self.list_hotel_info_with_options_async(headers, runtime)

    def list_hotel_info_with_options(
        self,
        headers: ali_genieip__1__0_models.ListHotelInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelInfoResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListHotelInfo',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotel_info_with_options_async(
        self,
        headers: ali_genieip__1__0_models.ListHotelInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelInfoResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListHotelInfo',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotel_message_template(self) -> ali_genieip__1__0_models.ListHotelMessageTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelMessageTemplateHeaders()
        return self.list_hotel_message_template_with_options(headers, runtime)

    async def list_hotel_message_template_async(self) -> ali_genieip__1__0_models.ListHotelMessageTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelMessageTemplateHeaders()
        return await self.list_hotel_message_template_with_options_async(headers, runtime)

    def list_hotel_message_template_with_options(
        self,
        headers: ali_genieip__1__0_models.ListHotelMessageTemplateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelMessageTemplateResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListHotelMessageTemplate',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelMessageTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelMessageTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotel_message_template_with_options_async(
        self,
        headers: ali_genieip__1__0_models.ListHotelMessageTemplateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelMessageTemplateResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListHotelMessageTemplate',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelMessageTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelMessageTemplateResponse(),
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

    def list_hotel_rooms(
        self,
        request: ali_genieip__1__0_models.ListHotelRoomsRequest,
    ) -> ali_genieip__1__0_models.ListHotelRoomsResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelRoomsHeaders()
        return self.list_hotel_rooms_with_options(request, headers, runtime)

    async def list_hotel_rooms_async(
        self,
        request: ali_genieip__1__0_models.ListHotelRoomsRequest,
    ) -> ali_genieip__1__0_models.ListHotelRoomsResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelRoomsHeaders()
        return await self.list_hotel_rooms_with_options_async(request, headers, runtime)

    def list_hotel_rooms_with_options(
        self,
        request: ali_genieip__1__0_models.ListHotelRoomsRequest,
        headers: ali_genieip__1__0_models.ListHotelRoomsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelRoomsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotelRooms',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelRooms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelRoomsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotel_rooms_with_options_async(
        self,
        request: ali_genieip__1__0_models.ListHotelRoomsRequest,
        headers: ali_genieip__1__0_models.ListHotelRoomsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelRoomsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotelRooms',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelRooms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelRoomsResponse(),
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

    def push_hotel_message(
        self,
        request: ali_genieip__1__0_models.PushHotelMessageRequest,
    ) -> ali_genieip__1__0_models.PushHotelMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.PushHotelMessageHeaders()
        return self.push_hotel_message_with_options(request, headers, runtime)

    async def push_hotel_message_async(
        self,
        request: ali_genieip__1__0_models.PushHotelMessageRequest,
    ) -> ali_genieip__1__0_models.PushHotelMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.PushHotelMessageHeaders()
        return await self.push_hotel_message_with_options_async(request, headers, runtime)

    def push_hotel_message_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.PushHotelMessageRequest,
        headers: ali_genieip__1__0_models.PushHotelMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.PushHotelMessageResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.PushHotelMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.push_hotel_message_req):
            request.push_hotel_message_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.push_hotel_message_req), 'PushHotelMessageReq', 'json')
        query = {}
        if not UtilClient.is_unset(request.push_hotel_message_req_shrink):
            query['PushHotelMessageReq'] = request.push_hotel_message_req_shrink
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
            action='PushHotelMessage',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/pushHotelMessage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.PushHotelMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_hotel_message_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.PushHotelMessageRequest,
        headers: ali_genieip__1__0_models.PushHotelMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.PushHotelMessageResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.PushHotelMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.push_hotel_message_req):
            request.push_hotel_message_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.push_hotel_message_req), 'PushHotelMessageReq', 'json')
        query = {}
        if not UtilClient.is_unset(request.push_hotel_message_req_shrink):
            query['PushHotelMessageReq'] = request.push_hotel_message_req_shrink
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
            action='PushHotelMessage',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/pushHotelMessage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.PushHotelMessageResponse(),
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

    def query_room_control_devices(
        self,
        request: ali_genieip__1__0_models.QueryRoomControlDevicesRequest,
    ) -> ali_genieip__1__0_models.QueryRoomControlDevicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.QueryRoomControlDevicesHeaders()
        return self.query_room_control_devices_with_options(request, headers, runtime)

    async def query_room_control_devices_async(
        self,
        request: ali_genieip__1__0_models.QueryRoomControlDevicesRequest,
    ) -> ali_genieip__1__0_models.QueryRoomControlDevicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.QueryRoomControlDevicesHeaders()
        return await self.query_room_control_devices_with_options_async(request, headers, runtime)

    def query_room_control_devices_with_options(
        self,
        request: ali_genieip__1__0_models.QueryRoomControlDevicesRequest,
        headers: ali_genieip__1__0_models.QueryRoomControlDevicesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.QueryRoomControlDevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hotel_id):
            query['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            query['RoomNo'] = request.room_no
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
            action='QueryRoomControlDevices',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/queryRoomControlDevices',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.QueryRoomControlDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_room_control_devices_with_options_async(
        self,
        request: ali_genieip__1__0_models.QueryRoomControlDevicesRequest,
        headers: ali_genieip__1__0_models.QueryRoomControlDevicesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.QueryRoomControlDevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hotel_id):
            query['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            query['RoomNo'] = request.room_no
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
            action='QueryRoomControlDevices',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/queryRoomControlDevices',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.QueryRoomControlDevicesResponse(),
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

    def update_hotel_alarm(
        self,
        request: ali_genieip__1__0_models.UpdateHotelAlarmRequest,
    ) -> ali_genieip__1__0_models.UpdateHotelAlarmResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateHotelAlarmHeaders()
        return self.update_hotel_alarm_with_options(request, headers, runtime)

    async def update_hotel_alarm_async(
        self,
        request: ali_genieip__1__0_models.UpdateHotelAlarmRequest,
    ) -> ali_genieip__1__0_models.UpdateHotelAlarmResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateHotelAlarmHeaders()
        return await self.update_hotel_alarm_with_options_async(request, headers, runtime)

    def update_hotel_alarm_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.UpdateHotelAlarmRequest,
        headers: ali_genieip__1__0_models.UpdateHotelAlarmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.UpdateHotelAlarmResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.UpdateHotelAlarmShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alarms):
            request.alarms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alarms, 'Alarms', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_info):
            request.schedule_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.schedule_info), 'ScheduleInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.alarms_shrink):
            body['Alarms'] = request.alarms_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.schedule_info_shrink):
            body['ScheduleInfo'] = request.schedule_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHotelAlarm',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/updateHotelAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.UpdateHotelAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_hotel_alarm_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.UpdateHotelAlarmRequest,
        headers: ali_genieip__1__0_models.UpdateHotelAlarmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.UpdateHotelAlarmResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.UpdateHotelAlarmShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alarms):
            request.alarms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alarms, 'Alarms', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_info):
            request.schedule_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.schedule_info), 'ScheduleInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.alarms_shrink):
            body['Alarms'] = request.alarms_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.schedule_info_shrink):
            body['ScheduleInfo'] = request.schedule_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHotelAlarm',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/updateHotelAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.UpdateHotelAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )
