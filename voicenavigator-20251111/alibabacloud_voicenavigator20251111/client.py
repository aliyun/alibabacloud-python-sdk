# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_voicenavigator20251111 import models as main_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('voicenavigator', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_llm_access_profile_with_options(
        self,
        tmp_req: main_models.CreateLlmAccessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLlmAccessProfileResponse:
        tmp_req.validate()
        request = main_models.CreateLlmAccessProfileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.profile):
            request.profile_shrink = Utils.array_to_string_with_specified_style(tmp_req.profile, 'Profile', 'json')
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.profile_shrink):
            body['Profile'] = request.profile_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLlmAccessProfile',
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
            main_models.CreateLlmAccessProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_llm_access_profile_with_options_async(
        self,
        tmp_req: main_models.CreateLlmAccessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLlmAccessProfileResponse:
        tmp_req.validate()
        request = main_models.CreateLlmAccessProfileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.profile):
            request.profile_shrink = Utils.array_to_string_with_specified_style(tmp_req.profile, 'Profile', 'json')
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.profile_shrink):
            body['Profile'] = request.profile_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLlmAccessProfile',
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
            main_models.CreateLlmAccessProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_llm_access_profile(
        self,
        request: main_models.CreateLlmAccessProfileRequest,
    ) -> main_models.CreateLlmAccessProfileResponse:
        runtime = RuntimeOptions()
        return self.create_llm_access_profile_with_options(request, runtime)

    async def create_llm_access_profile_async(
        self,
        request: main_models.CreateLlmAccessProfileRequest,
    ) -> main_models.CreateLlmAccessProfileResponse:
        runtime = RuntimeOptions()
        return await self.create_llm_access_profile_with_options_async(request, runtime)

    def create_script_with_options(
        self,
        request: main_models.CreateScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScriptResponse:
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
        if not DaraCore.is_null(request.concurrency):
            body['Concurrency'] = request.concurrency
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
        if not DaraCore.is_null(tmp_req.label_config):
            request.label_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.label_config, 'LabelConfig', 'json')
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
        if not DaraCore.is_null(request.label_config_shrink):
            body['LabelConfig'] = request.label_config_shrink
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
        if not DaraCore.is_null(tmp_req.label_config):
            request.label_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.label_config, 'LabelConfig', 'json')
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
        if not DaraCore.is_null(request.label_config_shrink):
            body['LabelConfig'] = request.label_config_shrink
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

    def create_variable_with_options(
        self,
        request: main_models.CreateVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVariableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVariable',
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
            main_models.CreateVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_variable_with_options_async(
        self,
        request: main_models.CreateVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVariableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVariable',
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
            main_models.CreateVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_variable(
        self,
        request: main_models.CreateVariableRequest,
    ) -> main_models.CreateVariableResponse:
        runtime = RuntimeOptions()
        return self.create_variable_with_options(request, runtime)

    async def create_variable_async(
        self,
        request: main_models.CreateVariableRequest,
    ) -> main_models.CreateVariableResponse:
        runtime = RuntimeOptions()
        return await self.create_variable_with_options_async(request, runtime)

    def create_vocabulary_with_options(
        self,
        tmp_req: main_models.CreateVocabularyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVocabularyResponse:
        tmp_req.validate()
        request = main_models.CreateVocabularyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.words):
            request.words_shrink = Utils.array_to_string_with_specified_style(tmp_req.words, 'Words', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.words_shrink):
            body['Words'] = request.words_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVocabulary',
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
            main_models.CreateVocabularyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vocabulary_with_options_async(
        self,
        tmp_req: main_models.CreateVocabularyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVocabularyResponse:
        tmp_req.validate()
        request = main_models.CreateVocabularyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.words):
            request.words_shrink = Utils.array_to_string_with_specified_style(tmp_req.words, 'Words', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.words_shrink):
            body['Words'] = request.words_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVocabulary',
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
            main_models.CreateVocabularyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vocabulary(
        self,
        request: main_models.CreateVocabularyRequest,
    ) -> main_models.CreateVocabularyResponse:
        runtime = RuntimeOptions()
        return self.create_vocabulary_with_options(request, runtime)

    async def create_vocabulary_async(
        self,
        request: main_models.CreateVocabularyRequest,
    ) -> main_models.CreateVocabularyResponse:
        runtime = RuntimeOptions()
        return await self.create_vocabulary_with_options_async(request, runtime)

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

    def delete_llm_access_profile_with_options(
        self,
        request: main_models.DeleteLlmAccessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLlmAccessProfileResponse:
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
            action = 'DeleteLlmAccessProfile',
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
            main_models.DeleteLlmAccessProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_llm_access_profile_with_options_async(
        self,
        request: main_models.DeleteLlmAccessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLlmAccessProfileResponse:
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
            action = 'DeleteLlmAccessProfile',
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
            main_models.DeleteLlmAccessProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_llm_access_profile(
        self,
        request: main_models.DeleteLlmAccessProfileRequest,
    ) -> main_models.DeleteLlmAccessProfileResponse:
        runtime = RuntimeOptions()
        return self.delete_llm_access_profile_with_options(request, runtime)

    async def delete_llm_access_profile_async(
        self,
        request: main_models.DeleteLlmAccessProfileRequest,
    ) -> main_models.DeleteLlmAccessProfileResponse:
        runtime = RuntimeOptions()
        return await self.delete_llm_access_profile_with_options_async(request, runtime)

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

    def delete_variable_with_options(
        self,
        request: main_models.DeleteVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVariableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.variable_id):
            body['VariableId'] = request.variable_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVariable',
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
            main_models.DeleteVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_variable_with_options_async(
        self,
        request: main_models.DeleteVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVariableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.variable_id):
            body['VariableId'] = request.variable_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVariable',
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
            main_models.DeleteVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_variable(
        self,
        request: main_models.DeleteVariableRequest,
    ) -> main_models.DeleteVariableResponse:
        runtime = RuntimeOptions()
        return self.delete_variable_with_options(request, runtime)

    async def delete_variable_async(
        self,
        request: main_models.DeleteVariableRequest,
    ) -> main_models.DeleteVariableResponse:
        runtime = RuntimeOptions()
        return await self.delete_variable_with_options_async(request, runtime)

    def delete_vocabulary_with_options(
        self,
        request: main_models.DeleteVocabularyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVocabularyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.vocabulary_id):
            body['VocabularyId'] = request.vocabulary_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVocabulary',
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
            main_models.DeleteVocabularyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vocabulary_with_options_async(
        self,
        request: main_models.DeleteVocabularyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVocabularyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.vocabulary_id):
            body['VocabularyId'] = request.vocabulary_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVocabulary',
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
            main_models.DeleteVocabularyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vocabulary(
        self,
        request: main_models.DeleteVocabularyRequest,
    ) -> main_models.DeleteVocabularyResponse:
        runtime = RuntimeOptions()
        return self.delete_vocabulary_with_options(request, runtime)

    async def delete_vocabulary_async(
        self,
        request: main_models.DeleteVocabularyRequest,
    ) -> main_models.DeleteVocabularyResponse:
        runtime = RuntimeOptions()
        return await self.delete_vocabulary_with_options_async(request, runtime)

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

    def export_script_with_options(
        self,
        request: main_models.ExportScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportScriptResponse:
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
            action = 'ExportScript',
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
            main_models.ExportScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_script_with_options_async(
        self,
        request: main_models.ExportScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportScriptResponse:
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
            action = 'ExportScript',
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
            main_models.ExportScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_script(
        self,
        request: main_models.ExportScriptRequest,
    ) -> main_models.ExportScriptResponse:
        runtime = RuntimeOptions()
        return self.export_script_with_options(request, runtime)

    async def export_script_async(
        self,
        request: main_models.ExportScriptRequest,
    ) -> main_models.ExportScriptResponse:
        runtime = RuntimeOptions()
        return await self.export_script_with_options_async(request, runtime)

    def export_vocabulary_with_options(
        self,
        tmp_req: main_models.ExportVocabularyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportVocabularyResponse:
        tmp_req.validate()
        request = main_models.ExportVocabularyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.vocabulary_ids):
            request.vocabulary_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.vocabulary_ids, 'VocabularyIds', 'json')
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.vocabulary_ids_shrink):
            body['VocabularyIds'] = request.vocabulary_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportVocabulary',
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
            main_models.ExportVocabularyResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_vocabulary_with_options_async(
        self,
        tmp_req: main_models.ExportVocabularyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportVocabularyResponse:
        tmp_req.validate()
        request = main_models.ExportVocabularyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.vocabulary_ids):
            request.vocabulary_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.vocabulary_ids, 'VocabularyIds', 'json')
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.vocabulary_ids_shrink):
            body['VocabularyIds'] = request.vocabulary_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportVocabulary',
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
            main_models.ExportVocabularyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_vocabulary(
        self,
        request: main_models.ExportVocabularyRequest,
    ) -> main_models.ExportVocabularyResponse:
        runtime = RuntimeOptions()
        return self.export_vocabulary_with_options(request, runtime)

    async def export_vocabulary_async(
        self,
        request: main_models.ExportVocabularyRequest,
    ) -> main_models.ExportVocabularyResponse:
        runtime = RuntimeOptions()
        return await self.export_vocabulary_with_options_async(request, runtime)

    def generate_file_upload_params_with_options(
        self,
        request: main_models.GenerateFileUploadParamsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateFileUploadParamsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_type):
            body['BusinessType'] = request.business_type
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateFileUploadParams',
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
            main_models.GenerateFileUploadParamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_file_upload_params_with_options_async(
        self,
        request: main_models.GenerateFileUploadParamsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateFileUploadParamsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_type):
            body['BusinessType'] = request.business_type
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateFileUploadParams',
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
            main_models.GenerateFileUploadParamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_file_upload_params(
        self,
        request: main_models.GenerateFileUploadParamsRequest,
    ) -> main_models.GenerateFileUploadParamsResponse:
        runtime = RuntimeOptions()
        return self.generate_file_upload_params_with_options(request, runtime)

    async def generate_file_upload_params_async(
        self,
        request: main_models.GenerateFileUploadParamsRequest,
    ) -> main_models.GenerateFileUploadParamsResponse:
        runtime = RuntimeOptions()
        return await self.generate_file_upload_params_with_options_async(request, runtime)

    def get_call_detail_record_with_options(
        self,
        request: main_models.GetCallDetailRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCallDetailRecordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCallDetailRecord',
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
            main_models.GetCallDetailRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_call_detail_record_with_options_async(
        self,
        request: main_models.GetCallDetailRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCallDetailRecordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCallDetailRecord',
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
            main_models.GetCallDetailRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_call_detail_record(
        self,
        request: main_models.GetCallDetailRecordRequest,
    ) -> main_models.GetCallDetailRecordResponse:
        runtime = RuntimeOptions()
        return self.get_call_detail_record_with_options(request, runtime)

    async def get_call_detail_record_async(
        self,
        request: main_models.GetCallDetailRecordRequest,
    ) -> main_models.GetCallDetailRecordResponse:
        runtime = RuntimeOptions()
        return await self.get_call_detail_record_with_options_async(request, runtime)

    def get_realtime_instance_stats_with_options(
        self,
        request: main_models.GetRealtimeInstanceStatsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRealtimeInstanceStatsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetRealtimeInstanceStats',
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
            main_models.GetRealtimeInstanceStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_realtime_instance_stats_with_options_async(
        self,
        request: main_models.GetRealtimeInstanceStatsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRealtimeInstanceStatsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetRealtimeInstanceStats',
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
            main_models.GetRealtimeInstanceStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_realtime_instance_stats(
        self,
        request: main_models.GetRealtimeInstanceStatsRequest,
    ) -> main_models.GetRealtimeInstanceStatsResponse:
        runtime = RuntimeOptions()
        return self.get_realtime_instance_stats_with_options(request, runtime)

    async def get_realtime_instance_stats_async(
        self,
        request: main_models.GetRealtimeInstanceStatsRequest,
    ) -> main_models.GetRealtimeInstanceStatsResponse:
        runtime = RuntimeOptions()
        return await self.get_realtime_instance_stats_with_options_async(request, runtime)

    def get_recording_with_options(
        self,
        request: main_models.GetRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRecordingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetRecording',
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
            main_models.GetRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_recording_with_options_async(
        self,
        request: main_models.GetRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRecordingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetRecording',
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
            main_models.GetRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_recording(
        self,
        request: main_models.GetRecordingRequest,
    ) -> main_models.GetRecordingResponse:
        runtime = RuntimeOptions()
        return self.get_recording_with_options(request, runtime)

    async def get_recording_async(
        self,
        request: main_models.GetRecordingRequest,
    ) -> main_models.GetRecordingResponse:
        runtime = RuntimeOptions()
        return await self.get_recording_with_options_async(request, runtime)

    def get_script_with_options(
        self,
        request: main_models.GetScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScriptResponse:
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
            action = 'GetScript',
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
            main_models.GetScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_script_with_options_async(
        self,
        request: main_models.GetScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScriptResponse:
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
            action = 'GetScript',
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
            main_models.GetScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_script(
        self,
        request: main_models.GetScriptRequest,
    ) -> main_models.GetScriptResponse:
        runtime = RuntimeOptions()
        return self.get_script_with_options(request, runtime)

    async def get_script_async(
        self,
        request: main_models.GetScriptRequest,
    ) -> main_models.GetScriptResponse:
        runtime = RuntimeOptions()
        return await self.get_script_with_options_async(request, runtime)

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

    def get_vocabulary_with_options(
        self,
        request: main_models.GetVocabularyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVocabularyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.vocabulary_id):
            body['VocabularyId'] = request.vocabulary_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVocabulary',
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
            main_models.GetVocabularyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vocabulary_with_options_async(
        self,
        request: main_models.GetVocabularyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVocabularyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.vocabulary_id):
            body['VocabularyId'] = request.vocabulary_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVocabulary',
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
            main_models.GetVocabularyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vocabulary(
        self,
        request: main_models.GetVocabularyRequest,
    ) -> main_models.GetVocabularyResponse:
        runtime = RuntimeOptions()
        return self.get_vocabulary_with_options(request, runtime)

    async def get_vocabulary_async(
        self,
        request: main_models.GetVocabularyRequest,
    ) -> main_models.GetVocabularyResponse:
        runtime = RuntimeOptions()
        return await self.get_vocabulary_with_options_async(request, runtime)

    def import_vocabulary_with_options(
        self,
        request: main_models.ImportVocabularyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportVocabularyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_key):
            body['FileKey'] = request.file_key
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportVocabulary',
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
            main_models.ImportVocabularyResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_vocabulary_with_options_async(
        self,
        request: main_models.ImportVocabularyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportVocabularyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_key):
            body['FileKey'] = request.file_key
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportVocabulary',
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
            main_models.ImportVocabularyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_vocabulary(
        self,
        request: main_models.ImportVocabularyRequest,
    ) -> main_models.ImportVocabularyResponse:
        runtime = RuntimeOptions()
        return self.import_vocabulary_with_options(request, runtime)

    async def import_vocabulary_async(
        self,
        request: main_models.ImportVocabularyRequest,
    ) -> main_models.ImportVocabularyResponse:
        runtime = RuntimeOptions()
        return await self.import_vocabulary_with_options_async(request, runtime)

    def list_background_musics_with_options(
        self,
        request: main_models.ListBackgroundMusicsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBackgroundMusicsResponse:
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
            action = 'ListBackgroundMusics',
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
            main_models.ListBackgroundMusicsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_background_musics_with_options_async(
        self,
        request: main_models.ListBackgroundMusicsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBackgroundMusicsResponse:
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
            action = 'ListBackgroundMusics',
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
            main_models.ListBackgroundMusicsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_background_musics(
        self,
        request: main_models.ListBackgroundMusicsRequest,
    ) -> main_models.ListBackgroundMusicsResponse:
        runtime = RuntimeOptions()
        return self.list_background_musics_with_options(request, runtime)

    async def list_background_musics_async(
        self,
        request: main_models.ListBackgroundMusicsRequest,
    ) -> main_models.ListBackgroundMusicsResponse:
        runtime = RuntimeOptions()
        return await self.list_background_musics_with_options_async(request, runtime)

    def list_call_detail_records_with_options(
        self,
        tmp_req: main_models.ListCallDetailRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCallDetailRecordsResponse:
        tmp_req.validate()
        request = main_models.ListCallDetailRecordsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.disposition_codes):
            request.disposition_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.disposition_codes, 'DispositionCodes', 'json')
        if not DaraCore.is_null(tmp_req.disposition_reasons):
            request.disposition_reasons_shrink = Utils.array_to_string_with_specified_style(tmp_req.disposition_reasons, 'DispositionReasons', 'json')
        if not DaraCore.is_null(tmp_req.session_ids):
            request.session_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.session_ids, 'SessionIds', 'json')
        query = {}
        if not DaraCore.is_null(request.access_channel_id):
            query['AccessChannelId'] = request.access_channel_id
        if not DaraCore.is_null(request.access_channel_type):
            query['AccessChannelType'] = request.access_channel_type
        if not DaraCore.is_null(request.draft_version):
            query['DraftVersion'] = request.draft_version
        if not DaraCore.is_null(request.issue_resolved):
            query['IssueResolved'] = request.issue_resolved
        if not DaraCore.is_null(request.max_talk_turns):
            query['MaxTalkTurns'] = request.max_talk_turns
        if not DaraCore.is_null(request.min_talk_turns):
            query['MinTalkTurns'] = request.min_talk_turns
        body = {}
        if not DaraCore.is_null(request.callee):
            body['Callee'] = request.callee
        if not DaraCore.is_null(request.caller):
            body['Caller'] = request.caller
        if not DaraCore.is_null(request.disposition_codes_shrink):
            body['DispositionCodes'] = request.disposition_codes_shrink
        if not DaraCore.is_null(request.disposition_reasons_shrink):
            body['DispositionReasons'] = request.disposition_reasons_shrink
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.script_id):
            body['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.session_ids_shrink):
            body['SessionIds'] = request.session_ids_shrink
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCallDetailRecords',
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
            main_models.ListCallDetailRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_call_detail_records_with_options_async(
        self,
        tmp_req: main_models.ListCallDetailRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCallDetailRecordsResponse:
        tmp_req.validate()
        request = main_models.ListCallDetailRecordsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.disposition_codes):
            request.disposition_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.disposition_codes, 'DispositionCodes', 'json')
        if not DaraCore.is_null(tmp_req.disposition_reasons):
            request.disposition_reasons_shrink = Utils.array_to_string_with_specified_style(tmp_req.disposition_reasons, 'DispositionReasons', 'json')
        if not DaraCore.is_null(tmp_req.session_ids):
            request.session_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.session_ids, 'SessionIds', 'json')
        query = {}
        if not DaraCore.is_null(request.access_channel_id):
            query['AccessChannelId'] = request.access_channel_id
        if not DaraCore.is_null(request.access_channel_type):
            query['AccessChannelType'] = request.access_channel_type
        if not DaraCore.is_null(request.draft_version):
            query['DraftVersion'] = request.draft_version
        if not DaraCore.is_null(request.issue_resolved):
            query['IssueResolved'] = request.issue_resolved
        if not DaraCore.is_null(request.max_talk_turns):
            query['MaxTalkTurns'] = request.max_talk_turns
        if not DaraCore.is_null(request.min_talk_turns):
            query['MinTalkTurns'] = request.min_talk_turns
        body = {}
        if not DaraCore.is_null(request.callee):
            body['Callee'] = request.callee
        if not DaraCore.is_null(request.caller):
            body['Caller'] = request.caller
        if not DaraCore.is_null(request.disposition_codes_shrink):
            body['DispositionCodes'] = request.disposition_codes_shrink
        if not DaraCore.is_null(request.disposition_reasons_shrink):
            body['DispositionReasons'] = request.disposition_reasons_shrink
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.script_id):
            body['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.session_ids_shrink):
            body['SessionIds'] = request.session_ids_shrink
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCallDetailRecords',
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
            main_models.ListCallDetailRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_call_detail_records(
        self,
        request: main_models.ListCallDetailRecordsRequest,
    ) -> main_models.ListCallDetailRecordsResponse:
        runtime = RuntimeOptions()
        return self.list_call_detail_records_with_options(request, runtime)

    async def list_call_detail_records_async(
        self,
        request: main_models.ListCallDetailRecordsRequest,
    ) -> main_models.ListCallDetailRecordsResponse:
        runtime = RuntimeOptions()
        return await self.list_call_detail_records_with_options_async(request, runtime)

    def list_clone_voice_with_options(
        self,
        request: main_models.ListCloneVoiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloneVoiceResponse:
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
            action = 'ListCloneVoice',
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
            main_models.ListCloneVoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clone_voice_with_options_async(
        self,
        request: main_models.ListCloneVoiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloneVoiceResponse:
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
            action = 'ListCloneVoice',
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
            main_models.ListCloneVoiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_clone_voice(
        self,
        request: main_models.ListCloneVoiceRequest,
    ) -> main_models.ListCloneVoiceResponse:
        runtime = RuntimeOptions()
        return self.list_clone_voice_with_options(request, runtime)

    async def list_clone_voice_async(
        self,
        request: main_models.ListCloneVoiceRequest,
    ) -> main_models.ListCloneVoiceResponse:
        runtime = RuntimeOptions()
        return await self.list_clone_voice_with_options_async(request, runtime)

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

    def list_llm_access_profiles_with_options(
        self,
        request: main_models.ListLlmAccessProfilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLlmAccessProfilesResponse:
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
            action = 'ListLlmAccessProfiles',
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
            main_models.ListLlmAccessProfilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_llm_access_profiles_with_options_async(
        self,
        request: main_models.ListLlmAccessProfilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLlmAccessProfilesResponse:
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
            action = 'ListLlmAccessProfiles',
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
            main_models.ListLlmAccessProfilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_llm_access_profiles(
        self,
        request: main_models.ListLlmAccessProfilesRequest,
    ) -> main_models.ListLlmAccessProfilesResponse:
        runtime = RuntimeOptions()
        return self.list_llm_access_profiles_with_options(request, runtime)

    async def list_llm_access_profiles_async(
        self,
        request: main_models.ListLlmAccessProfilesRequest,
    ) -> main_models.ListLlmAccessProfilesResponse:
        runtime = RuntimeOptions()
        return await self.list_llm_access_profiles_with_options_async(request, runtime)

    def list_nlu_models_with_options(
        self,
        request: main_models.ListNluModelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNluModelsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNluModels',
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
            main_models.ListNluModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nlu_models_with_options_async(
        self,
        request: main_models.ListNluModelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNluModelsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNluModels',
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
            main_models.ListNluModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nlu_models(
        self,
        request: main_models.ListNluModelsRequest,
    ) -> main_models.ListNluModelsResponse:
        runtime = RuntimeOptions()
        return self.list_nlu_models_with_options(request, runtime)

    async def list_nlu_models_async(
        self,
        request: main_models.ListNluModelsRequest,
    ) -> main_models.ListNluModelsResponse:
        runtime = RuntimeOptions()
        return await self.list_nlu_models_with_options_async(request, runtime)

    def list_script_profile_templates_with_options(
        self,
        request: main_models.ListScriptProfileTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScriptProfileTemplatesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
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
        if not DaraCore.is_null(request.number):
            body['Number'] = request.number
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.script_ids_shrink):
            body['ScriptIds'] = request.script_ids_shrink
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
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
        if not DaraCore.is_null(request.number):
            body['Number'] = request.number
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.script_ids_shrink):
            body['ScriptIds'] = request.script_ids_shrink
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
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

    def list_variable_with_options(
        self,
        request: main_models.ListVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVariableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            body['SearchPattern'] = request.search_pattern
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVariable',
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
            main_models.ListVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_variable_with_options_async(
        self,
        request: main_models.ListVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVariableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            body['SearchPattern'] = request.search_pattern
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVariable',
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
            main_models.ListVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_variable(
        self,
        request: main_models.ListVariableRequest,
    ) -> main_models.ListVariableResponse:
        runtime = RuntimeOptions()
        return self.list_variable_with_options(request, runtime)

    async def list_variable_async(
        self,
        request: main_models.ListVariableRequest,
    ) -> main_models.ListVariableResponse:
        runtime = RuntimeOptions()
        return await self.list_variable_with_options_async(request, runtime)

    def list_vocabulary_with_options(
        self,
        request: main_models.ListVocabularyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVocabularyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
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
            action = 'ListVocabulary',
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
            main_models.ListVocabularyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vocabulary_with_options_async(
        self,
        request: main_models.ListVocabularyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVocabularyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
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
            action = 'ListVocabulary',
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
            main_models.ListVocabularyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vocabulary(
        self,
        request: main_models.ListVocabularyRequest,
    ) -> main_models.ListVocabularyResponse:
        runtime = RuntimeOptions()
        return self.list_vocabulary_with_options(request, runtime)

    async def list_vocabulary_async(
        self,
        request: main_models.ListVocabularyRequest,
    ) -> main_models.ListVocabularyResponse:
        runtime = RuntimeOptions()
        return await self.list_vocabulary_with_options_async(request, runtime)

    def list_voice_access_profile_with_options(
        self,
        request: main_models.ListVoiceAccessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVoiceAccessProfileResponse:
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
            action = 'ListVoiceAccessProfile',
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
            main_models.ListVoiceAccessProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_voice_access_profile_with_options_async(
        self,
        request: main_models.ListVoiceAccessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVoiceAccessProfileResponse:
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
            action = 'ListVoiceAccessProfile',
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
            main_models.ListVoiceAccessProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_voice_access_profile(
        self,
        request: main_models.ListVoiceAccessProfileRequest,
    ) -> main_models.ListVoiceAccessProfileResponse:
        runtime = RuntimeOptions()
        return self.list_voice_access_profile_with_options(request, runtime)

    async def list_voice_access_profile_async(
        self,
        request: main_models.ListVoiceAccessProfileRequest,
    ) -> main_models.ListVoiceAccessProfileResponse:
        runtime = RuntimeOptions()
        return await self.list_voice_access_profile_with_options_async(request, runtime)

    def list_voice_engines_with_options(
        self,
        request: main_models.ListVoiceEnginesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVoiceEnginesResponse:
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
            action = 'ListVoiceEngines',
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
            main_models.ListVoiceEnginesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_voice_engines_with_options_async(
        self,
        request: main_models.ListVoiceEnginesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVoiceEnginesResponse:
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
            action = 'ListVoiceEngines',
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
            main_models.ListVoiceEnginesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_voice_engines(
        self,
        request: main_models.ListVoiceEnginesRequest,
    ) -> main_models.ListVoiceEnginesResponse:
        runtime = RuntimeOptions()
        return self.list_voice_engines_with_options(request, runtime)

    async def list_voice_engines_async(
        self,
        request: main_models.ListVoiceEnginesRequest,
    ) -> main_models.ListVoiceEnginesResponse:
        runtime = RuntimeOptions()
        return await self.list_voice_engines_with_options_async(request, runtime)

    def list_voices_with_options(
        self,
        request: main_models.ListVoicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVoicesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nls_access_type):
            body['NlsAccessType'] = request.nls_access_type
        if not DaraCore.is_null(request.nls_engine):
            body['NlsEngine'] = request.nls_engine
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVoices',
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
            main_models.ListVoicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_voices_with_options_async(
        self,
        request: main_models.ListVoicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVoicesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nls_access_type):
            body['NlsAccessType'] = request.nls_access_type
        if not DaraCore.is_null(request.nls_engine):
            body['NlsEngine'] = request.nls_engine
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVoices',
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
            main_models.ListVoicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_voices(
        self,
        request: main_models.ListVoicesRequest,
    ) -> main_models.ListVoicesResponse:
        runtime = RuntimeOptions()
        return self.list_voices_with_options(request, runtime)

    async def list_voices_async(
        self,
        request: main_models.ListVoicesRequest,
    ) -> main_models.ListVoicesResponse:
        runtime = RuntimeOptions()
        return await self.list_voices_with_options_async(request, runtime)

    def preview_voice_with_options(
        self,
        tmp_req: main_models.PreviewVoiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PreviewVoiceResponse:
        tmp_req.validate()
        request = main_models.PreviewVoiceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.nls_access_type):
            body['NlsAccessType'] = request.nls_access_type
        if not DaraCore.is_null(request.nls_engine):
            body['NlsEngine'] = request.nls_engine
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        if not DaraCore.is_null(request.text):
            body['Text'] = request.text
        if not DaraCore.is_null(request.voice):
            body['Voice'] = request.voice
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PreviewVoice',
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
            main_models.PreviewVoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def preview_voice_with_options_async(
        self,
        tmp_req: main_models.PreviewVoiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PreviewVoiceResponse:
        tmp_req.validate()
        request = main_models.PreviewVoiceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.nls_access_type):
            body['NlsAccessType'] = request.nls_access_type
        if not DaraCore.is_null(request.nls_engine):
            body['NlsEngine'] = request.nls_engine
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        if not DaraCore.is_null(request.text):
            body['Text'] = request.text
        if not DaraCore.is_null(request.voice):
            body['Voice'] = request.voice
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PreviewVoice',
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
            main_models.PreviewVoiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def preview_voice(
        self,
        request: main_models.PreviewVoiceRequest,
    ) -> main_models.PreviewVoiceResponse:
        runtime = RuntimeOptions()
        return self.preview_voice_with_options(request, runtime)

    async def preview_voice_async(
        self,
        request: main_models.PreviewVoiceRequest,
    ) -> main_models.PreviewVoiceResponse:
        runtime = RuntimeOptions()
        return await self.preview_voice_with_options_async(request, runtime)

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

    def update_llm_access_profile_with_options(
        self,
        tmp_req: main_models.UpdateLlmAccessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLlmAccessProfileResponse:
        tmp_req.validate()
        request = main_models.UpdateLlmAccessProfileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.profile):
            request.profile_shrink = Utils.array_to_string_with_specified_style(tmp_req.profile, 'Profile', 'json')
        body = {}
        if not DaraCore.is_null(request.access_profile_id):
            body['AccessProfileId'] = request.access_profile_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.profile_shrink):
            body['Profile'] = request.profile_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLlmAccessProfile',
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
            main_models.UpdateLlmAccessProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_llm_access_profile_with_options_async(
        self,
        tmp_req: main_models.UpdateLlmAccessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLlmAccessProfileResponse:
        tmp_req.validate()
        request = main_models.UpdateLlmAccessProfileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.profile):
            request.profile_shrink = Utils.array_to_string_with_specified_style(tmp_req.profile, 'Profile', 'json')
        body = {}
        if not DaraCore.is_null(request.access_profile_id):
            body['AccessProfileId'] = request.access_profile_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.profile_shrink):
            body['Profile'] = request.profile_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLlmAccessProfile',
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
            main_models.UpdateLlmAccessProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_llm_access_profile(
        self,
        request: main_models.UpdateLlmAccessProfileRequest,
    ) -> main_models.UpdateLlmAccessProfileResponse:
        runtime = RuntimeOptions()
        return self.update_llm_access_profile_with_options(request, runtime)

    async def update_llm_access_profile_async(
        self,
        request: main_models.UpdateLlmAccessProfileRequest,
    ) -> main_models.UpdateLlmAccessProfileResponse:
        runtime = RuntimeOptions()
        return await self.update_llm_access_profile_with_options_async(request, runtime)

    def update_script_with_options(
        self,
        request: main_models.UpdateScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateScriptResponse:
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
        if not DaraCore.is_null(request.concurrency):
            body['Concurrency'] = request.concurrency
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

    def update_variable_with_options(
        self,
        request: main_models.UpdateVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVariableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.variable_id):
            body['VariableId'] = request.variable_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVariable',
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
            main_models.UpdateVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_variable_with_options_async(
        self,
        request: main_models.UpdateVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVariableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.variable_id):
            body['VariableId'] = request.variable_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVariable',
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
            main_models.UpdateVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_variable(
        self,
        request: main_models.UpdateVariableRequest,
    ) -> main_models.UpdateVariableResponse:
        runtime = RuntimeOptions()
        return self.update_variable_with_options(request, runtime)

    async def update_variable_async(
        self,
        request: main_models.UpdateVariableRequest,
    ) -> main_models.UpdateVariableResponse:
        runtime = RuntimeOptions()
        return await self.update_variable_with_options_async(request, runtime)

    def update_vocabulary_with_options(
        self,
        tmp_req: main_models.UpdateVocabularyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVocabularyResponse:
        tmp_req.validate()
        request = main_models.UpdateVocabularyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.words):
            request.words_shrink = Utils.array_to_string_with_specified_style(tmp_req.words, 'Words', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.vocabulary_id):
            body['VocabularyId'] = request.vocabulary_id
        if not DaraCore.is_null(request.words_shrink):
            body['Words'] = request.words_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVocabulary',
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
            main_models.UpdateVocabularyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vocabulary_with_options_async(
        self,
        tmp_req: main_models.UpdateVocabularyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVocabularyResponse:
        tmp_req.validate()
        request = main_models.UpdateVocabularyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.words):
            request.words_shrink = Utils.array_to_string_with_specified_style(tmp_req.words, 'Words', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.vocabulary_id):
            body['VocabularyId'] = request.vocabulary_id
        if not DaraCore.is_null(request.words_shrink):
            body['Words'] = request.words_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVocabulary',
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
            main_models.UpdateVocabularyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vocabulary(
        self,
        request: main_models.UpdateVocabularyRequest,
    ) -> main_models.UpdateVocabularyResponse:
        runtime = RuntimeOptions()
        return self.update_vocabulary_with_options(request, runtime)

    async def update_vocabulary_async(
        self,
        request: main_models.UpdateVocabularyRequest,
    ) -> main_models.UpdateVocabularyResponse:
        runtime = RuntimeOptions()
        return await self.update_vocabulary_with_options_async(request, runtime)

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
