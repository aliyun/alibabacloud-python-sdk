# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_outboundbot20251111 import models as main_models
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
            'cn-shanghai': 'outboundbot.cn-shanghai.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('outboundbot', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_clone_voice_with_options(
        self,
        request: main_models.CreateCloneVoiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloneVoiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_key):
            body['FileKey'] = request.file_key
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloneVoice',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloneVoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_clone_voice_with_options_async(
        self,
        request: main_models.CreateCloneVoiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloneVoiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_key):
            body['FileKey'] = request.file_key
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloneVoice',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloneVoiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_clone_voice(
        self,
        request: main_models.CreateCloneVoiceRequest,
    ) -> main_models.CreateCloneVoiceResponse:
        runtime = RuntimeOptions()
        return self.create_clone_voice_with_options(request, runtime)

    async def create_clone_voice_async(
        self,
        request: main_models.CreateCloneVoiceRequest,
    ) -> main_models.CreateCloneVoiceResponse:
        runtime = RuntimeOptions()
        return await self.create_clone_voice_with_options_async(request, runtime)

    def create_flash_sms_access_profile_with_options(
        self,
        tmp_req: main_models.CreateFlashSmsAccessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFlashSmsAccessProfileResponse:
        tmp_req.validate()
        request = main_models.CreateFlashSmsAccessProfileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.access_profile):
            request.access_profile_shrink = Utils.array_to_string_with_specified_style(tmp_req.access_profile, 'AccessProfile', 'json')
        body = {}
        if not DaraCore.is_null(request.access_profile_shrink):
            body['AccessProfile'] = request.access_profile_shrink
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.provider_id):
            body['ProviderId'] = request.provider_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFlashSmsAccessProfile',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFlashSmsAccessProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flash_sms_access_profile_with_options_async(
        self,
        tmp_req: main_models.CreateFlashSmsAccessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFlashSmsAccessProfileResponse:
        tmp_req.validate()
        request = main_models.CreateFlashSmsAccessProfileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.access_profile):
            request.access_profile_shrink = Utils.array_to_string_with_specified_style(tmp_req.access_profile, 'AccessProfile', 'json')
        body = {}
        if not DaraCore.is_null(request.access_profile_shrink):
            body['AccessProfile'] = request.access_profile_shrink
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.provider_id):
            body['ProviderId'] = request.provider_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFlashSmsAccessProfile',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFlashSmsAccessProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flash_sms_access_profile(
        self,
        request: main_models.CreateFlashSmsAccessProfileRequest,
    ) -> main_models.CreateFlashSmsAccessProfileResponse:
        runtime = RuntimeOptions()
        return self.create_flash_sms_access_profile_with_options(request, runtime)

    async def create_flash_sms_access_profile_async(
        self,
        request: main_models.CreateFlashSmsAccessProfileRequest,
    ) -> main_models.CreateFlashSmsAccessProfileResponse:
        runtime = RuntimeOptions()
        return await self.create_flash_sms_access_profile_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: main_models.CreateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.concurrency):
            body['Concurrency'] = request.concurrency
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.service_mode):
            body['ServiceMode'] = request.service_mode
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: main_models.CreateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.concurrency):
            body['Concurrency'] = request.concurrency
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.service_mode):
            body['ServiceMode'] = request.service_mode
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_outbound_call_restriction_with_options(
        self,
        tmp_req: main_models.CreateOutboundCallRestrictionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOutboundCallRestrictionResponse:
        tmp_req.validate()
        request = main_models.CreateOutboundCallRestrictionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.outbound_call_restriction):
            request.outbound_call_restriction_shrink = Utils.array_to_string_with_specified_style(tmp_req.outbound_call_restriction, 'OutboundCallRestriction', 'json')
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.outbound_call_restriction_shrink):
            body['OutboundCallRestriction'] = request.outbound_call_restriction_shrink
        if not DaraCore.is_null(request.policy):
            body['Policy'] = request.policy
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOutboundCallRestriction',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOutboundCallRestrictionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_outbound_call_restriction_with_options_async(
        self,
        tmp_req: main_models.CreateOutboundCallRestrictionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOutboundCallRestrictionResponse:
        tmp_req.validate()
        request = main_models.CreateOutboundCallRestrictionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.outbound_call_restriction):
            request.outbound_call_restriction_shrink = Utils.array_to_string_with_specified_style(tmp_req.outbound_call_restriction, 'OutboundCallRestriction', 'json')
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.outbound_call_restriction_shrink):
            body['OutboundCallRestriction'] = request.outbound_call_restriction_shrink
        if not DaraCore.is_null(request.policy):
            body['Policy'] = request.policy
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOutboundCallRestriction',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOutboundCallRestrictionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_outbound_call_restriction(
        self,
        request: main_models.CreateOutboundCallRestrictionRequest,
    ) -> main_models.CreateOutboundCallRestrictionResponse:
        runtime = RuntimeOptions()
        return self.create_outbound_call_restriction_with_options(request, runtime)

    async def create_outbound_call_restriction_async(
        self,
        request: main_models.CreateOutboundCallRestrictionRequest,
    ) -> main_models.CreateOutboundCallRestrictionResponse:
        runtime = RuntimeOptions()
        return await self.create_outbound_call_restriction_with_options_async(request, runtime)

    def create_script_with_options(
        self,
        request: main_models.CreateScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScriptResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.nlu_engine):
            body['NluEngine'] = request.nlu_engine
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateScript',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_script_with_options_async(
        self,
        request: main_models.CreateScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScriptResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.nlu_engine):
            body['NluEngine'] = request.nlu_engine
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateScript',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_script(
        self,
        request: main_models.CreateScriptRequest,
    ) -> main_models.CreateScriptResponse:
        runtime = RuntimeOptions()
        return self.create_script_with_options(request, runtime)

    async def create_script_async(
        self,
        request: main_models.CreateScriptRequest,
    ) -> main_models.CreateScriptResponse:
        runtime = RuntimeOptions()
        return await self.create_script_with_options_async(request, runtime)

    def create_script_version_with_options(
        self,
        tmp_req: main_models.CreateScriptVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScriptVersionResponse:
        tmp_req.validate()
        request = main_models.CreateScriptVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.interaction_config):
            request.interaction_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.interaction_config, 'InteractionConfig', 'json')
        if not DaraCore.is_null(tmp_req.label_configs):
            request.label_configs_shrink = Utils.array_to_string_with_specified_style(tmp_req.label_configs, 'LabelConfigs', 'json')
        if not DaraCore.is_null(tmp_req.script_profile):
            request.script_profile_shrink = Utils.array_to_string_with_specified_style(tmp_req.script_profile, 'ScriptProfile', 'json')
        if not DaraCore.is_null(tmp_req.synthesizer_config):
            request.synthesizer_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.synthesizer_config, 'SynthesizerConfig', 'json')
        if not DaraCore.is_null(tmp_req.transcriber_config):
            request.transcriber_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.transcriber_config, 'TranscriberConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interaction_config_shrink):
            body['InteractionConfig'] = request.interaction_config_shrink
        if not DaraCore.is_null(request.label_configs_shrink):
            body['LabelConfigs'] = request.label_configs_shrink
        if not DaraCore.is_null(request.script_id):
            body['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.script_profile_shrink):
            body['ScriptProfile'] = request.script_profile_shrink
        if not DaraCore.is_null(request.source_version_id):
            body['SourceVersionId'] = request.source_version_id
        if not DaraCore.is_null(request.synthesizer_config_shrink):
            body['SynthesizerConfig'] = request.synthesizer_config_shrink
        if not DaraCore.is_null(request.transcriber_config_shrink):
            body['TranscriberConfig'] = request.transcriber_config_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateScriptVersion',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScriptVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_script_version_with_options_async(
        self,
        tmp_req: main_models.CreateScriptVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScriptVersionResponse:
        tmp_req.validate()
        request = main_models.CreateScriptVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.interaction_config):
            request.interaction_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.interaction_config, 'InteractionConfig', 'json')
        if not DaraCore.is_null(tmp_req.label_configs):
            request.label_configs_shrink = Utils.array_to_string_with_specified_style(tmp_req.label_configs, 'LabelConfigs', 'json')
        if not DaraCore.is_null(tmp_req.script_profile):
            request.script_profile_shrink = Utils.array_to_string_with_specified_style(tmp_req.script_profile, 'ScriptProfile', 'json')
        if not DaraCore.is_null(tmp_req.synthesizer_config):
            request.synthesizer_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.synthesizer_config, 'SynthesizerConfig', 'json')
        if not DaraCore.is_null(tmp_req.transcriber_config):
            request.transcriber_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.transcriber_config, 'TranscriberConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interaction_config_shrink):
            body['InteractionConfig'] = request.interaction_config_shrink
        if not DaraCore.is_null(request.label_configs_shrink):
            body['LabelConfigs'] = request.label_configs_shrink
        if not DaraCore.is_null(request.script_id):
            body['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.script_profile_shrink):
            body['ScriptProfile'] = request.script_profile_shrink
        if not DaraCore.is_null(request.source_version_id):
            body['SourceVersionId'] = request.source_version_id
        if not DaraCore.is_null(request.synthesizer_config_shrink):
            body['SynthesizerConfig'] = request.synthesizer_config_shrink
        if not DaraCore.is_null(request.transcriber_config_shrink):
            body['TranscriberConfig'] = request.transcriber_config_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateScriptVersion',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScriptVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_script_version(
        self,
        request: main_models.CreateScriptVersionRequest,
    ) -> main_models.CreateScriptVersionResponse:
        runtime = RuntimeOptions()
        return self.create_script_version_with_options(request, runtime)

    async def create_script_version_async(
        self,
        request: main_models.CreateScriptVersionRequest,
    ) -> main_models.CreateScriptVersionResponse:
        runtime = RuntimeOptions()
        return await self.create_script_version_with_options_async(request, runtime)

    def create_voice_access_profile_with_options(
        self,
        tmp_req: main_models.CreateVoiceAccessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVoiceAccessProfileResponse:
        tmp_req.validate()
        request = main_models.CreateVoiceAccessProfileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.profile):
            request.profile_shrink = Utils.array_to_string_with_specified_style(tmp_req.profile, 'Profile', 'json')
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nls_engine):
            body['NlsEngine'] = request.nls_engine
        if not DaraCore.is_null(request.profile_shrink):
            body['Profile'] = request.profile_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVoiceAccessProfile',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVoiceAccessProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_voice_access_profile_with_options_async(
        self,
        tmp_req: main_models.CreateVoiceAccessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVoiceAccessProfileResponse:
        tmp_req.validate()
        request = main_models.CreateVoiceAccessProfileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.profile):
            request.profile_shrink = Utils.array_to_string_with_specified_style(tmp_req.profile, 'Profile', 'json')
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nls_engine):
            body['NlsEngine'] = request.nls_engine
        if not DaraCore.is_null(request.profile_shrink):
            body['Profile'] = request.profile_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVoiceAccessProfile',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVoiceAccessProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_voice_access_profile(
        self,
        request: main_models.CreateVoiceAccessProfileRequest,
    ) -> main_models.CreateVoiceAccessProfileResponse:
        runtime = RuntimeOptions()
        return self.create_voice_access_profile_with_options(request, runtime)

    async def create_voice_access_profile_async(
        self,
        request: main_models.CreateVoiceAccessProfileRequest,
    ) -> main_models.CreateVoiceAccessProfileResponse:
        runtime = RuntimeOptions()
        return await self.create_voice_access_profile_with_options_async(request, runtime)

    def delete_clone_voice_with_options(
        self,
        request: main_models.DeleteCloneVoiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloneVoiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clone_voice_id):
            body['CloneVoiceId'] = request.clone_voice_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloneVoice',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloneVoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_clone_voice_with_options_async(
        self,
        request: main_models.DeleteCloneVoiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloneVoiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clone_voice_id):
            body['CloneVoiceId'] = request.clone_voice_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloneVoice',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloneVoiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_clone_voice(
        self,
        request: main_models.DeleteCloneVoiceRequest,
    ) -> main_models.DeleteCloneVoiceResponse:
        runtime = RuntimeOptions()
        return self.delete_clone_voice_with_options(request, runtime)

    async def delete_clone_voice_async(
        self,
        request: main_models.DeleteCloneVoiceRequest,
    ) -> main_models.DeleteCloneVoiceResponse:
        runtime = RuntimeOptions()
        return await self.delete_clone_voice_with_options_async(request, runtime)

    def delete_flash_sms_access_profile_with_options(
        self,
        request: main_models.DeleteFlashSmsAccessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFlashSmsAccessProfileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_profile_id):
            body['AccessProfileId'] = request.access_profile_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFlashSmsAccessProfile',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFlashSmsAccessProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flash_sms_access_profile_with_options_async(
        self,
        request: main_models.DeleteFlashSmsAccessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFlashSmsAccessProfileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_profile_id):
            body['AccessProfileId'] = request.access_profile_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFlashSmsAccessProfile',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFlashSmsAccessProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flash_sms_access_profile(
        self,
        request: main_models.DeleteFlashSmsAccessProfileRequest,
    ) -> main_models.DeleteFlashSmsAccessProfileResponse:
        runtime = RuntimeOptions()
        return self.delete_flash_sms_access_profile_with_options(request, runtime)

    async def delete_flash_sms_access_profile_async(
        self,
        request: main_models.DeleteFlashSmsAccessProfileRequest,
    ) -> main_models.DeleteFlashSmsAccessProfileResponse:
        runtime = RuntimeOptions()
        return await self.delete_flash_sms_access_profile_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: main_models.DeleteInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: main_models.DeleteInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_outbound_call_restriction_with_options(
        self,
        tmp_req: main_models.DeleteOutboundCallRestrictionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOutboundCallRestrictionResponse:
        tmp_req.validate()
        request = main_models.DeleteOutboundCallRestrictionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.restriction_id_list):
            request.restriction_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.restriction_id_list, 'RestrictionIdList', 'json')
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.restriction_id_list_shrink):
            body['RestrictionIdList'] = request.restriction_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOutboundCallRestriction',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOutboundCallRestrictionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_outbound_call_restriction_with_options_async(
        self,
        tmp_req: main_models.DeleteOutboundCallRestrictionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOutboundCallRestrictionResponse:
        tmp_req.validate()
        request = main_models.DeleteOutboundCallRestrictionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.restriction_id_list):
            request.restriction_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.restriction_id_list, 'RestrictionIdList', 'json')
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.restriction_id_list_shrink):
            body['RestrictionIdList'] = request.restriction_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOutboundCallRestriction',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOutboundCallRestrictionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_outbound_call_restriction(
        self,
        request: main_models.DeleteOutboundCallRestrictionRequest,
    ) -> main_models.DeleteOutboundCallRestrictionResponse:
        runtime = RuntimeOptions()
        return self.delete_outbound_call_restriction_with_options(request, runtime)

    async def delete_outbound_call_restriction_async(
        self,
        request: main_models.DeleteOutboundCallRestrictionRequest,
    ) -> main_models.DeleteOutboundCallRestrictionResponse:
        runtime = RuntimeOptions()
        return await self.delete_outbound_call_restriction_with_options_async(request, runtime)

    def delete_script_with_options(
        self,
        request: main_models.DeleteScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScriptResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            body['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScript',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_script_with_options_async(
        self,
        request: main_models.DeleteScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScriptResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            body['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScript',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_script(
        self,
        request: main_models.DeleteScriptRequest,
    ) -> main_models.DeleteScriptResponse:
        runtime = RuntimeOptions()
        return self.delete_script_with_options(request, runtime)

    async def delete_script_async(
        self,
        request: main_models.DeleteScriptRequest,
    ) -> main_models.DeleteScriptResponse:
        runtime = RuntimeOptions()
        return await self.delete_script_with_options_async(request, runtime)

    def delete_voice_access_profile_with_options(
        self,
        request: main_models.DeleteVoiceAccessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVoiceAccessProfileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_profile_id):
            body['AccessProfileId'] = request.access_profile_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVoiceAccessProfile',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVoiceAccessProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_voice_access_profile_with_options_async(
        self,
        request: main_models.DeleteVoiceAccessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVoiceAccessProfileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_profile_id):
            body['AccessProfileId'] = request.access_profile_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVoiceAccessProfile',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVoiceAccessProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_voice_access_profile(
        self,
        request: main_models.DeleteVoiceAccessProfileRequest,
    ) -> main_models.DeleteVoiceAccessProfileResponse:
        runtime = RuntimeOptions()
        return self.delete_voice_access_profile_with_options(request, runtime)

    async def delete_voice_access_profile_async(
        self,
        request: main_models.DeleteVoiceAccessProfileRequest,
    ) -> main_models.DeleteVoiceAccessProfileResponse:
        runtime = RuntimeOptions()
        return await self.delete_voice_access_profile_with_options_async(request, runtime)

    def disable_subscription_with_options(
        self,
        request: main_models.DisableSubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableSubscriptionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisableSubscription',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_subscription_with_options_async(
        self,
        request: main_models.DisableSubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableSubscriptionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisableSubscription',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_subscription(
        self,
        request: main_models.DisableSubscriptionRequest,
    ) -> main_models.DisableSubscriptionResponse:
        runtime = RuntimeOptions()
        return self.disable_subscription_with_options(request, runtime)

    async def disable_subscription_async(
        self,
        request: main_models.DisableSubscriptionRequest,
    ) -> main_models.DisableSubscriptionResponse:
        runtime = RuntimeOptions()
        return await self.disable_subscription_with_options_async(request, runtime)

    def get_instance_with_options(
        self,
        request: main_models.GetInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        request: main_models.GetInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        request: main_models.GetInstanceRequest,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    async def get_instance_async(
        self,
        request: main_models.GetInstanceRequest,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_with_options_async(request, runtime)

    def get_script_profile_template_with_options(
        self,
        request: main_models.GetScriptProfileTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScriptProfileTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetScriptProfileTemplate',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScriptProfileTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_script_profile_template_with_options_async(
        self,
        request: main_models.GetScriptProfileTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScriptProfileTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetScriptProfileTemplate',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScriptProfileTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_script_profile_template(
        self,
        request: main_models.GetScriptProfileTemplateRequest,
    ) -> main_models.GetScriptProfileTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_script_profile_template_with_options(request, runtime)

    async def get_script_profile_template_async(
        self,
        request: main_models.GetScriptProfileTemplateRequest,
    ) -> main_models.GetScriptProfileTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_script_profile_template_with_options_async(request, runtime)

    def get_subscription_with_options(
        self,
        request: main_models.GetSubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSubscriptionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSubscription',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_subscription_with_options_async(
        self,
        request: main_models.GetSubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSubscriptionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSubscription',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_subscription(
        self,
        request: main_models.GetSubscriptionRequest,
    ) -> main_models.GetSubscriptionResponse:
        runtime = RuntimeOptions()
        return self.get_subscription_with_options(request, runtime)

    async def get_subscription_async(
        self,
        request: main_models.GetSubscriptionRequest,
    ) -> main_models.GetSubscriptionResponse:
        runtime = RuntimeOptions()
        return await self.get_subscription_with_options_async(request, runtime)

    def list_clone_voice_models_with_options(
        self,
        request: main_models.ListCloneVoiceModelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloneVoiceModelsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCloneVoiceModels',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloneVoiceModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clone_voice_models_with_options_async(
        self,
        request: main_models.ListCloneVoiceModelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloneVoiceModelsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCloneVoiceModels',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloneVoiceModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_clone_voice_models(
        self,
        request: main_models.ListCloneVoiceModelsRequest,
    ) -> main_models.ListCloneVoiceModelsResponse:
        runtime = RuntimeOptions()
        return self.list_clone_voice_models_with_options(request, runtime)

    async def list_clone_voice_models_async(
        self,
        request: main_models.ListCloneVoiceModelsRequest,
    ) -> main_models.ListCloneVoiceModelsResponse:
        runtime = RuntimeOptions()
        return await self.list_clone_voice_models_with_options_async(request, runtime)

    def list_clone_voices_with_options(
        self,
        request: main_models.ListCloneVoicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloneVoicesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCloneVoices',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloneVoicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clone_voices_with_options_async(
        self,
        request: main_models.ListCloneVoicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloneVoicesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCloneVoices',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloneVoicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_clone_voices(
        self,
        request: main_models.ListCloneVoicesRequest,
    ) -> main_models.ListCloneVoicesResponse:
        runtime = RuntimeOptions()
        return self.list_clone_voices_with_options(request, runtime)

    async def list_clone_voices_async(
        self,
        request: main_models.ListCloneVoicesRequest,
    ) -> main_models.ListCloneVoicesResponse:
        runtime = RuntimeOptions()
        return await self.list_clone_voices_with_options_async(request, runtime)

    def list_flash_sms_access_profiles_with_options(
        self,
        request: main_models.ListFlashSmsAccessProfilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlashSmsAccessProfilesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFlashSmsAccessProfiles',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlashSmsAccessProfilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flash_sms_access_profiles_with_options_async(
        self,
        request: main_models.ListFlashSmsAccessProfilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlashSmsAccessProfilesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFlashSmsAccessProfiles',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlashSmsAccessProfilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flash_sms_access_profiles(
        self,
        request: main_models.ListFlashSmsAccessProfilesRequest,
    ) -> main_models.ListFlashSmsAccessProfilesResponse:
        runtime = RuntimeOptions()
        return self.list_flash_sms_access_profiles_with_options(request, runtime)

    async def list_flash_sms_access_profiles_async(
        self,
        request: main_models.ListFlashSmsAccessProfilesRequest,
    ) -> main_models.ListFlashSmsAccessProfilesResponse:
        runtime = RuntimeOptions()
        return await self.list_flash_sms_access_profiles_with_options_async(request, runtime)

    def list_flash_sms_providers_with_options(
        self,
        request: main_models.ListFlashSmsProvidersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlashSmsProvidersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFlashSmsProviders',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlashSmsProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flash_sms_providers_with_options_async(
        self,
        request: main_models.ListFlashSmsProvidersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlashSmsProvidersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFlashSmsProviders',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlashSmsProvidersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flash_sms_providers(
        self,
        request: main_models.ListFlashSmsProvidersRequest,
    ) -> main_models.ListFlashSmsProvidersResponse:
        runtime = RuntimeOptions()
        return self.list_flash_sms_providers_with_options(request, runtime)

    async def list_flash_sms_providers_async(
        self,
        request: main_models.ListFlashSmsProvidersRequest,
    ) -> main_models.ListFlashSmsProvidersResponse:
        runtime = RuntimeOptions()
        return await self.list_flash_sms_providers_with_options_async(request, runtime)

    def list_flash_sms_templates_with_options(
        self,
        request: main_models.ListFlashSmsTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlashSmsTemplatesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.provider_id):
            body['ProviderId'] = request.provider_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFlashSmsTemplates',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlashSmsTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flash_sms_templates_with_options_async(
        self,
        request: main_models.ListFlashSmsTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlashSmsTemplatesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.provider_id):
            body['ProviderId'] = request.provider_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFlashSmsTemplates',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlashSmsTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flash_sms_templates(
        self,
        request: main_models.ListFlashSmsTemplatesRequest,
    ) -> main_models.ListFlashSmsTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_flash_sms_templates_with_options(request, runtime)

    async def list_flash_sms_templates_async(
        self,
        request: main_models.ListFlashSmsTemplatesRequest,
    ) -> main_models.ListFlashSmsTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_flash_sms_templates_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: main_models.ListInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: main_models.ListInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def list_outbound_call_restrictions_with_options(
        self,
        request: main_models.ListOutboundCallRestrictionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOutboundCallRestrictionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy):
            body['Policy'] = request.policy
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListOutboundCallRestrictions',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOutboundCallRestrictionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_outbound_call_restrictions_with_options_async(
        self,
        request: main_models.ListOutboundCallRestrictionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOutboundCallRestrictionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy):
            body['Policy'] = request.policy
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListOutboundCallRestrictions',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOutboundCallRestrictionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_outbound_call_restrictions(
        self,
        request: main_models.ListOutboundCallRestrictionsRequest,
    ) -> main_models.ListOutboundCallRestrictionsResponse:
        runtime = RuntimeOptions()
        return self.list_outbound_call_restrictions_with_options(request, runtime)

    async def list_outbound_call_restrictions_async(
        self,
        request: main_models.ListOutboundCallRestrictionsRequest,
    ) -> main_models.ListOutboundCallRestrictionsResponse:
        runtime = RuntimeOptions()
        return await self.list_outbound_call_restrictions_with_options_async(request, runtime)

    def list_script_profile_templates_with_options(
        self,
        request: main_models.ListScriptProfileTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScriptProfileTemplatesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nlu_engine):
            body['NluEngine'] = request.nlu_engine
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListScriptProfileTemplates',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScriptProfileTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_script_profile_templates_with_options_async(
        self,
        request: main_models.ListScriptProfileTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScriptProfileTemplatesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nlu_engine):
            body['NluEngine'] = request.nlu_engine
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListScriptProfileTemplates',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScriptProfileTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_script_profile_templates(
        self,
        request: main_models.ListScriptProfileTemplatesRequest,
    ) -> main_models.ListScriptProfileTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_script_profile_templates_with_options(request, runtime)

    async def list_script_profile_templates_async(
        self,
        request: main_models.ListScriptProfileTemplatesRequest,
    ) -> main_models.ListScriptProfileTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_script_profile_templates_with_options_async(request, runtime)

    def list_scripts_with_options(
        self,
        tmp_req: main_models.ListScriptsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScriptsResponse:
        tmp_req.validate()
        request = main_models.ListScriptsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.script_ids):
            request.script_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.script_ids, 'ScriptIds', 'json')
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.publish_only):
            body['PublishOnly'] = request.publish_only
        if not DaraCore.is_null(request.script_ids_shrink):
            body['ScriptIds'] = request.script_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListScripts',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scripts_with_options_async(
        self,
        tmp_req: main_models.ListScriptsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScriptsResponse:
        tmp_req.validate()
        request = main_models.ListScriptsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.script_ids):
            request.script_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.script_ids, 'ScriptIds', 'json')
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.publish_only):
            body['PublishOnly'] = request.publish_only
        if not DaraCore.is_null(request.script_ids_shrink):
            body['ScriptIds'] = request.script_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListScripts',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScriptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scripts(
        self,
        request: main_models.ListScriptsRequest,
    ) -> main_models.ListScriptsResponse:
        runtime = RuntimeOptions()
        return self.list_scripts_with_options(request, runtime)

    async def list_scripts_async(
        self,
        request: main_models.ListScriptsRequest,
    ) -> main_models.ListScriptsResponse:
        runtime = RuntimeOptions()
        return await self.list_scripts_with_options_async(request, runtime)

    def list_scripts_by_flow_with_options(
        self,
        request: main_models.ListScriptsByFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScriptsByFlowResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.flow_id):
            body['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListScriptsByFlow',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScriptsByFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scripts_by_flow_with_options_async(
        self,
        request: main_models.ListScriptsByFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScriptsByFlowResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.flow_id):
            body['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListScriptsByFlow',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScriptsByFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scripts_by_flow(
        self,
        request: main_models.ListScriptsByFlowRequest,
    ) -> main_models.ListScriptsByFlowResponse:
        runtime = RuntimeOptions()
        return self.list_scripts_by_flow_with_options(request, runtime)

    async def list_scripts_by_flow_async(
        self,
        request: main_models.ListScriptsByFlowRequest,
    ) -> main_models.ListScriptsByFlowResponse:
        runtime = RuntimeOptions()
        return await self.list_scripts_by_flow_with_options_async(request, runtime)

    def list_system_configs_with_options(
        self,
        request: main_models.ListSystemConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSystemConfigsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.object_id):
            body['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.object_type):
            body['ObjectType'] = request.object_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSystemConfigs',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSystemConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_system_configs_with_options_async(
        self,
        request: main_models.ListSystemConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSystemConfigsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.object_id):
            body['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.object_type):
            body['ObjectType'] = request.object_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSystemConfigs',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSystemConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_system_configs(
        self,
        request: main_models.ListSystemConfigsRequest,
    ) -> main_models.ListSystemConfigsResponse:
        runtime = RuntimeOptions()
        return self.list_system_configs_with_options(request, runtime)

    async def list_system_configs_async(
        self,
        request: main_models.ListSystemConfigsRequest,
    ) -> main_models.ListSystemConfigsResponse:
        runtime = RuntimeOptions()
        return await self.list_system_configs_with_options_async(request, runtime)

    def list_voice_access_profiles_with_options(
        self,
        request: main_models.ListVoiceAccessProfilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVoiceAccessProfilesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVoiceAccessProfiles',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVoiceAccessProfilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_voice_access_profiles_with_options_async(
        self,
        request: main_models.ListVoiceAccessProfilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVoiceAccessProfilesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVoiceAccessProfiles',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVoiceAccessProfilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_voice_access_profiles(
        self,
        request: main_models.ListVoiceAccessProfilesRequest,
    ) -> main_models.ListVoiceAccessProfilesResponse:
        runtime = RuntimeOptions()
        return self.list_voice_access_profiles_with_options(request, runtime)

    async def list_voice_access_profiles_async(
        self,
        request: main_models.ListVoiceAccessProfilesRequest,
    ) -> main_models.ListVoiceAccessProfilesResponse:
        runtime = RuntimeOptions()
        return await self.list_voice_access_profiles_with_options_async(request, runtime)

    def publish_script_with_options(
        self,
        request: main_models.PublishScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishScriptResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            body['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.version_id):
            body['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishScript',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_script_with_options_async(
        self,
        request: main_models.PublishScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishScriptResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            body['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.version_id):
            body['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishScript',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_script(
        self,
        request: main_models.PublishScriptRequest,
    ) -> main_models.PublishScriptResponse:
        runtime = RuntimeOptions()
        return self.publish_script_with_options(request, runtime)

    async def publish_script_async(
        self,
        request: main_models.PublishScriptRequest,
    ) -> main_models.PublishScriptResponse:
        runtime = RuntimeOptions()
        return await self.publish_script_with_options_async(request, runtime)

    def update_clone_voice_with_options(
        self,
        request: main_models.UpdateCloneVoiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloneVoiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clone_voice_id):
            body['CloneVoiceId'] = request.clone_voice_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloneVoice',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloneVoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_clone_voice_with_options_async(
        self,
        request: main_models.UpdateCloneVoiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloneVoiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clone_voice_id):
            body['CloneVoiceId'] = request.clone_voice_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloneVoice',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloneVoiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_clone_voice(
        self,
        request: main_models.UpdateCloneVoiceRequest,
    ) -> main_models.UpdateCloneVoiceResponse:
        runtime = RuntimeOptions()
        return self.update_clone_voice_with_options(request, runtime)

    async def update_clone_voice_async(
        self,
        request: main_models.UpdateCloneVoiceRequest,
    ) -> main_models.UpdateCloneVoiceResponse:
        runtime = RuntimeOptions()
        return await self.update_clone_voice_with_options_async(request, runtime)

    def update_flash_sms_access_profile_with_options(
        self,
        tmp_req: main_models.UpdateFlashSmsAccessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFlashSmsAccessProfileResponse:
        tmp_req.validate()
        request = main_models.UpdateFlashSmsAccessProfileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.access_profile):
            request.access_profile_shrink = Utils.array_to_string_with_specified_style(tmp_req.access_profile, 'AccessProfile', 'json')
        body = {}
        if not DaraCore.is_null(request.access_profile_shrink):
            body['AccessProfile'] = request.access_profile_shrink
        if not DaraCore.is_null(request.access_profile_id):
            body['AccessProfileId'] = request.access_profile_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.provider_id):
            body['ProviderId'] = request.provider_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFlashSmsAccessProfile',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFlashSmsAccessProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_flash_sms_access_profile_with_options_async(
        self,
        tmp_req: main_models.UpdateFlashSmsAccessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFlashSmsAccessProfileResponse:
        tmp_req.validate()
        request = main_models.UpdateFlashSmsAccessProfileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.access_profile):
            request.access_profile_shrink = Utils.array_to_string_with_specified_style(tmp_req.access_profile, 'AccessProfile', 'json')
        body = {}
        if not DaraCore.is_null(request.access_profile_shrink):
            body['AccessProfile'] = request.access_profile_shrink
        if not DaraCore.is_null(request.access_profile_id):
            body['AccessProfileId'] = request.access_profile_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.provider_id):
            body['ProviderId'] = request.provider_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFlashSmsAccessProfile',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFlashSmsAccessProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_flash_sms_access_profile(
        self,
        request: main_models.UpdateFlashSmsAccessProfileRequest,
    ) -> main_models.UpdateFlashSmsAccessProfileResponse:
        runtime = RuntimeOptions()
        return self.update_flash_sms_access_profile_with_options(request, runtime)

    async def update_flash_sms_access_profile_async(
        self,
        request: main_models.UpdateFlashSmsAccessProfileRequest,
    ) -> main_models.UpdateFlashSmsAccessProfileResponse:
        runtime = RuntimeOptions()
        return await self.update_flash_sms_access_profile_with_options_async(request, runtime)

    def update_instance_with_options(
        self,
        request: main_models.UpdateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.concurrency):
            body['Concurrency'] = request.concurrency
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        request: main_models.UpdateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.concurrency):
            body['Concurrency'] = request.concurrency
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance(
        self,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        return self.update_instance_with_options(request, runtime)

    async def update_instance_async(
        self,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        return await self.update_instance_with_options_async(request, runtime)

    def update_script_with_options(
        self,
        request: main_models.UpdateScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateScriptResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.script_id):
            body['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateScript',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_script_with_options_async(
        self,
        request: main_models.UpdateScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateScriptResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.script_id):
            body['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateScript',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_script(
        self,
        request: main_models.UpdateScriptRequest,
    ) -> main_models.UpdateScriptResponse:
        runtime = RuntimeOptions()
        return self.update_script_with_options(request, runtime)

    async def update_script_async(
        self,
        request: main_models.UpdateScriptRequest,
    ) -> main_models.UpdateScriptResponse:
        runtime = RuntimeOptions()
        return await self.update_script_with_options_async(request, runtime)

    def update_subscription_with_options(
        self,
        tmp_req: main_models.UpdateSubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSubscriptionResponse:
        tmp_req.validate()
        request = main_models.UpdateSubscriptionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.event_subscriptions):
            request.event_subscriptions_shrink = Utils.array_to_string_with_specified_style(tmp_req.event_subscriptions, 'EventSubscriptions', 'json')
        body = {}
        if not DaraCore.is_null(request.endpoint):
            body['Endpoint'] = request.endpoint
        if not DaraCore.is_null(request.event_subscriptions_shrink):
            body['EventSubscriptions'] = request.event_subscriptions_shrink
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mq_instance_id):
            body['MqInstanceId'] = request.mq_instance_id
        if not DaraCore.is_null(request.mq_type):
            body['MqType'] = request.mq_type
        if not DaraCore.is_null(request.password):
            body['Password'] = request.password
        if not DaraCore.is_null(request.producer_id):
            body['ProducerId'] = request.producer_id
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSubscription',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_subscription_with_options_async(
        self,
        tmp_req: main_models.UpdateSubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSubscriptionResponse:
        tmp_req.validate()
        request = main_models.UpdateSubscriptionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.event_subscriptions):
            request.event_subscriptions_shrink = Utils.array_to_string_with_specified_style(tmp_req.event_subscriptions, 'EventSubscriptions', 'json')
        body = {}
        if not DaraCore.is_null(request.endpoint):
            body['Endpoint'] = request.endpoint
        if not DaraCore.is_null(request.event_subscriptions_shrink):
            body['EventSubscriptions'] = request.event_subscriptions_shrink
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mq_instance_id):
            body['MqInstanceId'] = request.mq_instance_id
        if not DaraCore.is_null(request.mq_type):
            body['MqType'] = request.mq_type
        if not DaraCore.is_null(request.password):
            body['Password'] = request.password
        if not DaraCore.is_null(request.producer_id):
            body['ProducerId'] = request.producer_id
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSubscription',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_subscription(
        self,
        request: main_models.UpdateSubscriptionRequest,
    ) -> main_models.UpdateSubscriptionResponse:
        runtime = RuntimeOptions()
        return self.update_subscription_with_options(request, runtime)

    async def update_subscription_async(
        self,
        request: main_models.UpdateSubscriptionRequest,
    ) -> main_models.UpdateSubscriptionResponse:
        runtime = RuntimeOptions()
        return await self.update_subscription_with_options_async(request, runtime)

    def update_system_configs_with_options(
        self,
        tmp_req: main_models.UpdateSystemConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSystemConfigsResponse:
        tmp_req.validate()
        request = main_models.UpdateSystemConfigsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.configs):
            request.configs_shrink = Utils.array_to_string_with_specified_style(tmp_req.configs, 'Configs', 'json')
        body = {}
        if not DaraCore.is_null(request.configs_shrink):
            body['Configs'] = request.configs_shrink
        if not DaraCore.is_null(request.object_id):
            body['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.object_type):
            body['ObjectType'] = request.object_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSystemConfigs',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSystemConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_system_configs_with_options_async(
        self,
        tmp_req: main_models.UpdateSystemConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSystemConfigsResponse:
        tmp_req.validate()
        request = main_models.UpdateSystemConfigsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.configs):
            request.configs_shrink = Utils.array_to_string_with_specified_style(tmp_req.configs, 'Configs', 'json')
        body = {}
        if not DaraCore.is_null(request.configs_shrink):
            body['Configs'] = request.configs_shrink
        if not DaraCore.is_null(request.object_id):
            body['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.object_type):
            body['ObjectType'] = request.object_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSystemConfigs',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSystemConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_system_configs(
        self,
        request: main_models.UpdateSystemConfigsRequest,
    ) -> main_models.UpdateSystemConfigsResponse:
        runtime = RuntimeOptions()
        return self.update_system_configs_with_options(request, runtime)

    async def update_system_configs_async(
        self,
        request: main_models.UpdateSystemConfigsRequest,
    ) -> main_models.UpdateSystemConfigsResponse:
        runtime = RuntimeOptions()
        return await self.update_system_configs_with_options_async(request, runtime)

    def update_voice_access_profile_with_options(
        self,
        tmp_req: main_models.UpdateVoiceAccessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVoiceAccessProfileResponse:
        tmp_req.validate()
        request = main_models.UpdateVoiceAccessProfileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.profile):
            request.profile_shrink = Utils.array_to_string_with_specified_style(tmp_req.profile, 'Profile', 'json')
        body = {}
        if not DaraCore.is_null(request.access_profile_id):
            body['AccessProfileId'] = request.access_profile_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nls_engine):
            body['NlsEngine'] = request.nls_engine
        if not DaraCore.is_null(request.profile_shrink):
            body['Profile'] = request.profile_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVoiceAccessProfile',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVoiceAccessProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_voice_access_profile_with_options_async(
        self,
        tmp_req: main_models.UpdateVoiceAccessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVoiceAccessProfileResponse:
        tmp_req.validate()
        request = main_models.UpdateVoiceAccessProfileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.profile):
            request.profile_shrink = Utils.array_to_string_with_specified_style(tmp_req.profile, 'Profile', 'json')
        body = {}
        if not DaraCore.is_null(request.access_profile_id):
            body['AccessProfileId'] = request.access_profile_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nls_engine):
            body['NlsEngine'] = request.nls_engine
        if not DaraCore.is_null(request.profile_shrink):
            body['Profile'] = request.profile_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVoiceAccessProfile',
            version = '2025-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVoiceAccessProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_voice_access_profile(
        self,
        request: main_models.UpdateVoiceAccessProfileRequest,
    ) -> main_models.UpdateVoiceAccessProfileResponse:
        runtime = RuntimeOptions()
        return self.update_voice_access_profile_with_options(request, runtime)

    async def update_voice_access_profile_async(
        self,
        request: main_models.UpdateVoiceAccessProfileRequest,
    ) -> main_models.UpdateVoiceAccessProfileResponse:
        runtime = RuntimeOptions()
        return await self.update_voice_access_profile_with_options_async(request, runtime)
