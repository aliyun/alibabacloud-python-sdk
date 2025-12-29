# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aligenieip_1_0 import models as main_models
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_cartoon_with_options(
        self,
        request: main_models.AddCartoonRequest,
        headers: main_models.AddCartoonHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AddCartoonResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.start_video_md_5):
            body['StartVideoMd5'] = request.start_video_md_5
        if not DaraCore.is_null(request.start_video_url):
            body['StartVideoUrl'] = request.start_video_url
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddCartoon',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/addCartoon',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCartoonResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_cartoon_with_options_async(
        self,
        request: main_models.AddCartoonRequest,
        headers: main_models.AddCartoonHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AddCartoonResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.start_video_md_5):
            body['StartVideoMd5'] = request.start_video_md_5
        if not DaraCore.is_null(request.start_video_url):
            body['StartVideoUrl'] = request.start_video_url
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddCartoon',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/addCartoon',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCartoonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_cartoon(
        self,
        request: main_models.AddCartoonRequest,
    ) -> main_models.AddCartoonResponse:
        runtime = RuntimeOptions()
        headers = main_models.AddCartoonHeaders()
        return self.add_cartoon_with_options(request, headers, runtime)

    async def add_cartoon_async(
        self,
        request: main_models.AddCartoonRequest,
    ) -> main_models.AddCartoonResponse:
        runtime = RuntimeOptions()
        headers = main_models.AddCartoonHeaders()
        return await self.add_cartoon_with_options_async(request, headers, runtime)

    def add_custom_qawith_options(
        self,
        tmp_req: main_models.AddCustomQARequest,
        headers: main_models.AddCustomQAHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomQAResponse:
        tmp_req.validate()
        request = main_models.AddCustomQAShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.answers):
            request.answers_shrink = Utils.array_to_string_with_specified_style(tmp_req.answers, 'Answers', 'json')
        if not DaraCore.is_null(tmp_req.key_words):
            request.key_words_shrink = Utils.array_to_string_with_specified_style(tmp_req.key_words, 'KeyWords', 'json')
        if not DaraCore.is_null(tmp_req.supplementary_questions):
            request.supplementary_questions_shrink = Utils.array_to_string_with_specified_style(tmp_req.supplementary_questions, 'SupplementaryQuestions', 'json')
        body = {}
        if not DaraCore.is_null(request.answers_shrink):
            body['Answers'] = request.answers_shrink
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.key_words_shrink):
            body['KeyWords'] = request.key_words_shrink
        if not DaraCore.is_null(request.major_question):
            body['MajorQuestion'] = request.major_question
        if not DaraCore.is_null(request.supplementary_questions_shrink):
            body['SupplementaryQuestions'] = request.supplementary_questions_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomQA',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/addCustomQA',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomQAResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_custom_qawith_options_async(
        self,
        tmp_req: main_models.AddCustomQARequest,
        headers: main_models.AddCustomQAHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomQAResponse:
        tmp_req.validate()
        request = main_models.AddCustomQAShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.answers):
            request.answers_shrink = Utils.array_to_string_with_specified_style(tmp_req.answers, 'Answers', 'json')
        if not DaraCore.is_null(tmp_req.key_words):
            request.key_words_shrink = Utils.array_to_string_with_specified_style(tmp_req.key_words, 'KeyWords', 'json')
        if not DaraCore.is_null(tmp_req.supplementary_questions):
            request.supplementary_questions_shrink = Utils.array_to_string_with_specified_style(tmp_req.supplementary_questions, 'SupplementaryQuestions', 'json')
        body = {}
        if not DaraCore.is_null(request.answers_shrink):
            body['Answers'] = request.answers_shrink
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.key_words_shrink):
            body['KeyWords'] = request.key_words_shrink
        if not DaraCore.is_null(request.major_question):
            body['MajorQuestion'] = request.major_question
        if not DaraCore.is_null(request.supplementary_questions_shrink):
            body['SupplementaryQuestions'] = request.supplementary_questions_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomQA',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/addCustomQA',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomQAResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_custom_qa(
        self,
        request: main_models.AddCustomQARequest,
    ) -> main_models.AddCustomQAResponse:
        runtime = RuntimeOptions()
        headers = main_models.AddCustomQAHeaders()
        return self.add_custom_qawith_options(request, headers, runtime)

    async def add_custom_qa_async(
        self,
        request: main_models.AddCustomQARequest,
    ) -> main_models.AddCustomQAResponse:
        runtime = RuntimeOptions()
        headers = main_models.AddCustomQAHeaders()
        return await self.add_custom_qawith_options_async(request, headers, runtime)

    def add_custom_qav2with_options(
        self,
        tmp_req: main_models.AddCustomQAV2Request,
        headers: main_models.AddCustomQAV2Headers,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomQAV2Response:
        tmp_req.validate()
        request = main_models.AddCustomQAV2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.answers):
            request.answers_shrink = Utils.array_to_string_with_specified_style(tmp_req.answers, 'Answers', 'json')
        if not DaraCore.is_null(tmp_req.key_words):
            request.key_words_shrink = Utils.array_to_string_with_specified_style(tmp_req.key_words, 'KeyWords', 'json')
        if not DaraCore.is_null(tmp_req.supplementary_questions):
            request.supplementary_questions_shrink = Utils.array_to_string_with_specified_style(tmp_req.supplementary_questions, 'SupplementaryQuestions', 'json')
        body = {}
        if not DaraCore.is_null(request.answers_shrink):
            body['Answers'] = request.answers_shrink
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.key_words_shrink):
            body['KeyWords'] = request.key_words_shrink
        if not DaraCore.is_null(request.major_question):
            body['MajorQuestion'] = request.major_question
        if not DaraCore.is_null(request.supplementary_questions_shrink):
            body['SupplementaryQuestions'] = request.supplementary_questions_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomQAV2',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/addQAV2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomQAV2Response(),
            self.call_api(params, req, runtime)
        )

    async def add_custom_qav2with_options_async(
        self,
        tmp_req: main_models.AddCustomQAV2Request,
        headers: main_models.AddCustomQAV2Headers,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomQAV2Response:
        tmp_req.validate()
        request = main_models.AddCustomQAV2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.answers):
            request.answers_shrink = Utils.array_to_string_with_specified_style(tmp_req.answers, 'Answers', 'json')
        if not DaraCore.is_null(tmp_req.key_words):
            request.key_words_shrink = Utils.array_to_string_with_specified_style(tmp_req.key_words, 'KeyWords', 'json')
        if not DaraCore.is_null(tmp_req.supplementary_questions):
            request.supplementary_questions_shrink = Utils.array_to_string_with_specified_style(tmp_req.supplementary_questions, 'SupplementaryQuestions', 'json')
        body = {}
        if not DaraCore.is_null(request.answers_shrink):
            body['Answers'] = request.answers_shrink
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.key_words_shrink):
            body['KeyWords'] = request.key_words_shrink
        if not DaraCore.is_null(request.major_question):
            body['MajorQuestion'] = request.major_question
        if not DaraCore.is_null(request.supplementary_questions_shrink):
            body['SupplementaryQuestions'] = request.supplementary_questions_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomQAV2',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/addQAV2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomQAV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def add_custom_qav2(
        self,
        request: main_models.AddCustomQAV2Request,
    ) -> main_models.AddCustomQAV2Response:
        runtime = RuntimeOptions()
        headers = main_models.AddCustomQAV2Headers()
        return self.add_custom_qav2with_options(request, headers, runtime)

    async def add_custom_qav2_async(
        self,
        request: main_models.AddCustomQAV2Request,
    ) -> main_models.AddCustomQAV2Response:
        runtime = RuntimeOptions()
        headers = main_models.AddCustomQAV2Headers()
        return await self.add_custom_qav2with_options_async(request, headers, runtime)

    def add_message_template_with_options(
        self,
        request: main_models.AddMessageTemplateRequest,
        headers: main_models.AddMessageTemplateHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AddMessageTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.template_detail):
            body['TemplateDetail'] = request.template_detail
        if not DaraCore.is_null(request.template_name):
            body['TemplateName'] = request.template_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddMessageTemplate',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/addMessageTemplate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMessageTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_message_template_with_options_async(
        self,
        request: main_models.AddMessageTemplateRequest,
        headers: main_models.AddMessageTemplateHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AddMessageTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.template_detail):
            body['TemplateDetail'] = request.template_detail
        if not DaraCore.is_null(request.template_name):
            body['TemplateName'] = request.template_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddMessageTemplate',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/addMessageTemplate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMessageTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_message_template(
        self,
        request: main_models.AddMessageTemplateRequest,
    ) -> main_models.AddMessageTemplateResponse:
        runtime = RuntimeOptions()
        headers = main_models.AddMessageTemplateHeaders()
        return self.add_message_template_with_options(request, headers, runtime)

    async def add_message_template_async(
        self,
        request: main_models.AddMessageTemplateRequest,
    ) -> main_models.AddMessageTemplateResponse:
        runtime = RuntimeOptions()
        headers = main_models.AddMessageTemplateHeaders()
        return await self.add_message_template_with_options_async(request, headers, runtime)

    def add_or_update_dis_play_modes_with_options(
        self,
        tmp_req: main_models.AddOrUpdateDisPlayModesRequest,
        headers: main_models.AddOrUpdateDisPlayModesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AddOrUpdateDisPlayModesResponse:
        tmp_req.validate()
        request = main_models.AddOrUpdateDisPlayModesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.hotel_device_mode_list):
            request.hotel_device_mode_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.hotel_device_mode_list, 'HotelDeviceModeList', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_device_mode_list_shrink):
            body['HotelDeviceModeList'] = request.hotel_device_mode_list_shrink
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddOrUpdateDisPlayModes',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/addOrUpdateDisPlayModes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddOrUpdateDisPlayModesResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_or_update_dis_play_modes_with_options_async(
        self,
        tmp_req: main_models.AddOrUpdateDisPlayModesRequest,
        headers: main_models.AddOrUpdateDisPlayModesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AddOrUpdateDisPlayModesResponse:
        tmp_req.validate()
        request = main_models.AddOrUpdateDisPlayModesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.hotel_device_mode_list):
            request.hotel_device_mode_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.hotel_device_mode_list, 'HotelDeviceModeList', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_device_mode_list_shrink):
            body['HotelDeviceModeList'] = request.hotel_device_mode_list_shrink
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddOrUpdateDisPlayModes',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/addOrUpdateDisPlayModes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddOrUpdateDisPlayModesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_or_update_dis_play_modes(
        self,
        request: main_models.AddOrUpdateDisPlayModesRequest,
    ) -> main_models.AddOrUpdateDisPlayModesResponse:
        runtime = RuntimeOptions()
        headers = main_models.AddOrUpdateDisPlayModesHeaders()
        return self.add_or_update_dis_play_modes_with_options(request, headers, runtime)

    async def add_or_update_dis_play_modes_async(
        self,
        request: main_models.AddOrUpdateDisPlayModesRequest,
    ) -> main_models.AddOrUpdateDisPlayModesResponse:
        runtime = RuntimeOptions()
        headers = main_models.AddOrUpdateDisPlayModesHeaders()
        return await self.add_or_update_dis_play_modes_with_options_async(request, headers, runtime)

    def add_or_update_hotel_setting_with_options(
        self,
        tmp_req: main_models.AddOrUpdateHotelSettingRequest,
        headers: main_models.AddOrUpdateHotelSettingHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AddOrUpdateHotelSettingResponse:
        tmp_req.validate()
        request = main_models.AddOrUpdateHotelSettingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.hotel_device_mode_list):
            request.hotel_device_mode_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.hotel_device_mode_list, 'HotelDeviceModeList', 'json')
        if not DaraCore.is_null(tmp_req.hotel_screen_saver):
            request.hotel_screen_saver_shrink = Utils.array_to_string_with_specified_style(tmp_req.hotel_screen_saver, 'HotelScreenSaver', 'json')
        if not DaraCore.is_null(tmp_req.night_mode):
            request.night_mode_shrink = Utils.array_to_string_with_specified_style(tmp_req.night_mode, 'NightMode', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_device_mode_list_shrink):
            body['HotelDeviceModeList'] = request.hotel_device_mode_list_shrink
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.hotel_screen_saver_shrink):
            body['HotelScreenSaver'] = request.hotel_screen_saver_shrink
        if not DaraCore.is_null(request.night_mode_shrink):
            body['NightMode'] = request.night_mode_shrink
        if not DaraCore.is_null(request.setting_type):
            body['SettingType'] = request.setting_type
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddOrUpdateHotelSetting',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/addOrUpdateHotelSetting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddOrUpdateHotelSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_or_update_hotel_setting_with_options_async(
        self,
        tmp_req: main_models.AddOrUpdateHotelSettingRequest,
        headers: main_models.AddOrUpdateHotelSettingHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AddOrUpdateHotelSettingResponse:
        tmp_req.validate()
        request = main_models.AddOrUpdateHotelSettingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.hotel_device_mode_list):
            request.hotel_device_mode_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.hotel_device_mode_list, 'HotelDeviceModeList', 'json')
        if not DaraCore.is_null(tmp_req.hotel_screen_saver):
            request.hotel_screen_saver_shrink = Utils.array_to_string_with_specified_style(tmp_req.hotel_screen_saver, 'HotelScreenSaver', 'json')
        if not DaraCore.is_null(tmp_req.night_mode):
            request.night_mode_shrink = Utils.array_to_string_with_specified_style(tmp_req.night_mode, 'NightMode', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_device_mode_list_shrink):
            body['HotelDeviceModeList'] = request.hotel_device_mode_list_shrink
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.hotel_screen_saver_shrink):
            body['HotelScreenSaver'] = request.hotel_screen_saver_shrink
        if not DaraCore.is_null(request.night_mode_shrink):
            body['NightMode'] = request.night_mode_shrink
        if not DaraCore.is_null(request.setting_type):
            body['SettingType'] = request.setting_type
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddOrUpdateHotelSetting',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/addOrUpdateHotelSetting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddOrUpdateHotelSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_or_update_hotel_setting(
        self,
        request: main_models.AddOrUpdateHotelSettingRequest,
    ) -> main_models.AddOrUpdateHotelSettingResponse:
        runtime = RuntimeOptions()
        headers = main_models.AddOrUpdateHotelSettingHeaders()
        return self.add_or_update_hotel_setting_with_options(request, headers, runtime)

    async def add_or_update_hotel_setting_async(
        self,
        request: main_models.AddOrUpdateHotelSettingRequest,
    ) -> main_models.AddOrUpdateHotelSettingResponse:
        runtime = RuntimeOptions()
        headers = main_models.AddOrUpdateHotelSettingHeaders()
        return await self.add_or_update_hotel_setting_with_options_async(request, headers, runtime)

    def add_or_update_screen_saver_with_options(
        self,
        tmp_req: main_models.AddOrUpdateScreenSaverRequest,
        headers: main_models.AddOrUpdateScreenSaverHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AddOrUpdateScreenSaverResponse:
        tmp_req.validate()
        request = main_models.AddOrUpdateScreenSaverShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.hotel_screen_saver):
            request.hotel_screen_saver_shrink = Utils.array_to_string_with_specified_style(tmp_req.hotel_screen_saver, 'HotelScreenSaver', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.hotel_screen_saver_shrink):
            body['HotelScreenSaver'] = request.hotel_screen_saver_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddOrUpdateScreenSaver',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/addOrUpdateScreenSaver',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddOrUpdateScreenSaverResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_or_update_screen_saver_with_options_async(
        self,
        tmp_req: main_models.AddOrUpdateScreenSaverRequest,
        headers: main_models.AddOrUpdateScreenSaverHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AddOrUpdateScreenSaverResponse:
        tmp_req.validate()
        request = main_models.AddOrUpdateScreenSaverShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.hotel_screen_saver):
            request.hotel_screen_saver_shrink = Utils.array_to_string_with_specified_style(tmp_req.hotel_screen_saver, 'HotelScreenSaver', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.hotel_screen_saver_shrink):
            body['HotelScreenSaver'] = request.hotel_screen_saver_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddOrUpdateScreenSaver',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/addOrUpdateScreenSaver',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddOrUpdateScreenSaverResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_or_update_screen_saver(
        self,
        request: main_models.AddOrUpdateScreenSaverRequest,
    ) -> main_models.AddOrUpdateScreenSaverResponse:
        runtime = RuntimeOptions()
        headers = main_models.AddOrUpdateScreenSaverHeaders()
        return self.add_or_update_screen_saver_with_options(request, headers, runtime)

    async def add_or_update_screen_saver_async(
        self,
        request: main_models.AddOrUpdateScreenSaverRequest,
    ) -> main_models.AddOrUpdateScreenSaverResponse:
        runtime = RuntimeOptions()
        headers = main_models.AddOrUpdateScreenSaverHeaders()
        return await self.add_or_update_screen_saver_with_options_async(request, headers, runtime)

    def add_or_update_welcome_text_with_options(
        self,
        request: main_models.AddOrUpdateWelcomeTextRequest,
        headers: main_models.AddOrUpdateWelcomeTextHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AddOrUpdateWelcomeTextResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.music_url):
            body['MusicUrl'] = request.music_url
        if not DaraCore.is_null(request.welcome_text):
            body['WelcomeText'] = request.welcome_text
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddOrUpdateWelcomeText',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/addOrUpdateWelcomeText',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddOrUpdateWelcomeTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_or_update_welcome_text_with_options_async(
        self,
        request: main_models.AddOrUpdateWelcomeTextRequest,
        headers: main_models.AddOrUpdateWelcomeTextHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AddOrUpdateWelcomeTextResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.music_url):
            body['MusicUrl'] = request.music_url
        if not DaraCore.is_null(request.welcome_text):
            body['WelcomeText'] = request.welcome_text
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddOrUpdateWelcomeText',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/addOrUpdateWelcomeText',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddOrUpdateWelcomeTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_or_update_welcome_text(
        self,
        request: main_models.AddOrUpdateWelcomeTextRequest,
    ) -> main_models.AddOrUpdateWelcomeTextResponse:
        runtime = RuntimeOptions()
        headers = main_models.AddOrUpdateWelcomeTextHeaders()
        return self.add_or_update_welcome_text_with_options(request, headers, runtime)

    async def add_or_update_welcome_text_async(
        self,
        request: main_models.AddOrUpdateWelcomeTextRequest,
    ) -> main_models.AddOrUpdateWelcomeTextResponse:
        runtime = RuntimeOptions()
        headers = main_models.AddOrUpdateWelcomeTextHeaders()
        return await self.add_or_update_welcome_text_with_options_async(request, headers, runtime)

    def audit_hotel_with_options(
        self,
        tmp_req: main_models.AuditHotelRequest,
        headers: main_models.AuditHotelHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AuditHotelResponse:
        tmp_req.validate()
        request = main_models.AuditHotelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.audit_hotel_req):
            request.audit_hotel_req_shrink = Utils.array_to_string_with_specified_style(tmp_req.audit_hotel_req, 'AuditHotelReq', 'json')
        query = {}
        if not DaraCore.is_null(request.audit_hotel_req_shrink):
            query['AuditHotelReq'] = request.audit_hotel_req_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuditHotel',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/auditHotel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuditHotelResponse(),
            self.call_api(params, req, runtime)
        )

    async def audit_hotel_with_options_async(
        self,
        tmp_req: main_models.AuditHotelRequest,
        headers: main_models.AuditHotelHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AuditHotelResponse:
        tmp_req.validate()
        request = main_models.AuditHotelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.audit_hotel_req):
            request.audit_hotel_req_shrink = Utils.array_to_string_with_specified_style(tmp_req.audit_hotel_req, 'AuditHotelReq', 'json')
        query = {}
        if not DaraCore.is_null(request.audit_hotel_req_shrink):
            query['AuditHotelReq'] = request.audit_hotel_req_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuditHotel',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/auditHotel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuditHotelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def audit_hotel(
        self,
        request: main_models.AuditHotelRequest,
    ) -> main_models.AuditHotelResponse:
        runtime = RuntimeOptions()
        headers = main_models.AuditHotelHeaders()
        return self.audit_hotel_with_options(request, headers, runtime)

    async def audit_hotel_async(
        self,
        request: main_models.AuditHotelRequest,
    ) -> main_models.AuditHotelResponse:
        runtime = RuntimeOptions()
        headers = main_models.AuditHotelHeaders()
        return await self.audit_hotel_with_options_async(request, headers, runtime)

    def batch_add_hotel_room_with_options(
        self,
        tmp_req: main_models.BatchAddHotelRoomRequest,
        headers: main_models.BatchAddHotelRoomHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.BatchAddHotelRoomResponse:
        tmp_req.validate()
        request = main_models.BatchAddHotelRoomShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.room_no_list):
            request.room_no_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.room_no_list, 'RoomNoList', 'simple')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_no_list_shrink):
            body['RoomNoList'] = request.room_no_list_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchAddHotelRoom',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/batchAddHotelRoom',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchAddHotelRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_add_hotel_room_with_options_async(
        self,
        tmp_req: main_models.BatchAddHotelRoomRequest,
        headers: main_models.BatchAddHotelRoomHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.BatchAddHotelRoomResponse:
        tmp_req.validate()
        request = main_models.BatchAddHotelRoomShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.room_no_list):
            request.room_no_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.room_no_list, 'RoomNoList', 'simple')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_no_list_shrink):
            body['RoomNoList'] = request.room_no_list_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchAddHotelRoom',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/batchAddHotelRoom',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchAddHotelRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_add_hotel_room(
        self,
        request: main_models.BatchAddHotelRoomRequest,
    ) -> main_models.BatchAddHotelRoomResponse:
        runtime = RuntimeOptions()
        headers = main_models.BatchAddHotelRoomHeaders()
        return self.batch_add_hotel_room_with_options(request, headers, runtime)

    async def batch_add_hotel_room_async(
        self,
        request: main_models.BatchAddHotelRoomRequest,
    ) -> main_models.BatchAddHotelRoomResponse:
        runtime = RuntimeOptions()
        headers = main_models.BatchAddHotelRoomHeaders()
        return await self.batch_add_hotel_room_with_options_async(request, headers, runtime)

    def batch_delete_hotel_room_with_options(
        self,
        tmp_req: main_models.BatchDeleteHotelRoomRequest,
        headers: main_models.BatchDeleteHotelRoomHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteHotelRoomResponse:
        tmp_req.validate()
        request = main_models.BatchDeleteHotelRoomShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.room_no_list):
            request.room_no_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.room_no_list, 'RoomNoList', 'simple')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_no_list_shrink):
            body['RoomNoList'] = request.room_no_list_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteHotelRoom',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/batchDeleteHotelRoom',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteHotelRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_hotel_room_with_options_async(
        self,
        tmp_req: main_models.BatchDeleteHotelRoomRequest,
        headers: main_models.BatchDeleteHotelRoomHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteHotelRoomResponse:
        tmp_req.validate()
        request = main_models.BatchDeleteHotelRoomShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.room_no_list):
            request.room_no_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.room_no_list, 'RoomNoList', 'simple')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_no_list_shrink):
            body['RoomNoList'] = request.room_no_list_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteHotelRoom',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/batchDeleteHotelRoom',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteHotelRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_hotel_room(
        self,
        request: main_models.BatchDeleteHotelRoomRequest,
    ) -> main_models.BatchDeleteHotelRoomResponse:
        runtime = RuntimeOptions()
        headers = main_models.BatchDeleteHotelRoomHeaders()
        return self.batch_delete_hotel_room_with_options(request, headers, runtime)

    async def batch_delete_hotel_room_async(
        self,
        request: main_models.BatchDeleteHotelRoomRequest,
    ) -> main_models.BatchDeleteHotelRoomResponse:
        runtime = RuntimeOptions()
        headers = main_models.BatchDeleteHotelRoomHeaders()
        return await self.batch_delete_hotel_room_with_options_async(request, headers, runtime)

    def checkout_with_akwith_options(
        self,
        request: main_models.CheckoutWithAKRequest,
        headers: main_models.CheckoutWithAKHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CheckoutWithAKResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckoutWithAK',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/checkoutWithAK',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckoutWithAKResponse(),
            self.call_api(params, req, runtime)
        )

    async def checkout_with_akwith_options_async(
        self,
        request: main_models.CheckoutWithAKRequest,
        headers: main_models.CheckoutWithAKHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CheckoutWithAKResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckoutWithAK',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/checkoutWithAK',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckoutWithAKResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def checkout_with_ak(
        self,
        request: main_models.CheckoutWithAKRequest,
    ) -> main_models.CheckoutWithAKResponse:
        runtime = RuntimeOptions()
        headers = main_models.CheckoutWithAKHeaders()
        return self.checkout_with_akwith_options(request, headers, runtime)

    async def checkout_with_ak_async(
        self,
        request: main_models.CheckoutWithAKRequest,
    ) -> main_models.CheckoutWithAKResponse:
        runtime = RuntimeOptions()
        headers = main_models.CheckoutWithAKHeaders()
        return await self.checkout_with_akwith_options_async(request, headers, runtime)

    def child_account_auth_with_options(
        self,
        request: main_models.ChildAccountAuthRequest,
        headers: main_models.ChildAccountAuthHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ChildAccountAuthResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account):
            body['Account'] = request.account
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChildAccountAuth',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/childAccountAuth',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChildAccountAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def child_account_auth_with_options_async(
        self,
        request: main_models.ChildAccountAuthRequest,
        headers: main_models.ChildAccountAuthHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ChildAccountAuthResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account):
            body['Account'] = request.account
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChildAccountAuth',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/childAccountAuth',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChildAccountAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def child_account_auth(
        self,
        request: main_models.ChildAccountAuthRequest,
    ) -> main_models.ChildAccountAuthResponse:
        runtime = RuntimeOptions()
        headers = main_models.ChildAccountAuthHeaders()
        return self.child_account_auth_with_options(request, headers, runtime)

    async def child_account_auth_async(
        self,
        request: main_models.ChildAccountAuthRequest,
    ) -> main_models.ChildAccountAuthResponse:
        runtime = RuntimeOptions()
        headers = main_models.ChildAccountAuthHeaders()
        return await self.child_account_auth_with_options_async(request, headers, runtime)

    def control_room_device_with_options(
        self,
        tmp_req: main_models.ControlRoomDeviceRequest,
        headers: main_models.ControlRoomDeviceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ControlRoomDeviceResponse:
        tmp_req.validate()
        request = main_models.ControlRoomDeviceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.properties):
            request.properties_shrink = Utils.array_to_string_with_specified_style(tmp_req.properties, 'Properties', 'json')
        body = {}
        if not DaraCore.is_null(request.cmd):
            body['Cmd'] = request.cmd
        if not DaraCore.is_null(request.device_index):
            body['DeviceIndex'] = request.device_index
        if not DaraCore.is_null(request.device_number):
            body['DeviceNumber'] = request.device_number
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.properties_shrink):
            body['Properties'] = request.properties_shrink
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ControlRoomDevice',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/controlRoomDevice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ControlRoomDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def control_room_device_with_options_async(
        self,
        tmp_req: main_models.ControlRoomDeviceRequest,
        headers: main_models.ControlRoomDeviceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ControlRoomDeviceResponse:
        tmp_req.validate()
        request = main_models.ControlRoomDeviceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.properties):
            request.properties_shrink = Utils.array_to_string_with_specified_style(tmp_req.properties, 'Properties', 'json')
        body = {}
        if not DaraCore.is_null(request.cmd):
            body['Cmd'] = request.cmd
        if not DaraCore.is_null(request.device_index):
            body['DeviceIndex'] = request.device_index
        if not DaraCore.is_null(request.device_number):
            body['DeviceNumber'] = request.device_number
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.properties_shrink):
            body['Properties'] = request.properties_shrink
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ControlRoomDevice',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/controlRoomDevice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ControlRoomDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def control_room_device(
        self,
        request: main_models.ControlRoomDeviceRequest,
    ) -> main_models.ControlRoomDeviceResponse:
        runtime = RuntimeOptions()
        headers = main_models.ControlRoomDeviceHeaders()
        return self.control_room_device_with_options(request, headers, runtime)

    async def control_room_device_async(
        self,
        request: main_models.ControlRoomDeviceRequest,
    ) -> main_models.ControlRoomDeviceResponse:
        runtime = RuntimeOptions()
        headers = main_models.ControlRoomDeviceHeaders()
        return await self.control_room_device_with_options_async(request, headers, runtime)

    def create_hotel_with_options(
        self,
        tmp_req: main_models.CreateHotelRequest,
        headers: main_models.CreateHotelHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHotelResponse:
        tmp_req.validate()
        request = main_models.CreateHotelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.related_pks):
            request.related_pks_shrink = Utils.array_to_string_with_specified_style(tmp_req.related_pks, 'RelatedPks', 'json')
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.est_open_time):
            body['EstOpenTime'] = request.est_open_time
        if not DaraCore.is_null(request.hotel_address):
            body['HotelAddress'] = request.hotel_address
        if not DaraCore.is_null(request.hotel_email):
            body['HotelEmail'] = request.hotel_email
        if not DaraCore.is_null(request.hotel_name):
            body['HotelName'] = request.hotel_name
        if not DaraCore.is_null(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.related_pk):
            body['RelatedPk'] = request.related_pk
        if not DaraCore.is_null(request.related_pks_shrink):
            body['RelatedPks'] = request.related_pks_shrink
        if not DaraCore.is_null(request.remark):
            body['Remark'] = request.remark
        if not DaraCore.is_null(request.room_num):
            body['RoomNum'] = request.room_num
        if not DaraCore.is_null(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateHotel',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/createHotel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHotelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hotel_with_options_async(
        self,
        tmp_req: main_models.CreateHotelRequest,
        headers: main_models.CreateHotelHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHotelResponse:
        tmp_req.validate()
        request = main_models.CreateHotelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.related_pks):
            request.related_pks_shrink = Utils.array_to_string_with_specified_style(tmp_req.related_pks, 'RelatedPks', 'json')
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.est_open_time):
            body['EstOpenTime'] = request.est_open_time
        if not DaraCore.is_null(request.hotel_address):
            body['HotelAddress'] = request.hotel_address
        if not DaraCore.is_null(request.hotel_email):
            body['HotelEmail'] = request.hotel_email
        if not DaraCore.is_null(request.hotel_name):
            body['HotelName'] = request.hotel_name
        if not DaraCore.is_null(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.related_pk):
            body['RelatedPk'] = request.related_pk
        if not DaraCore.is_null(request.related_pks_shrink):
            body['RelatedPks'] = request.related_pks_shrink
        if not DaraCore.is_null(request.remark):
            body['Remark'] = request.remark
        if not DaraCore.is_null(request.room_num):
            body['RoomNum'] = request.room_num
        if not DaraCore.is_null(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateHotel',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/createHotel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHotelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hotel(
        self,
        request: main_models.CreateHotelRequest,
    ) -> main_models.CreateHotelResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateHotelHeaders()
        return self.create_hotel_with_options(request, headers, runtime)

    async def create_hotel_async(
        self,
        request: main_models.CreateHotelRequest,
    ) -> main_models.CreateHotelResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateHotelHeaders()
        return await self.create_hotel_with_options_async(request, headers, runtime)

    def create_hotel_alarm_with_options(
        self,
        tmp_req: main_models.CreateHotelAlarmRequest,
        headers: main_models.CreateHotelAlarmHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHotelAlarmResponse:
        tmp_req.validate()
        request = main_models.CreateHotelAlarmShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rooms):
            request.rooms_shrink = Utils.array_to_string_with_specified_style(tmp_req.rooms, 'Rooms', 'json')
        if not DaraCore.is_null(tmp_req.schedule_info):
            request.schedule_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.schedule_info, 'ScheduleInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.music_type):
            body['MusicType'] = request.music_type
        if not DaraCore.is_null(request.rooms_shrink):
            body['Rooms'] = request.rooms_shrink
        if not DaraCore.is_null(request.schedule_info_shrink):
            body['ScheduleInfo'] = request.schedule_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateHotelAlarm',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/createHotelAlarm',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHotelAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hotel_alarm_with_options_async(
        self,
        tmp_req: main_models.CreateHotelAlarmRequest,
        headers: main_models.CreateHotelAlarmHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHotelAlarmResponse:
        tmp_req.validate()
        request = main_models.CreateHotelAlarmShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rooms):
            request.rooms_shrink = Utils.array_to_string_with_specified_style(tmp_req.rooms, 'Rooms', 'json')
        if not DaraCore.is_null(tmp_req.schedule_info):
            request.schedule_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.schedule_info, 'ScheduleInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.music_type):
            body['MusicType'] = request.music_type
        if not DaraCore.is_null(request.rooms_shrink):
            body['Rooms'] = request.rooms_shrink
        if not DaraCore.is_null(request.schedule_info_shrink):
            body['ScheduleInfo'] = request.schedule_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateHotelAlarm',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/createHotelAlarm',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHotelAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hotel_alarm(
        self,
        request: main_models.CreateHotelAlarmRequest,
    ) -> main_models.CreateHotelAlarmResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateHotelAlarmHeaders()
        return self.create_hotel_alarm_with_options(request, headers, runtime)

    async def create_hotel_alarm_async(
        self,
        request: main_models.CreateHotelAlarmRequest,
    ) -> main_models.CreateHotelAlarmResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateHotelAlarmHeaders()
        return await self.create_hotel_alarm_with_options_async(request, headers, runtime)

    def create_rcu_scene_with_options(
        self,
        tmp_req: main_models.CreateRcuSceneRequest,
        headers: main_models.CreateRcuSceneHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRcuSceneResponse:
        tmp_req.validate()
        request = main_models.CreateRcuSceneShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scene_relation_ext_dto):
            request.scene_relation_ext_dtoshrink = Utils.array_to_string_with_specified_style(tmp_req.scene_relation_ext_dto, 'SceneRelationExtDTO', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.scene_relation_ext_dtoshrink):
            body['SceneRelationExtDTO'] = request.scene_relation_ext_dtoshrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRcuScene',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/createRcuScene',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRcuSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rcu_scene_with_options_async(
        self,
        tmp_req: main_models.CreateRcuSceneRequest,
        headers: main_models.CreateRcuSceneHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRcuSceneResponse:
        tmp_req.validate()
        request = main_models.CreateRcuSceneShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scene_relation_ext_dto):
            request.scene_relation_ext_dtoshrink = Utils.array_to_string_with_specified_style(tmp_req.scene_relation_ext_dto, 'SceneRelationExtDTO', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.scene_relation_ext_dtoshrink):
            body['SceneRelationExtDTO'] = request.scene_relation_ext_dtoshrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRcuScene',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/createRcuScene',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRcuSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rcu_scene(
        self,
        request: main_models.CreateRcuSceneRequest,
    ) -> main_models.CreateRcuSceneResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateRcuSceneHeaders()
        return self.create_rcu_scene_with_options(request, headers, runtime)

    async def create_rcu_scene_async(
        self,
        request: main_models.CreateRcuSceneRequest,
    ) -> main_models.CreateRcuSceneResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateRcuSceneHeaders()
        return await self.create_rcu_scene_with_options_async(request, headers, runtime)

    def delete_cartoon_with_options(
        self,
        request: main_models.DeleteCartoonRequest,
        headers: main_models.DeleteCartoonHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCartoonResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCartoon',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/deleteCartoon',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCartoonResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cartoon_with_options_async(
        self,
        request: main_models.DeleteCartoonRequest,
        headers: main_models.DeleteCartoonHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCartoonResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCartoon',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/deleteCartoon',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCartoonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cartoon(
        self,
        request: main_models.DeleteCartoonRequest,
    ) -> main_models.DeleteCartoonResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteCartoonHeaders()
        return self.delete_cartoon_with_options(request, headers, runtime)

    async def delete_cartoon_async(
        self,
        request: main_models.DeleteCartoonRequest,
    ) -> main_models.DeleteCartoonResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteCartoonHeaders()
        return await self.delete_cartoon_with_options_async(request, headers, runtime)

    def delete_custom_qawith_options(
        self,
        tmp_req: main_models.DeleteCustomQARequest,
        headers: main_models.DeleteCustomQAHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomQAResponse:
        tmp_req.validate()
        request = main_models.DeleteCustomQAShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_qaids):
            request.custom_qaids_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_qaids, 'CustomQAIds', 'json')
        body = {}
        if not DaraCore.is_null(request.custom_qaids_shrink):
            body['CustomQAIds'] = request.custom_qaids_shrink
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomQA',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/deleteCustomQA',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomQAResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_qawith_options_async(
        self,
        tmp_req: main_models.DeleteCustomQARequest,
        headers: main_models.DeleteCustomQAHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomQAResponse:
        tmp_req.validate()
        request = main_models.DeleteCustomQAShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_qaids):
            request.custom_qaids_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_qaids, 'CustomQAIds', 'json')
        body = {}
        if not DaraCore.is_null(request.custom_qaids_shrink):
            body['CustomQAIds'] = request.custom_qaids_shrink
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomQA',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/deleteCustomQA',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomQAResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_qa(
        self,
        request: main_models.DeleteCustomQARequest,
    ) -> main_models.DeleteCustomQAResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteCustomQAHeaders()
        return self.delete_custom_qawith_options(request, headers, runtime)

    async def delete_custom_qa_async(
        self,
        request: main_models.DeleteCustomQARequest,
    ) -> main_models.DeleteCustomQAResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteCustomQAHeaders()
        return await self.delete_custom_qawith_options_async(request, headers, runtime)

    def delete_hotel_alarm_with_options(
        self,
        tmp_req: main_models.DeleteHotelAlarmRequest,
        headers: main_models.DeleteHotelAlarmHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHotelAlarmResponse:
        tmp_req.validate()
        request = main_models.DeleteHotelAlarmShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.alarms):
            request.alarms_shrink = Utils.array_to_string_with_specified_style(tmp_req.alarms, 'Alarms', 'json')
        body = {}
        if not DaraCore.is_null(request.alarms_shrink):
            body['Alarms'] = request.alarms_shrink
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHotelAlarm',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/deleteHotelAlarm',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHotelAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hotel_alarm_with_options_async(
        self,
        tmp_req: main_models.DeleteHotelAlarmRequest,
        headers: main_models.DeleteHotelAlarmHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHotelAlarmResponse:
        tmp_req.validate()
        request = main_models.DeleteHotelAlarmShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.alarms):
            request.alarms_shrink = Utils.array_to_string_with_specified_style(tmp_req.alarms, 'Alarms', 'json')
        body = {}
        if not DaraCore.is_null(request.alarms_shrink):
            body['Alarms'] = request.alarms_shrink
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHotelAlarm',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/deleteHotelAlarm',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHotelAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hotel_alarm(
        self,
        request: main_models.DeleteHotelAlarmRequest,
    ) -> main_models.DeleteHotelAlarmResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteHotelAlarmHeaders()
        return self.delete_hotel_alarm_with_options(request, headers, runtime)

    async def delete_hotel_alarm_async(
        self,
        request: main_models.DeleteHotelAlarmRequest,
    ) -> main_models.DeleteHotelAlarmResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteHotelAlarmHeaders()
        return await self.delete_hotel_alarm_with_options_async(request, headers, runtime)

    def delete_hotel_scene_book_item_with_options(
        self,
        request: main_models.DeleteHotelSceneBookItemRequest,
        headers: main_models.DeleteHotelSceneBookItemHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHotelSceneBookItemResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHotelSceneBookItem',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/deleteHotelSceneBookItem',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHotelSceneBookItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hotel_scene_book_item_with_options_async(
        self,
        request: main_models.DeleteHotelSceneBookItemRequest,
        headers: main_models.DeleteHotelSceneBookItemHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHotelSceneBookItemResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHotelSceneBookItem',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/deleteHotelSceneBookItem',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHotelSceneBookItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hotel_scene_book_item(
        self,
        request: main_models.DeleteHotelSceneBookItemRequest,
    ) -> main_models.DeleteHotelSceneBookItemResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteHotelSceneBookItemHeaders()
        return self.delete_hotel_scene_book_item_with_options(request, headers, runtime)

    async def delete_hotel_scene_book_item_async(
        self,
        request: main_models.DeleteHotelSceneBookItemRequest,
    ) -> main_models.DeleteHotelSceneBookItemResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteHotelSceneBookItemHeaders()
        return await self.delete_hotel_scene_book_item_with_options_async(request, headers, runtime)

    def delete_hotel_setting_with_options(
        self,
        request: main_models.DeleteHotelSettingRequest,
        headers: main_models.DeleteHotelSettingHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHotelSettingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.setting_type):
            body['SettingType'] = request.setting_type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHotelSetting',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/deleteHotelSetting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHotelSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hotel_setting_with_options_async(
        self,
        request: main_models.DeleteHotelSettingRequest,
        headers: main_models.DeleteHotelSettingHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHotelSettingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.setting_type):
            body['SettingType'] = request.setting_type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHotelSetting',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/deleteHotelSetting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHotelSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hotel_setting(
        self,
        request: main_models.DeleteHotelSettingRequest,
    ) -> main_models.DeleteHotelSettingResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteHotelSettingHeaders()
        return self.delete_hotel_setting_with_options(request, headers, runtime)

    async def delete_hotel_setting_async(
        self,
        request: main_models.DeleteHotelSettingRequest,
    ) -> main_models.DeleteHotelSettingResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteHotelSettingHeaders()
        return await self.delete_hotel_setting_with_options_async(request, headers, runtime)

    def delete_message_template_with_options(
        self,
        request: main_models.DeleteMessageTemplateRequest,
        headers: main_models.DeleteMessageTemplateHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMessageTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.template_id):
            body['TemplateId'] = request.template_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMessageTemplate',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/deleteMessageTemplate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMessageTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_message_template_with_options_async(
        self,
        request: main_models.DeleteMessageTemplateRequest,
        headers: main_models.DeleteMessageTemplateHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMessageTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.template_id):
            body['TemplateId'] = request.template_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMessageTemplate',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/deleteMessageTemplate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMessageTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_message_template(
        self,
        request: main_models.DeleteMessageTemplateRequest,
    ) -> main_models.DeleteMessageTemplateResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteMessageTemplateHeaders()
        return self.delete_message_template_with_options(request, headers, runtime)

    async def delete_message_template_async(
        self,
        request: main_models.DeleteMessageTemplateRequest,
    ) -> main_models.DeleteMessageTemplateResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteMessageTemplateHeaders()
        return await self.delete_message_template_with_options_async(request, headers, runtime)

    def delete_rcu_scene_with_options(
        self,
        request: main_models.DeleteRcuSceneRequest,
        headers: main_models.DeleteRcuSceneHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRcuSceneResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRcuScene',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/deleteRcuScene',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRcuSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rcu_scene_with_options_async(
        self,
        request: main_models.DeleteRcuSceneRequest,
        headers: main_models.DeleteRcuSceneHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRcuSceneResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRcuScene',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/deleteRcuScene',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRcuSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rcu_scene(
        self,
        request: main_models.DeleteRcuSceneRequest,
    ) -> main_models.DeleteRcuSceneResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteRcuSceneHeaders()
        return self.delete_rcu_scene_with_options(request, headers, runtime)

    async def delete_rcu_scene_async(
        self,
        request: main_models.DeleteRcuSceneRequest,
    ) -> main_models.DeleteRcuSceneResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteRcuSceneHeaders()
        return await self.delete_rcu_scene_with_options_async(request, headers, runtime)

    def device_control_with_options(
        self,
        tmp_req: main_models.DeviceControlRequest,
        headers: main_models.DeviceControlHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeviceControlResponse:
        tmp_req.validate()
        request = main_models.DeviceControlShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeviceControl',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/deviceControl',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeviceControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def device_control_with_options_async(
        self,
        tmp_req: main_models.DeviceControlRequest,
        headers: main_models.DeviceControlHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeviceControlResponse:
        tmp_req.validate()
        request = main_models.DeviceControlShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeviceControl',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/deviceControl',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeviceControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def device_control(
        self,
        request: main_models.DeviceControlRequest,
    ) -> main_models.DeviceControlResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeviceControlHeaders()
        return self.device_control_with_options(request, headers, runtime)

    async def device_control_async(
        self,
        request: main_models.DeviceControlRequest,
    ) -> main_models.DeviceControlResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeviceControlHeaders()
        return await self.device_control_with_options_async(request, headers, runtime)

    def execute_scene_with_options(
        self,
        request: main_models.ExecuteSceneRequest,
        headers: main_models.ExecuteSceneHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteSceneResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        if not DaraCore.is_null(request.scene_name):
            body['SceneName'] = request.scene_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteScene',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/executeScene',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_scene_with_options_async(
        self,
        request: main_models.ExecuteSceneRequest,
        headers: main_models.ExecuteSceneHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteSceneResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        if not DaraCore.is_null(request.scene_name):
            body['SceneName'] = request.scene_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteScene',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/executeScene',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_scene(
        self,
        request: main_models.ExecuteSceneRequest,
    ) -> main_models.ExecuteSceneResponse:
        runtime = RuntimeOptions()
        headers = main_models.ExecuteSceneHeaders()
        return self.execute_scene_with_options(request, headers, runtime)

    async def execute_scene_async(
        self,
        request: main_models.ExecuteSceneRequest,
    ) -> main_models.ExecuteSceneResponse:
        runtime = RuntimeOptions()
        headers = main_models.ExecuteSceneHeaders()
        return await self.execute_scene_with_options_async(request, headers, runtime)

    def get_basic_info_qawith_options(
        self,
        request: main_models.GetBasicInfoQARequest,
        headers: main_models.GetBasicInfoQAHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetBasicInfoQAResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetBasicInfoQA',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getBasicInfoQA',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBasicInfoQAResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_basic_info_qawith_options_async(
        self,
        request: main_models.GetBasicInfoQARequest,
        headers: main_models.GetBasicInfoQAHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetBasicInfoQAResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetBasicInfoQA',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getBasicInfoQA',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBasicInfoQAResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_basic_info_qa(
        self,
        request: main_models.GetBasicInfoQARequest,
    ) -> main_models.GetBasicInfoQAResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetBasicInfoQAHeaders()
        return self.get_basic_info_qawith_options(request, headers, runtime)

    async def get_basic_info_qa_async(
        self,
        request: main_models.GetBasicInfoQARequest,
    ) -> main_models.GetBasicInfoQAResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetBasicInfoQAHeaders()
        return await self.get_basic_info_qawith_options_async(request, headers, runtime)

    def get_cartoon_with_options(
        self,
        request: main_models.GetCartoonRequest,
        headers: main_models.GetCartoonHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetCartoonResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCartoon',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getCartoon',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCartoonResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cartoon_with_options_async(
        self,
        request: main_models.GetCartoonRequest,
        headers: main_models.GetCartoonHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetCartoonResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCartoon',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getCartoon',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCartoonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cartoon(
        self,
        request: main_models.GetCartoonRequest,
    ) -> main_models.GetCartoonResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetCartoonHeaders()
        return self.get_cartoon_with_options(request, headers, runtime)

    async def get_cartoon_async(
        self,
        request: main_models.GetCartoonRequest,
    ) -> main_models.GetCartoonResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetCartoonHeaders()
        return await self.get_cartoon_with_options_async(request, headers, runtime)

    def get_hotel_contact_by_genie_device_with_options(
        self,
        tmp_req: main_models.GetHotelContactByGenieDeviceRequest,
        headers: main_models.GetHotelContactByGenieDeviceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelContactByGenieDeviceResponse:
        tmp_req.validate()
        request = main_models.GetHotelContactByGenieDeviceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelContactByGenieDevice',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelContactByGenieDevice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelContactByGenieDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotel_contact_by_genie_device_with_options_async(
        self,
        tmp_req: main_models.GetHotelContactByGenieDeviceRequest,
        headers: main_models.GetHotelContactByGenieDeviceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelContactByGenieDeviceResponse:
        tmp_req.validate()
        request = main_models.GetHotelContactByGenieDeviceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelContactByGenieDevice',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelContactByGenieDevice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelContactByGenieDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotel_contact_by_genie_device(
        self,
        request: main_models.GetHotelContactByGenieDeviceRequest,
    ) -> main_models.GetHotelContactByGenieDeviceResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelContactByGenieDeviceHeaders()
        return self.get_hotel_contact_by_genie_device_with_options(request, headers, runtime)

    async def get_hotel_contact_by_genie_device_async(
        self,
        request: main_models.GetHotelContactByGenieDeviceRequest,
    ) -> main_models.GetHotelContactByGenieDeviceResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelContactByGenieDeviceHeaders()
        return await self.get_hotel_contact_by_genie_device_with_options_async(request, headers, runtime)

    def get_hotel_contact_by_number_with_options(
        self,
        tmp_req: main_models.GetHotelContactByNumberRequest,
        headers: main_models.GetHotelContactByNumberHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelContactByNumberResponse:
        tmp_req.validate()
        request = main_models.GetHotelContactByNumberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.number):
            body['Number'] = request.number
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelContactByNumber',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelContactByNumber',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelContactByNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotel_contact_by_number_with_options_async(
        self,
        tmp_req: main_models.GetHotelContactByNumberRequest,
        headers: main_models.GetHotelContactByNumberHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelContactByNumberResponse:
        tmp_req.validate()
        request = main_models.GetHotelContactByNumberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.number):
            body['Number'] = request.number
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelContactByNumber',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelContactByNumber',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelContactByNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotel_contact_by_number(
        self,
        request: main_models.GetHotelContactByNumberRequest,
    ) -> main_models.GetHotelContactByNumberResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelContactByNumberHeaders()
        return self.get_hotel_contact_by_number_with_options(request, headers, runtime)

    async def get_hotel_contact_by_number_async(
        self,
        request: main_models.GetHotelContactByNumberRequest,
    ) -> main_models.GetHotelContactByNumberResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelContactByNumberHeaders()
        return await self.get_hotel_contact_by_number_with_options_async(request, headers, runtime)

    def get_hotel_contacts_with_options(
        self,
        tmp_req: main_models.GetHotelContactsRequest,
        headers: main_models.GetHotelContactsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelContactsResponse:
        tmp_req.validate()
        request = main_models.GetHotelContactsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelContacts',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelContacts',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelContactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotel_contacts_with_options_async(
        self,
        tmp_req: main_models.GetHotelContactsRequest,
        headers: main_models.GetHotelContactsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelContactsResponse:
        tmp_req.validate()
        request = main_models.GetHotelContactsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelContacts',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelContacts',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelContactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotel_contacts(
        self,
        request: main_models.GetHotelContactsRequest,
    ) -> main_models.GetHotelContactsResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelContactsHeaders()
        return self.get_hotel_contacts_with_options(request, headers, runtime)

    async def get_hotel_contacts_async(
        self,
        request: main_models.GetHotelContactsRequest,
    ) -> main_models.GetHotelContactsResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelContactsHeaders()
        return await self.get_hotel_contacts_with_options_async(request, headers, runtime)

    def get_hotel_home_back_image_and_modes_with_options(
        self,
        tmp_req: main_models.GetHotelHomeBackImageAndModesRequest,
        headers: main_models.GetHotelHomeBackImageAndModesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelHomeBackImageAndModesResponse:
        tmp_req.validate()
        request = main_models.GetHotelHomeBackImageAndModesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelHomeBackImageAndModes',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelHomeBackImageAndModes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelHomeBackImageAndModesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotel_home_back_image_and_modes_with_options_async(
        self,
        tmp_req: main_models.GetHotelHomeBackImageAndModesRequest,
        headers: main_models.GetHotelHomeBackImageAndModesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelHomeBackImageAndModesResponse:
        tmp_req.validate()
        request = main_models.GetHotelHomeBackImageAndModesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelHomeBackImageAndModes',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelHomeBackImageAndModes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelHomeBackImageAndModesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotel_home_back_image_and_modes(
        self,
        request: main_models.GetHotelHomeBackImageAndModesRequest,
    ) -> main_models.GetHotelHomeBackImageAndModesResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelHomeBackImageAndModesHeaders()
        return self.get_hotel_home_back_image_and_modes_with_options(request, headers, runtime)

    async def get_hotel_home_back_image_and_modes_async(
        self,
        request: main_models.GetHotelHomeBackImageAndModesRequest,
    ) -> main_models.GetHotelHomeBackImageAndModesResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelHomeBackImageAndModesHeaders()
        return await self.get_hotel_home_back_image_and_modes_with_options_async(request, headers, runtime)

    def get_hotel_notice_with_options(
        self,
        tmp_req: main_models.GetHotelNoticeRequest,
        headers: main_models.GetHotelNoticeHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelNoticeResponse:
        tmp_req.validate()
        request = main_models.GetHotelNoticeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelNotice',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelNotice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelNoticeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotel_notice_with_options_async(
        self,
        tmp_req: main_models.GetHotelNoticeRequest,
        headers: main_models.GetHotelNoticeHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelNoticeResponse:
        tmp_req.validate()
        request = main_models.GetHotelNoticeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelNotice',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelNotice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelNoticeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotel_notice(
        self,
        request: main_models.GetHotelNoticeRequest,
    ) -> main_models.GetHotelNoticeResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelNoticeHeaders()
        return self.get_hotel_notice_with_options(request, headers, runtime)

    async def get_hotel_notice_async(
        self,
        request: main_models.GetHotelNoticeRequest,
    ) -> main_models.GetHotelNoticeResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelNoticeHeaders()
        return await self.get_hotel_notice_with_options_async(request, headers, runtime)

    def get_hotel_notice_v2with_options(
        self,
        tmp_req: main_models.GetHotelNoticeV2Request,
        headers: main_models.GetHotelNoticeV2Headers,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelNoticeV2Response:
        tmp_req.validate()
        request = main_models.GetHotelNoticeV2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelNoticeV2',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelNoticeV2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelNoticeV2Response(),
            self.call_api(params, req, runtime)
        )

    async def get_hotel_notice_v2with_options_async(
        self,
        tmp_req: main_models.GetHotelNoticeV2Request,
        headers: main_models.GetHotelNoticeV2Headers,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelNoticeV2Response:
        tmp_req.validate()
        request = main_models.GetHotelNoticeV2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelNoticeV2',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelNoticeV2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelNoticeV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotel_notice_v2(
        self,
        request: main_models.GetHotelNoticeV2Request,
    ) -> main_models.GetHotelNoticeV2Response:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelNoticeV2Headers()
        return self.get_hotel_notice_v2with_options(request, headers, runtime)

    async def get_hotel_notice_v2_async(
        self,
        request: main_models.GetHotelNoticeV2Request,
    ) -> main_models.GetHotelNoticeV2Response:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelNoticeV2Headers()
        return await self.get_hotel_notice_v2with_options_async(request, headers, runtime)

    def get_hotel_order_detail_with_options(
        self,
        tmp_req: main_models.GetHotelOrderDetailRequest,
        headers: main_models.GetHotelOrderDetailHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelOrderDetailResponse:
        tmp_req.validate()
        request = main_models.GetHotelOrderDetailShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        query = {}
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelOrderDetail',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelOrderDetail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelOrderDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotel_order_detail_with_options_async(
        self,
        tmp_req: main_models.GetHotelOrderDetailRequest,
        headers: main_models.GetHotelOrderDetailHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelOrderDetailResponse:
        tmp_req.validate()
        request = main_models.GetHotelOrderDetailShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        query = {}
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelOrderDetail',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelOrderDetail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelOrderDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotel_order_detail(
        self,
        request: main_models.GetHotelOrderDetailRequest,
    ) -> main_models.GetHotelOrderDetailResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelOrderDetailHeaders()
        return self.get_hotel_order_detail_with_options(request, headers, runtime)

    async def get_hotel_order_detail_async(
        self,
        request: main_models.GetHotelOrderDetailRequest,
    ) -> main_models.GetHotelOrderDetailResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelOrderDetailHeaders()
        return await self.get_hotel_order_detail_with_options_async(request, headers, runtime)

    def get_hotel_room_device_with_options(
        self,
        request: main_models.GetHotelRoomDeviceRequest,
        headers: main_models.GetHotelRoomDeviceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelRoomDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hotel_id):
            query['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_no):
            query['RoomNo'] = request.room_no
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelRoomDevice',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelRoomDevice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelRoomDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotel_room_device_with_options_async(
        self,
        request: main_models.GetHotelRoomDeviceRequest,
        headers: main_models.GetHotelRoomDeviceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelRoomDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hotel_id):
            query['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_no):
            query['RoomNo'] = request.room_no
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelRoomDevice',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelRoomDevice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelRoomDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotel_room_device(
        self,
        request: main_models.GetHotelRoomDeviceRequest,
    ) -> main_models.GetHotelRoomDeviceResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelRoomDeviceHeaders()
        return self.get_hotel_room_device_with_options(request, headers, runtime)

    async def get_hotel_room_device_async(
        self,
        request: main_models.GetHotelRoomDeviceRequest,
    ) -> main_models.GetHotelRoomDeviceResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelRoomDeviceHeaders()
        return await self.get_hotel_room_device_with_options_async(request, headers, runtime)

    def get_hotel_sample_utterances_with_options(
        self,
        tmp_req: main_models.GetHotelSampleUtterancesRequest,
        headers: main_models.GetHotelSampleUtterancesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelSampleUtterancesResponse:
        tmp_req.validate()
        request = main_models.GetHotelSampleUtterancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelSampleUtterances',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelSampleUtterances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelSampleUtterancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotel_sample_utterances_with_options_async(
        self,
        tmp_req: main_models.GetHotelSampleUtterancesRequest,
        headers: main_models.GetHotelSampleUtterancesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelSampleUtterancesResponse:
        tmp_req.validate()
        request = main_models.GetHotelSampleUtterancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelSampleUtterances',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelSampleUtterances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelSampleUtterancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotel_sample_utterances(
        self,
        request: main_models.GetHotelSampleUtterancesRequest,
    ) -> main_models.GetHotelSampleUtterancesResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelSampleUtterancesHeaders()
        return self.get_hotel_sample_utterances_with_options(request, headers, runtime)

    async def get_hotel_sample_utterances_async(
        self,
        request: main_models.GetHotelSampleUtterancesRequest,
    ) -> main_models.GetHotelSampleUtterancesResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelSampleUtterancesHeaders()
        return await self.get_hotel_sample_utterances_with_options_async(request, headers, runtime)

    def get_hotel_scene_item_detail_with_options(
        self,
        request: main_models.GetHotelSceneItemDetailRequest,
        headers: main_models.GetHotelSceneItemDetailHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelSceneItemDetailResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.item_id):
            body['ItemId'] = request.item_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelSceneItemDetail',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelSceneItemDetail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelSceneItemDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotel_scene_item_detail_with_options_async(
        self,
        request: main_models.GetHotelSceneItemDetailRequest,
        headers: main_models.GetHotelSceneItemDetailHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelSceneItemDetailResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.item_id):
            body['ItemId'] = request.item_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelSceneItemDetail',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelSceneItemDetail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelSceneItemDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotel_scene_item_detail(
        self,
        request: main_models.GetHotelSceneItemDetailRequest,
    ) -> main_models.GetHotelSceneItemDetailResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelSceneItemDetailHeaders()
        return self.get_hotel_scene_item_detail_with_options(request, headers, runtime)

    async def get_hotel_scene_item_detail_async(
        self,
        request: main_models.GetHotelSceneItemDetailRequest,
    ) -> main_models.GetHotelSceneItemDetailResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelSceneItemDetailHeaders()
        return await self.get_hotel_scene_item_detail_with_options_async(request, headers, runtime)

    def get_hotel_screen_saver_with_options(
        self,
        tmp_req: main_models.GetHotelScreenSaverRequest,
        headers: main_models.GetHotelScreenSaverHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelScreenSaverResponse:
        tmp_req.validate()
        request = main_models.GetHotelScreenSaverShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelScreenSaver',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelScreenSaver',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelScreenSaverResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotel_screen_saver_with_options_async(
        self,
        tmp_req: main_models.GetHotelScreenSaverRequest,
        headers: main_models.GetHotelScreenSaverHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelScreenSaverResponse:
        tmp_req.validate()
        request = main_models.GetHotelScreenSaverShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelScreenSaver',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelScreenSaver',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelScreenSaverResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotel_screen_saver(
        self,
        request: main_models.GetHotelScreenSaverRequest,
    ) -> main_models.GetHotelScreenSaverResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelScreenSaverHeaders()
        return self.get_hotel_screen_saver_with_options(request, headers, runtime)

    async def get_hotel_screen_saver_async(
        self,
        request: main_models.GetHotelScreenSaverRequest,
    ) -> main_models.GetHotelScreenSaverResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelScreenSaverHeaders()
        return await self.get_hotel_screen_saver_with_options_async(request, headers, runtime)

    def get_hotel_screen_saver_style_with_options(
        self,
        request: main_models.GetHotelScreenSaverStyleRequest,
        headers: main_models.GetHotelScreenSaverStyleHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelScreenSaverStyleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelScreenSaverStyle',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelScreenSaverStyle',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelScreenSaverStyleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotel_screen_saver_style_with_options_async(
        self,
        request: main_models.GetHotelScreenSaverStyleRequest,
        headers: main_models.GetHotelScreenSaverStyleHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelScreenSaverStyleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelScreenSaverStyle',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelScreenSaverStyle',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelScreenSaverStyleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotel_screen_saver_style(
        self,
        request: main_models.GetHotelScreenSaverStyleRequest,
    ) -> main_models.GetHotelScreenSaverStyleResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelScreenSaverStyleHeaders()
        return self.get_hotel_screen_saver_style_with_options(request, headers, runtime)

    async def get_hotel_screen_saver_style_async(
        self,
        request: main_models.GetHotelScreenSaverStyleRequest,
    ) -> main_models.GetHotelScreenSaverStyleResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelScreenSaverStyleHeaders()
        return await self.get_hotel_screen_saver_style_with_options_async(request, headers, runtime)

    def get_hotel_setting_with_options(
        self,
        request: main_models.GetHotelSettingRequest,
        headers: main_models.GetHotelSettingHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelSettingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.setting_type):
            body['SettingType'] = request.setting_type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelSetting',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelSetting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotel_setting_with_options_async(
        self,
        request: main_models.GetHotelSettingRequest,
        headers: main_models.GetHotelSettingHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotelSettingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.setting_type):
            body['SettingType'] = request.setting_type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotelSetting',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelSetting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotelSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotel_setting(
        self,
        request: main_models.GetHotelSettingRequest,
    ) -> main_models.GetHotelSettingResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelSettingHeaders()
        return self.get_hotel_setting_with_options(request, headers, runtime)

    async def get_hotel_setting_async(
        self,
        request: main_models.GetHotelSettingRequest,
    ) -> main_models.GetHotelSettingResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotelSettingHeaders()
        return await self.get_hotel_setting_with_options_async(request, headers, runtime)

    def get_relation_product_list_with_options(
        self,
        headers: main_models.GetRelationProductListHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetRelationProductListResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetRelationProductList',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getRelationProductList',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRelationProductListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_relation_product_list_with_options_async(
        self,
        headers: main_models.GetRelationProductListHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetRelationProductListResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetRelationProductList',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getRelationProductList',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRelationProductListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_relation_product_list(self) -> main_models.GetRelationProductListResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetRelationProductListHeaders()
        return self.get_relation_product_list_with_options(headers, runtime)

    async def get_relation_product_list_async(self) -> main_models.GetRelationProductListResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetRelationProductListHeaders()
        return await self.get_relation_product_list_with_options_async(headers, runtime)

    def get_union_id_with_options(
        self,
        request: main_models.GetUnionIdRequest,
        headers: main_models.GetUnionIdHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetUnionIdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.encode_key):
            body['EncodeKey'] = request.encode_key
        if not DaraCore.is_null(request.encode_type):
            body['EncodeType'] = request.encode_type
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.id_type):
            body['IdType'] = request.id_type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUnionId',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getUnionId',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUnionIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_union_id_with_options_async(
        self,
        request: main_models.GetUnionIdRequest,
        headers: main_models.GetUnionIdHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetUnionIdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.encode_key):
            body['EncodeKey'] = request.encode_key
        if not DaraCore.is_null(request.encode_type):
            body['EncodeType'] = request.encode_type
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.id_type):
            body['IdType'] = request.id_type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUnionId',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getUnionId',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUnionIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_union_id(
        self,
        request: main_models.GetUnionIdRequest,
    ) -> main_models.GetUnionIdResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetUnionIdHeaders()
        return self.get_union_id_with_options(request, headers, runtime)

    async def get_union_id_async(
        self,
        request: main_models.GetUnionIdRequest,
    ) -> main_models.GetUnionIdResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetUnionIdHeaders()
        return await self.get_union_id_with_options_async(request, headers, runtime)

    def get_welcome_text_and_music_with_options(
        self,
        request: main_models.GetWelcomeTextAndMusicRequest,
        headers: main_models.GetWelcomeTextAndMusicHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetWelcomeTextAndMusicResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetWelcomeTextAndMusic',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getWelcomeTextAndMusic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWelcomeTextAndMusicResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_welcome_text_and_music_with_options_async(
        self,
        request: main_models.GetWelcomeTextAndMusicRequest,
        headers: main_models.GetWelcomeTextAndMusicHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetWelcomeTextAndMusicResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetWelcomeTextAndMusic',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getWelcomeTextAndMusic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWelcomeTextAndMusicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_welcome_text_and_music(
        self,
        request: main_models.GetWelcomeTextAndMusicRequest,
    ) -> main_models.GetWelcomeTextAndMusicResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetWelcomeTextAndMusicHeaders()
        return self.get_welcome_text_and_music_with_options(request, headers, runtime)

    async def get_welcome_text_and_music_async(
        self,
        request: main_models.GetWelcomeTextAndMusicRequest,
    ) -> main_models.GetWelcomeTextAndMusicResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetWelcomeTextAndMusicHeaders()
        return await self.get_welcome_text_and_music_with_options_async(request, headers, runtime)

    def hotel_qr_bind_with_options(
        self,
        request: main_models.HotelQrBindRequest,
        headers: main_models.HotelQrBindHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.HotelQrBindResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.code):
            body['Code'] = request.code
        if not DaraCore.is_null(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'HotelQrBind',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/hotelQrBind',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HotelQrBindResponse(),
            self.call_api(params, req, runtime)
        )

    async def hotel_qr_bind_with_options_async(
        self,
        request: main_models.HotelQrBindRequest,
        headers: main_models.HotelQrBindHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.HotelQrBindResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.code):
            body['Code'] = request.code
        if not DaraCore.is_null(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'HotelQrBind',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/hotelQrBind',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HotelQrBindResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hotel_qr_bind(
        self,
        request: main_models.HotelQrBindRequest,
    ) -> main_models.HotelQrBindResponse:
        runtime = RuntimeOptions()
        headers = main_models.HotelQrBindHeaders()
        return self.hotel_qr_bind_with_options(request, headers, runtime)

    async def hotel_qr_bind_async(
        self,
        request: main_models.HotelQrBindRequest,
    ) -> main_models.HotelQrBindResponse:
        runtime = RuntimeOptions()
        headers = main_models.HotelQrBindHeaders()
        return await self.hotel_qr_bind_with_options_async(request, headers, runtime)

    def import_hotel_config_with_options(
        self,
        tmp_req: main_models.ImportHotelConfigRequest,
        headers: main_models.ImportHotelConfigHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ImportHotelConfigResponse:
        tmp_req.validate()
        request = main_models.ImportHotelConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.import_hotel_config):
            request.import_hotel_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.import_hotel_config, 'ImportHotelConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.import_hotel_config_shrink):
            body['ImportHotelConfig'] = request.import_hotel_config_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportHotelConfig',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/importHotelConfig',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportHotelConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_hotel_config_with_options_async(
        self,
        tmp_req: main_models.ImportHotelConfigRequest,
        headers: main_models.ImportHotelConfigHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ImportHotelConfigResponse:
        tmp_req.validate()
        request = main_models.ImportHotelConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.import_hotel_config):
            request.import_hotel_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.import_hotel_config, 'ImportHotelConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.import_hotel_config_shrink):
            body['ImportHotelConfig'] = request.import_hotel_config_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportHotelConfig',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/importHotelConfig',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportHotelConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_hotel_config(
        self,
        request: main_models.ImportHotelConfigRequest,
    ) -> main_models.ImportHotelConfigResponse:
        runtime = RuntimeOptions()
        headers = main_models.ImportHotelConfigHeaders()
        return self.import_hotel_config_with_options(request, headers, runtime)

    async def import_hotel_config_async(
        self,
        request: main_models.ImportHotelConfigRequest,
    ) -> main_models.ImportHotelConfigResponse:
        runtime = RuntimeOptions()
        headers = main_models.ImportHotelConfigHeaders()
        return await self.import_hotel_config_with_options_async(request, headers, runtime)

    def import_room_control_devices_with_options(
        self,
        tmp_req: main_models.ImportRoomControlDevicesRequest,
        headers: main_models.ImportRoomControlDevicesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ImportRoomControlDevicesResponse:
        tmp_req.validate()
        request = main_models.ImportRoomControlDevicesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.location_devices):
            request.location_devices_shrink = Utils.array_to_string_with_specified_style(tmp_req.location_devices, 'LocationDevices', 'json')
        body = {}
        if not DaraCore.is_null(request.enable_infrared_device_import):
            body['EnableInfraredDeviceImport'] = request.enable_infrared_device_import
        if not DaraCore.is_null(request.enable_mesh_device_import):
            body['EnableMeshDeviceImport'] = request.enable_mesh_device_import
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.location_devices_shrink):
            body['LocationDevices'] = request.location_devices_shrink
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportRoomControlDevices',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/importRoomControlDevices',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportRoomControlDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_room_control_devices_with_options_async(
        self,
        tmp_req: main_models.ImportRoomControlDevicesRequest,
        headers: main_models.ImportRoomControlDevicesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ImportRoomControlDevicesResponse:
        tmp_req.validate()
        request = main_models.ImportRoomControlDevicesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.location_devices):
            request.location_devices_shrink = Utils.array_to_string_with_specified_style(tmp_req.location_devices, 'LocationDevices', 'json')
        body = {}
        if not DaraCore.is_null(request.enable_infrared_device_import):
            body['EnableInfraredDeviceImport'] = request.enable_infrared_device_import
        if not DaraCore.is_null(request.enable_mesh_device_import):
            body['EnableMeshDeviceImport'] = request.enable_mesh_device_import
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.location_devices_shrink):
            body['LocationDevices'] = request.location_devices_shrink
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportRoomControlDevices',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/importRoomControlDevices',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportRoomControlDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_room_control_devices(
        self,
        request: main_models.ImportRoomControlDevicesRequest,
    ) -> main_models.ImportRoomControlDevicesResponse:
        runtime = RuntimeOptions()
        headers = main_models.ImportRoomControlDevicesHeaders()
        return self.import_room_control_devices_with_options(request, headers, runtime)

    async def import_room_control_devices_async(
        self,
        request: main_models.ImportRoomControlDevicesRequest,
    ) -> main_models.ImportRoomControlDevicesResponse:
        runtime = RuntimeOptions()
        headers = main_models.ImportRoomControlDevicesHeaders()
        return await self.import_room_control_devices_with_options_async(request, headers, runtime)

    def import_room_genie_scenes_with_options(
        self,
        tmp_req: main_models.ImportRoomGenieScenesRequest,
        headers: main_models.ImportRoomGenieScenesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ImportRoomGenieScenesResponse:
        tmp_req.validate()
        request = main_models.ImportRoomGenieScenesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scene_list):
            request.scene_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.scene_list, 'SceneList', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        if not DaraCore.is_null(request.scene_list_shrink):
            body['SceneList'] = request.scene_list_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportRoomGenieScenes',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/importRoomGenieScenes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportRoomGenieScenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_room_genie_scenes_with_options_async(
        self,
        tmp_req: main_models.ImportRoomGenieScenesRequest,
        headers: main_models.ImportRoomGenieScenesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ImportRoomGenieScenesResponse:
        tmp_req.validate()
        request = main_models.ImportRoomGenieScenesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scene_list):
            request.scene_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.scene_list, 'SceneList', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        if not DaraCore.is_null(request.scene_list_shrink):
            body['SceneList'] = request.scene_list_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportRoomGenieScenes',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/importRoomGenieScenes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportRoomGenieScenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_room_genie_scenes(
        self,
        request: main_models.ImportRoomGenieScenesRequest,
    ) -> main_models.ImportRoomGenieScenesResponse:
        runtime = RuntimeOptions()
        headers = main_models.ImportRoomGenieScenesHeaders()
        return self.import_room_genie_scenes_with_options(request, headers, runtime)

    async def import_room_genie_scenes_async(
        self,
        request: main_models.ImportRoomGenieScenesRequest,
    ) -> main_models.ImportRoomGenieScenesResponse:
        runtime = RuntimeOptions()
        headers = main_models.ImportRoomGenieScenesHeaders()
        return await self.import_room_genie_scenes_with_options_async(request, headers, runtime)

    def insert_hotel_scene_book_item_with_options(
        self,
        tmp_req: main_models.InsertHotelSceneBookItemRequest,
        headers: main_models.InsertHotelSceneBookItemHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.InsertHotelSceneBookItemResponse:
        tmp_req.validate()
        request = main_models.InsertHotelSceneBookItemShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_hotel_scene_item_req):
            request.add_hotel_scene_item_req_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_hotel_scene_item_req, 'AddHotelSceneItemReq', 'json')
        query = {}
        if not DaraCore.is_null(request.add_hotel_scene_item_req_shrink):
            query['AddHotelSceneItemReq'] = request.add_hotel_scene_item_req_shrink
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InsertHotelSceneBookItem',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/insertHotelSceneBookItem',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertHotelSceneBookItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_hotel_scene_book_item_with_options_async(
        self,
        tmp_req: main_models.InsertHotelSceneBookItemRequest,
        headers: main_models.InsertHotelSceneBookItemHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.InsertHotelSceneBookItemResponse:
        tmp_req.validate()
        request = main_models.InsertHotelSceneBookItemShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_hotel_scene_item_req):
            request.add_hotel_scene_item_req_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_hotel_scene_item_req, 'AddHotelSceneItemReq', 'json')
        query = {}
        if not DaraCore.is_null(request.add_hotel_scene_item_req_shrink):
            query['AddHotelSceneItemReq'] = request.add_hotel_scene_item_req_shrink
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InsertHotelSceneBookItem',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/insertHotelSceneBookItem',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertHotelSceneBookItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_hotel_scene_book_item(
        self,
        request: main_models.InsertHotelSceneBookItemRequest,
    ) -> main_models.InsertHotelSceneBookItemResponse:
        runtime = RuntimeOptions()
        headers = main_models.InsertHotelSceneBookItemHeaders()
        return self.insert_hotel_scene_book_item_with_options(request, headers, runtime)

    async def insert_hotel_scene_book_item_async(
        self,
        request: main_models.InsertHotelSceneBookItemRequest,
    ) -> main_models.InsertHotelSceneBookItemResponse:
        runtime = RuntimeOptions()
        headers = main_models.InsertHotelSceneBookItemHeaders()
        return await self.insert_hotel_scene_book_item_with_options_async(request, headers, runtime)

    def invoke_robot_push_with_options(
        self,
        request: main_models.InvokeRobotPushRequest,
        headers: main_models.InvokeRobotPushHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.InvokeRobotPushResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.push_type):
            body['PushType'] = request.push_type
        if not DaraCore.is_null(request.room_name):
            body['RoomName'] = request.room_name
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InvokeRobotPush',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/invokeRobotPush',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvokeRobotPushResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoke_robot_push_with_options_async(
        self,
        request: main_models.InvokeRobotPushRequest,
        headers: main_models.InvokeRobotPushHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.InvokeRobotPushResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.push_type):
            body['PushType'] = request.push_type
        if not DaraCore.is_null(request.room_name):
            body['RoomName'] = request.room_name
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InvokeRobotPush',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/invokeRobotPush',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvokeRobotPushResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invoke_robot_push(
        self,
        request: main_models.InvokeRobotPushRequest,
    ) -> main_models.InvokeRobotPushResponse:
        runtime = RuntimeOptions()
        headers = main_models.InvokeRobotPushHeaders()
        return self.invoke_robot_push_with_options(request, headers, runtime)

    async def invoke_robot_push_async(
        self,
        request: main_models.InvokeRobotPushRequest,
    ) -> main_models.InvokeRobotPushResponse:
        runtime = RuntimeOptions()
        headers = main_models.InvokeRobotPushHeaders()
        return await self.invoke_robot_push_with_options_async(request, headers, runtime)

    def list_all_provinces_with_options(
        self,
        headers: main_models.ListAllProvincesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListAllProvincesResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'ListAllProvinces',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listAllProvinces',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAllProvincesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_provinces_with_options_async(
        self,
        headers: main_models.ListAllProvincesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListAllProvincesResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'ListAllProvinces',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listAllProvinces',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAllProvincesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_provinces(self) -> main_models.ListAllProvincesResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListAllProvincesHeaders()
        return self.list_all_provinces_with_options(headers, runtime)

    async def list_all_provinces_async(self) -> main_models.ListAllProvincesResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListAllProvincesHeaders()
        return await self.list_all_provinces_with_options_async(headers, runtime)

    def list_cities_by_province_with_options(
        self,
        request: main_models.ListCitiesByProvinceRequest,
        headers: main_models.ListCitiesByProvinceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListCitiesByProvinceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.province):
            body['Province'] = request.province
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCitiesByProvince',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listCitiesByProvince',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCitiesByProvinceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cities_by_province_with_options_async(
        self,
        request: main_models.ListCitiesByProvinceRequest,
        headers: main_models.ListCitiesByProvinceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListCitiesByProvinceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.province):
            body['Province'] = request.province
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCitiesByProvince',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listCitiesByProvince',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCitiesByProvinceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cities_by_province(
        self,
        request: main_models.ListCitiesByProvinceRequest,
    ) -> main_models.ListCitiesByProvinceResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListCitiesByProvinceHeaders()
        return self.list_cities_by_province_with_options(request, headers, runtime)

    async def list_cities_by_province_async(
        self,
        request: main_models.ListCitiesByProvinceRequest,
    ) -> main_models.ListCitiesByProvinceResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListCitiesByProvinceHeaders()
        return await self.list_cities_by_province_with_options_async(request, headers, runtime)

    def list_custom_qawith_options(
        self,
        tmp_req: main_models.ListCustomQARequest,
        headers: main_models.ListCustomQAHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomQAResponse:
        tmp_req.validate()
        request = main_models.ListCustomQAShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_shrink):
            body['Page'] = request.page_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomQA',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listCustomQA',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomQAResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_qawith_options_async(
        self,
        tmp_req: main_models.ListCustomQARequest,
        headers: main_models.ListCustomQAHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomQAResponse:
        tmp_req.validate()
        request = main_models.ListCustomQAShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_shrink):
            body['Page'] = request.page_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomQA',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listCustomQA',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomQAResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_qa(
        self,
        request: main_models.ListCustomQARequest,
    ) -> main_models.ListCustomQAResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListCustomQAHeaders()
        return self.list_custom_qawith_options(request, headers, runtime)

    async def list_custom_qa_async(
        self,
        request: main_models.ListCustomQARequest,
    ) -> main_models.ListCustomQAResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListCustomQAHeaders()
        return await self.list_custom_qawith_options_async(request, headers, runtime)

    def list_dialogue_template_with_options(
        self,
        request: main_models.ListDialogueTemplateRequest,
        headers: main_models.ListDialogueTemplateHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListDialogueTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDialogueTemplate',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listDialogueTemplate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDialogueTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dialogue_template_with_options_async(
        self,
        request: main_models.ListDialogueTemplateRequest,
        headers: main_models.ListDialogueTemplateHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListDialogueTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDialogueTemplate',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listDialogueTemplate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDialogueTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dialogue_template(
        self,
        request: main_models.ListDialogueTemplateRequest,
    ) -> main_models.ListDialogueTemplateResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListDialogueTemplateHeaders()
        return self.list_dialogue_template_with_options(request, headers, runtime)

    async def list_dialogue_template_async(
        self,
        request: main_models.ListDialogueTemplateRequest,
    ) -> main_models.ListDialogueTemplateResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListDialogueTemplateHeaders()
        return await self.list_dialogue_template_with_options_async(request, headers, runtime)

    def list_hotel_alarm_with_options(
        self,
        tmp_req: main_models.ListHotelAlarmRequest,
        headers: main_models.ListHotelAlarmHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotelAlarmResponse:
        tmp_req.validate()
        request = main_models.ListHotelAlarmShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rooms):
            request.rooms_shrink = Utils.array_to_string_with_specified_style(tmp_req.rooms, 'Rooms', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.rooms_shrink):
            body['Rooms'] = request.rooms_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHotelAlarm',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelAlarmList',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotelAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotel_alarm_with_options_async(
        self,
        tmp_req: main_models.ListHotelAlarmRequest,
        headers: main_models.ListHotelAlarmHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotelAlarmResponse:
        tmp_req.validate()
        request = main_models.ListHotelAlarmShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rooms):
            request.rooms_shrink = Utils.array_to_string_with_specified_style(tmp_req.rooms, 'Rooms', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.rooms_shrink):
            body['Rooms'] = request.rooms_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHotelAlarm',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/getHotelAlarmList',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotelAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotel_alarm(
        self,
        request: main_models.ListHotelAlarmRequest,
    ) -> main_models.ListHotelAlarmResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListHotelAlarmHeaders()
        return self.list_hotel_alarm_with_options(request, headers, runtime)

    async def list_hotel_alarm_async(
        self,
        request: main_models.ListHotelAlarmRequest,
    ) -> main_models.ListHotelAlarmResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListHotelAlarmHeaders()
        return await self.list_hotel_alarm_with_options_async(request, headers, runtime)

    def list_hotel_control_device_with_options(
        self,
        tmp_req: main_models.ListHotelControlDeviceRequest,
        headers: main_models.ListHotelControlDeviceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotelControlDeviceResponse:
        tmp_req.validate()
        request = main_models.ListHotelControlDeviceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHotelControlDevice',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listHotelControlDevice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotelControlDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotel_control_device_with_options_async(
        self,
        tmp_req: main_models.ListHotelControlDeviceRequest,
        headers: main_models.ListHotelControlDeviceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotelControlDeviceResponse:
        tmp_req.validate()
        request = main_models.ListHotelControlDeviceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHotelControlDevice',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listHotelControlDevice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotelControlDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotel_control_device(
        self,
        request: main_models.ListHotelControlDeviceRequest,
    ) -> main_models.ListHotelControlDeviceResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListHotelControlDeviceHeaders()
        return self.list_hotel_control_device_with_options(request, headers, runtime)

    async def list_hotel_control_device_async(
        self,
        request: main_models.ListHotelControlDeviceRequest,
    ) -> main_models.ListHotelControlDeviceResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListHotelControlDeviceHeaders()
        return await self.list_hotel_control_device_with_options_async(request, headers, runtime)

    def list_hotel_info_with_options(
        self,
        headers: main_models.ListHotelInfoHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotelInfoResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'ListHotelInfo',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listHotelInfo',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotelInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotel_info_with_options_async(
        self,
        headers: main_models.ListHotelInfoHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotelInfoResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'ListHotelInfo',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listHotelInfo',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotelInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotel_info(self) -> main_models.ListHotelInfoResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListHotelInfoHeaders()
        return self.list_hotel_info_with_options(headers, runtime)

    async def list_hotel_info_async(self) -> main_models.ListHotelInfoResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListHotelInfoHeaders()
        return await self.list_hotel_info_with_options_async(headers, runtime)

    def list_hotel_message_template_with_options(
        self,
        headers: main_models.ListHotelMessageTemplateHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotelMessageTemplateResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'ListHotelMessageTemplate',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listHotelMessageTemplate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotelMessageTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotel_message_template_with_options_async(
        self,
        headers: main_models.ListHotelMessageTemplateHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotelMessageTemplateResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'ListHotelMessageTemplate',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listHotelMessageTemplate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotelMessageTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotel_message_template(self) -> main_models.ListHotelMessageTemplateResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListHotelMessageTemplateHeaders()
        return self.list_hotel_message_template_with_options(headers, runtime)

    async def list_hotel_message_template_async(self) -> main_models.ListHotelMessageTemplateResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListHotelMessageTemplateHeaders()
        return await self.list_hotel_message_template_with_options_async(headers, runtime)

    def list_hotel_order_with_options(
        self,
        tmp_req: main_models.ListHotelOrderRequest,
        headers: main_models.ListHotelOrderHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotelOrderResponse:
        tmp_req.validate()
        request = main_models.ListHotelOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHotelOrder',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listHotelOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotelOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotel_order_with_options_async(
        self,
        tmp_req: main_models.ListHotelOrderRequest,
        headers: main_models.ListHotelOrderHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotelOrderResponse:
        tmp_req.validate()
        request = main_models.ListHotelOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHotelOrder',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listHotelOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotelOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotel_order(
        self,
        request: main_models.ListHotelOrderRequest,
    ) -> main_models.ListHotelOrderResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListHotelOrderHeaders()
        return self.list_hotel_order_with_options(request, headers, runtime)

    async def list_hotel_order_async(
        self,
        request: main_models.ListHotelOrderRequest,
    ) -> main_models.ListHotelOrderResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListHotelOrderHeaders()
        return await self.list_hotel_order_with_options_async(request, headers, runtime)

    def list_hotel_rooms_with_options(
        self,
        tmp_req: main_models.ListHotelRoomsRequest,
        headers: main_models.ListHotelRoomsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotelRoomsResponse:
        tmp_req.validate()
        request = main_models.ListHotelRoomsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.hotel_admin_room):
            request.hotel_admin_room_shrink = Utils.array_to_string_with_specified_style(tmp_req.hotel_admin_room, 'HotelAdminRoom', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_admin_room_shrink):
            body['HotelAdminRoom'] = request.hotel_admin_room_shrink
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHotelRooms',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listHotelRooms',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotelRoomsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotel_rooms_with_options_async(
        self,
        tmp_req: main_models.ListHotelRoomsRequest,
        headers: main_models.ListHotelRoomsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotelRoomsResponse:
        tmp_req.validate()
        request = main_models.ListHotelRoomsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.hotel_admin_room):
            request.hotel_admin_room_shrink = Utils.array_to_string_with_specified_style(tmp_req.hotel_admin_room, 'HotelAdminRoom', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_admin_room_shrink):
            body['HotelAdminRoom'] = request.hotel_admin_room_shrink
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHotelRooms',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listHotelRooms',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotelRoomsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotel_rooms(
        self,
        request: main_models.ListHotelRoomsRequest,
    ) -> main_models.ListHotelRoomsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListHotelRoomsHeaders()
        return self.list_hotel_rooms_with_options(request, headers, runtime)

    async def list_hotel_rooms_async(
        self,
        request: main_models.ListHotelRoomsRequest,
    ) -> main_models.ListHotelRoomsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListHotelRoomsHeaders()
        return await self.list_hotel_rooms_with_options_async(request, headers, runtime)

    def list_hotel_scene_book_items_with_options(
        self,
        tmp_req: main_models.ListHotelSceneBookItemsRequest,
        headers: main_models.ListHotelSceneBookItemsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotelSceneBookItemsResponse:
        tmp_req.validate()
        request = main_models.ListHotelSceneBookItemsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not DaraCore.is_null(request.page_shrink):
            query['Page'] = request.page_shrink
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHotelSceneBookItems',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listHotelSceneBookItems',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotelSceneBookItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotel_scene_book_items_with_options_async(
        self,
        tmp_req: main_models.ListHotelSceneBookItemsRequest,
        headers: main_models.ListHotelSceneBookItemsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotelSceneBookItemsResponse:
        tmp_req.validate()
        request = main_models.ListHotelSceneBookItemsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not DaraCore.is_null(request.page_shrink):
            query['Page'] = request.page_shrink
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHotelSceneBookItems',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listHotelSceneBookItems',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotelSceneBookItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotel_scene_book_items(
        self,
        request: main_models.ListHotelSceneBookItemsRequest,
    ) -> main_models.ListHotelSceneBookItemsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListHotelSceneBookItemsHeaders()
        return self.list_hotel_scene_book_items_with_options(request, headers, runtime)

    async def list_hotel_scene_book_items_async(
        self,
        request: main_models.ListHotelSceneBookItemsRequest,
    ) -> main_models.ListHotelSceneBookItemsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListHotelSceneBookItemsHeaders()
        return await self.list_hotel_scene_book_items_with_options_async(request, headers, runtime)

    def list_hotel_scene_item_with_options(
        self,
        tmp_req: main_models.ListHotelSceneItemRequest,
        headers: main_models.ListHotelSceneItemHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotelSceneItemResponse:
        tmp_req.validate()
        request = main_models.ListHotelSceneItemShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHotelSceneItem',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listHotelSceneItem',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotelSceneItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotel_scene_item_with_options_async(
        self,
        tmp_req: main_models.ListHotelSceneItemRequest,
        headers: main_models.ListHotelSceneItemHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotelSceneItemResponse:
        tmp_req.validate()
        request = main_models.ListHotelSceneItemShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHotelSceneItem',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listHotelSceneItem',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotelSceneItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotel_scene_item(
        self,
        request: main_models.ListHotelSceneItemRequest,
    ) -> main_models.ListHotelSceneItemResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListHotelSceneItemHeaders()
        return self.list_hotel_scene_item_with_options(request, headers, runtime)

    async def list_hotel_scene_item_async(
        self,
        request: main_models.ListHotelSceneItemRequest,
    ) -> main_models.ListHotelSceneItemResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListHotelSceneItemHeaders()
        return await self.list_hotel_scene_item_with_options_async(request, headers, runtime)

    def list_hotel_scene_items_with_options(
        self,
        tmp_req: main_models.ListHotelSceneItemsRequest,
        headers: main_models.ListHotelSceneItemsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotelSceneItemsResponse:
        tmp_req.validate()
        request = main_models.ListHotelSceneItemsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_hotel_scene_req):
            request.list_hotel_scene_req_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_hotel_scene_req, 'ListHotelSceneReq', 'json')
        query = {}
        if not DaraCore.is_null(request.list_hotel_scene_req_shrink):
            query['ListHotelSceneReq'] = request.list_hotel_scene_req_shrink
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHotelSceneItems',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listHotelSceneItems',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotelSceneItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotel_scene_items_with_options_async(
        self,
        tmp_req: main_models.ListHotelSceneItemsRequest,
        headers: main_models.ListHotelSceneItemsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotelSceneItemsResponse:
        tmp_req.validate()
        request = main_models.ListHotelSceneItemsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_hotel_scene_req):
            request.list_hotel_scene_req_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_hotel_scene_req, 'ListHotelSceneReq', 'json')
        query = {}
        if not DaraCore.is_null(request.list_hotel_scene_req_shrink):
            query['ListHotelSceneReq'] = request.list_hotel_scene_req_shrink
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHotelSceneItems',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listHotelSceneItems',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotelSceneItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotel_scene_items(
        self,
        request: main_models.ListHotelSceneItemsRequest,
    ) -> main_models.ListHotelSceneItemsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListHotelSceneItemsHeaders()
        return self.list_hotel_scene_items_with_options(request, headers, runtime)

    async def list_hotel_scene_items_async(
        self,
        request: main_models.ListHotelSceneItemsRequest,
    ) -> main_models.ListHotelSceneItemsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListHotelSceneItemsHeaders()
        return await self.list_hotel_scene_items_with_options_async(request, headers, runtime)

    def list_hotel_service_category_with_options(
        self,
        tmp_req: main_models.ListHotelServiceCategoryRequest,
        headers: main_models.ListHotelServiceCategoryHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotelServiceCategoryResponse:
        tmp_req.validate()
        request = main_models.ListHotelServiceCategoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        query = {}
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHotelServiceCategory',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listHotelServiceCategory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotelServiceCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotel_service_category_with_options_async(
        self,
        tmp_req: main_models.ListHotelServiceCategoryRequest,
        headers: main_models.ListHotelServiceCategoryHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotelServiceCategoryResponse:
        tmp_req.validate()
        request = main_models.ListHotelServiceCategoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        query = {}
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHotelServiceCategory',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listHotelServiceCategory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotelServiceCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotel_service_category(
        self,
        request: main_models.ListHotelServiceCategoryRequest,
    ) -> main_models.ListHotelServiceCategoryResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListHotelServiceCategoryHeaders()
        return self.list_hotel_service_category_with_options(request, headers, runtime)

    async def list_hotel_service_category_async(
        self,
        request: main_models.ListHotelServiceCategoryRequest,
    ) -> main_models.ListHotelServiceCategoryResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListHotelServiceCategoryHeaders()
        return await self.list_hotel_service_category_with_options_async(request, headers, runtime)

    def list_hotels_with_options(
        self,
        tmp_req: main_models.ListHotelsRequest,
        headers: main_models.ListHotelsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotelsResponse:
        tmp_req.validate()
        request = main_models.ListHotelsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.hotel_request):
            request.hotel_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.hotel_request, 'HotelRequest', 'json')
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not DaraCore.is_null(request.hotel_request_shrink):
            query['HotelRequest'] = request.hotel_request_shrink
        if not DaraCore.is_null(request.page_shrink):
            query['Page'] = request.page_shrink
        body = {}
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHotels',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listHotels',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotels_with_options_async(
        self,
        tmp_req: main_models.ListHotelsRequest,
        headers: main_models.ListHotelsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotelsResponse:
        tmp_req.validate()
        request = main_models.ListHotelsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.hotel_request):
            request.hotel_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.hotel_request, 'HotelRequest', 'json')
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not DaraCore.is_null(request.hotel_request_shrink):
            query['HotelRequest'] = request.hotel_request_shrink
        if not DaraCore.is_null(request.page_shrink):
            query['Page'] = request.page_shrink
        body = {}
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHotels',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listHotels',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotels(
        self,
        request: main_models.ListHotelsRequest,
    ) -> main_models.ListHotelsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListHotelsHeaders()
        return self.list_hotels_with_options(request, headers, runtime)

    async def list_hotels_async(
        self,
        request: main_models.ListHotelsRequest,
    ) -> main_models.ListHotelsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListHotelsHeaders()
        return await self.list_hotels_with_options_async(request, headers, runtime)

    def list_infrared_device_brands_with_options(
        self,
        request: main_models.ListInfraredDeviceBrandsRequest,
        headers: main_models.ListInfraredDeviceBrandsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListInfraredDeviceBrandsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category):
            body['Category'] = request.category
        if not DaraCore.is_null(request.service_provider):
            body['ServiceProvider'] = request.service_provider
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListInfraredDeviceBrands',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listInfraredDeviceBrands',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInfraredDeviceBrandsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_infrared_device_brands_with_options_async(
        self,
        request: main_models.ListInfraredDeviceBrandsRequest,
        headers: main_models.ListInfraredDeviceBrandsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListInfraredDeviceBrandsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category):
            body['Category'] = request.category
        if not DaraCore.is_null(request.service_provider):
            body['ServiceProvider'] = request.service_provider
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListInfraredDeviceBrands',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listInfraredDeviceBrands',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInfraredDeviceBrandsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_infrared_device_brands(
        self,
        request: main_models.ListInfraredDeviceBrandsRequest,
    ) -> main_models.ListInfraredDeviceBrandsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListInfraredDeviceBrandsHeaders()
        return self.list_infrared_device_brands_with_options(request, headers, runtime)

    async def list_infrared_device_brands_async(
        self,
        request: main_models.ListInfraredDeviceBrandsRequest,
    ) -> main_models.ListInfraredDeviceBrandsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListInfraredDeviceBrandsHeaders()
        return await self.list_infrared_device_brands_with_options_async(request, headers, runtime)

    def list_infrared_remote_controllers_with_options(
        self,
        request: main_models.ListInfraredRemoteControllersRequest,
        headers: main_models.ListInfraredRemoteControllersHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListInfraredRemoteControllersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.brand):
            body['Brand'] = request.brand
        if not DaraCore.is_null(request.category):
            body['Category'] = request.category
        if not DaraCore.is_null(request.city):
            body['City'] = request.city
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.province):
            body['Province'] = request.province
        if not DaraCore.is_null(request.service_provider):
            body['ServiceProvider'] = request.service_provider
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListInfraredRemoteControllers',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listInfraredRemoteControllers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInfraredRemoteControllersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_infrared_remote_controllers_with_options_async(
        self,
        request: main_models.ListInfraredRemoteControllersRequest,
        headers: main_models.ListInfraredRemoteControllersHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListInfraredRemoteControllersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.brand):
            body['Brand'] = request.brand
        if not DaraCore.is_null(request.category):
            body['Category'] = request.category
        if not DaraCore.is_null(request.city):
            body['City'] = request.city
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.province):
            body['Province'] = request.province
        if not DaraCore.is_null(request.service_provider):
            body['ServiceProvider'] = request.service_provider
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListInfraredRemoteControllers',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listInfraredRemoteControllers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInfraredRemoteControllersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_infrared_remote_controllers(
        self,
        request: main_models.ListInfraredRemoteControllersRequest,
    ) -> main_models.ListInfraredRemoteControllersResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListInfraredRemoteControllersHeaders()
        return self.list_infrared_remote_controllers_with_options(request, headers, runtime)

    async def list_infrared_remote_controllers_async(
        self,
        request: main_models.ListInfraredRemoteControllersRequest,
    ) -> main_models.ListInfraredRemoteControllersResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListInfraredRemoteControllersHeaders()
        return await self.list_infrared_remote_controllers_with_options_async(request, headers, runtime)

    def list_stbservice_providers_with_options(
        self,
        request: main_models.ListSTBServiceProvidersRequest,
        headers: main_models.ListSTBServiceProvidersHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListSTBServiceProvidersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.city):
            body['City'] = request.city
        if not DaraCore.is_null(request.province):
            body['Province'] = request.province
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSTBServiceProviders',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listSTBServiceProviders',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSTBServiceProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_stbservice_providers_with_options_async(
        self,
        request: main_models.ListSTBServiceProvidersRequest,
        headers: main_models.ListSTBServiceProvidersHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListSTBServiceProvidersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.city):
            body['City'] = request.city
        if not DaraCore.is_null(request.province):
            body['Province'] = request.province
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSTBServiceProviders',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listSTBServiceProviders',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSTBServiceProvidersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_stbservice_providers(
        self,
        request: main_models.ListSTBServiceProvidersRequest,
    ) -> main_models.ListSTBServiceProvidersResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListSTBServiceProvidersHeaders()
        return self.list_stbservice_providers_with_options(request, headers, runtime)

    async def list_stbservice_providers_async(
        self,
        request: main_models.ListSTBServiceProvidersRequest,
    ) -> main_models.ListSTBServiceProvidersResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListSTBServiceProvidersHeaders()
        return await self.list_stbservice_providers_with_options_async(request, headers, runtime)

    def list_scene_category_with_options(
        self,
        request: main_models.ListSceneCategoryRequest,
        headers: main_models.ListSceneCategoryHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListSceneCategoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSceneCategory',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listSceneCategory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSceneCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scene_category_with_options_async(
        self,
        request: main_models.ListSceneCategoryRequest,
        headers: main_models.ListSceneCategoryHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListSceneCategoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSceneCategory',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listSceneCategory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSceneCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scene_category(
        self,
        request: main_models.ListSceneCategoryRequest,
    ) -> main_models.ListSceneCategoryResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListSceneCategoryHeaders()
        return self.list_scene_category_with_options(request, headers, runtime)

    async def list_scene_category_async(
        self,
        request: main_models.ListSceneCategoryRequest,
    ) -> main_models.ListSceneCategoryResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListSceneCategoryHeaders()
        return await self.list_scene_category_with_options_async(request, headers, runtime)

    def list_service_qawith_options(
        self,
        tmp_req: main_models.ListServiceQARequest,
        headers: main_models.ListServiceQAHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceQAResponse:
        tmp_req.validate()
        request = main_models.ListServiceQAShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        body = {}
        if not DaraCore.is_null(request.active):
            body['Active'] = request.active
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_shrink):
            body['Page'] = request.page_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceQA',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listServiceQA',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceQAResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_qawith_options_async(
        self,
        tmp_req: main_models.ListServiceQARequest,
        headers: main_models.ListServiceQAHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceQAResponse:
        tmp_req.validate()
        request = main_models.ListServiceQAShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        body = {}
        if not DaraCore.is_null(request.active):
            body['Active'] = request.active
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_shrink):
            body['Page'] = request.page_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceQA',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listServiceQA',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceQAResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_qa(
        self,
        request: main_models.ListServiceQARequest,
    ) -> main_models.ListServiceQAResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListServiceQAHeaders()
        return self.list_service_qawith_options(request, headers, runtime)

    async def list_service_qa_async(
        self,
        request: main_models.ListServiceQARequest,
    ) -> main_models.ListServiceQAResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListServiceQAHeaders()
        return await self.list_service_qawith_options_async(request, headers, runtime)

    def list_tickets_with_options(
        self,
        tmp_req: main_models.ListTicketsRequest,
        headers: main_models.ListTicketsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListTicketsResponse:
        tmp_req.validate()
        request = main_models.ListTicketsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.is_desc):
            body['IsDesc'] = request.is_desc
        if not DaraCore.is_null(request.is_need_callback):
            body['IsNeedCallback'] = request.is_need_callback
        if not DaraCore.is_null(request.is_need_charges):
            body['IsNeedCharges'] = request.is_need_charges
        if not DaraCore.is_null(request.page_shrink):
            body['Page'] = request.page_shrink
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        if not DaraCore.is_null(request.sort_field):
            body['SortField'] = request.sort_field
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTickets',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listTickets',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTicketsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tickets_with_options_async(
        self,
        tmp_req: main_models.ListTicketsRequest,
        headers: main_models.ListTicketsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListTicketsResponse:
        tmp_req.validate()
        request = main_models.ListTicketsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.is_desc):
            body['IsDesc'] = request.is_desc
        if not DaraCore.is_null(request.is_need_callback):
            body['IsNeedCallback'] = request.is_need_callback
        if not DaraCore.is_null(request.is_need_charges):
            body['IsNeedCharges'] = request.is_need_charges
        if not DaraCore.is_null(request.page_shrink):
            body['Page'] = request.page_shrink
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        if not DaraCore.is_null(request.sort_field):
            body['SortField'] = request.sort_field
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTickets',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/listTickets',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTicketsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tickets(
        self,
        request: main_models.ListTicketsRequest,
    ) -> main_models.ListTicketsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListTicketsHeaders()
        return self.list_tickets_with_options(request, headers, runtime)

    async def list_tickets_async(
        self,
        request: main_models.ListTicketsRequest,
    ) -> main_models.ListTicketsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListTicketsHeaders()
        return await self.list_tickets_with_options_async(request, headers, runtime)

    def page_get_hotel_room_devices_with_options(
        self,
        request: main_models.PageGetHotelRoomDevicesRequest,
        headers: main_models.PageGetHotelRoomDevicesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PageGetHotelRoomDevicesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PageGetHotelRoomDevices',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/pageGetHotelRoomDevices',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PageGetHotelRoomDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def page_get_hotel_room_devices_with_options_async(
        self,
        request: main_models.PageGetHotelRoomDevicesRequest,
        headers: main_models.PageGetHotelRoomDevicesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PageGetHotelRoomDevicesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PageGetHotelRoomDevices',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/pageGetHotelRoomDevices',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PageGetHotelRoomDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def page_get_hotel_room_devices(
        self,
        request: main_models.PageGetHotelRoomDevicesRequest,
    ) -> main_models.PageGetHotelRoomDevicesResponse:
        runtime = RuntimeOptions()
        headers = main_models.PageGetHotelRoomDevicesHeaders()
        return self.page_get_hotel_room_devices_with_options(request, headers, runtime)

    async def page_get_hotel_room_devices_async(
        self,
        request: main_models.PageGetHotelRoomDevicesRequest,
    ) -> main_models.PageGetHotelRoomDevicesResponse:
        runtime = RuntimeOptions()
        headers = main_models.PageGetHotelRoomDevicesHeaders()
        return await self.page_get_hotel_room_devices_with_options_async(request, headers, runtime)

    def pms_event_report_with_options(
        self,
        request: main_models.PmsEventReportRequest,
        headers: main_models.PmsEventReportHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PmsEventReportResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.payload):
            body['Payload'] = request.payload
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PmsEventReport',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/pmsEventReport',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PmsEventReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def pms_event_report_with_options_async(
        self,
        request: main_models.PmsEventReportRequest,
        headers: main_models.PmsEventReportHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PmsEventReportResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.payload):
            body['Payload'] = request.payload
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PmsEventReport',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/pmsEventReport',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PmsEventReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pms_event_report(
        self,
        request: main_models.PmsEventReportRequest,
    ) -> main_models.PmsEventReportResponse:
        runtime = RuntimeOptions()
        headers = main_models.PmsEventReportHeaders()
        return self.pms_event_report_with_options(request, headers, runtime)

    async def pms_event_report_async(
        self,
        request: main_models.PmsEventReportRequest,
    ) -> main_models.PmsEventReportResponse:
        runtime = RuntimeOptions()
        headers = main_models.PmsEventReportHeaders()
        return await self.pms_event_report_with_options_async(request, headers, runtime)

    def push_hotel_message_with_options(
        self,
        tmp_req: main_models.PushHotelMessageRequest,
        headers: main_models.PushHotelMessageHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PushHotelMessageResponse:
        tmp_req.validate()
        request = main_models.PushHotelMessageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.push_hotel_message_req):
            request.push_hotel_message_req_shrink = Utils.array_to_string_with_specified_style(tmp_req.push_hotel_message_req, 'PushHotelMessageReq', 'json')
        query = {}
        if not DaraCore.is_null(request.push_hotel_message_req_shrink):
            query['PushHotelMessageReq'] = request.push_hotel_message_req_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushHotelMessage',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/pushHotelMessage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushHotelMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_hotel_message_with_options_async(
        self,
        tmp_req: main_models.PushHotelMessageRequest,
        headers: main_models.PushHotelMessageHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PushHotelMessageResponse:
        tmp_req.validate()
        request = main_models.PushHotelMessageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.push_hotel_message_req):
            request.push_hotel_message_req_shrink = Utils.array_to_string_with_specified_style(tmp_req.push_hotel_message_req, 'PushHotelMessageReq', 'json')
        query = {}
        if not DaraCore.is_null(request.push_hotel_message_req_shrink):
            query['PushHotelMessageReq'] = request.push_hotel_message_req_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushHotelMessage',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/pushHotelMessage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushHotelMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_hotel_message(
        self,
        request: main_models.PushHotelMessageRequest,
    ) -> main_models.PushHotelMessageResponse:
        runtime = RuntimeOptions()
        headers = main_models.PushHotelMessageHeaders()
        return self.push_hotel_message_with_options(request, headers, runtime)

    async def push_hotel_message_async(
        self,
        request: main_models.PushHotelMessageRequest,
    ) -> main_models.PushHotelMessageResponse:
        runtime = RuntimeOptions()
        headers = main_models.PushHotelMessageHeaders()
        return await self.push_hotel_message_with_options_async(request, headers, runtime)

    def push_voice_box_commands_with_options(
        self,
        tmp_req: main_models.PushVoiceBoxCommandsRequest,
        headers: main_models.PushVoiceBoxCommandsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PushVoiceBoxCommandsResponse:
        tmp_req.validate()
        request = main_models.PushVoiceBoxCommandsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.commands):
            request.commands_shrink = Utils.array_to_string_with_specified_style(tmp_req.commands, 'Commands', 'json')
        body = {}
        if not DaraCore.is_null(request.commands_shrink):
            body['Commands'] = request.commands_shrink
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushVoiceBoxCommands',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/pushVoiceBoxCommands',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushVoiceBoxCommandsResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_voice_box_commands_with_options_async(
        self,
        tmp_req: main_models.PushVoiceBoxCommandsRequest,
        headers: main_models.PushVoiceBoxCommandsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PushVoiceBoxCommandsResponse:
        tmp_req.validate()
        request = main_models.PushVoiceBoxCommandsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.commands):
            request.commands_shrink = Utils.array_to_string_with_specified_style(tmp_req.commands, 'Commands', 'json')
        body = {}
        if not DaraCore.is_null(request.commands_shrink):
            body['Commands'] = request.commands_shrink
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushVoiceBoxCommands',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/pushVoiceBoxCommands',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushVoiceBoxCommandsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_voice_box_commands(
        self,
        request: main_models.PushVoiceBoxCommandsRequest,
    ) -> main_models.PushVoiceBoxCommandsResponse:
        runtime = RuntimeOptions()
        headers = main_models.PushVoiceBoxCommandsHeaders()
        return self.push_voice_box_commands_with_options(request, headers, runtime)

    async def push_voice_box_commands_async(
        self,
        request: main_models.PushVoiceBoxCommandsRequest,
    ) -> main_models.PushVoiceBoxCommandsResponse:
        runtime = RuntimeOptions()
        headers = main_models.PushVoiceBoxCommandsHeaders()
        return await self.push_voice_box_commands_with_options_async(request, headers, runtime)

    def push_welcome_with_options(
        self,
        request: main_models.PushWelcomeRequest,
        headers: main_models.PushWelcomeHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PushWelcomeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_name):
            body['RoomName'] = request.room_name
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        if not DaraCore.is_null(request.welcome_music_url):
            body['WelcomeMusicUrl'] = request.welcome_music_url
        if not DaraCore.is_null(request.welcome_text):
            body['WelcomeText'] = request.welcome_text
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushWelcome',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/pushWelcome',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushWelcomeResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_welcome_with_options_async(
        self,
        request: main_models.PushWelcomeRequest,
        headers: main_models.PushWelcomeHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PushWelcomeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_name):
            body['RoomName'] = request.room_name
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        if not DaraCore.is_null(request.welcome_music_url):
            body['WelcomeMusicUrl'] = request.welcome_music_url
        if not DaraCore.is_null(request.welcome_text):
            body['WelcomeText'] = request.welcome_text
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushWelcome',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/pushWelcome',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushWelcomeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_welcome(
        self,
        request: main_models.PushWelcomeRequest,
    ) -> main_models.PushWelcomeResponse:
        runtime = RuntimeOptions()
        headers = main_models.PushWelcomeHeaders()
        return self.push_welcome_with_options(request, headers, runtime)

    async def push_welcome_async(
        self,
        request: main_models.PushWelcomeRequest,
    ) -> main_models.PushWelcomeResponse:
        runtime = RuntimeOptions()
        headers = main_models.PushWelcomeHeaders()
        return await self.push_welcome_with_options_async(request, headers, runtime)

    def push_welcome_text_and_music_with_options(
        self,
        tmp_req: main_models.PushWelcomeTextAndMusicRequest,
        headers: main_models.PushWelcomeTextAndMusicHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PushWelcomeTextAndMusicResponse:
        tmp_req.validate()
        request = main_models.PushWelcomeTextAndMusicShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.template_variable):
            request.template_variable_shrink = Utils.array_to_string_with_specified_style(tmp_req.template_variable, 'TemplateVariable', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_name):
            body['RoomName'] = request.room_name
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        if not DaraCore.is_null(request.template_variable_shrink):
            body['TemplateVariable'] = request.template_variable_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushWelcomeTextAndMusic',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/pushWelcomeTextAndMusic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushWelcomeTextAndMusicResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_welcome_text_and_music_with_options_async(
        self,
        tmp_req: main_models.PushWelcomeTextAndMusicRequest,
        headers: main_models.PushWelcomeTextAndMusicHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PushWelcomeTextAndMusicResponse:
        tmp_req.validate()
        request = main_models.PushWelcomeTextAndMusicShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.template_variable):
            request.template_variable_shrink = Utils.array_to_string_with_specified_style(tmp_req.template_variable, 'TemplateVariable', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_name):
            body['RoomName'] = request.room_name
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        if not DaraCore.is_null(request.template_variable_shrink):
            body['TemplateVariable'] = request.template_variable_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushWelcomeTextAndMusic',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/pushWelcomeTextAndMusic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushWelcomeTextAndMusicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_welcome_text_and_music(
        self,
        request: main_models.PushWelcomeTextAndMusicRequest,
    ) -> main_models.PushWelcomeTextAndMusicResponse:
        runtime = RuntimeOptions()
        headers = main_models.PushWelcomeTextAndMusicHeaders()
        return self.push_welcome_text_and_music_with_options(request, headers, runtime)

    async def push_welcome_text_and_music_async(
        self,
        request: main_models.PushWelcomeTextAndMusicRequest,
    ) -> main_models.PushWelcomeTextAndMusicResponse:
        runtime = RuntimeOptions()
        headers = main_models.PushWelcomeTextAndMusicHeaders()
        return await self.push_welcome_text_and_music_with_options_async(request, headers, runtime)

    def query_device_status_with_options(
        self,
        tmp_req: main_models.QueryDeviceStatusRequest,
        headers: main_models.QueryDeviceStatusHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDeviceStatusResponse:
        tmp_req.validate()
        request = main_models.QueryDeviceStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDeviceStatus',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/queryDeviceStatus',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDeviceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_status_with_options_async(
        self,
        tmp_req: main_models.QueryDeviceStatusRequest,
        headers: main_models.QueryDeviceStatusHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDeviceStatusResponse:
        tmp_req.validate()
        request = main_models.QueryDeviceStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDeviceStatus',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/queryDeviceStatus',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDeviceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_device_status(
        self,
        request: main_models.QueryDeviceStatusRequest,
    ) -> main_models.QueryDeviceStatusResponse:
        runtime = RuntimeOptions()
        headers = main_models.QueryDeviceStatusHeaders()
        return self.query_device_status_with_options(request, headers, runtime)

    async def query_device_status_async(
        self,
        request: main_models.QueryDeviceStatusRequest,
    ) -> main_models.QueryDeviceStatusResponse:
        runtime = RuntimeOptions()
        headers = main_models.QueryDeviceStatusHeaders()
        return await self.query_device_status_with_options_async(request, headers, runtime)

    def query_hotel_room_detail_with_options(
        self,
        request: main_models.QueryHotelRoomDetailRequest,
        headers: main_models.QueryHotelRoomDetailHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.QueryHotelRoomDetailResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.mac):
            body['Mac'] = request.mac
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        if not DaraCore.is_null(request.sn):
            body['Sn'] = request.sn
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryHotelRoomDetail',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/queryHotelRoomDetail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryHotelRoomDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_hotel_room_detail_with_options_async(
        self,
        request: main_models.QueryHotelRoomDetailRequest,
        headers: main_models.QueryHotelRoomDetailHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.QueryHotelRoomDetailResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.mac):
            body['Mac'] = request.mac
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        if not DaraCore.is_null(request.sn):
            body['Sn'] = request.sn
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryHotelRoomDetail',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/queryHotelRoomDetail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryHotelRoomDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_hotel_room_detail(
        self,
        request: main_models.QueryHotelRoomDetailRequest,
    ) -> main_models.QueryHotelRoomDetailResponse:
        runtime = RuntimeOptions()
        headers = main_models.QueryHotelRoomDetailHeaders()
        return self.query_hotel_room_detail_with_options(request, headers, runtime)

    async def query_hotel_room_detail_async(
        self,
        request: main_models.QueryHotelRoomDetailRequest,
    ) -> main_models.QueryHotelRoomDetailResponse:
        runtime = RuntimeOptions()
        headers = main_models.QueryHotelRoomDetailHeaders()
        return await self.query_hotel_room_detail_with_options_async(request, headers, runtime)

    def query_room_control_devices_with_options(
        self,
        request: main_models.QueryRoomControlDevicesRequest,
        headers: main_models.QueryRoomControlDevicesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRoomControlDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hotel_id):
            query['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_no):
            query['RoomNo'] = request.room_no
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRoomControlDevices',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/queryRoomControlDevices',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRoomControlDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_room_control_devices_with_options_async(
        self,
        request: main_models.QueryRoomControlDevicesRequest,
        headers: main_models.QueryRoomControlDevicesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRoomControlDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hotel_id):
            query['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_no):
            query['RoomNo'] = request.room_no
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRoomControlDevices',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/queryRoomControlDevices',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRoomControlDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_room_control_devices(
        self,
        request: main_models.QueryRoomControlDevicesRequest,
    ) -> main_models.QueryRoomControlDevicesResponse:
        runtime = RuntimeOptions()
        headers = main_models.QueryRoomControlDevicesHeaders()
        return self.query_room_control_devices_with_options(request, headers, runtime)

    async def query_room_control_devices_async(
        self,
        request: main_models.QueryRoomControlDevicesRequest,
    ) -> main_models.QueryRoomControlDevicesResponse:
        runtime = RuntimeOptions()
        headers = main_models.QueryRoomControlDevicesHeaders()
        return await self.query_room_control_devices_with_options_async(request, headers, runtime)

    def query_room_control_devices_and_status_with_options(
        self,
        request: main_models.QueryRoomControlDevicesAndStatusRequest,
        headers: main_models.QueryRoomControlDevicesAndStatusHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRoomControlDevicesAndStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryRoomControlDevicesAndStatus',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/queryRoomControlDevicesAndStatus',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRoomControlDevicesAndStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_room_control_devices_and_status_with_options_async(
        self,
        request: main_models.QueryRoomControlDevicesAndStatusRequest,
        headers: main_models.QueryRoomControlDevicesAndStatusHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRoomControlDevicesAndStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryRoomControlDevicesAndStatus',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/queryRoomControlDevicesAndStatus',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRoomControlDevicesAndStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_room_control_devices_and_status(
        self,
        request: main_models.QueryRoomControlDevicesAndStatusRequest,
    ) -> main_models.QueryRoomControlDevicesAndStatusResponse:
        runtime = RuntimeOptions()
        headers = main_models.QueryRoomControlDevicesAndStatusHeaders()
        return self.query_room_control_devices_and_status_with_options(request, headers, runtime)

    async def query_room_control_devices_and_status_async(
        self,
        request: main_models.QueryRoomControlDevicesAndStatusRequest,
    ) -> main_models.QueryRoomControlDevicesAndStatusResponse:
        runtime = RuntimeOptions()
        headers = main_models.QueryRoomControlDevicesAndStatusHeaders()
        return await self.query_room_control_devices_and_status_with_options_async(request, headers, runtime)

    def query_room_status_with_options(
        self,
        request: main_models.QueryRoomStatusRequest,
        headers: main_models.QueryRoomStatusHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRoomStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryRoomStatus',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/queryRoomStatus',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRoomStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_room_status_with_options_async(
        self,
        request: main_models.QueryRoomStatusRequest,
        headers: main_models.QueryRoomStatusHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRoomStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryRoomStatus',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/queryRoomStatus',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRoomStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_room_status(
        self,
        request: main_models.QueryRoomStatusRequest,
    ) -> main_models.QueryRoomStatusResponse:
        runtime = RuntimeOptions()
        headers = main_models.QueryRoomStatusHeaders()
        return self.query_room_status_with_options(request, headers, runtime)

    async def query_room_status_async(
        self,
        request: main_models.QueryRoomStatusRequest,
    ) -> main_models.QueryRoomStatusResponse:
        runtime = RuntimeOptions()
        headers = main_models.QueryRoomStatusHeaders()
        return await self.query_room_status_with_options_async(request, headers, runtime)

    def query_scene_list_with_options(
        self,
        tmp_req: main_models.QuerySceneListRequest,
        headers: main_models.QuerySceneListHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySceneListResponse:
        tmp_req.validate()
        request = main_models.QuerySceneListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scene_states):
            request.scene_states_shrink = Utils.array_to_string_with_specified_style(tmp_req.scene_states, 'SceneStates', 'json')
        if not DaraCore.is_null(tmp_req.scene_types):
            request.scene_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.scene_types, 'SceneTypes', 'json')
        if not DaraCore.is_null(tmp_req.template_info_ids):
            request.template_info_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.template_info_ids, 'TemplateInfoIds', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.scene_states_shrink):
            body['SceneStates'] = request.scene_states_shrink
        if not DaraCore.is_null(request.scene_types_shrink):
            body['SceneTypes'] = request.scene_types_shrink
        if not DaraCore.is_null(request.template_info_ids_shrink):
            body['TemplateInfoIds'] = request.template_info_ids_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QuerySceneList',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/querySceneList',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySceneListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_scene_list_with_options_async(
        self,
        tmp_req: main_models.QuerySceneListRequest,
        headers: main_models.QuerySceneListHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySceneListResponse:
        tmp_req.validate()
        request = main_models.QuerySceneListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scene_states):
            request.scene_states_shrink = Utils.array_to_string_with_specified_style(tmp_req.scene_states, 'SceneStates', 'json')
        if not DaraCore.is_null(tmp_req.scene_types):
            request.scene_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.scene_types, 'SceneTypes', 'json')
        if not DaraCore.is_null(tmp_req.template_info_ids):
            request.template_info_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.template_info_ids, 'TemplateInfoIds', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.scene_states_shrink):
            body['SceneStates'] = request.scene_states_shrink
        if not DaraCore.is_null(request.scene_types_shrink):
            body['SceneTypes'] = request.scene_types_shrink
        if not DaraCore.is_null(request.template_info_ids_shrink):
            body['TemplateInfoIds'] = request.template_info_ids_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QuerySceneList',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/querySceneList',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySceneListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_scene_list(
        self,
        request: main_models.QuerySceneListRequest,
    ) -> main_models.QuerySceneListResponse:
        runtime = RuntimeOptions()
        headers = main_models.QuerySceneListHeaders()
        return self.query_scene_list_with_options(request, headers, runtime)

    async def query_scene_list_async(
        self,
        request: main_models.QuerySceneListRequest,
    ) -> main_models.QuerySceneListResponse:
        runtime = RuntimeOptions()
        headers = main_models.QuerySceneListHeaders()
        return await self.query_scene_list_with_options_async(request, headers, runtime)

    def remove_child_account_auth_with_options(
        self,
        request: main_models.RemoveChildAccountAuthRequest,
        headers: main_models.RemoveChildAccountAuthHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveChildAccountAuthResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.child_account_name):
            body['ChildAccountName'] = request.child_account_name
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveChildAccountAuth',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/removeChildAccountAuth',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveChildAccountAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_child_account_auth_with_options_async(
        self,
        request: main_models.RemoveChildAccountAuthRequest,
        headers: main_models.RemoveChildAccountAuthHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveChildAccountAuthResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.child_account_name):
            body['ChildAccountName'] = request.child_account_name
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveChildAccountAuth',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/removeChildAccountAuth',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveChildAccountAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_child_account_auth(
        self,
        request: main_models.RemoveChildAccountAuthRequest,
    ) -> main_models.RemoveChildAccountAuthResponse:
        runtime = RuntimeOptions()
        headers = main_models.RemoveChildAccountAuthHeaders()
        return self.remove_child_account_auth_with_options(request, headers, runtime)

    async def remove_child_account_auth_async(
        self,
        request: main_models.RemoveChildAccountAuthRequest,
    ) -> main_models.RemoveChildAccountAuthResponse:
        runtime = RuntimeOptions()
        headers = main_models.RemoveChildAccountAuthHeaders()
        return await self.remove_child_account_auth_with_options_async(request, headers, runtime)

    def remove_hotel_with_options(
        self,
        request: main_models.RemoveHotelRequest,
        headers: main_models.RemoveHotelHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveHotelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveHotel',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/removeHotel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveHotelResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_hotel_with_options_async(
        self,
        request: main_models.RemoveHotelRequest,
        headers: main_models.RemoveHotelHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveHotelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveHotel',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/removeHotel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveHotelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_hotel(
        self,
        request: main_models.RemoveHotelRequest,
    ) -> main_models.RemoveHotelResponse:
        runtime = RuntimeOptions()
        headers = main_models.RemoveHotelHeaders()
        return self.remove_hotel_with_options(request, headers, runtime)

    async def remove_hotel_async(
        self,
        request: main_models.RemoveHotelRequest,
    ) -> main_models.RemoveHotelResponse:
        runtime = RuntimeOptions()
        headers = main_models.RemoveHotelHeaders()
        return await self.remove_hotel_with_options_async(request, headers, runtime)

    def reset_welcome_text_and_music_with_options(
        self,
        request: main_models.ResetWelcomeTextAndMusicRequest,
        headers: main_models.ResetWelcomeTextAndMusicHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ResetWelcomeTextAndMusicResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetWelcomeTextAndMusic',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/resetWelcomeTextAndMusic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetWelcomeTextAndMusicResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_welcome_text_and_music_with_options_async(
        self,
        request: main_models.ResetWelcomeTextAndMusicRequest,
        headers: main_models.ResetWelcomeTextAndMusicHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ResetWelcomeTextAndMusicResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetWelcomeTextAndMusic',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/resetWelcomeTextAndMusic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetWelcomeTextAndMusicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_welcome_text_and_music(
        self,
        request: main_models.ResetWelcomeTextAndMusicRequest,
    ) -> main_models.ResetWelcomeTextAndMusicResponse:
        runtime = RuntimeOptions()
        headers = main_models.ResetWelcomeTextAndMusicHeaders()
        return self.reset_welcome_text_and_music_with_options(request, headers, runtime)

    async def reset_welcome_text_and_music_async(
        self,
        request: main_models.ResetWelcomeTextAndMusicRequest,
    ) -> main_models.ResetWelcomeTextAndMusicResponse:
        runtime = RuntimeOptions()
        headers = main_models.ResetWelcomeTextAndMusicHeaders()
        return await self.reset_welcome_text_and_music_with_options_async(request, headers, runtime)

    def room_check_out_with_options(
        self,
        tmp_req: main_models.RoomCheckOutRequest,
        headers: main_models.RoomCheckOutHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.RoomCheckOutResponse:
        tmp_req.validate()
        request = main_models.RoomCheckOutShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RoomCheckOut',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/roomCheckOut',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RoomCheckOutResponse(),
            self.call_api(params, req, runtime)
        )

    async def room_check_out_with_options_async(
        self,
        tmp_req: main_models.RoomCheckOutRequest,
        headers: main_models.RoomCheckOutHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.RoomCheckOutResponse:
        tmp_req.validate()
        request = main_models.RoomCheckOutShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RoomCheckOut',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/roomCheckOut',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RoomCheckOutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def room_check_out(
        self,
        request: main_models.RoomCheckOutRequest,
    ) -> main_models.RoomCheckOutResponse:
        runtime = RuntimeOptions()
        headers = main_models.RoomCheckOutHeaders()
        return self.room_check_out_with_options(request, headers, runtime)

    async def room_check_out_async(
        self,
        request: main_models.RoomCheckOutRequest,
    ) -> main_models.RoomCheckOutResponse:
        runtime = RuntimeOptions()
        headers = main_models.RoomCheckOutHeaders()
        return await self.room_check_out_with_options_async(request, headers, runtime)

    def submit_hotel_order_with_options(
        self,
        tmp_req: main_models.SubmitHotelOrderRequest,
        headers: main_models.SubmitHotelOrderHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitHotelOrderResponse:
        tmp_req.validate()
        request = main_models.SubmitHotelOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitHotelOrder',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/submitHotelOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitHotelOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_hotel_order_with_options_async(
        self,
        tmp_req: main_models.SubmitHotelOrderRequest,
        headers: main_models.SubmitHotelOrderHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitHotelOrderResponse:
        tmp_req.validate()
        request = main_models.SubmitHotelOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitHotelOrder',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/submitHotelOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitHotelOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_hotel_order(
        self,
        request: main_models.SubmitHotelOrderRequest,
    ) -> main_models.SubmitHotelOrderResponse:
        runtime = RuntimeOptions()
        headers = main_models.SubmitHotelOrderHeaders()
        return self.submit_hotel_order_with_options(request, headers, runtime)

    async def submit_hotel_order_async(
        self,
        request: main_models.SubmitHotelOrderRequest,
    ) -> main_models.SubmitHotelOrderResponse:
        runtime = RuntimeOptions()
        headers = main_models.SubmitHotelOrderHeaders()
        return await self.submit_hotel_order_with_options_async(request, headers, runtime)

    def sync_device_status_with_ak_with_options(
        self,
        request: main_models.SyncDeviceStatusWithAkRequest,
        headers: main_models.SyncDeviceStatusWithAkHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.SyncDeviceStatusWithAkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_cn_name):
            body['CategoryCnName'] = request.category_cn_name
        if not DaraCore.is_null(request.category_en_name):
            body['CategoryEnName'] = request.category_en_name
        if not DaraCore.is_null(request.device_name):
            body['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.location):
            body['Location'] = request.location
        if not DaraCore.is_null(request.location_cn_name):
            body['LocationCnName'] = request.location_cn_name
        if not DaraCore.is_null(request.number):
            body['Number'] = request.number
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        if not DaraCore.is_null(request.switch):
            body['Switch'] = request.switch
        if not DaraCore.is_null(request.fan_speed):
            body['fanSpeed'] = request.fan_speed
        if not DaraCore.is_null(request.mode):
            body['mode'] = request.mode
        if not DaraCore.is_null(request.room_temperature):
            body['roomTemperature'] = request.room_temperature
        if not DaraCore.is_null(request.temperature):
            body['temperature'] = request.temperature
        if not DaraCore.is_null(request.value):
            body['value'] = request.value
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SyncDeviceStatusWithAk',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/syncDeviceStatusWithAk',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncDeviceStatusWithAkResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_device_status_with_ak_with_options_async(
        self,
        request: main_models.SyncDeviceStatusWithAkRequest,
        headers: main_models.SyncDeviceStatusWithAkHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.SyncDeviceStatusWithAkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_cn_name):
            body['CategoryCnName'] = request.category_cn_name
        if not DaraCore.is_null(request.category_en_name):
            body['CategoryEnName'] = request.category_en_name
        if not DaraCore.is_null(request.device_name):
            body['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.location):
            body['Location'] = request.location
        if not DaraCore.is_null(request.location_cn_name):
            body['LocationCnName'] = request.location_cn_name
        if not DaraCore.is_null(request.number):
            body['Number'] = request.number
        if not DaraCore.is_null(request.room_no):
            body['RoomNo'] = request.room_no
        if not DaraCore.is_null(request.switch):
            body['Switch'] = request.switch
        if not DaraCore.is_null(request.fan_speed):
            body['fanSpeed'] = request.fan_speed
        if not DaraCore.is_null(request.mode):
            body['mode'] = request.mode
        if not DaraCore.is_null(request.room_temperature):
            body['roomTemperature'] = request.room_temperature
        if not DaraCore.is_null(request.temperature):
            body['temperature'] = request.temperature
        if not DaraCore.is_null(request.value):
            body['value'] = request.value
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SyncDeviceStatusWithAk',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/syncDeviceStatusWithAk',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncDeviceStatusWithAkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_device_status_with_ak(
        self,
        request: main_models.SyncDeviceStatusWithAkRequest,
    ) -> main_models.SyncDeviceStatusWithAkResponse:
        runtime = RuntimeOptions()
        headers = main_models.SyncDeviceStatusWithAkHeaders()
        return self.sync_device_status_with_ak_with_options(request, headers, runtime)

    async def sync_device_status_with_ak_async(
        self,
        request: main_models.SyncDeviceStatusWithAkRequest,
    ) -> main_models.SyncDeviceStatusWithAkResponse:
        runtime = RuntimeOptions()
        headers = main_models.SyncDeviceStatusWithAkHeaders()
        return await self.sync_device_status_with_ak_with_options_async(request, headers, runtime)

    def update_basic_info_qawith_options(
        self,
        request: main_models.UpdateBasicInfoQARequest,
        headers: main_models.UpdateBasicInfoQAHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBasicInfoQAResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_in_time):
            body['CheckInTime'] = request.check_in_time
        if not DaraCore.is_null(request.check_out_time):
            body['CheckOutTime'] = request.check_out_time
        if not DaraCore.is_null(request.hotel_address):
            body['HotelAddress'] = request.hotel_address
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.hotel_introduction):
            body['HotelIntroduction'] = request.hotel_introduction
        if not DaraCore.is_null(request.hotel_member):
            body['HotelMember'] = request.hotel_member
        if not DaraCore.is_null(request.hotel_service):
            body['HotelService'] = request.hotel_service
        if not DaraCore.is_null(request.parking_expenses):
            body['ParkingExpenses'] = request.parking_expenses
        if not DaraCore.is_null(request.parking_position):
            body['ParkingPosition'] = request.parking_position
        if not DaraCore.is_null(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.wifi_name):
            body['WifiName'] = request.wifi_name
        if not DaraCore.is_null(request.wifi_password):
            body['WifiPassword'] = request.wifi_password
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBasicInfoQA',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/updateBasicInfoQA',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBasicInfoQAResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_basic_info_qawith_options_async(
        self,
        request: main_models.UpdateBasicInfoQARequest,
        headers: main_models.UpdateBasicInfoQAHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBasicInfoQAResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_in_time):
            body['CheckInTime'] = request.check_in_time
        if not DaraCore.is_null(request.check_out_time):
            body['CheckOutTime'] = request.check_out_time
        if not DaraCore.is_null(request.hotel_address):
            body['HotelAddress'] = request.hotel_address
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.hotel_introduction):
            body['HotelIntroduction'] = request.hotel_introduction
        if not DaraCore.is_null(request.hotel_member):
            body['HotelMember'] = request.hotel_member
        if not DaraCore.is_null(request.hotel_service):
            body['HotelService'] = request.hotel_service
        if not DaraCore.is_null(request.parking_expenses):
            body['ParkingExpenses'] = request.parking_expenses
        if not DaraCore.is_null(request.parking_position):
            body['ParkingPosition'] = request.parking_position
        if not DaraCore.is_null(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.wifi_name):
            body['WifiName'] = request.wifi_name
        if not DaraCore.is_null(request.wifi_password):
            body['WifiPassword'] = request.wifi_password
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBasicInfoQA',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/updateBasicInfoQA',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBasicInfoQAResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_basic_info_qa(
        self,
        request: main_models.UpdateBasicInfoQARequest,
    ) -> main_models.UpdateBasicInfoQAResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateBasicInfoQAHeaders()
        return self.update_basic_info_qawith_options(request, headers, runtime)

    async def update_basic_info_qa_async(
        self,
        request: main_models.UpdateBasicInfoQARequest,
    ) -> main_models.UpdateBasicInfoQAResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateBasicInfoQAHeaders()
        return await self.update_basic_info_qawith_options_async(request, headers, runtime)

    def update_custom_qawith_options(
        self,
        tmp_req: main_models.UpdateCustomQARequest,
        headers: main_models.UpdateCustomQAHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomQAResponse:
        tmp_req.validate()
        request = main_models.UpdateCustomQAShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.answers):
            request.answers_shrink = Utils.array_to_string_with_specified_style(tmp_req.answers, 'Answers', 'json')
        if not DaraCore.is_null(tmp_req.key_words):
            request.key_words_shrink = Utils.array_to_string_with_specified_style(tmp_req.key_words, 'KeyWords', 'json')
        if not DaraCore.is_null(tmp_req.supplementary_questions):
            request.supplementary_questions_shrink = Utils.array_to_string_with_specified_style(tmp_req.supplementary_questions, 'SupplementaryQuestions', 'json')
        body = {}
        if not DaraCore.is_null(request.answers_shrink):
            body['Answers'] = request.answers_shrink
        if not DaraCore.is_null(request.custom_qaid):
            body['CustomQAId'] = request.custom_qaid
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.key_words_shrink):
            body['KeyWords'] = request.key_words_shrink
        if not DaraCore.is_null(request.major_question):
            body['MajorQuestion'] = request.major_question
        if not DaraCore.is_null(request.supplementary_questions_shrink):
            body['SupplementaryQuestions'] = request.supplementary_questions_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomQA',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/updateCustomQA',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomQAResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_qawith_options_async(
        self,
        tmp_req: main_models.UpdateCustomQARequest,
        headers: main_models.UpdateCustomQAHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomQAResponse:
        tmp_req.validate()
        request = main_models.UpdateCustomQAShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.answers):
            request.answers_shrink = Utils.array_to_string_with_specified_style(tmp_req.answers, 'Answers', 'json')
        if not DaraCore.is_null(tmp_req.key_words):
            request.key_words_shrink = Utils.array_to_string_with_specified_style(tmp_req.key_words, 'KeyWords', 'json')
        if not DaraCore.is_null(tmp_req.supplementary_questions):
            request.supplementary_questions_shrink = Utils.array_to_string_with_specified_style(tmp_req.supplementary_questions, 'SupplementaryQuestions', 'json')
        body = {}
        if not DaraCore.is_null(request.answers_shrink):
            body['Answers'] = request.answers_shrink
        if not DaraCore.is_null(request.custom_qaid):
            body['CustomQAId'] = request.custom_qaid
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.key_words_shrink):
            body['KeyWords'] = request.key_words_shrink
        if not DaraCore.is_null(request.major_question):
            body['MajorQuestion'] = request.major_question
        if not DaraCore.is_null(request.supplementary_questions_shrink):
            body['SupplementaryQuestions'] = request.supplementary_questions_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomQA',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/updateCustomQA',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomQAResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_qa(
        self,
        request: main_models.UpdateCustomQARequest,
    ) -> main_models.UpdateCustomQAResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateCustomQAHeaders()
        return self.update_custom_qawith_options(request, headers, runtime)

    async def update_custom_qa_async(
        self,
        request: main_models.UpdateCustomQARequest,
    ) -> main_models.UpdateCustomQAResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateCustomQAHeaders()
        return await self.update_custom_qawith_options_async(request, headers, runtime)

    def update_hotel_with_options(
        self,
        tmp_req: main_models.UpdateHotelRequest,
        headers: main_models.UpdateHotelHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHotelResponse:
        tmp_req.validate()
        request = main_models.UpdateHotelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.related_pks):
            request.related_pks_shrink = Utils.array_to_string_with_specified_style(tmp_req.related_pks, 'RelatedPks', 'json')
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.est_open_time):
            body['EstOpenTime'] = request.est_open_time
        if not DaraCore.is_null(request.hotel_address):
            body['HotelAddress'] = request.hotel_address
        if not DaraCore.is_null(request.hotel_email):
            body['HotelEmail'] = request.hotel_email
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.hotel_name):
            body['HotelName'] = request.hotel_name
        if not DaraCore.is_null(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.related_pks_shrink):
            body['RelatedPks'] = request.related_pks_shrink
        if not DaraCore.is_null(request.remark):
            body['Remark'] = request.remark
        if not DaraCore.is_null(request.room_num):
            body['RoomNum'] = request.room_num
        if not DaraCore.is_null(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHotel',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/updateHotel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHotelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_hotel_with_options_async(
        self,
        tmp_req: main_models.UpdateHotelRequest,
        headers: main_models.UpdateHotelHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHotelResponse:
        tmp_req.validate()
        request = main_models.UpdateHotelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.related_pks):
            request.related_pks_shrink = Utils.array_to_string_with_specified_style(tmp_req.related_pks, 'RelatedPks', 'json')
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.est_open_time):
            body['EstOpenTime'] = request.est_open_time
        if not DaraCore.is_null(request.hotel_address):
            body['HotelAddress'] = request.hotel_address
        if not DaraCore.is_null(request.hotel_email):
            body['HotelEmail'] = request.hotel_email
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.hotel_name):
            body['HotelName'] = request.hotel_name
        if not DaraCore.is_null(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.related_pks_shrink):
            body['RelatedPks'] = request.related_pks_shrink
        if not DaraCore.is_null(request.remark):
            body['Remark'] = request.remark
        if not DaraCore.is_null(request.room_num):
            body['RoomNum'] = request.room_num
        if not DaraCore.is_null(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHotel',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/updateHotel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHotelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_hotel(
        self,
        request: main_models.UpdateHotelRequest,
    ) -> main_models.UpdateHotelResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateHotelHeaders()
        return self.update_hotel_with_options(request, headers, runtime)

    async def update_hotel_async(
        self,
        request: main_models.UpdateHotelRequest,
    ) -> main_models.UpdateHotelResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateHotelHeaders()
        return await self.update_hotel_with_options_async(request, headers, runtime)

    def update_hotel_alarm_with_options(
        self,
        tmp_req: main_models.UpdateHotelAlarmRequest,
        headers: main_models.UpdateHotelAlarmHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHotelAlarmResponse:
        tmp_req.validate()
        request = main_models.UpdateHotelAlarmShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.alarms):
            request.alarms_shrink = Utils.array_to_string_with_specified_style(tmp_req.alarms, 'Alarms', 'json')
        if not DaraCore.is_null(tmp_req.schedule_info):
            request.schedule_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.schedule_info, 'ScheduleInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.alarms_shrink):
            body['Alarms'] = request.alarms_shrink
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.schedule_info_shrink):
            body['ScheduleInfo'] = request.schedule_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHotelAlarm',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/updateHotelAlarm',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHotelAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_hotel_alarm_with_options_async(
        self,
        tmp_req: main_models.UpdateHotelAlarmRequest,
        headers: main_models.UpdateHotelAlarmHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHotelAlarmResponse:
        tmp_req.validate()
        request = main_models.UpdateHotelAlarmShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.alarms):
            request.alarms_shrink = Utils.array_to_string_with_specified_style(tmp_req.alarms, 'Alarms', 'json')
        if not DaraCore.is_null(tmp_req.schedule_info):
            request.schedule_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.schedule_info, 'ScheduleInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.alarms_shrink):
            body['Alarms'] = request.alarms_shrink
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.schedule_info_shrink):
            body['ScheduleInfo'] = request.schedule_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHotelAlarm',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/updateHotelAlarm',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHotelAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_hotel_alarm(
        self,
        request: main_models.UpdateHotelAlarmRequest,
    ) -> main_models.UpdateHotelAlarmResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateHotelAlarmHeaders()
        return self.update_hotel_alarm_with_options(request, headers, runtime)

    async def update_hotel_alarm_async(
        self,
        request: main_models.UpdateHotelAlarmRequest,
    ) -> main_models.UpdateHotelAlarmResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateHotelAlarmHeaders()
        return await self.update_hotel_alarm_with_options_async(request, headers, runtime)

    def update_hotel_scene_book_item_with_options(
        self,
        tmp_req: main_models.UpdateHotelSceneBookItemRequest,
        headers: main_models.UpdateHotelSceneBookItemHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHotelSceneBookItemResponse:
        tmp_req.validate()
        request = main_models.UpdateHotelSceneBookItemShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_hotel_scene_book_req):
            request.update_hotel_scene_book_req_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_hotel_scene_book_req, 'UpdateHotelSceneBookReq', 'json')
        query = {}
        if not DaraCore.is_null(request.update_hotel_scene_book_req_shrink):
            query['UpdateHotelSceneBookReq'] = request.update_hotel_scene_book_req_shrink
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHotelSceneBookItem',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/updateHotelSceneBookItem',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHotelSceneBookItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_hotel_scene_book_item_with_options_async(
        self,
        tmp_req: main_models.UpdateHotelSceneBookItemRequest,
        headers: main_models.UpdateHotelSceneBookItemHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHotelSceneBookItemResponse:
        tmp_req.validate()
        request = main_models.UpdateHotelSceneBookItemShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_hotel_scene_book_req):
            request.update_hotel_scene_book_req_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_hotel_scene_book_req, 'UpdateHotelSceneBookReq', 'json')
        query = {}
        if not DaraCore.is_null(request.update_hotel_scene_book_req_shrink):
            query['UpdateHotelSceneBookReq'] = request.update_hotel_scene_book_req_shrink
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHotelSceneBookItem',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/updateHotelSceneBookItem',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHotelSceneBookItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_hotel_scene_book_item(
        self,
        request: main_models.UpdateHotelSceneBookItemRequest,
    ) -> main_models.UpdateHotelSceneBookItemResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateHotelSceneBookItemHeaders()
        return self.update_hotel_scene_book_item_with_options(request, headers, runtime)

    async def update_hotel_scene_book_item_async(
        self,
        request: main_models.UpdateHotelSceneBookItemRequest,
    ) -> main_models.UpdateHotelSceneBookItemResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateHotelSceneBookItemHeaders()
        return await self.update_hotel_scene_book_item_with_options_async(request, headers, runtime)

    def update_hotel_scene_item_with_options(
        self,
        tmp_req: main_models.UpdateHotelSceneItemRequest,
        headers: main_models.UpdateHotelSceneItemHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHotelSceneItemResponse:
        tmp_req.validate()
        request = main_models.UpdateHotelSceneItemShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_hotel_scene_operate_req):
            request.update_hotel_scene_operate_req_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_hotel_scene_operate_req, 'UpdateHotelSceneOperateReq', 'json')
        if not DaraCore.is_null(tmp_req.update_hotel_scene_req):
            request.update_hotel_scene_req_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_hotel_scene_req, 'UpdateHotelSceneReq', 'json')
        query = {}
        if not DaraCore.is_null(request.update_hotel_scene_operate_req_shrink):
            query['UpdateHotelSceneOperateReq'] = request.update_hotel_scene_operate_req_shrink
        if not DaraCore.is_null(request.update_hotel_scene_req_shrink):
            query['UpdateHotelSceneReq'] = request.update_hotel_scene_req_shrink
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHotelSceneItem',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/updateHotelSceneItem',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHotelSceneItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_hotel_scene_item_with_options_async(
        self,
        tmp_req: main_models.UpdateHotelSceneItemRequest,
        headers: main_models.UpdateHotelSceneItemHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHotelSceneItemResponse:
        tmp_req.validate()
        request = main_models.UpdateHotelSceneItemShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_hotel_scene_operate_req):
            request.update_hotel_scene_operate_req_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_hotel_scene_operate_req, 'UpdateHotelSceneOperateReq', 'json')
        if not DaraCore.is_null(tmp_req.update_hotel_scene_req):
            request.update_hotel_scene_req_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_hotel_scene_req, 'UpdateHotelSceneReq', 'json')
        query = {}
        if not DaraCore.is_null(request.update_hotel_scene_operate_req_shrink):
            query['UpdateHotelSceneOperateReq'] = request.update_hotel_scene_operate_req_shrink
        if not DaraCore.is_null(request.update_hotel_scene_req_shrink):
            query['UpdateHotelSceneReq'] = request.update_hotel_scene_req_shrink
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHotelSceneItem',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/updateHotelSceneItem',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHotelSceneItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_hotel_scene_item(
        self,
        request: main_models.UpdateHotelSceneItemRequest,
    ) -> main_models.UpdateHotelSceneItemResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateHotelSceneItemHeaders()
        return self.update_hotel_scene_item_with_options(request, headers, runtime)

    async def update_hotel_scene_item_async(
        self,
        request: main_models.UpdateHotelSceneItemRequest,
    ) -> main_models.UpdateHotelSceneItemResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateHotelSceneItemHeaders()
        return await self.update_hotel_scene_item_with_options_async(request, headers, runtime)

    def update_message_template_with_options(
        self,
        request: main_models.UpdateMessageTemplateRequest,
        headers: main_models.UpdateMessageTemplateHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMessageTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.template_detail):
            body['TemplateDetail'] = request.template_detail
        if not DaraCore.is_null(request.template_id):
            body['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            body['TemplateName'] = request.template_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMessageTemplate',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/updateMessageTemplate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMessageTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_message_template_with_options_async(
        self,
        request: main_models.UpdateMessageTemplateRequest,
        headers: main_models.UpdateMessageTemplateHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMessageTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.template_detail):
            body['TemplateDetail'] = request.template_detail
        if not DaraCore.is_null(request.template_id):
            body['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            body['TemplateName'] = request.template_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMessageTemplate',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/updateMessageTemplate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMessageTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_message_template(
        self,
        request: main_models.UpdateMessageTemplateRequest,
    ) -> main_models.UpdateMessageTemplateResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateMessageTemplateHeaders()
        return self.update_message_template_with_options(request, headers, runtime)

    async def update_message_template_async(
        self,
        request: main_models.UpdateMessageTemplateRequest,
    ) -> main_models.UpdateMessageTemplateResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateMessageTemplateHeaders()
        return await self.update_message_template_with_options_async(request, headers, runtime)

    def update_rcu_scene_with_options(
        self,
        tmp_req: main_models.UpdateRcuSceneRequest,
        headers: main_models.UpdateRcuSceneHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRcuSceneResponse:
        tmp_req.validate()
        request = main_models.UpdateRcuSceneShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scene_relation_ext_dto):
            request.scene_relation_ext_dtoshrink = Utils.array_to_string_with_specified_style(tmp_req.scene_relation_ext_dto, 'SceneRelationExtDTO', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.scene_relation_ext_dtoshrink):
            body['SceneRelationExtDTO'] = request.scene_relation_ext_dtoshrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRcuScene',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/updateRcuScene',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRcuSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rcu_scene_with_options_async(
        self,
        tmp_req: main_models.UpdateRcuSceneRequest,
        headers: main_models.UpdateRcuSceneHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRcuSceneResponse:
        tmp_req.validate()
        request = main_models.UpdateRcuSceneShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scene_relation_ext_dto):
            request.scene_relation_ext_dtoshrink = Utils.array_to_string_with_specified_style(tmp_req.scene_relation_ext_dto, 'SceneRelationExtDTO', 'json')
        body = {}
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.scene_relation_ext_dtoshrink):
            body['SceneRelationExtDTO'] = request.scene_relation_ext_dtoshrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRcuScene',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/updateRcuScene',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRcuSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rcu_scene(
        self,
        request: main_models.UpdateRcuSceneRequest,
    ) -> main_models.UpdateRcuSceneResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateRcuSceneHeaders()
        return self.update_rcu_scene_with_options(request, headers, runtime)

    async def update_rcu_scene_async(
        self,
        request: main_models.UpdateRcuSceneRequest,
    ) -> main_models.UpdateRcuSceneResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateRcuSceneHeaders()
        return await self.update_rcu_scene_with_options_async(request, headers, runtime)

    def update_service_qawith_options(
        self,
        request: main_models.UpdateServiceQARequest,
        headers: main_models.UpdateServiceQAHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceQAResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.answer):
            body['Answer'] = request.answer
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.service_qaid):
            body['ServiceQAId'] = request.service_qaid
        if not DaraCore.is_null(request.is_active):
            body['isActive'] = request.is_active
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceQA',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/updateServiceQA',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceQAResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_qawith_options_async(
        self,
        request: main_models.UpdateServiceQARequest,
        headers: main_models.UpdateServiceQAHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceQAResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.answer):
            body['Answer'] = request.answer
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.service_qaid):
            body['ServiceQAId'] = request.service_qaid
        if not DaraCore.is_null(request.is_active):
            body['isActive'] = request.is_active
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceQA',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/updateServiceQA',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceQAResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_qa(
        self,
        request: main_models.UpdateServiceQARequest,
    ) -> main_models.UpdateServiceQAResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateServiceQAHeaders()
        return self.update_service_qawith_options(request, headers, runtime)

    async def update_service_qa_async(
        self,
        request: main_models.UpdateServiceQARequest,
    ) -> main_models.UpdateServiceQAResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateServiceQAHeaders()
        return await self.update_service_qawith_options_async(request, headers, runtime)

    def update_ticket_with_options(
        self,
        request: main_models.UpdateTicketRequest,
        headers: main_models.UpdateTicketHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTicketResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.group_key):
            body['GroupKey'] = request.group_key
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTicket',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/updateTicket',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ticket_with_options_async(
        self,
        request: main_models.UpdateTicketRequest,
        headers: main_models.UpdateTicketHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTicketResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.group_key):
            body['GroupKey'] = request.group_key
        if not DaraCore.is_null(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTicket',
            version = 'ip_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ip/updateTicket',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ticket(
        self,
        request: main_models.UpdateTicketRequest,
    ) -> main_models.UpdateTicketResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateTicketHeaders()
        return self.update_ticket_with_options(request, headers, runtime)

    async def update_ticket_async(
        self,
        request: main_models.UpdateTicketRequest,
    ) -> main_models.UpdateTicketResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateTicketHeaders()
        return await self.update_ticket_with_options_async(request, headers, runtime)
