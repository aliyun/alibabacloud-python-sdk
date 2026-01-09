# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aiccs20191015 import models as main_models
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
        self._endpoint = self.get_endpoint('aiccs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_hotline_number_with_options(
        self,
        tmp_req: main_models.AddHotlineNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddHotlineNumberResponse:
        tmp_req.validate()
        request = main_models.AddHotlineNumberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.outbound_range_list):
            request.outbound_range_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.outbound_range_list, 'OutboundRangeList', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.enable_inbound):
            body['EnableInbound'] = request.enable_inbound
        if not DaraCore.is_null(request.enable_inbound_evaluation):
            body['EnableInboundEvaluation'] = request.enable_inbound_evaluation
        if not DaraCore.is_null(request.enable_outbound):
            body['EnableOutbound'] = request.enable_outbound
        if not DaraCore.is_null(request.enable_outbound_evaluation):
            body['EnableOutboundEvaluation'] = request.enable_outbound_evaluation
        if not DaraCore.is_null(request.evaluation_level):
            body['EvaluationLevel'] = request.evaluation_level
        if not DaraCore.is_null(request.hotline_number):
            body['HotlineNumber'] = request.hotline_number
        if not DaraCore.is_null(request.inbound_flow_id):
            body['InboundFlowId'] = request.inbound_flow_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.outbound_all_depart):
            body['OutboundAllDepart'] = request.outbound_all_depart
        if not DaraCore.is_null(request.outbound_range_list_shrink):
            body['OutboundRangeList'] = request.outbound_range_list_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddHotlineNumber',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddHotlineNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_hotline_number_with_options_async(
        self,
        tmp_req: main_models.AddHotlineNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddHotlineNumberResponse:
        tmp_req.validate()
        request = main_models.AddHotlineNumberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.outbound_range_list):
            request.outbound_range_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.outbound_range_list, 'OutboundRangeList', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.enable_inbound):
            body['EnableInbound'] = request.enable_inbound
        if not DaraCore.is_null(request.enable_inbound_evaluation):
            body['EnableInboundEvaluation'] = request.enable_inbound_evaluation
        if not DaraCore.is_null(request.enable_outbound):
            body['EnableOutbound'] = request.enable_outbound
        if not DaraCore.is_null(request.enable_outbound_evaluation):
            body['EnableOutboundEvaluation'] = request.enable_outbound_evaluation
        if not DaraCore.is_null(request.evaluation_level):
            body['EvaluationLevel'] = request.evaluation_level
        if not DaraCore.is_null(request.hotline_number):
            body['HotlineNumber'] = request.hotline_number
        if not DaraCore.is_null(request.inbound_flow_id):
            body['InboundFlowId'] = request.inbound_flow_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.outbound_all_depart):
            body['OutboundAllDepart'] = request.outbound_all_depart
        if not DaraCore.is_null(request.outbound_range_list_shrink):
            body['OutboundRangeList'] = request.outbound_range_list_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddHotlineNumber',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddHotlineNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_hotline_number(
        self,
        request: main_models.AddHotlineNumberRequest,
    ) -> main_models.AddHotlineNumberResponse:
        runtime = RuntimeOptions()
        return self.add_hotline_number_with_options(request, runtime)

    async def add_hotline_number_async(
        self,
        request: main_models.AddHotlineNumberRequest,
    ) -> main_models.AddHotlineNumberResponse:
        runtime = RuntimeOptions()
        return await self.add_hotline_number_with_options_async(request, runtime)

    def add_outer_account_with_options(
        self,
        request: main_models.AddOuterAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddOuterAccountResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddOuterAccount',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddOuterAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_outer_account_with_options_async(
        self,
        request: main_models.AddOuterAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddOuterAccountResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddOuterAccount',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddOuterAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_outer_account(
        self,
        request: main_models.AddOuterAccountRequest,
    ) -> main_models.AddOuterAccountResponse:
        runtime = RuntimeOptions()
        return self.add_outer_account_with_options(request, runtime)

    async def add_outer_account_async(
        self,
        request: main_models.AddOuterAccountRequest,
    ) -> main_models.AddOuterAccountResponse:
        runtime = RuntimeOptions()
        return await self.add_outer_account_with_options_async(request, runtime)

    def add_skill_group_with_options(
        self,
        request: main_models.AddSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSkillGroupResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSkillGroup',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_skill_group_with_options_async(
        self,
        request: main_models.AddSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSkillGroupResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSkillGroup',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_skill_group(
        self,
        request: main_models.AddSkillGroupRequest,
    ) -> main_models.AddSkillGroupResponse:
        runtime = RuntimeOptions()
        return self.add_skill_group_with_options(request, runtime)

    async def add_skill_group_async(
        self,
        request: main_models.AddSkillGroupRequest,
    ) -> main_models.AddSkillGroupResponse:
        runtime = RuntimeOptions()
        return await self.add_skill_group_with_options_async(request, runtime)

    def aiccs_smart_call_with_options(
        self,
        request: main_models.AiccsSmartCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AiccsSmartCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_code_break):
            query['ActionCodeBreak'] = request.action_code_break
        if not DaraCore.is_null(request.action_code_time_break):
            query['ActionCodeTimeBreak'] = request.action_code_time_break
        if not DaraCore.is_null(request.asr_als_am_id):
            query['AsrAlsAmId'] = request.asr_als_am_id
        if not DaraCore.is_null(request.asr_base_id):
            query['AsrBaseId'] = request.asr_base_id
        if not DaraCore.is_null(request.asr_model_id):
            query['AsrModelId'] = request.asr_model_id
        if not DaraCore.is_null(request.asr_vocabulary_id):
            query['AsrVocabularyId'] = request.asr_vocabulary_id
        if not DaraCore.is_null(request.background_file_code):
            query['BackgroundFileCode'] = request.background_file_code
        if not DaraCore.is_null(request.background_speed):
            query['BackgroundSpeed'] = request.background_speed
        if not DaraCore.is_null(request.background_volume):
            query['BackgroundVolume'] = request.background_volume
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not DaraCore.is_null(request.dynamic_id):
            query['DynamicId'] = request.dynamic_id
        if not DaraCore.is_null(request.early_media_asr):
            query['EarlyMediaAsr'] = request.early_media_asr
        if not DaraCore.is_null(request.enable_itn):
            query['EnableITN'] = request.enable_itn
        if not DaraCore.is_null(request.mute_time):
            query['MuteTime'] = request.mute_time
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pause_time):
            query['PauseTime'] = request.pause_time
        if not DaraCore.is_null(request.play_times):
            query['PlayTimes'] = request.play_times
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.record_flag):
            query['RecordFlag'] = request.record_flag
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.session_timeout):
            query['SessionTimeout'] = request.session_timeout
        if not DaraCore.is_null(request.speed):
            query['Speed'] = request.speed
        if not DaraCore.is_null(request.tts_conf):
            query['TtsConf'] = request.tts_conf
        if not DaraCore.is_null(request.tts_speed):
            query['TtsSpeed'] = request.tts_speed
        if not DaraCore.is_null(request.tts_style):
            query['TtsStyle'] = request.tts_style
        if not DaraCore.is_null(request.tts_volume):
            query['TtsVolume'] = request.tts_volume
        if not DaraCore.is_null(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not DaraCore.is_null(request.voice_code_param):
            query['VoiceCodeParam'] = request.voice_code_param
        if not DaraCore.is_null(request.volume):
            query['Volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AiccsSmartCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AiccsSmartCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def aiccs_smart_call_with_options_async(
        self,
        request: main_models.AiccsSmartCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AiccsSmartCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_code_break):
            query['ActionCodeBreak'] = request.action_code_break
        if not DaraCore.is_null(request.action_code_time_break):
            query['ActionCodeTimeBreak'] = request.action_code_time_break
        if not DaraCore.is_null(request.asr_als_am_id):
            query['AsrAlsAmId'] = request.asr_als_am_id
        if not DaraCore.is_null(request.asr_base_id):
            query['AsrBaseId'] = request.asr_base_id
        if not DaraCore.is_null(request.asr_model_id):
            query['AsrModelId'] = request.asr_model_id
        if not DaraCore.is_null(request.asr_vocabulary_id):
            query['AsrVocabularyId'] = request.asr_vocabulary_id
        if not DaraCore.is_null(request.background_file_code):
            query['BackgroundFileCode'] = request.background_file_code
        if not DaraCore.is_null(request.background_speed):
            query['BackgroundSpeed'] = request.background_speed
        if not DaraCore.is_null(request.background_volume):
            query['BackgroundVolume'] = request.background_volume
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not DaraCore.is_null(request.dynamic_id):
            query['DynamicId'] = request.dynamic_id
        if not DaraCore.is_null(request.early_media_asr):
            query['EarlyMediaAsr'] = request.early_media_asr
        if not DaraCore.is_null(request.enable_itn):
            query['EnableITN'] = request.enable_itn
        if not DaraCore.is_null(request.mute_time):
            query['MuteTime'] = request.mute_time
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pause_time):
            query['PauseTime'] = request.pause_time
        if not DaraCore.is_null(request.play_times):
            query['PlayTimes'] = request.play_times
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.record_flag):
            query['RecordFlag'] = request.record_flag
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.session_timeout):
            query['SessionTimeout'] = request.session_timeout
        if not DaraCore.is_null(request.speed):
            query['Speed'] = request.speed
        if not DaraCore.is_null(request.tts_conf):
            query['TtsConf'] = request.tts_conf
        if not DaraCore.is_null(request.tts_speed):
            query['TtsSpeed'] = request.tts_speed
        if not DaraCore.is_null(request.tts_style):
            query['TtsStyle'] = request.tts_style
        if not DaraCore.is_null(request.tts_volume):
            query['TtsVolume'] = request.tts_volume
        if not DaraCore.is_null(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not DaraCore.is_null(request.voice_code_param):
            query['VoiceCodeParam'] = request.voice_code_param
        if not DaraCore.is_null(request.volume):
            query['Volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AiccsSmartCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AiccsSmartCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def aiccs_smart_call(
        self,
        request: main_models.AiccsSmartCallRequest,
    ) -> main_models.AiccsSmartCallResponse:
        runtime = RuntimeOptions()
        return self.aiccs_smart_call_with_options(request, runtime)

    async def aiccs_smart_call_async(
        self,
        request: main_models.AiccsSmartCallRequest,
    ) -> main_models.AiccsSmartCallResponse:
        runtime = RuntimeOptions()
        return await self.aiccs_smart_call_with_options_async(request, runtime)

    def aiccs_smart_call_operate_with_options(
        self,
        request: main_models.AiccsSmartCallOperateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AiccsSmartCallOperateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.command):
            query['Command'] = request.command
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.param):
            query['Param'] = request.param
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AiccsSmartCallOperate',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AiccsSmartCallOperateResponse(),
            self.call_api(params, req, runtime)
        )

    async def aiccs_smart_call_operate_with_options_async(
        self,
        request: main_models.AiccsSmartCallOperateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AiccsSmartCallOperateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.command):
            query['Command'] = request.command
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.param):
            query['Param'] = request.param
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AiccsSmartCallOperate',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AiccsSmartCallOperateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def aiccs_smart_call_operate(
        self,
        request: main_models.AiccsSmartCallOperateRequest,
    ) -> main_models.AiccsSmartCallOperateResponse:
        runtime = RuntimeOptions()
        return self.aiccs_smart_call_operate_with_options(request, runtime)

    async def aiccs_smart_call_operate_async(
        self,
        request: main_models.AiccsSmartCallOperateRequest,
    ) -> main_models.AiccsSmartCallOperateResponse:
        runtime = RuntimeOptions()
        return await self.aiccs_smart_call_operate_with_options_async(request, runtime)

    def answer_call_with_options(
        self,
        request: main_models.AnswerCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AnswerCallResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.call_id):
            body['CallId'] = request.call_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AnswerCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AnswerCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def answer_call_with_options_async(
        self,
        request: main_models.AnswerCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AnswerCallResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.call_id):
            body['CallId'] = request.call_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AnswerCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AnswerCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def answer_call(
        self,
        request: main_models.AnswerCallRequest,
    ) -> main_models.AnswerCallResponse:
        runtime = RuntimeOptions()
        return self.answer_call_with_options(request, runtime)

    async def answer_call_async(
        self,
        request: main_models.AnswerCallRequest,
    ) -> main_models.AnswerCallResponse:
        runtime = RuntimeOptions()
        return await self.answer_call_with_options_async(request, runtime)

    def attach_task_with_options(
        self,
        request: main_models.AttachTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_string):
            query['CallString'] = request.call_string
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_task_with_options_async(
        self,
        request: main_models.AttachTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_string):
            query['CallString'] = request.call_string
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_task(
        self,
        request: main_models.AttachTaskRequest,
    ) -> main_models.AttachTaskResponse:
        runtime = RuntimeOptions()
        return self.attach_task_with_options(request, runtime)

    async def attach_task_async(
        self,
        request: main_models.AttachTaskRequest,
    ) -> main_models.AttachTaskResponse:
        runtime = RuntimeOptions()
        return await self.attach_task_with_options_async(request, runtime)

    def batch_create_quality_projects_with_options(
        self,
        request: main_models.BatchCreateQualityProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchCreateQualityProjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.analysis_ids):
            query['AnalysisIds'] = request.analysis_ids
        if not DaraCore.is_null(request.channel_touch_type):
            query['ChannelTouchType'] = request.channel_touch_type
        if not DaraCore.is_null(request.check_freq_type):
            query['CheckFreqType'] = request.check_freq_type
        if not DaraCore.is_null(request.instance_list):
            query['InstanceList'] = request.instance_list
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.time_range_end):
            query['TimeRangeEnd'] = request.time_range_end
        if not DaraCore.is_null(request.time_range_start):
            query['TimeRangeStart'] = request.time_range_start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchCreateQualityProjects',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchCreateQualityProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_create_quality_projects_with_options_async(
        self,
        request: main_models.BatchCreateQualityProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchCreateQualityProjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.analysis_ids):
            query['AnalysisIds'] = request.analysis_ids
        if not DaraCore.is_null(request.channel_touch_type):
            query['ChannelTouchType'] = request.channel_touch_type
        if not DaraCore.is_null(request.check_freq_type):
            query['CheckFreqType'] = request.check_freq_type
        if not DaraCore.is_null(request.instance_list):
            query['InstanceList'] = request.instance_list
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.time_range_end):
            query['TimeRangeEnd'] = request.time_range_end
        if not DaraCore.is_null(request.time_range_start):
            query['TimeRangeStart'] = request.time_range_start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchCreateQualityProjects',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchCreateQualityProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_create_quality_projects(
        self,
        request: main_models.BatchCreateQualityProjectsRequest,
    ) -> main_models.BatchCreateQualityProjectsResponse:
        runtime = RuntimeOptions()
        return self.batch_create_quality_projects_with_options(request, runtime)

    async def batch_create_quality_projects_async(
        self,
        request: main_models.BatchCreateQualityProjectsRequest,
    ) -> main_models.BatchCreateQualityProjectsResponse:
        runtime = RuntimeOptions()
        return await self.batch_create_quality_projects_with_options_async(request, runtime)

    def cancel_ai_call_details_with_options(
        self,
        tmp_req: main_models.CancelAiCallDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelAiCallDetailsResponse:
        tmp_req.validate()
        request = main_models.CancelAiCallDetailsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.detail_id_list):
            request.detail_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.detail_id_list, 'DetailIdList', 'json')
        if not DaraCore.is_null(tmp_req.phone_numbers):
            request.phone_numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.phone_numbers, 'PhoneNumbers', 'json')
        query = {}
        if not DaraCore.is_null(request.batch_id):
            query['BatchId'] = request.batch_id
        if not DaraCore.is_null(request.detail_id_list_shrink):
            query['DetailIdList'] = request.detail_id_list_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_numbers_shrink):
            query['PhoneNumbers'] = request.phone_numbers_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelAiCallDetails',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAiCallDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_ai_call_details_with_options_async(
        self,
        tmp_req: main_models.CancelAiCallDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelAiCallDetailsResponse:
        tmp_req.validate()
        request = main_models.CancelAiCallDetailsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.detail_id_list):
            request.detail_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.detail_id_list, 'DetailIdList', 'json')
        if not DaraCore.is_null(tmp_req.phone_numbers):
            request.phone_numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.phone_numbers, 'PhoneNumbers', 'json')
        query = {}
        if not DaraCore.is_null(request.batch_id):
            query['BatchId'] = request.batch_id
        if not DaraCore.is_null(request.detail_id_list_shrink):
            query['DetailIdList'] = request.detail_id_list_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_numbers_shrink):
            query['PhoneNumbers'] = request.phone_numbers_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelAiCallDetails',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAiCallDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_ai_call_details(
        self,
        request: main_models.CancelAiCallDetailsRequest,
    ) -> main_models.CancelAiCallDetailsResponse:
        runtime = RuntimeOptions()
        return self.cancel_ai_call_details_with_options(request, runtime)

    async def cancel_ai_call_details_async(
        self,
        request: main_models.CancelAiCallDetailsRequest,
    ) -> main_models.CancelAiCallDetailsResponse:
        runtime = RuntimeOptions()
        return await self.cancel_ai_call_details_with_options_async(request, runtime)

    def cancel_task_with_options(
        self,
        request: main_models.CancelTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_task_with_options_async(
        self,
        request: main_models.CancelTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_task(
        self,
        request: main_models.CancelTaskRequest,
    ) -> main_models.CancelTaskResponse:
        runtime = RuntimeOptions()
        return self.cancel_task_with_options(request, runtime)

    async def cancel_task_async(
        self,
        request: main_models.CancelTaskRequest,
    ) -> main_models.CancelTaskResponse:
        runtime = RuntimeOptions()
        return await self.cancel_task_with_options_async(request, runtime)

    def change_chat_agent_status_with_options(
        self,
        request: main_models.ChangeChatAgentStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeChatAgentStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.method):
            body['Method'] = request.method
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeChatAgentStatus',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeChatAgentStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_chat_agent_status_with_options_async(
        self,
        request: main_models.ChangeChatAgentStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeChatAgentStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.method):
            body['Method'] = request.method
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeChatAgentStatus',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeChatAgentStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_chat_agent_status(
        self,
        request: main_models.ChangeChatAgentStatusRequest,
    ) -> main_models.ChangeChatAgentStatusResponse:
        runtime = RuntimeOptions()
        return self.change_chat_agent_status_with_options(request, runtime)

    async def change_chat_agent_status_async(
        self,
        request: main_models.ChangeChatAgentStatusRequest,
    ) -> main_models.ChangeChatAgentStatusResponse:
        runtime = RuntimeOptions()
        return await self.change_chat_agent_status_with_options_async(request, runtime)

    def change_quality_project_status_with_options(
        self,
        request: main_models.ChangeQualityProjectStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeQualityProjectStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeQualityProjectStatus',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeQualityProjectStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_quality_project_status_with_options_async(
        self,
        request: main_models.ChangeQualityProjectStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeQualityProjectStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeQualityProjectStatus',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeQualityProjectStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_quality_project_status(
        self,
        request: main_models.ChangeQualityProjectStatusRequest,
    ) -> main_models.ChangeQualityProjectStatusResponse:
        runtime = RuntimeOptions()
        return self.change_quality_project_status_with_options(request, runtime)

    async def change_quality_project_status_async(
        self,
        request: main_models.ChangeQualityProjectStatusRequest,
    ) -> main_models.ChangeQualityProjectStatusResponse:
        runtime = RuntimeOptions()
        return await self.change_quality_project_status_with_options_async(request, runtime)

    def create_agent_with_options(
        self,
        request: main_models.CreateAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        body_flat = {}
        if not DaraCore.is_null(request.skill_group_id):
            body_flat['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.skill_group_id_list):
            body_flat['SkillGroupIdList'] = request.skill_group_id_list
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgent',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_agent_with_options_async(
        self,
        request: main_models.CreateAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        body_flat = {}
        if not DaraCore.is_null(request.skill_group_id):
            body_flat['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.skill_group_id_list):
            body_flat['SkillGroupIdList'] = request.skill_group_id_list
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgent',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_agent(
        self,
        request: main_models.CreateAgentRequest,
    ) -> main_models.CreateAgentResponse:
        runtime = RuntimeOptions()
        return self.create_agent_with_options(request, runtime)

    async def create_agent_async(
        self,
        request: main_models.CreateAgentRequest,
    ) -> main_models.CreateAgentResponse:
        runtime = RuntimeOptions()
        return await self.create_agent_with_options_async(request, runtime)

    def create_ai_call_task_with_options(
        self,
        tmp_req: main_models.CreateAiCallTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAiCallTaskResponse:
        tmp_req.validate()
        request = main_models.CreateAiCallTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.call_day):
            request.call_day_shrink = Utils.array_to_string_with_specified_style(tmp_req.call_day, 'CallDay', 'json')
        if not DaraCore.is_null(tmp_req.call_retry_reason):
            request.call_retry_reason_shrink = Utils.array_to_string_with_specified_style(tmp_req.call_retry_reason, 'CallRetryReason', 'json')
        if not DaraCore.is_null(tmp_req.call_time):
            request.call_time_shrink = Utils.array_to_string_with_specified_style(tmp_req.call_time, 'CallTime', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.call_day_shrink):
            query['CallDay'] = request.call_day_shrink
        if not DaraCore.is_null(request.call_retry_interval):
            query['CallRetryInterval'] = request.call_retry_interval
        if not DaraCore.is_null(request.call_retry_reason_shrink):
            query['CallRetryReason'] = request.call_retry_reason_shrink
        if not DaraCore.is_null(request.call_retry_times):
            query['CallRetryTimes'] = request.call_retry_times
        if not DaraCore.is_null(request.call_time_shrink):
            query['CallTime'] = request.call_time_shrink
        if not DaraCore.is_null(request.miss_call_retry):
            query['MissCallRetry'] = request.miss_call_retry
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_type):
            query['StartType'] = request.start_type
        if not DaraCore.is_null(request.task_cps):
            query['TaskCps'] = request.task_cps
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_start_time):
            query['TaskStartTime'] = request.task_start_time
        if not DaraCore.is_null(request.virtual_number):
            query['VirtualNumber'] = request.virtual_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAiCallTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAiCallTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ai_call_task_with_options_async(
        self,
        tmp_req: main_models.CreateAiCallTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAiCallTaskResponse:
        tmp_req.validate()
        request = main_models.CreateAiCallTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.call_day):
            request.call_day_shrink = Utils.array_to_string_with_specified_style(tmp_req.call_day, 'CallDay', 'json')
        if not DaraCore.is_null(tmp_req.call_retry_reason):
            request.call_retry_reason_shrink = Utils.array_to_string_with_specified_style(tmp_req.call_retry_reason, 'CallRetryReason', 'json')
        if not DaraCore.is_null(tmp_req.call_time):
            request.call_time_shrink = Utils.array_to_string_with_specified_style(tmp_req.call_time, 'CallTime', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.call_day_shrink):
            query['CallDay'] = request.call_day_shrink
        if not DaraCore.is_null(request.call_retry_interval):
            query['CallRetryInterval'] = request.call_retry_interval
        if not DaraCore.is_null(request.call_retry_reason_shrink):
            query['CallRetryReason'] = request.call_retry_reason_shrink
        if not DaraCore.is_null(request.call_retry_times):
            query['CallRetryTimes'] = request.call_retry_times
        if not DaraCore.is_null(request.call_time_shrink):
            query['CallTime'] = request.call_time_shrink
        if not DaraCore.is_null(request.miss_call_retry):
            query['MissCallRetry'] = request.miss_call_retry
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_type):
            query['StartType'] = request.start_type
        if not DaraCore.is_null(request.task_cps):
            query['TaskCps'] = request.task_cps
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_start_time):
            query['TaskStartTime'] = request.task_start_time
        if not DaraCore.is_null(request.virtual_number):
            query['VirtualNumber'] = request.virtual_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAiCallTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAiCallTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ai_call_task(
        self,
        request: main_models.CreateAiCallTaskRequest,
    ) -> main_models.CreateAiCallTaskResponse:
        runtime = RuntimeOptions()
        return self.create_ai_call_task_with_options(request, runtime)

    async def create_ai_call_task_async(
        self,
        request: main_models.CreateAiCallTaskRequest,
    ) -> main_models.CreateAiCallTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_ai_call_task_with_options_async(request, runtime)

    def create_ai_outbound_task_with_options(
        self,
        tmp_req: main_models.CreateAiOutboundTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAiOutboundTaskResponse:
        tmp_req.validate()
        request = main_models.CreateAiOutboundTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.outbound_nums):
            request.outbound_nums_shrink = Utils.array_to_string_with_specified_style(tmp_req.outbound_nums, 'OutboundNums', 'json')
        if not DaraCore.is_null(tmp_req.recall_rule):
            request.recall_rule_shrink = Utils.array_to_string_with_specified_style(tmp_req.recall_rule, 'RecallRule', 'json')
        query = {}
        if not DaraCore.is_null(request.concurrent_rate):
            query['ConcurrentRate'] = request.concurrent_rate
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.execution_time):
            query['ExecutionTime'] = request.execution_time
        if not DaraCore.is_null(request.forecast_call_rate):
            query['ForecastCallRate'] = request.forecast_call_rate
        if not DaraCore.is_null(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.num_repeated):
            query['NumRepeated'] = request.num_repeated
        if not DaraCore.is_null(request.outbound_nums_shrink):
            query['OutboundNums'] = request.outbound_nums_shrink
        if not DaraCore.is_null(request.recall_rule_shrink):
            query['RecallRule'] = request.recall_rule_shrink
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAiOutboundTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAiOutboundTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ai_outbound_task_with_options_async(
        self,
        tmp_req: main_models.CreateAiOutboundTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAiOutboundTaskResponse:
        tmp_req.validate()
        request = main_models.CreateAiOutboundTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.outbound_nums):
            request.outbound_nums_shrink = Utils.array_to_string_with_specified_style(tmp_req.outbound_nums, 'OutboundNums', 'json')
        if not DaraCore.is_null(tmp_req.recall_rule):
            request.recall_rule_shrink = Utils.array_to_string_with_specified_style(tmp_req.recall_rule, 'RecallRule', 'json')
        query = {}
        if not DaraCore.is_null(request.concurrent_rate):
            query['ConcurrentRate'] = request.concurrent_rate
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.execution_time):
            query['ExecutionTime'] = request.execution_time
        if not DaraCore.is_null(request.forecast_call_rate):
            query['ForecastCallRate'] = request.forecast_call_rate
        if not DaraCore.is_null(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.num_repeated):
            query['NumRepeated'] = request.num_repeated
        if not DaraCore.is_null(request.outbound_nums_shrink):
            query['OutboundNums'] = request.outbound_nums_shrink
        if not DaraCore.is_null(request.recall_rule_shrink):
            query['RecallRule'] = request.recall_rule_shrink
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAiOutboundTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAiOutboundTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ai_outbound_task(
        self,
        request: main_models.CreateAiOutboundTaskRequest,
    ) -> main_models.CreateAiOutboundTaskResponse:
        runtime = RuntimeOptions()
        return self.create_ai_outbound_task_with_options(request, runtime)

    async def create_ai_outbound_task_async(
        self,
        request: main_models.CreateAiOutboundTaskRequest,
    ) -> main_models.CreateAiOutboundTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_ai_outbound_task_with_options_async(request, runtime)

    def create_ai_outbound_task_batch_with_options(
        self,
        request: main_models.CreateAiOutboundTaskBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAiOutboundTaskBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAiOutboundTaskBatch',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAiOutboundTaskBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ai_outbound_task_batch_with_options_async(
        self,
        request: main_models.CreateAiOutboundTaskBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAiOutboundTaskBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAiOutboundTaskBatch',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAiOutboundTaskBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ai_outbound_task_batch(
        self,
        request: main_models.CreateAiOutboundTaskBatchRequest,
    ) -> main_models.CreateAiOutboundTaskBatchResponse:
        runtime = RuntimeOptions()
        return self.create_ai_outbound_task_batch_with_options(request, runtime)

    async def create_ai_outbound_task_batch_async(
        self,
        request: main_models.CreateAiOutboundTaskBatchRequest,
    ) -> main_models.CreateAiOutboundTaskBatchResponse:
        runtime = RuntimeOptions()
        return await self.create_ai_outbound_task_batch_with_options_async(request, runtime)

    def create_department_with_options(
        self,
        request: main_models.CreateDepartmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDepartmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.department_name):
            query['DepartmentName'] = request.department_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDepartment',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDepartmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_department_with_options_async(
        self,
        request: main_models.CreateDepartmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDepartmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.department_name):
            query['DepartmentName'] = request.department_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDepartment',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDepartmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_department(
        self,
        request: main_models.CreateDepartmentRequest,
    ) -> main_models.CreateDepartmentResponse:
        runtime = RuntimeOptions()
        return self.create_department_with_options(request, runtime)

    async def create_department_async(
        self,
        request: main_models.CreateDepartmentRequest,
    ) -> main_models.CreateDepartmentResponse:
        runtime = RuntimeOptions()
        return await self.create_department_with_options_async(request, runtime)

    def create_outbound_task_with_options(
        self,
        request: main_models.CreateOutboundTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOutboundTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ani):
            query['Ani'] = request.ani
        if not DaraCore.is_null(request.call_infos):
            query['CallInfos'] = request.call_infos
        if not DaraCore.is_null(request.department_id):
            query['DepartmentId'] = request.department_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ext_attrs):
            query['ExtAttrs'] = request.ext_attrs
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.retry_interval):
            query['RetryInterval'] = request.retry_interval
        if not DaraCore.is_null(request.retry_time):
            query['RetryTime'] = request.retry_time
        if not DaraCore.is_null(request.skill_group):
            query['SkillGroup'] = request.skill_group
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOutboundTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOutboundTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_outbound_task_with_options_async(
        self,
        request: main_models.CreateOutboundTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOutboundTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ani):
            query['Ani'] = request.ani
        if not DaraCore.is_null(request.call_infos):
            query['CallInfos'] = request.call_infos
        if not DaraCore.is_null(request.department_id):
            query['DepartmentId'] = request.department_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ext_attrs):
            query['ExtAttrs'] = request.ext_attrs
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.retry_interval):
            query['RetryInterval'] = request.retry_interval
        if not DaraCore.is_null(request.retry_time):
            query['RetryTime'] = request.retry_time
        if not DaraCore.is_null(request.skill_group):
            query['SkillGroup'] = request.skill_group
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOutboundTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOutboundTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_outbound_task(
        self,
        request: main_models.CreateOutboundTaskRequest,
    ) -> main_models.CreateOutboundTaskResponse:
        runtime = RuntimeOptions()
        return self.create_outbound_task_with_options(request, runtime)

    async def create_outbound_task_async(
        self,
        request: main_models.CreateOutboundTaskRequest,
    ) -> main_models.CreateOutboundTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_outbound_task_with_options_async(request, runtime)

    def create_quality_project_with_options(
        self,
        request: main_models.CreateQualityProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQualityProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.analysis_ids):
            body['AnalysisIds'] = request.analysis_ids
        if not DaraCore.is_null(request.channel_touch_type):
            body['ChannelTouchType'] = request.channel_touch_type
        if not DaraCore.is_null(request.check_freq_type):
            body['CheckFreqType'] = request.check_freq_type
        if not DaraCore.is_null(request.dep_list):
            body['DepList'] = request.dep_list
        if not DaraCore.is_null(request.group_list):
            body['GroupList'] = request.group_list
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.scope_type):
            body['ScopeType'] = request.scope_type
        if not DaraCore.is_null(request.servicer_list):
            body['ServicerList'] = request.servicer_list
        if not DaraCore.is_null(request.time_range_end):
            body['TimeRangeEnd'] = request.time_range_end
        if not DaraCore.is_null(request.time_range_start):
            body['TimeRangeStart'] = request.time_range_start
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateQualityProject',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQualityProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_quality_project_with_options_async(
        self,
        request: main_models.CreateQualityProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQualityProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.analysis_ids):
            body['AnalysisIds'] = request.analysis_ids
        if not DaraCore.is_null(request.channel_touch_type):
            body['ChannelTouchType'] = request.channel_touch_type
        if not DaraCore.is_null(request.check_freq_type):
            body['CheckFreqType'] = request.check_freq_type
        if not DaraCore.is_null(request.dep_list):
            body['DepList'] = request.dep_list
        if not DaraCore.is_null(request.group_list):
            body['GroupList'] = request.group_list
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.scope_type):
            body['ScopeType'] = request.scope_type
        if not DaraCore.is_null(request.servicer_list):
            body['ServicerList'] = request.servicer_list
        if not DaraCore.is_null(request.time_range_end):
            body['TimeRangeEnd'] = request.time_range_end
        if not DaraCore.is_null(request.time_range_start):
            body['TimeRangeStart'] = request.time_range_start
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateQualityProject',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQualityProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_quality_project(
        self,
        request: main_models.CreateQualityProjectRequest,
    ) -> main_models.CreateQualityProjectResponse:
        runtime = RuntimeOptions()
        return self.create_quality_project_with_options(request, runtime)

    async def create_quality_project_async(
        self,
        request: main_models.CreateQualityProjectRequest,
    ) -> main_models.CreateQualityProjectResponse:
        runtime = RuntimeOptions()
        return await self.create_quality_project_with_options_async(request, runtime)

    def create_quality_rule_with_options(
        self,
        request: main_models.CreateQualityRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQualityRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.key_words):
            body['KeyWords'] = request.key_words
        if not DaraCore.is_null(request.match_type):
            body['MatchType'] = request.match_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.rule_tag):
            body['RuleTag'] = request.rule_tag
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateQualityRule',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQualityRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_quality_rule_with_options_async(
        self,
        request: main_models.CreateQualityRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQualityRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.key_words):
            body['KeyWords'] = request.key_words
        if not DaraCore.is_null(request.match_type):
            body['MatchType'] = request.match_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.rule_tag):
            body['RuleTag'] = request.rule_tag
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateQualityRule',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQualityRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_quality_rule(
        self,
        request: main_models.CreateQualityRuleRequest,
    ) -> main_models.CreateQualityRuleResponse:
        runtime = RuntimeOptions()
        return self.create_quality_rule_with_options(request, runtime)

    async def create_quality_rule_async(
        self,
        request: main_models.CreateQualityRuleRequest,
    ) -> main_models.CreateQualityRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_quality_rule_with_options_async(request, runtime)

    def create_skill_group_with_options(
        self,
        request: main_models.CreateSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSkillGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channel_type):
            body['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.department_id):
            body['DepartmentId'] = request.department_id
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_name):
            body['SkillGroupName'] = request.skill_group_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSkillGroup',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_skill_group_with_options_async(
        self,
        request: main_models.CreateSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSkillGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channel_type):
            body['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.department_id):
            body['DepartmentId'] = request.department_id
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_name):
            body['SkillGroupName'] = request.skill_group_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSkillGroup',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_skill_group(
        self,
        request: main_models.CreateSkillGroupRequest,
    ) -> main_models.CreateSkillGroupResponse:
        runtime = RuntimeOptions()
        return self.create_skill_group_with_options(request, runtime)

    async def create_skill_group_async(
        self,
        request: main_models.CreateSkillGroupRequest,
    ) -> main_models.CreateSkillGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_skill_group_with_options_async(request, runtime)

    def create_task_with_options(
        self,
        request: main_models.CreateTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_string):
            query['CallString'] = request.call_string
        if not DaraCore.is_null(request.call_string_type):
            query['CallStringType'] = request.call_string_type
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.retry_count):
            query['RetryCount'] = request.retry_count
        if not DaraCore.is_null(request.retry_flag):
            query['RetryFlag'] = request.retry_flag
        if not DaraCore.is_null(request.retry_interval):
            query['RetryInterval'] = request.retry_interval
        if not DaraCore.is_null(request.retry_status_code):
            query['RetryStatusCode'] = request.retry_status_code
        if not DaraCore.is_null(request.robot_id):
            query['RobotId'] = request.robot_id
        if not DaraCore.is_null(request.seat_count):
            query['SeatCount'] = request.seat_count
        if not DaraCore.is_null(request.start_now):
            query['StartNow'] = request.start_now
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.work_day):
            query['WorkDay'] = request.work_day
        if not DaraCore.is_null(request.work_time_list):
            query['WorkTimeList'] = request.work_time_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_task_with_options_async(
        self,
        request: main_models.CreateTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_string):
            query['CallString'] = request.call_string
        if not DaraCore.is_null(request.call_string_type):
            query['CallStringType'] = request.call_string_type
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.retry_count):
            query['RetryCount'] = request.retry_count
        if not DaraCore.is_null(request.retry_flag):
            query['RetryFlag'] = request.retry_flag
        if not DaraCore.is_null(request.retry_interval):
            query['RetryInterval'] = request.retry_interval
        if not DaraCore.is_null(request.retry_status_code):
            query['RetryStatusCode'] = request.retry_status_code
        if not DaraCore.is_null(request.robot_id):
            query['RobotId'] = request.robot_id
        if not DaraCore.is_null(request.seat_count):
            query['SeatCount'] = request.seat_count
        if not DaraCore.is_null(request.start_now):
            query['StartNow'] = request.start_now
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.work_day):
            query['WorkDay'] = request.work_day
        if not DaraCore.is_null(request.work_time_list):
            query['WorkTimeList'] = request.work_time_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_task(
        self,
        request: main_models.CreateTaskRequest,
    ) -> main_models.CreateTaskResponse:
        runtime = RuntimeOptions()
        return self.create_task_with_options(request, runtime)

    async def create_task_async(
        self,
        request: main_models.CreateTaskRequest,
    ) -> main_models.CreateTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_task_with_options_async(request, runtime)

    def create_third_sso_agent_with_options(
        self,
        request: main_models.CreateThirdSsoAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateThirdSsoAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        body_flat = {}
        if not DaraCore.is_null(request.role_ids):
            body_flat['RoleIds'] = request.role_ids
        if not DaraCore.is_null(request.skill_group_ids):
            body_flat['SkillGroupIds'] = request.skill_group_ids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateThirdSsoAgent',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateThirdSsoAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_third_sso_agent_with_options_async(
        self,
        request: main_models.CreateThirdSsoAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateThirdSsoAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        body_flat = {}
        if not DaraCore.is_null(request.role_ids):
            body_flat['RoleIds'] = request.role_ids
        if not DaraCore.is_null(request.skill_group_ids):
            body_flat['SkillGroupIds'] = request.skill_group_ids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateThirdSsoAgent',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateThirdSsoAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_third_sso_agent(
        self,
        request: main_models.CreateThirdSsoAgentRequest,
    ) -> main_models.CreateThirdSsoAgentResponse:
        runtime = RuntimeOptions()
        return self.create_third_sso_agent_with_options(request, runtime)

    async def create_third_sso_agent_async(
        self,
        request: main_models.CreateThirdSsoAgentRequest,
    ) -> main_models.CreateThirdSsoAgentResponse:
        runtime = RuntimeOptions()
        return await self.create_third_sso_agent_with_options_async(request, runtime)

    def delete_agent_with_options(
        self,
        request: main_models.DeleteAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgent',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_agent_with_options_async(
        self,
        request: main_models.DeleteAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgent',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_agent(
        self,
        request: main_models.DeleteAgentRequest,
    ) -> main_models.DeleteAgentResponse:
        runtime = RuntimeOptions()
        return self.delete_agent_with_options(request, runtime)

    async def delete_agent_async(
        self,
        request: main_models.DeleteAgentRequest,
    ) -> main_models.DeleteAgentResponse:
        runtime = RuntimeOptions()
        return await self.delete_agent_with_options_async(request, runtime)

    def delete_ai_outbound_task_with_options(
        self,
        request: main_models.DeleteAiOutboundTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAiOutboundTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAiOutboundTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAiOutboundTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ai_outbound_task_with_options_async(
        self,
        request: main_models.DeleteAiOutboundTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAiOutboundTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAiOutboundTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAiOutboundTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ai_outbound_task(
        self,
        request: main_models.DeleteAiOutboundTaskRequest,
    ) -> main_models.DeleteAiOutboundTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_ai_outbound_task_with_options(request, runtime)

    async def delete_ai_outbound_task_async(
        self,
        request: main_models.DeleteAiOutboundTaskRequest,
    ) -> main_models.DeleteAiOutboundTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_ai_outbound_task_with_options_async(request, runtime)

    def delete_department_with_options(
        self,
        request: main_models.DeleteDepartmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDepartmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.department_id):
            query['DepartmentId'] = request.department_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDepartment',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDepartmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_department_with_options_async(
        self,
        request: main_models.DeleteDepartmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDepartmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.department_id):
            query['DepartmentId'] = request.department_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDepartment',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDepartmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_department(
        self,
        request: main_models.DeleteDepartmentRequest,
    ) -> main_models.DeleteDepartmentResponse:
        runtime = RuntimeOptions()
        return self.delete_department_with_options(request, runtime)

    async def delete_department_async(
        self,
        request: main_models.DeleteDepartmentRequest,
    ) -> main_models.DeleteDepartmentResponse:
        runtime = RuntimeOptions()
        return await self.delete_department_with_options_async(request, runtime)

    def delete_hotline_number_with_options(
        self,
        request: main_models.DeleteHotlineNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHotlineNumberResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotline_number):
            body['HotlineNumber'] = request.hotline_number
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHotlineNumber',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHotlineNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hotline_number_with_options_async(
        self,
        request: main_models.DeleteHotlineNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHotlineNumberResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hotline_number):
            body['HotlineNumber'] = request.hotline_number
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHotlineNumber',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHotlineNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hotline_number(
        self,
        request: main_models.DeleteHotlineNumberRequest,
    ) -> main_models.DeleteHotlineNumberResponse:
        runtime = RuntimeOptions()
        return self.delete_hotline_number_with_options(request, runtime)

    async def delete_hotline_number_async(
        self,
        request: main_models.DeleteHotlineNumberRequest,
    ) -> main_models.DeleteHotlineNumberResponse:
        runtime = RuntimeOptions()
        return await self.delete_hotline_number_with_options_async(request, runtime)

    def delete_outbound_task_with_options(
        self,
        request: main_models.DeleteOutboundTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOutboundTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.outbound_task_id):
            query['OutboundTaskId'] = request.outbound_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOutboundTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOutboundTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_outbound_task_with_options_async(
        self,
        request: main_models.DeleteOutboundTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOutboundTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.outbound_task_id):
            query['OutboundTaskId'] = request.outbound_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOutboundTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOutboundTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_outbound_task(
        self,
        request: main_models.DeleteOutboundTaskRequest,
    ) -> main_models.DeleteOutboundTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_outbound_task_with_options(request, runtime)

    async def delete_outbound_task_async(
        self,
        request: main_models.DeleteOutboundTaskRequest,
    ) -> main_models.DeleteOutboundTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_outbound_task_with_options_async(request, runtime)

    def delete_outer_account_with_options(
        self,
        request: main_models.DeleteOuterAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOuterAccountResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOuterAccount',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOuterAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_outer_account_with_options_async(
        self,
        request: main_models.DeleteOuterAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOuterAccountResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOuterAccount',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOuterAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_outer_account(
        self,
        request: main_models.DeleteOuterAccountRequest,
    ) -> main_models.DeleteOuterAccountResponse:
        runtime = RuntimeOptions()
        return self.delete_outer_account_with_options(request, runtime)

    async def delete_outer_account_async(
        self,
        request: main_models.DeleteOuterAccountRequest,
    ) -> main_models.DeleteOuterAccountResponse:
        runtime = RuntimeOptions()
        return await self.delete_outer_account_with_options_async(request, runtime)

    def delete_quality_project_with_options(
        self,
        request: main_models.DeleteQualityProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQualityProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQualityProject',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQualityProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_quality_project_with_options_async(
        self,
        request: main_models.DeleteQualityProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQualityProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQualityProject',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQualityProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_quality_project(
        self,
        request: main_models.DeleteQualityProjectRequest,
    ) -> main_models.DeleteQualityProjectResponse:
        runtime = RuntimeOptions()
        return self.delete_quality_project_with_options(request, runtime)

    async def delete_quality_project_async(
        self,
        request: main_models.DeleteQualityProjectRequest,
    ) -> main_models.DeleteQualityProjectResponse:
        runtime = RuntimeOptions()
        return await self.delete_quality_project_with_options_async(request, runtime)

    def delete_quality_rule_with_options(
        self,
        request: main_models.DeleteQualityRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQualityRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQualityRule',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQualityRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_quality_rule_with_options_async(
        self,
        request: main_models.DeleteQualityRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQualityRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQualityRule',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQualityRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_quality_rule(
        self,
        request: main_models.DeleteQualityRuleRequest,
    ) -> main_models.DeleteQualityRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_quality_rule_with_options(request, runtime)

    async def delete_quality_rule_async(
        self,
        request: main_models.DeleteQualityRuleRequest,
    ) -> main_models.DeleteQualityRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_quality_rule_with_options_async(request, runtime)

    def delete_skill_group_with_options(
        self,
        request: main_models.DeleteSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSkillGroupResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSkillGroup',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_skill_group_with_options_async(
        self,
        request: main_models.DeleteSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSkillGroupResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSkillGroup',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_skill_group(
        self,
        request: main_models.DeleteSkillGroupRequest,
    ) -> main_models.DeleteSkillGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_skill_group_with_options(request, runtime)

    async def delete_skill_group_async(
        self,
        request: main_models.DeleteSkillGroupRequest,
    ) -> main_models.DeleteSkillGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_skill_group_with_options_async(request, runtime)

    def describe_record_data_with_options(
        self,
        request: main_models.DescribeRecordDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecordDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.acid):
            query['Acid'] = request.acid
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sec_level):
            query['SecLevel'] = request.sec_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecordData',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecordDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_record_data_with_options_async(
        self,
        request: main_models.DescribeRecordDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecordDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.acid):
            query['Acid'] = request.acid
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sec_level):
            query['SecLevel'] = request.sec_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecordData',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecordDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_record_data(
        self,
        request: main_models.DescribeRecordDataRequest,
    ) -> main_models.DescribeRecordDataResponse:
        runtime = RuntimeOptions()
        return self.describe_record_data_with_options(request, runtime)

    async def describe_record_data_async(
        self,
        request: main_models.DescribeRecordDataRequest,
    ) -> main_models.DescribeRecordDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_record_data_with_options_async(request, runtime)

    def edit_quality_project_with_options(
        self,
        request: main_models.EditQualityProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditQualityProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.analysis_ids):
            query['AnalysisIds'] = request.analysis_ids
        if not DaraCore.is_null(request.channel_touch_type):
            query['ChannelTouchType'] = request.channel_touch_type
        if not DaraCore.is_null(request.check_freq_type):
            query['CheckFreqType'] = request.check_freq_type
        if not DaraCore.is_null(request.dep_list):
            query['DepList'] = request.dep_list
        if not DaraCore.is_null(request.group_list):
            query['GroupList'] = request.group_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_version):
            query['ProjectVersion'] = request.project_version
        if not DaraCore.is_null(request.scope_type):
            query['ScopeType'] = request.scope_type
        if not DaraCore.is_null(request.servicer_list):
            query['ServicerList'] = request.servicer_list
        if not DaraCore.is_null(request.time_range_end):
            query['TimeRangeEnd'] = request.time_range_end
        if not DaraCore.is_null(request.time_range_start):
            query['TimeRangeStart'] = request.time_range_start
        body = {}
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EditQualityProject',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditQualityProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_quality_project_with_options_async(
        self,
        request: main_models.EditQualityProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditQualityProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.analysis_ids):
            query['AnalysisIds'] = request.analysis_ids
        if not DaraCore.is_null(request.channel_touch_type):
            query['ChannelTouchType'] = request.channel_touch_type
        if not DaraCore.is_null(request.check_freq_type):
            query['CheckFreqType'] = request.check_freq_type
        if not DaraCore.is_null(request.dep_list):
            query['DepList'] = request.dep_list
        if not DaraCore.is_null(request.group_list):
            query['GroupList'] = request.group_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_version):
            query['ProjectVersion'] = request.project_version
        if not DaraCore.is_null(request.scope_type):
            query['ScopeType'] = request.scope_type
        if not DaraCore.is_null(request.servicer_list):
            query['ServicerList'] = request.servicer_list
        if not DaraCore.is_null(request.time_range_end):
            query['TimeRangeEnd'] = request.time_range_end
        if not DaraCore.is_null(request.time_range_start):
            query['TimeRangeStart'] = request.time_range_start
        body = {}
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EditQualityProject',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditQualityProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_quality_project(
        self,
        request: main_models.EditQualityProjectRequest,
    ) -> main_models.EditQualityProjectResponse:
        runtime = RuntimeOptions()
        return self.edit_quality_project_with_options(request, runtime)

    async def edit_quality_project_async(
        self,
        request: main_models.EditQualityProjectRequest,
    ) -> main_models.EditQualityProjectResponse:
        runtime = RuntimeOptions()
        return await self.edit_quality_project_with_options_async(request, runtime)

    def edit_quality_rule_with_options(
        self,
        request: main_models.EditQualityRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditQualityRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.key_words):
            body['KeyWords'] = request.key_words
        if not DaraCore.is_null(request.match_type):
            body['MatchType'] = request.match_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.quality_rule_id):
            body['QualityRuleId'] = request.quality_rule_id
        if not DaraCore.is_null(request.rule_tag):
            body['RuleTag'] = request.rule_tag
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EditQualityRule',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditQualityRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_quality_rule_with_options_async(
        self,
        request: main_models.EditQualityRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditQualityRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.key_words):
            body['KeyWords'] = request.key_words
        if not DaraCore.is_null(request.match_type):
            body['MatchType'] = request.match_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.quality_rule_id):
            body['QualityRuleId'] = request.quality_rule_id
        if not DaraCore.is_null(request.rule_tag):
            body['RuleTag'] = request.rule_tag
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EditQualityRule',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditQualityRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_quality_rule(
        self,
        request: main_models.EditQualityRuleRequest,
    ) -> main_models.EditQualityRuleResponse:
        runtime = RuntimeOptions()
        return self.edit_quality_rule_with_options(request, runtime)

    async def edit_quality_rule_async(
        self,
        request: main_models.EditQualityRuleRequest,
    ) -> main_models.EditQualityRuleResponse:
        runtime = RuntimeOptions()
        return await self.edit_quality_rule_with_options_async(request, runtime)

    def edit_quality_rule_tag_with_options(
        self,
        request: main_models.EditQualityRuleTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditQualityRuleTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.analysis_types):
            query['AnalysisTypes'] = request.analysis_types
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EditQualityRuleTag',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditQualityRuleTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_quality_rule_tag_with_options_async(
        self,
        request: main_models.EditQualityRuleTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditQualityRuleTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.analysis_types):
            query['AnalysisTypes'] = request.analysis_types
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EditQualityRuleTag',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditQualityRuleTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_quality_rule_tag(
        self,
        request: main_models.EditQualityRuleTagRequest,
    ) -> main_models.EditQualityRuleTagResponse:
        runtime = RuntimeOptions()
        return self.edit_quality_rule_tag_with_options(request, runtime)

    async def edit_quality_rule_tag_async(
        self,
        request: main_models.EditQualityRuleTagRequest,
    ) -> main_models.EditQualityRuleTagResponse:
        runtime = RuntimeOptions()
        return await self.edit_quality_rule_tag_with_options_async(request, runtime)

    def encrypt_phone_num_with_options(
        self,
        request: main_models.EncryptPhoneNumRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EncryptPhoneNumResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EncryptPhoneNum',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EncryptPhoneNumResponse(),
            self.call_api(params, req, runtime)
        )

    async def encrypt_phone_num_with_options_async(
        self,
        request: main_models.EncryptPhoneNumRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EncryptPhoneNumResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EncryptPhoneNum',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EncryptPhoneNumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def encrypt_phone_num(
        self,
        request: main_models.EncryptPhoneNumRequest,
    ) -> main_models.EncryptPhoneNumResponse:
        runtime = RuntimeOptions()
        return self.encrypt_phone_num_with_options(request, runtime)

    async def encrypt_phone_num_async(
        self,
        request: main_models.EncryptPhoneNumRequest,
    ) -> main_models.EncryptPhoneNumResponse:
        runtime = RuntimeOptions()
        return await self.encrypt_phone_num_with_options_async(request, runtime)

    def fetch_call_with_options(
        self,
        request: main_models.FetchCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FetchCallResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.call_id):
            body['CallId'] = request.call_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not DaraCore.is_null(request.hold_connection_id):
            body['HoldConnectionId'] = request.hold_connection_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FetchCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FetchCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def fetch_call_with_options_async(
        self,
        request: main_models.FetchCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FetchCallResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.call_id):
            body['CallId'] = request.call_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not DaraCore.is_null(request.hold_connection_id):
            body['HoldConnectionId'] = request.hold_connection_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FetchCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FetchCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fetch_call(
        self,
        request: main_models.FetchCallRequest,
    ) -> main_models.FetchCallResponse:
        runtime = RuntimeOptions()
        return self.fetch_call_with_options(request, runtime)

    async def fetch_call_async(
        self,
        request: main_models.FetchCallRequest,
    ) -> main_models.FetchCallResponse:
        runtime = RuntimeOptions()
        return await self.fetch_call_with_options_async(request, runtime)

    def finish_hotline_service_with_options(
        self,
        request: main_models.FinishHotlineServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FinishHotlineServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FinishHotlineService',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FinishHotlineServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def finish_hotline_service_with_options_async(
        self,
        request: main_models.FinishHotlineServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FinishHotlineServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FinishHotlineService',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FinishHotlineServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def finish_hotline_service(
        self,
        request: main_models.FinishHotlineServiceRequest,
    ) -> main_models.FinishHotlineServiceResponse:
        runtime = RuntimeOptions()
        return self.finish_hotline_service_with_options(request, runtime)

    async def finish_hotline_service_async(
        self,
        request: main_models.FinishHotlineServiceRequest,
    ) -> main_models.FinishHotlineServiceResponse:
        runtime = RuntimeOptions()
        return await self.finish_hotline_service_with_options_async(request, runtime)

    def generate_web_socket_sign_with_options(
        self,
        request: main_models.GenerateWebSocketSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateWebSocketSignResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateWebSocketSign',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateWebSocketSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_web_socket_sign_with_options_async(
        self,
        request: main_models.GenerateWebSocketSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateWebSocketSignResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateWebSocketSign',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateWebSocketSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_web_socket_sign(
        self,
        request: main_models.GenerateWebSocketSignRequest,
    ) -> main_models.GenerateWebSocketSignResponse:
        runtime = RuntimeOptions()
        return self.generate_web_socket_sign_with_options(request, runtime)

    async def generate_web_socket_sign_async(
        self,
        request: main_models.GenerateWebSocketSignRequest,
    ) -> main_models.GenerateWebSocketSignResponse:
        runtime = RuntimeOptions()
        return await self.generate_web_socket_sign_with_options_async(request, runtime)

    def get_agent_with_options(
        self,
        request: main_models.GetAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgent',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
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
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgent',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
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

    def get_agent_basis_status_with_options(
        self,
        tmp_req: main_models.GetAgentBasisStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentBasisStatusResponse:
        tmp_req.validate()
        request = main_models.GetAgentBasisStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentBasisStatus',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentBasisStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_basis_status_with_options_async(
        self,
        tmp_req: main_models.GetAgentBasisStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentBasisStatusResponse:
        tmp_req.validate()
        request = main_models.GetAgentBasisStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentBasisStatus',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentBasisStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_basis_status(
        self,
        request: main_models.GetAgentBasisStatusRequest,
    ) -> main_models.GetAgentBasisStatusResponse:
        runtime = RuntimeOptions()
        return self.get_agent_basis_status_with_options(request, runtime)

    async def get_agent_basis_status_async(
        self,
        request: main_models.GetAgentBasisStatusRequest,
    ) -> main_models.GetAgentBasisStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_agent_basis_status_with_options_async(request, runtime)

    def get_agent_by_id_with_options(
        self,
        request: main_models.GetAgentByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentByIdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentById',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_by_id_with_options_async(
        self,
        request: main_models.GetAgentByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentByIdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentById',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_by_id(
        self,
        request: main_models.GetAgentByIdRequest,
    ) -> main_models.GetAgentByIdResponse:
        runtime = RuntimeOptions()
        return self.get_agent_by_id_with_options(request, runtime)

    async def get_agent_by_id_async(
        self,
        request: main_models.GetAgentByIdRequest,
    ) -> main_models.GetAgentByIdResponse:
        runtime = RuntimeOptions()
        return await self.get_agent_by_id_with_options_async(request, runtime)

    def get_agent_detail_report_with_options(
        self,
        tmp_req: main_models.GetAgentDetailReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentDetailReportResponse:
        tmp_req.validate()
        request = main_models.GetAgentDetailReportShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentDetailReport',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentDetailReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_detail_report_with_options_async(
        self,
        tmp_req: main_models.GetAgentDetailReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentDetailReportResponse:
        tmp_req.validate()
        request = main_models.GetAgentDetailReportShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentDetailReport',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentDetailReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_detail_report(
        self,
        request: main_models.GetAgentDetailReportRequest,
    ) -> main_models.GetAgentDetailReportResponse:
        runtime = RuntimeOptions()
        return self.get_agent_detail_report_with_options(request, runtime)

    async def get_agent_detail_report_async(
        self,
        request: main_models.GetAgentDetailReportRequest,
    ) -> main_models.GetAgentDetailReportResponse:
        runtime = RuntimeOptions()
        return await self.get_agent_detail_report_with_options_async(request, runtime)

    def get_agent_index_real_time_with_options(
        self,
        request: main_models.GetAgentIndexRealTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentIndexRealTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dep_ids):
            query['DepIds'] = request.dep_ids
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentIndexRealTime',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentIndexRealTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_index_real_time_with_options_async(
        self,
        request: main_models.GetAgentIndexRealTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentIndexRealTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dep_ids):
            query['DepIds'] = request.dep_ids
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentIndexRealTime',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentIndexRealTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_index_real_time(
        self,
        request: main_models.GetAgentIndexRealTimeRequest,
    ) -> main_models.GetAgentIndexRealTimeResponse:
        runtime = RuntimeOptions()
        return self.get_agent_index_real_time_with_options(request, runtime)

    async def get_agent_index_real_time_async(
        self,
        request: main_models.GetAgentIndexRealTimeRequest,
    ) -> main_models.GetAgentIndexRealTimeResponse:
        runtime = RuntimeOptions()
        return await self.get_agent_index_real_time_with_options_async(request, runtime)

    def get_agent_service_status_with_options(
        self,
        tmp_req: main_models.GetAgentServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentServiceStatusResponse:
        tmp_req.validate()
        request = main_models.GetAgentServiceStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentServiceStatus',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_service_status_with_options_async(
        self,
        tmp_req: main_models.GetAgentServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentServiceStatusResponse:
        tmp_req.validate()
        request = main_models.GetAgentServiceStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentServiceStatus',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_service_status(
        self,
        request: main_models.GetAgentServiceStatusRequest,
    ) -> main_models.GetAgentServiceStatusResponse:
        runtime = RuntimeOptions()
        return self.get_agent_service_status_with_options(request, runtime)

    async def get_agent_service_status_async(
        self,
        request: main_models.GetAgentServiceStatusRequest,
    ) -> main_models.GetAgentServiceStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_agent_service_status_with_options_async(request, runtime)

    def get_agent_statistics_with_options(
        self,
        tmp_req: main_models.GetAgentStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentStatisticsResponse:
        tmp_req.validate()
        request = main_models.GetAgentStatisticsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentStatistics',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_statistics_with_options_async(
        self,
        tmp_req: main_models.GetAgentStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentStatisticsResponse:
        tmp_req.validate()
        request = main_models.GetAgentStatisticsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentStatistics',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_statistics(
        self,
        request: main_models.GetAgentStatisticsRequest,
    ) -> main_models.GetAgentStatisticsResponse:
        runtime = RuntimeOptions()
        return self.get_agent_statistics_with_options(request, runtime)

    async def get_agent_statistics_async(
        self,
        request: main_models.GetAgentStatisticsRequest,
    ) -> main_models.GetAgentStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.get_agent_statistics_with_options_async(request, runtime)

    def get_ai_outbound_task_biz_data_with_options(
        self,
        request: main_models.GetAiOutboundTaskBizDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAiOutboundTaskBizDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAiOutboundTaskBizData',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAiOutboundTaskBizDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ai_outbound_task_biz_data_with_options_async(
        self,
        request: main_models.GetAiOutboundTaskBizDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAiOutboundTaskBizDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAiOutboundTaskBizData',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAiOutboundTaskBizDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ai_outbound_task_biz_data(
        self,
        request: main_models.GetAiOutboundTaskBizDataRequest,
    ) -> main_models.GetAiOutboundTaskBizDataResponse:
        runtime = RuntimeOptions()
        return self.get_ai_outbound_task_biz_data_with_options(request, runtime)

    async def get_ai_outbound_task_biz_data_async(
        self,
        request: main_models.GetAiOutboundTaskBizDataRequest,
    ) -> main_models.GetAiOutboundTaskBizDataResponse:
        runtime = RuntimeOptions()
        return await self.get_ai_outbound_task_biz_data_with_options_async(request, runtime)

    def get_ai_outbound_task_detail_with_options(
        self,
        request: main_models.GetAiOutboundTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAiOutboundTaskDetailResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAiOutboundTaskDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAiOutboundTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ai_outbound_task_detail_with_options_async(
        self,
        request: main_models.GetAiOutboundTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAiOutboundTaskDetailResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAiOutboundTaskDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAiOutboundTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ai_outbound_task_detail(
        self,
        request: main_models.GetAiOutboundTaskDetailRequest,
    ) -> main_models.GetAiOutboundTaskDetailResponse:
        runtime = RuntimeOptions()
        return self.get_ai_outbound_task_detail_with_options(request, runtime)

    async def get_ai_outbound_task_detail_async(
        self,
        request: main_models.GetAiOutboundTaskDetailRequest,
    ) -> main_models.GetAiOutboundTaskDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_ai_outbound_task_detail_with_options_async(request, runtime)

    def get_ai_outbound_task_exec_detail_with_options(
        self,
        request: main_models.GetAiOutboundTaskExecDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAiOutboundTaskExecDetailResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAiOutboundTaskExecDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAiOutboundTaskExecDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ai_outbound_task_exec_detail_with_options_async(
        self,
        request: main_models.GetAiOutboundTaskExecDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAiOutboundTaskExecDetailResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAiOutboundTaskExecDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAiOutboundTaskExecDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ai_outbound_task_exec_detail(
        self,
        request: main_models.GetAiOutboundTaskExecDetailRequest,
    ) -> main_models.GetAiOutboundTaskExecDetailResponse:
        runtime = RuntimeOptions()
        return self.get_ai_outbound_task_exec_detail_with_options(request, runtime)

    async def get_ai_outbound_task_exec_detail_async(
        self,
        request: main_models.GetAiOutboundTaskExecDetailRequest,
    ) -> main_models.GetAiOutboundTaskExecDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_ai_outbound_task_exec_detail_with_options_async(request, runtime)

    def get_ai_outbound_task_list_with_options(
        self,
        request: main_models.GetAiOutboundTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAiOutboundTaskListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAiOutboundTaskList',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAiOutboundTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ai_outbound_task_list_with_options_async(
        self,
        request: main_models.GetAiOutboundTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAiOutboundTaskListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAiOutboundTaskList',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAiOutboundTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ai_outbound_task_list(
        self,
        request: main_models.GetAiOutboundTaskListRequest,
    ) -> main_models.GetAiOutboundTaskListResponse:
        runtime = RuntimeOptions()
        return self.get_ai_outbound_task_list_with_options(request, runtime)

    async def get_ai_outbound_task_list_async(
        self,
        request: main_models.GetAiOutboundTaskListRequest,
    ) -> main_models.GetAiOutboundTaskListResponse:
        runtime = RuntimeOptions()
        return await self.get_ai_outbound_task_list_with_options_async(request, runtime)

    def get_ai_outbound_task_progress_with_options(
        self,
        request: main_models.GetAiOutboundTaskProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAiOutboundTaskProgressResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAiOutboundTaskProgress',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAiOutboundTaskProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ai_outbound_task_progress_with_options_async(
        self,
        request: main_models.GetAiOutboundTaskProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAiOutboundTaskProgressResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAiOutboundTaskProgress',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAiOutboundTaskProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ai_outbound_task_progress(
        self,
        request: main_models.GetAiOutboundTaskProgressRequest,
    ) -> main_models.GetAiOutboundTaskProgressResponse:
        runtime = RuntimeOptions()
        return self.get_ai_outbound_task_progress_with_options(request, runtime)

    async def get_ai_outbound_task_progress_async(
        self,
        request: main_models.GetAiOutboundTaskProgressRequest,
    ) -> main_models.GetAiOutboundTaskProgressResponse:
        runtime = RuntimeOptions()
        return await self.get_ai_outbound_task_progress_with_options_async(request, runtime)

    def get_all_department_with_options(
        self,
        request: main_models.GetAllDepartmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAllDepartmentResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAllDepartment',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAllDepartmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_all_department_with_options_async(
        self,
        request: main_models.GetAllDepartmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAllDepartmentResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAllDepartment',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAllDepartmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_all_department(
        self,
        request: main_models.GetAllDepartmentRequest,
    ) -> main_models.GetAllDepartmentResponse:
        runtime = RuntimeOptions()
        return self.get_all_department_with_options(request, runtime)

    async def get_all_department_async(
        self,
        request: main_models.GetAllDepartmentRequest,
    ) -> main_models.GetAllDepartmentResponse:
        runtime = RuntimeOptions()
        return await self.get_all_department_with_options_async(request, runtime)

    def get_call_dialog_content_with_options(
        self,
        request: main_models.GetCallDialogContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCallDialogContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_date):
            query['CallDate'] = request.call_date
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCallDialogContent',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCallDialogContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_call_dialog_content_with_options_async(
        self,
        request: main_models.GetCallDialogContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCallDialogContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_date):
            query['CallDate'] = request.call_date
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCallDialogContent',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCallDialogContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_call_dialog_content(
        self,
        request: main_models.GetCallDialogContentRequest,
    ) -> main_models.GetCallDialogContentResponse:
        runtime = RuntimeOptions()
        return self.get_call_dialog_content_with_options(request, runtime)

    async def get_call_dialog_content_async(
        self,
        request: main_models.GetCallDialogContentRequest,
    ) -> main_models.GetCallDialogContentResponse:
        runtime = RuntimeOptions()
        return await self.get_call_dialog_content_with_options_async(request, runtime)

    def get_call_sound_record_with_options(
        self,
        request: main_models.GetCallSoundRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCallSoundRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.create_time):
            query['CreateTime'] = request.create_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCallSoundRecord',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCallSoundRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_call_sound_record_with_options_async(
        self,
        request: main_models.GetCallSoundRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCallSoundRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.create_time):
            query['CreateTime'] = request.create_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCallSoundRecord',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCallSoundRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_call_sound_record(
        self,
        request: main_models.GetCallSoundRecordRequest,
    ) -> main_models.GetCallSoundRecordResponse:
        runtime = RuntimeOptions()
        return self.get_call_sound_record_with_options(request, runtime)

    async def get_call_sound_record_async(
        self,
        request: main_models.GetCallSoundRecordRequest,
    ) -> main_models.GetCallSoundRecordResponse:
        runtime = RuntimeOptions()
        return await self.get_call_sound_record_with_options_async(request, runtime)

    def get_config_num_list_with_options(
        self,
        request: main_models.GetConfigNumListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigNumListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConfigNumList',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigNumListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_config_num_list_with_options_async(
        self,
        request: main_models.GetConfigNumListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigNumListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConfigNumList',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigNumListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_config_num_list(
        self,
        request: main_models.GetConfigNumListRequest,
    ) -> main_models.GetConfigNumListResponse:
        runtime = RuntimeOptions()
        return self.get_config_num_list_with_options(request, runtime)

    async def get_config_num_list_async(
        self,
        request: main_models.GetConfigNumListRequest,
    ) -> main_models.GetConfigNumListResponse:
        runtime = RuntimeOptions()
        return await self.get_config_num_list_with_options_async(request, runtime)

    def get_customer_info_with_options(
        self,
        request: main_models.GetCustomerInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomerInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomerInfo',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomerInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_customer_info_with_options_async(
        self,
        request: main_models.GetCustomerInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomerInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomerInfo',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomerInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_customer_info(
        self,
        request: main_models.GetCustomerInfoRequest,
    ) -> main_models.GetCustomerInfoResponse:
        runtime = RuntimeOptions()
        return self.get_customer_info_with_options(request, runtime)

    async def get_customer_info_async(
        self,
        request: main_models.GetCustomerInfoRequest,
    ) -> main_models.GetCustomerInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_customer_info_with_options_async(request, runtime)

    def get_dep_group_tree_data_with_options(
        self,
        request: main_models.GetDepGroupTreeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDepGroupTreeDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDepGroupTreeData',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDepGroupTreeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dep_group_tree_data_with_options_async(
        self,
        request: main_models.GetDepGroupTreeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDepGroupTreeDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDepGroupTreeData',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDepGroupTreeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dep_group_tree_data(
        self,
        request: main_models.GetDepGroupTreeDataRequest,
    ) -> main_models.GetDepGroupTreeDataResponse:
        runtime = RuntimeOptions()
        return self.get_dep_group_tree_data_with_options(request, runtime)

    async def get_dep_group_tree_data_async(
        self,
        request: main_models.GetDepGroupTreeDataRequest,
    ) -> main_models.GetDepGroupTreeDataResponse:
        runtime = RuntimeOptions()
        return await self.get_dep_group_tree_data_with_options_async(request, runtime)

    def get_departmental_latitude_agent_status_with_options(
        self,
        tmp_req: main_models.GetDepartmentalLatitudeAgentStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDepartmentalLatitudeAgentStatusResponse:
        tmp_req.validate()
        request = main_models.GetDepartmentalLatitudeAgentStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDepartmentalLatitudeAgentStatus',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDepartmentalLatitudeAgentStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_departmental_latitude_agent_status_with_options_async(
        self,
        tmp_req: main_models.GetDepartmentalLatitudeAgentStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDepartmentalLatitudeAgentStatusResponse:
        tmp_req.validate()
        request = main_models.GetDepartmentalLatitudeAgentStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDepartmentalLatitudeAgentStatus',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDepartmentalLatitudeAgentStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_departmental_latitude_agent_status(
        self,
        request: main_models.GetDepartmentalLatitudeAgentStatusRequest,
    ) -> main_models.GetDepartmentalLatitudeAgentStatusResponse:
        runtime = RuntimeOptions()
        return self.get_departmental_latitude_agent_status_with_options(request, runtime)

    async def get_departmental_latitude_agent_status_async(
        self,
        request: main_models.GetDepartmentalLatitudeAgentStatusRequest,
    ) -> main_models.GetDepartmentalLatitudeAgentStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_departmental_latitude_agent_status_with_options_async(request, runtime)

    def get_hotline_agent_detail_with_options(
        self,
        request: main_models.GetHotlineAgentDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotlineAgentDetailResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotlineAgentDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotlineAgentDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotline_agent_detail_with_options_async(
        self,
        request: main_models.GetHotlineAgentDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotlineAgentDetailResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotlineAgentDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotlineAgentDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotline_agent_detail(
        self,
        request: main_models.GetHotlineAgentDetailRequest,
    ) -> main_models.GetHotlineAgentDetailResponse:
        runtime = RuntimeOptions()
        return self.get_hotline_agent_detail_with_options(request, runtime)

    async def get_hotline_agent_detail_async(
        self,
        request: main_models.GetHotlineAgentDetailRequest,
    ) -> main_models.GetHotlineAgentDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_hotline_agent_detail_with_options_async(request, runtime)

    def get_hotline_agent_detail_report_with_options(
        self,
        request: main_models.GetHotlineAgentDetailReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotlineAgentDetailReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dep_ids):
            query['DepIds'] = request.dep_ids
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotlineAgentDetailReport',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotlineAgentDetailReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotline_agent_detail_report_with_options_async(
        self,
        request: main_models.GetHotlineAgentDetailReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotlineAgentDetailReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dep_ids):
            query['DepIds'] = request.dep_ids
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotlineAgentDetailReport',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotlineAgentDetailReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotline_agent_detail_report(
        self,
        request: main_models.GetHotlineAgentDetailReportRequest,
    ) -> main_models.GetHotlineAgentDetailReportResponse:
        runtime = RuntimeOptions()
        return self.get_hotline_agent_detail_report_with_options(request, runtime)

    async def get_hotline_agent_detail_report_async(
        self,
        request: main_models.GetHotlineAgentDetailReportRequest,
    ) -> main_models.GetHotlineAgentDetailReportResponse:
        runtime = RuntimeOptions()
        return await self.get_hotline_agent_detail_report_with_options_async(request, runtime)

    def get_hotline_agent_status_with_options(
        self,
        request: main_models.GetHotlineAgentStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotlineAgentStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotlineAgentStatus',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotlineAgentStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotline_agent_status_with_options_async(
        self,
        request: main_models.GetHotlineAgentStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotlineAgentStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotlineAgentStatus',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotlineAgentStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotline_agent_status(
        self,
        request: main_models.GetHotlineAgentStatusRequest,
    ) -> main_models.GetHotlineAgentStatusResponse:
        runtime = RuntimeOptions()
        return self.get_hotline_agent_status_with_options(request, runtime)

    async def get_hotline_agent_status_async(
        self,
        request: main_models.GetHotlineAgentStatusRequest,
    ) -> main_models.GetHotlineAgentStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_hotline_agent_status_with_options_async(request, runtime)

    def get_hotline_call_action_with_options(
        self,
        request: main_models.GetHotlineCallActionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotlineCallActionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.acc):
            body['Acc'] = request.acc
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.act):
            body['Act'] = request.act
        if not DaraCore.is_null(request.biz):
            body['Biz'] = request.biz
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.from_source):
            body['FromSource'] = request.from_source
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotlineCallAction',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotlineCallActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotline_call_action_with_options_async(
        self,
        request: main_models.GetHotlineCallActionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotlineCallActionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.acc):
            body['Acc'] = request.acc
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.act):
            body['Act'] = request.act
        if not DaraCore.is_null(request.biz):
            body['Biz'] = request.biz
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.from_source):
            body['FromSource'] = request.from_source
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotlineCallAction',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotlineCallActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotline_call_action(
        self,
        request: main_models.GetHotlineCallActionRequest,
    ) -> main_models.GetHotlineCallActionResponse:
        runtime = RuntimeOptions()
        return self.get_hotline_call_action_with_options(request, runtime)

    async def get_hotline_call_action_async(
        self,
        request: main_models.GetHotlineCallActionRequest,
    ) -> main_models.GetHotlineCallActionResponse:
        runtime = RuntimeOptions()
        return await self.get_hotline_call_action_with_options_async(request, runtime)

    def get_hotline_group_detail_report_with_options(
        self,
        request: main_models.GetHotlineGroupDetailReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotlineGroupDetailReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dep_ids):
            query['DepIds'] = request.dep_ids
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotlineGroupDetailReport',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotlineGroupDetailReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotline_group_detail_report_with_options_async(
        self,
        request: main_models.GetHotlineGroupDetailReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotlineGroupDetailReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dep_ids):
            query['DepIds'] = request.dep_ids
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotlineGroupDetailReport',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotlineGroupDetailReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotline_group_detail_report(
        self,
        request: main_models.GetHotlineGroupDetailReportRequest,
    ) -> main_models.GetHotlineGroupDetailReportResponse:
        runtime = RuntimeOptions()
        return self.get_hotline_group_detail_report_with_options(request, runtime)

    async def get_hotline_group_detail_report_async(
        self,
        request: main_models.GetHotlineGroupDetailReportRequest,
    ) -> main_models.GetHotlineGroupDetailReportResponse:
        runtime = RuntimeOptions()
        return await self.get_hotline_group_detail_report_with_options_async(request, runtime)

    def get_hotline_message_log_with_options(
        self,
        request: main_models.GetHotlineMessageLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotlineMessageLogResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotlineMessageLog',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotlineMessageLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotline_message_log_with_options_async(
        self,
        request: main_models.GetHotlineMessageLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotlineMessageLogResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotlineMessageLog',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotlineMessageLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotline_message_log(
        self,
        request: main_models.GetHotlineMessageLogRequest,
    ) -> main_models.GetHotlineMessageLogResponse:
        runtime = RuntimeOptions()
        return self.get_hotline_message_log_with_options(request, runtime)

    async def get_hotline_message_log_async(
        self,
        request: main_models.GetHotlineMessageLogRequest,
    ) -> main_models.GetHotlineMessageLogResponse:
        runtime = RuntimeOptions()
        return await self.get_hotline_message_log_with_options_async(request, runtime)

    def get_hotline_runtime_info_with_options(
        self,
        request: main_models.GetHotlineRuntimeInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotlineRuntimeInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotlineRuntimeInfo',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotlineRuntimeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotline_runtime_info_with_options_async(
        self,
        request: main_models.GetHotlineRuntimeInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotlineRuntimeInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotlineRuntimeInfo',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotlineRuntimeInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotline_runtime_info(
        self,
        request: main_models.GetHotlineRuntimeInfoRequest,
    ) -> main_models.GetHotlineRuntimeInfoResponse:
        runtime = RuntimeOptions()
        return self.get_hotline_runtime_info_with_options(request, runtime)

    async def get_hotline_runtime_info_async(
        self,
        request: main_models.GetHotlineRuntimeInfoRequest,
    ) -> main_models.GetHotlineRuntimeInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_hotline_runtime_info_with_options_async(request, runtime)

    def get_hotline_service_statistics_with_options(
        self,
        tmp_req: main_models.GetHotlineServiceStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotlineServiceStatisticsResponse:
        tmp_req.validate()
        request = main_models.GetHotlineServiceStatisticsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not DaraCore.is_null(tmp_req.group_ids):
            request.group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotlineServiceStatistics',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotlineServiceStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotline_service_statistics_with_options_async(
        self,
        tmp_req: main_models.GetHotlineServiceStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotlineServiceStatisticsResponse:
        tmp_req.validate()
        request = main_models.GetHotlineServiceStatisticsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not DaraCore.is_null(tmp_req.group_ids):
            request.group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotlineServiceStatistics',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotlineServiceStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotline_service_statistics(
        self,
        request: main_models.GetHotlineServiceStatisticsRequest,
    ) -> main_models.GetHotlineServiceStatisticsResponse:
        runtime = RuntimeOptions()
        return self.get_hotline_service_statistics_with_options(request, runtime)

    async def get_hotline_service_statistics_async(
        self,
        request: main_models.GetHotlineServiceStatisticsRequest,
    ) -> main_models.GetHotlineServiceStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.get_hotline_service_statistics_with_options_async(request, runtime)

    def get_hotline_waiting_number_with_options(
        self,
        request: main_models.GetHotlineWaitingNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotlineWaitingNumberResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotlineWaitingNumber',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotlineWaitingNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotline_waiting_number_with_options_async(
        self,
        request: main_models.GetHotlineWaitingNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotlineWaitingNumberResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotlineWaitingNumber',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotlineWaitingNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotline_waiting_number(
        self,
        request: main_models.GetHotlineWaitingNumberRequest,
    ) -> main_models.GetHotlineWaitingNumberResponse:
        runtime = RuntimeOptions()
        return self.get_hotline_waiting_number_with_options(request, runtime)

    async def get_hotline_waiting_number_async(
        self,
        request: main_models.GetHotlineWaitingNumberRequest,
    ) -> main_models.GetHotlineWaitingNumberResponse:
        runtime = RuntimeOptions()
        return await self.get_hotline_waiting_number_with_options_async(request, runtime)

    def get_index_current_value_with_options(
        self,
        request: main_models.GetIndexCurrentValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIndexCurrentValueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dep_ids):
            query['DepIds'] = request.dep_ids
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIndexCurrentValue',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIndexCurrentValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_index_current_value_with_options_async(
        self,
        request: main_models.GetIndexCurrentValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIndexCurrentValueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dep_ids):
            query['DepIds'] = request.dep_ids
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIndexCurrentValue',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIndexCurrentValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_index_current_value(
        self,
        request: main_models.GetIndexCurrentValueRequest,
    ) -> main_models.GetIndexCurrentValueResponse:
        runtime = RuntimeOptions()
        return self.get_index_current_value_with_options(request, runtime)

    async def get_index_current_value_async(
        self,
        request: main_models.GetIndexCurrentValueRequest,
    ) -> main_models.GetIndexCurrentValueResponse:
        runtime = RuntimeOptions()
        return await self.get_index_current_value_with_options_async(request, runtime)

    def get_instance_list_with_options(
        self,
        request: main_models.GetInstanceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceListResponse:
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
            action = 'GetInstanceList',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_list_with_options_async(
        self,
        request: main_models.GetInstanceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceListResponse:
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
            action = 'GetInstanceList',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_list(
        self,
        request: main_models.GetInstanceListRequest,
    ) -> main_models.GetInstanceListResponse:
        runtime = RuntimeOptions()
        return self.get_instance_list_with_options(request, runtime)

    async def get_instance_list_async(
        self,
        request: main_models.GetInstanceListRequest,
    ) -> main_models.GetInstanceListResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_list_with_options_async(request, runtime)

    def get_mcu_lvs_ip_with_options(
        self,
        request: main_models.GetMcuLvsIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMcuLvsIpResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMcuLvsIp',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMcuLvsIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mcu_lvs_ip_with_options_async(
        self,
        request: main_models.GetMcuLvsIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMcuLvsIpResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMcuLvsIp',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMcuLvsIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mcu_lvs_ip(
        self,
        request: main_models.GetMcuLvsIpRequest,
    ) -> main_models.GetMcuLvsIpResponse:
        runtime = RuntimeOptions()
        return self.get_mcu_lvs_ip_with_options(request, runtime)

    async def get_mcu_lvs_ip_async(
        self,
        request: main_models.GetMcuLvsIpRequest,
    ) -> main_models.GetMcuLvsIpResponse:
        runtime = RuntimeOptions()
        return await self.get_mcu_lvs_ip_with_options_async(request, runtime)

    def get_num_location_with_options(
        self,
        request: main_models.GetNumLocationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNumLocationResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNumLocation',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNumLocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_num_location_with_options_async(
        self,
        request: main_models.GetNumLocationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNumLocationResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNumLocation',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNumLocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_num_location(
        self,
        request: main_models.GetNumLocationRequest,
    ) -> main_models.GetNumLocationResponse:
        runtime = RuntimeOptions()
        return self.get_num_location_with_options(request, runtime)

    async def get_num_location_async(
        self,
        request: main_models.GetNumLocationRequest,
    ) -> main_models.GetNumLocationResponse:
        runtime = RuntimeOptions()
        return await self.get_num_location_with_options_async(request, runtime)

    def get_online_seat_information_with_options(
        self,
        tmp_req: main_models.GetOnlineSeatInformationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOnlineSeatInformationResponse:
        tmp_req.validate()
        request = main_models.GetOnlineSeatInformationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOnlineSeatInformation',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOnlineSeatInformationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_online_seat_information_with_options_async(
        self,
        tmp_req: main_models.GetOnlineSeatInformationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOnlineSeatInformationResponse:
        tmp_req.validate()
        request = main_models.GetOnlineSeatInformationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOnlineSeatInformation',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOnlineSeatInformationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_online_seat_information(
        self,
        request: main_models.GetOnlineSeatInformationRequest,
    ) -> main_models.GetOnlineSeatInformationResponse:
        runtime = RuntimeOptions()
        return self.get_online_seat_information_with_options(request, runtime)

    async def get_online_seat_information_async(
        self,
        request: main_models.GetOnlineSeatInformationRequest,
    ) -> main_models.GetOnlineSeatInformationResponse:
        runtime = RuntimeOptions()
        return await self.get_online_seat_information_with_options_async(request, runtime)

    def get_online_service_volume_with_options(
        self,
        tmp_req: main_models.GetOnlineServiceVolumeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOnlineServiceVolumeResponse:
        tmp_req.validate()
        request = main_models.GetOnlineServiceVolumeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not DaraCore.is_null(tmp_req.group_ids):
            request.group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOnlineServiceVolume',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOnlineServiceVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_online_service_volume_with_options_async(
        self,
        tmp_req: main_models.GetOnlineServiceVolumeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOnlineServiceVolumeResponse:
        tmp_req.validate()
        request = main_models.GetOnlineServiceVolumeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not DaraCore.is_null(tmp_req.group_ids):
            request.group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOnlineServiceVolume',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOnlineServiceVolumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_online_service_volume(
        self,
        request: main_models.GetOnlineServiceVolumeRequest,
    ) -> main_models.GetOnlineServiceVolumeResponse:
        runtime = RuntimeOptions()
        return self.get_online_service_volume_with_options(request, runtime)

    async def get_online_service_volume_async(
        self,
        request: main_models.GetOnlineServiceVolumeRequest,
    ) -> main_models.GetOnlineServiceVolumeResponse:
        runtime = RuntimeOptions()
        return await self.get_online_service_volume_with_options_async(request, runtime)

    def get_outboun_num_list_with_options(
        self,
        request: main_models.GetOutbounNumListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOutbounNumListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetOutbounNumList',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOutbounNumListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_outboun_num_list_with_options_async(
        self,
        request: main_models.GetOutbounNumListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOutbounNumListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetOutbounNumList',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOutbounNumListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_outboun_num_list(
        self,
        request: main_models.GetOutbounNumListRequest,
    ) -> main_models.GetOutbounNumListResponse:
        runtime = RuntimeOptions()
        return self.get_outboun_num_list_with_options(request, runtime)

    async def get_outboun_num_list_async(
        self,
        request: main_models.GetOutbounNumListRequest,
    ) -> main_models.GetOutbounNumListResponse:
        runtime = RuntimeOptions()
        return await self.get_outboun_num_list_with_options_async(request, runtime)

    def get_quality_project_detail_with_options(
        self,
        request: main_models.GetQualityProjectDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityProjectDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityProjectDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityProjectDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_project_detail_with_options_async(
        self,
        request: main_models.GetQualityProjectDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityProjectDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityProjectDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityProjectDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_project_detail(
        self,
        request: main_models.GetQualityProjectDetailRequest,
    ) -> main_models.GetQualityProjectDetailResponse:
        runtime = RuntimeOptions()
        return self.get_quality_project_detail_with_options(request, runtime)

    async def get_quality_project_detail_async(
        self,
        request: main_models.GetQualityProjectDetailRequest,
    ) -> main_models.GetQualityProjectDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_quality_project_detail_with_options_async(request, runtime)

    def get_quality_project_list_with_options(
        self,
        request: main_models.GetQualityProjectListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityProjectListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.check_freq_type):
            query['checkFreqType'] = request.check_freq_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityProjectList',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityProjectListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_project_list_with_options_async(
        self,
        request: main_models.GetQualityProjectListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityProjectListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.check_freq_type):
            query['checkFreqType'] = request.check_freq_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityProjectList',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityProjectListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_project_list(
        self,
        request: main_models.GetQualityProjectListRequest,
    ) -> main_models.GetQualityProjectListResponse:
        runtime = RuntimeOptions()
        return self.get_quality_project_list_with_options(request, runtime)

    async def get_quality_project_list_async(
        self,
        request: main_models.GetQualityProjectListRequest,
    ) -> main_models.GetQualityProjectListResponse:
        runtime = RuntimeOptions()
        return await self.get_quality_project_list_with_options_async(request, runtime)

    def get_quality_project_log_with_options(
        self,
        request: main_models.GetQualityProjectLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityProjectLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityProjectLog',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityProjectLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_project_log_with_options_async(
        self,
        request: main_models.GetQualityProjectLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityProjectLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityProjectLog',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityProjectLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_project_log(
        self,
        request: main_models.GetQualityProjectLogRequest,
    ) -> main_models.GetQualityProjectLogResponse:
        runtime = RuntimeOptions()
        return self.get_quality_project_log_with_options(request, runtime)

    async def get_quality_project_log_async(
        self,
        request: main_models.GetQualityProjectLogRequest,
    ) -> main_models.GetQualityProjectLogResponse:
        runtime = RuntimeOptions()
        return await self.get_quality_project_log_with_options_async(request, runtime)

    def get_quality_result_with_options(
        self,
        request: main_models.GetQualityResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.hit_status):
            query['HitStatus'] = request.hit_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_ids):
            query['ProjectIds'] = request.project_ids
        if not DaraCore.is_null(request.quality_rule_ids):
            query['QualityRuleIds'] = request.quality_rule_ids
        if not DaraCore.is_null(request.touch_end_time):
            query['TouchEndTime'] = request.touch_end_time
        if not DaraCore.is_null(request.touch_start_time):
            query['TouchStartTime'] = request.touch_start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityResult',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_result_with_options_async(
        self,
        request: main_models.GetQualityResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.hit_status):
            query['HitStatus'] = request.hit_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_ids):
            query['ProjectIds'] = request.project_ids
        if not DaraCore.is_null(request.quality_rule_ids):
            query['QualityRuleIds'] = request.quality_rule_ids
        if not DaraCore.is_null(request.touch_end_time):
            query['TouchEndTime'] = request.touch_end_time
        if not DaraCore.is_null(request.touch_start_time):
            query['TouchStartTime'] = request.touch_start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityResult',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_result(
        self,
        request: main_models.GetQualityResultRequest,
    ) -> main_models.GetQualityResultResponse:
        runtime = RuntimeOptions()
        return self.get_quality_result_with_options(request, runtime)

    async def get_quality_result_async(
        self,
        request: main_models.GetQualityResultRequest,
    ) -> main_models.GetQualityResultResponse:
        runtime = RuntimeOptions()
        return await self.get_quality_result_with_options_async(request, runtime)

    def get_quality_rule_detail_with_options(
        self,
        request: main_models.GetQualityRuleDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityRuleDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.quality_rule_id):
            query['QualityRuleId'] = request.quality_rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityRuleDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityRuleDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_rule_detail_with_options_async(
        self,
        request: main_models.GetQualityRuleDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityRuleDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.quality_rule_id):
            query['QualityRuleId'] = request.quality_rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityRuleDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityRuleDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_rule_detail(
        self,
        request: main_models.GetQualityRuleDetailRequest,
    ) -> main_models.GetQualityRuleDetailResponse:
        runtime = RuntimeOptions()
        return self.get_quality_rule_detail_with_options(request, runtime)

    async def get_quality_rule_detail_async(
        self,
        request: main_models.GetQualityRuleDetailRequest,
    ) -> main_models.GetQualityRuleDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_quality_rule_detail_with_options_async(request, runtime)

    def get_quality_rule_list_with_options(
        self,
        request: main_models.GetQualityRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityRuleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityRuleList',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_rule_list_with_options_async(
        self,
        request: main_models.GetQualityRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityRuleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityRuleList',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_rule_list(
        self,
        request: main_models.GetQualityRuleListRequest,
    ) -> main_models.GetQualityRuleListResponse:
        runtime = RuntimeOptions()
        return self.get_quality_rule_list_with_options(request, runtime)

    async def get_quality_rule_list_async(
        self,
        request: main_models.GetQualityRuleListRequest,
    ) -> main_models.GetQualityRuleListResponse:
        runtime = RuntimeOptions()
        return await self.get_quality_rule_list_with_options_async(request, runtime)

    def get_quality_rule_tag_list_with_options(
        self,
        request: main_models.GetQualityRuleTagListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityRuleTagListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityRuleTagList',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityRuleTagListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_rule_tag_list_with_options_async(
        self,
        request: main_models.GetQualityRuleTagListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityRuleTagListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityRuleTagList',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityRuleTagListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_rule_tag_list(
        self,
        request: main_models.GetQualityRuleTagListRequest,
    ) -> main_models.GetQualityRuleTagListResponse:
        runtime = RuntimeOptions()
        return self.get_quality_rule_tag_list_with_options(request, runtime)

    async def get_quality_rule_tag_list_async(
        self,
        request: main_models.GetQualityRuleTagListRequest,
    ) -> main_models.GetQualityRuleTagListResponse:
        runtime = RuntimeOptions()
        return await self.get_quality_rule_tag_list_with_options_async(request, runtime)

    def get_queue_information_with_options(
        self,
        tmp_req: main_models.GetQueueInformationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueueInformationResponse:
        tmp_req.validate()
        request = main_models.GetQueueInformationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not DaraCore.is_null(tmp_req.group_ids):
            request.group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueueInformation',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueueInformationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_queue_information_with_options_async(
        self,
        tmp_req: main_models.GetQueueInformationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueueInformationResponse:
        tmp_req.validate()
        request = main_models.GetQueueInformationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not DaraCore.is_null(tmp_req.group_ids):
            request.group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueueInformation',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueueInformationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_queue_information(
        self,
        request: main_models.GetQueueInformationRequest,
    ) -> main_models.GetQueueInformationResponse:
        runtime = RuntimeOptions()
        return self.get_queue_information_with_options(request, runtime)

    async def get_queue_information_async(
        self,
        request: main_models.GetQueueInformationRequest,
    ) -> main_models.GetQueueInformationResponse:
        runtime = RuntimeOptions()
        return await self.get_queue_information_with_options_async(request, runtime)

    def get_record_data_with_options(
        self,
        request: main_models.GetRecordDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRecordDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acid):
            query['Acid'] = request.acid
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRecordData',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRecordDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_record_data_with_options_async(
        self,
        request: main_models.GetRecordDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRecordDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acid):
            query['Acid'] = request.acid
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRecordData',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRecordDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_record_data(
        self,
        request: main_models.GetRecordDataRequest,
    ) -> main_models.GetRecordDataResponse:
        runtime = RuntimeOptions()
        return self.get_record_data_with_options(request, runtime)

    async def get_record_data_async(
        self,
        request: main_models.GetRecordDataRequest,
    ) -> main_models.GetRecordDataResponse:
        runtime = RuntimeOptions()
        return await self.get_record_data_with_options_async(request, runtime)

    def get_record_url_with_options(
        self,
        request: main_models.GetRecordUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRecordUrlResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRecordUrl',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRecordUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_record_url_with_options_async(
        self,
        request: main_models.GetRecordUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRecordUrlResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRecordUrl',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRecordUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_record_url(
        self,
        request: main_models.GetRecordUrlRequest,
    ) -> main_models.GetRecordUrlResponse:
        runtime = RuntimeOptions()
        return self.get_record_url_with_options(request, runtime)

    async def get_record_url_async(
        self,
        request: main_models.GetRecordUrlRequest,
    ) -> main_models.GetRecordUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_record_url_with_options_async(request, runtime)

    def get_rtc_token_with_options(
        self,
        request: main_models.GetRtcTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRtcTokenResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRtcToken',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRtcTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rtc_token_with_options_async(
        self,
        request: main_models.GetRtcTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRtcTokenResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRtcToken',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRtcTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rtc_token(
        self,
        request: main_models.GetRtcTokenRequest,
    ) -> main_models.GetRtcTokenResponse:
        runtime = RuntimeOptions()
        return self.get_rtc_token_with_options(request, runtime)

    async def get_rtc_token_async(
        self,
        request: main_models.GetRtcTokenRequest,
    ) -> main_models.GetRtcTokenResponse:
        runtime = RuntimeOptions()
        return await self.get_rtc_token_with_options_async(request, runtime)

    def get_seat_information_with_options(
        self,
        tmp_req: main_models.GetSeatInformationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSeatInformationResponse:
        tmp_req.validate()
        request = main_models.GetSeatInformationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'depIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSeatInformation',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSeatInformationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_seat_information_with_options_async(
        self,
        tmp_req: main_models.GetSeatInformationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSeatInformationResponse:
        tmp_req.validate()
        request = main_models.GetSeatInformationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'depIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSeatInformation',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSeatInformationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_seat_information(
        self,
        request: main_models.GetSeatInformationRequest,
    ) -> main_models.GetSeatInformationResponse:
        runtime = RuntimeOptions()
        return self.get_seat_information_with_options(request, runtime)

    async def get_seat_information_async(
        self,
        request: main_models.GetSeatInformationRequest,
    ) -> main_models.GetSeatInformationResponse:
        runtime = RuntimeOptions()
        return await self.get_seat_information_with_options_async(request, runtime)

    def get_skill_group_agent_status_details_with_options(
        self,
        tmp_req: main_models.GetSkillGroupAgentStatusDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillGroupAgentStatusDetailsResponse:
        tmp_req.validate()
        request = main_models.GetSkillGroupAgentStatusDetailsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not DaraCore.is_null(tmp_req.group_ids):
            request.group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillGroupAgentStatusDetails',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillGroupAgentStatusDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_group_agent_status_details_with_options_async(
        self,
        tmp_req: main_models.GetSkillGroupAgentStatusDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillGroupAgentStatusDetailsResponse:
        tmp_req.validate()
        request = main_models.GetSkillGroupAgentStatusDetailsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not DaraCore.is_null(tmp_req.group_ids):
            request.group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillGroupAgentStatusDetails',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillGroupAgentStatusDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_group_agent_status_details(
        self,
        request: main_models.GetSkillGroupAgentStatusDetailsRequest,
    ) -> main_models.GetSkillGroupAgentStatusDetailsResponse:
        runtime = RuntimeOptions()
        return self.get_skill_group_agent_status_details_with_options(request, runtime)

    async def get_skill_group_agent_status_details_async(
        self,
        request: main_models.GetSkillGroupAgentStatusDetailsRequest,
    ) -> main_models.GetSkillGroupAgentStatusDetailsResponse:
        runtime = RuntimeOptions()
        return await self.get_skill_group_agent_status_details_with_options_async(request, runtime)

    def get_skill_group_and_agent_status_summary_with_options(
        self,
        tmp_req: main_models.GetSkillGroupAndAgentStatusSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillGroupAndAgentStatusSummaryResponse:
        tmp_req.validate()
        request = main_models.GetSkillGroupAndAgentStatusSummaryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not DaraCore.is_null(tmp_req.group_ids):
            request.group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillGroupAndAgentStatusSummary',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillGroupAndAgentStatusSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_group_and_agent_status_summary_with_options_async(
        self,
        tmp_req: main_models.GetSkillGroupAndAgentStatusSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillGroupAndAgentStatusSummaryResponse:
        tmp_req.validate()
        request = main_models.GetSkillGroupAndAgentStatusSummaryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not DaraCore.is_null(tmp_req.group_ids):
            request.group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillGroupAndAgentStatusSummary',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillGroupAndAgentStatusSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_group_and_agent_status_summary(
        self,
        request: main_models.GetSkillGroupAndAgentStatusSummaryRequest,
    ) -> main_models.GetSkillGroupAndAgentStatusSummaryResponse:
        runtime = RuntimeOptions()
        return self.get_skill_group_and_agent_status_summary_with_options(request, runtime)

    async def get_skill_group_and_agent_status_summary_async(
        self,
        request: main_models.GetSkillGroupAndAgentStatusSummaryRequest,
    ) -> main_models.GetSkillGroupAndAgentStatusSummaryResponse:
        runtime = RuntimeOptions()
        return await self.get_skill_group_and_agent_status_summary_with_options_async(request, runtime)

    def get_skill_group_latitude_state_with_options(
        self,
        tmp_req: main_models.GetSkillGroupLatitudeStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillGroupLatitudeStateResponse:
        tmp_req.validate()
        request = main_models.GetSkillGroupLatitudeStateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not DaraCore.is_null(tmp_req.group_ids):
            request.group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillGroupLatitudeState',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillGroupLatitudeStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_group_latitude_state_with_options_async(
        self,
        tmp_req: main_models.GetSkillGroupLatitudeStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillGroupLatitudeStateResponse:
        tmp_req.validate()
        request = main_models.GetSkillGroupLatitudeStateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not DaraCore.is_null(tmp_req.group_ids):
            request.group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillGroupLatitudeState',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillGroupLatitudeStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_group_latitude_state(
        self,
        request: main_models.GetSkillGroupLatitudeStateRequest,
    ) -> main_models.GetSkillGroupLatitudeStateResponse:
        runtime = RuntimeOptions()
        return self.get_skill_group_latitude_state_with_options(request, runtime)

    async def get_skill_group_latitude_state_async(
        self,
        request: main_models.GetSkillGroupLatitudeStateRequest,
    ) -> main_models.GetSkillGroupLatitudeStateResponse:
        runtime = RuntimeOptions()
        return await self.get_skill_group_latitude_state_with_options_async(request, runtime)

    def get_skill_group_service_capability_with_options(
        self,
        tmp_req: main_models.GetSkillGroupServiceCapabilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillGroupServiceCapabilityResponse:
        tmp_req.validate()
        request = main_models.GetSkillGroupServiceCapabilityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not DaraCore.is_null(tmp_req.group_ids):
            request.group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillGroupServiceCapability',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillGroupServiceCapabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_group_service_capability_with_options_async(
        self,
        tmp_req: main_models.GetSkillGroupServiceCapabilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillGroupServiceCapabilityResponse:
        tmp_req.validate()
        request = main_models.GetSkillGroupServiceCapabilityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not DaraCore.is_null(tmp_req.group_ids):
            request.group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillGroupServiceCapability',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillGroupServiceCapabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_group_service_capability(
        self,
        request: main_models.GetSkillGroupServiceCapabilityRequest,
    ) -> main_models.GetSkillGroupServiceCapabilityResponse:
        runtime = RuntimeOptions()
        return self.get_skill_group_service_capability_with_options(request, runtime)

    async def get_skill_group_service_capability_async(
        self,
        request: main_models.GetSkillGroupServiceCapabilityRequest,
    ) -> main_models.GetSkillGroupServiceCapabilityResponse:
        runtime = RuntimeOptions()
        return await self.get_skill_group_service_capability_with_options_async(request, runtime)

    def get_skill_group_service_status_with_options(
        self,
        tmp_req: main_models.GetSkillGroupServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillGroupServiceStatusResponse:
        tmp_req.validate()
        request = main_models.GetSkillGroupServiceStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not DaraCore.is_null(tmp_req.group_ids):
            request.group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillGroupServiceStatus',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillGroupServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_group_service_status_with_options_async(
        self,
        tmp_req: main_models.GetSkillGroupServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillGroupServiceStatusResponse:
        tmp_req.validate()
        request = main_models.GetSkillGroupServiceStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not DaraCore.is_null(tmp_req.group_ids):
            request.group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillGroupServiceStatus',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillGroupServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_group_service_status(
        self,
        request: main_models.GetSkillGroupServiceStatusRequest,
    ) -> main_models.GetSkillGroupServiceStatusResponse:
        runtime = RuntimeOptions()
        return self.get_skill_group_service_status_with_options(request, runtime)

    async def get_skill_group_service_status_async(
        self,
        request: main_models.GetSkillGroupServiceStatusRequest,
    ) -> main_models.GetSkillGroupServiceStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_skill_group_service_status_with_options_async(request, runtime)

    def get_skill_group_status_total_with_options(
        self,
        tmp_req: main_models.GetSkillGroupStatusTotalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillGroupStatusTotalResponse:
        tmp_req.validate()
        request = main_models.GetSkillGroupStatusTotalShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not DaraCore.is_null(tmp_req.group_ids):
            request.group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillGroupStatusTotal',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillGroupStatusTotalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_group_status_total_with_options_async(
        self,
        tmp_req: main_models.GetSkillGroupStatusTotalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillGroupStatusTotalResponse:
        tmp_req.validate()
        request = main_models.GetSkillGroupStatusTotalShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not DaraCore.is_null(tmp_req.dep_ids):
            request.dep_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not DaraCore.is_null(tmp_req.group_ids):
            request.group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillGroupStatusTotal',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillGroupStatusTotalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_group_status_total(
        self,
        request: main_models.GetSkillGroupStatusTotalRequest,
    ) -> main_models.GetSkillGroupStatusTotalResponse:
        runtime = RuntimeOptions()
        return self.get_skill_group_status_total_with_options(request, runtime)

    async def get_skill_group_status_total_async(
        self,
        request: main_models.GetSkillGroupStatusTotalRequest,
    ) -> main_models.GetSkillGroupStatusTotalResponse:
        runtime = RuntimeOptions()
        return await self.get_skill_group_status_total_with_options_async(request, runtime)

    def hang_up_double_call_with_options(
        self,
        request: main_models.HangUpDoubleCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HangUpDoubleCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acid):
            query['Acid'] = request.acid
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'HangUpDoubleCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HangUpDoubleCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def hang_up_double_call_with_options_async(
        self,
        request: main_models.HangUpDoubleCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HangUpDoubleCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acid):
            query['Acid'] = request.acid
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'HangUpDoubleCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HangUpDoubleCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hang_up_double_call(
        self,
        request: main_models.HangUpDoubleCallRequest,
    ) -> main_models.HangUpDoubleCallResponse:
        runtime = RuntimeOptions()
        return self.hang_up_double_call_with_options(request, runtime)

    async def hang_up_double_call_async(
        self,
        request: main_models.HangUpDoubleCallRequest,
    ) -> main_models.HangUpDoubleCallResponse:
        runtime = RuntimeOptions()
        return await self.hang_up_double_call_with_options_async(request, runtime)

    def hangup_call_with_options(
        self,
        request: main_models.HangupCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HangupCallResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.call_id):
            body['CallId'] = request.call_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'HangupCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HangupCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def hangup_call_with_options_async(
        self,
        request: main_models.HangupCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HangupCallResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.call_id):
            body['CallId'] = request.call_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'HangupCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HangupCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hangup_call(
        self,
        request: main_models.HangupCallRequest,
    ) -> main_models.HangupCallResponse:
        runtime = RuntimeOptions()
        return self.hangup_call_with_options(request, runtime)

    async def hangup_call_async(
        self,
        request: main_models.HangupCallRequest,
    ) -> main_models.HangupCallResponse:
        runtime = RuntimeOptions()
        return await self.hangup_call_with_options_async(request, runtime)

    def hangup_operate_with_options(
        self,
        request: main_models.HangupOperateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HangupOperateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.immediate_hangup):
            query['ImmediateHangup'] = request.immediate_hangup
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'HangupOperate',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HangupOperateResponse(),
            self.call_api(params, req, runtime)
        )

    async def hangup_operate_with_options_async(
        self,
        request: main_models.HangupOperateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HangupOperateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.immediate_hangup):
            query['ImmediateHangup'] = request.immediate_hangup
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'HangupOperate',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HangupOperateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hangup_operate(
        self,
        request: main_models.HangupOperateRequest,
    ) -> main_models.HangupOperateResponse:
        runtime = RuntimeOptions()
        return self.hangup_operate_with_options(request, runtime)

    async def hangup_operate_async(
        self,
        request: main_models.HangupOperateRequest,
    ) -> main_models.HangupOperateResponse:
        runtime = RuntimeOptions()
        return await self.hangup_operate_with_options_async(request, runtime)

    def hangup_third_call_with_options(
        self,
        request: main_models.HangupThirdCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HangupThirdCallResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.call_id):
            body['CallId'] = request.call_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'HangupThirdCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HangupThirdCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def hangup_third_call_with_options_async(
        self,
        request: main_models.HangupThirdCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HangupThirdCallResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.call_id):
            body['CallId'] = request.call_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'HangupThirdCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HangupThirdCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hangup_third_call(
        self,
        request: main_models.HangupThirdCallRequest,
    ) -> main_models.HangupThirdCallResponse:
        runtime = RuntimeOptions()
        return self.hangup_third_call_with_options(request, runtime)

    async def hangup_third_call_async(
        self,
        request: main_models.HangupThirdCallRequest,
    ) -> main_models.HangupThirdCallResponse:
        runtime = RuntimeOptions()
        return await self.hangup_third_call_with_options_async(request, runtime)

    def hold_call_with_options(
        self,
        request: main_models.HoldCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HoldCallResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.call_id):
            body['CallId'] = request.call_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'HoldCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HoldCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def hold_call_with_options_async(
        self,
        request: main_models.HoldCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HoldCallResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.call_id):
            body['CallId'] = request.call_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'HoldCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HoldCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hold_call(
        self,
        request: main_models.HoldCallRequest,
    ) -> main_models.HoldCallResponse:
        runtime = RuntimeOptions()
        return self.hold_call_with_options(request, runtime)

    async def hold_call_async(
        self,
        request: main_models.HoldCallRequest,
    ) -> main_models.HoldCallResponse:
        runtime = RuntimeOptions()
        return await self.hold_call_with_options_async(request, runtime)

    def hotline_session_query_with_options(
        self,
        request: main_models.HotlineSessionQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HotlineSessionQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acid):
            query['Acid'] = request.acid
        if not DaraCore.is_null(request.acid_list):
            query['AcidList'] = request.acid_list
        if not DaraCore.is_null(request.call_result):
            query['CallResult'] = request.call_result
        if not DaraCore.is_null(request.call_result_list):
            query['CallResultList'] = request.call_result_list
        if not DaraCore.is_null(request.call_type):
            query['CallType'] = request.call_type
        if not DaraCore.is_null(request.call_type_list):
            query['CallTypeList'] = request.call_type_list
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.called_number_list):
            query['CalledNumberList'] = request.called_number_list
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.calling_number_list):
            query['CallingNumberList'] = request.calling_number_list
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_id_list):
            query['GroupIdList'] = request.group_id_list
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.member_id):
            query['MemberId'] = request.member_id
        if not DaraCore.is_null(request.member_id_list):
            query['MemberIdList'] = request.member_id_list
        if not DaraCore.is_null(request.member_name):
            query['MemberName'] = request.member_name
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.query_end_time):
            query['QueryEndTime'] = request.query_end_time
        if not DaraCore.is_null(request.query_start_time):
            query['QueryStartTime'] = request.query_start_time
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.servicer_id):
            query['ServicerId'] = request.servicer_id
        if not DaraCore.is_null(request.servicer_id_list):
            query['ServicerIdList'] = request.servicer_id_list
        if not DaraCore.is_null(request.servicer_name):
            query['ServicerName'] = request.servicer_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'HotlineSessionQuery',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HotlineSessionQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def hotline_session_query_with_options_async(
        self,
        request: main_models.HotlineSessionQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HotlineSessionQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acid):
            query['Acid'] = request.acid
        if not DaraCore.is_null(request.acid_list):
            query['AcidList'] = request.acid_list
        if not DaraCore.is_null(request.call_result):
            query['CallResult'] = request.call_result
        if not DaraCore.is_null(request.call_result_list):
            query['CallResultList'] = request.call_result_list
        if not DaraCore.is_null(request.call_type):
            query['CallType'] = request.call_type
        if not DaraCore.is_null(request.call_type_list):
            query['CallTypeList'] = request.call_type_list
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.called_number_list):
            query['CalledNumberList'] = request.called_number_list
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.calling_number_list):
            query['CallingNumberList'] = request.calling_number_list
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_id_list):
            query['GroupIdList'] = request.group_id_list
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.member_id):
            query['MemberId'] = request.member_id
        if not DaraCore.is_null(request.member_id_list):
            query['MemberIdList'] = request.member_id_list
        if not DaraCore.is_null(request.member_name):
            query['MemberName'] = request.member_name
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.query_end_time):
            query['QueryEndTime'] = request.query_end_time
        if not DaraCore.is_null(request.query_start_time):
            query['QueryStartTime'] = request.query_start_time
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.servicer_id):
            query['ServicerId'] = request.servicer_id
        if not DaraCore.is_null(request.servicer_id_list):
            query['ServicerIdList'] = request.servicer_id_list
        if not DaraCore.is_null(request.servicer_name):
            query['ServicerName'] = request.servicer_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'HotlineSessionQuery',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HotlineSessionQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hotline_session_query(
        self,
        request: main_models.HotlineSessionQueryRequest,
    ) -> main_models.HotlineSessionQueryResponse:
        runtime = RuntimeOptions()
        return self.hotline_session_query_with_options(request, runtime)

    async def hotline_session_query_async(
        self,
        request: main_models.HotlineSessionQueryRequest,
    ) -> main_models.HotlineSessionQueryResponse:
        runtime = RuntimeOptions()
        return await self.hotline_session_query_with_options_async(request, runtime)

    def import_one_task_phone_number_with_options(
        self,
        tmp_req: main_models.ImportOneTaskPhoneNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportOneTaskPhoneNumberResponse:
        tmp_req.validate()
        request = main_models.ImportOneTaskPhoneNumberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.variables):
            request.variables_shrink = Utils.array_to_string_with_specified_style(tmp_req.variables, 'Variables', 'json')
        query = {}
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.variables_shrink):
            query['Variables'] = request.variables_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportOneTaskPhoneNumber',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportOneTaskPhoneNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_one_task_phone_number_with_options_async(
        self,
        tmp_req: main_models.ImportOneTaskPhoneNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportOneTaskPhoneNumberResponse:
        tmp_req.validate()
        request = main_models.ImportOneTaskPhoneNumberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.variables):
            request.variables_shrink = Utils.array_to_string_with_specified_style(tmp_req.variables, 'Variables', 'json')
        query = {}
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.variables_shrink):
            query['Variables'] = request.variables_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportOneTaskPhoneNumber',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportOneTaskPhoneNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_one_task_phone_number(
        self,
        request: main_models.ImportOneTaskPhoneNumberRequest,
    ) -> main_models.ImportOneTaskPhoneNumberResponse:
        runtime = RuntimeOptions()
        return self.import_one_task_phone_number_with_options(request, runtime)

    async def import_one_task_phone_number_async(
        self,
        request: main_models.ImportOneTaskPhoneNumberRequest,
    ) -> main_models.ImportOneTaskPhoneNumberResponse:
        runtime = RuntimeOptions()
        return await self.import_one_task_phone_number_with_options_async(request, runtime)

    def import_task_number_datas_with_options(
        self,
        tmp_req: main_models.ImportTaskNumberDatasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportTaskNumberDatasResponse:
        tmp_req.validate()
        request = main_models.ImportTaskNumberDatasShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.phone_number_list):
            request.phone_number_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.phone_number_list, 'PhoneNumberList', 'json')
        query = {}
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.oss_file_name):
            query['OssFileName'] = request.oss_file_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        body = {}
        if not DaraCore.is_null(request.phone_number_list_shrink):
            body['PhoneNumberList'] = request.phone_number_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportTaskNumberDatas',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportTaskNumberDatasResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_task_number_datas_with_options_async(
        self,
        tmp_req: main_models.ImportTaskNumberDatasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportTaskNumberDatasResponse:
        tmp_req.validate()
        request = main_models.ImportTaskNumberDatasShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.phone_number_list):
            request.phone_number_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.phone_number_list, 'PhoneNumberList', 'json')
        query = {}
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.oss_file_name):
            query['OssFileName'] = request.oss_file_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        body = {}
        if not DaraCore.is_null(request.phone_number_list_shrink):
            body['PhoneNumberList'] = request.phone_number_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportTaskNumberDatas',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportTaskNumberDatasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_task_number_datas(
        self,
        request: main_models.ImportTaskNumberDatasRequest,
    ) -> main_models.ImportTaskNumberDatasResponse:
        runtime = RuntimeOptions()
        return self.import_task_number_datas_with_options(request, runtime)

    async def import_task_number_datas_async(
        self,
        request: main_models.ImportTaskNumberDatasRequest,
    ) -> main_models.ImportTaskNumberDatasResponse:
        runtime = RuntimeOptions()
        return await self.import_task_number_datas_with_options_async(request, runtime)

    def insert_ai_outbound_phone_nums_with_options(
        self,
        tmp_req: main_models.InsertAiOutboundPhoneNumsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InsertAiOutboundPhoneNumsResponse:
        tmp_req.validate()
        request = main_models.InsertAiOutboundPhoneNumsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.details):
            request.details_shrink = Utils.array_to_string_with_specified_style(tmp_req.details, 'Details', 'json')
        query = {}
        if not DaraCore.is_null(request.batch_version):
            query['BatchVersion'] = request.batch_version
        if not DaraCore.is_null(request.details_shrink):
            query['Details'] = request.details_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertAiOutboundPhoneNums',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertAiOutboundPhoneNumsResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_ai_outbound_phone_nums_with_options_async(
        self,
        tmp_req: main_models.InsertAiOutboundPhoneNumsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InsertAiOutboundPhoneNumsResponse:
        tmp_req.validate()
        request = main_models.InsertAiOutboundPhoneNumsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.details):
            request.details_shrink = Utils.array_to_string_with_specified_style(tmp_req.details, 'Details', 'json')
        query = {}
        if not DaraCore.is_null(request.batch_version):
            query['BatchVersion'] = request.batch_version
        if not DaraCore.is_null(request.details_shrink):
            query['Details'] = request.details_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertAiOutboundPhoneNums',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertAiOutboundPhoneNumsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_ai_outbound_phone_nums(
        self,
        request: main_models.InsertAiOutboundPhoneNumsRequest,
    ) -> main_models.InsertAiOutboundPhoneNumsResponse:
        runtime = RuntimeOptions()
        return self.insert_ai_outbound_phone_nums_with_options(request, runtime)

    async def insert_ai_outbound_phone_nums_async(
        self,
        request: main_models.InsertAiOutboundPhoneNumsRequest,
    ) -> main_models.InsertAiOutboundPhoneNumsResponse:
        runtime = RuntimeOptions()
        return await self.insert_ai_outbound_phone_nums_with_options_async(request, runtime)

    def insert_task_detail_with_options(
        self,
        request: main_models.InsertTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InsertTaskDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_infos):
            query['CallInfos'] = request.call_infos
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.outbound_task_id):
            query['OutboundTaskId'] = request.outbound_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertTaskDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_task_detail_with_options_async(
        self,
        request: main_models.InsertTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InsertTaskDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_infos):
            query['CallInfos'] = request.call_infos
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.outbound_task_id):
            query['OutboundTaskId'] = request.outbound_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertTaskDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_task_detail(
        self,
        request: main_models.InsertTaskDetailRequest,
    ) -> main_models.InsertTaskDetailResponse:
        runtime = RuntimeOptions()
        return self.insert_task_detail_with_options(request, runtime)

    async def insert_task_detail_async(
        self,
        request: main_models.InsertTaskDetailRequest,
    ) -> main_models.InsertTaskDetailResponse:
        runtime = RuntimeOptions()
        return await self.insert_task_detail_with_options_async(request, runtime)

    def join_third_call_with_options(
        self,
        request: main_models.JoinThirdCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.JoinThirdCallResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.call_id):
            body['CallId'] = request.call_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not DaraCore.is_null(request.hold_connection_id):
            body['HoldConnectionId'] = request.hold_connection_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'JoinThirdCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.JoinThirdCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def join_third_call_with_options_async(
        self,
        request: main_models.JoinThirdCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.JoinThirdCallResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.call_id):
            body['CallId'] = request.call_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not DaraCore.is_null(request.hold_connection_id):
            body['HoldConnectionId'] = request.hold_connection_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'JoinThirdCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.JoinThirdCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def join_third_call(
        self,
        request: main_models.JoinThirdCallRequest,
    ) -> main_models.JoinThirdCallResponse:
        runtime = RuntimeOptions()
        return self.join_third_call_with_options(request, runtime)

    async def join_third_call_async(
        self,
        request: main_models.JoinThirdCallRequest,
    ) -> main_models.JoinThirdCallResponse:
        runtime = RuntimeOptions()
        return await self.join_third_call_with_options_async(request, runtime)

    def list_agent_by_skill_group_id_with_options(
        self,
        request: main_models.ListAgentBySkillGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentBySkillGroupIdResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentBySkillGroupId',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentBySkillGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_by_skill_group_id_with_options_async(
        self,
        request: main_models.ListAgentBySkillGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentBySkillGroupIdResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentBySkillGroupId',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentBySkillGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_by_skill_group_id(
        self,
        request: main_models.ListAgentBySkillGroupIdRequest,
    ) -> main_models.ListAgentBySkillGroupIdResponse:
        runtime = RuntimeOptions()
        return self.list_agent_by_skill_group_id_with_options(request, runtime)

    async def list_agent_by_skill_group_id_async(
        self,
        request: main_models.ListAgentBySkillGroupIdRequest,
    ) -> main_models.ListAgentBySkillGroupIdResponse:
        runtime = RuntimeOptions()
        return await self.list_agent_by_skill_group_id_with_options_async(request, runtime)

    def list_aiccs_robot_with_options(
        self,
        request: main_models.ListAiccsRobotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAiccsRobotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.robot_name):
            query['RobotName'] = request.robot_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAiccsRobot',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAiccsRobotResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aiccs_robot_with_options_async(
        self,
        request: main_models.ListAiccsRobotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAiccsRobotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.robot_name):
            query['RobotName'] = request.robot_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAiccsRobot',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAiccsRobotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aiccs_robot(
        self,
        request: main_models.ListAiccsRobotRequest,
    ) -> main_models.ListAiccsRobotResponse:
        runtime = RuntimeOptions()
        return self.list_aiccs_robot_with_options(request, runtime)

    async def list_aiccs_robot_async(
        self,
        request: main_models.ListAiccsRobotRequest,
    ) -> main_models.ListAiccsRobotResponse:
        runtime = RuntimeOptions()
        return await self.list_aiccs_robot_with_options_async(request, runtime)

    def list_available_tts_with_options(
        self,
        request: main_models.ListAvailableTtsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAvailableTtsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tts_voice_code):
            query['TtsVoiceCode'] = request.tts_voice_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAvailableTts',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAvailableTtsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_available_tts_with_options_async(
        self,
        request: main_models.ListAvailableTtsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAvailableTtsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tts_voice_code):
            query['TtsVoiceCode'] = request.tts_voice_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAvailableTts',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAvailableTtsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_available_tts(
        self,
        request: main_models.ListAvailableTtsRequest,
    ) -> main_models.ListAvailableTtsResponse:
        runtime = RuntimeOptions()
        return self.list_available_tts_with_options(request, runtime)

    async def list_available_tts_async(
        self,
        request: main_models.ListAvailableTtsRequest,
    ) -> main_models.ListAvailableTtsResponse:
        runtime = RuntimeOptions()
        return await self.list_available_tts_with_options_async(request, runtime)

    def list_chat_record_detail_with_options(
        self,
        request: main_models.ListChatRecordDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChatRecordDetailResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChatRecordDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChatRecordDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chat_record_detail_with_options_async(
        self,
        request: main_models.ListChatRecordDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChatRecordDetailResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChatRecordDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChatRecordDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chat_record_detail(
        self,
        request: main_models.ListChatRecordDetailRequest,
    ) -> main_models.ListChatRecordDetailResponse:
        runtime = RuntimeOptions()
        return self.list_chat_record_detail_with_options(request, runtime)

    async def list_chat_record_detail_async(
        self,
        request: main_models.ListChatRecordDetailRequest,
    ) -> main_models.ListChatRecordDetailResponse:
        runtime = RuntimeOptions()
        return await self.list_chat_record_detail_with_options_async(request, runtime)

    def list_dialog_with_options(
        self,
        request: main_models.ListDialogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDialogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called):
            query['Called'] = request.called
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDialog',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDialogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dialog_with_options_async(
        self,
        request: main_models.ListDialogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDialogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called):
            query['Called'] = request.called
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDialog',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDialogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dialog(
        self,
        request: main_models.ListDialogRequest,
    ) -> main_models.ListDialogResponse:
        runtime = RuntimeOptions()
        return self.list_dialog_with_options(request, runtime)

    async def list_dialog_async(
        self,
        request: main_models.ListDialogRequest,
    ) -> main_models.ListDialogResponse:
        runtime = RuntimeOptions()
        return await self.list_dialog_with_options_async(request, runtime)

    def list_hotline_record_with_options(
        self,
        request: main_models.ListHotlineRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotlineRecordResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHotlineRecord',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotlineRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotline_record_with_options_async(
        self,
        request: main_models.ListHotlineRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotlineRecordResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHotlineRecord',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotlineRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotline_record(
        self,
        request: main_models.ListHotlineRecordRequest,
    ) -> main_models.ListHotlineRecordResponse:
        runtime = RuntimeOptions()
        return self.list_hotline_record_with_options(request, runtime)

    async def list_hotline_record_async(
        self,
        request: main_models.ListHotlineRecordRequest,
    ) -> main_models.ListHotlineRecordResponse:
        runtime = RuntimeOptions()
        return await self.list_hotline_record_with_options_async(request, runtime)

    def list_hotline_record_detail_with_options(
        self,
        request: main_models.ListHotlineRecordDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotlineRecordDetailResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHotlineRecordDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotlineRecordDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotline_record_detail_with_options_async(
        self,
        request: main_models.ListHotlineRecordDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotlineRecordDetailResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHotlineRecordDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotlineRecordDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotline_record_detail(
        self,
        request: main_models.ListHotlineRecordDetailRequest,
    ) -> main_models.ListHotlineRecordDetailResponse:
        runtime = RuntimeOptions()
        return self.list_hotline_record_detail_with_options(request, runtime)

    async def list_hotline_record_detail_async(
        self,
        request: main_models.ListHotlineRecordDetailRequest,
    ) -> main_models.ListHotlineRecordDetailResponse:
        runtime = RuntimeOptions()
        return await self.list_hotline_record_detail_with_options_async(request, runtime)

    def list_outbound_phone_number_with_options(
        self,
        request: main_models.ListOutboundPhoneNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOutboundPhoneNumberResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOutboundPhoneNumber',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOutboundPhoneNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_outbound_phone_number_with_options_async(
        self,
        request: main_models.ListOutboundPhoneNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOutboundPhoneNumberResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOutboundPhoneNumber',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOutboundPhoneNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_outbound_phone_number(
        self,
        request: main_models.ListOutboundPhoneNumberRequest,
    ) -> main_models.ListOutboundPhoneNumberResponse:
        runtime = RuntimeOptions()
        return self.list_outbound_phone_number_with_options(request, runtime)

    async def list_outbound_phone_number_async(
        self,
        request: main_models.ListOutboundPhoneNumberRequest,
    ) -> main_models.ListOutboundPhoneNumberResponse:
        runtime = RuntimeOptions()
        return await self.list_outbound_phone_number_with_options_async(request, runtime)

    def list_robot_call_dialog_with_options(
        self,
        request: main_models.ListRobotCallDialogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRobotCallDialogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.create_time):
            query['CreateTime'] = request.create_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRobotCallDialog',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRobotCallDialogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_robot_call_dialog_with_options_async(
        self,
        request: main_models.ListRobotCallDialogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRobotCallDialogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.create_time):
            query['CreateTime'] = request.create_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRobotCallDialog',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRobotCallDialogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_robot_call_dialog(
        self,
        request: main_models.ListRobotCallDialogRequest,
    ) -> main_models.ListRobotCallDialogResponse:
        runtime = RuntimeOptions()
        return self.list_robot_call_dialog_with_options(request, runtime)

    async def list_robot_call_dialog_async(
        self,
        request: main_models.ListRobotCallDialogRequest,
    ) -> main_models.ListRobotCallDialogResponse:
        runtime = RuntimeOptions()
        return await self.list_robot_call_dialog_with_options_async(request, runtime)

    def list_robot_node_with_options(
        self,
        request: main_models.ListRobotNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRobotNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.robot_id):
            query['RobotId'] = request.robot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRobotNode',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRobotNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_robot_node_with_options_async(
        self,
        request: main_models.ListRobotNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRobotNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.robot_id):
            query['RobotId'] = request.robot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRobotNode',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRobotNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_robot_node(
        self,
        request: main_models.ListRobotNodeRequest,
    ) -> main_models.ListRobotNodeResponse:
        runtime = RuntimeOptions()
        return self.list_robot_node_with_options(request, runtime)

    async def list_robot_node_async(
        self,
        request: main_models.ListRobotNodeRequest,
    ) -> main_models.ListRobotNodeResponse:
        runtime = RuntimeOptions()
        return await self.list_robot_node_with_options_async(request, runtime)

    def list_robot_params_with_options(
        self,
        request: main_models.ListRobotParamsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRobotParamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.robot_id):
            query['RobotId'] = request.robot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRobotParams',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRobotParamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_robot_params_with_options_async(
        self,
        request: main_models.ListRobotParamsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRobotParamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.robot_id):
            query['RobotId'] = request.robot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRobotParams',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRobotParamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_robot_params(
        self,
        request: main_models.ListRobotParamsRequest,
    ) -> main_models.ListRobotParamsResponse:
        runtime = RuntimeOptions()
        return self.list_robot_params_with_options(request, runtime)

    async def list_robot_params_async(
        self,
        request: main_models.ListRobotParamsRequest,
    ) -> main_models.ListRobotParamsResponse:
        runtime = RuntimeOptions()
        return await self.list_robot_params_with_options_async(request, runtime)

    def list_roles_with_options(
        self,
        request: main_models.ListRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRolesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRoles',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        request: main_models.ListRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRolesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRoles',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_roles(
        self,
        request: main_models.ListRolesRequest,
    ) -> main_models.ListRolesResponse:
        runtime = RuntimeOptions()
        return self.list_roles_with_options(request, runtime)

    async def list_roles_async(
        self,
        request: main_models.ListRolesRequest,
    ) -> main_models.ListRolesResponse:
        runtime = RuntimeOptions()
        return await self.list_roles_with_options_async(request, runtime)

    def list_skill_group_with_options(
        self,
        request: main_models.ListSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillGroupResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkillGroup',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_skill_group_with_options_async(
        self,
        request: main_models.ListSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillGroupResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkillGroup',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_skill_group(
        self,
        request: main_models.ListSkillGroupRequest,
    ) -> main_models.ListSkillGroupResponse:
        runtime = RuntimeOptions()
        return self.list_skill_group_with_options(request, runtime)

    async def list_skill_group_async(
        self,
        request: main_models.ListSkillGroupRequest,
    ) -> main_models.ListSkillGroupResponse:
        runtime = RuntimeOptions()
        return await self.list_skill_group_with_options_async(request, runtime)

    def list_task_with_options(
        self,
        request: main_models.ListTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.robot_name):
            query['RobotName'] = request.robot_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_with_options_async(
        self,
        request: main_models.ListTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.robot_name):
            query['RobotName'] = request.robot_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task(
        self,
        request: main_models.ListTaskRequest,
    ) -> main_models.ListTaskResponse:
        runtime = RuntimeOptions()
        return self.list_task_with_options(request, runtime)

    async def list_task_async(
        self,
        request: main_models.ListTaskRequest,
    ) -> main_models.ListTaskResponse:
        runtime = RuntimeOptions()
        return await self.list_task_with_options_async(request, runtime)

    def list_task_detail_with_options(
        self,
        request: main_models.ListTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTaskDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called):
            query['Called'] = request.called
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.status_code):
            query['StatusCode'] = request.status_code
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTaskDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_detail_with_options_async(
        self,
        request: main_models.ListTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTaskDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called):
            query['Called'] = request.called
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.status_code):
            query['StatusCode'] = request.status_code
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTaskDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task_detail(
        self,
        request: main_models.ListTaskDetailRequest,
    ) -> main_models.ListTaskDetailResponse:
        runtime = RuntimeOptions()
        return self.list_task_detail_with_options(request, runtime)

    async def list_task_detail_async(
        self,
        request: main_models.ListTaskDetailRequest,
    ) -> main_models.ListTaskDetailResponse:
        runtime = RuntimeOptions()
        return await self.list_task_detail_with_options_async(request, runtime)

    def llm_smart_call_with_options(
        self,
        tmp_req: main_models.LlmSmartCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LlmSmartCallResponse:
        tmp_req.validate()
        request = main_models.LlmSmartCallShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_param):
            request.biz_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_param, 'BizParam', 'json')
        if not DaraCore.is_null(tmp_req.prompt_param):
            request.prompt_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.prompt_param, 'PromptParam', 'json')
        if not DaraCore.is_null(tmp_req.start_word_param):
            request.start_word_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.start_word_param, 'StartWordParam', 'json')
        query = {}
        if not DaraCore.is_null(request.application_code):
            query['ApplicationCode'] = request.application_code
        if not DaraCore.is_null(request.biz_param_shrink):
            query['BizParam'] = request.biz_param_shrink
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.caller_number):
            query['CallerNumber'] = request.caller_number
        if not DaraCore.is_null(request.customer_line_code):
            query['CustomerLineCode'] = request.customer_line_code
        if not DaraCore.is_null(request.extension):
            query['Extension'] = request.extension
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.prompt_param_shrink):
            query['PromptParam'] = request.prompt_param_shrink
        if not DaraCore.is_null(request.session_timeout):
            query['SessionTimeout'] = request.session_timeout
        if not DaraCore.is_null(request.start_word_param_shrink):
            query['StartWordParam'] = request.start_word_param_shrink
        if not DaraCore.is_null(request.tts_speed):
            query['TtsSpeed'] = request.tts_speed
        if not DaraCore.is_null(request.tts_voice_code):
            query['TtsVoiceCode'] = request.tts_voice_code
        if not DaraCore.is_null(request.tts_volume):
            query['TtsVolume'] = request.tts_volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LlmSmartCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LlmSmartCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def llm_smart_call_with_options_async(
        self,
        tmp_req: main_models.LlmSmartCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LlmSmartCallResponse:
        tmp_req.validate()
        request = main_models.LlmSmartCallShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_param):
            request.biz_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_param, 'BizParam', 'json')
        if not DaraCore.is_null(tmp_req.prompt_param):
            request.prompt_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.prompt_param, 'PromptParam', 'json')
        if not DaraCore.is_null(tmp_req.start_word_param):
            request.start_word_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.start_word_param, 'StartWordParam', 'json')
        query = {}
        if not DaraCore.is_null(request.application_code):
            query['ApplicationCode'] = request.application_code
        if not DaraCore.is_null(request.biz_param_shrink):
            query['BizParam'] = request.biz_param_shrink
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.caller_number):
            query['CallerNumber'] = request.caller_number
        if not DaraCore.is_null(request.customer_line_code):
            query['CustomerLineCode'] = request.customer_line_code
        if not DaraCore.is_null(request.extension):
            query['Extension'] = request.extension
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.prompt_param_shrink):
            query['PromptParam'] = request.prompt_param_shrink
        if not DaraCore.is_null(request.session_timeout):
            query['SessionTimeout'] = request.session_timeout
        if not DaraCore.is_null(request.start_word_param_shrink):
            query['StartWordParam'] = request.start_word_param_shrink
        if not DaraCore.is_null(request.tts_speed):
            query['TtsSpeed'] = request.tts_speed
        if not DaraCore.is_null(request.tts_voice_code):
            query['TtsVoiceCode'] = request.tts_voice_code
        if not DaraCore.is_null(request.tts_volume):
            query['TtsVolume'] = request.tts_volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LlmSmartCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LlmSmartCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def llm_smart_call(
        self,
        request: main_models.LlmSmartCallRequest,
    ) -> main_models.LlmSmartCallResponse:
        runtime = RuntimeOptions()
        return self.llm_smart_call_with_options(request, runtime)

    async def llm_smart_call_async(
        self,
        request: main_models.LlmSmartCallRequest,
    ) -> main_models.LlmSmartCallResponse:
        runtime = RuntimeOptions()
        return await self.llm_smart_call_with_options_async(request, runtime)

    def llm_smart_call_encrypt_with_options(
        self,
        tmp_req: main_models.LlmSmartCallEncryptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LlmSmartCallEncryptResponse:
        tmp_req.validate()
        request = main_models.LlmSmartCallEncryptShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.prompt_param):
            request.prompt_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.prompt_param, 'PromptParam', 'json')
        if not DaraCore.is_null(tmp_req.start_word_param):
            request.start_word_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.start_word_param, 'StartWordParam', 'json')
        query = {}
        if not DaraCore.is_null(request.application_code):
            query['ApplicationCode'] = request.application_code
        if not DaraCore.is_null(request.caller_number):
            query['CallerNumber'] = request.caller_number
        if not DaraCore.is_null(request.encrypt_called_number):
            query['EncryptCalledNumber'] = request.encrypt_called_number
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prompt_param_shrink):
            query['PromptParam'] = request.prompt_param_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_word_param_shrink):
            query['StartWordParam'] = request.start_word_param_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LlmSmartCallEncrypt',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LlmSmartCallEncryptResponse(),
            self.call_api(params, req, runtime)
        )

    async def llm_smart_call_encrypt_with_options_async(
        self,
        tmp_req: main_models.LlmSmartCallEncryptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LlmSmartCallEncryptResponse:
        tmp_req.validate()
        request = main_models.LlmSmartCallEncryptShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.prompt_param):
            request.prompt_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.prompt_param, 'PromptParam', 'json')
        if not DaraCore.is_null(tmp_req.start_word_param):
            request.start_word_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.start_word_param, 'StartWordParam', 'json')
        query = {}
        if not DaraCore.is_null(request.application_code):
            query['ApplicationCode'] = request.application_code
        if not DaraCore.is_null(request.caller_number):
            query['CallerNumber'] = request.caller_number
        if not DaraCore.is_null(request.encrypt_called_number):
            query['EncryptCalledNumber'] = request.encrypt_called_number
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prompt_param_shrink):
            query['PromptParam'] = request.prompt_param_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_word_param_shrink):
            query['StartWordParam'] = request.start_word_param_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LlmSmartCallEncrypt',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LlmSmartCallEncryptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def llm_smart_call_encrypt(
        self,
        request: main_models.LlmSmartCallEncryptRequest,
    ) -> main_models.LlmSmartCallEncryptResponse:
        runtime = RuntimeOptions()
        return self.llm_smart_call_encrypt_with_options(request, runtime)

    async def llm_smart_call_encrypt_async(
        self,
        request: main_models.LlmSmartCallEncryptRequest,
    ) -> main_models.LlmSmartCallEncryptResponse:
        runtime = RuntimeOptions()
        return await self.llm_smart_call_encrypt_with_options_async(request, runtime)

    def make_call_with_options(
        self,
        request: main_models.MakeCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MakeCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.command_code):
            query['CommandCode'] = request.command_code
        if not DaraCore.is_null(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not DaraCore.is_null(request.outer_account_id):
            query['OuterAccountId'] = request.outer_account_id
        if not DaraCore.is_null(request.outer_account_type):
            query['OuterAccountType'] = request.outer_account_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MakeCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MakeCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def make_call_with_options_async(
        self,
        request: main_models.MakeCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MakeCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.command_code):
            query['CommandCode'] = request.command_code
        if not DaraCore.is_null(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not DaraCore.is_null(request.outer_account_id):
            query['OuterAccountId'] = request.outer_account_id
        if not DaraCore.is_null(request.outer_account_type):
            query['OuterAccountType'] = request.outer_account_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MakeCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MakeCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def make_call(
        self,
        request: main_models.MakeCallRequest,
    ) -> main_models.MakeCallResponse:
        runtime = RuntimeOptions()
        return self.make_call_with_options(request, runtime)

    async def make_call_async(
        self,
        request: main_models.MakeCallRequest,
    ) -> main_models.MakeCallResponse:
        runtime = RuntimeOptions()
        return await self.make_call_with_options_async(request, runtime)

    def make_double_call_with_options(
        self,
        request: main_models.MakeDoubleCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MakeDoubleCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.biz_data):
            query['BizData'] = request.biz_data
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.member_phone):
            query['MemberPhone'] = request.member_phone
        if not DaraCore.is_null(request.outbound_call_number):
            query['OutboundCallNumber'] = request.outbound_call_number
        if not DaraCore.is_null(request.servicer_phone):
            query['ServicerPhone'] = request.servicer_phone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MakeDoubleCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MakeDoubleCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def make_double_call_with_options_async(
        self,
        request: main_models.MakeDoubleCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MakeDoubleCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.biz_data):
            query['BizData'] = request.biz_data
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.member_phone):
            query['MemberPhone'] = request.member_phone
        if not DaraCore.is_null(request.outbound_call_number):
            query['OutboundCallNumber'] = request.outbound_call_number
        if not DaraCore.is_null(request.servicer_phone):
            query['ServicerPhone'] = request.servicer_phone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MakeDoubleCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MakeDoubleCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def make_double_call(
        self,
        request: main_models.MakeDoubleCallRequest,
    ) -> main_models.MakeDoubleCallResponse:
        runtime = RuntimeOptions()
        return self.make_double_call_with_options(request, runtime)

    async def make_double_call_async(
        self,
        request: main_models.MakeDoubleCallRequest,
    ) -> main_models.MakeDoubleCallResponse:
        runtime = RuntimeOptions()
        return await self.make_double_call_with_options_async(request, runtime)

    def page_query_agent_list_with_options(
        self,
        request: main_models.PageQueryAgentListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PageQueryAgentListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_name):
            query['AgentName'] = request.agent_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PageQueryAgentList',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PageQueryAgentListResponse(),
            self.call_api(params, req, runtime)
        )

    async def page_query_agent_list_with_options_async(
        self,
        request: main_models.PageQueryAgentListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PageQueryAgentListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_name):
            query['AgentName'] = request.agent_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PageQueryAgentList',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PageQueryAgentListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def page_query_agent_list(
        self,
        request: main_models.PageQueryAgentListRequest,
    ) -> main_models.PageQueryAgentListResponse:
        runtime = RuntimeOptions()
        return self.page_query_agent_list_with_options(request, runtime)

    async def page_query_agent_list_async(
        self,
        request: main_models.PageQueryAgentListRequest,
    ) -> main_models.PageQueryAgentListResponse:
        runtime = RuntimeOptions()
        return await self.page_query_agent_list_with_options_async(request, runtime)

    def query_ai_call_detail_page_with_options(
        self,
        tmp_req: main_models.QueryAiCallDetailPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAiCallDetailPageResponse:
        tmp_req.validate()
        request = main_models.QueryAiCallDetailPageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.detail_ids):
            request.detail_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.detail_ids, 'DetailIds', 'json')
        query = {}
        if not DaraCore.is_null(request.batch_id):
            query['BatchId'] = request.batch_id
        if not DaraCore.is_null(request.call_result):
            query['CallResult'] = request.call_result
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.detail_ids_shrink):
            query['DetailIds'] = request.detail_ids_shrink
        if not DaraCore.is_null(request.end_calling_time):
            query['EndCallingTime'] = request.end_calling_time
        if not DaraCore.is_null(request.end_imported_time):
            query['EndImportedTime'] = request.end_imported_time
        if not DaraCore.is_null(request.major_intent):
            query['MajorIntent'] = request.major_intent
        if not DaraCore.is_null(request.max_conversation_duration):
            query['MaxConversationDuration'] = request.max_conversation_duration
        if not DaraCore.is_null(request.min_conversation_duration):
            query['MinConversationDuration'] = request.min_conversation_duration
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_calling_time):
            query['StartCallingTime'] = request.start_calling_time
        if not DaraCore.is_null(request.start_imported_time):
            query['StartImportedTime'] = request.start_imported_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAiCallDetailPage',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAiCallDetailPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ai_call_detail_page_with_options_async(
        self,
        tmp_req: main_models.QueryAiCallDetailPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAiCallDetailPageResponse:
        tmp_req.validate()
        request = main_models.QueryAiCallDetailPageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.detail_ids):
            request.detail_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.detail_ids, 'DetailIds', 'json')
        query = {}
        if not DaraCore.is_null(request.batch_id):
            query['BatchId'] = request.batch_id
        if not DaraCore.is_null(request.call_result):
            query['CallResult'] = request.call_result
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.detail_ids_shrink):
            query['DetailIds'] = request.detail_ids_shrink
        if not DaraCore.is_null(request.end_calling_time):
            query['EndCallingTime'] = request.end_calling_time
        if not DaraCore.is_null(request.end_imported_time):
            query['EndImportedTime'] = request.end_imported_time
        if not DaraCore.is_null(request.major_intent):
            query['MajorIntent'] = request.major_intent
        if not DaraCore.is_null(request.max_conversation_duration):
            query['MaxConversationDuration'] = request.max_conversation_duration
        if not DaraCore.is_null(request.min_conversation_duration):
            query['MinConversationDuration'] = request.min_conversation_duration
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_calling_time):
            query['StartCallingTime'] = request.start_calling_time
        if not DaraCore.is_null(request.start_imported_time):
            query['StartImportedTime'] = request.start_imported_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAiCallDetailPage',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAiCallDetailPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ai_call_detail_page(
        self,
        request: main_models.QueryAiCallDetailPageRequest,
    ) -> main_models.QueryAiCallDetailPageResponse:
        runtime = RuntimeOptions()
        return self.query_ai_call_detail_page_with_options(request, runtime)

    async def query_ai_call_detail_page_async(
        self,
        request: main_models.QueryAiCallDetailPageRequest,
    ) -> main_models.QueryAiCallDetailPageResponse:
        runtime = RuntimeOptions()
        return await self.query_ai_call_detail_page_with_options_async(request, runtime)

    def query_ai_call_task_detail_with_options(
        self,
        request: main_models.QueryAiCallTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAiCallTaskDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAiCallTaskDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAiCallTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ai_call_task_detail_with_options_async(
        self,
        request: main_models.QueryAiCallTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAiCallTaskDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAiCallTaskDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAiCallTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ai_call_task_detail(
        self,
        request: main_models.QueryAiCallTaskDetailRequest,
    ) -> main_models.QueryAiCallTaskDetailResponse:
        runtime = RuntimeOptions()
        return self.query_ai_call_task_detail_with_options(request, runtime)

    async def query_ai_call_task_detail_async(
        self,
        request: main_models.QueryAiCallTaskDetailRequest,
    ) -> main_models.QueryAiCallTaskDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_ai_call_task_detail_with_options_async(request, runtime)

    def query_ai_call_task_page_with_options(
        self,
        request: main_models.QueryAiCallTaskPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAiCallTaskPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_name):
            query['AgentName'] = request.agent_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAiCallTaskPage',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAiCallTaskPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ai_call_task_page_with_options_async(
        self,
        request: main_models.QueryAiCallTaskPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAiCallTaskPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_name):
            query['AgentName'] = request.agent_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAiCallTaskPage',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAiCallTaskPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ai_call_task_page(
        self,
        request: main_models.QueryAiCallTaskPageRequest,
    ) -> main_models.QueryAiCallTaskPageResponse:
        runtime = RuntimeOptions()
        return self.query_ai_call_task_page_with_options(request, runtime)

    async def query_ai_call_task_page_async(
        self,
        request: main_models.QueryAiCallTaskPageRequest,
    ) -> main_models.QueryAiCallTaskPageResponse:
        runtime = RuntimeOptions()
        return await self.query_ai_call_task_page_with_options_async(request, runtime)

    def query_ai_voice_agent_detail_with_options(
        self,
        request: main_models.QueryAiVoiceAgentDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAiVoiceAgentDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAiVoiceAgentDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAiVoiceAgentDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ai_voice_agent_detail_with_options_async(
        self,
        request: main_models.QueryAiVoiceAgentDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAiVoiceAgentDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAiVoiceAgentDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAiVoiceAgentDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ai_voice_agent_detail(
        self,
        request: main_models.QueryAiVoiceAgentDetailRequest,
    ) -> main_models.QueryAiVoiceAgentDetailResponse:
        runtime = RuntimeOptions()
        return self.query_ai_voice_agent_detail_with_options(request, runtime)

    async def query_ai_voice_agent_detail_async(
        self,
        request: main_models.QueryAiVoiceAgentDetailRequest,
    ) -> main_models.QueryAiVoiceAgentDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_ai_voice_agent_detail_with_options_async(request, runtime)

    def query_conversation_detail_info_with_options(
        self,
        request: main_models.QueryConversationDetailInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryConversationDetailInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_id):
            query['BatchId'] = request.batch_id
        if not DaraCore.is_null(request.detail_id):
            query['DetailId'] = request.detail_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryConversationDetailInfo',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryConversationDetailInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_conversation_detail_info_with_options_async(
        self,
        request: main_models.QueryConversationDetailInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryConversationDetailInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_id):
            query['BatchId'] = request.batch_id
        if not DaraCore.is_null(request.detail_id):
            query['DetailId'] = request.detail_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryConversationDetailInfo',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryConversationDetailInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_conversation_detail_info(
        self,
        request: main_models.QueryConversationDetailInfoRequest,
    ) -> main_models.QueryConversationDetailInfoResponse:
        runtime = RuntimeOptions()
        return self.query_conversation_detail_info_with_options(request, runtime)

    async def query_conversation_detail_info_async(
        self,
        request: main_models.QueryConversationDetailInfoRequest,
    ) -> main_models.QueryConversationDetailInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_conversation_detail_info_with_options_async(request, runtime)

    def query_hotline_in_queue_with_options(
        self,
        request: main_models.QueryHotlineInQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryHotlineInQueueResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryHotlineInQueue',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryHotlineInQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_hotline_in_queue_with_options_async(
        self,
        request: main_models.QueryHotlineInQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryHotlineInQueueResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryHotlineInQueue',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryHotlineInQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_hotline_in_queue(
        self,
        request: main_models.QueryHotlineInQueueRequest,
    ) -> main_models.QueryHotlineInQueueResponse:
        runtime = RuntimeOptions()
        return self.query_hotline_in_queue_with_options(request, runtime)

    async def query_hotline_in_queue_async(
        self,
        request: main_models.QueryHotlineInQueueRequest,
    ) -> main_models.QueryHotlineInQueueResponse:
        runtime = RuntimeOptions()
        return await self.query_hotline_in_queue_with_options_async(request, runtime)

    def query_hotline_number_with_options(
        self,
        tmp_req: main_models.QueryHotlineNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryHotlineNumberResponse:
        tmp_req.validate()
        request = main_models.QueryHotlineNumberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.group_ids):
            request.group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryHotlineNumber',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryHotlineNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_hotline_number_with_options_async(
        self,
        tmp_req: main_models.QueryHotlineNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryHotlineNumberResponse:
        tmp_req.validate()
        request = main_models.QueryHotlineNumberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.group_ids):
            request.group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryHotlineNumber',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryHotlineNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_hotline_number(
        self,
        request: main_models.QueryHotlineNumberRequest,
    ) -> main_models.QueryHotlineNumberResponse:
        runtime = RuntimeOptions()
        return self.query_hotline_number_with_options(request, runtime)

    async def query_hotline_number_async(
        self,
        request: main_models.QueryHotlineNumberRequest,
    ) -> main_models.QueryHotlineNumberResponse:
        runtime = RuntimeOptions()
        return await self.query_hotline_number_with_options_async(request, runtime)

    def query_outbound_task_with_options(
        self,
        request: main_models.QueryOutboundTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryOutboundTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ani):
            query['Ani'] = request.ani
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.department_id):
            query['DepartmentId'] = request.department_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.skill_group):
            query['SkillGroup'] = request.skill_group
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryOutboundTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryOutboundTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_outbound_task_with_options_async(
        self,
        request: main_models.QueryOutboundTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryOutboundTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ani):
            query['Ani'] = request.ani
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.department_id):
            query['DepartmentId'] = request.department_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.skill_group):
            query['SkillGroup'] = request.skill_group
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryOutboundTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryOutboundTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_outbound_task(
        self,
        request: main_models.QueryOutboundTaskRequest,
    ) -> main_models.QueryOutboundTaskResponse:
        runtime = RuntimeOptions()
        return self.query_outbound_task_with_options(request, runtime)

    async def query_outbound_task_async(
        self,
        request: main_models.QueryOutboundTaskRequest,
    ) -> main_models.QueryOutboundTaskResponse:
        runtime = RuntimeOptions()
        return await self.query_outbound_task_with_options_async(request, runtime)

    def query_skill_groups_with_options(
        self,
        request: main_models.QuerySkillGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySkillGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.department_id):
            query['DepartmentId'] = request.department_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySkillGroups',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySkillGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_skill_groups_with_options_async(
        self,
        request: main_models.QuerySkillGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySkillGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.department_id):
            query['DepartmentId'] = request.department_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySkillGroups',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySkillGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_skill_groups(
        self,
        request: main_models.QuerySkillGroupsRequest,
    ) -> main_models.QuerySkillGroupsResponse:
        runtime = RuntimeOptions()
        return self.query_skill_groups_with_options(request, runtime)

    async def query_skill_groups_async(
        self,
        request: main_models.QuerySkillGroupsRequest,
    ) -> main_models.QuerySkillGroupsResponse:
        runtime = RuntimeOptions()
        return await self.query_skill_groups_with_options_async(request, runtime)

    def query_task_detail_with_options(
        self,
        request: main_models.QueryTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTaskDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ani):
            query['Ani'] = request.ani
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.department_id_list):
            query['DepartmentIdList'] = request.department_id_list
        if not DaraCore.is_null(request.dnis):
            query['Dnis'] = request.dnis
        if not DaraCore.is_null(request.end_reason_list):
            query['EndReasonList'] = request.end_reason_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.outbound_task_id):
            query['OutboundTaskId'] = request.outbound_task_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.priority_list):
            query['PriorityList'] = request.priority_list
        if not DaraCore.is_null(request.servicer_id):
            query['ServicerId'] = request.servicer_id
        if not DaraCore.is_null(request.servicer_name):
            query['ServicerName'] = request.servicer_name
        if not DaraCore.is_null(request.sid):
            query['Sid'] = request.sid
        if not DaraCore.is_null(request.skill_group):
            query['SkillGroup'] = request.skill_group
        if not DaraCore.is_null(request.status_list):
            query['StatusList'] = request.status_list
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTaskDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_task_detail_with_options_async(
        self,
        request: main_models.QueryTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTaskDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ani):
            query['Ani'] = request.ani
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.department_id_list):
            query['DepartmentIdList'] = request.department_id_list
        if not DaraCore.is_null(request.dnis):
            query['Dnis'] = request.dnis
        if not DaraCore.is_null(request.end_reason_list):
            query['EndReasonList'] = request.end_reason_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.outbound_task_id):
            query['OutboundTaskId'] = request.outbound_task_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.priority_list):
            query['PriorityList'] = request.priority_list
        if not DaraCore.is_null(request.servicer_id):
            query['ServicerId'] = request.servicer_id
        if not DaraCore.is_null(request.servicer_name):
            query['ServicerName'] = request.servicer_name
        if not DaraCore.is_null(request.sid):
            query['Sid'] = request.sid
        if not DaraCore.is_null(request.skill_group):
            query['SkillGroup'] = request.skill_group
        if not DaraCore.is_null(request.status_list):
            query['StatusList'] = request.status_list
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTaskDetail',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_task_detail(
        self,
        request: main_models.QueryTaskDetailRequest,
    ) -> main_models.QueryTaskDetailResponse:
        runtime = RuntimeOptions()
        return self.query_task_detail_with_options(request, runtime)

    async def query_task_detail_async(
        self,
        request: main_models.QueryTaskDetailRequest,
    ) -> main_models.QueryTaskDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_task_detail_with_options_async(request, runtime)

    def query_tickets_with_options(
        self,
        tmp_req: main_models.QueryTicketsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTicketsResponse:
        tmp_req.validate()
        request = main_models.QueryTicketsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extra):
            request.extra_shrink = Utils.array_to_string_with_specified_style(tmp_req.extra, 'Extra', 'json')
        body = {}
        if not DaraCore.is_null(request.case_id):
            body['CaseId'] = request.case_id
        if not DaraCore.is_null(request.case_status):
            body['CaseStatus'] = request.case_status
        if not DaraCore.is_null(request.case_type):
            body['CaseType'] = request.case_type
        if not DaraCore.is_null(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.channel_type):
            body['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.deal_id):
            body['DealId'] = request.deal_id
        if not DaraCore.is_null(request.extra_shrink):
            body['Extra'] = request.extra_shrink
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sr_type):
            body['SrType'] = request.sr_type
        if not DaraCore.is_null(request.task_status):
            body['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.touch_id):
            body['TouchId'] = request.touch_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryTickets',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTicketsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tickets_with_options_async(
        self,
        tmp_req: main_models.QueryTicketsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTicketsResponse:
        tmp_req.validate()
        request = main_models.QueryTicketsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extra):
            request.extra_shrink = Utils.array_to_string_with_specified_style(tmp_req.extra, 'Extra', 'json')
        body = {}
        if not DaraCore.is_null(request.case_id):
            body['CaseId'] = request.case_id
        if not DaraCore.is_null(request.case_status):
            body['CaseStatus'] = request.case_status
        if not DaraCore.is_null(request.case_type):
            body['CaseType'] = request.case_type
        if not DaraCore.is_null(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.channel_type):
            body['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.deal_id):
            body['DealId'] = request.deal_id
        if not DaraCore.is_null(request.extra_shrink):
            body['Extra'] = request.extra_shrink
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sr_type):
            body['SrType'] = request.sr_type
        if not DaraCore.is_null(request.task_status):
            body['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.touch_id):
            body['TouchId'] = request.touch_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryTickets',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTicketsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_tickets(
        self,
        request: main_models.QueryTicketsRequest,
    ) -> main_models.QueryTicketsResponse:
        runtime = RuntimeOptions()
        return self.query_tickets_with_options(request, runtime)

    async def query_tickets_async(
        self,
        request: main_models.QueryTicketsRequest,
    ) -> main_models.QueryTicketsResponse:
        runtime = RuntimeOptions()
        return await self.query_tickets_with_options_async(request, runtime)

    def query_touch_list_with_options(
        self,
        request: main_models.QueryTouchListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTouchListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.channel_type):
            body['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.close_time_end):
            body['CloseTimeEnd'] = request.close_time_end
        if not DaraCore.is_null(request.close_time_start):
            body['CloseTimeStart'] = request.close_time_start
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.evaluation_level):
            body['EvaluationLevel'] = request.evaluation_level
        if not DaraCore.is_null(request.evaluation_score):
            body['EvaluationScore'] = request.evaluation_score
        if not DaraCore.is_null(request.evaluation_status):
            body['EvaluationStatus'] = request.evaluation_status
        if not DaraCore.is_null(request.first_time_end):
            body['FirstTimeEnd'] = request.first_time_end
        if not DaraCore.is_null(request.first_time_start):
            body['FirstTimeStart'] = request.first_time_start
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.member_id):
            body['MemberId'] = request.member_id
        if not DaraCore.is_null(request.member_name):
            body['MemberName'] = request.member_name
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.queue_id):
            body['QueueId'] = request.queue_id
        if not DaraCore.is_null(request.servicer_id):
            body['ServicerId'] = request.servicer_id
        if not DaraCore.is_null(request.servicer_name):
            body['ServicerName'] = request.servicer_name
        if not DaraCore.is_null(request.touch_id):
            body['TouchId'] = request.touch_id
        if not DaraCore.is_null(request.touch_type):
            body['TouchType'] = request.touch_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryTouchList',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTouchListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_touch_list_with_options_async(
        self,
        request: main_models.QueryTouchListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTouchListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.channel_type):
            body['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.close_time_end):
            body['CloseTimeEnd'] = request.close_time_end
        if not DaraCore.is_null(request.close_time_start):
            body['CloseTimeStart'] = request.close_time_start
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.evaluation_level):
            body['EvaluationLevel'] = request.evaluation_level
        if not DaraCore.is_null(request.evaluation_score):
            body['EvaluationScore'] = request.evaluation_score
        if not DaraCore.is_null(request.evaluation_status):
            body['EvaluationStatus'] = request.evaluation_status
        if not DaraCore.is_null(request.first_time_end):
            body['FirstTimeEnd'] = request.first_time_end
        if not DaraCore.is_null(request.first_time_start):
            body['FirstTimeStart'] = request.first_time_start
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.member_id):
            body['MemberId'] = request.member_id
        if not DaraCore.is_null(request.member_name):
            body['MemberName'] = request.member_name
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.queue_id):
            body['QueueId'] = request.queue_id
        if not DaraCore.is_null(request.servicer_id):
            body['ServicerId'] = request.servicer_id
        if not DaraCore.is_null(request.servicer_name):
            body['ServicerName'] = request.servicer_name
        if not DaraCore.is_null(request.touch_id):
            body['TouchId'] = request.touch_id
        if not DaraCore.is_null(request.touch_type):
            body['TouchType'] = request.touch_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryTouchList',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTouchListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_touch_list(
        self,
        request: main_models.QueryTouchListRequest,
    ) -> main_models.QueryTouchListResponse:
        runtime = RuntimeOptions()
        return self.query_touch_list_with_options(request, runtime)

    async def query_touch_list_async(
        self,
        request: main_models.QueryTouchListRequest,
    ) -> main_models.QueryTouchListResponse:
        runtime = RuntimeOptions()
        return await self.query_touch_list_with_options_async(request, runtime)

    def remove_agent_from_skill_group_with_options(
        self,
        tmp_req: main_models.RemoveAgentFromSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveAgentFromSkillGroupResponse:
        tmp_req.validate()
        request = main_models.RemoveAgentFromSkillGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_ids_shrink):
            query['AgentIds'] = request.agent_ids_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveAgentFromSkillGroup',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveAgentFromSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_agent_from_skill_group_with_options_async(
        self,
        tmp_req: main_models.RemoveAgentFromSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveAgentFromSkillGroupResponse:
        tmp_req.validate()
        request = main_models.RemoveAgentFromSkillGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_ids):
            request.agent_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_ids_shrink):
            query['AgentIds'] = request.agent_ids_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveAgentFromSkillGroup',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveAgentFromSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_agent_from_skill_group(
        self,
        request: main_models.RemoveAgentFromSkillGroupRequest,
    ) -> main_models.RemoveAgentFromSkillGroupResponse:
        runtime = RuntimeOptions()
        return self.remove_agent_from_skill_group_with_options(request, runtime)

    async def remove_agent_from_skill_group_async(
        self,
        request: main_models.RemoveAgentFromSkillGroupRequest,
    ) -> main_models.RemoveAgentFromSkillGroupResponse:
        runtime = RuntimeOptions()
        return await self.remove_agent_from_skill_group_with_options_async(request, runtime)

    def remove_skill_group_with_options(
        self,
        request: main_models.RemoveSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveSkillGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id):
            body['SkillGroupId'] = request.skill_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveSkillGroup',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_skill_group_with_options_async(
        self,
        request: main_models.RemoveSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveSkillGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id):
            body['SkillGroupId'] = request.skill_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveSkillGroup',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_skill_group(
        self,
        request: main_models.RemoveSkillGroupRequest,
    ) -> main_models.RemoveSkillGroupResponse:
        runtime = RuntimeOptions()
        return self.remove_skill_group_with_options(request, runtime)

    async def remove_skill_group_async(
        self,
        request: main_models.RemoveSkillGroupRequest,
    ) -> main_models.RemoveSkillGroupResponse:
        runtime = RuntimeOptions()
        return await self.remove_skill_group_with_options_async(request, runtime)

    def reset_hotline_number_with_options(
        self,
        tmp_req: main_models.ResetHotlineNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetHotlineNumberResponse:
        tmp_req.validate()
        request = main_models.ResetHotlineNumberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.outbound_range_list):
            request.outbound_range_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.outbound_range_list, 'OutboundRangeList', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.enable_inbound):
            body['EnableInbound'] = request.enable_inbound
        if not DaraCore.is_null(request.enable_inbound_evaluation):
            body['EnableInboundEvaluation'] = request.enable_inbound_evaluation
        if not DaraCore.is_null(request.enable_outbound):
            body['EnableOutbound'] = request.enable_outbound
        if not DaraCore.is_null(request.enable_outbound_evaluation):
            body['EnableOutboundEvaluation'] = request.enable_outbound_evaluation
        if not DaraCore.is_null(request.evaluation_level):
            body['EvaluationLevel'] = request.evaluation_level
        if not DaraCore.is_null(request.hotline_number):
            body['HotlineNumber'] = request.hotline_number
        if not DaraCore.is_null(request.inbound_flow_id):
            body['InboundFlowId'] = request.inbound_flow_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.outbound_all_depart):
            body['OutboundAllDepart'] = request.outbound_all_depart
        if not DaraCore.is_null(request.outbound_range_list_shrink):
            body['OutboundRangeList'] = request.outbound_range_list_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetHotlineNumber',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetHotlineNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_hotline_number_with_options_async(
        self,
        tmp_req: main_models.ResetHotlineNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetHotlineNumberResponse:
        tmp_req.validate()
        request = main_models.ResetHotlineNumberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.outbound_range_list):
            request.outbound_range_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.outbound_range_list, 'OutboundRangeList', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.enable_inbound):
            body['EnableInbound'] = request.enable_inbound
        if not DaraCore.is_null(request.enable_inbound_evaluation):
            body['EnableInboundEvaluation'] = request.enable_inbound_evaluation
        if not DaraCore.is_null(request.enable_outbound):
            body['EnableOutbound'] = request.enable_outbound
        if not DaraCore.is_null(request.enable_outbound_evaluation):
            body['EnableOutboundEvaluation'] = request.enable_outbound_evaluation
        if not DaraCore.is_null(request.evaluation_level):
            body['EvaluationLevel'] = request.evaluation_level
        if not DaraCore.is_null(request.hotline_number):
            body['HotlineNumber'] = request.hotline_number
        if not DaraCore.is_null(request.inbound_flow_id):
            body['InboundFlowId'] = request.inbound_flow_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.outbound_all_depart):
            body['OutboundAllDepart'] = request.outbound_all_depart
        if not DaraCore.is_null(request.outbound_range_list_shrink):
            body['OutboundRangeList'] = request.outbound_range_list_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetHotlineNumber',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetHotlineNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_hotline_number(
        self,
        request: main_models.ResetHotlineNumberRequest,
    ) -> main_models.ResetHotlineNumberResponse:
        runtime = RuntimeOptions()
        return self.reset_hotline_number_with_options(request, runtime)

    async def reset_hotline_number_async(
        self,
        request: main_models.ResetHotlineNumberRequest,
    ) -> main_models.ResetHotlineNumberResponse:
        runtime = RuntimeOptions()
        return await self.reset_hotline_number_with_options_async(request, runtime)

    def restart_outbound_task_with_options(
        self,
        request: main_models.RestartOutboundTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartOutboundTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.outbound_task_id):
            query['OutboundTaskId'] = request.outbound_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartOutboundTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartOutboundTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_outbound_task_with_options_async(
        self,
        request: main_models.RestartOutboundTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartOutboundTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.outbound_task_id):
            query['OutboundTaskId'] = request.outbound_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartOutboundTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartOutboundTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_outbound_task(
        self,
        request: main_models.RestartOutboundTaskRequest,
    ) -> main_models.RestartOutboundTaskResponse:
        runtime = RuntimeOptions()
        return self.restart_outbound_task_with_options(request, runtime)

    async def restart_outbound_task_async(
        self,
        request: main_models.RestartOutboundTaskRequest,
    ) -> main_models.RestartOutboundTaskResponse:
        runtime = RuntimeOptions()
        return await self.restart_outbound_task_with_options_async(request, runtime)

    def robot_call_with_options(
        self,
        request: main_models.RobotCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RobotCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not DaraCore.is_null(request.early_media_asr):
            query['EarlyMediaAsr'] = request.early_media_asr
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.record_flag):
            query['RecordFlag'] = request.record_flag
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.robot_id):
            query['RobotId'] = request.robot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RobotCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RobotCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def robot_call_with_options_async(
        self,
        request: main_models.RobotCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RobotCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not DaraCore.is_null(request.early_media_asr):
            query['EarlyMediaAsr'] = request.early_media_asr
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.record_flag):
            query['RecordFlag'] = request.record_flag
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.robot_id):
            query['RobotId'] = request.robot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RobotCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RobotCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def robot_call(
        self,
        request: main_models.RobotCallRequest,
    ) -> main_models.RobotCallResponse:
        runtime = RuntimeOptions()
        return self.robot_call_with_options(request, runtime)

    async def robot_call_async(
        self,
        request: main_models.RobotCallRequest,
    ) -> main_models.RobotCallResponse:
        runtime = RuntimeOptions()
        return await self.robot_call_with_options_async(request, runtime)

    def send_cco_smart_call_with_options(
        self,
        request: main_models.SendCcoSmartCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendCcoSmartCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_code_break):
            query['ActionCodeBreak'] = request.action_code_break
        if not DaraCore.is_null(request.action_code_time_break):
            query['ActionCodeTimeBreak'] = request.action_code_time_break
        if not DaraCore.is_null(request.asr_als_am_id):
            query['AsrAlsAmId'] = request.asr_als_am_id
        if not DaraCore.is_null(request.asr_base_id):
            query['AsrBaseId'] = request.asr_base_id
        if not DaraCore.is_null(request.asr_model_id):
            query['AsrModelId'] = request.asr_model_id
        if not DaraCore.is_null(request.asr_vocabulary_id):
            query['AsrVocabularyId'] = request.asr_vocabulary_id
        if not DaraCore.is_null(request.background_file_code):
            query['BackgroundFileCode'] = request.background_file_code
        if not DaraCore.is_null(request.background_speed):
            query['BackgroundSpeed'] = request.background_speed
        if not DaraCore.is_null(request.background_volume):
            query['BackgroundVolume'] = request.background_volume
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not DaraCore.is_null(request.dynamic_id):
            query['DynamicId'] = request.dynamic_id
        if not DaraCore.is_null(request.early_media_asr):
            query['EarlyMediaAsr'] = request.early_media_asr
        if not DaraCore.is_null(request.enable_itn):
            query['EnableITN'] = request.enable_itn
        if not DaraCore.is_null(request.mute_time):
            query['MuteTime'] = request.mute_time
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pause_time):
            query['PauseTime'] = request.pause_time
        if not DaraCore.is_null(request.play_times):
            query['PlayTimes'] = request.play_times
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.record_flag):
            query['RecordFlag'] = request.record_flag
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.session_timeout):
            query['SessionTimeout'] = request.session_timeout
        if not DaraCore.is_null(request.speed):
            query['Speed'] = request.speed
        if not DaraCore.is_null(request.tts_conf):
            query['TtsConf'] = request.tts_conf
        if not DaraCore.is_null(request.tts_speed):
            query['TtsSpeed'] = request.tts_speed
        if not DaraCore.is_null(request.tts_style):
            query['TtsStyle'] = request.tts_style
        if not DaraCore.is_null(request.tts_volume):
            query['TtsVolume'] = request.tts_volume
        if not DaraCore.is_null(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not DaraCore.is_null(request.voice_code_param):
            query['VoiceCodeParam'] = request.voice_code_param
        if not DaraCore.is_null(request.volume):
            query['Volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendCcoSmartCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendCcoSmartCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_cco_smart_call_with_options_async(
        self,
        request: main_models.SendCcoSmartCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendCcoSmartCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_code_break):
            query['ActionCodeBreak'] = request.action_code_break
        if not DaraCore.is_null(request.action_code_time_break):
            query['ActionCodeTimeBreak'] = request.action_code_time_break
        if not DaraCore.is_null(request.asr_als_am_id):
            query['AsrAlsAmId'] = request.asr_als_am_id
        if not DaraCore.is_null(request.asr_base_id):
            query['AsrBaseId'] = request.asr_base_id
        if not DaraCore.is_null(request.asr_model_id):
            query['AsrModelId'] = request.asr_model_id
        if not DaraCore.is_null(request.asr_vocabulary_id):
            query['AsrVocabularyId'] = request.asr_vocabulary_id
        if not DaraCore.is_null(request.background_file_code):
            query['BackgroundFileCode'] = request.background_file_code
        if not DaraCore.is_null(request.background_speed):
            query['BackgroundSpeed'] = request.background_speed
        if not DaraCore.is_null(request.background_volume):
            query['BackgroundVolume'] = request.background_volume
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not DaraCore.is_null(request.dynamic_id):
            query['DynamicId'] = request.dynamic_id
        if not DaraCore.is_null(request.early_media_asr):
            query['EarlyMediaAsr'] = request.early_media_asr
        if not DaraCore.is_null(request.enable_itn):
            query['EnableITN'] = request.enable_itn
        if not DaraCore.is_null(request.mute_time):
            query['MuteTime'] = request.mute_time
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pause_time):
            query['PauseTime'] = request.pause_time
        if not DaraCore.is_null(request.play_times):
            query['PlayTimes'] = request.play_times
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.record_flag):
            query['RecordFlag'] = request.record_flag
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.session_timeout):
            query['SessionTimeout'] = request.session_timeout
        if not DaraCore.is_null(request.speed):
            query['Speed'] = request.speed
        if not DaraCore.is_null(request.tts_conf):
            query['TtsConf'] = request.tts_conf
        if not DaraCore.is_null(request.tts_speed):
            query['TtsSpeed'] = request.tts_speed
        if not DaraCore.is_null(request.tts_style):
            query['TtsStyle'] = request.tts_style
        if not DaraCore.is_null(request.tts_volume):
            query['TtsVolume'] = request.tts_volume
        if not DaraCore.is_null(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not DaraCore.is_null(request.voice_code_param):
            query['VoiceCodeParam'] = request.voice_code_param
        if not DaraCore.is_null(request.volume):
            query['Volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendCcoSmartCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendCcoSmartCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_cco_smart_call(
        self,
        request: main_models.SendCcoSmartCallRequest,
    ) -> main_models.SendCcoSmartCallResponse:
        runtime = RuntimeOptions()
        return self.send_cco_smart_call_with_options(request, runtime)

    async def send_cco_smart_call_async(
        self,
        request: main_models.SendCcoSmartCallRequest,
    ) -> main_models.SendCcoSmartCallResponse:
        runtime = RuntimeOptions()
        return await self.send_cco_smart_call_with_options_async(request, runtime)

    def send_cco_smart_call_operate_with_options(
        self,
        request: main_models.SendCcoSmartCallOperateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendCcoSmartCallOperateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.command):
            query['Command'] = request.command
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.param):
            query['Param'] = request.param
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendCcoSmartCallOperate',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendCcoSmartCallOperateResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_cco_smart_call_operate_with_options_async(
        self,
        request: main_models.SendCcoSmartCallOperateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendCcoSmartCallOperateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.command):
            query['Command'] = request.command
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.param):
            query['Param'] = request.param
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendCcoSmartCallOperate',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendCcoSmartCallOperateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_cco_smart_call_operate(
        self,
        request: main_models.SendCcoSmartCallOperateRequest,
    ) -> main_models.SendCcoSmartCallOperateResponse:
        runtime = RuntimeOptions()
        return self.send_cco_smart_call_operate_with_options(request, runtime)

    async def send_cco_smart_call_operate_async(
        self,
        request: main_models.SendCcoSmartCallOperateRequest,
    ) -> main_models.SendCcoSmartCallOperateResponse:
        runtime = RuntimeOptions()
        return await self.send_cco_smart_call_operate_with_options_async(request, runtime)

    def send_hotline_heart_beat_with_options(
        self,
        request: main_models.SendHotlineHeartBeatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendHotlineHeartBeatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.token):
            body['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendHotlineHeartBeat',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendHotlineHeartBeatResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_hotline_heart_beat_with_options_async(
        self,
        request: main_models.SendHotlineHeartBeatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendHotlineHeartBeatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.token):
            body['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendHotlineHeartBeat',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendHotlineHeartBeatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_hotline_heart_beat(
        self,
        request: main_models.SendHotlineHeartBeatRequest,
    ) -> main_models.SendHotlineHeartBeatResponse:
        runtime = RuntimeOptions()
        return self.send_hotline_heart_beat_with_options(request, runtime)

    async def send_hotline_heart_beat_async(
        self,
        request: main_models.SendHotlineHeartBeatRequest,
    ) -> main_models.SendHotlineHeartBeatResponse:
        runtime = RuntimeOptions()
        return await self.send_hotline_heart_beat_with_options_async(request, runtime)

    def start_ai_call_task_with_options(
        self,
        request: main_models.StartAiCallTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartAiCallTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartAiCallTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAiCallTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_ai_call_task_with_options_async(
        self,
        request: main_models.StartAiCallTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartAiCallTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartAiCallTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAiCallTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_ai_call_task(
        self,
        request: main_models.StartAiCallTaskRequest,
    ) -> main_models.StartAiCallTaskResponse:
        runtime = RuntimeOptions()
        return self.start_ai_call_task_with_options(request, runtime)

    async def start_ai_call_task_async(
        self,
        request: main_models.StartAiCallTaskRequest,
    ) -> main_models.StartAiCallTaskResponse:
        runtime = RuntimeOptions()
        return await self.start_ai_call_task_with_options_async(request, runtime)

    def start_ai_outbound_task_with_options(
        self,
        request: main_models.StartAiOutboundTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartAiOutboundTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartAiOutboundTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAiOutboundTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_ai_outbound_task_with_options_async(
        self,
        request: main_models.StartAiOutboundTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartAiOutboundTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartAiOutboundTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAiOutboundTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_ai_outbound_task(
        self,
        request: main_models.StartAiOutboundTaskRequest,
    ) -> main_models.StartAiOutboundTaskResponse:
        runtime = RuntimeOptions()
        return self.start_ai_outbound_task_with_options(request, runtime)

    async def start_ai_outbound_task_async(
        self,
        request: main_models.StartAiOutboundTaskRequest,
    ) -> main_models.StartAiOutboundTaskResponse:
        runtime = RuntimeOptions()
        return await self.start_ai_outbound_task_with_options_async(request, runtime)

    def start_call_with_options(
        self,
        request: main_models.StartCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartCallResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.callee):
            body['Callee'] = request.callee
        if not DaraCore.is_null(request.caller):
            body['Caller'] = request.caller
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_call_with_options_async(
        self,
        request: main_models.StartCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartCallResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.callee):
            body['Callee'] = request.callee
        if not DaraCore.is_null(request.caller):
            body['Caller'] = request.caller
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartCall',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_call(
        self,
        request: main_models.StartCallRequest,
    ) -> main_models.StartCallResponse:
        runtime = RuntimeOptions()
        return self.start_call_with_options(request, runtime)

    async def start_call_async(
        self,
        request: main_models.StartCallRequest,
    ) -> main_models.StartCallResponse:
        runtime = RuntimeOptions()
        return await self.start_call_with_options_async(request, runtime)

    def start_call_v2with_options(
        self,
        request: main_models.StartCallV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.StartCallV2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.callee):
            body['Callee'] = request.callee
        if not DaraCore.is_null(request.caller):
            body['Caller'] = request.caller
        if not DaraCore.is_null(request.caller_type):
            body['CallerType'] = request.caller_type
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartCallV2',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartCallV2Response(),
            self.call_api(params, req, runtime)
        )

    async def start_call_v2with_options_async(
        self,
        request: main_models.StartCallV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.StartCallV2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.callee):
            body['Callee'] = request.callee
        if not DaraCore.is_null(request.caller):
            body['Caller'] = request.caller
        if not DaraCore.is_null(request.caller_type):
            body['CallerType'] = request.caller_type
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartCallV2',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartCallV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def start_call_v2(
        self,
        request: main_models.StartCallV2Request,
    ) -> main_models.StartCallV2Response:
        runtime = RuntimeOptions()
        return self.start_call_v2with_options(request, runtime)

    async def start_call_v2_async(
        self,
        request: main_models.StartCallV2Request,
    ) -> main_models.StartCallV2Response:
        runtime = RuntimeOptions()
        return await self.start_call_v2with_options_async(request, runtime)

    def start_chat_work_with_options(
        self,
        request: main_models.StartChatWorkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartChatWorkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartChatWork',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartChatWorkResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_chat_work_with_options_async(
        self,
        request: main_models.StartChatWorkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartChatWorkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartChatWork',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartChatWorkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_chat_work(
        self,
        request: main_models.StartChatWorkRequest,
    ) -> main_models.StartChatWorkResponse:
        runtime = RuntimeOptions()
        return self.start_chat_work_with_options(request, runtime)

    async def start_chat_work_async(
        self,
        request: main_models.StartChatWorkRequest,
    ) -> main_models.StartChatWorkResponse:
        runtime = RuntimeOptions()
        return await self.start_chat_work_with_options_async(request, runtime)

    def start_hotline_service_with_options(
        self,
        request: main_models.StartHotlineServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartHotlineServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartHotlineService',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartHotlineServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_hotline_service_with_options_async(
        self,
        request: main_models.StartHotlineServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartHotlineServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartHotlineService',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartHotlineServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_hotline_service(
        self,
        request: main_models.StartHotlineServiceRequest,
    ) -> main_models.StartHotlineServiceResponse:
        runtime = RuntimeOptions()
        return self.start_hotline_service_with_options(request, runtime)

    async def start_hotline_service_async(
        self,
        request: main_models.StartHotlineServiceRequest,
    ) -> main_models.StartHotlineServiceResponse:
        runtime = RuntimeOptions()
        return await self.start_hotline_service_with_options_async(request, runtime)

    def start_micro_outbound_with_options(
        self,
        request: main_models.StartMicroOutboundRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartMicroOutboundResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.command_code):
            query['CommandCode'] = request.command_code
        if not DaraCore.is_null(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartMicroOutbound',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartMicroOutboundResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_micro_outbound_with_options_async(
        self,
        request: main_models.StartMicroOutboundRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartMicroOutboundResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.command_code):
            query['CommandCode'] = request.command_code
        if not DaraCore.is_null(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartMicroOutbound',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartMicroOutboundResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_micro_outbound(
        self,
        request: main_models.StartMicroOutboundRequest,
    ) -> main_models.StartMicroOutboundResponse:
        runtime = RuntimeOptions()
        return self.start_micro_outbound_with_options(request, runtime)

    async def start_micro_outbound_async(
        self,
        request: main_models.StartMicroOutboundRequest,
    ) -> main_models.StartMicroOutboundResponse:
        runtime = RuntimeOptions()
        return await self.start_micro_outbound_with_options_async(request, runtime)

    def start_task_with_options(
        self,
        request: main_models.StartTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_now):
            query['StartNow'] = request.start_now
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_task_with_options_async(
        self,
        request: main_models.StartTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_now):
            query['StartNow'] = request.start_now
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_task(
        self,
        request: main_models.StartTaskRequest,
    ) -> main_models.StartTaskResponse:
        runtime = RuntimeOptions()
        return self.start_task_with_options(request, runtime)

    async def start_task_async(
        self,
        request: main_models.StartTaskRequest,
    ) -> main_models.StartTaskResponse:
        runtime = RuntimeOptions()
        return await self.start_task_with_options_async(request, runtime)

    def stop_ai_call_task_with_options(
        self,
        request: main_models.StopAiCallTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopAiCallTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopAiCallTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopAiCallTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_ai_call_task_with_options_async(
        self,
        request: main_models.StopAiCallTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopAiCallTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopAiCallTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopAiCallTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_ai_call_task(
        self,
        request: main_models.StopAiCallTaskRequest,
    ) -> main_models.StopAiCallTaskResponse:
        runtime = RuntimeOptions()
        return self.stop_ai_call_task_with_options(request, runtime)

    async def stop_ai_call_task_async(
        self,
        request: main_models.StopAiCallTaskRequest,
    ) -> main_models.StopAiCallTaskResponse:
        runtime = RuntimeOptions()
        return await self.stop_ai_call_task_with_options_async(request, runtime)

    def stop_ai_outbound_task_with_options(
        self,
        request: main_models.StopAiOutboundTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopAiOutboundTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopAiOutboundTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopAiOutboundTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_ai_outbound_task_with_options_async(
        self,
        request: main_models.StopAiOutboundTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopAiOutboundTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopAiOutboundTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopAiOutboundTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_ai_outbound_task(
        self,
        request: main_models.StopAiOutboundTaskRequest,
    ) -> main_models.StopAiOutboundTaskResponse:
        runtime = RuntimeOptions()
        return self.stop_ai_outbound_task_with_options(request, runtime)

    async def stop_ai_outbound_task_async(
        self,
        request: main_models.StopAiOutboundTaskRequest,
    ) -> main_models.StopAiOutboundTaskResponse:
        runtime = RuntimeOptions()
        return await self.stop_ai_outbound_task_with_options_async(request, runtime)

    def stop_task_with_options(
        self,
        request: main_models.StopTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_task_with_options_async(
        self,
        request: main_models.StopTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_task(
        self,
        request: main_models.StopTaskRequest,
    ) -> main_models.StopTaskResponse:
        runtime = RuntimeOptions()
        return self.stop_task_with_options(request, runtime)

    async def stop_task_async(
        self,
        request: main_models.StopTaskRequest,
    ) -> main_models.StopTaskResponse:
        runtime = RuntimeOptions()
        return await self.stop_task_with_options_async(request, runtime)

    def suspend_hotline_service_with_options(
        self,
        request: main_models.SuspendHotlineServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendHotlineServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SuspendHotlineService',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendHotlineServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_hotline_service_with_options_async(
        self,
        request: main_models.SuspendHotlineServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendHotlineServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SuspendHotlineService',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendHotlineServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_hotline_service(
        self,
        request: main_models.SuspendHotlineServiceRequest,
    ) -> main_models.SuspendHotlineServiceResponse:
        runtime = RuntimeOptions()
        return self.suspend_hotline_service_with_options(request, runtime)

    async def suspend_hotline_service_async(
        self,
        request: main_models.SuspendHotlineServiceRequest,
    ) -> main_models.SuspendHotlineServiceResponse:
        runtime = RuntimeOptions()
        return await self.suspend_hotline_service_with_options_async(request, runtime)

    def suspend_outbound_task_with_options(
        self,
        request: main_models.SuspendOutboundTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendOutboundTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.outbound_task_id):
            query['OutboundTaskId'] = request.outbound_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuspendOutboundTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendOutboundTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_outbound_task_with_options_async(
        self,
        request: main_models.SuspendOutboundTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendOutboundTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.outbound_task_id):
            query['OutboundTaskId'] = request.outbound_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuspendOutboundTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendOutboundTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_outbound_task(
        self,
        request: main_models.SuspendOutboundTaskRequest,
    ) -> main_models.SuspendOutboundTaskResponse:
        runtime = RuntimeOptions()
        return self.suspend_outbound_task_with_options(request, runtime)

    async def suspend_outbound_task_async(
        self,
        request: main_models.SuspendOutboundTaskRequest,
    ) -> main_models.SuspendOutboundTaskResponse:
        runtime = RuntimeOptions()
        return await self.suspend_outbound_task_with_options_async(request, runtime)

    def terminate_ai_outbound_task_with_options(
        self,
        request: main_models.TerminateAiOutboundTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TerminateAiOutboundTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TerminateAiOutboundTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TerminateAiOutboundTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def terminate_ai_outbound_task_with_options_async(
        self,
        request: main_models.TerminateAiOutboundTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TerminateAiOutboundTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TerminateAiOutboundTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TerminateAiOutboundTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def terminate_ai_outbound_task(
        self,
        request: main_models.TerminateAiOutboundTaskRequest,
    ) -> main_models.TerminateAiOutboundTaskResponse:
        runtime = RuntimeOptions()
        return self.terminate_ai_outbound_task_with_options(request, runtime)

    async def terminate_ai_outbound_task_async(
        self,
        request: main_models.TerminateAiOutboundTaskRequest,
    ) -> main_models.TerminateAiOutboundTaskResponse:
        runtime = RuntimeOptions()
        return await self.terminate_ai_outbound_task_with_options_async(request, runtime)

    def transfer_call_to_skill_group_with_options(
        self,
        request: main_models.TransferCallToSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferCallToSkillGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.call_id):
            body['CallId'] = request.call_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not DaraCore.is_null(request.hold_connection_id):
            body['HoldConnectionId'] = request.hold_connection_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_single_transfer):
            body['IsSingleTransfer'] = request.is_single_transfer
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.skill_group_id):
            body['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TransferCallToSkillGroup',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferCallToSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_call_to_skill_group_with_options_async(
        self,
        request: main_models.TransferCallToSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferCallToSkillGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.call_id):
            body['CallId'] = request.call_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not DaraCore.is_null(request.hold_connection_id):
            body['HoldConnectionId'] = request.hold_connection_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_single_transfer):
            body['IsSingleTransfer'] = request.is_single_transfer
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.skill_group_id):
            body['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TransferCallToSkillGroup',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferCallToSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_call_to_skill_group(
        self,
        request: main_models.TransferCallToSkillGroupRequest,
    ) -> main_models.TransferCallToSkillGroupResponse:
        runtime = RuntimeOptions()
        return self.transfer_call_to_skill_group_with_options(request, runtime)

    async def transfer_call_to_skill_group_async(
        self,
        request: main_models.TransferCallToSkillGroupRequest,
    ) -> main_models.TransferCallToSkillGroupResponse:
        runtime = RuntimeOptions()
        return await self.transfer_call_to_skill_group_with_options_async(request, runtime)

    def update_agent_with_options(
        self,
        request: main_models.UpdateAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id):
            body['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.skill_group_id_list):
            body['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgent',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'PUT',
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
        request: main_models.UpdateAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id):
            body['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.skill_group_id_list):
            body['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgent',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'PUT',
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

    def update_ai_call_task_with_options(
        self,
        tmp_req: main_models.UpdateAiCallTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAiCallTaskResponse:
        tmp_req.validate()
        request = main_models.UpdateAiCallTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.call_day):
            request.call_day_shrink = Utils.array_to_string_with_specified_style(tmp_req.call_day, 'CallDay', 'json')
        if not DaraCore.is_null(tmp_req.call_retry_reason):
            request.call_retry_reason_shrink = Utils.array_to_string_with_specified_style(tmp_req.call_retry_reason, 'CallRetryReason', 'json')
        if not DaraCore.is_null(tmp_req.call_time):
            request.call_time_shrink = Utils.array_to_string_with_specified_style(tmp_req.call_time, 'CallTime', 'json')
        query = {}
        if not DaraCore.is_null(request.call_day_shrink):
            query['CallDay'] = request.call_day_shrink
        if not DaraCore.is_null(request.call_retry_interval):
            query['CallRetryInterval'] = request.call_retry_interval
        if not DaraCore.is_null(request.call_retry_reason_shrink):
            query['CallRetryReason'] = request.call_retry_reason_shrink
        if not DaraCore.is_null(request.call_retry_times):
            query['CallRetryTimes'] = request.call_retry_times
        if not DaraCore.is_null(request.call_time_shrink):
            query['CallTime'] = request.call_time_shrink
        if not DaraCore.is_null(request.miss_call_retry):
            query['MissCallRetry'] = request.miss_call_retry
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_type):
            query['StartType'] = request.start_type
        if not DaraCore.is_null(request.task_cps):
            query['TaskCps'] = request.task_cps
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_start_time):
            query['TaskStartTime'] = request.task_start_time
        if not DaraCore.is_null(request.virtual_number):
            query['VirtualNumber'] = request.virtual_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAiCallTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAiCallTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ai_call_task_with_options_async(
        self,
        tmp_req: main_models.UpdateAiCallTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAiCallTaskResponse:
        tmp_req.validate()
        request = main_models.UpdateAiCallTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.call_day):
            request.call_day_shrink = Utils.array_to_string_with_specified_style(tmp_req.call_day, 'CallDay', 'json')
        if not DaraCore.is_null(tmp_req.call_retry_reason):
            request.call_retry_reason_shrink = Utils.array_to_string_with_specified_style(tmp_req.call_retry_reason, 'CallRetryReason', 'json')
        if not DaraCore.is_null(tmp_req.call_time):
            request.call_time_shrink = Utils.array_to_string_with_specified_style(tmp_req.call_time, 'CallTime', 'json')
        query = {}
        if not DaraCore.is_null(request.call_day_shrink):
            query['CallDay'] = request.call_day_shrink
        if not DaraCore.is_null(request.call_retry_interval):
            query['CallRetryInterval'] = request.call_retry_interval
        if not DaraCore.is_null(request.call_retry_reason_shrink):
            query['CallRetryReason'] = request.call_retry_reason_shrink
        if not DaraCore.is_null(request.call_retry_times):
            query['CallRetryTimes'] = request.call_retry_times
        if not DaraCore.is_null(request.call_time_shrink):
            query['CallTime'] = request.call_time_shrink
        if not DaraCore.is_null(request.miss_call_retry):
            query['MissCallRetry'] = request.miss_call_retry
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_type):
            query['StartType'] = request.start_type
        if not DaraCore.is_null(request.task_cps):
            query['TaskCps'] = request.task_cps
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_start_time):
            query['TaskStartTime'] = request.task_start_time
        if not DaraCore.is_null(request.virtual_number):
            query['VirtualNumber'] = request.virtual_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAiCallTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAiCallTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ai_call_task(
        self,
        request: main_models.UpdateAiCallTaskRequest,
    ) -> main_models.UpdateAiCallTaskResponse:
        runtime = RuntimeOptions()
        return self.update_ai_call_task_with_options(request, runtime)

    async def update_ai_call_task_async(
        self,
        request: main_models.UpdateAiCallTaskRequest,
    ) -> main_models.UpdateAiCallTaskResponse:
        runtime = RuntimeOptions()
        return await self.update_ai_call_task_with_options_async(request, runtime)

    def update_ai_outbound_task_with_options(
        self,
        tmp_req: main_models.UpdateAiOutboundTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAiOutboundTaskResponse:
        tmp_req.validate()
        request = main_models.UpdateAiOutboundTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.outbound_nums):
            request.outbound_nums_shrink = Utils.array_to_string_with_specified_style(tmp_req.outbound_nums, 'OutboundNums', 'json')
        if not DaraCore.is_null(tmp_req.recall_rule):
            request.recall_rule_shrink = Utils.array_to_string_with_specified_style(tmp_req.recall_rule, 'RecallRule', 'json')
        query = {}
        if not DaraCore.is_null(request.concurrent_rate):
            query['ConcurrentRate'] = request.concurrent_rate
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.execution_time):
            query['ExecutionTime'] = request.execution_time
        if not DaraCore.is_null(request.forecast_call_rate):
            query['ForecastCallRate'] = request.forecast_call_rate
        if not DaraCore.is_null(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.num_repeated):
            query['NumRepeated'] = request.num_repeated
        if not DaraCore.is_null(request.outbound_nums_shrink):
            query['OutboundNums'] = request.outbound_nums_shrink
        if not DaraCore.is_null(request.recall_rule_shrink):
            query['RecallRule'] = request.recall_rule_shrink
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAiOutboundTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAiOutboundTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ai_outbound_task_with_options_async(
        self,
        tmp_req: main_models.UpdateAiOutboundTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAiOutboundTaskResponse:
        tmp_req.validate()
        request = main_models.UpdateAiOutboundTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.outbound_nums):
            request.outbound_nums_shrink = Utils.array_to_string_with_specified_style(tmp_req.outbound_nums, 'OutboundNums', 'json')
        if not DaraCore.is_null(tmp_req.recall_rule):
            request.recall_rule_shrink = Utils.array_to_string_with_specified_style(tmp_req.recall_rule, 'RecallRule', 'json')
        query = {}
        if not DaraCore.is_null(request.concurrent_rate):
            query['ConcurrentRate'] = request.concurrent_rate
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.execution_time):
            query['ExecutionTime'] = request.execution_time
        if not DaraCore.is_null(request.forecast_call_rate):
            query['ForecastCallRate'] = request.forecast_call_rate
        if not DaraCore.is_null(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.num_repeated):
            query['NumRepeated'] = request.num_repeated
        if not DaraCore.is_null(request.outbound_nums_shrink):
            query['OutboundNums'] = request.outbound_nums_shrink
        if not DaraCore.is_null(request.recall_rule_shrink):
            query['RecallRule'] = request.recall_rule_shrink
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAiOutboundTask',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAiOutboundTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ai_outbound_task(
        self,
        request: main_models.UpdateAiOutboundTaskRequest,
    ) -> main_models.UpdateAiOutboundTaskResponse:
        runtime = RuntimeOptions()
        return self.update_ai_outbound_task_with_options(request, runtime)

    async def update_ai_outbound_task_async(
        self,
        request: main_models.UpdateAiOutboundTaskRequest,
    ) -> main_models.UpdateAiOutboundTaskResponse:
        runtime = RuntimeOptions()
        return await self.update_ai_outbound_task_with_options_async(request, runtime)

    def update_department_with_options(
        self,
        request: main_models.UpdateDepartmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDepartmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.department_id):
            query['DepartmentId'] = request.department_id
        if not DaraCore.is_null(request.department_name):
            query['DepartmentName'] = request.department_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDepartment',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDepartmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_department_with_options_async(
        self,
        request: main_models.UpdateDepartmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDepartmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.department_id):
            query['DepartmentId'] = request.department_id
        if not DaraCore.is_null(request.department_name):
            query['DepartmentName'] = request.department_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDepartment',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDepartmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_department(
        self,
        request: main_models.UpdateDepartmentRequest,
    ) -> main_models.UpdateDepartmentResponse:
        runtime = RuntimeOptions()
        return self.update_department_with_options(request, runtime)

    async def update_department_async(
        self,
        request: main_models.UpdateDepartmentRequest,
    ) -> main_models.UpdateDepartmentResponse:
        runtime = RuntimeOptions()
        return await self.update_department_with_options_async(request, runtime)

    def update_outer_account_with_options(
        self,
        request: main_models.UpdateOuterAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOuterAccountResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOuterAccount',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOuterAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_outer_account_with_options_async(
        self,
        request: main_models.UpdateOuterAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOuterAccountResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOuterAccount',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOuterAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_outer_account(
        self,
        request: main_models.UpdateOuterAccountRequest,
    ) -> main_models.UpdateOuterAccountResponse:
        runtime = RuntimeOptions()
        return self.update_outer_account_with_options(request, runtime)

    async def update_outer_account_async(
        self,
        request: main_models.UpdateOuterAccountRequest,
    ) -> main_models.UpdateOuterAccountResponse:
        runtime = RuntimeOptions()
        return await self.update_outer_account_with_options_async(request, runtime)

    def update_skill_group_with_options(
        self,
        request: main_models.UpdateSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.skill_group_name):
            query['SkillGroupName'] = request.skill_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSkillGroup',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_skill_group_with_options_async(
        self,
        request: main_models.UpdateSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.skill_group_name):
            query['SkillGroupName'] = request.skill_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSkillGroup',
            version = '2019-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_skill_group(
        self,
        request: main_models.UpdateSkillGroupRequest,
    ) -> main_models.UpdateSkillGroupResponse:
        runtime = RuntimeOptions()
        return self.update_skill_group_with_options(request, runtime)

    async def update_skill_group_async(
        self,
        request: main_models.UpdateSkillGroupRequest,
    ) -> main_models.UpdateSkillGroupResponse:
        runtime = RuntimeOptions()
        return await self.update_skill_group_with_options_async(request, runtime)
