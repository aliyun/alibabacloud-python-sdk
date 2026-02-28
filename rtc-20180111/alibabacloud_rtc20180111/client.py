# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_rtc20180111 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.core import DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('rtc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_record_template_with_options(
        self,
        request: main_models.AddRecordTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddRecordTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not DaraCore.is_null(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not DaraCore.is_null(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not DaraCore.is_null(request.delay_stop_time):
            query['DelayStopTime'] = request.delay_stop_time
        if not DaraCore.is_null(request.enable_m3u_8date_time):
            query['EnableM3u8DateTime'] = request.enable_m3u_8date_time
        if not DaraCore.is_null(request.file_split_interval):
            query['FileSplitInterval'] = request.file_split_interval
        if not DaraCore.is_null(request.formats):
            query['Formats'] = request.formats
        if not DaraCore.is_null(request.http_callback_url):
            query['HttpCallbackUrl'] = request.http_callback_url
        if not DaraCore.is_null(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not DaraCore.is_null(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not DaraCore.is_null(request.mns_queue):
            query['MnsQueue'] = request.mns_queue
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not DaraCore.is_null(request.oss_file_prefix):
            query['OssFilePrefix'] = request.oss_file_prefix
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.task_profile):
            query['TaskProfile'] = request.task_profile
        if not DaraCore.is_null(request.watermarks):
            query['Watermarks'] = request.watermarks
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddRecordTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_record_template_with_options_async(
        self,
        request: main_models.AddRecordTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddRecordTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not DaraCore.is_null(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not DaraCore.is_null(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not DaraCore.is_null(request.delay_stop_time):
            query['DelayStopTime'] = request.delay_stop_time
        if not DaraCore.is_null(request.enable_m3u_8date_time):
            query['EnableM3u8DateTime'] = request.enable_m3u_8date_time
        if not DaraCore.is_null(request.file_split_interval):
            query['FileSplitInterval'] = request.file_split_interval
        if not DaraCore.is_null(request.formats):
            query['Formats'] = request.formats
        if not DaraCore.is_null(request.http_callback_url):
            query['HttpCallbackUrl'] = request.http_callback_url
        if not DaraCore.is_null(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not DaraCore.is_null(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not DaraCore.is_null(request.mns_queue):
            query['MnsQueue'] = request.mns_queue
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not DaraCore.is_null(request.oss_file_prefix):
            query['OssFilePrefix'] = request.oss_file_prefix
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.task_profile):
            query['TaskProfile'] = request.task_profile
        if not DaraCore.is_null(request.watermarks):
            query['Watermarks'] = request.watermarks
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddRecordTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRecordTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_record_template(
        self,
        request: main_models.AddRecordTemplateRequest,
    ) -> main_models.AddRecordTemplateResponse:
        runtime = RuntimeOptions()
        return self.add_record_template_with_options(request, runtime)

    async def add_record_template_async(
        self,
        request: main_models.AddRecordTemplateRequest,
    ) -> main_models.AddRecordTemplateResponse:
        runtime = RuntimeOptions()
        return await self.add_record_template_with_options_async(request, runtime)

    def create_app_agent_template_with_options(
        self,
        tmp_req: main_models.CreateAppAgentTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppAgentTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateAppAgentTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_silence_config):
            request.agent_silence_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_silence_config, 'AgentSilenceConfig', 'json')
        if not DaraCore.is_null(tmp_req.ambient_sound_config):
            request.ambient_sound_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.ambient_sound_config, 'AmbientSoundConfig', 'json')
        if not DaraCore.is_null(tmp_req.asr_config):
            request.asr_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.asr_config, 'AsrConfig', 'json')
        if not DaraCore.is_null(tmp_req.back_channel_config):
            request.back_channel_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.back_channel_config, 'BackChannelConfig', 'json')
        if not DaraCore.is_null(tmp_req.interrupt_config):
            request.interrupt_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.interrupt_config, 'InterruptConfig', 'json')
        if not DaraCore.is_null(tmp_req.llm_config):
            request.llm_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.llm_config, 'LlmConfig', 'json')
        if not DaraCore.is_null(tmp_req.tts_config):
            request.tts_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.tts_config, 'TtsConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_silence_config_shrink):
            query['AgentSilenceConfig'] = request.agent_silence_config_shrink
        if not DaraCore.is_null(request.ambient_sound_config_shrink):
            query['AmbientSoundConfig'] = request.ambient_sound_config_shrink
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.asr_config_shrink):
            query['AsrConfig'] = request.asr_config_shrink
        if not DaraCore.is_null(request.back_channel_config_shrink):
            query['BackChannelConfig'] = request.back_channel_config_shrink
        if not DaraCore.is_null(request.chat_mode):
            query['ChatMode'] = request.chat_mode
        if not DaraCore.is_null(request.greeting):
            query['Greeting'] = request.greeting
        if not DaraCore.is_null(request.interrupt_config_shrink):
            query['InterruptConfig'] = request.interrupt_config_shrink
        if not DaraCore.is_null(request.interrupt_mode):
            query['InterruptMode'] = request.interrupt_mode
        if not DaraCore.is_null(request.llm_config_shrink):
            query['LlmConfig'] = request.llm_config_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.tts_config_shrink):
            query['TtsConfig'] = request.tts_config_shrink
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppAgentTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppAgentTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_agent_template_with_options_async(
        self,
        tmp_req: main_models.CreateAppAgentTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppAgentTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateAppAgentTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_silence_config):
            request.agent_silence_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_silence_config, 'AgentSilenceConfig', 'json')
        if not DaraCore.is_null(tmp_req.ambient_sound_config):
            request.ambient_sound_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.ambient_sound_config, 'AmbientSoundConfig', 'json')
        if not DaraCore.is_null(tmp_req.asr_config):
            request.asr_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.asr_config, 'AsrConfig', 'json')
        if not DaraCore.is_null(tmp_req.back_channel_config):
            request.back_channel_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.back_channel_config, 'BackChannelConfig', 'json')
        if not DaraCore.is_null(tmp_req.interrupt_config):
            request.interrupt_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.interrupt_config, 'InterruptConfig', 'json')
        if not DaraCore.is_null(tmp_req.llm_config):
            request.llm_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.llm_config, 'LlmConfig', 'json')
        if not DaraCore.is_null(tmp_req.tts_config):
            request.tts_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.tts_config, 'TtsConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_silence_config_shrink):
            query['AgentSilenceConfig'] = request.agent_silence_config_shrink
        if not DaraCore.is_null(request.ambient_sound_config_shrink):
            query['AmbientSoundConfig'] = request.ambient_sound_config_shrink
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.asr_config_shrink):
            query['AsrConfig'] = request.asr_config_shrink
        if not DaraCore.is_null(request.back_channel_config_shrink):
            query['BackChannelConfig'] = request.back_channel_config_shrink
        if not DaraCore.is_null(request.chat_mode):
            query['ChatMode'] = request.chat_mode
        if not DaraCore.is_null(request.greeting):
            query['Greeting'] = request.greeting
        if not DaraCore.is_null(request.interrupt_config_shrink):
            query['InterruptConfig'] = request.interrupt_config_shrink
        if not DaraCore.is_null(request.interrupt_mode):
            query['InterruptMode'] = request.interrupt_mode
        if not DaraCore.is_null(request.llm_config_shrink):
            query['LlmConfig'] = request.llm_config_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.tts_config_shrink):
            query['TtsConfig'] = request.tts_config_shrink
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppAgentTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppAgentTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_agent_template(
        self,
        request: main_models.CreateAppAgentTemplateRequest,
    ) -> main_models.CreateAppAgentTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_app_agent_template_with_options(request, runtime)

    async def create_app_agent_template_async(
        self,
        request: main_models.CreateAppAgentTemplateRequest,
    ) -> main_models.CreateAppAgentTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_app_agent_template_with_options_async(request, runtime)

    def create_app_layout_with_options(
        self,
        tmp_req: main_models.CreateAppLayoutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppLayoutResponse:
        tmp_req.validate()
        request = main_models.CreateAppLayoutShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.layout):
            request.layout_shrink = Utils.array_to_string_with_specified_style(tmp_req.layout, 'Layout', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.layout_shrink):
            query['Layout'] = request.layout_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppLayout',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppLayoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_layout_with_options_async(
        self,
        tmp_req: main_models.CreateAppLayoutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppLayoutResponse:
        tmp_req.validate()
        request = main_models.CreateAppLayoutShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.layout):
            request.layout_shrink = Utils.array_to_string_with_specified_style(tmp_req.layout, 'Layout', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.layout_shrink):
            query['Layout'] = request.layout_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppLayout',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppLayoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_layout(
        self,
        request: main_models.CreateAppLayoutRequest,
    ) -> main_models.CreateAppLayoutResponse:
        runtime = RuntimeOptions()
        return self.create_app_layout_with_options(request, runtime)

    async def create_app_layout_async(
        self,
        request: main_models.CreateAppLayoutRequest,
    ) -> main_models.CreateAppLayoutResponse:
        runtime = RuntimeOptions()
        return await self.create_app_layout_with_options_async(request, runtime)

    def create_app_record_template_with_options(
        self,
        tmp_req: main_models.CreateAppRecordTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppRecordTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateAppRecordTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.record_template):
            request.record_template_shrink = Utils.array_to_string_with_specified_style(tmp_req.record_template, 'RecordTemplate', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.record_template_shrink):
            query['RecordTemplate'] = request.record_template_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppRecordTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_record_template_with_options_async(
        self,
        tmp_req: main_models.CreateAppRecordTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppRecordTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateAppRecordTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.record_template):
            request.record_template_shrink = Utils.array_to_string_with_specified_style(tmp_req.record_template, 'RecordTemplate', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.record_template_shrink):
            query['RecordTemplate'] = request.record_template_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppRecordTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppRecordTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_record_template(
        self,
        request: main_models.CreateAppRecordTemplateRequest,
    ) -> main_models.CreateAppRecordTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_app_record_template_with_options(request, runtime)

    async def create_app_record_template_async(
        self,
        request: main_models.CreateAppRecordTemplateRequest,
    ) -> main_models.CreateAppRecordTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_app_record_template_with_options_async(request, runtime)

    def create_app_streaming_out_template_with_options(
        self,
        tmp_req: main_models.CreateAppStreamingOutTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppStreamingOutTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateAppStreamingOutTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.streaming_out_template):
            request.streaming_out_template_shrink = Utils.array_to_string_with_specified_style(tmp_req.streaming_out_template, 'StreamingOutTemplate', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.streaming_out_template_shrink):
            query['StreamingOutTemplate'] = request.streaming_out_template_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppStreamingOutTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppStreamingOutTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_streaming_out_template_with_options_async(
        self,
        tmp_req: main_models.CreateAppStreamingOutTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppStreamingOutTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateAppStreamingOutTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.streaming_out_template):
            request.streaming_out_template_shrink = Utils.array_to_string_with_specified_style(tmp_req.streaming_out_template, 'StreamingOutTemplate', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.streaming_out_template_shrink):
            query['StreamingOutTemplate'] = request.streaming_out_template_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppStreamingOutTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppStreamingOutTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_streaming_out_template(
        self,
        request: main_models.CreateAppStreamingOutTemplateRequest,
    ) -> main_models.CreateAppStreamingOutTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_app_streaming_out_template_with_options(request, runtime)

    async def create_app_streaming_out_template_async(
        self,
        request: main_models.CreateAppStreamingOutTemplateRequest,
    ) -> main_models.CreateAppStreamingOutTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_app_streaming_out_template_with_options_async(request, runtime)

    def create_app_view_template_with_options(
        self,
        tmp_req: main_models.CreateAppViewTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppViewTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateAppViewTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.template):
            request.template_shrink = Utils.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.template_shrink):
            query['Template'] = request.template_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppViewTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppViewTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_view_template_with_options_async(
        self,
        tmp_req: main_models.CreateAppViewTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppViewTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateAppViewTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.template):
            request.template_shrink = Utils.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.template_shrink):
            query['Template'] = request.template_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppViewTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppViewTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_view_template(
        self,
        request: main_models.CreateAppViewTemplateRequest,
    ) -> main_models.CreateAppViewTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_app_view_template_with_options(request, runtime)

    async def create_app_view_template_async(
        self,
        request: main_models.CreateAppViewTemplateRequest,
    ) -> main_models.CreateAppViewTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_app_view_template_with_options_async(request, runtime)

    def create_auto_live_stream_rule_with_options(
        self,
        request: main_models.CreateAutoLiveStreamRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAutoLiveStreamRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.call_back):
            query['CallBack'] = request.call_back
        if not DaraCore.is_null(request.channel_id_prefixes):
            query['ChannelIdPrefixes'] = request.channel_id_prefixes
        if not DaraCore.is_null(request.channel_ids):
            query['ChannelIds'] = request.channel_ids
        if not DaraCore.is_null(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAutoLiveStreamRule',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_auto_live_stream_rule_with_options_async(
        self,
        request: main_models.CreateAutoLiveStreamRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAutoLiveStreamRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.call_back):
            query['CallBack'] = request.call_back
        if not DaraCore.is_null(request.channel_id_prefixes):
            query['ChannelIdPrefixes'] = request.channel_id_prefixes
        if not DaraCore.is_null(request.channel_ids):
            query['ChannelIds'] = request.channel_ids
        if not DaraCore.is_null(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAutoLiveStreamRule',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAutoLiveStreamRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_auto_live_stream_rule(
        self,
        request: main_models.CreateAutoLiveStreamRuleRequest,
    ) -> main_models.CreateAutoLiveStreamRuleResponse:
        runtime = RuntimeOptions()
        return self.create_auto_live_stream_rule_with_options(request, runtime)

    async def create_auto_live_stream_rule_async(
        self,
        request: main_models.CreateAutoLiveStreamRuleRequest,
    ) -> main_models.CreateAutoLiveStreamRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_auto_live_stream_rule_with_options_async(request, runtime)

    def create_cloud_note_phrases_with_options(
        self,
        tmp_req: main_models.CreateCloudNotePhrasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudNotePhrasesResponse:
        tmp_req.validate()
        request = main_models.CreateCloudNotePhrasesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.phrase):
            request.phrase_shrink = Utils.array_to_string_with_specified_style(tmp_req.phrase, 'Phrase', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.phrase_shrink):
            query['Phrase'] = request.phrase_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudNotePhrases',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudNotePhrasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_note_phrases_with_options_async(
        self,
        tmp_req: main_models.CreateCloudNotePhrasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudNotePhrasesResponse:
        tmp_req.validate()
        request = main_models.CreateCloudNotePhrasesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.phrase):
            request.phrase_shrink = Utils.array_to_string_with_specified_style(tmp_req.phrase, 'Phrase', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.phrase_shrink):
            query['Phrase'] = request.phrase_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudNotePhrases',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudNotePhrasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_note_phrases(
        self,
        request: main_models.CreateCloudNotePhrasesRequest,
    ) -> main_models.CreateCloudNotePhrasesResponse:
        runtime = RuntimeOptions()
        return self.create_cloud_note_phrases_with_options(request, runtime)

    async def create_cloud_note_phrases_async(
        self,
        request: main_models.CreateCloudNotePhrasesRequest,
    ) -> main_models.CreateCloudNotePhrasesResponse:
        runtime = RuntimeOptions()
        return await self.create_cloud_note_phrases_with_options_async(request, runtime)

    def create_event_subscribe_with_options(
        self,
        request: main_models.CreateEventSubscribeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEventSubscribeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.events):
            query['Events'] = request.events
        if not DaraCore.is_null(request.need_callback_auth):
            query['NeedCallbackAuth'] = request.need_callback_auth
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        if not DaraCore.is_null(request.users):
            query['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateEventSubscribe',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEventSubscribeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_event_subscribe_with_options_async(
        self,
        request: main_models.CreateEventSubscribeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEventSubscribeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.events):
            query['Events'] = request.events
        if not DaraCore.is_null(request.need_callback_auth):
            query['NeedCallbackAuth'] = request.need_callback_auth
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        if not DaraCore.is_null(request.users):
            query['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateEventSubscribe',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEventSubscribeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_event_subscribe(
        self,
        request: main_models.CreateEventSubscribeRequest,
    ) -> main_models.CreateEventSubscribeResponse:
        runtime = RuntimeOptions()
        return self.create_event_subscribe_with_options(request, runtime)

    async def create_event_subscribe_async(
        self,
        request: main_models.CreateEventSubscribeRequest,
    ) -> main_models.CreateEventSubscribeResponse:
        runtime = RuntimeOptions()
        return await self.create_event_subscribe_with_options_async(request, runtime)

    def create_mpulayout_with_options(
        self,
        request: main_models.CreateMPULayoutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMPULayoutResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.audio_mix_count):
            query['AudioMixCount'] = request.audio_mix_count
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.panes):
            query['Panes'] = request.panes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMPULayout',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMPULayoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mpulayout_with_options_async(
        self,
        request: main_models.CreateMPULayoutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMPULayoutResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.audio_mix_count):
            query['AudioMixCount'] = request.audio_mix_count
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.panes):
            query['Panes'] = request.panes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMPULayout',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMPULayoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mpulayout(
        self,
        request: main_models.CreateMPULayoutRequest,
    ) -> main_models.CreateMPULayoutResponse:
        runtime = RuntimeOptions()
        return self.create_mpulayout_with_options(request, runtime)

    async def create_mpulayout_async(
        self,
        request: main_models.CreateMPULayoutRequest,
    ) -> main_models.CreateMPULayoutResponse:
        runtime = RuntimeOptions()
        return await self.create_mpulayout_with_options_async(request, runtime)

    def delete_app_agent_template_with_options(
        self,
        request: main_models.DeleteAppAgentTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppAgentTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppAgentTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppAgentTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_agent_template_with_options_async(
        self,
        request: main_models.DeleteAppAgentTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppAgentTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppAgentTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppAgentTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_agent_template(
        self,
        request: main_models.DeleteAppAgentTemplateRequest,
    ) -> main_models.DeleteAppAgentTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_app_agent_template_with_options(request, runtime)

    async def delete_app_agent_template_async(
        self,
        request: main_models.DeleteAppAgentTemplateRequest,
    ) -> main_models.DeleteAppAgentTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_app_agent_template_with_options_async(request, runtime)

    def delete_app_layout_with_options(
        self,
        tmp_req: main_models.DeleteAppLayoutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppLayoutResponse:
        tmp_req.validate()
        request = main_models.DeleteAppLayoutShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.layout):
            request.layout_shrink = Utils.array_to_string_with_specified_style(tmp_req.layout, 'Layout', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.layout_shrink):
            query['Layout'] = request.layout_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppLayout',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppLayoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_layout_with_options_async(
        self,
        tmp_req: main_models.DeleteAppLayoutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppLayoutResponse:
        tmp_req.validate()
        request = main_models.DeleteAppLayoutShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.layout):
            request.layout_shrink = Utils.array_to_string_with_specified_style(tmp_req.layout, 'Layout', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.layout_shrink):
            query['Layout'] = request.layout_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppLayout',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppLayoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_layout(
        self,
        request: main_models.DeleteAppLayoutRequest,
    ) -> main_models.DeleteAppLayoutResponse:
        runtime = RuntimeOptions()
        return self.delete_app_layout_with_options(request, runtime)

    async def delete_app_layout_async(
        self,
        request: main_models.DeleteAppLayoutRequest,
    ) -> main_models.DeleteAppLayoutResponse:
        runtime = RuntimeOptions()
        return await self.delete_app_layout_with_options_async(request, runtime)

    def delete_app_record_template_with_options(
        self,
        tmp_req: main_models.DeleteAppRecordTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppRecordTemplateResponse:
        tmp_req.validate()
        request = main_models.DeleteAppRecordTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.template):
            request.template_shrink = Utils.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.template_shrink):
            query['Template'] = request.template_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppRecordTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_record_template_with_options_async(
        self,
        tmp_req: main_models.DeleteAppRecordTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppRecordTemplateResponse:
        tmp_req.validate()
        request = main_models.DeleteAppRecordTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.template):
            request.template_shrink = Utils.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.template_shrink):
            query['Template'] = request.template_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppRecordTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppRecordTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_record_template(
        self,
        request: main_models.DeleteAppRecordTemplateRequest,
    ) -> main_models.DeleteAppRecordTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_app_record_template_with_options(request, runtime)

    async def delete_app_record_template_async(
        self,
        request: main_models.DeleteAppRecordTemplateRequest,
    ) -> main_models.DeleteAppRecordTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_app_record_template_with_options_async(request, runtime)

    def delete_app_streaming_out_template_with_options(
        self,
        tmp_req: main_models.DeleteAppStreamingOutTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppStreamingOutTemplateResponse:
        tmp_req.validate()
        request = main_models.DeleteAppStreamingOutTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.streaming_out_template):
            request.streaming_out_template_shrink = Utils.array_to_string_with_specified_style(tmp_req.streaming_out_template, 'StreamingOutTemplate', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.streaming_out_template_shrink):
            query['StreamingOutTemplate'] = request.streaming_out_template_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppStreamingOutTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppStreamingOutTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_streaming_out_template_with_options_async(
        self,
        tmp_req: main_models.DeleteAppStreamingOutTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppStreamingOutTemplateResponse:
        tmp_req.validate()
        request = main_models.DeleteAppStreamingOutTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.streaming_out_template):
            request.streaming_out_template_shrink = Utils.array_to_string_with_specified_style(tmp_req.streaming_out_template, 'StreamingOutTemplate', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.streaming_out_template_shrink):
            query['StreamingOutTemplate'] = request.streaming_out_template_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppStreamingOutTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppStreamingOutTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_streaming_out_template(
        self,
        request: main_models.DeleteAppStreamingOutTemplateRequest,
    ) -> main_models.DeleteAppStreamingOutTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_app_streaming_out_template_with_options(request, runtime)

    async def delete_app_streaming_out_template_async(
        self,
        request: main_models.DeleteAppStreamingOutTemplateRequest,
    ) -> main_models.DeleteAppStreamingOutTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_app_streaming_out_template_with_options_async(request, runtime)

    def delete_app_view_template_with_options(
        self,
        tmp_req: main_models.DeleteAppViewTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppViewTemplateResponse:
        tmp_req.validate()
        request = main_models.DeleteAppViewTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.template):
            request.template_shrink = Utils.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.template_shrink):
            query['Template'] = request.template_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppViewTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppViewTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_view_template_with_options_async(
        self,
        tmp_req: main_models.DeleteAppViewTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppViewTemplateResponse:
        tmp_req.validate()
        request = main_models.DeleteAppViewTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.template):
            request.template_shrink = Utils.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.template_shrink):
            query['Template'] = request.template_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppViewTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppViewTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_view_template(
        self,
        request: main_models.DeleteAppViewTemplateRequest,
    ) -> main_models.DeleteAppViewTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_app_view_template_with_options(request, runtime)

    async def delete_app_view_template_async(
        self,
        request: main_models.DeleteAppViewTemplateRequest,
    ) -> main_models.DeleteAppViewTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_app_view_template_with_options_async(request, runtime)

    def delete_auto_live_stream_rule_with_options(
        self,
        request: main_models.DeleteAutoLiveStreamRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAutoLiveStreamRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAutoLiveStreamRule',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_auto_live_stream_rule_with_options_async(
        self,
        request: main_models.DeleteAutoLiveStreamRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAutoLiveStreamRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAutoLiveStreamRule',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAutoLiveStreamRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_auto_live_stream_rule(
        self,
        request: main_models.DeleteAutoLiveStreamRuleRequest,
    ) -> main_models.DeleteAutoLiveStreamRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_auto_live_stream_rule_with_options(request, runtime)

    async def delete_auto_live_stream_rule_async(
        self,
        request: main_models.DeleteAutoLiveStreamRuleRequest,
    ) -> main_models.DeleteAutoLiveStreamRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_auto_live_stream_rule_with_options_async(request, runtime)

    def delete_channel_with_options(
        self,
        request: main_models.DeleteChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChannel',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_channel_with_options_async(
        self,
        request: main_models.DeleteChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChannel',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_channel(
        self,
        request: main_models.DeleteChannelRequest,
    ) -> main_models.DeleteChannelResponse:
        runtime = RuntimeOptions()
        return self.delete_channel_with_options(request, runtime)

    async def delete_channel_async(
        self,
        request: main_models.DeleteChannelRequest,
    ) -> main_models.DeleteChannelResponse:
        runtime = RuntimeOptions()
        return await self.delete_channel_with_options_async(request, runtime)

    def delete_cloud_note_phrases_with_options(
        self,
        tmp_req: main_models.DeleteCloudNotePhrasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudNotePhrasesResponse:
        tmp_req.validate()
        request = main_models.DeleteCloudNotePhrasesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.phrase):
            request.phrase_shrink = Utils.array_to_string_with_specified_style(tmp_req.phrase, 'Phrase', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.phrase_shrink):
            query['Phrase'] = request.phrase_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudNotePhrases',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudNotePhrasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_note_phrases_with_options_async(
        self,
        tmp_req: main_models.DeleteCloudNotePhrasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudNotePhrasesResponse:
        tmp_req.validate()
        request = main_models.DeleteCloudNotePhrasesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.phrase):
            request.phrase_shrink = Utils.array_to_string_with_specified_style(tmp_req.phrase, 'Phrase', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.phrase_shrink):
            query['Phrase'] = request.phrase_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudNotePhrases',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudNotePhrasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloud_note_phrases(
        self,
        request: main_models.DeleteCloudNotePhrasesRequest,
    ) -> main_models.DeleteCloudNotePhrasesResponse:
        runtime = RuntimeOptions()
        return self.delete_cloud_note_phrases_with_options(request, runtime)

    async def delete_cloud_note_phrases_async(
        self,
        request: main_models.DeleteCloudNotePhrasesRequest,
    ) -> main_models.DeleteCloudNotePhrasesResponse:
        runtime = RuntimeOptions()
        return await self.delete_cloud_note_phrases_with_options_async(request, runtime)

    def delete_event_subscribe_with_options(
        self,
        request: main_models.DeleteEventSubscribeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventSubscribeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.subscribe_id):
            query['SubscribeId'] = request.subscribe_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventSubscribe',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventSubscribeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_subscribe_with_options_async(
        self,
        request: main_models.DeleteEventSubscribeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventSubscribeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.subscribe_id):
            query['SubscribeId'] = request.subscribe_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventSubscribe',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventSubscribeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_event_subscribe(
        self,
        request: main_models.DeleteEventSubscribeRequest,
    ) -> main_models.DeleteEventSubscribeResponse:
        runtime = RuntimeOptions()
        return self.delete_event_subscribe_with_options(request, runtime)

    async def delete_event_subscribe_async(
        self,
        request: main_models.DeleteEventSubscribeRequest,
    ) -> main_models.DeleteEventSubscribeResponse:
        runtime = RuntimeOptions()
        return await self.delete_event_subscribe_with_options_async(request, runtime)

    def delete_mpulayout_with_options(
        self,
        request: main_models.DeleteMPULayoutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMPULayoutResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMPULayout',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMPULayoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mpulayout_with_options_async(
        self,
        request: main_models.DeleteMPULayoutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMPULayoutResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMPULayout',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMPULayoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mpulayout(
        self,
        request: main_models.DeleteMPULayoutRequest,
    ) -> main_models.DeleteMPULayoutResponse:
        runtime = RuntimeOptions()
        return self.delete_mpulayout_with_options(request, runtime)

    async def delete_mpulayout_async(
        self,
        request: main_models.DeleteMPULayoutRequest,
    ) -> main_models.DeleteMPULayoutResponse:
        runtime = RuntimeOptions()
        return await self.delete_mpulayout_with_options_async(request, runtime)

    def delete_record_template_with_options(
        self,
        request: main_models.DeleteRecordTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRecordTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRecordTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_record_template_with_options_async(
        self,
        request: main_models.DeleteRecordTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRecordTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRecordTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRecordTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_record_template(
        self,
        request: main_models.DeleteRecordTemplateRequest,
    ) -> main_models.DeleteRecordTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_record_template_with_options(request, runtime)

    async def delete_record_template_async(
        self,
        request: main_models.DeleteRecordTemplateRequest,
    ) -> main_models.DeleteRecordTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_record_template_with_options_async(request, runtime)

    def describe_all_callback_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAllCallbackResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeAllCallback',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAllCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_callback_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAllCallbackResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeAllCallback',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAllCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_callback(self) -> main_models.DescribeAllCallbackResponse:
        runtime = RuntimeOptions()
        return self.describe_all_callback_with_options(runtime)

    async def describe_all_callback_async(self) -> main_models.DescribeAllCallbackResponse:
        runtime = RuntimeOptions()
        return await self.describe_all_callback_with_options_async(runtime)

    def describe_app_agent_function_status_with_options(
        self,
        request: main_models.DescribeAppAgentFunctionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppAgentFunctionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppAgentFunctionStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppAgentFunctionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_agent_function_status_with_options_async(
        self,
        request: main_models.DescribeAppAgentFunctionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppAgentFunctionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppAgentFunctionStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppAgentFunctionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_agent_function_status(
        self,
        request: main_models.DescribeAppAgentFunctionStatusRequest,
    ) -> main_models.DescribeAppAgentFunctionStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_app_agent_function_status_with_options(request, runtime)

    async def describe_app_agent_function_status_async(
        self,
        request: main_models.DescribeAppAgentFunctionStatusRequest,
    ) -> main_models.DescribeAppAgentFunctionStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_app_agent_function_status_with_options_async(request, runtime)

    def describe_app_agent_templates_with_options(
        self,
        request: main_models.DescribeAppAgentTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppAgentTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppAgentTemplates',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppAgentTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_agent_templates_with_options_async(
        self,
        request: main_models.DescribeAppAgentTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppAgentTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppAgentTemplates',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppAgentTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_agent_templates(
        self,
        request: main_models.DescribeAppAgentTemplatesRequest,
    ) -> main_models.DescribeAppAgentTemplatesResponse:
        runtime = RuntimeOptions()
        return self.describe_app_agent_templates_with_options(request, runtime)

    async def describe_app_agent_templates_async(
        self,
        request: main_models.DescribeAppAgentTemplatesRequest,
    ) -> main_models.DescribeAppAgentTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.describe_app_agent_templates_with_options_async(request, runtime)

    def describe_app_call_status_with_options(
        self,
        request: main_models.DescribeAppCallStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppCallStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppCallStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppCallStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_call_status_with_options_async(
        self,
        request: main_models.DescribeAppCallStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppCallStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppCallStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppCallStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_call_status(
        self,
        request: main_models.DescribeAppCallStatusRequest,
    ) -> main_models.DescribeAppCallStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_app_call_status_with_options(request, runtime)

    async def describe_app_call_status_async(
        self,
        request: main_models.DescribeAppCallStatusRequest,
    ) -> main_models.DescribeAppCallStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_app_call_status_with_options_async(request, runtime)

    def describe_app_callback_secret_key_with_options(
        self,
        request: main_models.DescribeAppCallbackSecretKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppCallbackSecretKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppCallbackSecretKey',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppCallbackSecretKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_callback_secret_key_with_options_async(
        self,
        request: main_models.DescribeAppCallbackSecretKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppCallbackSecretKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppCallbackSecretKey',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppCallbackSecretKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_callback_secret_key(
        self,
        request: main_models.DescribeAppCallbackSecretKeyRequest,
    ) -> main_models.DescribeAppCallbackSecretKeyResponse:
        runtime = RuntimeOptions()
        return self.describe_app_callback_secret_key_with_options(request, runtime)

    async def describe_app_callback_secret_key_async(
        self,
        request: main_models.DescribeAppCallbackSecretKeyRequest,
    ) -> main_models.DescribeAppCallbackSecretKeyResponse:
        runtime = RuntimeOptions()
        return await self.describe_app_callback_secret_key_with_options_async(request, runtime)

    def describe_app_key_with_options(
        self,
        request: main_models.DescribeAppKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppKey',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_key_with_options_async(
        self,
        request: main_models.DescribeAppKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppKey',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_key(
        self,
        request: main_models.DescribeAppKeyRequest,
    ) -> main_models.DescribeAppKeyResponse:
        runtime = RuntimeOptions()
        return self.describe_app_key_with_options(request, runtime)

    async def describe_app_key_async(
        self,
        request: main_models.DescribeAppKeyRequest,
    ) -> main_models.DescribeAppKeyResponse:
        runtime = RuntimeOptions()
        return await self.describe_app_key_with_options_async(request, runtime)

    def describe_app_layouts_with_options(
        self,
        tmp_req: main_models.DescribeAppLayoutsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppLayoutsResponse:
        tmp_req.validate()
        request = main_models.DescribeAppLayoutsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.condition):
            request.condition_shrink = Utils.array_to_string_with_specified_style(tmp_req.condition, 'Condition', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppLayouts',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppLayoutsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_layouts_with_options_async(
        self,
        tmp_req: main_models.DescribeAppLayoutsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppLayoutsResponse:
        tmp_req.validate()
        request = main_models.DescribeAppLayoutsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.condition):
            request.condition_shrink = Utils.array_to_string_with_specified_style(tmp_req.condition, 'Condition', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppLayouts',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppLayoutsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_layouts(
        self,
        request: main_models.DescribeAppLayoutsRequest,
    ) -> main_models.DescribeAppLayoutsResponse:
        runtime = RuntimeOptions()
        return self.describe_app_layouts_with_options(request, runtime)

    async def describe_app_layouts_async(
        self,
        request: main_models.DescribeAppLayoutsRequest,
    ) -> main_models.DescribeAppLayoutsResponse:
        runtime = RuntimeOptions()
        return await self.describe_app_layouts_with_options_async(request, runtime)

    def describe_app_live_stream_status_with_options(
        self,
        request: main_models.DescribeAppLiveStreamStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppLiveStreamStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppLiveStreamStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppLiveStreamStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_live_stream_status_with_options_async(
        self,
        request: main_models.DescribeAppLiveStreamStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppLiveStreamStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppLiveStreamStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppLiveStreamStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_live_stream_status(
        self,
        request: main_models.DescribeAppLiveStreamStatusRequest,
    ) -> main_models.DescribeAppLiveStreamStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_app_live_stream_status_with_options(request, runtime)

    async def describe_app_live_stream_status_async(
        self,
        request: main_models.DescribeAppLiveStreamStatusRequest,
    ) -> main_models.DescribeAppLiveStreamStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_app_live_stream_status_with_options_async(request, runtime)

    def describe_app_record_status_with_options(
        self,
        request: main_models.DescribeAppRecordStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppRecordStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppRecordStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppRecordStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_record_status_with_options_async(
        self,
        request: main_models.DescribeAppRecordStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppRecordStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppRecordStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppRecordStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_record_status(
        self,
        request: main_models.DescribeAppRecordStatusRequest,
    ) -> main_models.DescribeAppRecordStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_app_record_status_with_options(request, runtime)

    async def describe_app_record_status_async(
        self,
        request: main_models.DescribeAppRecordStatusRequest,
    ) -> main_models.DescribeAppRecordStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_app_record_status_with_options_async(request, runtime)

    def describe_app_record_templates_with_options(
        self,
        tmp_req: main_models.DescribeAppRecordTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppRecordTemplatesResponse:
        tmp_req.validate()
        request = main_models.DescribeAppRecordTemplatesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.condition):
            request.condition_shrink = Utils.array_to_string_with_specified_style(tmp_req.condition, 'Condition', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppRecordTemplates',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppRecordTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_record_templates_with_options_async(
        self,
        tmp_req: main_models.DescribeAppRecordTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppRecordTemplatesResponse:
        tmp_req.validate()
        request = main_models.DescribeAppRecordTemplatesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.condition):
            request.condition_shrink = Utils.array_to_string_with_specified_style(tmp_req.condition, 'Condition', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppRecordTemplates',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppRecordTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_record_templates(
        self,
        request: main_models.DescribeAppRecordTemplatesRequest,
    ) -> main_models.DescribeAppRecordTemplatesResponse:
        runtime = RuntimeOptions()
        return self.describe_app_record_templates_with_options(request, runtime)

    async def describe_app_record_templates_async(
        self,
        request: main_models.DescribeAppRecordTemplatesRequest,
    ) -> main_models.DescribeAppRecordTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.describe_app_record_templates_with_options_async(request, runtime)

    def describe_app_recording_files_with_options(
        self,
        tmp_req: main_models.DescribeAppRecordingFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppRecordingFilesResponse:
        tmp_req.validate()
        request = main_models.DescribeAppRecordingFilesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_ids):
            request.task_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppRecordingFiles',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppRecordingFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_recording_files_with_options_async(
        self,
        tmp_req: main_models.DescribeAppRecordingFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppRecordingFilesResponse:
        tmp_req.validate()
        request = main_models.DescribeAppRecordingFilesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_ids):
            request.task_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppRecordingFiles',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppRecordingFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_recording_files(
        self,
        request: main_models.DescribeAppRecordingFilesRequest,
    ) -> main_models.DescribeAppRecordingFilesResponse:
        runtime = RuntimeOptions()
        return self.describe_app_recording_files_with_options(request, runtime)

    async def describe_app_recording_files_async(
        self,
        request: main_models.DescribeAppRecordingFilesRequest,
    ) -> main_models.DescribeAppRecordingFilesResponse:
        runtime = RuntimeOptions()
        return await self.describe_app_recording_files_with_options_async(request, runtime)

    def describe_app_streaming_out_templates_with_options(
        self,
        tmp_req: main_models.DescribeAppStreamingOutTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppStreamingOutTemplatesResponse:
        tmp_req.validate()
        request = main_models.DescribeAppStreamingOutTemplatesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.condition):
            request.condition_shrink = Utils.array_to_string_with_specified_style(tmp_req.condition, 'Condition', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.condition_shrink):
            query['Condition'] = request.condition_shrink
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppStreamingOutTemplates',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppStreamingOutTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_streaming_out_templates_with_options_async(
        self,
        tmp_req: main_models.DescribeAppStreamingOutTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppStreamingOutTemplatesResponse:
        tmp_req.validate()
        request = main_models.DescribeAppStreamingOutTemplatesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.condition):
            request.condition_shrink = Utils.array_to_string_with_specified_style(tmp_req.condition, 'Condition', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.condition_shrink):
            query['Condition'] = request.condition_shrink
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppStreamingOutTemplates',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppStreamingOutTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_streaming_out_templates(
        self,
        request: main_models.DescribeAppStreamingOutTemplatesRequest,
    ) -> main_models.DescribeAppStreamingOutTemplatesResponse:
        runtime = RuntimeOptions()
        return self.describe_app_streaming_out_templates_with_options(request, runtime)

    async def describe_app_streaming_out_templates_async(
        self,
        request: main_models.DescribeAppStreamingOutTemplatesRequest,
    ) -> main_models.DescribeAppStreamingOutTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.describe_app_streaming_out_templates_with_options_async(request, runtime)

    def describe_app_view_status_with_options(
        self,
        request: main_models.DescribeAppViewStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppViewStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppViewStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppViewStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_view_status_with_options_async(
        self,
        request: main_models.DescribeAppViewStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppViewStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppViewStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppViewStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_view_status(
        self,
        request: main_models.DescribeAppViewStatusRequest,
    ) -> main_models.DescribeAppViewStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_app_view_status_with_options(request, runtime)

    async def describe_app_view_status_async(
        self,
        request: main_models.DescribeAppViewStatusRequest,
    ) -> main_models.DescribeAppViewStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_app_view_status_with_options_async(request, runtime)

    def describe_app_view_templates_with_options(
        self,
        tmp_req: main_models.DescribeAppViewTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppViewTemplatesResponse:
        tmp_req.validate()
        request = main_models.DescribeAppViewTemplatesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.condition):
            request.condition_shrink = Utils.array_to_string_with_specified_style(tmp_req.condition, 'Condition', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.condition_shrink):
            query['Condition'] = request.condition_shrink
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppViewTemplates',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppViewTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_view_templates_with_options_async(
        self,
        tmp_req: main_models.DescribeAppViewTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppViewTemplatesResponse:
        tmp_req.validate()
        request = main_models.DescribeAppViewTemplatesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.condition):
            request.condition_shrink = Utils.array_to_string_with_specified_style(tmp_req.condition, 'Condition', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.condition_shrink):
            query['Condition'] = request.condition_shrink
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppViewTemplates',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppViewTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_view_templates(
        self,
        request: main_models.DescribeAppViewTemplatesRequest,
    ) -> main_models.DescribeAppViewTemplatesResponse:
        runtime = RuntimeOptions()
        return self.describe_app_view_templates_with_options(request, runtime)

    async def describe_app_view_templates_async(
        self,
        request: main_models.DescribeAppViewTemplatesRequest,
    ) -> main_models.DescribeAppViewTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.describe_app_view_templates_with_options_async(request, runtime)

    def describe_apps_with_options(
        self,
        request: main_models.DescribeAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_version):
            query['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApps',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apps_with_options_async(
        self,
        request: main_models.DescribeAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_version):
            query['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApps',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apps(
        self,
        request: main_models.DescribeAppsRequest,
    ) -> main_models.DescribeAppsResponse:
        runtime = RuntimeOptions()
        return self.describe_apps_with_options(request, runtime)

    async def describe_apps_async(
        self,
        request: main_models.DescribeAppsRequest,
    ) -> main_models.DescribeAppsResponse:
        runtime = RuntimeOptions()
        return await self.describe_apps_with_options_async(request, runtime)

    def describe_auto_live_stream_rule_with_options(
        self,
        request: main_models.DescribeAutoLiveStreamRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutoLiveStreamRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutoLiveStreamRule',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_live_stream_rule_with_options_async(
        self,
        request: main_models.DescribeAutoLiveStreamRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutoLiveStreamRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutoLiveStreamRule',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutoLiveStreamRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auto_live_stream_rule(
        self,
        request: main_models.DescribeAutoLiveStreamRuleRequest,
    ) -> main_models.DescribeAutoLiveStreamRuleResponse:
        runtime = RuntimeOptions()
        return self.describe_auto_live_stream_rule_with_options(request, runtime)

    async def describe_auto_live_stream_rule_async(
        self,
        request: main_models.DescribeAutoLiveStreamRuleRequest,
    ) -> main_models.DescribeAutoLiveStreamRuleResponse:
        runtime = RuntimeOptions()
        return await self.describe_auto_live_stream_rule_with_options_async(request, runtime)

    def describe_call_with_options(
        self,
        request: main_models.DescribeCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not DaraCore.is_null(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not DaraCore.is_null(request.ext_data_type):
            query['ExtDataType'] = request.ext_data_type
        if not DaraCore.is_null(request.query_exp_info):
            query['QueryExpInfo'] = request.query_exp_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCall',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_call_with_options_async(
        self,
        request: main_models.DescribeCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not DaraCore.is_null(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not DaraCore.is_null(request.ext_data_type):
            query['ExtDataType'] = request.ext_data_type
        if not DaraCore.is_null(request.query_exp_info):
            query['QueryExpInfo'] = request.query_exp_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCall',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_call(
        self,
        request: main_models.DescribeCallRequest,
    ) -> main_models.DescribeCallResponse:
        runtime = RuntimeOptions()
        return self.describe_call_with_options(request, runtime)

    async def describe_call_async(
        self,
        request: main_models.DescribeCallRequest,
    ) -> main_models.DescribeCallResponse:
        runtime = RuntimeOptions()
        return await self.describe_call_with_options_async(request, runtime)

    def describe_call_list_with_options(
        self,
        request: main_models.DescribeCallListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCallListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.call_status):
            query['CallStatus'] = request.call_status
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.end_ts):
            query['EndTs'] = request.end_ts
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_mode):
            query['QueryMode'] = request.query_mode
        if not DaraCore.is_null(request.start_ts):
            query['StartTs'] = request.start_ts
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCallList',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCallListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_call_list_with_options_async(
        self,
        request: main_models.DescribeCallListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCallListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.call_status):
            query['CallStatus'] = request.call_status
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.end_ts):
            query['EndTs'] = request.end_ts
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_mode):
            query['QueryMode'] = request.query_mode
        if not DaraCore.is_null(request.start_ts):
            query['StartTs'] = request.start_ts
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCallList',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCallListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_call_list(
        self,
        request: main_models.DescribeCallListRequest,
    ) -> main_models.DescribeCallListResponse:
        runtime = RuntimeOptions()
        return self.describe_call_list_with_options(request, runtime)

    async def describe_call_list_async(
        self,
        request: main_models.DescribeCallListRequest,
    ) -> main_models.DescribeCallListResponse:
        runtime = RuntimeOptions()
        return await self.describe_call_list_with_options_async(request, runtime)

    def describe_callbacks_with_options(
        self,
        request: main_models.DescribeCallbacksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCallbacksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCallbacks',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCallbacksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_callbacks_with_options_async(
        self,
        request: main_models.DescribeCallbacksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCallbacksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCallbacks',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCallbacksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_callbacks(
        self,
        request: main_models.DescribeCallbacksRequest,
    ) -> main_models.DescribeCallbacksResponse:
        runtime = RuntimeOptions()
        return self.describe_callbacks_with_options(request, runtime)

    async def describe_callbacks_async(
        self,
        request: main_models.DescribeCallbacksRequest,
    ) -> main_models.DescribeCallbacksResponse:
        runtime = RuntimeOptions()
        return await self.describe_callbacks_with_options_async(request, runtime)

    def describe_channel_with_options(
        self,
        request: main_models.DescribeChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannel',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_with_options_async(
        self,
        request: main_models.DescribeChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannel',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel(
        self,
        request: main_models.DescribeChannelRequest,
    ) -> main_models.DescribeChannelResponse:
        runtime = RuntimeOptions()
        return self.describe_channel_with_options(request, runtime)

    async def describe_channel_async(
        self,
        request: main_models.DescribeChannelRequest,
    ) -> main_models.DescribeChannelResponse:
        runtime = RuntimeOptions()
        return await self.describe_channel_with_options_async(request, runtime)

    def describe_channel_all_users_with_options(
        self,
        request: main_models.DescribeChannelAllUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelAllUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannelAllUsers',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelAllUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_all_users_with_options_async(
        self,
        request: main_models.DescribeChannelAllUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelAllUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannelAllUsers',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelAllUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel_all_users(
        self,
        request: main_models.DescribeChannelAllUsersRequest,
    ) -> main_models.DescribeChannelAllUsersResponse:
        runtime = RuntimeOptions()
        return self.describe_channel_all_users_with_options(request, runtime)

    async def describe_channel_all_users_async(
        self,
        request: main_models.DescribeChannelAllUsersRequest,
    ) -> main_models.DescribeChannelAllUsersResponse:
        runtime = RuntimeOptions()
        return await self.describe_channel_all_users_with_options_async(request, runtime)

    def describe_channel_area_distribution_stat_data_with_options(
        self,
        request: main_models.DescribeChannelAreaDistributionStatDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelAreaDistributionStatDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not DaraCore.is_null(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not DaraCore.is_null(request.parent_area):
            query['ParentArea'] = request.parent_area
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannelAreaDistributionStatData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelAreaDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_area_distribution_stat_data_with_options_async(
        self,
        request: main_models.DescribeChannelAreaDistributionStatDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelAreaDistributionStatDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not DaraCore.is_null(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not DaraCore.is_null(request.parent_area):
            query['ParentArea'] = request.parent_area
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannelAreaDistributionStatData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelAreaDistributionStatDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel_area_distribution_stat_data(
        self,
        request: main_models.DescribeChannelAreaDistributionStatDataRequest,
    ) -> main_models.DescribeChannelAreaDistributionStatDataResponse:
        runtime = RuntimeOptions()
        return self.describe_channel_area_distribution_stat_data_with_options(request, runtime)

    async def describe_channel_area_distribution_stat_data_async(
        self,
        request: main_models.DescribeChannelAreaDistributionStatDataRequest,
    ) -> main_models.DescribeChannelAreaDistributionStatDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_channel_area_distribution_stat_data_with_options_async(request, runtime)

    def describe_channel_distribution_stat_data_with_options(
        self,
        request: main_models.DescribeChannelDistributionStatDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelDistributionStatDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not DaraCore.is_null(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not DaraCore.is_null(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannelDistributionStatData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_distribution_stat_data_with_options_async(
        self,
        request: main_models.DescribeChannelDistributionStatDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelDistributionStatDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not DaraCore.is_null(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not DaraCore.is_null(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannelDistributionStatData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelDistributionStatDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel_distribution_stat_data(
        self,
        request: main_models.DescribeChannelDistributionStatDataRequest,
    ) -> main_models.DescribeChannelDistributionStatDataResponse:
        runtime = RuntimeOptions()
        return self.describe_channel_distribution_stat_data_with_options(request, runtime)

    async def describe_channel_distribution_stat_data_async(
        self,
        request: main_models.DescribeChannelDistributionStatDataRequest,
    ) -> main_models.DescribeChannelDistributionStatDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_channel_distribution_stat_data_with_options_async(request, runtime)

    def describe_channel_overall_data_with_options(
        self,
        request: main_models.DescribeChannelOverallDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelOverallDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not DaraCore.is_null(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannelOverallData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelOverallDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_overall_data_with_options_async(
        self,
        request: main_models.DescribeChannelOverallDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelOverallDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not DaraCore.is_null(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannelOverallData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelOverallDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel_overall_data(
        self,
        request: main_models.DescribeChannelOverallDataRequest,
    ) -> main_models.DescribeChannelOverallDataResponse:
        runtime = RuntimeOptions()
        return self.describe_channel_overall_data_with_options(request, runtime)

    async def describe_channel_overall_data_async(
        self,
        request: main_models.DescribeChannelOverallDataRequest,
    ) -> main_models.DescribeChannelOverallDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_channel_overall_data_with_options_async(request, runtime)

    def describe_channel_participants_with_options(
        self,
        request: main_models.DescribeChannelParticipantsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelParticipantsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannelParticipants',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelParticipantsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_participants_with_options_async(
        self,
        request: main_models.DescribeChannelParticipantsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelParticipantsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannelParticipants',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelParticipantsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel_participants(
        self,
        request: main_models.DescribeChannelParticipantsRequest,
    ) -> main_models.DescribeChannelParticipantsResponse:
        runtime = RuntimeOptions()
        return self.describe_channel_participants_with_options(request, runtime)

    async def describe_channel_participants_async(
        self,
        request: main_models.DescribeChannelParticipantsRequest,
    ) -> main_models.DescribeChannelParticipantsResponse:
        runtime = RuntimeOptions()
        return await self.describe_channel_participants_with_options_async(request, runtime)

    def describe_channel_top_pub_user_list_with_options(
        self,
        request: main_models.DescribeChannelTopPubUserListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelTopPubUserListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not DaraCore.is_null(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannelTopPubUserList',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelTopPubUserListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_top_pub_user_list_with_options_async(
        self,
        request: main_models.DescribeChannelTopPubUserListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelTopPubUserListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not DaraCore.is_null(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannelTopPubUserList',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelTopPubUserListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel_top_pub_user_list(
        self,
        request: main_models.DescribeChannelTopPubUserListRequest,
    ) -> main_models.DescribeChannelTopPubUserListResponse:
        runtime = RuntimeOptions()
        return self.describe_channel_top_pub_user_list_with_options(request, runtime)

    async def describe_channel_top_pub_user_list_async(
        self,
        request: main_models.DescribeChannelTopPubUserListRequest,
    ) -> main_models.DescribeChannelTopPubUserListResponse:
        runtime = RuntimeOptions()
        return await self.describe_channel_top_pub_user_list_with_options_async(request, runtime)

    def describe_channel_user_with_options(
        self,
        request: main_models.DescribeChannelUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannelUser',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_user_with_options_async(
        self,
        request: main_models.DescribeChannelUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannelUser',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel_user(
        self,
        request: main_models.DescribeChannelUserRequest,
    ) -> main_models.DescribeChannelUserResponse:
        runtime = RuntimeOptions()
        return self.describe_channel_user_with_options(request, runtime)

    async def describe_channel_user_async(
        self,
        request: main_models.DescribeChannelUserRequest,
    ) -> main_models.DescribeChannelUserResponse:
        runtime = RuntimeOptions()
        return await self.describe_channel_user_with_options_async(request, runtime)

    def describe_channel_user_metrics_with_options(
        self,
        request: main_models.DescribeChannelUserMetricsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelUserMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not DaraCore.is_null(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannelUserMetrics',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelUserMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_user_metrics_with_options_async(
        self,
        request: main_models.DescribeChannelUserMetricsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelUserMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not DaraCore.is_null(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannelUserMetrics',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelUserMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel_user_metrics(
        self,
        request: main_models.DescribeChannelUserMetricsRequest,
    ) -> main_models.DescribeChannelUserMetricsResponse:
        runtime = RuntimeOptions()
        return self.describe_channel_user_metrics_with_options(request, runtime)

    async def describe_channel_user_metrics_async(
        self,
        request: main_models.DescribeChannelUserMetricsRequest,
    ) -> main_models.DescribeChannelUserMetricsResponse:
        runtime = RuntimeOptions()
        return await self.describe_channel_user_metrics_with_options_async(request, runtime)

    def describe_channel_users_with_options(
        self,
        request: main_models.DescribeChannelUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannelUsers',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_users_with_options_async(
        self,
        request: main_models.DescribeChannelUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannelUsers',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel_users(
        self,
        request: main_models.DescribeChannelUsersRequest,
    ) -> main_models.DescribeChannelUsersResponse:
        runtime = RuntimeOptions()
        return self.describe_channel_users_with_options(request, runtime)

    async def describe_channel_users_async(
        self,
        request: main_models.DescribeChannelUsersRequest,
    ) -> main_models.DescribeChannelUsersResponse:
        runtime = RuntimeOptions()
        return await self.describe_channel_users_with_options_async(request, runtime)

    def describe_channels_with_options(
        self,
        request: main_models.DescribeChannelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannels',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channels_with_options_async(
        self,
        request: main_models.DescribeChannelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChannelsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChannels',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChannelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channels(
        self,
        request: main_models.DescribeChannelsRequest,
    ) -> main_models.DescribeChannelsResponse:
        runtime = RuntimeOptions()
        return self.describe_channels_with_options(request, runtime)

    async def describe_channels_async(
        self,
        request: main_models.DescribeChannelsRequest,
    ) -> main_models.DescribeChannelsResponse:
        runtime = RuntimeOptions()
        return await self.describe_channels_with_options_async(request, runtime)

    def describe_cloud_note_phrases_with_options(
        self,
        tmp_req: main_models.DescribeCloudNotePhrasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudNotePhrasesResponse:
        tmp_req.validate()
        request = main_models.DescribeCloudNotePhrasesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.condition):
            request.condition_shrink = Utils.array_to_string_with_specified_style(tmp_req.condition, 'Condition', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.condition_shrink):
            query['Condition'] = request.condition_shrink
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudNotePhrases',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudNotePhrasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_note_phrases_with_options_async(
        self,
        tmp_req: main_models.DescribeCloudNotePhrasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudNotePhrasesResponse:
        tmp_req.validate()
        request = main_models.DescribeCloudNotePhrasesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.condition):
            request.condition_shrink = Utils.array_to_string_with_specified_style(tmp_req.condition, 'Condition', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.condition_shrink):
            query['Condition'] = request.condition_shrink
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudNotePhrases',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudNotePhrasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_note_phrases(
        self,
        request: main_models.DescribeCloudNotePhrasesRequest,
    ) -> main_models.DescribeCloudNotePhrasesResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_note_phrases_with_options(request, runtime)

    async def describe_cloud_note_phrases_async(
        self,
        request: main_models.DescribeCloudNotePhrasesRequest,
    ) -> main_models.DescribeCloudNotePhrasesResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_note_phrases_with_options_async(request, runtime)

    def describe_cloud_notes_with_options(
        self,
        tmp_req: main_models.DescribeCloudNotesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudNotesResponse:
        tmp_req.validate()
        request = main_models.DescribeCloudNotesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_ids):
            request.task_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudNotes',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudNotesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_notes_with_options_async(
        self,
        tmp_req: main_models.DescribeCloudNotesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudNotesResponse:
        tmp_req.validate()
        request = main_models.DescribeCloudNotesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_ids):
            request.task_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudNotes',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudNotesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_notes(
        self,
        request: main_models.DescribeCloudNotesRequest,
    ) -> main_models.DescribeCloudNotesResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_notes_with_options(request, runtime)

    async def describe_cloud_notes_async(
        self,
        request: main_models.DescribeCloudNotesRequest,
    ) -> main_models.DescribeCloudNotesResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_notes_with_options_async(request, runtime)

    def describe_cloud_record_status_with_options(
        self,
        request: main_models.DescribeCloudRecordStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudRecordStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudRecordStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudRecordStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_record_status_with_options_async(
        self,
        request: main_models.DescribeCloudRecordStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudRecordStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudRecordStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudRecordStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_record_status(
        self,
        request: main_models.DescribeCloudRecordStatusRequest,
    ) -> main_models.DescribeCloudRecordStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_record_status_with_options(request, runtime)

    async def describe_cloud_record_status_async(
        self,
        request: main_models.DescribeCloudRecordStatusRequest,
    ) -> main_models.DescribeCloudRecordStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_record_status_with_options_async(request, runtime)

    def describe_end_point_event_list_with_options(
        self,
        request: main_models.DescribeEndPointEventListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEndPointEventListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not DaraCore.is_null(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not DaraCore.is_null(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEndPointEventList',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEndPointEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_end_point_event_list_with_options_async(
        self,
        request: main_models.DescribeEndPointEventListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEndPointEventListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not DaraCore.is_null(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not DaraCore.is_null(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEndPointEventList',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEndPointEventListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_end_point_event_list(
        self,
        request: main_models.DescribeEndPointEventListRequest,
    ) -> main_models.DescribeEndPointEventListResponse:
        runtime = RuntimeOptions()
        return self.describe_end_point_event_list_with_options(request, runtime)

    async def describe_end_point_event_list_async(
        self,
        request: main_models.DescribeEndPointEventListRequest,
    ) -> main_models.DescribeEndPointEventListResponse:
        runtime = RuntimeOptions()
        return await self.describe_end_point_event_list_with_options_async(request, runtime)

    def describe_end_point_metric_data_with_options(
        self,
        request: main_models.DescribeEndPointMetricDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEndPointMetricDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not DaraCore.is_null(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not DaraCore.is_null(request.metrics):
            query['Metrics'] = request.metrics
        if not DaraCore.is_null(request.pub_call_id_list):
            query['PubCallIdList'] = request.pub_call_id_list
        if not DaraCore.is_null(request.pub_user_id):
            query['PubUserId'] = request.pub_user_id
        if not DaraCore.is_null(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEndPointMetricData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEndPointMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_end_point_metric_data_with_options_async(
        self,
        request: main_models.DescribeEndPointMetricDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEndPointMetricDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not DaraCore.is_null(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not DaraCore.is_null(request.metrics):
            query['Metrics'] = request.metrics
        if not DaraCore.is_null(request.pub_call_id_list):
            query['PubCallIdList'] = request.pub_call_id_list
        if not DaraCore.is_null(request.pub_user_id):
            query['PubUserId'] = request.pub_user_id
        if not DaraCore.is_null(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEndPointMetricData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEndPointMetricDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_end_point_metric_data(
        self,
        request: main_models.DescribeEndPointMetricDataRequest,
    ) -> main_models.DescribeEndPointMetricDataResponse:
        runtime = RuntimeOptions()
        return self.describe_end_point_metric_data_with_options(request, runtime)

    async def describe_end_point_metric_data_async(
        self,
        request: main_models.DescribeEndPointMetricDataRequest,
    ) -> main_models.DescribeEndPointMetricDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_end_point_metric_data_with_options_async(request, runtime)

    def describe_fault_diagnosis_factor_distribution_stat_with_options(
        self,
        request: main_models.DescribeFaultDiagnosisFactorDistributionStatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFaultDiagnosisFactorDistributionStatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_ts):
            query['EndTs'] = request.end_ts
        if not DaraCore.is_null(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFaultDiagnosisFactorDistributionStat',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFaultDiagnosisFactorDistributionStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fault_diagnosis_factor_distribution_stat_with_options_async(
        self,
        request: main_models.DescribeFaultDiagnosisFactorDistributionStatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFaultDiagnosisFactorDistributionStatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_ts):
            query['EndTs'] = request.end_ts
        if not DaraCore.is_null(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFaultDiagnosisFactorDistributionStat',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFaultDiagnosisFactorDistributionStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fault_diagnosis_factor_distribution_stat(
        self,
        request: main_models.DescribeFaultDiagnosisFactorDistributionStatRequest,
    ) -> main_models.DescribeFaultDiagnosisFactorDistributionStatResponse:
        runtime = RuntimeOptions()
        return self.describe_fault_diagnosis_factor_distribution_stat_with_options(request, runtime)

    async def describe_fault_diagnosis_factor_distribution_stat_async(
        self,
        request: main_models.DescribeFaultDiagnosisFactorDistributionStatRequest,
    ) -> main_models.DescribeFaultDiagnosisFactorDistributionStatResponse:
        runtime = RuntimeOptions()
        return await self.describe_fault_diagnosis_factor_distribution_stat_with_options_async(request, runtime)

    def describe_fault_diagnosis_overall_data_with_options(
        self,
        request: main_models.DescribeFaultDiagnosisOverallDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFaultDiagnosisOverallDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_ts):
            query['EndTs'] = request.end_ts
        if not DaraCore.is_null(request.start_ts):
            query['StartTs'] = request.start_ts
        if not DaraCore.is_null(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFaultDiagnosisOverallData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFaultDiagnosisOverallDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fault_diagnosis_overall_data_with_options_async(
        self,
        request: main_models.DescribeFaultDiagnosisOverallDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFaultDiagnosisOverallDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_ts):
            query['EndTs'] = request.end_ts
        if not DaraCore.is_null(request.start_ts):
            query['StartTs'] = request.start_ts
        if not DaraCore.is_null(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFaultDiagnosisOverallData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFaultDiagnosisOverallDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fault_diagnosis_overall_data(
        self,
        request: main_models.DescribeFaultDiagnosisOverallDataRequest,
    ) -> main_models.DescribeFaultDiagnosisOverallDataResponse:
        runtime = RuntimeOptions()
        return self.describe_fault_diagnosis_overall_data_with_options(request, runtime)

    async def describe_fault_diagnosis_overall_data_async(
        self,
        request: main_models.DescribeFaultDiagnosisOverallDataRequest,
    ) -> main_models.DescribeFaultDiagnosisOverallDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_fault_diagnosis_overall_data_with_options_async(request, runtime)

    def describe_fault_diagnosis_user_detail_with_options(
        self,
        request: main_models.DescribeFaultDiagnosisUserDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFaultDiagnosisUserDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not DaraCore.is_null(request.fault_type):
            query['FaultType'] = request.fault_type
        if not DaraCore.is_null(request.query_call_user_info):
            query['QueryCallUserInfo'] = request.query_call_user_info
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFaultDiagnosisUserDetail',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFaultDiagnosisUserDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fault_diagnosis_user_detail_with_options_async(
        self,
        request: main_models.DescribeFaultDiagnosisUserDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFaultDiagnosisUserDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not DaraCore.is_null(request.fault_type):
            query['FaultType'] = request.fault_type
        if not DaraCore.is_null(request.query_call_user_info):
            query['QueryCallUserInfo'] = request.query_call_user_info
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFaultDiagnosisUserDetail',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFaultDiagnosisUserDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fault_diagnosis_user_detail(
        self,
        request: main_models.DescribeFaultDiagnosisUserDetailRequest,
    ) -> main_models.DescribeFaultDiagnosisUserDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_fault_diagnosis_user_detail_with_options(request, runtime)

    async def describe_fault_diagnosis_user_detail_async(
        self,
        request: main_models.DescribeFaultDiagnosisUserDetailRequest,
    ) -> main_models.DescribeFaultDiagnosisUserDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_fault_diagnosis_user_detail_with_options_async(request, runtime)

    def describe_fault_diagnosis_user_list_with_options(
        self,
        request: main_models.DescribeFaultDiagnosisUserListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFaultDiagnosisUserListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.end_ts):
            query['EndTs'] = request.end_ts
        if not DaraCore.is_null(request.fault_types):
            query['FaultTypes'] = request.fault_types
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_ts):
            query['StartTs'] = request.start_ts
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFaultDiagnosisUserList',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFaultDiagnosisUserListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fault_diagnosis_user_list_with_options_async(
        self,
        request: main_models.DescribeFaultDiagnosisUserListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFaultDiagnosisUserListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.end_ts):
            query['EndTs'] = request.end_ts
        if not DaraCore.is_null(request.fault_types):
            query['FaultTypes'] = request.fault_types
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_ts):
            query['StartTs'] = request.start_ts
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFaultDiagnosisUserList',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFaultDiagnosisUserListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fault_diagnosis_user_list(
        self,
        request: main_models.DescribeFaultDiagnosisUserListRequest,
    ) -> main_models.DescribeFaultDiagnosisUserListResponse:
        runtime = RuntimeOptions()
        return self.describe_fault_diagnosis_user_list_with_options(request, runtime)

    async def describe_fault_diagnosis_user_list_async(
        self,
        request: main_models.DescribeFaultDiagnosisUserListRequest,
    ) -> main_models.DescribeFaultDiagnosisUserListResponse:
        runtime = RuntimeOptions()
        return await self.describe_fault_diagnosis_user_list_with_options_async(request, runtime)

    def describe_mpulayout_info_list_with_options(
        self,
        request: main_models.DescribeMPULayoutInfoListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMPULayoutInfoListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMPULayoutInfoList',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMPULayoutInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mpulayout_info_list_with_options_async(
        self,
        request: main_models.DescribeMPULayoutInfoListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMPULayoutInfoListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMPULayoutInfoList',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMPULayoutInfoListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mpulayout_info_list(
        self,
        request: main_models.DescribeMPULayoutInfoListRequest,
    ) -> main_models.DescribeMPULayoutInfoListResponse:
        runtime = RuntimeOptions()
        return self.describe_mpulayout_info_list_with_options(request, runtime)

    async def describe_mpulayout_info_list_async(
        self,
        request: main_models.DescribeMPULayoutInfoListRequest,
    ) -> main_models.DescribeMPULayoutInfoListResponse:
        runtime = RuntimeOptions()
        return await self.describe_mpulayout_info_list_with_options_async(request, runtime)

    def describe_pub_user_list_by_sub_user_with_options(
        self,
        request: main_models.DescribePubUserListBySubUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePubUserListBySubUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not DaraCore.is_null(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not DaraCore.is_null(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePubUserListBySubUser',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePubUserListBySubUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pub_user_list_by_sub_user_with_options_async(
        self,
        request: main_models.DescribePubUserListBySubUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePubUserListBySubUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not DaraCore.is_null(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not DaraCore.is_null(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePubUserListBySubUser',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePubUserListBySubUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pub_user_list_by_sub_user(
        self,
        request: main_models.DescribePubUserListBySubUserRequest,
    ) -> main_models.DescribePubUserListBySubUserResponse:
        runtime = RuntimeOptions()
        return self.describe_pub_user_list_by_sub_user_with_options(request, runtime)

    async def describe_pub_user_list_by_sub_user_async(
        self,
        request: main_models.DescribePubUserListBySubUserRequest,
    ) -> main_models.DescribePubUserListBySubUserResponse:
        runtime = RuntimeOptions()
        return await self.describe_pub_user_list_by_sub_user_with_options_async(request, runtime)

    def describe_qoe_metric_data_with_options(
        self,
        request: main_models.DescribeQoeMetricDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQoeMetricDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not DaraCore.is_null(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQoeMetricData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQoeMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_qoe_metric_data_with_options_async(
        self,
        request: main_models.DescribeQoeMetricDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQoeMetricDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not DaraCore.is_null(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQoeMetricData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQoeMetricDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_qoe_metric_data(
        self,
        request: main_models.DescribeQoeMetricDataRequest,
    ) -> main_models.DescribeQoeMetricDataResponse:
        runtime = RuntimeOptions()
        return self.describe_qoe_metric_data_with_options(request, runtime)

    async def describe_qoe_metric_data_async(
        self,
        request: main_models.DescribeQoeMetricDataRequest,
    ) -> main_models.DescribeQoeMetricDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_qoe_metric_data_with_options_async(request, runtime)

    def describe_quality_area_distribution_stat_data_with_options(
        self,
        request: main_models.DescribeQualityAreaDistributionStatDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQualityAreaDistributionStatDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.parent_area):
            query['ParentArea'] = request.parent_area
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQualityAreaDistributionStatData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQualityAreaDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_quality_area_distribution_stat_data_with_options_async(
        self,
        request: main_models.DescribeQualityAreaDistributionStatDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQualityAreaDistributionStatDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.parent_area):
            query['ParentArea'] = request.parent_area
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQualityAreaDistributionStatData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQualityAreaDistributionStatDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_quality_area_distribution_stat_data(
        self,
        request: main_models.DescribeQualityAreaDistributionStatDataRequest,
    ) -> main_models.DescribeQualityAreaDistributionStatDataResponse:
        runtime = RuntimeOptions()
        return self.describe_quality_area_distribution_stat_data_with_options(request, runtime)

    async def describe_quality_area_distribution_stat_data_async(
        self,
        request: main_models.DescribeQualityAreaDistributionStatDataRequest,
    ) -> main_models.DescribeQualityAreaDistributionStatDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_quality_area_distribution_stat_data_with_options_async(request, runtime)

    def describe_quality_distribution_stat_data_with_options(
        self,
        request: main_models.DescribeQualityDistributionStatDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQualityDistributionStatDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQualityDistributionStatData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQualityDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_quality_distribution_stat_data_with_options_async(
        self,
        request: main_models.DescribeQualityDistributionStatDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQualityDistributionStatDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQualityDistributionStatData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQualityDistributionStatDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_quality_distribution_stat_data(
        self,
        request: main_models.DescribeQualityDistributionStatDataRequest,
    ) -> main_models.DescribeQualityDistributionStatDataResponse:
        runtime = RuntimeOptions()
        return self.describe_quality_distribution_stat_data_with_options(request, runtime)

    async def describe_quality_distribution_stat_data_async(
        self,
        request: main_models.DescribeQualityDistributionStatDataRequest,
    ) -> main_models.DescribeQualityDistributionStatDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_quality_distribution_stat_data_with_options_async(request, runtime)

    def describe_quality_os_sdk_version_distribution_stat_data_with_options(
        self,
        request: main_models.DescribeQualityOsSdkVersionDistributionStatDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQualityOsSdkVersionDistributionStatDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQualityOsSdkVersionDistributionStatData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQualityOsSdkVersionDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_quality_os_sdk_version_distribution_stat_data_with_options_async(
        self,
        request: main_models.DescribeQualityOsSdkVersionDistributionStatDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQualityOsSdkVersionDistributionStatDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQualityOsSdkVersionDistributionStatData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQualityOsSdkVersionDistributionStatDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_quality_os_sdk_version_distribution_stat_data(
        self,
        request: main_models.DescribeQualityOsSdkVersionDistributionStatDataRequest,
    ) -> main_models.DescribeQualityOsSdkVersionDistributionStatDataResponse:
        runtime = RuntimeOptions()
        return self.describe_quality_os_sdk_version_distribution_stat_data_with_options(request, runtime)

    async def describe_quality_os_sdk_version_distribution_stat_data_async(
        self,
        request: main_models.DescribeQualityOsSdkVersionDistributionStatDataRequest,
    ) -> main_models.DescribeQualityOsSdkVersionDistributionStatDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_quality_os_sdk_version_distribution_stat_data_with_options_async(request, runtime)

    def describe_quality_overall_data_with_options(
        self,
        request: main_models.DescribeQualityOverallDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQualityOverallDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.types):
            query['Types'] = request.types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQualityOverallData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQualityOverallDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_quality_overall_data_with_options_async(
        self,
        request: main_models.DescribeQualityOverallDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQualityOverallDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.types):
            query['Types'] = request.types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQualityOverallData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQualityOverallDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_quality_overall_data(
        self,
        request: main_models.DescribeQualityOverallDataRequest,
    ) -> main_models.DescribeQualityOverallDataResponse:
        runtime = RuntimeOptions()
        return self.describe_quality_overall_data_with_options(request, runtime)

    async def describe_quality_overall_data_async(
        self,
        request: main_models.DescribeQualityOverallDataRequest,
    ) -> main_models.DescribeQualityOverallDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_quality_overall_data_with_options_async(request, runtime)

    def describe_record_files_with_options(
        self,
        request: main_models.DescribeRecordFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecordFilesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecordFiles',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecordFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_record_files_with_options_async(
        self,
        request: main_models.DescribeRecordFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecordFilesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecordFiles',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecordFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_record_files(
        self,
        request: main_models.DescribeRecordFilesRequest,
    ) -> main_models.DescribeRecordFilesResponse:
        runtime = RuntimeOptions()
        return self.describe_record_files_with_options(request, runtime)

    async def describe_record_files_async(
        self,
        request: main_models.DescribeRecordFilesRequest,
    ) -> main_models.DescribeRecordFilesResponse:
        runtime = RuntimeOptions()
        return await self.describe_record_files_with_options_async(request, runtime)

    def describe_record_templates_with_options(
        self,
        request: main_models.DescribeRecordTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecordTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.template_ids):
            query['TemplateIds'] = request.template_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecordTemplates',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecordTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_record_templates_with_options_async(
        self,
        request: main_models.DescribeRecordTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecordTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.template_ids):
            query['TemplateIds'] = request.template_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecordTemplates',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecordTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_record_templates(
        self,
        request: main_models.DescribeRecordTemplatesRequest,
    ) -> main_models.DescribeRecordTemplatesResponse:
        runtime = RuntimeOptions()
        return self.describe_record_templates_with_options(request, runtime)

    async def describe_record_templates_async(
        self,
        request: main_models.DescribeRecordTemplatesRequest,
    ) -> main_models.DescribeRecordTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.describe_record_templates_with_options_async(request, runtime)

    def describe_rtc_channel_list_with_options(
        self,
        request: main_models.DescribeRtcChannelListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRtcChannelListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.service_area):
            query['ServiceArea'] = request.service_area
        if not DaraCore.is_null(request.sort_type):
            query['SortType'] = request.sort_type
        if not DaraCore.is_null(request.time_point):
            query['TimePoint'] = request.time_point
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRtcChannelList',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRtcChannelListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rtc_channel_list_with_options_async(
        self,
        request: main_models.DescribeRtcChannelListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRtcChannelListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.service_area):
            query['ServiceArea'] = request.service_area
        if not DaraCore.is_null(request.sort_type):
            query['SortType'] = request.sort_type
        if not DaraCore.is_null(request.time_point):
            query['TimePoint'] = request.time_point
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRtcChannelList',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRtcChannelListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rtc_channel_list(
        self,
        request: main_models.DescribeRtcChannelListRequest,
    ) -> main_models.DescribeRtcChannelListResponse:
        runtime = RuntimeOptions()
        return self.describe_rtc_channel_list_with_options(request, runtime)

    async def describe_rtc_channel_list_async(
        self,
        request: main_models.DescribeRtcChannelListRequest,
    ) -> main_models.DescribeRtcChannelListResponse:
        runtime = RuntimeOptions()
        return await self.describe_rtc_channel_list_with_options_async(request, runtime)

    def describe_rtc_channel_metric_with_options(
        self,
        request: main_models.DescribeRtcChannelMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRtcChannelMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRtcChannelMetric',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRtcChannelMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rtc_channel_metric_with_options_async(
        self,
        request: main_models.DescribeRtcChannelMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRtcChannelMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRtcChannelMetric',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRtcChannelMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rtc_channel_metric(
        self,
        request: main_models.DescribeRtcChannelMetricRequest,
    ) -> main_models.DescribeRtcChannelMetricResponse:
        runtime = RuntimeOptions()
        return self.describe_rtc_channel_metric_with_options(request, runtime)

    async def describe_rtc_channel_metric_async(
        self,
        request: main_models.DescribeRtcChannelMetricRequest,
    ) -> main_models.DescribeRtcChannelMetricResponse:
        runtime = RuntimeOptions()
        return await self.describe_rtc_channel_metric_with_options_async(request, runtime)

    def describe_rtc_duration_data_with_options(
        self,
        request: main_models.DescribeRtcDurationDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRtcDurationDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.service_area):
            query['ServiceArea'] = request.service_area
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRtcDurationData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRtcDurationDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rtc_duration_data_with_options_async(
        self,
        request: main_models.DescribeRtcDurationDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRtcDurationDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.service_area):
            query['ServiceArea'] = request.service_area
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRtcDurationData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRtcDurationDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rtc_duration_data(
        self,
        request: main_models.DescribeRtcDurationDataRequest,
    ) -> main_models.DescribeRtcDurationDataResponse:
        runtime = RuntimeOptions()
        return self.describe_rtc_duration_data_with_options(request, runtime)

    async def describe_rtc_duration_data_async(
        self,
        request: main_models.DescribeRtcDurationDataRequest,
    ) -> main_models.DescribeRtcDurationDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_rtc_duration_data_with_options_async(request, runtime)

    def describe_rtc_peak_channel_cnt_data_with_options(
        self,
        request: main_models.DescribeRtcPeakChannelCntDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRtcPeakChannelCntDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.service_area):
            query['ServiceArea'] = request.service_area
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRtcPeakChannelCntData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRtcPeakChannelCntDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rtc_peak_channel_cnt_data_with_options_async(
        self,
        request: main_models.DescribeRtcPeakChannelCntDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRtcPeakChannelCntDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.service_area):
            query['ServiceArea'] = request.service_area
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRtcPeakChannelCntData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRtcPeakChannelCntDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rtc_peak_channel_cnt_data(
        self,
        request: main_models.DescribeRtcPeakChannelCntDataRequest,
    ) -> main_models.DescribeRtcPeakChannelCntDataResponse:
        runtime = RuntimeOptions()
        return self.describe_rtc_peak_channel_cnt_data_with_options(request, runtime)

    async def describe_rtc_peak_channel_cnt_data_async(
        self,
        request: main_models.DescribeRtcPeakChannelCntDataRequest,
    ) -> main_models.DescribeRtcPeakChannelCntDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_rtc_peak_channel_cnt_data_with_options_async(request, runtime)

    def describe_rtc_user_cnt_data_with_options(
        self,
        request: main_models.DescribeRtcUserCntDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRtcUserCntDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.service_area):
            query['ServiceArea'] = request.service_area
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRtcUserCntData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRtcUserCntDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rtc_user_cnt_data_with_options_async(
        self,
        request: main_models.DescribeRtcUserCntDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRtcUserCntDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.service_area):
            query['ServiceArea'] = request.service_area
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRtcUserCntData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRtcUserCntDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rtc_user_cnt_data(
        self,
        request: main_models.DescribeRtcUserCntDataRequest,
    ) -> main_models.DescribeRtcUserCntDataResponse:
        runtime = RuntimeOptions()
        return self.describe_rtc_user_cnt_data_with_options(request, runtime)

    async def describe_rtc_user_cnt_data_async(
        self,
        request: main_models.DescribeRtcUserCntDataRequest,
    ) -> main_models.DescribeRtcUserCntDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_rtc_user_cnt_data_with_options_async(request, runtime)

    def describe_streaming_out_status_with_options(
        self,
        request: main_models.DescribeStreamingOutStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStreamingOutStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStreamingOutStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStreamingOutStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_streaming_out_status_with_options_async(
        self,
        request: main_models.DescribeStreamingOutStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStreamingOutStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStreamingOutStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStreamingOutStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_streaming_out_status(
        self,
        request: main_models.DescribeStreamingOutStatusRequest,
    ) -> main_models.DescribeStreamingOutStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_streaming_out_status_with_options(request, runtime)

    async def describe_streaming_out_status_async(
        self,
        request: main_models.DescribeStreamingOutStatusRequest,
    ) -> main_models.DescribeStreamingOutStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_streaming_out_status_with_options_async(request, runtime)

    def describe_system_layout_list_with_options(
        self,
        request: main_models.DescribeSystemLayoutListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSystemLayoutListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSystemLayoutList',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSystemLayoutListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_system_layout_list_with_options_async(
        self,
        request: main_models.DescribeSystemLayoutListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSystemLayoutListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSystemLayoutList',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSystemLayoutListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_system_layout_list(
        self,
        request: main_models.DescribeSystemLayoutListRequest,
    ) -> main_models.DescribeSystemLayoutListResponse:
        runtime = RuntimeOptions()
        return self.describe_system_layout_list_with_options(request, runtime)

    async def describe_system_layout_list_async(
        self,
        request: main_models.DescribeSystemLayoutListRequest,
    ) -> main_models.DescribeSystemLayoutListResponse:
        runtime = RuntimeOptions()
        return await self.describe_system_layout_list_with_options_async(request, runtime)

    def describe_usage_area_distribution_stat_data_with_options(
        self,
        request: main_models.DescribeUsageAreaDistributionStatDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUsageAreaDistributionStatDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.parent_area):
            query['ParentArea'] = request.parent_area
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUsageAreaDistributionStatData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUsageAreaDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_usage_area_distribution_stat_data_with_options_async(
        self,
        request: main_models.DescribeUsageAreaDistributionStatDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUsageAreaDistributionStatDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.parent_area):
            query['ParentArea'] = request.parent_area
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUsageAreaDistributionStatData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUsageAreaDistributionStatDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_usage_area_distribution_stat_data(
        self,
        request: main_models.DescribeUsageAreaDistributionStatDataRequest,
    ) -> main_models.DescribeUsageAreaDistributionStatDataResponse:
        runtime = RuntimeOptions()
        return self.describe_usage_area_distribution_stat_data_with_options(request, runtime)

    async def describe_usage_area_distribution_stat_data_async(
        self,
        request: main_models.DescribeUsageAreaDistributionStatDataRequest,
    ) -> main_models.DescribeUsageAreaDistributionStatDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_usage_area_distribution_stat_data_with_options_async(request, runtime)

    def describe_usage_distribution_stat_data_with_options(
        self,
        request: main_models.DescribeUsageDistributionStatDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUsageDistributionStatDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUsageDistributionStatData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUsageDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_usage_distribution_stat_data_with_options_async(
        self,
        request: main_models.DescribeUsageDistributionStatDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUsageDistributionStatDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUsageDistributionStatData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUsageDistributionStatDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_usage_distribution_stat_data(
        self,
        request: main_models.DescribeUsageDistributionStatDataRequest,
    ) -> main_models.DescribeUsageDistributionStatDataResponse:
        runtime = RuntimeOptions()
        return self.describe_usage_distribution_stat_data_with_options(request, runtime)

    async def describe_usage_distribution_stat_data_async(
        self,
        request: main_models.DescribeUsageDistributionStatDataRequest,
    ) -> main_models.DescribeUsageDistributionStatDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_usage_distribution_stat_data_with_options_async(request, runtime)

    def describe_usage_os_sdk_version_distribution_stat_data_with_options(
        self,
        request: main_models.DescribeUsageOsSdkVersionDistributionStatDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUsageOsSdkVersionDistributionStatDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUsageOsSdkVersionDistributionStatData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUsageOsSdkVersionDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_usage_os_sdk_version_distribution_stat_data_with_options_async(
        self,
        request: main_models.DescribeUsageOsSdkVersionDistributionStatDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUsageOsSdkVersionDistributionStatDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUsageOsSdkVersionDistributionStatData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUsageOsSdkVersionDistributionStatDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_usage_os_sdk_version_distribution_stat_data(
        self,
        request: main_models.DescribeUsageOsSdkVersionDistributionStatDataRequest,
    ) -> main_models.DescribeUsageOsSdkVersionDistributionStatDataResponse:
        runtime = RuntimeOptions()
        return self.describe_usage_os_sdk_version_distribution_stat_data_with_options(request, runtime)

    async def describe_usage_os_sdk_version_distribution_stat_data_async(
        self,
        request: main_models.DescribeUsageOsSdkVersionDistributionStatDataRequest,
    ) -> main_models.DescribeUsageOsSdkVersionDistributionStatDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_usage_os_sdk_version_distribution_stat_data_with_options_async(request, runtime)

    def describe_usage_overall_data_with_options(
        self,
        request: main_models.DescribeUsageOverallDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUsageOverallDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.types):
            query['Types'] = request.types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUsageOverallData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUsageOverallDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_usage_overall_data_with_options_async(
        self,
        request: main_models.DescribeUsageOverallDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUsageOverallDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.types):
            query['Types'] = request.types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUsageOverallData',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUsageOverallDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_usage_overall_data(
        self,
        request: main_models.DescribeUsageOverallDataRequest,
    ) -> main_models.DescribeUsageOverallDataResponse:
        runtime = RuntimeOptions()
        return self.describe_usage_overall_data_with_options(request, runtime)

    async def describe_usage_overall_data_async(
        self,
        request: main_models.DescribeUsageOverallDataRequest,
    ) -> main_models.DescribeUsageOverallDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_usage_overall_data_with_options_async(request, runtime)

    def describe_user_info_in_channel_with_options(
        self,
        request: main_models.DescribeUserInfoInChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserInfoInChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserInfoInChannel',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserInfoInChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_info_in_channel_with_options_async(
        self,
        request: main_models.DescribeUserInfoInChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserInfoInChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserInfoInChannel',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserInfoInChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_info_in_channel(
        self,
        request: main_models.DescribeUserInfoInChannelRequest,
    ) -> main_models.DescribeUserInfoInChannelResponse:
        runtime = RuntimeOptions()
        return self.describe_user_info_in_channel_with_options(request, runtime)

    async def describe_user_info_in_channel_async(
        self,
        request: main_models.DescribeUserInfoInChannelRequest,
    ) -> main_models.DescribeUserInfoInChannelResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_info_in_channel_with_options_async(request, runtime)

    def disable_auto_live_stream_rule_with_options(
        self,
        request: main_models.DisableAutoLiveStreamRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableAutoLiveStreamRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableAutoLiveStreamRule',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_auto_live_stream_rule_with_options_async(
        self,
        request: main_models.DisableAutoLiveStreamRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableAutoLiveStreamRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableAutoLiveStreamRule',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableAutoLiveStreamRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_auto_live_stream_rule(
        self,
        request: main_models.DisableAutoLiveStreamRuleRequest,
    ) -> main_models.DisableAutoLiveStreamRuleResponse:
        runtime = RuntimeOptions()
        return self.disable_auto_live_stream_rule_with_options(request, runtime)

    async def disable_auto_live_stream_rule_async(
        self,
        request: main_models.DisableAutoLiveStreamRuleRequest,
    ) -> main_models.DisableAutoLiveStreamRuleResponse:
        runtime = RuntimeOptions()
        return await self.disable_auto_live_stream_rule_with_options_async(request, runtime)

    def enable_auto_live_stream_rule_with_options(
        self,
        request: main_models.EnableAutoLiveStreamRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableAutoLiveStreamRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableAutoLiveStreamRule',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_auto_live_stream_rule_with_options_async(
        self,
        request: main_models.EnableAutoLiveStreamRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableAutoLiveStreamRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableAutoLiveStreamRule',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableAutoLiveStreamRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_auto_live_stream_rule(
        self,
        request: main_models.EnableAutoLiveStreamRuleRequest,
    ) -> main_models.EnableAutoLiveStreamRuleResponse:
        runtime = RuntimeOptions()
        return self.enable_auto_live_stream_rule_with_options(request, runtime)

    async def enable_auto_live_stream_rule_async(
        self,
        request: main_models.EnableAutoLiveStreamRuleRequest,
    ) -> main_models.EnableAutoLiveStreamRuleResponse:
        runtime = RuntimeOptions()
        return await self.enable_auto_live_stream_rule_with_options_async(request, runtime)

    def get_agent_with_options(
        self,
        request: main_models.GetAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgent',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_with_options_async(
        self,
        request: main_models.GetAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgent',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent(
        self,
        request: main_models.GetAgentRequest,
    ) -> main_models.GetAgentResponse:
        runtime = RuntimeOptions()
        return self.get_agent_with_options(request, runtime)

    async def get_agent_async(
        self,
        request: main_models.GetAgentRequest,
    ) -> main_models.GetAgentResponse:
        runtime = RuntimeOptions()
        return await self.get_agent_with_options_async(request, runtime)

    def get_mputask_status_with_options(
        self,
        request: main_models.GetMPUTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMPUTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMPUTaskStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMPUTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mputask_status_with_options_async(
        self,
        request: main_models.GetMPUTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMPUTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMPUTaskStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMPUTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mputask_status(
        self,
        request: main_models.GetMPUTaskStatusRequest,
    ) -> main_models.GetMPUTaskStatusResponse:
        runtime = RuntimeOptions()
        return self.get_mputask_status_with_options(request, runtime)

    async def get_mputask_status_async(
        self,
        request: main_models.GetMPUTaskStatusRequest,
    ) -> main_models.GetMPUTaskStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_mputask_status_with_options_async(request, runtime)

    def modify_app_with_options(
        self,
        request: main_models.ModifyAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApp',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_with_options_async(
        self,
        request: main_models.ModifyAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApp',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app(
        self,
        request: main_models.ModifyAppRequest,
    ) -> main_models.ModifyAppResponse:
        runtime = RuntimeOptions()
        return self.modify_app_with_options(request, runtime)

    async def modify_app_async(
        self,
        request: main_models.ModifyAppRequest,
    ) -> main_models.ModifyAppResponse:
        runtime = RuntimeOptions()
        return await self.modify_app_with_options_async(request, runtime)

    def modify_app_agent_function_status_with_options(
        self,
        request: main_models.ModifyAppAgentFunctionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppAgentFunctionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppAgentFunctionStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppAgentFunctionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_agent_function_status_with_options_async(
        self,
        request: main_models.ModifyAppAgentFunctionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppAgentFunctionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppAgentFunctionStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppAgentFunctionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_agent_function_status(
        self,
        request: main_models.ModifyAppAgentFunctionStatusRequest,
    ) -> main_models.ModifyAppAgentFunctionStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_app_agent_function_status_with_options(request, runtime)

    async def modify_app_agent_function_status_async(
        self,
        request: main_models.ModifyAppAgentFunctionStatusRequest,
    ) -> main_models.ModifyAppAgentFunctionStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_app_agent_function_status_with_options_async(request, runtime)

    def modify_app_agent_template_with_options(
        self,
        tmp_req: main_models.ModifyAppAgentTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppAgentTemplateResponse:
        tmp_req.validate()
        request = main_models.ModifyAppAgentTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_silence_config):
            request.agent_silence_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_silence_config, 'AgentSilenceConfig', 'json')
        if not DaraCore.is_null(tmp_req.ambient_sound_config):
            request.ambient_sound_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.ambient_sound_config, 'AmbientSoundConfig', 'json')
        if not DaraCore.is_null(tmp_req.asr_config):
            request.asr_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.asr_config, 'AsrConfig', 'json')
        if not DaraCore.is_null(tmp_req.back_channel_config):
            request.back_channel_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.back_channel_config, 'BackChannelConfig', 'json')
        if not DaraCore.is_null(tmp_req.interrupt_config):
            request.interrupt_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.interrupt_config, 'InterruptConfig', 'json')
        if not DaraCore.is_null(tmp_req.llm_config):
            request.llm_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.llm_config, 'LlmConfig', 'json')
        if not DaraCore.is_null(tmp_req.tts_config):
            request.tts_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.tts_config, 'TtsConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_silence_config_shrink):
            query['AgentSilenceConfig'] = request.agent_silence_config_shrink
        if not DaraCore.is_null(request.ambient_sound_config_shrink):
            query['AmbientSoundConfig'] = request.ambient_sound_config_shrink
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.asr_config_shrink):
            query['AsrConfig'] = request.asr_config_shrink
        if not DaraCore.is_null(request.back_channel_config_shrink):
            query['BackChannelConfig'] = request.back_channel_config_shrink
        if not DaraCore.is_null(request.chat_mode):
            query['ChatMode'] = request.chat_mode
        if not DaraCore.is_null(request.greeting):
            query['Greeting'] = request.greeting
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.interrupt_config_shrink):
            query['InterruptConfig'] = request.interrupt_config_shrink
        if not DaraCore.is_null(request.interrupt_mode):
            query['InterruptMode'] = request.interrupt_mode
        if not DaraCore.is_null(request.llm_config_shrink):
            query['LlmConfig'] = request.llm_config_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.tts_config_shrink):
            query['TtsConfig'] = request.tts_config_shrink
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppAgentTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppAgentTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_agent_template_with_options_async(
        self,
        tmp_req: main_models.ModifyAppAgentTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppAgentTemplateResponse:
        tmp_req.validate()
        request = main_models.ModifyAppAgentTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_silence_config):
            request.agent_silence_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_silence_config, 'AgentSilenceConfig', 'json')
        if not DaraCore.is_null(tmp_req.ambient_sound_config):
            request.ambient_sound_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.ambient_sound_config, 'AmbientSoundConfig', 'json')
        if not DaraCore.is_null(tmp_req.asr_config):
            request.asr_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.asr_config, 'AsrConfig', 'json')
        if not DaraCore.is_null(tmp_req.back_channel_config):
            request.back_channel_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.back_channel_config, 'BackChannelConfig', 'json')
        if not DaraCore.is_null(tmp_req.interrupt_config):
            request.interrupt_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.interrupt_config, 'InterruptConfig', 'json')
        if not DaraCore.is_null(tmp_req.llm_config):
            request.llm_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.llm_config, 'LlmConfig', 'json')
        if not DaraCore.is_null(tmp_req.tts_config):
            request.tts_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.tts_config, 'TtsConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_silence_config_shrink):
            query['AgentSilenceConfig'] = request.agent_silence_config_shrink
        if not DaraCore.is_null(request.ambient_sound_config_shrink):
            query['AmbientSoundConfig'] = request.ambient_sound_config_shrink
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.asr_config_shrink):
            query['AsrConfig'] = request.asr_config_shrink
        if not DaraCore.is_null(request.back_channel_config_shrink):
            query['BackChannelConfig'] = request.back_channel_config_shrink
        if not DaraCore.is_null(request.chat_mode):
            query['ChatMode'] = request.chat_mode
        if not DaraCore.is_null(request.greeting):
            query['Greeting'] = request.greeting
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.interrupt_config_shrink):
            query['InterruptConfig'] = request.interrupt_config_shrink
        if not DaraCore.is_null(request.interrupt_mode):
            query['InterruptMode'] = request.interrupt_mode
        if not DaraCore.is_null(request.llm_config_shrink):
            query['LlmConfig'] = request.llm_config_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.tts_config_shrink):
            query['TtsConfig'] = request.tts_config_shrink
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppAgentTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppAgentTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_agent_template(
        self,
        request: main_models.ModifyAppAgentTemplateRequest,
    ) -> main_models.ModifyAppAgentTemplateResponse:
        runtime = RuntimeOptions()
        return self.modify_app_agent_template_with_options(request, runtime)

    async def modify_app_agent_template_async(
        self,
        request: main_models.ModifyAppAgentTemplateRequest,
    ) -> main_models.ModifyAppAgentTemplateResponse:
        runtime = RuntimeOptions()
        return await self.modify_app_agent_template_with_options_async(request, runtime)

    def modify_app_callback_status_with_options(
        self,
        request: main_models.ModifyAppCallbackStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppCallbackStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppCallbackStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppCallbackStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_callback_status_with_options_async(
        self,
        request: main_models.ModifyAppCallbackStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppCallbackStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppCallbackStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppCallbackStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_callback_status(
        self,
        request: main_models.ModifyAppCallbackStatusRequest,
    ) -> main_models.ModifyAppCallbackStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_app_callback_status_with_options(request, runtime)

    async def modify_app_callback_status_async(
        self,
        request: main_models.ModifyAppCallbackStatusRequest,
    ) -> main_models.ModifyAppCallbackStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_app_callback_status_with_options_async(request, runtime)

    def modify_app_layout_with_options(
        self,
        tmp_req: main_models.ModifyAppLayoutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppLayoutResponse:
        tmp_req.validate()
        request = main_models.ModifyAppLayoutShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.layout):
            request.layout_shrink = Utils.array_to_string_with_specified_style(tmp_req.layout, 'Layout', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.layout_shrink):
            query['Layout'] = request.layout_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppLayout',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppLayoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_layout_with_options_async(
        self,
        tmp_req: main_models.ModifyAppLayoutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppLayoutResponse:
        tmp_req.validate()
        request = main_models.ModifyAppLayoutShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.layout):
            request.layout_shrink = Utils.array_to_string_with_specified_style(tmp_req.layout, 'Layout', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.layout_shrink):
            query['Layout'] = request.layout_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppLayout',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppLayoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_layout(
        self,
        request: main_models.ModifyAppLayoutRequest,
    ) -> main_models.ModifyAppLayoutResponse:
        runtime = RuntimeOptions()
        return self.modify_app_layout_with_options(request, runtime)

    async def modify_app_layout_async(
        self,
        request: main_models.ModifyAppLayoutRequest,
    ) -> main_models.ModifyAppLayoutResponse:
        runtime = RuntimeOptions()
        return await self.modify_app_layout_with_options_async(request, runtime)

    def modify_app_live_stream_status_with_options(
        self,
        request: main_models.ModifyAppLiveStreamStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppLiveStreamStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppLiveStreamStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppLiveStreamStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_live_stream_status_with_options_async(
        self,
        request: main_models.ModifyAppLiveStreamStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppLiveStreamStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppLiveStreamStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppLiveStreamStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_live_stream_status(
        self,
        request: main_models.ModifyAppLiveStreamStatusRequest,
    ) -> main_models.ModifyAppLiveStreamStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_app_live_stream_status_with_options(request, runtime)

    async def modify_app_live_stream_status_async(
        self,
        request: main_models.ModifyAppLiveStreamStatusRequest,
    ) -> main_models.ModifyAppLiveStreamStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_app_live_stream_status_with_options_async(request, runtime)

    def modify_app_record_status_with_options(
        self,
        request: main_models.ModifyAppRecordStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppRecordStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppRecordStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppRecordStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_record_status_with_options_async(
        self,
        request: main_models.ModifyAppRecordStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppRecordStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppRecordStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppRecordStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_record_status(
        self,
        request: main_models.ModifyAppRecordStatusRequest,
    ) -> main_models.ModifyAppRecordStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_app_record_status_with_options(request, runtime)

    async def modify_app_record_status_async(
        self,
        request: main_models.ModifyAppRecordStatusRequest,
    ) -> main_models.ModifyAppRecordStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_app_record_status_with_options_async(request, runtime)

    def modify_app_record_template_with_options(
        self,
        tmp_req: main_models.ModifyAppRecordTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppRecordTemplateResponse:
        tmp_req.validate()
        request = main_models.ModifyAppRecordTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.record_template):
            request.record_template_shrink = Utils.array_to_string_with_specified_style(tmp_req.record_template, 'RecordTemplate', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.record_template_shrink):
            query['RecordTemplate'] = request.record_template_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppRecordTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_record_template_with_options_async(
        self,
        tmp_req: main_models.ModifyAppRecordTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppRecordTemplateResponse:
        tmp_req.validate()
        request = main_models.ModifyAppRecordTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.record_template):
            request.record_template_shrink = Utils.array_to_string_with_specified_style(tmp_req.record_template, 'RecordTemplate', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.record_template_shrink):
            query['RecordTemplate'] = request.record_template_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppRecordTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppRecordTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_record_template(
        self,
        request: main_models.ModifyAppRecordTemplateRequest,
    ) -> main_models.ModifyAppRecordTemplateResponse:
        runtime = RuntimeOptions()
        return self.modify_app_record_template_with_options(request, runtime)

    async def modify_app_record_template_async(
        self,
        request: main_models.ModifyAppRecordTemplateRequest,
    ) -> main_models.ModifyAppRecordTemplateResponse:
        runtime = RuntimeOptions()
        return await self.modify_app_record_template_with_options_async(request, runtime)

    def modify_app_streaming_out_template_with_options(
        self,
        tmp_req: main_models.ModifyAppStreamingOutTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppStreamingOutTemplateResponse:
        tmp_req.validate()
        request = main_models.ModifyAppStreamingOutTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.streaming_out_template):
            request.streaming_out_template_shrink = Utils.array_to_string_with_specified_style(tmp_req.streaming_out_template, 'StreamingOutTemplate', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.streaming_out_template_shrink):
            query['StreamingOutTemplate'] = request.streaming_out_template_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppStreamingOutTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppStreamingOutTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_streaming_out_template_with_options_async(
        self,
        tmp_req: main_models.ModifyAppStreamingOutTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppStreamingOutTemplateResponse:
        tmp_req.validate()
        request = main_models.ModifyAppStreamingOutTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.streaming_out_template):
            request.streaming_out_template_shrink = Utils.array_to_string_with_specified_style(tmp_req.streaming_out_template, 'StreamingOutTemplate', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.streaming_out_template_shrink):
            query['StreamingOutTemplate'] = request.streaming_out_template_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppStreamingOutTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppStreamingOutTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_streaming_out_template(
        self,
        request: main_models.ModifyAppStreamingOutTemplateRequest,
    ) -> main_models.ModifyAppStreamingOutTemplateResponse:
        runtime = RuntimeOptions()
        return self.modify_app_streaming_out_template_with_options(request, runtime)

    async def modify_app_streaming_out_template_async(
        self,
        request: main_models.ModifyAppStreamingOutTemplateRequest,
    ) -> main_models.ModifyAppStreamingOutTemplateResponse:
        runtime = RuntimeOptions()
        return await self.modify_app_streaming_out_template_with_options_async(request, runtime)

    def modify_app_view_status_with_options(
        self,
        request: main_models.ModifyAppViewStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppViewStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppViewStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppViewStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_view_status_with_options_async(
        self,
        request: main_models.ModifyAppViewStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppViewStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppViewStatus',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppViewStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_view_status(
        self,
        request: main_models.ModifyAppViewStatusRequest,
    ) -> main_models.ModifyAppViewStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_app_view_status_with_options(request, runtime)

    async def modify_app_view_status_async(
        self,
        request: main_models.ModifyAppViewStatusRequest,
    ) -> main_models.ModifyAppViewStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_app_view_status_with_options_async(request, runtime)

    def modify_app_view_template_with_options(
        self,
        tmp_req: main_models.ModifyAppViewTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppViewTemplateResponse:
        tmp_req.validate()
        request = main_models.ModifyAppViewTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.template):
            request.template_shrink = Utils.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.template_shrink):
            query['Template'] = request.template_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppViewTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppViewTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_view_template_with_options_async(
        self,
        tmp_req: main_models.ModifyAppViewTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppViewTemplateResponse:
        tmp_req.validate()
        request = main_models.ModifyAppViewTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.template):
            request.template_shrink = Utils.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.template_shrink):
            query['Template'] = request.template_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppViewTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppViewTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_view_template(
        self,
        request: main_models.ModifyAppViewTemplateRequest,
    ) -> main_models.ModifyAppViewTemplateResponse:
        runtime = RuntimeOptions()
        return self.modify_app_view_template_with_options(request, runtime)

    async def modify_app_view_template_async(
        self,
        request: main_models.ModifyAppViewTemplateRequest,
    ) -> main_models.ModifyAppViewTemplateResponse:
        runtime = RuntimeOptions()
        return await self.modify_app_view_template_with_options_async(request, runtime)

    def modify_callback_meta_with_options(
        self,
        tmp_req: main_models.ModifyCallbackMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCallbackMetaResponse:
        tmp_req.validate()
        request = main_models.ModifyCallbackMetaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.callback):
            request.callback_shrink = Utils.array_to_string_with_specified_style(tmp_req.callback, 'Callback', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.callback_shrink):
            query['Callback'] = request.callback_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCallbackMeta',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCallbackMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_callback_meta_with_options_async(
        self,
        tmp_req: main_models.ModifyCallbackMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCallbackMetaResponse:
        tmp_req.validate()
        request = main_models.ModifyCallbackMetaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.callback):
            request.callback_shrink = Utils.array_to_string_with_specified_style(tmp_req.callback, 'Callback', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.callback_shrink):
            query['Callback'] = request.callback_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCallbackMeta',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCallbackMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_callback_meta(
        self,
        request: main_models.ModifyCallbackMetaRequest,
    ) -> main_models.ModifyCallbackMetaResponse:
        runtime = RuntimeOptions()
        return self.modify_callback_meta_with_options(request, runtime)

    async def modify_callback_meta_async(
        self,
        request: main_models.ModifyCallbackMetaRequest,
    ) -> main_models.ModifyCallbackMetaResponse:
        runtime = RuntimeOptions()
        return await self.modify_callback_meta_with_options_async(request, runtime)

    def modify_cloud_note_phrases_with_options(
        self,
        tmp_req: main_models.ModifyCloudNotePhrasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCloudNotePhrasesResponse:
        tmp_req.validate()
        request = main_models.ModifyCloudNotePhrasesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.phrase):
            request.phrase_shrink = Utils.array_to_string_with_specified_style(tmp_req.phrase, 'Phrase', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.phrase_shrink):
            query['Phrase'] = request.phrase_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCloudNotePhrases',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCloudNotePhrasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cloud_note_phrases_with_options_async(
        self,
        tmp_req: main_models.ModifyCloudNotePhrasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCloudNotePhrasesResponse:
        tmp_req.validate()
        request = main_models.ModifyCloudNotePhrasesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.phrase):
            request.phrase_shrink = Utils.array_to_string_with_specified_style(tmp_req.phrase, 'Phrase', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.phrase_shrink):
            query['Phrase'] = request.phrase_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCloudNotePhrases',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCloudNotePhrasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cloud_note_phrases(
        self,
        request: main_models.ModifyCloudNotePhrasesRequest,
    ) -> main_models.ModifyCloudNotePhrasesResponse:
        runtime = RuntimeOptions()
        return self.modify_cloud_note_phrases_with_options(request, runtime)

    async def modify_cloud_note_phrases_async(
        self,
        request: main_models.ModifyCloudNotePhrasesRequest,
    ) -> main_models.ModifyCloudNotePhrasesResponse:
        runtime = RuntimeOptions()
        return await self.modify_cloud_note_phrases_with_options_async(request, runtime)

    def modify_mpulayout_with_options(
        self,
        request: main_models.ModifyMPULayoutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMPULayoutResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.audio_mix_count):
            query['AudioMixCount'] = request.audio_mix_count
        if not DaraCore.is_null(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.panes):
            query['Panes'] = request.panes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMPULayout',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMPULayoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_mpulayout_with_options_async(
        self,
        request: main_models.ModifyMPULayoutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMPULayoutResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.audio_mix_count):
            query['AudioMixCount'] = request.audio_mix_count
        if not DaraCore.is_null(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.panes):
            query['Panes'] = request.panes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMPULayout',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMPULayoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_mpulayout(
        self,
        request: main_models.ModifyMPULayoutRequest,
    ) -> main_models.ModifyMPULayoutResponse:
        runtime = RuntimeOptions()
        return self.modify_mpulayout_with_options(request, runtime)

    async def modify_mpulayout_async(
        self,
        request: main_models.ModifyMPULayoutRequest,
    ) -> main_models.ModifyMPULayoutResponse:
        runtime = RuntimeOptions()
        return await self.modify_mpulayout_with_options_async(request, runtime)

    def modify_streaming_property_with_options(
        self,
        tmp_req: main_models.ModifyStreamingPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyStreamingPropertyResponse:
        tmp_req.validate()
        request = main_models.ModifyStreamingPropertyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.view_subscribers):
            request.view_subscribers_shrink = Utils.array_to_string_with_specified_style(tmp_req.view_subscribers, 'ViewSubscribers', 'simple')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.view_content):
            query['ViewContent'] = request.view_content
        if not DaraCore.is_null(request.view_subscribers_shrink):
            query['ViewSubscribers'] = request.view_subscribers_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyStreamingProperty',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyStreamingPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_streaming_property_with_options_async(
        self,
        tmp_req: main_models.ModifyStreamingPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyStreamingPropertyResponse:
        tmp_req.validate()
        request = main_models.ModifyStreamingPropertyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.view_subscribers):
            request.view_subscribers_shrink = Utils.array_to_string_with_specified_style(tmp_req.view_subscribers, 'ViewSubscribers', 'simple')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.view_content):
            query['ViewContent'] = request.view_content
        if not DaraCore.is_null(request.view_subscribers_shrink):
            query['ViewSubscribers'] = request.view_subscribers_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyStreamingProperty',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyStreamingPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_streaming_property(
        self,
        request: main_models.ModifyStreamingPropertyRequest,
    ) -> main_models.ModifyStreamingPropertyResponse:
        runtime = RuntimeOptions()
        return self.modify_streaming_property_with_options(request, runtime)

    async def modify_streaming_property_async(
        self,
        request: main_models.ModifyStreamingPropertyRequest,
    ) -> main_models.ModifyStreamingPropertyResponse:
        runtime = RuntimeOptions()
        return await self.modify_streaming_property_with_options_async(request, runtime)

    def modify_view_layout_with_options(
        self,
        tmp_req: main_models.ModifyViewLayoutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyViewLayoutResponse:
        tmp_req.validate()
        request = main_models.ModifyViewLayoutShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.layout_specified_users):
            request.layout_specified_users_shrink = Utils.array_to_string_with_specified_style(tmp_req.layout_specified_users, 'LayoutSpecifiedUsers', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not DaraCore.is_null(request.images):
            query['Images'] = request.images
        if not DaraCore.is_null(request.layout_specified_users_shrink):
            query['LayoutSpecifiedUsers'] = request.layout_specified_users_shrink
        if not DaraCore.is_null(request.panes):
            query['Panes'] = request.panes
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.texts):
            query['Texts'] = request.texts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyViewLayout',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyViewLayoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_view_layout_with_options_async(
        self,
        tmp_req: main_models.ModifyViewLayoutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyViewLayoutResponse:
        tmp_req.validate()
        request = main_models.ModifyViewLayoutShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.layout_specified_users):
            request.layout_specified_users_shrink = Utils.array_to_string_with_specified_style(tmp_req.layout_specified_users, 'LayoutSpecifiedUsers', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not DaraCore.is_null(request.images):
            query['Images'] = request.images
        if not DaraCore.is_null(request.layout_specified_users_shrink):
            query['LayoutSpecifiedUsers'] = request.layout_specified_users_shrink
        if not DaraCore.is_null(request.panes):
            query['Panes'] = request.panes
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.texts):
            query['Texts'] = request.texts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyViewLayout',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyViewLayoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_view_layout(
        self,
        request: main_models.ModifyViewLayoutRequest,
    ) -> main_models.ModifyViewLayoutResponse:
        runtime = RuntimeOptions()
        return self.modify_view_layout_with_options(request, runtime)

    async def modify_view_layout_async(
        self,
        request: main_models.ModifyViewLayoutRequest,
    ) -> main_models.ModifyViewLayoutResponse:
        runtime = RuntimeOptions()
        return await self.modify_view_layout_with_options_async(request, runtime)

    def notify_agent_with_options(
        self,
        tmp_req: main_models.NotifyAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.NotifyAgentResponse:
        tmp_req.validate()
        request = main_models.NotifyAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.background_music):
            request.background_music_shrink = Utils.array_to_string_with_specified_style(tmp_req.background_music, 'BackgroundMusic', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.background_music_shrink):
            query['BackgroundMusic'] = request.background_music_shrink
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.custom_attribute):
            query['CustomAttribute'] = request.custom_attribute
        if not DaraCore.is_null(request.interruptable):
            query['Interruptable'] = request.interruptable
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'NotifyAgent',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.NotifyAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def notify_agent_with_options_async(
        self,
        tmp_req: main_models.NotifyAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.NotifyAgentResponse:
        tmp_req.validate()
        request = main_models.NotifyAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.background_music):
            request.background_music_shrink = Utils.array_to_string_with_specified_style(tmp_req.background_music, 'BackgroundMusic', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.background_music_shrink):
            query['BackgroundMusic'] = request.background_music_shrink
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.custom_attribute):
            query['CustomAttribute'] = request.custom_attribute
        if not DaraCore.is_null(request.interruptable):
            query['Interruptable'] = request.interruptable
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'NotifyAgent',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.NotifyAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def notify_agent(
        self,
        request: main_models.NotifyAgentRequest,
    ) -> main_models.NotifyAgentResponse:
        runtime = RuntimeOptions()
        return self.notify_agent_with_options(request, runtime)

    async def notify_agent_async(
        self,
        request: main_models.NotifyAgentRequest,
    ) -> main_models.NotifyAgentResponse:
        runtime = RuntimeOptions()
        return await self.notify_agent_with_options_async(request, runtime)

    def remove_terminals_with_options(
        self,
        request: main_models.RemoveTerminalsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveTerminalsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.terminal_ids):
            query['TerminalIds'] = request.terminal_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveTerminals',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveTerminalsResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_terminals_with_options_async(
        self,
        request: main_models.RemoveTerminalsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveTerminalsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.terminal_ids):
            query['TerminalIds'] = request.terminal_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveTerminals',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveTerminalsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_terminals(
        self,
        request: main_models.RemoveTerminalsRequest,
    ) -> main_models.RemoveTerminalsResponse:
        runtime = RuntimeOptions()
        return self.remove_terminals_with_options(request, runtime)

    async def remove_terminals_async(
        self,
        request: main_models.RemoveTerminalsRequest,
    ) -> main_models.RemoveTerminalsResponse:
        runtime = RuntimeOptions()
        return await self.remove_terminals_with_options_async(request, runtime)

    def remove_users_with_options(
        self,
        request: main_models.RemoveUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.users):
            query['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUsers',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_users_with_options_async(
        self,
        request: main_models.RemoveUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.users):
            query['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUsers',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_users(
        self,
        request: main_models.RemoveUsersRequest,
    ) -> main_models.RemoveUsersResponse:
        runtime = RuntimeOptions()
        return self.remove_users_with_options(request, runtime)

    async def remove_users_async(
        self,
        request: main_models.RemoveUsersRequest,
    ) -> main_models.RemoveUsersResponse:
        runtime = RuntimeOptions()
        return await self.remove_users_with_options_async(request, runtime)

    def rtc_cancel_sip_invite_with_options(
        self,
        request: main_models.RtcCancelSipInviteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RtcCancelSipInviteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.device_type):
            query['DeviceType'] = request.device_type
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RtcCancelSipInvite',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RtcCancelSipInviteResponse(),
            self.call_api(params, req, runtime)
        )

    async def rtc_cancel_sip_invite_with_options_async(
        self,
        request: main_models.RtcCancelSipInviteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RtcCancelSipInviteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.device_type):
            query['DeviceType'] = request.device_type
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RtcCancelSipInvite',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RtcCancelSipInviteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rtc_cancel_sip_invite(
        self,
        request: main_models.RtcCancelSipInviteRequest,
    ) -> main_models.RtcCancelSipInviteResponse:
        runtime = RuntimeOptions()
        return self.rtc_cancel_sip_invite_with_options(request, runtime)

    async def rtc_cancel_sip_invite_async(
        self,
        request: main_models.RtcCancelSipInviteRequest,
    ) -> main_models.RtcCancelSipInviteResponse:
        runtime = RuntimeOptions()
        return await self.rtc_cancel_sip_invite_with_options_async(request, runtime)

    def rtc_sip_invite_member_with_options(
        self,
        request: main_models.RtcSipInviteMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RtcSipInviteMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_token):
            query['AppToken'] = request.app_token
        if not DaraCore.is_null(request.call_number):
            query['CallNumber'] = request.call_number
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.device_type):
            query['DeviceType'] = request.device_type
        if not DaraCore.is_null(request.registered):
            query['Registered'] = request.registered
        if not DaraCore.is_null(request.server_address):
            query['ServerAddress'] = request.server_address
        if not DaraCore.is_null(request.sip_display_name):
            query['SipDisplayName'] = request.sip_display_name
        if not DaraCore.is_null(request.sip_room_id):
            query['SipRoomId'] = request.sip_room_id
        if not DaraCore.is_null(request.sip_uri):
            query['SipUri'] = request.sip_uri
        if not DaraCore.is_null(request.sip_user_agent):
            query['SipUserAgent'] = request.sip_user_agent
        if not DaraCore.is_null(request.sip_user_id):
            query['SipUserId'] = request.sip_user_id
        if not DaraCore.is_null(request.sip_user_password):
            query['SipUserPassword'] = request.sip_user_password
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RtcSipInviteMember',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RtcSipInviteMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def rtc_sip_invite_member_with_options_async(
        self,
        request: main_models.RtcSipInviteMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RtcSipInviteMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_token):
            query['AppToken'] = request.app_token
        if not DaraCore.is_null(request.call_number):
            query['CallNumber'] = request.call_number
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.device_type):
            query['DeviceType'] = request.device_type
        if not DaraCore.is_null(request.registered):
            query['Registered'] = request.registered
        if not DaraCore.is_null(request.server_address):
            query['ServerAddress'] = request.server_address
        if not DaraCore.is_null(request.sip_display_name):
            query['SipDisplayName'] = request.sip_display_name
        if not DaraCore.is_null(request.sip_room_id):
            query['SipRoomId'] = request.sip_room_id
        if not DaraCore.is_null(request.sip_uri):
            query['SipUri'] = request.sip_uri
        if not DaraCore.is_null(request.sip_user_agent):
            query['SipUserAgent'] = request.sip_user_agent
        if not DaraCore.is_null(request.sip_user_id):
            query['SipUserId'] = request.sip_user_id
        if not DaraCore.is_null(request.sip_user_password):
            query['SipUserPassword'] = request.sip_user_password
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RtcSipInviteMember',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RtcSipInviteMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rtc_sip_invite_member(
        self,
        request: main_models.RtcSipInviteMemberRequest,
    ) -> main_models.RtcSipInviteMemberResponse:
        runtime = RuntimeOptions()
        return self.rtc_sip_invite_member_with_options(request, runtime)

    async def rtc_sip_invite_member_async(
        self,
        request: main_models.RtcSipInviteMemberRequest,
    ) -> main_models.RtcSipInviteMemberResponse:
        runtime = RuntimeOptions()
        return await self.rtc_sip_invite_member_with_options_async(request, runtime)

    def rtc_sip_mute_with_options(
        self,
        request: main_models.RtcSipMuteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RtcSipMuteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.operations):
            query['Operations'] = request.operations
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RtcSipMute',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RtcSipMuteResponse(),
            self.call_api(params, req, runtime)
        )

    async def rtc_sip_mute_with_options_async(
        self,
        request: main_models.RtcSipMuteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RtcSipMuteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.operations):
            query['Operations'] = request.operations
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RtcSipMute',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RtcSipMuteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rtc_sip_mute(
        self,
        request: main_models.RtcSipMuteRequest,
    ) -> main_models.RtcSipMuteResponse:
        runtime = RuntimeOptions()
        return self.rtc_sip_mute_with_options(request, runtime)

    async def rtc_sip_mute_async(
        self,
        request: main_models.RtcSipMuteRequest,
    ) -> main_models.RtcSipMuteResponse:
        runtime = RuntimeOptions()
        return await self.rtc_sip_mute_with_options_async(request, runtime)

    def start_agent_with_options(
        self,
        tmp_req: main_models.StartAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartAgentResponse:
        tmp_req.validate()
        request = main_models.StartAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rtc_config):
            request.rtc_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.rtc_config, 'RtcConfig', 'json')
        if not DaraCore.is_null(tmp_req.voice_chat_config):
            request.voice_chat_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.voice_chat_config, 'VoiceChatConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.rtc_config_shrink):
            query['RtcConfig'] = request.rtc_config_shrink
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.voice_chat_config_shrink):
            query['VoiceChatConfig'] = request.voice_chat_config_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartAgent',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_agent_with_options_async(
        self,
        tmp_req: main_models.StartAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartAgentResponse:
        tmp_req.validate()
        request = main_models.StartAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rtc_config):
            request.rtc_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.rtc_config, 'RtcConfig', 'json')
        if not DaraCore.is_null(tmp_req.voice_chat_config):
            request.voice_chat_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.voice_chat_config, 'VoiceChatConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.rtc_config_shrink):
            query['RtcConfig'] = request.rtc_config_shrink
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.voice_chat_config_shrink):
            query['VoiceChatConfig'] = request.voice_chat_config_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartAgent',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_agent(
        self,
        request: main_models.StartAgentRequest,
    ) -> main_models.StartAgentResponse:
        runtime = RuntimeOptions()
        return self.start_agent_with_options(request, runtime)

    async def start_agent_async(
        self,
        request: main_models.StartAgentRequest,
    ) -> main_models.StartAgentResponse:
        runtime = RuntimeOptions()
        return await self.start_agent_with_options_async(request, runtime)

    def start_category_callback_with_options(
        self,
        tmp_req: main_models.StartCategoryCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartCategoryCallbackResponse:
        tmp_req.validate()
        request = main_models.StartCategoryCallbackShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.callback):
            request.callback_shrink = Utils.array_to_string_with_specified_style(tmp_req.callback, 'Callback', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.callback_shrink):
            query['Callback'] = request.callback_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartCategoryCallback',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartCategoryCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_category_callback_with_options_async(
        self,
        tmp_req: main_models.StartCategoryCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartCategoryCallbackResponse:
        tmp_req.validate()
        request = main_models.StartCategoryCallbackShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.callback):
            request.callback_shrink = Utils.array_to_string_with_specified_style(tmp_req.callback, 'Callback', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.callback_shrink):
            query['Callback'] = request.callback_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartCategoryCallback',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartCategoryCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_category_callback(
        self,
        request: main_models.StartCategoryCallbackRequest,
    ) -> main_models.StartCategoryCallbackResponse:
        runtime = RuntimeOptions()
        return self.start_category_callback_with_options(request, runtime)

    async def start_category_callback_async(
        self,
        request: main_models.StartCategoryCallbackRequest,
    ) -> main_models.StartCategoryCallbackResponse:
        runtime = RuntimeOptions()
        return await self.start_category_callback_with_options_async(request, runtime)

    def start_cloud_note_with_options(
        self,
        tmp_req: main_models.StartCloudNoteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartCloudNoteResponse:
        tmp_req.validate()
        request = main_models.StartCloudNoteShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auto_chapters):
            request.auto_chapters_shrink = Utils.array_to_string_with_specified_style(tmp_req.auto_chapters, 'AutoChapters', 'json')
        if not DaraCore.is_null(tmp_req.custom_prompt):
            request.custom_prompt_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_prompt, 'CustomPrompt', 'json')
        if not DaraCore.is_null(tmp_req.meeting_assistance):
            request.meeting_assistance_shrink = Utils.array_to_string_with_specified_style(tmp_req.meeting_assistance, 'MeetingAssistance', 'json')
        if not DaraCore.is_null(tmp_req.realtime_subtitle):
            request.realtime_subtitle_shrink = Utils.array_to_string_with_specified_style(tmp_req.realtime_subtitle, 'RealtimeSubtitle', 'json')
        if not DaraCore.is_null(tmp_req.service_inspection):
            request.service_inspection_shrink = Utils.array_to_string_with_specified_style(tmp_req.service_inspection, 'ServiceInspection', 'json')
        if not DaraCore.is_null(tmp_req.summarization):
            request.summarization_shrink = Utils.array_to_string_with_specified_style(tmp_req.summarization, 'Summarization', 'json')
        if not DaraCore.is_null(tmp_req.text_polish):
            request.text_polish_shrink = Utils.array_to_string_with_specified_style(tmp_req.text_polish, 'TextPolish', 'json')
        if not DaraCore.is_null(tmp_req.transcription):
            request.transcription_shrink = Utils.array_to_string_with_specified_style(tmp_req.transcription, 'Transcription', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auto_chapters_shrink):
            query['AutoChapters'] = request.auto_chapters_shrink
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.custom_prompt_shrink):
            query['CustomPrompt'] = request.custom_prompt_shrink
        if not DaraCore.is_null(request.language_hints):
            query['LanguageHints'] = request.language_hints
        if not DaraCore.is_null(request.meeting_assistance_shrink):
            query['MeetingAssistance'] = request.meeting_assistance_shrink
        if not DaraCore.is_null(request.realtime_subtitle_shrink):
            query['RealtimeSubtitle'] = request.realtime_subtitle_shrink
        if not DaraCore.is_null(request.service_inspection_shrink):
            query['ServiceInspection'] = request.service_inspection_shrink
        if not DaraCore.is_null(request.source_language):
            query['SourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.storage_config):
            query['StorageConfig'] = request.storage_config
        if not DaraCore.is_null(request.summarization_shrink):
            query['Summarization'] = request.summarization_shrink
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.text_polish_shrink):
            query['TextPolish'] = request.text_polish_shrink
        if not DaraCore.is_null(request.transcription_shrink):
            query['Transcription'] = request.transcription_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartCloudNote',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartCloudNoteResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_cloud_note_with_options_async(
        self,
        tmp_req: main_models.StartCloudNoteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartCloudNoteResponse:
        tmp_req.validate()
        request = main_models.StartCloudNoteShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auto_chapters):
            request.auto_chapters_shrink = Utils.array_to_string_with_specified_style(tmp_req.auto_chapters, 'AutoChapters', 'json')
        if not DaraCore.is_null(tmp_req.custom_prompt):
            request.custom_prompt_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_prompt, 'CustomPrompt', 'json')
        if not DaraCore.is_null(tmp_req.meeting_assistance):
            request.meeting_assistance_shrink = Utils.array_to_string_with_specified_style(tmp_req.meeting_assistance, 'MeetingAssistance', 'json')
        if not DaraCore.is_null(tmp_req.realtime_subtitle):
            request.realtime_subtitle_shrink = Utils.array_to_string_with_specified_style(tmp_req.realtime_subtitle, 'RealtimeSubtitle', 'json')
        if not DaraCore.is_null(tmp_req.service_inspection):
            request.service_inspection_shrink = Utils.array_to_string_with_specified_style(tmp_req.service_inspection, 'ServiceInspection', 'json')
        if not DaraCore.is_null(tmp_req.summarization):
            request.summarization_shrink = Utils.array_to_string_with_specified_style(tmp_req.summarization, 'Summarization', 'json')
        if not DaraCore.is_null(tmp_req.text_polish):
            request.text_polish_shrink = Utils.array_to_string_with_specified_style(tmp_req.text_polish, 'TextPolish', 'json')
        if not DaraCore.is_null(tmp_req.transcription):
            request.transcription_shrink = Utils.array_to_string_with_specified_style(tmp_req.transcription, 'Transcription', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auto_chapters_shrink):
            query['AutoChapters'] = request.auto_chapters_shrink
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.custom_prompt_shrink):
            query['CustomPrompt'] = request.custom_prompt_shrink
        if not DaraCore.is_null(request.language_hints):
            query['LanguageHints'] = request.language_hints
        if not DaraCore.is_null(request.meeting_assistance_shrink):
            query['MeetingAssistance'] = request.meeting_assistance_shrink
        if not DaraCore.is_null(request.realtime_subtitle_shrink):
            query['RealtimeSubtitle'] = request.realtime_subtitle_shrink
        if not DaraCore.is_null(request.service_inspection_shrink):
            query['ServiceInspection'] = request.service_inspection_shrink
        if not DaraCore.is_null(request.source_language):
            query['SourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.storage_config):
            query['StorageConfig'] = request.storage_config
        if not DaraCore.is_null(request.summarization_shrink):
            query['Summarization'] = request.summarization_shrink
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.text_polish_shrink):
            query['TextPolish'] = request.text_polish_shrink
        if not DaraCore.is_null(request.transcription_shrink):
            query['Transcription'] = request.transcription_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartCloudNote',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartCloudNoteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_cloud_note(
        self,
        request: main_models.StartCloudNoteRequest,
    ) -> main_models.StartCloudNoteResponse:
        runtime = RuntimeOptions()
        return self.start_cloud_note_with_options(request, runtime)

    async def start_cloud_note_async(
        self,
        request: main_models.StartCloudNoteRequest,
    ) -> main_models.StartCloudNoteResponse:
        runtime = RuntimeOptions()
        return await self.start_cloud_note_with_options_async(request, runtime)

    def start_cloud_record_with_options(
        self,
        tmp_req: main_models.StartCloudRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartCloudRecordResponse:
        tmp_req.validate()
        request = main_models.StartCloudRecordShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.layout_specified_users):
            request.layout_specified_users_shrink = Utils.array_to_string_with_specified_style(tmp_req.layout_specified_users, 'LayoutSpecifiedUsers', 'json')
        if not DaraCore.is_null(tmp_req.single_streaming_record):
            request.single_streaming_record_shrink = Utils.array_to_string_with_specified_style(tmp_req.single_streaming_record, 'SingleStreamingRecord', 'json')
        query = {}
        if not DaraCore.is_null(request.annotation):
            query['Annotation'] = request.annotation
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not DaraCore.is_null(request.bg_color):
            query['BgColor'] = request.bg_color
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not DaraCore.is_null(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not DaraCore.is_null(request.images):
            query['Images'] = request.images
        if not DaraCore.is_null(request.layout_specified_users_shrink):
            query['LayoutSpecifiedUsers'] = request.layout_specified_users_shrink
        if not DaraCore.is_null(request.panes):
            query['Panes'] = request.panes
        if not DaraCore.is_null(request.record_mode):
            query['RecordMode'] = request.record_mode
        if not DaraCore.is_null(request.region_color):
            query['RegionColor'] = request.region_color
        if not DaraCore.is_null(request.reserve_pane_for_no_camera_user):
            query['ReservePaneForNoCameraUser'] = request.reserve_pane_for_no_camera_user
        if not DaraCore.is_null(request.show_default_background_on_mute):
            query['ShowDefaultBackgroundOnMute'] = request.show_default_background_on_mute
        if not DaraCore.is_null(request.single_streaming_record_shrink):
            query['SingleStreamingRecord'] = request.single_streaming_record_shrink
        if not DaraCore.is_null(request.start_without_channel):
            query['StartWithoutChannel'] = request.start_without_channel
        if not DaraCore.is_null(request.start_without_channel_wait_time):
            query['StartWithoutChannelWaitTime'] = request.start_without_channel_wait_time
        if not DaraCore.is_null(request.storage_config):
            query['StorageConfig'] = request.storage_config
        if not DaraCore.is_null(request.sub_high_resolution_stream):
            query['SubHighResolutionStream'] = request.sub_high_resolution_stream
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.texts):
            query['Texts'] = request.texts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartCloudRecord',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartCloudRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_cloud_record_with_options_async(
        self,
        tmp_req: main_models.StartCloudRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartCloudRecordResponse:
        tmp_req.validate()
        request = main_models.StartCloudRecordShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.layout_specified_users):
            request.layout_specified_users_shrink = Utils.array_to_string_with_specified_style(tmp_req.layout_specified_users, 'LayoutSpecifiedUsers', 'json')
        if not DaraCore.is_null(tmp_req.single_streaming_record):
            request.single_streaming_record_shrink = Utils.array_to_string_with_specified_style(tmp_req.single_streaming_record, 'SingleStreamingRecord', 'json')
        query = {}
        if not DaraCore.is_null(request.annotation):
            query['Annotation'] = request.annotation
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not DaraCore.is_null(request.bg_color):
            query['BgColor'] = request.bg_color
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not DaraCore.is_null(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not DaraCore.is_null(request.images):
            query['Images'] = request.images
        if not DaraCore.is_null(request.layout_specified_users_shrink):
            query['LayoutSpecifiedUsers'] = request.layout_specified_users_shrink
        if not DaraCore.is_null(request.panes):
            query['Panes'] = request.panes
        if not DaraCore.is_null(request.record_mode):
            query['RecordMode'] = request.record_mode
        if not DaraCore.is_null(request.region_color):
            query['RegionColor'] = request.region_color
        if not DaraCore.is_null(request.reserve_pane_for_no_camera_user):
            query['ReservePaneForNoCameraUser'] = request.reserve_pane_for_no_camera_user
        if not DaraCore.is_null(request.show_default_background_on_mute):
            query['ShowDefaultBackgroundOnMute'] = request.show_default_background_on_mute
        if not DaraCore.is_null(request.single_streaming_record_shrink):
            query['SingleStreamingRecord'] = request.single_streaming_record_shrink
        if not DaraCore.is_null(request.start_without_channel):
            query['StartWithoutChannel'] = request.start_without_channel
        if not DaraCore.is_null(request.start_without_channel_wait_time):
            query['StartWithoutChannelWaitTime'] = request.start_without_channel_wait_time
        if not DaraCore.is_null(request.storage_config):
            query['StorageConfig'] = request.storage_config
        if not DaraCore.is_null(request.sub_high_resolution_stream):
            query['SubHighResolutionStream'] = request.sub_high_resolution_stream
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.texts):
            query['Texts'] = request.texts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartCloudRecord',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartCloudRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_cloud_record(
        self,
        request: main_models.StartCloudRecordRequest,
    ) -> main_models.StartCloudRecordResponse:
        runtime = RuntimeOptions()
        return self.start_cloud_record_with_options(request, runtime)

    async def start_cloud_record_async(
        self,
        request: main_models.StartCloudRecordRequest,
    ) -> main_models.StartCloudRecordResponse:
        runtime = RuntimeOptions()
        return await self.start_cloud_record_with_options_async(request, runtime)

    def start_mputask_with_options(
        self,
        request: main_models.StartMPUTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartMPUTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not DaraCore.is_null(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not DaraCore.is_null(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not DaraCore.is_null(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not DaraCore.is_null(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not DaraCore.is_null(request.mix_mode):
            query['MixMode'] = request.mix_mode
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.payload_type):
            query['PayloadType'] = request.payload_type
        if not DaraCore.is_null(request.report_vad):
            query['ReportVad'] = request.report_vad
        if not DaraCore.is_null(request.rtp_ext_info):
            query['RtpExtInfo'] = request.rtp_ext_info
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        if not DaraCore.is_null(request.stream_url):
            query['StreamURL'] = request.stream_url
        if not DaraCore.is_null(request.sub_spec_audio_users):
            query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        if not DaraCore.is_null(request.sub_spec_camera_users):
            query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        if not DaraCore.is_null(request.sub_spec_share_screen_users):
            query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        if not DaraCore.is_null(request.sub_spec_users):
            query['SubSpecUsers'] = request.sub_spec_users
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.time_stamp_ref):
            query['TimeStampRef'] = request.time_stamp_ref
        if not DaraCore.is_null(request.unsub_spec_audio_users):
            query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        if not DaraCore.is_null(request.unsub_spec_camera_users):
            query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        if not DaraCore.is_null(request.unsub_spec_share_screen_users):
            query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        if not DaraCore.is_null(request.user_panes):
            query['UserPanes'] = request.user_panes
        if not DaraCore.is_null(request.vad_interval):
            query['VadInterval'] = request.vad_interval
        if not DaraCore.is_null(request.watermarks):
            query['Watermarks'] = request.watermarks
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.enhanced_param):
            body_flat['EnhancedParam'] = request.enhanced_param
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartMPUTask',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartMPUTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_mputask_with_options_async(
        self,
        request: main_models.StartMPUTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartMPUTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not DaraCore.is_null(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not DaraCore.is_null(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not DaraCore.is_null(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not DaraCore.is_null(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not DaraCore.is_null(request.mix_mode):
            query['MixMode'] = request.mix_mode
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.payload_type):
            query['PayloadType'] = request.payload_type
        if not DaraCore.is_null(request.report_vad):
            query['ReportVad'] = request.report_vad
        if not DaraCore.is_null(request.rtp_ext_info):
            query['RtpExtInfo'] = request.rtp_ext_info
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        if not DaraCore.is_null(request.stream_url):
            query['StreamURL'] = request.stream_url
        if not DaraCore.is_null(request.sub_spec_audio_users):
            query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        if not DaraCore.is_null(request.sub_spec_camera_users):
            query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        if not DaraCore.is_null(request.sub_spec_share_screen_users):
            query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        if not DaraCore.is_null(request.sub_spec_users):
            query['SubSpecUsers'] = request.sub_spec_users
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.time_stamp_ref):
            query['TimeStampRef'] = request.time_stamp_ref
        if not DaraCore.is_null(request.unsub_spec_audio_users):
            query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        if not DaraCore.is_null(request.unsub_spec_camera_users):
            query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        if not DaraCore.is_null(request.unsub_spec_share_screen_users):
            query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        if not DaraCore.is_null(request.user_panes):
            query['UserPanes'] = request.user_panes
        if not DaraCore.is_null(request.vad_interval):
            query['VadInterval'] = request.vad_interval
        if not DaraCore.is_null(request.watermarks):
            query['Watermarks'] = request.watermarks
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.enhanced_param):
            body_flat['EnhancedParam'] = request.enhanced_param
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartMPUTask',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartMPUTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_mputask(
        self,
        request: main_models.StartMPUTaskRequest,
    ) -> main_models.StartMPUTaskResponse:
        runtime = RuntimeOptions()
        return self.start_mputask_with_options(request, runtime)

    async def start_mputask_async(
        self,
        request: main_models.StartMPUTaskRequest,
    ) -> main_models.StartMPUTaskResponse:
        runtime = RuntimeOptions()
        return await self.start_mputask_with_options_async(request, runtime)

    def start_record_task_with_options(
        self,
        request: main_models.StartRecordTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartRecordTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not DaraCore.is_null(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not DaraCore.is_null(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not DaraCore.is_null(request.mix_mode):
            query['MixMode'] = request.mix_mode
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        if not DaraCore.is_null(request.sub_spec_audio_users):
            query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        if not DaraCore.is_null(request.sub_spec_camera_users):
            query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        if not DaraCore.is_null(request.sub_spec_share_screen_users):
            query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        if not DaraCore.is_null(request.sub_spec_users):
            query['SubSpecUsers'] = request.sub_spec_users
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_profile):
            query['TaskProfile'] = request.task_profile
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.unsub_spec_audio_users):
            query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        if not DaraCore.is_null(request.unsub_spec_camera_users):
            query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        if not DaraCore.is_null(request.unsub_spec_share_screen_users):
            query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        if not DaraCore.is_null(request.user_panes):
            query['UserPanes'] = request.user_panes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartRecordTask',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartRecordTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_record_task_with_options_async(
        self,
        request: main_models.StartRecordTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartRecordTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not DaraCore.is_null(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not DaraCore.is_null(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not DaraCore.is_null(request.mix_mode):
            query['MixMode'] = request.mix_mode
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        if not DaraCore.is_null(request.sub_spec_audio_users):
            query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        if not DaraCore.is_null(request.sub_spec_camera_users):
            query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        if not DaraCore.is_null(request.sub_spec_share_screen_users):
            query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        if not DaraCore.is_null(request.sub_spec_users):
            query['SubSpecUsers'] = request.sub_spec_users
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_profile):
            query['TaskProfile'] = request.task_profile
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.unsub_spec_audio_users):
            query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        if not DaraCore.is_null(request.unsub_spec_camera_users):
            query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        if not DaraCore.is_null(request.unsub_spec_share_screen_users):
            query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        if not DaraCore.is_null(request.user_panes):
            query['UserPanes'] = request.user_panes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartRecordTask',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartRecordTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_record_task(
        self,
        request: main_models.StartRecordTaskRequest,
    ) -> main_models.StartRecordTaskResponse:
        runtime = RuntimeOptions()
        return self.start_record_task_with_options(request, runtime)

    async def start_record_task_async(
        self,
        request: main_models.StartRecordTaskRequest,
    ) -> main_models.StartRecordTaskResponse:
        runtime = RuntimeOptions()
        return await self.start_record_task_with_options_async(request, runtime)

    def start_streaming_out_with_options(
        self,
        tmp_req: main_models.StartStreamingOutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartStreamingOutResponse:
        tmp_req.validate()
        request = main_models.StartStreamingOutShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.layout_specified_users):
            request.layout_specified_users_shrink = Utils.array_to_string_with_specified_style(tmp_req.layout_specified_users, 'LayoutSpecifiedUsers', 'json')
        query = {}
        if not DaraCore.is_null(request.annotation):
            query['Annotation'] = request.annotation
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not DaraCore.is_null(request.bg_color):
            query['BgColor'] = request.bg_color
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not DaraCore.is_null(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not DaraCore.is_null(request.images):
            query['Images'] = request.images
        if not DaraCore.is_null(request.layout_specified_users_shrink):
            query['LayoutSpecifiedUsers'] = request.layout_specified_users_shrink
        if not DaraCore.is_null(request.panes):
            query['Panes'] = request.panes
        if not DaraCore.is_null(request.region_color):
            query['RegionColor'] = request.region_color
        if not DaraCore.is_null(request.reserve_pane_for_no_camera_user):
            query['ReservePaneForNoCameraUser'] = request.reserve_pane_for_no_camera_user
        if not DaraCore.is_null(request.show_default_background_on_mute):
            query['ShowDefaultBackgroundOnMute'] = request.show_default_background_on_mute
        if not DaraCore.is_null(request.spec_mixed_user_list):
            query['SpecMixedUserList'] = request.spec_mixed_user_list
        if not DaraCore.is_null(request.start_without_channel):
            query['StartWithoutChannel'] = request.start_without_channel
        if not DaraCore.is_null(request.start_without_channel_wait_time):
            query['StartWithoutChannelWaitTime'] = request.start_without_channel_wait_time
        if not DaraCore.is_null(request.sub_high_resolution_stream):
            query['SubHighResolutionStream'] = request.sub_high_resolution_stream
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.texts):
            query['Texts'] = request.texts
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartStreamingOut',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartStreamingOutResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_streaming_out_with_options_async(
        self,
        tmp_req: main_models.StartStreamingOutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartStreamingOutResponse:
        tmp_req.validate()
        request = main_models.StartStreamingOutShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.layout_specified_users):
            request.layout_specified_users_shrink = Utils.array_to_string_with_specified_style(tmp_req.layout_specified_users, 'LayoutSpecifiedUsers', 'json')
        query = {}
        if not DaraCore.is_null(request.annotation):
            query['Annotation'] = request.annotation
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not DaraCore.is_null(request.bg_color):
            query['BgColor'] = request.bg_color
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not DaraCore.is_null(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not DaraCore.is_null(request.images):
            query['Images'] = request.images
        if not DaraCore.is_null(request.layout_specified_users_shrink):
            query['LayoutSpecifiedUsers'] = request.layout_specified_users_shrink
        if not DaraCore.is_null(request.panes):
            query['Panes'] = request.panes
        if not DaraCore.is_null(request.region_color):
            query['RegionColor'] = request.region_color
        if not DaraCore.is_null(request.reserve_pane_for_no_camera_user):
            query['ReservePaneForNoCameraUser'] = request.reserve_pane_for_no_camera_user
        if not DaraCore.is_null(request.show_default_background_on_mute):
            query['ShowDefaultBackgroundOnMute'] = request.show_default_background_on_mute
        if not DaraCore.is_null(request.spec_mixed_user_list):
            query['SpecMixedUserList'] = request.spec_mixed_user_list
        if not DaraCore.is_null(request.start_without_channel):
            query['StartWithoutChannel'] = request.start_without_channel
        if not DaraCore.is_null(request.start_without_channel_wait_time):
            query['StartWithoutChannelWaitTime'] = request.start_without_channel_wait_time
        if not DaraCore.is_null(request.sub_high_resolution_stream):
            query['SubHighResolutionStream'] = request.sub_high_resolution_stream
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.texts):
            query['Texts'] = request.texts
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartStreamingOut',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartStreamingOutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_streaming_out(
        self,
        request: main_models.StartStreamingOutRequest,
    ) -> main_models.StartStreamingOutResponse:
        runtime = RuntimeOptions()
        return self.start_streaming_out_with_options(request, runtime)

    async def start_streaming_out_async(
        self,
        request: main_models.StartStreamingOutRequest,
    ) -> main_models.StartStreamingOutResponse:
        runtime = RuntimeOptions()
        return await self.start_streaming_out_with_options_async(request, runtime)

    def start_view_with_options(
        self,
        tmp_req: main_models.StartViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartViewResponse:
        tmp_req.validate()
        request = main_models.StartViewShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.view_subscribers):
            request.view_subscribers_shrink = Utils.array_to_string_with_specified_style(tmp_req.view_subscribers, 'ViewSubscribers', 'simple')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.bg_color):
            query['BgColor'] = request.bg_color
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not DaraCore.is_null(request.region_color):
            query['RegionColor'] = request.region_color
        if not DaraCore.is_null(request.start_without_channel):
            query['StartWithoutChannel'] = request.start_without_channel
        if not DaraCore.is_null(request.start_without_channel_wait_time):
            query['StartWithoutChannelWaitTime'] = request.start_without_channel_wait_time
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.view_content):
            query['ViewContent'] = request.view_content
        if not DaraCore.is_null(request.view_subscribers_shrink):
            query['ViewSubscribers'] = request.view_subscribers_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartView',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_view_with_options_async(
        self,
        tmp_req: main_models.StartViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartViewResponse:
        tmp_req.validate()
        request = main_models.StartViewShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.view_subscribers):
            request.view_subscribers_shrink = Utils.array_to_string_with_specified_style(tmp_req.view_subscribers, 'ViewSubscribers', 'simple')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.bg_color):
            query['BgColor'] = request.bg_color
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not DaraCore.is_null(request.region_color):
            query['RegionColor'] = request.region_color
        if not DaraCore.is_null(request.start_without_channel):
            query['StartWithoutChannel'] = request.start_without_channel
        if not DaraCore.is_null(request.start_without_channel_wait_time):
            query['StartWithoutChannelWaitTime'] = request.start_without_channel_wait_time
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.view_content):
            query['ViewContent'] = request.view_content
        if not DaraCore.is_null(request.view_subscribers_shrink):
            query['ViewSubscribers'] = request.view_subscribers_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartView',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_view(
        self,
        request: main_models.StartViewRequest,
    ) -> main_models.StartViewResponse:
        runtime = RuntimeOptions()
        return self.start_view_with_options(request, runtime)

    async def start_view_async(
        self,
        request: main_models.StartViewRequest,
    ) -> main_models.StartViewResponse:
        runtime = RuntimeOptions()
        return await self.start_view_with_options_async(request, runtime)

    def stop_agent_with_options(
        self,
        request: main_models.StopAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopAgent',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_agent_with_options_async(
        self,
        request: main_models.StopAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopAgent',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_agent(
        self,
        request: main_models.StopAgentRequest,
    ) -> main_models.StopAgentResponse:
        runtime = RuntimeOptions()
        return self.stop_agent_with_options(request, runtime)

    async def stop_agent_async(
        self,
        request: main_models.StopAgentRequest,
    ) -> main_models.StopAgentResponse:
        runtime = RuntimeOptions()
        return await self.stop_agent_with_options_async(request, runtime)

    def stop_category_callback_with_options(
        self,
        tmp_req: main_models.StopCategoryCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopCategoryCallbackResponse:
        tmp_req.validate()
        request = main_models.StopCategoryCallbackShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.callback):
            request.callback_shrink = Utils.array_to_string_with_specified_style(tmp_req.callback, 'Callback', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.callback_shrink):
            query['Callback'] = request.callback_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopCategoryCallback',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopCategoryCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_category_callback_with_options_async(
        self,
        tmp_req: main_models.StopCategoryCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopCategoryCallbackResponse:
        tmp_req.validate()
        request = main_models.StopCategoryCallbackShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.callback):
            request.callback_shrink = Utils.array_to_string_with_specified_style(tmp_req.callback, 'Callback', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.callback_shrink):
            query['Callback'] = request.callback_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopCategoryCallback',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopCategoryCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_category_callback(
        self,
        request: main_models.StopCategoryCallbackRequest,
    ) -> main_models.StopCategoryCallbackResponse:
        runtime = RuntimeOptions()
        return self.stop_category_callback_with_options(request, runtime)

    async def stop_category_callback_async(
        self,
        request: main_models.StopCategoryCallbackRequest,
    ) -> main_models.StopCategoryCallbackResponse:
        runtime = RuntimeOptions()
        return await self.stop_category_callback_with_options_async(request, runtime)

    def stop_channel_with_options(
        self,
        request: main_models.StopChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopChannel',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_channel_with_options_async(
        self,
        request: main_models.StopChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopChannel',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_channel(
        self,
        request: main_models.StopChannelRequest,
    ) -> main_models.StopChannelResponse:
        runtime = RuntimeOptions()
        return self.stop_channel_with_options(request, runtime)

    async def stop_channel_async(
        self,
        request: main_models.StopChannelRequest,
    ) -> main_models.StopChannelResponse:
        runtime = RuntimeOptions()
        return await self.stop_channel_with_options_async(request, runtime)

    def stop_cloud_note_with_options(
        self,
        request: main_models.StopCloudNoteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopCloudNoteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopCloudNote',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopCloudNoteResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_cloud_note_with_options_async(
        self,
        request: main_models.StopCloudNoteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopCloudNoteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopCloudNote',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopCloudNoteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_cloud_note(
        self,
        request: main_models.StopCloudNoteRequest,
    ) -> main_models.StopCloudNoteResponse:
        runtime = RuntimeOptions()
        return self.stop_cloud_note_with_options(request, runtime)

    async def stop_cloud_note_async(
        self,
        request: main_models.StopCloudNoteRequest,
    ) -> main_models.StopCloudNoteResponse:
        runtime = RuntimeOptions()
        return await self.stop_cloud_note_with_options_async(request, runtime)

    def stop_cloud_record_with_options(
        self,
        request: main_models.StopCloudRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopCloudRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopCloudRecord',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopCloudRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_cloud_record_with_options_async(
        self,
        request: main_models.StopCloudRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopCloudRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopCloudRecord',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopCloudRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_cloud_record(
        self,
        request: main_models.StopCloudRecordRequest,
    ) -> main_models.StopCloudRecordResponse:
        runtime = RuntimeOptions()
        return self.stop_cloud_record_with_options(request, runtime)

    async def stop_cloud_record_async(
        self,
        request: main_models.StopCloudRecordRequest,
    ) -> main_models.StopCloudRecordResponse:
        runtime = RuntimeOptions()
        return await self.stop_cloud_record_with_options_async(request, runtime)

    def stop_mputask_with_options(
        self,
        request: main_models.StopMPUTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopMPUTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopMPUTask',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopMPUTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_mputask_with_options_async(
        self,
        request: main_models.StopMPUTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopMPUTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopMPUTask',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopMPUTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_mputask(
        self,
        request: main_models.StopMPUTaskRequest,
    ) -> main_models.StopMPUTaskResponse:
        runtime = RuntimeOptions()
        return self.stop_mputask_with_options(request, runtime)

    async def stop_mputask_async(
        self,
        request: main_models.StopMPUTaskRequest,
    ) -> main_models.StopMPUTaskResponse:
        runtime = RuntimeOptions()
        return await self.stop_mputask_with_options_async(request, runtime)

    def stop_record_task_with_options(
        self,
        request: main_models.StopRecordTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopRecordTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopRecordTask',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopRecordTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_record_task_with_options_async(
        self,
        request: main_models.StopRecordTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopRecordTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopRecordTask',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopRecordTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_record_task(
        self,
        request: main_models.StopRecordTaskRequest,
    ) -> main_models.StopRecordTaskResponse:
        runtime = RuntimeOptions()
        return self.stop_record_task_with_options(request, runtime)

    async def stop_record_task_async(
        self,
        request: main_models.StopRecordTaskRequest,
    ) -> main_models.StopRecordTaskResponse:
        runtime = RuntimeOptions()
        return await self.stop_record_task_with_options_async(request, runtime)

    def stop_streaming_out_with_options(
        self,
        request: main_models.StopStreamingOutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopStreamingOutResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopStreamingOut',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopStreamingOutResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_streaming_out_with_options_async(
        self,
        request: main_models.StopStreamingOutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopStreamingOutResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopStreamingOut',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopStreamingOutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_streaming_out(
        self,
        request: main_models.StopStreamingOutRequest,
    ) -> main_models.StopStreamingOutResponse:
        runtime = RuntimeOptions()
        return self.stop_streaming_out_with_options(request, runtime)

    async def stop_streaming_out_async(
        self,
        request: main_models.StopStreamingOutRequest,
    ) -> main_models.StopStreamingOutResponse:
        runtime = RuntimeOptions()
        return await self.stop_streaming_out_with_options_async(request, runtime)

    def stop_view_with_options(
        self,
        request: main_models.StopViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopView',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_view_with_options_async(
        self,
        request: main_models.StopViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopView',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_view(
        self,
        request: main_models.StopViewRequest,
    ) -> main_models.StopViewResponse:
        runtime = RuntimeOptions()
        return self.stop_view_with_options(request, runtime)

    async def stop_view_async(
        self,
        request: main_models.StopViewRequest,
    ) -> main_models.StopViewResponse:
        runtime = RuntimeOptions()
        return await self.stop_view_with_options_async(request, runtime)

    def update_agent_with_options(
        self,
        tmp_req: main_models.UpdateAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentResponse:
        tmp_req.validate()
        request = main_models.UpdateAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.voice_chat_config):
            request.voice_chat_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.voice_chat_config, 'VoiceChatConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.voice_chat_config_shrink):
            query['VoiceChatConfig'] = request.voice_chat_config_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgent',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_agent_with_options_async(
        self,
        tmp_req: main_models.UpdateAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentResponse:
        tmp_req.validate()
        request = main_models.UpdateAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.voice_chat_config):
            request.voice_chat_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.voice_chat_config, 'VoiceChatConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.voice_chat_config_shrink):
            query['VoiceChatConfig'] = request.voice_chat_config_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgent',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_agent(
        self,
        request: main_models.UpdateAgentRequest,
    ) -> main_models.UpdateAgentResponse:
        runtime = RuntimeOptions()
        return self.update_agent_with_options(request, runtime)

    async def update_agent_async(
        self,
        request: main_models.UpdateAgentRequest,
    ) -> main_models.UpdateAgentResponse:
        runtime = RuntimeOptions()
        return await self.update_agent_with_options_async(request, runtime)

    def update_auto_live_stream_rule_with_options(
        self,
        request: main_models.UpdateAutoLiveStreamRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAutoLiveStreamRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.call_back):
            query['CallBack'] = request.call_back
        if not DaraCore.is_null(request.channel_id_prefixes):
            query['ChannelIdPrefixes'] = request.channel_id_prefixes
        if not DaraCore.is_null(request.channel_ids):
            query['ChannelIds'] = request.channel_ids
        if not DaraCore.is_null(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAutoLiveStreamRule',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_auto_live_stream_rule_with_options_async(
        self,
        request: main_models.UpdateAutoLiveStreamRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAutoLiveStreamRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.call_back):
            query['CallBack'] = request.call_back
        if not DaraCore.is_null(request.channel_id_prefixes):
            query['ChannelIdPrefixes'] = request.channel_id_prefixes
        if not DaraCore.is_null(request.channel_ids):
            query['ChannelIds'] = request.channel_ids
        if not DaraCore.is_null(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAutoLiveStreamRule',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAutoLiveStreamRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_auto_live_stream_rule(
        self,
        request: main_models.UpdateAutoLiveStreamRuleRequest,
    ) -> main_models.UpdateAutoLiveStreamRuleResponse:
        runtime = RuntimeOptions()
        return self.update_auto_live_stream_rule_with_options(request, runtime)

    async def update_auto_live_stream_rule_async(
        self,
        request: main_models.UpdateAutoLiveStreamRuleRequest,
    ) -> main_models.UpdateAutoLiveStreamRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_auto_live_stream_rule_with_options_async(request, runtime)

    def update_cloud_record_with_options(
        self,
        tmp_req: main_models.UpdateCloudRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudRecordResponse:
        tmp_req.validate()
        request = main_models.UpdateCloudRecordShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.layout_specified_users):
            request.layout_specified_users_shrink = Utils.array_to_string_with_specified_style(tmp_req.layout_specified_users, 'LayoutSpecifiedUsers', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not DaraCore.is_null(request.images):
            query['Images'] = request.images
        if not DaraCore.is_null(request.layout_specified_users_shrink):
            query['LayoutSpecifiedUsers'] = request.layout_specified_users_shrink
        if not DaraCore.is_null(request.panes):
            query['Panes'] = request.panes
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.texts):
            query['Texts'] = request.texts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudRecord',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_record_with_options_async(
        self,
        tmp_req: main_models.UpdateCloudRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudRecordResponse:
        tmp_req.validate()
        request = main_models.UpdateCloudRecordShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.layout_specified_users):
            request.layout_specified_users_shrink = Utils.array_to_string_with_specified_style(tmp_req.layout_specified_users, 'LayoutSpecifiedUsers', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not DaraCore.is_null(request.images):
            query['Images'] = request.images
        if not DaraCore.is_null(request.layout_specified_users_shrink):
            query['LayoutSpecifiedUsers'] = request.layout_specified_users_shrink
        if not DaraCore.is_null(request.panes):
            query['Panes'] = request.panes
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.texts):
            query['Texts'] = request.texts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudRecord',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_record(
        self,
        request: main_models.UpdateCloudRecordRequest,
    ) -> main_models.UpdateCloudRecordResponse:
        runtime = RuntimeOptions()
        return self.update_cloud_record_with_options(request, runtime)

    async def update_cloud_record_async(
        self,
        request: main_models.UpdateCloudRecordRequest,
    ) -> main_models.UpdateCloudRecordResponse:
        runtime = RuntimeOptions()
        return await self.update_cloud_record_with_options_async(request, runtime)

    def update_mputask_with_options(
        self,
        request: main_models.UpdateMPUTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMPUTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not DaraCore.is_null(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not DaraCore.is_null(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not DaraCore.is_null(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not DaraCore.is_null(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not DaraCore.is_null(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not DaraCore.is_null(request.mix_mode):
            query['MixMode'] = request.mix_mode
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        if not DaraCore.is_null(request.sub_spec_audio_users):
            query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        if not DaraCore.is_null(request.sub_spec_camera_users):
            query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        if not DaraCore.is_null(request.sub_spec_share_screen_users):
            query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        if not DaraCore.is_null(request.sub_spec_users):
            query['SubSpecUsers'] = request.sub_spec_users
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.unsub_spec_audio_users):
            query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        if not DaraCore.is_null(request.unsub_spec_camera_users):
            query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        if not DaraCore.is_null(request.unsub_spec_share_screen_users):
            query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        if not DaraCore.is_null(request.user_panes):
            query['UserPanes'] = request.user_panes
        if not DaraCore.is_null(request.watermarks):
            query['Watermarks'] = request.watermarks
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMPUTask',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMPUTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mputask_with_options_async(
        self,
        request: main_models.UpdateMPUTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMPUTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not DaraCore.is_null(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not DaraCore.is_null(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not DaraCore.is_null(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not DaraCore.is_null(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not DaraCore.is_null(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not DaraCore.is_null(request.mix_mode):
            query['MixMode'] = request.mix_mode
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        if not DaraCore.is_null(request.sub_spec_audio_users):
            query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        if not DaraCore.is_null(request.sub_spec_camera_users):
            query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        if not DaraCore.is_null(request.sub_spec_share_screen_users):
            query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        if not DaraCore.is_null(request.sub_spec_users):
            query['SubSpecUsers'] = request.sub_spec_users
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.unsub_spec_audio_users):
            query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        if not DaraCore.is_null(request.unsub_spec_camera_users):
            query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        if not DaraCore.is_null(request.unsub_spec_share_screen_users):
            query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        if not DaraCore.is_null(request.user_panes):
            query['UserPanes'] = request.user_panes
        if not DaraCore.is_null(request.watermarks):
            query['Watermarks'] = request.watermarks
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMPUTask',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMPUTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mputask(
        self,
        request: main_models.UpdateMPUTaskRequest,
    ) -> main_models.UpdateMPUTaskResponse:
        runtime = RuntimeOptions()
        return self.update_mputask_with_options(request, runtime)

    async def update_mputask_async(
        self,
        request: main_models.UpdateMPUTaskRequest,
    ) -> main_models.UpdateMPUTaskResponse:
        runtime = RuntimeOptions()
        return await self.update_mputask_with_options_async(request, runtime)

    def update_record_task_with_options(
        self,
        request: main_models.UpdateRecordTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecordTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not DaraCore.is_null(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not DaraCore.is_null(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.sub_spec_audio_users):
            query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        if not DaraCore.is_null(request.sub_spec_camera_users):
            query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        if not DaraCore.is_null(request.sub_spec_share_screen_users):
            query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        if not DaraCore.is_null(request.sub_spec_users):
            query['SubSpecUsers'] = request.sub_spec_users
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_profile):
            query['TaskProfile'] = request.task_profile
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.unsub_spec_audio_users):
            query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        if not DaraCore.is_null(request.unsub_spec_camera_users):
            query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        if not DaraCore.is_null(request.unsub_spec_share_screen_users):
            query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        if not DaraCore.is_null(request.user_panes):
            query['UserPanes'] = request.user_panes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecordTask',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecordTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_record_task_with_options_async(
        self,
        request: main_models.UpdateRecordTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecordTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not DaraCore.is_null(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not DaraCore.is_null(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.sub_spec_audio_users):
            query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        if not DaraCore.is_null(request.sub_spec_camera_users):
            query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        if not DaraCore.is_null(request.sub_spec_share_screen_users):
            query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        if not DaraCore.is_null(request.sub_spec_users):
            query['SubSpecUsers'] = request.sub_spec_users
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_profile):
            query['TaskProfile'] = request.task_profile
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.unsub_spec_audio_users):
            query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        if not DaraCore.is_null(request.unsub_spec_camera_users):
            query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        if not DaraCore.is_null(request.unsub_spec_share_screen_users):
            query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        if not DaraCore.is_null(request.user_panes):
            query['UserPanes'] = request.user_panes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecordTask',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecordTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_record_task(
        self,
        request: main_models.UpdateRecordTaskRequest,
    ) -> main_models.UpdateRecordTaskResponse:
        runtime = RuntimeOptions()
        return self.update_record_task_with_options(request, runtime)

    async def update_record_task_async(
        self,
        request: main_models.UpdateRecordTaskRequest,
    ) -> main_models.UpdateRecordTaskResponse:
        runtime = RuntimeOptions()
        return await self.update_record_task_with_options_async(request, runtime)

    def update_record_template_with_options(
        self,
        request: main_models.UpdateRecordTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecordTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not DaraCore.is_null(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not DaraCore.is_null(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not DaraCore.is_null(request.delay_stop_time):
            query['DelayStopTime'] = request.delay_stop_time
        if not DaraCore.is_null(request.enable_m3u_8date_time):
            query['EnableM3u8DateTime'] = request.enable_m3u_8date_time
        if not DaraCore.is_null(request.file_split_interval):
            query['FileSplitInterval'] = request.file_split_interval
        if not DaraCore.is_null(request.formats):
            query['Formats'] = request.formats
        if not DaraCore.is_null(request.http_callback_url):
            query['HttpCallbackUrl'] = request.http_callback_url
        if not DaraCore.is_null(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not DaraCore.is_null(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not DaraCore.is_null(request.mns_queue):
            query['MnsQueue'] = request.mns_queue
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not DaraCore.is_null(request.oss_file_prefix):
            query['OssFilePrefix'] = request.oss_file_prefix
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.task_profile):
            query['TaskProfile'] = request.task_profile
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.watermarks):
            query['Watermarks'] = request.watermarks
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecordTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_record_template_with_options_async(
        self,
        request: main_models.UpdateRecordTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecordTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not DaraCore.is_null(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not DaraCore.is_null(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not DaraCore.is_null(request.delay_stop_time):
            query['DelayStopTime'] = request.delay_stop_time
        if not DaraCore.is_null(request.enable_m3u_8date_time):
            query['EnableM3u8DateTime'] = request.enable_m3u_8date_time
        if not DaraCore.is_null(request.file_split_interval):
            query['FileSplitInterval'] = request.file_split_interval
        if not DaraCore.is_null(request.formats):
            query['Formats'] = request.formats
        if not DaraCore.is_null(request.http_callback_url):
            query['HttpCallbackUrl'] = request.http_callback_url
        if not DaraCore.is_null(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not DaraCore.is_null(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not DaraCore.is_null(request.mns_queue):
            query['MnsQueue'] = request.mns_queue
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not DaraCore.is_null(request.oss_file_prefix):
            query['OssFilePrefix'] = request.oss_file_prefix
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.task_profile):
            query['TaskProfile'] = request.task_profile
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.watermarks):
            query['Watermarks'] = request.watermarks
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecordTemplate',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecordTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_record_template(
        self,
        request: main_models.UpdateRecordTemplateRequest,
    ) -> main_models.UpdateRecordTemplateResponse:
        runtime = RuntimeOptions()
        return self.update_record_template_with_options(request, runtime)

    async def update_record_template_async(
        self,
        request: main_models.UpdateRecordTemplateRequest,
    ) -> main_models.UpdateRecordTemplateResponse:
        runtime = RuntimeOptions()
        return await self.update_record_template_with_options_async(request, runtime)

    def update_streaming_out_with_options(
        self,
        tmp_req: main_models.UpdateStreamingOutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStreamingOutResponse:
        tmp_req.validate()
        request = main_models.UpdateStreamingOutShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.layout_specified_users):
            request.layout_specified_users_shrink = Utils.array_to_string_with_specified_style(tmp_req.layout_specified_users, 'LayoutSpecifiedUsers', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not DaraCore.is_null(request.bg_color):
            query['BgColor'] = request.bg_color
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not DaraCore.is_null(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not DaraCore.is_null(request.images):
            query['Images'] = request.images
        if not DaraCore.is_null(request.layout_specified_users_shrink):
            query['LayoutSpecifiedUsers'] = request.layout_specified_users_shrink
        if not DaraCore.is_null(request.panes):
            query['Panes'] = request.panes
        if not DaraCore.is_null(request.region_color):
            query['RegionColor'] = request.region_color
        if not DaraCore.is_null(request.spec_mixed_user_list):
            query['SpecMixedUserList'] = request.spec_mixed_user_list
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.texts):
            query['Texts'] = request.texts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStreamingOut',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStreamingOutResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_streaming_out_with_options_async(
        self,
        tmp_req: main_models.UpdateStreamingOutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStreamingOutResponse:
        tmp_req.validate()
        request = main_models.UpdateStreamingOutShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.layout_specified_users):
            request.layout_specified_users_shrink = Utils.array_to_string_with_specified_style(tmp_req.layout_specified_users, 'LayoutSpecifiedUsers', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not DaraCore.is_null(request.bg_color):
            query['BgColor'] = request.bg_color
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not DaraCore.is_null(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not DaraCore.is_null(request.images):
            query['Images'] = request.images
        if not DaraCore.is_null(request.layout_specified_users_shrink):
            query['LayoutSpecifiedUsers'] = request.layout_specified_users_shrink
        if not DaraCore.is_null(request.panes):
            query['Panes'] = request.panes
        if not DaraCore.is_null(request.region_color):
            query['RegionColor'] = request.region_color
        if not DaraCore.is_null(request.spec_mixed_user_list):
            query['SpecMixedUserList'] = request.spec_mixed_user_list
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.texts):
            query['Texts'] = request.texts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStreamingOut',
            version = '2018-01-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStreamingOutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_streaming_out(
        self,
        request: main_models.UpdateStreamingOutRequest,
    ) -> main_models.UpdateStreamingOutResponse:
        runtime = RuntimeOptions()
        return self.update_streaming_out_with_options(request, runtime)

    async def update_streaming_out_async(
        self,
        request: main_models.UpdateStreamingOutRequest,
    ) -> main_models.UpdateStreamingOutResponse:
        runtime = RuntimeOptions()
        return await self.update_streaming_out_with_options_async(request, runtime)
