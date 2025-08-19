# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aiccs20191015 import models as aiccs_20191015_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_hotline_number_with_options(
        self,
        tmp_req: aiccs_20191015_models.AddHotlineNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.AddHotlineNumberResponse:
        """
        @summary 新增热线号码
        
        @param tmp_req: AddHotlineNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddHotlineNumberResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.AddHotlineNumberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.outbound_range_list):
            request.outbound_range_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.outbound_range_list, 'OutboundRangeList', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.enable_inbound):
            body['EnableInbound'] = request.enable_inbound
        if not UtilClient.is_unset(request.enable_inbound_evaluation):
            body['EnableInboundEvaluation'] = request.enable_inbound_evaluation
        if not UtilClient.is_unset(request.enable_outbound):
            body['EnableOutbound'] = request.enable_outbound
        if not UtilClient.is_unset(request.enable_outbound_evaluation):
            body['EnableOutboundEvaluation'] = request.enable_outbound_evaluation
        if not UtilClient.is_unset(request.evaluation_level):
            body['EvaluationLevel'] = request.evaluation_level
        if not UtilClient.is_unset(request.hotline_number):
            body['HotlineNumber'] = request.hotline_number
        if not UtilClient.is_unset(request.inbound_flow_id):
            body['InboundFlowId'] = request.inbound_flow_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.outbound_all_depart):
            body['OutboundAllDepart'] = request.outbound_all_depart
        if not UtilClient.is_unset(request.outbound_range_list_shrink):
            body['OutboundRangeList'] = request.outbound_range_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddHotlineNumber',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.AddHotlineNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_hotline_number_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.AddHotlineNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.AddHotlineNumberResponse:
        """
        @summary 新增热线号码
        
        @param tmp_req: AddHotlineNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddHotlineNumberResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.AddHotlineNumberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.outbound_range_list):
            request.outbound_range_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.outbound_range_list, 'OutboundRangeList', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.enable_inbound):
            body['EnableInbound'] = request.enable_inbound
        if not UtilClient.is_unset(request.enable_inbound_evaluation):
            body['EnableInboundEvaluation'] = request.enable_inbound_evaluation
        if not UtilClient.is_unset(request.enable_outbound):
            body['EnableOutbound'] = request.enable_outbound
        if not UtilClient.is_unset(request.enable_outbound_evaluation):
            body['EnableOutboundEvaluation'] = request.enable_outbound_evaluation
        if not UtilClient.is_unset(request.evaluation_level):
            body['EvaluationLevel'] = request.evaluation_level
        if not UtilClient.is_unset(request.hotline_number):
            body['HotlineNumber'] = request.hotline_number
        if not UtilClient.is_unset(request.inbound_flow_id):
            body['InboundFlowId'] = request.inbound_flow_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.outbound_all_depart):
            body['OutboundAllDepart'] = request.outbound_all_depart
        if not UtilClient.is_unset(request.outbound_range_list_shrink):
            body['OutboundRangeList'] = request.outbound_range_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddHotlineNumber',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.AddHotlineNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_hotline_number(
        self,
        request: aiccs_20191015_models.AddHotlineNumberRequest,
    ) -> aiccs_20191015_models.AddHotlineNumberResponse:
        """
        @summary 新增热线号码
        
        @param request: AddHotlineNumberRequest
        @return: AddHotlineNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_hotline_number_with_options(request, runtime)

    async def add_hotline_number_async(
        self,
        request: aiccs_20191015_models.AddHotlineNumberRequest,
    ) -> aiccs_20191015_models.AddHotlineNumberResponse:
        """
        @summary 新增热线号码
        
        @param request: AddHotlineNumberRequest
        @return: AddHotlineNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_hotline_number_with_options_async(request, runtime)

    def add_outer_account_with_options(
        self,
        request: aiccs_20191015_models.AddOuterAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.AddOuterAccountResponse:
        """
        @param request: AddOuterAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddOuterAccountResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddOuterAccount',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.AddOuterAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_outer_account_with_options_async(
        self,
        request: aiccs_20191015_models.AddOuterAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.AddOuterAccountResponse:
        """
        @param request: AddOuterAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddOuterAccountResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddOuterAccount',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.AddOuterAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_outer_account(
        self,
        request: aiccs_20191015_models.AddOuterAccountRequest,
    ) -> aiccs_20191015_models.AddOuterAccountResponse:
        """
        @param request: AddOuterAccountRequest
        @return: AddOuterAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_outer_account_with_options(request, runtime)

    async def add_outer_account_async(
        self,
        request: aiccs_20191015_models.AddOuterAccountRequest,
    ) -> aiccs_20191015_models.AddOuterAccountResponse:
        """
        @param request: AddOuterAccountRequest
        @return: AddOuterAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_outer_account_with_options_async(request, runtime)

    def add_skill_group_with_options(
        self,
        request: aiccs_20191015_models.AddSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.AddSkillGroupResponse:
        """
        @param request: AddSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSkillGroup',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.AddSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_skill_group_with_options_async(
        self,
        request: aiccs_20191015_models.AddSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.AddSkillGroupResponse:
        """
        @param request: AddSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSkillGroup',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.AddSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_skill_group(
        self,
        request: aiccs_20191015_models.AddSkillGroupRequest,
    ) -> aiccs_20191015_models.AddSkillGroupResponse:
        """
        @param request: AddSkillGroupRequest
        @return: AddSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_skill_group_with_options(request, runtime)

    async def add_skill_group_async(
        self,
        request: aiccs_20191015_models.AddSkillGroupRequest,
    ) -> aiccs_20191015_models.AddSkillGroupResponse:
        """
        @param request: AddSkillGroupRequest
        @return: AddSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_skill_group_with_options_async(request, runtime)

    def aiccs_smart_call_with_options(
        self,
        request: aiccs_20191015_models.AiccsSmartCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.AiccsSmartCallResponse:
        """
        @param request: AiccsSmartCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AiccsSmartCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_code_break):
            query['ActionCodeBreak'] = request.action_code_break
        if not UtilClient.is_unset(request.action_code_time_break):
            query['ActionCodeTimeBreak'] = request.action_code_time_break
        if not UtilClient.is_unset(request.asr_als_am_id):
            query['AsrAlsAmId'] = request.asr_als_am_id
        if not UtilClient.is_unset(request.asr_base_id):
            query['AsrBaseId'] = request.asr_base_id
        if not UtilClient.is_unset(request.asr_model_id):
            query['AsrModelId'] = request.asr_model_id
        if not UtilClient.is_unset(request.asr_vocabulary_id):
            query['AsrVocabularyId'] = request.asr_vocabulary_id
        if not UtilClient.is_unset(request.background_file_code):
            query['BackgroundFileCode'] = request.background_file_code
        if not UtilClient.is_unset(request.background_speed):
            query['BackgroundSpeed'] = request.background_speed
        if not UtilClient.is_unset(request.background_volume):
            query['BackgroundVolume'] = request.background_volume
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not UtilClient.is_unset(request.dynamic_id):
            query['DynamicId'] = request.dynamic_id
        if not UtilClient.is_unset(request.early_media_asr):
            query['EarlyMediaAsr'] = request.early_media_asr
        if not UtilClient.is_unset(request.enable_itn):
            query['EnableITN'] = request.enable_itn
        if not UtilClient.is_unset(request.mute_time):
            query['MuteTime'] = request.mute_time
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pause_time):
            query['PauseTime'] = request.pause_time
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.record_flag):
            query['RecordFlag'] = request.record_flag
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.session_timeout):
            query['SessionTimeout'] = request.session_timeout
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.tts_conf):
            query['TtsConf'] = request.tts_conf
        if not UtilClient.is_unset(request.tts_speed):
            query['TtsSpeed'] = request.tts_speed
        if not UtilClient.is_unset(request.tts_style):
            query['TtsStyle'] = request.tts_style
        if not UtilClient.is_unset(request.tts_volume):
            query['TtsVolume'] = request.tts_volume
        if not UtilClient.is_unset(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not UtilClient.is_unset(request.voice_code_param):
            query['VoiceCodeParam'] = request.voice_code_param
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AiccsSmartCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.AiccsSmartCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def aiccs_smart_call_with_options_async(
        self,
        request: aiccs_20191015_models.AiccsSmartCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.AiccsSmartCallResponse:
        """
        @param request: AiccsSmartCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AiccsSmartCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_code_break):
            query['ActionCodeBreak'] = request.action_code_break
        if not UtilClient.is_unset(request.action_code_time_break):
            query['ActionCodeTimeBreak'] = request.action_code_time_break
        if not UtilClient.is_unset(request.asr_als_am_id):
            query['AsrAlsAmId'] = request.asr_als_am_id
        if not UtilClient.is_unset(request.asr_base_id):
            query['AsrBaseId'] = request.asr_base_id
        if not UtilClient.is_unset(request.asr_model_id):
            query['AsrModelId'] = request.asr_model_id
        if not UtilClient.is_unset(request.asr_vocabulary_id):
            query['AsrVocabularyId'] = request.asr_vocabulary_id
        if not UtilClient.is_unset(request.background_file_code):
            query['BackgroundFileCode'] = request.background_file_code
        if not UtilClient.is_unset(request.background_speed):
            query['BackgroundSpeed'] = request.background_speed
        if not UtilClient.is_unset(request.background_volume):
            query['BackgroundVolume'] = request.background_volume
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not UtilClient.is_unset(request.dynamic_id):
            query['DynamicId'] = request.dynamic_id
        if not UtilClient.is_unset(request.early_media_asr):
            query['EarlyMediaAsr'] = request.early_media_asr
        if not UtilClient.is_unset(request.enable_itn):
            query['EnableITN'] = request.enable_itn
        if not UtilClient.is_unset(request.mute_time):
            query['MuteTime'] = request.mute_time
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pause_time):
            query['PauseTime'] = request.pause_time
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.record_flag):
            query['RecordFlag'] = request.record_flag
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.session_timeout):
            query['SessionTimeout'] = request.session_timeout
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.tts_conf):
            query['TtsConf'] = request.tts_conf
        if not UtilClient.is_unset(request.tts_speed):
            query['TtsSpeed'] = request.tts_speed
        if not UtilClient.is_unset(request.tts_style):
            query['TtsStyle'] = request.tts_style
        if not UtilClient.is_unset(request.tts_volume):
            query['TtsVolume'] = request.tts_volume
        if not UtilClient.is_unset(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not UtilClient.is_unset(request.voice_code_param):
            query['VoiceCodeParam'] = request.voice_code_param
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AiccsSmartCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.AiccsSmartCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def aiccs_smart_call(
        self,
        request: aiccs_20191015_models.AiccsSmartCallRequest,
    ) -> aiccs_20191015_models.AiccsSmartCallResponse:
        """
        @param request: AiccsSmartCallRequest
        @return: AiccsSmartCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.aiccs_smart_call_with_options(request, runtime)

    async def aiccs_smart_call_async(
        self,
        request: aiccs_20191015_models.AiccsSmartCallRequest,
    ) -> aiccs_20191015_models.AiccsSmartCallResponse:
        """
        @param request: AiccsSmartCallRequest
        @return: AiccsSmartCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.aiccs_smart_call_with_options_async(request, runtime)

    def aiccs_smart_call_operate_with_options(
        self,
        request: aiccs_20191015_models.AiccsSmartCallOperateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.AiccsSmartCallOperateResponse:
        """
        @param request: AiccsSmartCallOperateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AiccsSmartCallOperateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AiccsSmartCallOperate',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.AiccsSmartCallOperateResponse(),
            self.call_api(params, req, runtime)
        )

    async def aiccs_smart_call_operate_with_options_async(
        self,
        request: aiccs_20191015_models.AiccsSmartCallOperateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.AiccsSmartCallOperateResponse:
        """
        @param request: AiccsSmartCallOperateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AiccsSmartCallOperateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AiccsSmartCallOperate',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.AiccsSmartCallOperateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def aiccs_smart_call_operate(
        self,
        request: aiccs_20191015_models.AiccsSmartCallOperateRequest,
    ) -> aiccs_20191015_models.AiccsSmartCallOperateResponse:
        """
        @param request: AiccsSmartCallOperateRequest
        @return: AiccsSmartCallOperateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.aiccs_smart_call_operate_with_options(request, runtime)

    async def aiccs_smart_call_operate_async(
        self,
        request: aiccs_20191015_models.AiccsSmartCallOperateRequest,
    ) -> aiccs_20191015_models.AiccsSmartCallOperateResponse:
        """
        @param request: AiccsSmartCallOperateRequest
        @return: AiccsSmartCallOperateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.aiccs_smart_call_operate_with_options_async(request, runtime)

    def answer_call_with_options(
        self,
        request: aiccs_20191015_models.AnswerCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.AnswerCallResponse:
        """
        @param request: AnswerCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AnswerCallResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.call_id):
            body['CallId'] = request.call_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AnswerCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.AnswerCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def answer_call_with_options_async(
        self,
        request: aiccs_20191015_models.AnswerCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.AnswerCallResponse:
        """
        @param request: AnswerCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AnswerCallResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.call_id):
            body['CallId'] = request.call_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AnswerCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.AnswerCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def answer_call(
        self,
        request: aiccs_20191015_models.AnswerCallRequest,
    ) -> aiccs_20191015_models.AnswerCallResponse:
        """
        @param request: AnswerCallRequest
        @return: AnswerCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.answer_call_with_options(request, runtime)

    async def answer_call_async(
        self,
        request: aiccs_20191015_models.AnswerCallRequest,
    ) -> aiccs_20191015_models.AnswerCallResponse:
        """
        @param request: AnswerCallRequest
        @return: AnswerCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.answer_call_with_options_async(request, runtime)

    def attach_task_with_options(
        self,
        request: aiccs_20191015_models.AttachTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.AttachTaskResponse:
        """
        @summary 追加任务明细
        
        @param request: AttachTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_string):
            query['CallString'] = request.call_string
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.AttachTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_task_with_options_async(
        self,
        request: aiccs_20191015_models.AttachTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.AttachTaskResponse:
        """
        @summary 追加任务明细
        
        @param request: AttachTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_string):
            query['CallString'] = request.call_string
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.AttachTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_task(
        self,
        request: aiccs_20191015_models.AttachTaskRequest,
    ) -> aiccs_20191015_models.AttachTaskResponse:
        """
        @summary 追加任务明细
        
        @param request: AttachTaskRequest
        @return: AttachTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_task_with_options(request, runtime)

    async def attach_task_async(
        self,
        request: aiccs_20191015_models.AttachTaskRequest,
    ) -> aiccs_20191015_models.AttachTaskResponse:
        """
        @summary 追加任务明细
        
        @param request: AttachTaskRequest
        @return: AttachTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_task_with_options_async(request, runtime)

    def batch_create_quality_projects_with_options(
        self,
        request: aiccs_20191015_models.BatchCreateQualityProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.BatchCreateQualityProjectsResponse:
        """
        @param request: BatchCreateQualityProjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCreateQualityProjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analysis_ids):
            query['AnalysisIds'] = request.analysis_ids
        if not UtilClient.is_unset(request.channel_touch_type):
            query['ChannelTouchType'] = request.channel_touch_type
        if not UtilClient.is_unset(request.check_freq_type):
            query['CheckFreqType'] = request.check_freq_type
        if not UtilClient.is_unset(request.instance_list):
            query['InstanceList'] = request.instance_list
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.time_range_end):
            query['TimeRangeEnd'] = request.time_range_end
        if not UtilClient.is_unset(request.time_range_start):
            query['TimeRangeStart'] = request.time_range_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchCreateQualityProjects',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.BatchCreateQualityProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_create_quality_projects_with_options_async(
        self,
        request: aiccs_20191015_models.BatchCreateQualityProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.BatchCreateQualityProjectsResponse:
        """
        @param request: BatchCreateQualityProjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCreateQualityProjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analysis_ids):
            query['AnalysisIds'] = request.analysis_ids
        if not UtilClient.is_unset(request.channel_touch_type):
            query['ChannelTouchType'] = request.channel_touch_type
        if not UtilClient.is_unset(request.check_freq_type):
            query['CheckFreqType'] = request.check_freq_type
        if not UtilClient.is_unset(request.instance_list):
            query['InstanceList'] = request.instance_list
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.time_range_end):
            query['TimeRangeEnd'] = request.time_range_end
        if not UtilClient.is_unset(request.time_range_start):
            query['TimeRangeStart'] = request.time_range_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchCreateQualityProjects',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.BatchCreateQualityProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_create_quality_projects(
        self,
        request: aiccs_20191015_models.BatchCreateQualityProjectsRequest,
    ) -> aiccs_20191015_models.BatchCreateQualityProjectsResponse:
        """
        @param request: BatchCreateQualityProjectsRequest
        @return: BatchCreateQualityProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_create_quality_projects_with_options(request, runtime)

    async def batch_create_quality_projects_async(
        self,
        request: aiccs_20191015_models.BatchCreateQualityProjectsRequest,
    ) -> aiccs_20191015_models.BatchCreateQualityProjectsResponse:
        """
        @param request: BatchCreateQualityProjectsRequest
        @return: BatchCreateQualityProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_create_quality_projects_with_options_async(request, runtime)

    def cancel_ai_call_details_with_options(
        self,
        tmp_req: aiccs_20191015_models.CancelAiCallDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CancelAiCallDetailsResponse:
        """
        @summary 批量取消大模型解决方案Ai外呼明细任务
        
        @param tmp_req: CancelAiCallDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelAiCallDetailsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.CancelAiCallDetailsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.detail_id_list):
            request.detail_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.detail_id_list, 'DetailIdList', 'json')
        if not UtilClient.is_unset(tmp_req.phone_numbers):
            request.phone_numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phone_numbers, 'PhoneNumbers', 'json')
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.detail_id_list_shrink):
            query['DetailIdList'] = request.detail_id_list_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_numbers_shrink):
            query['PhoneNumbers'] = request.phone_numbers_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelAiCallDetails',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CancelAiCallDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_ai_call_details_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.CancelAiCallDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CancelAiCallDetailsResponse:
        """
        @summary 批量取消大模型解决方案Ai外呼明细任务
        
        @param tmp_req: CancelAiCallDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelAiCallDetailsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.CancelAiCallDetailsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.detail_id_list):
            request.detail_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.detail_id_list, 'DetailIdList', 'json')
        if not UtilClient.is_unset(tmp_req.phone_numbers):
            request.phone_numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phone_numbers, 'PhoneNumbers', 'json')
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.detail_id_list_shrink):
            query['DetailIdList'] = request.detail_id_list_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_numbers_shrink):
            query['PhoneNumbers'] = request.phone_numbers_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelAiCallDetails',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CancelAiCallDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_ai_call_details(
        self,
        request: aiccs_20191015_models.CancelAiCallDetailsRequest,
    ) -> aiccs_20191015_models.CancelAiCallDetailsResponse:
        """
        @summary 批量取消大模型解决方案Ai外呼明细任务
        
        @param request: CancelAiCallDetailsRequest
        @return: CancelAiCallDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_ai_call_details_with_options(request, runtime)

    async def cancel_ai_call_details_async(
        self,
        request: aiccs_20191015_models.CancelAiCallDetailsRequest,
    ) -> aiccs_20191015_models.CancelAiCallDetailsResponse:
        """
        @summary 批量取消大模型解决方案Ai外呼明细任务
        
        @param request: CancelAiCallDetailsRequest
        @return: CancelAiCallDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_ai_call_details_with_options_async(request, runtime)

    def cancel_task_with_options(
        self,
        request: aiccs_20191015_models.CancelTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CancelTaskResponse:
        """
        @summary 删除智能外呼任务
        
        @param request: CancelTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CancelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_task_with_options_async(
        self,
        request: aiccs_20191015_models.CancelTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CancelTaskResponse:
        """
        @summary 删除智能外呼任务
        
        @param request: CancelTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CancelTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_task(
        self,
        request: aiccs_20191015_models.CancelTaskRequest,
    ) -> aiccs_20191015_models.CancelTaskResponse:
        """
        @summary 删除智能外呼任务
        
        @param request: CancelTaskRequest
        @return: CancelTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_task_with_options(request, runtime)

    async def cancel_task_async(
        self,
        request: aiccs_20191015_models.CancelTaskRequest,
    ) -> aiccs_20191015_models.CancelTaskResponse:
        """
        @summary 删除智能外呼任务
        
        @param request: CancelTaskRequest
        @return: CancelTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_task_with_options_async(request, runtime)

    def change_chat_agent_status_with_options(
        self,
        request: aiccs_20191015_models.ChangeChatAgentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ChangeChatAgentStatusResponse:
        """
        @summary 修改在线客服状态
        
        @param request: ChangeChatAgentStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeChatAgentStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.method):
            body['Method'] = request.method
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeChatAgentStatus',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ChangeChatAgentStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_chat_agent_status_with_options_async(
        self,
        request: aiccs_20191015_models.ChangeChatAgentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ChangeChatAgentStatusResponse:
        """
        @summary 修改在线客服状态
        
        @param request: ChangeChatAgentStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeChatAgentStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.method):
            body['Method'] = request.method
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeChatAgentStatus',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ChangeChatAgentStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_chat_agent_status(
        self,
        request: aiccs_20191015_models.ChangeChatAgentStatusRequest,
    ) -> aiccs_20191015_models.ChangeChatAgentStatusResponse:
        """
        @summary 修改在线客服状态
        
        @param request: ChangeChatAgentStatusRequest
        @return: ChangeChatAgentStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_chat_agent_status_with_options(request, runtime)

    async def change_chat_agent_status_async(
        self,
        request: aiccs_20191015_models.ChangeChatAgentStatusRequest,
    ) -> aiccs_20191015_models.ChangeChatAgentStatusResponse:
        """
        @summary 修改在线客服状态
        
        @param request: ChangeChatAgentStatusRequest
        @return: ChangeChatAgentStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_chat_agent_status_with_options_async(request, runtime)

    def change_quality_project_status_with_options(
        self,
        request: aiccs_20191015_models.ChangeQualityProjectStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ChangeQualityProjectStatusResponse:
        """
        @param request: ChangeQualityProjectStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeQualityProjectStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeQualityProjectStatus',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ChangeQualityProjectStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_quality_project_status_with_options_async(
        self,
        request: aiccs_20191015_models.ChangeQualityProjectStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ChangeQualityProjectStatusResponse:
        """
        @param request: ChangeQualityProjectStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeQualityProjectStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeQualityProjectStatus',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ChangeQualityProjectStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_quality_project_status(
        self,
        request: aiccs_20191015_models.ChangeQualityProjectStatusRequest,
    ) -> aiccs_20191015_models.ChangeQualityProjectStatusResponse:
        """
        @param request: ChangeQualityProjectStatusRequest
        @return: ChangeQualityProjectStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_quality_project_status_with_options(request, runtime)

    async def change_quality_project_status_async(
        self,
        request: aiccs_20191015_models.ChangeQualityProjectStatusRequest,
    ) -> aiccs_20191015_models.ChangeQualityProjectStatusResponse:
        """
        @param request: ChangeQualityProjectStatusRequest
        @return: ChangeQualityProjectStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_quality_project_status_with_options_async(request, runtime)

    def create_agent_with_options(
        self,
        request: aiccs_20191015_models.CreateAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateAgentResponse:
        """
        @param request: CreateAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAgentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        body_flat = {}
        if not UtilClient.is_unset(request.skill_group_id):
            body_flat['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.skill_group_id_list):
            body_flat['SkillGroupIdList'] = request.skill_group_id_list
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAgent',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_agent_with_options_async(
        self,
        request: aiccs_20191015_models.CreateAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateAgentResponse:
        """
        @param request: CreateAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAgentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        body_flat = {}
        if not UtilClient.is_unset(request.skill_group_id):
            body_flat['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.skill_group_id_list):
            body_flat['SkillGroupIdList'] = request.skill_group_id_list
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAgent',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_agent(
        self,
        request: aiccs_20191015_models.CreateAgentRequest,
    ) -> aiccs_20191015_models.CreateAgentResponse:
        """
        @param request: CreateAgentRequest
        @return: CreateAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_agent_with_options(request, runtime)

    async def create_agent_async(
        self,
        request: aiccs_20191015_models.CreateAgentRequest,
    ) -> aiccs_20191015_models.CreateAgentResponse:
        """
        @param request: CreateAgentRequest
        @return: CreateAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_agent_with_options_async(request, runtime)

    def create_ai_call_task_with_options(
        self,
        tmp_req: aiccs_20191015_models.CreateAiCallTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateAiCallTaskResponse:
        """
        @summary 创建任务
        
        @param tmp_req: CreateAiCallTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAiCallTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.CreateAiCallTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.call_day):
            request.call_day_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.call_day, 'CallDay', 'json')
        if not UtilClient.is_unset(tmp_req.call_retry_reason):
            request.call_retry_reason_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.call_retry_reason, 'CallRetryReason', 'json')
        if not UtilClient.is_unset(tmp_req.call_time):
            request.call_time_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.call_time, 'CallTime', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.call_day_shrink):
            query['CallDay'] = request.call_day_shrink
        if not UtilClient.is_unset(request.call_retry_interval):
            query['CallRetryInterval'] = request.call_retry_interval
        if not UtilClient.is_unset(request.call_retry_reason_shrink):
            query['CallRetryReason'] = request.call_retry_reason_shrink
        if not UtilClient.is_unset(request.call_retry_times):
            query['CallRetryTimes'] = request.call_retry_times
        if not UtilClient.is_unset(request.call_time_shrink):
            query['CallTime'] = request.call_time_shrink
        if not UtilClient.is_unset(request.miss_call_retry):
            query['MissCallRetry'] = request.miss_call_retry
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_type):
            query['StartType'] = request.start_type
        if not UtilClient.is_unset(request.task_cps):
            query['TaskCps'] = request.task_cps
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_start_time):
            query['TaskStartTime'] = request.task_start_time
        if not UtilClient.is_unset(request.virtual_number):
            query['VirtualNumber'] = request.virtual_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAiCallTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateAiCallTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ai_call_task_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.CreateAiCallTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateAiCallTaskResponse:
        """
        @summary 创建任务
        
        @param tmp_req: CreateAiCallTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAiCallTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.CreateAiCallTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.call_day):
            request.call_day_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.call_day, 'CallDay', 'json')
        if not UtilClient.is_unset(tmp_req.call_retry_reason):
            request.call_retry_reason_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.call_retry_reason, 'CallRetryReason', 'json')
        if not UtilClient.is_unset(tmp_req.call_time):
            request.call_time_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.call_time, 'CallTime', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.call_day_shrink):
            query['CallDay'] = request.call_day_shrink
        if not UtilClient.is_unset(request.call_retry_interval):
            query['CallRetryInterval'] = request.call_retry_interval
        if not UtilClient.is_unset(request.call_retry_reason_shrink):
            query['CallRetryReason'] = request.call_retry_reason_shrink
        if not UtilClient.is_unset(request.call_retry_times):
            query['CallRetryTimes'] = request.call_retry_times
        if not UtilClient.is_unset(request.call_time_shrink):
            query['CallTime'] = request.call_time_shrink
        if not UtilClient.is_unset(request.miss_call_retry):
            query['MissCallRetry'] = request.miss_call_retry
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_type):
            query['StartType'] = request.start_type
        if not UtilClient.is_unset(request.task_cps):
            query['TaskCps'] = request.task_cps
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_start_time):
            query['TaskStartTime'] = request.task_start_time
        if not UtilClient.is_unset(request.virtual_number):
            query['VirtualNumber'] = request.virtual_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAiCallTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateAiCallTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ai_call_task(
        self,
        request: aiccs_20191015_models.CreateAiCallTaskRequest,
    ) -> aiccs_20191015_models.CreateAiCallTaskResponse:
        """
        @summary 创建任务
        
        @param request: CreateAiCallTaskRequest
        @return: CreateAiCallTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ai_call_task_with_options(request, runtime)

    async def create_ai_call_task_async(
        self,
        request: aiccs_20191015_models.CreateAiCallTaskRequest,
    ) -> aiccs_20191015_models.CreateAiCallTaskResponse:
        """
        @summary 创建任务
        
        @param request: CreateAiCallTaskRequest
        @return: CreateAiCallTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_ai_call_task_with_options_async(request, runtime)

    def create_ai_outbound_task_with_options(
        self,
        tmp_req: aiccs_20191015_models.CreateAiOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateAiOutboundTaskResponse:
        """
        @summary 创建智能外呼任务（预测式外呼、自动外呼）
        
        @param tmp_req: CreateAiOutboundTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAiOutboundTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.CreateAiOutboundTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.outbound_nums):
            request.outbound_nums_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.outbound_nums, 'OutboundNums', 'json')
        if not UtilClient.is_unset(tmp_req.recall_rule):
            request.recall_rule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.recall_rule, 'RecallRule', 'json')
        query = {}
        if not UtilClient.is_unset(request.concurrent_rate):
            query['ConcurrentRate'] = request.concurrent_rate
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execution_time):
            query['ExecutionTime'] = request.execution_time
        if not UtilClient.is_unset(request.forecast_call_rate):
            query['ForecastCallRate'] = request.forecast_call_rate
        if not UtilClient.is_unset(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num_repeated):
            query['NumRepeated'] = request.num_repeated
        if not UtilClient.is_unset(request.outbound_nums_shrink):
            query['OutboundNums'] = request.outbound_nums_shrink
        if not UtilClient.is_unset(request.recall_rule_shrink):
            query['RecallRule'] = request.recall_rule_shrink
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAiOutboundTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateAiOutboundTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ai_outbound_task_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.CreateAiOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateAiOutboundTaskResponse:
        """
        @summary 创建智能外呼任务（预测式外呼、自动外呼）
        
        @param tmp_req: CreateAiOutboundTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAiOutboundTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.CreateAiOutboundTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.outbound_nums):
            request.outbound_nums_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.outbound_nums, 'OutboundNums', 'json')
        if not UtilClient.is_unset(tmp_req.recall_rule):
            request.recall_rule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.recall_rule, 'RecallRule', 'json')
        query = {}
        if not UtilClient.is_unset(request.concurrent_rate):
            query['ConcurrentRate'] = request.concurrent_rate
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execution_time):
            query['ExecutionTime'] = request.execution_time
        if not UtilClient.is_unset(request.forecast_call_rate):
            query['ForecastCallRate'] = request.forecast_call_rate
        if not UtilClient.is_unset(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num_repeated):
            query['NumRepeated'] = request.num_repeated
        if not UtilClient.is_unset(request.outbound_nums_shrink):
            query['OutboundNums'] = request.outbound_nums_shrink
        if not UtilClient.is_unset(request.recall_rule_shrink):
            query['RecallRule'] = request.recall_rule_shrink
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAiOutboundTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateAiOutboundTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ai_outbound_task(
        self,
        request: aiccs_20191015_models.CreateAiOutboundTaskRequest,
    ) -> aiccs_20191015_models.CreateAiOutboundTaskResponse:
        """
        @summary 创建智能外呼任务（预测式外呼、自动外呼）
        
        @param request: CreateAiOutboundTaskRequest
        @return: CreateAiOutboundTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ai_outbound_task_with_options(request, runtime)

    async def create_ai_outbound_task_async(
        self,
        request: aiccs_20191015_models.CreateAiOutboundTaskRequest,
    ) -> aiccs_20191015_models.CreateAiOutboundTaskResponse:
        """
        @summary 创建智能外呼任务（预测式外呼、自动外呼）
        
        @param request: CreateAiOutboundTaskRequest
        @return: CreateAiOutboundTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_ai_outbound_task_with_options_async(request, runtime)

    def create_ai_outbound_task_batch_with_options(
        self,
        request: aiccs_20191015_models.CreateAiOutboundTaskBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateAiOutboundTaskBatchResponse:
        """
        @summary 创建智能外呼任务批次
        
        @param request: CreateAiOutboundTaskBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAiOutboundTaskBatchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAiOutboundTaskBatch',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateAiOutboundTaskBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ai_outbound_task_batch_with_options_async(
        self,
        request: aiccs_20191015_models.CreateAiOutboundTaskBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateAiOutboundTaskBatchResponse:
        """
        @summary 创建智能外呼任务批次
        
        @param request: CreateAiOutboundTaskBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAiOutboundTaskBatchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAiOutboundTaskBatch',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateAiOutboundTaskBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ai_outbound_task_batch(
        self,
        request: aiccs_20191015_models.CreateAiOutboundTaskBatchRequest,
    ) -> aiccs_20191015_models.CreateAiOutboundTaskBatchResponse:
        """
        @summary 创建智能外呼任务批次
        
        @param request: CreateAiOutboundTaskBatchRequest
        @return: CreateAiOutboundTaskBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ai_outbound_task_batch_with_options(request, runtime)

    async def create_ai_outbound_task_batch_async(
        self,
        request: aiccs_20191015_models.CreateAiOutboundTaskBatchRequest,
    ) -> aiccs_20191015_models.CreateAiOutboundTaskBatchResponse:
        """
        @summary 创建智能外呼任务批次
        
        @param request: CreateAiOutboundTaskBatchRequest
        @return: CreateAiOutboundTaskBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_ai_outbound_task_batch_with_options_async(request, runtime)

    def create_department_with_options(
        self,
        request: aiccs_20191015_models.CreateDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateDepartmentResponse:
        """
        @summary 创建部门信息
        
        @param request: CreateDepartmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDepartmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_name):
            query['DepartmentName'] = request.department_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDepartment',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateDepartmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_department_with_options_async(
        self,
        request: aiccs_20191015_models.CreateDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateDepartmentResponse:
        """
        @summary 创建部门信息
        
        @param request: CreateDepartmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDepartmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_name):
            query['DepartmentName'] = request.department_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDepartment',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateDepartmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_department(
        self,
        request: aiccs_20191015_models.CreateDepartmentRequest,
    ) -> aiccs_20191015_models.CreateDepartmentResponse:
        """
        @summary 创建部门信息
        
        @param request: CreateDepartmentRequest
        @return: CreateDepartmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_department_with_options(request, runtime)

    async def create_department_async(
        self,
        request: aiccs_20191015_models.CreateDepartmentRequest,
    ) -> aiccs_20191015_models.CreateDepartmentResponse:
        """
        @summary 创建部门信息
        
        @param request: CreateDepartmentRequest
        @return: CreateDepartmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_department_with_options_async(request, runtime)

    def create_outbound_task_with_options(
        self,
        request: aiccs_20191015_models.CreateOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateOutboundTaskResponse:
        """
        @param request: CreateOutboundTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOutboundTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ani):
            query['Ani'] = request.ani
        if not UtilClient.is_unset(request.call_infos):
            query['CallInfos'] = request.call_infos
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ext_attrs):
            query['ExtAttrs'] = request.ext_attrs
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        if not UtilClient.is_unset(request.retry_interval):
            query['RetryInterval'] = request.retry_interval
        if not UtilClient.is_unset(request.retry_time):
            query['RetryTime'] = request.retry_time
        if not UtilClient.is_unset(request.skill_group):
            query['SkillGroup'] = request.skill_group
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOutboundTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateOutboundTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_outbound_task_with_options_async(
        self,
        request: aiccs_20191015_models.CreateOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateOutboundTaskResponse:
        """
        @param request: CreateOutboundTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOutboundTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ani):
            query['Ani'] = request.ani
        if not UtilClient.is_unset(request.call_infos):
            query['CallInfos'] = request.call_infos
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ext_attrs):
            query['ExtAttrs'] = request.ext_attrs
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        if not UtilClient.is_unset(request.retry_interval):
            query['RetryInterval'] = request.retry_interval
        if not UtilClient.is_unset(request.retry_time):
            query['RetryTime'] = request.retry_time
        if not UtilClient.is_unset(request.skill_group):
            query['SkillGroup'] = request.skill_group
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOutboundTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateOutboundTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_outbound_task(
        self,
        request: aiccs_20191015_models.CreateOutboundTaskRequest,
    ) -> aiccs_20191015_models.CreateOutboundTaskResponse:
        """
        @param request: CreateOutboundTaskRequest
        @return: CreateOutboundTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_outbound_task_with_options(request, runtime)

    async def create_outbound_task_async(
        self,
        request: aiccs_20191015_models.CreateOutboundTaskRequest,
    ) -> aiccs_20191015_models.CreateOutboundTaskResponse:
        """
        @param request: CreateOutboundTaskRequest
        @return: CreateOutboundTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_outbound_task_with_options_async(request, runtime)

    def create_quality_project_with_options(
        self,
        request: aiccs_20191015_models.CreateQualityProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateQualityProjectResponse:
        """
        @param request: CreateQualityProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQualityProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.analysis_ids):
            body['AnalysisIds'] = request.analysis_ids
        if not UtilClient.is_unset(request.channel_touch_type):
            body['ChannelTouchType'] = request.channel_touch_type
        if not UtilClient.is_unset(request.check_freq_type):
            body['CheckFreqType'] = request.check_freq_type
        if not UtilClient.is_unset(request.dep_list):
            body['DepList'] = request.dep_list
        if not UtilClient.is_unset(request.group_list):
            body['GroupList'] = request.group_list
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.scope_type):
            body['ScopeType'] = request.scope_type
        if not UtilClient.is_unset(request.servicer_list):
            body['ServicerList'] = request.servicer_list
        if not UtilClient.is_unset(request.time_range_end):
            body['TimeRangeEnd'] = request.time_range_end
        if not UtilClient.is_unset(request.time_range_start):
            body['TimeRangeStart'] = request.time_range_start
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQualityProject',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateQualityProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_quality_project_with_options_async(
        self,
        request: aiccs_20191015_models.CreateQualityProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateQualityProjectResponse:
        """
        @param request: CreateQualityProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQualityProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.analysis_ids):
            body['AnalysisIds'] = request.analysis_ids
        if not UtilClient.is_unset(request.channel_touch_type):
            body['ChannelTouchType'] = request.channel_touch_type
        if not UtilClient.is_unset(request.check_freq_type):
            body['CheckFreqType'] = request.check_freq_type
        if not UtilClient.is_unset(request.dep_list):
            body['DepList'] = request.dep_list
        if not UtilClient.is_unset(request.group_list):
            body['GroupList'] = request.group_list
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.scope_type):
            body['ScopeType'] = request.scope_type
        if not UtilClient.is_unset(request.servicer_list):
            body['ServicerList'] = request.servicer_list
        if not UtilClient.is_unset(request.time_range_end):
            body['TimeRangeEnd'] = request.time_range_end
        if not UtilClient.is_unset(request.time_range_start):
            body['TimeRangeStart'] = request.time_range_start
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQualityProject',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateQualityProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_quality_project(
        self,
        request: aiccs_20191015_models.CreateQualityProjectRequest,
    ) -> aiccs_20191015_models.CreateQualityProjectResponse:
        """
        @param request: CreateQualityProjectRequest
        @return: CreateQualityProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_quality_project_with_options(request, runtime)

    async def create_quality_project_async(
        self,
        request: aiccs_20191015_models.CreateQualityProjectRequest,
    ) -> aiccs_20191015_models.CreateQualityProjectResponse:
        """
        @param request: CreateQualityProjectRequest
        @return: CreateQualityProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_quality_project_with_options_async(request, runtime)

    def create_quality_rule_with_options(
        self,
        request: aiccs_20191015_models.CreateQualityRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateQualityRuleResponse:
        """
        @param request: CreateQualityRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQualityRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.key_words):
            body['KeyWords'] = request.key_words
        if not UtilClient.is_unset(request.match_type):
            body['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.rule_tag):
            body['RuleTag'] = request.rule_tag
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQualityRule',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateQualityRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_quality_rule_with_options_async(
        self,
        request: aiccs_20191015_models.CreateQualityRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateQualityRuleResponse:
        """
        @param request: CreateQualityRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQualityRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.key_words):
            body['KeyWords'] = request.key_words
        if not UtilClient.is_unset(request.match_type):
            body['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.rule_tag):
            body['RuleTag'] = request.rule_tag
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQualityRule',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateQualityRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_quality_rule(
        self,
        request: aiccs_20191015_models.CreateQualityRuleRequest,
    ) -> aiccs_20191015_models.CreateQualityRuleResponse:
        """
        @param request: CreateQualityRuleRequest
        @return: CreateQualityRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_quality_rule_with_options(request, runtime)

    async def create_quality_rule_async(
        self,
        request: aiccs_20191015_models.CreateQualityRuleRequest,
    ) -> aiccs_20191015_models.CreateQualityRuleResponse:
        """
        @param request: CreateQualityRuleRequest
        @return: CreateQualityRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_quality_rule_with_options_async(request, runtime)

    def create_skill_group_with_options(
        self,
        request: aiccs_20191015_models.CreateSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateSkillGroupResponse:
        """
        @param request: CreateSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSkillGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_type):
            body['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.department_id):
            body['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_name):
            body['SkillGroupName'] = request.skill_group_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSkillGroup',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_skill_group_with_options_async(
        self,
        request: aiccs_20191015_models.CreateSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateSkillGroupResponse:
        """
        @param request: CreateSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSkillGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_type):
            body['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.department_id):
            body['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_name):
            body['SkillGroupName'] = request.skill_group_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSkillGroup',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_skill_group(
        self,
        request: aiccs_20191015_models.CreateSkillGroupRequest,
    ) -> aiccs_20191015_models.CreateSkillGroupResponse:
        """
        @param request: CreateSkillGroupRequest
        @return: CreateSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_skill_group_with_options(request, runtime)

    async def create_skill_group_async(
        self,
        request: aiccs_20191015_models.CreateSkillGroupRequest,
    ) -> aiccs_20191015_models.CreateSkillGroupResponse:
        """
        @param request: CreateSkillGroupRequest
        @return: CreateSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_skill_group_with_options_async(request, runtime)

    def create_task_with_options(
        self,
        request: aiccs_20191015_models.CreateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateTaskResponse:
        """
        @summary 创建外呼任务
        
        @param request: CreateTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_string):
            query['CallString'] = request.call_string
        if not UtilClient.is_unset(request.call_string_type):
            query['CallStringType'] = request.call_string_type
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.retry_count):
            query['RetryCount'] = request.retry_count
        if not UtilClient.is_unset(request.retry_flag):
            query['RetryFlag'] = request.retry_flag
        if not UtilClient.is_unset(request.retry_interval):
            query['RetryInterval'] = request.retry_interval
        if not UtilClient.is_unset(request.retry_status_code):
            query['RetryStatusCode'] = request.retry_status_code
        if not UtilClient.is_unset(request.robot_id):
            query['RobotId'] = request.robot_id
        if not UtilClient.is_unset(request.seat_count):
            query['SeatCount'] = request.seat_count
        if not UtilClient.is_unset(request.start_now):
            query['StartNow'] = request.start_now
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.work_day):
            query['WorkDay'] = request.work_day
        if not UtilClient.is_unset(request.work_time_list):
            query['WorkTimeList'] = request.work_time_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_task_with_options_async(
        self,
        request: aiccs_20191015_models.CreateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateTaskResponse:
        """
        @summary 创建外呼任务
        
        @param request: CreateTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_string):
            query['CallString'] = request.call_string
        if not UtilClient.is_unset(request.call_string_type):
            query['CallStringType'] = request.call_string_type
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.retry_count):
            query['RetryCount'] = request.retry_count
        if not UtilClient.is_unset(request.retry_flag):
            query['RetryFlag'] = request.retry_flag
        if not UtilClient.is_unset(request.retry_interval):
            query['RetryInterval'] = request.retry_interval
        if not UtilClient.is_unset(request.retry_status_code):
            query['RetryStatusCode'] = request.retry_status_code
        if not UtilClient.is_unset(request.robot_id):
            query['RobotId'] = request.robot_id
        if not UtilClient.is_unset(request.seat_count):
            query['SeatCount'] = request.seat_count
        if not UtilClient.is_unset(request.start_now):
            query['StartNow'] = request.start_now
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.work_day):
            query['WorkDay'] = request.work_day
        if not UtilClient.is_unset(request.work_time_list):
            query['WorkTimeList'] = request.work_time_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_task(
        self,
        request: aiccs_20191015_models.CreateTaskRequest,
    ) -> aiccs_20191015_models.CreateTaskResponse:
        """
        @summary 创建外呼任务
        
        @param request: CreateTaskRequest
        @return: CreateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_task_with_options(request, runtime)

    async def create_task_async(
        self,
        request: aiccs_20191015_models.CreateTaskRequest,
    ) -> aiccs_20191015_models.CreateTaskResponse:
        """
        @summary 创建外呼任务
        
        @param request: CreateTaskRequest
        @return: CreateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_task_with_options_async(request, runtime)

    def create_third_sso_agent_with_options(
        self,
        request: aiccs_20191015_models.CreateThirdSsoAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateThirdSsoAgentResponse:
        """
        @summary 创建坐席并开通sso登录能力
        
        @param request: CreateThirdSsoAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateThirdSsoAgentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        body_flat = {}
        if not UtilClient.is_unset(request.role_ids):
            body_flat['RoleIds'] = request.role_ids
        if not UtilClient.is_unset(request.skill_group_ids):
            body_flat['SkillGroupIds'] = request.skill_group_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateThirdSsoAgent',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateThirdSsoAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_third_sso_agent_with_options_async(
        self,
        request: aiccs_20191015_models.CreateThirdSsoAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateThirdSsoAgentResponse:
        """
        @summary 创建坐席并开通sso登录能力
        
        @param request: CreateThirdSsoAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateThirdSsoAgentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        body_flat = {}
        if not UtilClient.is_unset(request.role_ids):
            body_flat['RoleIds'] = request.role_ids
        if not UtilClient.is_unset(request.skill_group_ids):
            body_flat['SkillGroupIds'] = request.skill_group_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateThirdSsoAgent',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateThirdSsoAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_third_sso_agent(
        self,
        request: aiccs_20191015_models.CreateThirdSsoAgentRequest,
    ) -> aiccs_20191015_models.CreateThirdSsoAgentResponse:
        """
        @summary 创建坐席并开通sso登录能力
        
        @param request: CreateThirdSsoAgentRequest
        @return: CreateThirdSsoAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_third_sso_agent_with_options(request, runtime)

    async def create_third_sso_agent_async(
        self,
        request: aiccs_20191015_models.CreateThirdSsoAgentRequest,
    ) -> aiccs_20191015_models.CreateThirdSsoAgentResponse:
        """
        @summary 创建坐席并开通sso登录能力
        
        @param request: CreateThirdSsoAgentRequest
        @return: CreateThirdSsoAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_third_sso_agent_with_options_async(request, runtime)

    def delete_agent_with_options(
        self,
        request: aiccs_20191015_models.DeleteAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteAgentResponse:
        """
        @summary 删除坐席账号
        
        @param request: DeleteAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAgent',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='DELETE',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_agent_with_options_async(
        self,
        request: aiccs_20191015_models.DeleteAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteAgentResponse:
        """
        @summary 删除坐席账号
        
        @param request: DeleteAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAgent',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='DELETE',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_agent(
        self,
        request: aiccs_20191015_models.DeleteAgentRequest,
    ) -> aiccs_20191015_models.DeleteAgentResponse:
        """
        @summary 删除坐席账号
        
        @param request: DeleteAgentRequest
        @return: DeleteAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_agent_with_options(request, runtime)

    async def delete_agent_async(
        self,
        request: aiccs_20191015_models.DeleteAgentRequest,
    ) -> aiccs_20191015_models.DeleteAgentResponse:
        """
        @summary 删除坐席账号
        
        @param request: DeleteAgentRequest
        @return: DeleteAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_agent_with_options_async(request, runtime)

    def delete_ai_outbound_task_with_options(
        self,
        request: aiccs_20191015_models.DeleteAiOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteAiOutboundTaskResponse:
        """
        @summary 删除智能外呼任务
        
        @param request: DeleteAiOutboundTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAiOutboundTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAiOutboundTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteAiOutboundTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ai_outbound_task_with_options_async(
        self,
        request: aiccs_20191015_models.DeleteAiOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteAiOutboundTaskResponse:
        """
        @summary 删除智能外呼任务
        
        @param request: DeleteAiOutboundTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAiOutboundTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAiOutboundTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteAiOutboundTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ai_outbound_task(
        self,
        request: aiccs_20191015_models.DeleteAiOutboundTaskRequest,
    ) -> aiccs_20191015_models.DeleteAiOutboundTaskResponse:
        """
        @summary 删除智能外呼任务
        
        @param request: DeleteAiOutboundTaskRequest
        @return: DeleteAiOutboundTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_ai_outbound_task_with_options(request, runtime)

    async def delete_ai_outbound_task_async(
        self,
        request: aiccs_20191015_models.DeleteAiOutboundTaskRequest,
    ) -> aiccs_20191015_models.DeleteAiOutboundTaskResponse:
        """
        @summary 删除智能外呼任务
        
        @param request: DeleteAiOutboundTaskRequest
        @return: DeleteAiOutboundTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_ai_outbound_task_with_options_async(request, runtime)

    def delete_department_with_options(
        self,
        request: aiccs_20191015_models.DeleteDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteDepartmentResponse:
        """
        @summary 删除部门信息
        
        @param request: DeleteDepartmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDepartmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDepartment',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteDepartmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_department_with_options_async(
        self,
        request: aiccs_20191015_models.DeleteDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteDepartmentResponse:
        """
        @summary 删除部门信息
        
        @param request: DeleteDepartmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDepartmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDepartment',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteDepartmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_department(
        self,
        request: aiccs_20191015_models.DeleteDepartmentRequest,
    ) -> aiccs_20191015_models.DeleteDepartmentResponse:
        """
        @summary 删除部门信息
        
        @param request: DeleteDepartmentRequest
        @return: DeleteDepartmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_department_with_options(request, runtime)

    async def delete_department_async(
        self,
        request: aiccs_20191015_models.DeleteDepartmentRequest,
    ) -> aiccs_20191015_models.DeleteDepartmentResponse:
        """
        @summary 删除部门信息
        
        @param request: DeleteDepartmentRequest
        @return: DeleteDepartmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_department_with_options_async(request, runtime)

    def delete_hotline_number_with_options(
        self,
        request: aiccs_20191015_models.DeleteHotlineNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteHotlineNumberResponse:
        """
        @summary 删除热线号码
        
        @param request: DeleteHotlineNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHotlineNumberResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotline_number):
            body['HotlineNumber'] = request.hotline_number
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteHotlineNumber',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteHotlineNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hotline_number_with_options_async(
        self,
        request: aiccs_20191015_models.DeleteHotlineNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteHotlineNumberResponse:
        """
        @summary 删除热线号码
        
        @param request: DeleteHotlineNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHotlineNumberResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotline_number):
            body['HotlineNumber'] = request.hotline_number
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteHotlineNumber',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteHotlineNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hotline_number(
        self,
        request: aiccs_20191015_models.DeleteHotlineNumberRequest,
    ) -> aiccs_20191015_models.DeleteHotlineNumberResponse:
        """
        @summary 删除热线号码
        
        @param request: DeleteHotlineNumberRequest
        @return: DeleteHotlineNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_hotline_number_with_options(request, runtime)

    async def delete_hotline_number_async(
        self,
        request: aiccs_20191015_models.DeleteHotlineNumberRequest,
    ) -> aiccs_20191015_models.DeleteHotlineNumberResponse:
        """
        @summary 删除热线号码
        
        @param request: DeleteHotlineNumberRequest
        @return: DeleteHotlineNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_hotline_number_with_options_async(request, runtime)

    def delete_outbound_task_with_options(
        self,
        request: aiccs_20191015_models.DeleteOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteOutboundTaskResponse:
        """
        @param request: DeleteOutboundTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteOutboundTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.outbound_task_id):
            query['OutboundTaskId'] = request.outbound_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOutboundTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteOutboundTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_outbound_task_with_options_async(
        self,
        request: aiccs_20191015_models.DeleteOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteOutboundTaskResponse:
        """
        @param request: DeleteOutboundTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteOutboundTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.outbound_task_id):
            query['OutboundTaskId'] = request.outbound_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOutboundTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteOutboundTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_outbound_task(
        self,
        request: aiccs_20191015_models.DeleteOutboundTaskRequest,
    ) -> aiccs_20191015_models.DeleteOutboundTaskResponse:
        """
        @param request: DeleteOutboundTaskRequest
        @return: DeleteOutboundTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_outbound_task_with_options(request, runtime)

    async def delete_outbound_task_async(
        self,
        request: aiccs_20191015_models.DeleteOutboundTaskRequest,
    ) -> aiccs_20191015_models.DeleteOutboundTaskResponse:
        """
        @param request: DeleteOutboundTaskRequest
        @return: DeleteOutboundTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_outbound_task_with_options_async(request, runtime)

    def delete_outer_account_with_options(
        self,
        request: aiccs_20191015_models.DeleteOuterAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteOuterAccountResponse:
        """
        @param request: DeleteOuterAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteOuterAccountResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOuterAccount',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteOuterAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_outer_account_with_options_async(
        self,
        request: aiccs_20191015_models.DeleteOuterAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteOuterAccountResponse:
        """
        @param request: DeleteOuterAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteOuterAccountResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOuterAccount',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteOuterAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_outer_account(
        self,
        request: aiccs_20191015_models.DeleteOuterAccountRequest,
    ) -> aiccs_20191015_models.DeleteOuterAccountResponse:
        """
        @param request: DeleteOuterAccountRequest
        @return: DeleteOuterAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_outer_account_with_options(request, runtime)

    async def delete_outer_account_async(
        self,
        request: aiccs_20191015_models.DeleteOuterAccountRequest,
    ) -> aiccs_20191015_models.DeleteOuterAccountResponse:
        """
        @param request: DeleteOuterAccountRequest
        @return: DeleteOuterAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_outer_account_with_options_async(request, runtime)

    def delete_quality_project_with_options(
        self,
        request: aiccs_20191015_models.DeleteQualityProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteQualityProjectResponse:
        """
        @param request: DeleteQualityProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteQualityProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQualityProject',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteQualityProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_quality_project_with_options_async(
        self,
        request: aiccs_20191015_models.DeleteQualityProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteQualityProjectResponse:
        """
        @param request: DeleteQualityProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteQualityProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQualityProject',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteQualityProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_quality_project(
        self,
        request: aiccs_20191015_models.DeleteQualityProjectRequest,
    ) -> aiccs_20191015_models.DeleteQualityProjectResponse:
        """
        @param request: DeleteQualityProjectRequest
        @return: DeleteQualityProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_project_with_options(request, runtime)

    async def delete_quality_project_async(
        self,
        request: aiccs_20191015_models.DeleteQualityProjectRequest,
    ) -> aiccs_20191015_models.DeleteQualityProjectResponse:
        """
        @param request: DeleteQualityProjectRequest
        @return: DeleteQualityProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_quality_project_with_options_async(request, runtime)

    def delete_quality_rule_with_options(
        self,
        request: aiccs_20191015_models.DeleteQualityRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteQualityRuleResponse:
        """
        @param request: DeleteQualityRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteQualityRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQualityRule',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteQualityRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_quality_rule_with_options_async(
        self,
        request: aiccs_20191015_models.DeleteQualityRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteQualityRuleResponse:
        """
        @param request: DeleteQualityRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteQualityRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQualityRule',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteQualityRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_quality_rule(
        self,
        request: aiccs_20191015_models.DeleteQualityRuleRequest,
    ) -> aiccs_20191015_models.DeleteQualityRuleResponse:
        """
        @param request: DeleteQualityRuleRequest
        @return: DeleteQualityRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_rule_with_options(request, runtime)

    async def delete_quality_rule_async(
        self,
        request: aiccs_20191015_models.DeleteQualityRuleRequest,
    ) -> aiccs_20191015_models.DeleteQualityRuleResponse:
        """
        @param request: DeleteQualityRuleRequest
        @return: DeleteQualityRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_quality_rule_with_options_async(request, runtime)

    def delete_skill_group_with_options(
        self,
        request: aiccs_20191015_models.DeleteSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteSkillGroupResponse:
        """
        @param request: DeleteSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSkillGroup',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_skill_group_with_options_async(
        self,
        request: aiccs_20191015_models.DeleteSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteSkillGroupResponse:
        """
        @param request: DeleteSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSkillGroup',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_skill_group(
        self,
        request: aiccs_20191015_models.DeleteSkillGroupRequest,
    ) -> aiccs_20191015_models.DeleteSkillGroupResponse:
        """
        @param request: DeleteSkillGroupRequest
        @return: DeleteSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_skill_group_with_options(request, runtime)

    async def delete_skill_group_async(
        self,
        request: aiccs_20191015_models.DeleteSkillGroupRequest,
    ) -> aiccs_20191015_models.DeleteSkillGroupResponse:
        """
        @param request: DeleteSkillGroupRequest
        @return: DeleteSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_skill_group_with_options_async(request, runtime)

    def describe_record_data_with_options(
        self,
        request: aiccs_20191015_models.DescribeRecordDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DescribeRecordDataResponse:
        """
        @param request: DescribeRecordDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRecordDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.acid):
            query['Acid'] = request.acid
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sec_level):
            query['SecLevel'] = request.sec_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecordData',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DescribeRecordDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_record_data_with_options_async(
        self,
        request: aiccs_20191015_models.DescribeRecordDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DescribeRecordDataResponse:
        """
        @param request: DescribeRecordDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRecordDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.acid):
            query['Acid'] = request.acid
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sec_level):
            query['SecLevel'] = request.sec_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecordData',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DescribeRecordDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_record_data(
        self,
        request: aiccs_20191015_models.DescribeRecordDataRequest,
    ) -> aiccs_20191015_models.DescribeRecordDataResponse:
        """
        @param request: DescribeRecordDataRequest
        @return: DescribeRecordDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_record_data_with_options(request, runtime)

    async def describe_record_data_async(
        self,
        request: aiccs_20191015_models.DescribeRecordDataRequest,
    ) -> aiccs_20191015_models.DescribeRecordDataResponse:
        """
        @param request: DescribeRecordDataRequest
        @return: DescribeRecordDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_record_data_with_options_async(request, runtime)

    def edit_quality_project_with_options(
        self,
        request: aiccs_20191015_models.EditQualityProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.EditQualityProjectResponse:
        """
        @param request: EditQualityProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EditQualityProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analysis_ids):
            query['AnalysisIds'] = request.analysis_ids
        if not UtilClient.is_unset(request.channel_touch_type):
            query['ChannelTouchType'] = request.channel_touch_type
        if not UtilClient.is_unset(request.check_freq_type):
            query['CheckFreqType'] = request.check_freq_type
        if not UtilClient.is_unset(request.dep_list):
            query['DepList'] = request.dep_list
        if not UtilClient.is_unset(request.group_list):
            query['GroupList'] = request.group_list
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_version):
            query['ProjectVersion'] = request.project_version
        if not UtilClient.is_unset(request.scope_type):
            query['ScopeType'] = request.scope_type
        if not UtilClient.is_unset(request.servicer_list):
            query['ServicerList'] = request.servicer_list
        if not UtilClient.is_unset(request.time_range_end):
            query['TimeRangeEnd'] = request.time_range_end
        if not UtilClient.is_unset(request.time_range_start):
            query['TimeRangeStart'] = request.time_range_start
        body = {}
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EditQualityProject',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.EditQualityProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_quality_project_with_options_async(
        self,
        request: aiccs_20191015_models.EditQualityProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.EditQualityProjectResponse:
        """
        @param request: EditQualityProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EditQualityProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analysis_ids):
            query['AnalysisIds'] = request.analysis_ids
        if not UtilClient.is_unset(request.channel_touch_type):
            query['ChannelTouchType'] = request.channel_touch_type
        if not UtilClient.is_unset(request.check_freq_type):
            query['CheckFreqType'] = request.check_freq_type
        if not UtilClient.is_unset(request.dep_list):
            query['DepList'] = request.dep_list
        if not UtilClient.is_unset(request.group_list):
            query['GroupList'] = request.group_list
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_version):
            query['ProjectVersion'] = request.project_version
        if not UtilClient.is_unset(request.scope_type):
            query['ScopeType'] = request.scope_type
        if not UtilClient.is_unset(request.servicer_list):
            query['ServicerList'] = request.servicer_list
        if not UtilClient.is_unset(request.time_range_end):
            query['TimeRangeEnd'] = request.time_range_end
        if not UtilClient.is_unset(request.time_range_start):
            query['TimeRangeStart'] = request.time_range_start
        body = {}
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EditQualityProject',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.EditQualityProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_quality_project(
        self,
        request: aiccs_20191015_models.EditQualityProjectRequest,
    ) -> aiccs_20191015_models.EditQualityProjectResponse:
        """
        @param request: EditQualityProjectRequest
        @return: EditQualityProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.edit_quality_project_with_options(request, runtime)

    async def edit_quality_project_async(
        self,
        request: aiccs_20191015_models.EditQualityProjectRequest,
    ) -> aiccs_20191015_models.EditQualityProjectResponse:
        """
        @param request: EditQualityProjectRequest
        @return: EditQualityProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.edit_quality_project_with_options_async(request, runtime)

    def edit_quality_rule_with_options(
        self,
        request: aiccs_20191015_models.EditQualityRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.EditQualityRuleResponse:
        """
        @param request: EditQualityRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EditQualityRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.key_words):
            body['KeyWords'] = request.key_words
        if not UtilClient.is_unset(request.match_type):
            body['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.quality_rule_id):
            body['QualityRuleId'] = request.quality_rule_id
        if not UtilClient.is_unset(request.rule_tag):
            body['RuleTag'] = request.rule_tag
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EditQualityRule',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.EditQualityRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_quality_rule_with_options_async(
        self,
        request: aiccs_20191015_models.EditQualityRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.EditQualityRuleResponse:
        """
        @param request: EditQualityRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EditQualityRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.key_words):
            body['KeyWords'] = request.key_words
        if not UtilClient.is_unset(request.match_type):
            body['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.quality_rule_id):
            body['QualityRuleId'] = request.quality_rule_id
        if not UtilClient.is_unset(request.rule_tag):
            body['RuleTag'] = request.rule_tag
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EditQualityRule',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.EditQualityRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_quality_rule(
        self,
        request: aiccs_20191015_models.EditQualityRuleRequest,
    ) -> aiccs_20191015_models.EditQualityRuleResponse:
        """
        @param request: EditQualityRuleRequest
        @return: EditQualityRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.edit_quality_rule_with_options(request, runtime)

    async def edit_quality_rule_async(
        self,
        request: aiccs_20191015_models.EditQualityRuleRequest,
    ) -> aiccs_20191015_models.EditQualityRuleResponse:
        """
        @param request: EditQualityRuleRequest
        @return: EditQualityRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.edit_quality_rule_with_options_async(request, runtime)

    def edit_quality_rule_tag_with_options(
        self,
        request: aiccs_20191015_models.EditQualityRuleTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.EditQualityRuleTagResponse:
        """
        @param request: EditQualityRuleTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EditQualityRuleTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analysis_types):
            query['AnalysisTypes'] = request.analysis_types
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditQualityRuleTag',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.EditQualityRuleTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_quality_rule_tag_with_options_async(
        self,
        request: aiccs_20191015_models.EditQualityRuleTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.EditQualityRuleTagResponse:
        """
        @param request: EditQualityRuleTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EditQualityRuleTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analysis_types):
            query['AnalysisTypes'] = request.analysis_types
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditQualityRuleTag',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.EditQualityRuleTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_quality_rule_tag(
        self,
        request: aiccs_20191015_models.EditQualityRuleTagRequest,
    ) -> aiccs_20191015_models.EditQualityRuleTagResponse:
        """
        @param request: EditQualityRuleTagRequest
        @return: EditQualityRuleTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.edit_quality_rule_tag_with_options(request, runtime)

    async def edit_quality_rule_tag_async(
        self,
        request: aiccs_20191015_models.EditQualityRuleTagRequest,
    ) -> aiccs_20191015_models.EditQualityRuleTagResponse:
        """
        @param request: EditQualityRuleTagRequest
        @return: EditQualityRuleTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.edit_quality_rule_tag_with_options_async(request, runtime)

    def encrypt_phone_num_with_options(
        self,
        request: aiccs_20191015_models.EncryptPhoneNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.EncryptPhoneNumResponse:
        """
        @summary 热线号码加密
        
        @param request: EncryptPhoneNumRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EncryptPhoneNumResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EncryptPhoneNum',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.EncryptPhoneNumResponse(),
            self.call_api(params, req, runtime)
        )

    async def encrypt_phone_num_with_options_async(
        self,
        request: aiccs_20191015_models.EncryptPhoneNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.EncryptPhoneNumResponse:
        """
        @summary 热线号码加密
        
        @param request: EncryptPhoneNumRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EncryptPhoneNumResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EncryptPhoneNum',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.EncryptPhoneNumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def encrypt_phone_num(
        self,
        request: aiccs_20191015_models.EncryptPhoneNumRequest,
    ) -> aiccs_20191015_models.EncryptPhoneNumResponse:
        """
        @summary 热线号码加密
        
        @param request: EncryptPhoneNumRequest
        @return: EncryptPhoneNumResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.encrypt_phone_num_with_options(request, runtime)

    async def encrypt_phone_num_async(
        self,
        request: aiccs_20191015_models.EncryptPhoneNumRequest,
    ) -> aiccs_20191015_models.EncryptPhoneNumResponse:
        """
        @summary 热线号码加密
        
        @param request: EncryptPhoneNumRequest
        @return: EncryptPhoneNumResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.encrypt_phone_num_with_options_async(request, runtime)

    def fetch_call_with_options(
        self,
        request: aiccs_20191015_models.FetchCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.FetchCallResponse:
        """
        @param request: FetchCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FetchCallResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.call_id):
            body['CallId'] = request.call_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not UtilClient.is_unset(request.hold_connection_id):
            body['HoldConnectionId'] = request.hold_connection_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FetchCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.FetchCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def fetch_call_with_options_async(
        self,
        request: aiccs_20191015_models.FetchCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.FetchCallResponse:
        """
        @param request: FetchCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FetchCallResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.call_id):
            body['CallId'] = request.call_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not UtilClient.is_unset(request.hold_connection_id):
            body['HoldConnectionId'] = request.hold_connection_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FetchCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.FetchCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fetch_call(
        self,
        request: aiccs_20191015_models.FetchCallRequest,
    ) -> aiccs_20191015_models.FetchCallResponse:
        """
        @param request: FetchCallRequest
        @return: FetchCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.fetch_call_with_options(request, runtime)

    async def fetch_call_async(
        self,
        request: aiccs_20191015_models.FetchCallRequest,
    ) -> aiccs_20191015_models.FetchCallResponse:
        """
        @param request: FetchCallRequest
        @return: FetchCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.fetch_call_with_options_async(request, runtime)

    def finish_hotline_service_with_options(
        self,
        request: aiccs_20191015_models.FinishHotlineServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.FinishHotlineServiceResponse:
        """
        @param request: FinishHotlineServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FinishHotlineServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FinishHotlineService',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.FinishHotlineServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def finish_hotline_service_with_options_async(
        self,
        request: aiccs_20191015_models.FinishHotlineServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.FinishHotlineServiceResponse:
        """
        @param request: FinishHotlineServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FinishHotlineServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FinishHotlineService',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.FinishHotlineServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def finish_hotline_service(
        self,
        request: aiccs_20191015_models.FinishHotlineServiceRequest,
    ) -> aiccs_20191015_models.FinishHotlineServiceResponse:
        """
        @param request: FinishHotlineServiceRequest
        @return: FinishHotlineServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.finish_hotline_service_with_options(request, runtime)

    async def finish_hotline_service_async(
        self,
        request: aiccs_20191015_models.FinishHotlineServiceRequest,
    ) -> aiccs_20191015_models.FinishHotlineServiceResponse:
        """
        @param request: FinishHotlineServiceRequest
        @return: FinishHotlineServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.finish_hotline_service_with_options_async(request, runtime)

    def generate_web_socket_sign_with_options(
        self,
        request: aiccs_20191015_models.GenerateWebSocketSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GenerateWebSocketSignResponse:
        """
        @param request: GenerateWebSocketSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateWebSocketSignResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateWebSocketSign',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GenerateWebSocketSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_web_socket_sign_with_options_async(
        self,
        request: aiccs_20191015_models.GenerateWebSocketSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GenerateWebSocketSignResponse:
        """
        @param request: GenerateWebSocketSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateWebSocketSignResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateWebSocketSign',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GenerateWebSocketSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_web_socket_sign(
        self,
        request: aiccs_20191015_models.GenerateWebSocketSignRequest,
    ) -> aiccs_20191015_models.GenerateWebSocketSignResponse:
        """
        @param request: GenerateWebSocketSignRequest
        @return: GenerateWebSocketSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_web_socket_sign_with_options(request, runtime)

    async def generate_web_socket_sign_async(
        self,
        request: aiccs_20191015_models.GenerateWebSocketSignRequest,
    ) -> aiccs_20191015_models.GenerateWebSocketSignResponse:
        """
        @param request: GenerateWebSocketSignRequest
        @return: GenerateWebSocketSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_web_socket_sign_with_options_async(request, runtime)

    def get_agent_with_options(
        self,
        request: aiccs_20191015_models.GetAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentResponse:
        """
        @param request: GetAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgent',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_with_options_async(
        self,
        request: aiccs_20191015_models.GetAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentResponse:
        """
        @param request: GetAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgent',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent(
        self,
        request: aiccs_20191015_models.GetAgentRequest,
    ) -> aiccs_20191015_models.GetAgentResponse:
        """
        @param request: GetAgentRequest
        @return: GetAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_agent_with_options(request, runtime)

    async def get_agent_async(
        self,
        request: aiccs_20191015_models.GetAgentRequest,
    ) -> aiccs_20191015_models.GetAgentResponse:
        """
        @param request: GetAgentRequest
        @return: GetAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_with_options_async(request, runtime)

    def get_agent_basis_status_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetAgentBasisStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentBasisStatusResponse:
        """
        @summary 坐席纬度基础状态量
        
        @param tmp_req: GetAgentBasisStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentBasisStatusResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetAgentBasisStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgentBasisStatus',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentBasisStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_basis_status_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetAgentBasisStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentBasisStatusResponse:
        """
        @summary 坐席纬度基础状态量
        
        @param tmp_req: GetAgentBasisStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentBasisStatusResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetAgentBasisStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgentBasisStatus',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentBasisStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_basis_status(
        self,
        request: aiccs_20191015_models.GetAgentBasisStatusRequest,
    ) -> aiccs_20191015_models.GetAgentBasisStatusResponse:
        """
        @summary 坐席纬度基础状态量
        
        @param request: GetAgentBasisStatusRequest
        @return: GetAgentBasisStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_agent_basis_status_with_options(request, runtime)

    async def get_agent_basis_status_async(
        self,
        request: aiccs_20191015_models.GetAgentBasisStatusRequest,
    ) -> aiccs_20191015_models.GetAgentBasisStatusResponse:
        """
        @summary 坐席纬度基础状态量
        
        @param request: GetAgentBasisStatusRequest
        @return: GetAgentBasisStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_basis_status_with_options_async(request, runtime)

    def get_agent_by_id_with_options(
        self,
        request: aiccs_20191015_models.GetAgentByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentByIdResponse:
        """
        @param request: GetAgentByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentByIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_id):
            body['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAgentById',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_by_id_with_options_async(
        self,
        request: aiccs_20191015_models.GetAgentByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentByIdResponse:
        """
        @param request: GetAgentByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentByIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_id):
            body['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAgentById',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_by_id(
        self,
        request: aiccs_20191015_models.GetAgentByIdRequest,
    ) -> aiccs_20191015_models.GetAgentByIdResponse:
        """
        @param request: GetAgentByIdRequest
        @return: GetAgentByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_agent_by_id_with_options(request, runtime)

    async def get_agent_by_id_async(
        self,
        request: aiccs_20191015_models.GetAgentByIdRequest,
    ) -> aiccs_20191015_models.GetAgentByIdResponse:
        """
        @param request: GetAgentByIdRequest
        @return: GetAgentByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_by_id_with_options_async(request, runtime)

    def get_agent_detail_report_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetAgentDetailReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentDetailReportResponse:
        """
        @summary 热线坐席纬度详情汇总
        
        @param tmp_req: GetAgentDetailReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentDetailReportResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetAgentDetailReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgentDetailReport',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentDetailReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_detail_report_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetAgentDetailReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentDetailReportResponse:
        """
        @summary 热线坐席纬度详情汇总
        
        @param tmp_req: GetAgentDetailReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentDetailReportResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetAgentDetailReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgentDetailReport',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentDetailReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_detail_report(
        self,
        request: aiccs_20191015_models.GetAgentDetailReportRequest,
    ) -> aiccs_20191015_models.GetAgentDetailReportResponse:
        """
        @summary 热线坐席纬度详情汇总
        
        @param request: GetAgentDetailReportRequest
        @return: GetAgentDetailReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_agent_detail_report_with_options(request, runtime)

    async def get_agent_detail_report_async(
        self,
        request: aiccs_20191015_models.GetAgentDetailReportRequest,
    ) -> aiccs_20191015_models.GetAgentDetailReportResponse:
        """
        @summary 热线坐席纬度详情汇总
        
        @param request: GetAgentDetailReportRequest
        @return: GetAgentDetailReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_detail_report_with_options_async(request, runtime)

    def get_agent_index_real_time_with_options(
        self,
        request: aiccs_20191015_models.GetAgentIndexRealTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentIndexRealTimeResponse:
        """
        @param request: GetAgentIndexRealTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentIndexRealTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dep_ids):
            query['DepIds'] = request.dep_ids
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgentIndexRealTime',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentIndexRealTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_index_real_time_with_options_async(
        self,
        request: aiccs_20191015_models.GetAgentIndexRealTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentIndexRealTimeResponse:
        """
        @param request: GetAgentIndexRealTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentIndexRealTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dep_ids):
            query['DepIds'] = request.dep_ids
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgentIndexRealTime',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentIndexRealTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_index_real_time(
        self,
        request: aiccs_20191015_models.GetAgentIndexRealTimeRequest,
    ) -> aiccs_20191015_models.GetAgentIndexRealTimeResponse:
        """
        @param request: GetAgentIndexRealTimeRequest
        @return: GetAgentIndexRealTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_agent_index_real_time_with_options(request, runtime)

    async def get_agent_index_real_time_async(
        self,
        request: aiccs_20191015_models.GetAgentIndexRealTimeRequest,
    ) -> aiccs_20191015_models.GetAgentIndexRealTimeResponse:
        """
        @param request: GetAgentIndexRealTimeRequest
        @return: GetAgentIndexRealTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_index_real_time_with_options_async(request, runtime)

    def get_agent_service_status_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetAgentServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentServiceStatusResponse:
        """
        @summary 坐席服务状态量
        
        @param tmp_req: GetAgentServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentServiceStatusResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetAgentServiceStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgentServiceStatus',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_service_status_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetAgentServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentServiceStatusResponse:
        """
        @summary 坐席服务状态量
        
        @param tmp_req: GetAgentServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentServiceStatusResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetAgentServiceStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgentServiceStatus',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_service_status(
        self,
        request: aiccs_20191015_models.GetAgentServiceStatusRequest,
    ) -> aiccs_20191015_models.GetAgentServiceStatusResponse:
        """
        @summary 坐席服务状态量
        
        @param request: GetAgentServiceStatusRequest
        @return: GetAgentServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_agent_service_status_with_options(request, runtime)

    async def get_agent_service_status_async(
        self,
        request: aiccs_20191015_models.GetAgentServiceStatusRequest,
    ) -> aiccs_20191015_models.GetAgentServiceStatusResponse:
        """
        @summary 坐席服务状态量
        
        @param request: GetAgentServiceStatusRequest
        @return: GetAgentServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_service_status_with_options_async(request, runtime)

    def get_agent_statistics_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetAgentStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentStatisticsResponse:
        """
        @summary 坐席纬度统计量
        
        @param tmp_req: GetAgentStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentStatisticsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetAgentStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgentStatistics',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_statistics_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetAgentStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentStatisticsResponse:
        """
        @summary 坐席纬度统计量
        
        @param tmp_req: GetAgentStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentStatisticsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetAgentStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgentStatistics',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_statistics(
        self,
        request: aiccs_20191015_models.GetAgentStatisticsRequest,
    ) -> aiccs_20191015_models.GetAgentStatisticsResponse:
        """
        @summary 坐席纬度统计量
        
        @param request: GetAgentStatisticsRequest
        @return: GetAgentStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_agent_statistics_with_options(request, runtime)

    async def get_agent_statistics_async(
        self,
        request: aiccs_20191015_models.GetAgentStatisticsRequest,
    ) -> aiccs_20191015_models.GetAgentStatisticsResponse:
        """
        @summary 坐席纬度统计量
        
        @param request: GetAgentStatisticsRequest
        @return: GetAgentStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_statistics_with_options_async(request, runtime)

    def get_ai_outbound_task_biz_data_with_options(
        self,
        request: aiccs_20191015_models.GetAiOutboundTaskBizDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAiOutboundTaskBizDataResponse:
        """
        @summary 获取智能外呼任务业务自定义信息
        
        @param request: GetAiOutboundTaskBizDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAiOutboundTaskBizDataResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAiOutboundTaskBizData',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAiOutboundTaskBizDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ai_outbound_task_biz_data_with_options_async(
        self,
        request: aiccs_20191015_models.GetAiOutboundTaskBizDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAiOutboundTaskBizDataResponse:
        """
        @summary 获取智能外呼任务业务自定义信息
        
        @param request: GetAiOutboundTaskBizDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAiOutboundTaskBizDataResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAiOutboundTaskBizData',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAiOutboundTaskBizDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ai_outbound_task_biz_data(
        self,
        request: aiccs_20191015_models.GetAiOutboundTaskBizDataRequest,
    ) -> aiccs_20191015_models.GetAiOutboundTaskBizDataResponse:
        """
        @summary 获取智能外呼任务业务自定义信息
        
        @param request: GetAiOutboundTaskBizDataRequest
        @return: GetAiOutboundTaskBizDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ai_outbound_task_biz_data_with_options(request, runtime)

    async def get_ai_outbound_task_biz_data_async(
        self,
        request: aiccs_20191015_models.GetAiOutboundTaskBizDataRequest,
    ) -> aiccs_20191015_models.GetAiOutboundTaskBizDataResponse:
        """
        @summary 获取智能外呼任务业务自定义信息
        
        @param request: GetAiOutboundTaskBizDataRequest
        @return: GetAiOutboundTaskBizDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ai_outbound_task_biz_data_with_options_async(request, runtime)

    def get_ai_outbound_task_detail_with_options(
        self,
        request: aiccs_20191015_models.GetAiOutboundTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAiOutboundTaskDetailResponse:
        """
        @summary 智能外呼任务配置详情查询
        
        @param request: GetAiOutboundTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAiOutboundTaskDetailResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAiOutboundTaskDetail',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAiOutboundTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ai_outbound_task_detail_with_options_async(
        self,
        request: aiccs_20191015_models.GetAiOutboundTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAiOutboundTaskDetailResponse:
        """
        @summary 智能外呼任务配置详情查询
        
        @param request: GetAiOutboundTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAiOutboundTaskDetailResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAiOutboundTaskDetail',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAiOutboundTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ai_outbound_task_detail(
        self,
        request: aiccs_20191015_models.GetAiOutboundTaskDetailRequest,
    ) -> aiccs_20191015_models.GetAiOutboundTaskDetailResponse:
        """
        @summary 智能外呼任务配置详情查询
        
        @param request: GetAiOutboundTaskDetailRequest
        @return: GetAiOutboundTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ai_outbound_task_detail_with_options(request, runtime)

    async def get_ai_outbound_task_detail_async(
        self,
        request: aiccs_20191015_models.GetAiOutboundTaskDetailRequest,
    ) -> aiccs_20191015_models.GetAiOutboundTaskDetailResponse:
        """
        @summary 智能外呼任务配置详情查询
        
        @param request: GetAiOutboundTaskDetailRequest
        @return: GetAiOutboundTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ai_outbound_task_detail_with_options_async(request, runtime)

    def get_ai_outbound_task_exec_detail_with_options(
        self,
        request: aiccs_20191015_models.GetAiOutboundTaskExecDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAiOutboundTaskExecDetailResponse:
        """
        @summary 智能外呼任务执行详情
        
        @param request: GetAiOutboundTaskExecDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAiOutboundTaskExecDetailResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAiOutboundTaskExecDetail',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAiOutboundTaskExecDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ai_outbound_task_exec_detail_with_options_async(
        self,
        request: aiccs_20191015_models.GetAiOutboundTaskExecDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAiOutboundTaskExecDetailResponse:
        """
        @summary 智能外呼任务执行详情
        
        @param request: GetAiOutboundTaskExecDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAiOutboundTaskExecDetailResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAiOutboundTaskExecDetail',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAiOutboundTaskExecDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ai_outbound_task_exec_detail(
        self,
        request: aiccs_20191015_models.GetAiOutboundTaskExecDetailRequest,
    ) -> aiccs_20191015_models.GetAiOutboundTaskExecDetailResponse:
        """
        @summary 智能外呼任务执行详情
        
        @param request: GetAiOutboundTaskExecDetailRequest
        @return: GetAiOutboundTaskExecDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ai_outbound_task_exec_detail_with_options(request, runtime)

    async def get_ai_outbound_task_exec_detail_async(
        self,
        request: aiccs_20191015_models.GetAiOutboundTaskExecDetailRequest,
    ) -> aiccs_20191015_models.GetAiOutboundTaskExecDetailResponse:
        """
        @summary 智能外呼任务执行详情
        
        @param request: GetAiOutboundTaskExecDetailRequest
        @return: GetAiOutboundTaskExecDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ai_outbound_task_exec_detail_with_options_async(request, runtime)

    def get_ai_outbound_task_list_with_options(
        self,
        request: aiccs_20191015_models.GetAiOutboundTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAiOutboundTaskListResponse:
        """
        @summary 智能外呼任务列表查询
        
        @param request: GetAiOutboundTaskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAiOutboundTaskListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAiOutboundTaskList',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAiOutboundTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ai_outbound_task_list_with_options_async(
        self,
        request: aiccs_20191015_models.GetAiOutboundTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAiOutboundTaskListResponse:
        """
        @summary 智能外呼任务列表查询
        
        @param request: GetAiOutboundTaskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAiOutboundTaskListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAiOutboundTaskList',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAiOutboundTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ai_outbound_task_list(
        self,
        request: aiccs_20191015_models.GetAiOutboundTaskListRequest,
    ) -> aiccs_20191015_models.GetAiOutboundTaskListResponse:
        """
        @summary 智能外呼任务列表查询
        
        @param request: GetAiOutboundTaskListRequest
        @return: GetAiOutboundTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ai_outbound_task_list_with_options(request, runtime)

    async def get_ai_outbound_task_list_async(
        self,
        request: aiccs_20191015_models.GetAiOutboundTaskListRequest,
    ) -> aiccs_20191015_models.GetAiOutboundTaskListResponse:
        """
        @summary 智能外呼任务列表查询
        
        @param request: GetAiOutboundTaskListRequest
        @return: GetAiOutboundTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ai_outbound_task_list_with_options_async(request, runtime)

    def get_ai_outbound_task_progress_with_options(
        self,
        request: aiccs_20191015_models.GetAiOutboundTaskProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAiOutboundTaskProgressResponse:
        """
        @summary 智能外呼任务执行进度
        
        @param request: GetAiOutboundTaskProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAiOutboundTaskProgressResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAiOutboundTaskProgress',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAiOutboundTaskProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ai_outbound_task_progress_with_options_async(
        self,
        request: aiccs_20191015_models.GetAiOutboundTaskProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAiOutboundTaskProgressResponse:
        """
        @summary 智能外呼任务执行进度
        
        @param request: GetAiOutboundTaskProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAiOutboundTaskProgressResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAiOutboundTaskProgress',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAiOutboundTaskProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ai_outbound_task_progress(
        self,
        request: aiccs_20191015_models.GetAiOutboundTaskProgressRequest,
    ) -> aiccs_20191015_models.GetAiOutboundTaskProgressResponse:
        """
        @summary 智能外呼任务执行进度
        
        @param request: GetAiOutboundTaskProgressRequest
        @return: GetAiOutboundTaskProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ai_outbound_task_progress_with_options(request, runtime)

    async def get_ai_outbound_task_progress_async(
        self,
        request: aiccs_20191015_models.GetAiOutboundTaskProgressRequest,
    ) -> aiccs_20191015_models.GetAiOutboundTaskProgressResponse:
        """
        @summary 智能外呼任务执行进度
        
        @param request: GetAiOutboundTaskProgressRequest
        @return: GetAiOutboundTaskProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ai_outbound_task_progress_with_options_async(request, runtime)

    def get_all_department_with_options(
        self,
        request: aiccs_20191015_models.GetAllDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAllDepartmentResponse:
        """
        @summary getAllDepartment
        
        @param request: GetAllDepartmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAllDepartmentResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAllDepartment',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAllDepartmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_all_department_with_options_async(
        self,
        request: aiccs_20191015_models.GetAllDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAllDepartmentResponse:
        """
        @summary getAllDepartment
        
        @param request: GetAllDepartmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAllDepartmentResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAllDepartment',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAllDepartmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_all_department(
        self,
        request: aiccs_20191015_models.GetAllDepartmentRequest,
    ) -> aiccs_20191015_models.GetAllDepartmentResponse:
        """
        @summary getAllDepartment
        
        @param request: GetAllDepartmentRequest
        @return: GetAllDepartmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_all_department_with_options(request, runtime)

    async def get_all_department_async(
        self,
        request: aiccs_20191015_models.GetAllDepartmentRequest,
    ) -> aiccs_20191015_models.GetAllDepartmentResponse:
        """
        @summary getAllDepartment
        
        @param request: GetAllDepartmentRequest
        @return: GetAllDepartmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_all_department_with_options_async(request, runtime)

    def get_call_dialog_content_with_options(
        self,
        request: aiccs_20191015_models.GetCallDialogContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetCallDialogContentResponse:
        """
        @summary 查询对话内容
        
        @param request: GetCallDialogContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCallDialogContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_date):
            query['CallDate'] = request.call_date
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCallDialogContent',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetCallDialogContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_call_dialog_content_with_options_async(
        self,
        request: aiccs_20191015_models.GetCallDialogContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetCallDialogContentResponse:
        """
        @summary 查询对话内容
        
        @param request: GetCallDialogContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCallDialogContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_date):
            query['CallDate'] = request.call_date
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCallDialogContent',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetCallDialogContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_call_dialog_content(
        self,
        request: aiccs_20191015_models.GetCallDialogContentRequest,
    ) -> aiccs_20191015_models.GetCallDialogContentResponse:
        """
        @summary 查询对话内容
        
        @param request: GetCallDialogContentRequest
        @return: GetCallDialogContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_call_dialog_content_with_options(request, runtime)

    async def get_call_dialog_content_async(
        self,
        request: aiccs_20191015_models.GetCallDialogContentRequest,
    ) -> aiccs_20191015_models.GetCallDialogContentResponse:
        """
        @summary 查询对话内容
        
        @param request: GetCallDialogContentRequest
        @return: GetCallDialogContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_call_dialog_content_with_options_async(request, runtime)

    def get_call_sound_record_with_options(
        self,
        request: aiccs_20191015_models.GetCallSoundRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetCallSoundRecordResponse:
        """
        @summary 获取通话录音文件
        
        @param request: GetCallSoundRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCallSoundRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.create_time):
            query['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCallSoundRecord',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetCallSoundRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_call_sound_record_with_options_async(
        self,
        request: aiccs_20191015_models.GetCallSoundRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetCallSoundRecordResponse:
        """
        @summary 获取通话录音文件
        
        @param request: GetCallSoundRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCallSoundRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.create_time):
            query['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCallSoundRecord',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetCallSoundRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_call_sound_record(
        self,
        request: aiccs_20191015_models.GetCallSoundRecordRequest,
    ) -> aiccs_20191015_models.GetCallSoundRecordResponse:
        """
        @summary 获取通话录音文件
        
        @param request: GetCallSoundRecordRequest
        @return: GetCallSoundRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_call_sound_record_with_options(request, runtime)

    async def get_call_sound_record_async(
        self,
        request: aiccs_20191015_models.GetCallSoundRecordRequest,
    ) -> aiccs_20191015_models.GetCallSoundRecordResponse:
        """
        @summary 获取通话录音文件
        
        @param request: GetCallSoundRecordRequest
        @return: GetCallSoundRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_call_sound_record_with_options_async(request, runtime)

    def get_config_num_list_with_options(
        self,
        request: aiccs_20191015_models.GetConfigNumListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetConfigNumListResponse:
        """
        @summary 获取热线配置号码列表
        
        @param request: GetConfigNumListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConfigNumListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConfigNumList',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetConfigNumListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_config_num_list_with_options_async(
        self,
        request: aiccs_20191015_models.GetConfigNumListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetConfigNumListResponse:
        """
        @summary 获取热线配置号码列表
        
        @param request: GetConfigNumListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConfigNumListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConfigNumList',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetConfigNumListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_config_num_list(
        self,
        request: aiccs_20191015_models.GetConfigNumListRequest,
    ) -> aiccs_20191015_models.GetConfigNumListResponse:
        """
        @summary 获取热线配置号码列表
        
        @param request: GetConfigNumListRequest
        @return: GetConfigNumListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_config_num_list_with_options(request, runtime)

    async def get_config_num_list_async(
        self,
        request: aiccs_20191015_models.GetConfigNumListRequest,
    ) -> aiccs_20191015_models.GetConfigNumListResponse:
        """
        @summary 获取热线配置号码列表
        
        @param request: GetConfigNumListRequest
        @return: GetConfigNumListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_config_num_list_with_options_async(request, runtime)

    def get_customer_info_with_options(
        self,
        request: aiccs_20191015_models.GetCustomerInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetCustomerInfoResponse:
        """
        @summary 获取会员信息
        
        @param request: GetCustomerInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomerInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomerInfo',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetCustomerInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_customer_info_with_options_async(
        self,
        request: aiccs_20191015_models.GetCustomerInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetCustomerInfoResponse:
        """
        @summary 获取会员信息
        
        @param request: GetCustomerInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomerInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomerInfo',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetCustomerInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_customer_info(
        self,
        request: aiccs_20191015_models.GetCustomerInfoRequest,
    ) -> aiccs_20191015_models.GetCustomerInfoResponse:
        """
        @summary 获取会员信息
        
        @param request: GetCustomerInfoRequest
        @return: GetCustomerInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_customer_info_with_options(request, runtime)

    async def get_customer_info_async(
        self,
        request: aiccs_20191015_models.GetCustomerInfoRequest,
    ) -> aiccs_20191015_models.GetCustomerInfoResponse:
        """
        @summary 获取会员信息
        
        @param request: GetCustomerInfoRequest
        @return: GetCustomerInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_customer_info_with_options_async(request, runtime)

    def get_dep_group_tree_data_with_options(
        self,
        request: aiccs_20191015_models.GetDepGroupTreeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetDepGroupTreeDataResponse:
        """
        @summary 获取技能组分组
        
        @param request: GetDepGroupTreeDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDepGroupTreeDataResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDepGroupTreeData',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetDepGroupTreeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dep_group_tree_data_with_options_async(
        self,
        request: aiccs_20191015_models.GetDepGroupTreeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetDepGroupTreeDataResponse:
        """
        @summary 获取技能组分组
        
        @param request: GetDepGroupTreeDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDepGroupTreeDataResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDepGroupTreeData',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetDepGroupTreeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dep_group_tree_data(
        self,
        request: aiccs_20191015_models.GetDepGroupTreeDataRequest,
    ) -> aiccs_20191015_models.GetDepGroupTreeDataResponse:
        """
        @summary 获取技能组分组
        
        @param request: GetDepGroupTreeDataRequest
        @return: GetDepGroupTreeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dep_group_tree_data_with_options(request, runtime)

    async def get_dep_group_tree_data_async(
        self,
        request: aiccs_20191015_models.GetDepGroupTreeDataRequest,
    ) -> aiccs_20191015_models.GetDepGroupTreeDataResponse:
        """
        @summary 获取技能组分组
        
        @param request: GetDepGroupTreeDataRequest
        @return: GetDepGroupTreeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_dep_group_tree_data_with_options_async(request, runtime)

    def get_departmental_latitude_agent_status_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusResponse:
        """
        @summary 部门纬度坐席状态量
        
        @param tmp_req: GetDepartmentalLatitudeAgentStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDepartmentalLatitudeAgentStatusResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDepartmentalLatitudeAgentStatus',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_departmental_latitude_agent_status_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusResponse:
        """
        @summary 部门纬度坐席状态量
        
        @param tmp_req: GetDepartmentalLatitudeAgentStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDepartmentalLatitudeAgentStatusResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDepartmentalLatitudeAgentStatus',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_departmental_latitude_agent_status(
        self,
        request: aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusRequest,
    ) -> aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusResponse:
        """
        @summary 部门纬度坐席状态量
        
        @param request: GetDepartmentalLatitudeAgentStatusRequest
        @return: GetDepartmentalLatitudeAgentStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_departmental_latitude_agent_status_with_options(request, runtime)

    async def get_departmental_latitude_agent_status_async(
        self,
        request: aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusRequest,
    ) -> aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusResponse:
        """
        @summary 部门纬度坐席状态量
        
        @param request: GetDepartmentalLatitudeAgentStatusRequest
        @return: GetDepartmentalLatitudeAgentStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_departmental_latitude_agent_status_with_options_async(request, runtime)

    def get_hotline_agent_detail_with_options(
        self,
        request: aiccs_20191015_models.GetHotlineAgentDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineAgentDetailResponse:
        """
        @param request: GetHotlineAgentDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotlineAgentDetailResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotlineAgentDetail',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineAgentDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotline_agent_detail_with_options_async(
        self,
        request: aiccs_20191015_models.GetHotlineAgentDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineAgentDetailResponse:
        """
        @param request: GetHotlineAgentDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotlineAgentDetailResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotlineAgentDetail',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineAgentDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotline_agent_detail(
        self,
        request: aiccs_20191015_models.GetHotlineAgentDetailRequest,
    ) -> aiccs_20191015_models.GetHotlineAgentDetailResponse:
        """
        @param request: GetHotlineAgentDetailRequest
        @return: GetHotlineAgentDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_agent_detail_with_options(request, runtime)

    async def get_hotline_agent_detail_async(
        self,
        request: aiccs_20191015_models.GetHotlineAgentDetailRequest,
    ) -> aiccs_20191015_models.GetHotlineAgentDetailResponse:
        """
        @param request: GetHotlineAgentDetailRequest
        @return: GetHotlineAgentDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_agent_detail_with_options_async(request, runtime)

    def get_hotline_agent_detail_report_with_options(
        self,
        request: aiccs_20191015_models.GetHotlineAgentDetailReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineAgentDetailReportResponse:
        """
        @param request: GetHotlineAgentDetailReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotlineAgentDetailReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dep_ids):
            query['DepIds'] = request.dep_ids
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotlineAgentDetailReport',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineAgentDetailReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotline_agent_detail_report_with_options_async(
        self,
        request: aiccs_20191015_models.GetHotlineAgentDetailReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineAgentDetailReportResponse:
        """
        @param request: GetHotlineAgentDetailReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotlineAgentDetailReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dep_ids):
            query['DepIds'] = request.dep_ids
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotlineAgentDetailReport',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineAgentDetailReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotline_agent_detail_report(
        self,
        request: aiccs_20191015_models.GetHotlineAgentDetailReportRequest,
    ) -> aiccs_20191015_models.GetHotlineAgentDetailReportResponse:
        """
        @param request: GetHotlineAgentDetailReportRequest
        @return: GetHotlineAgentDetailReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_agent_detail_report_with_options(request, runtime)

    async def get_hotline_agent_detail_report_async(
        self,
        request: aiccs_20191015_models.GetHotlineAgentDetailReportRequest,
    ) -> aiccs_20191015_models.GetHotlineAgentDetailReportResponse:
        """
        @param request: GetHotlineAgentDetailReportRequest
        @return: GetHotlineAgentDetailReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_agent_detail_report_with_options_async(request, runtime)

    def get_hotline_agent_status_with_options(
        self,
        request: aiccs_20191015_models.GetHotlineAgentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineAgentStatusResponse:
        """
        @param request: GetHotlineAgentStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotlineAgentStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotlineAgentStatus',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineAgentStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotline_agent_status_with_options_async(
        self,
        request: aiccs_20191015_models.GetHotlineAgentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineAgentStatusResponse:
        """
        @param request: GetHotlineAgentStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotlineAgentStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotlineAgentStatus',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineAgentStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotline_agent_status(
        self,
        request: aiccs_20191015_models.GetHotlineAgentStatusRequest,
    ) -> aiccs_20191015_models.GetHotlineAgentStatusResponse:
        """
        @param request: GetHotlineAgentStatusRequest
        @return: GetHotlineAgentStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_agent_status_with_options(request, runtime)

    async def get_hotline_agent_status_async(
        self,
        request: aiccs_20191015_models.GetHotlineAgentStatusRequest,
    ) -> aiccs_20191015_models.GetHotlineAgentStatusResponse:
        """
        @param request: GetHotlineAgentStatusRequest
        @return: GetHotlineAgentStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_agent_status_with_options_async(request, runtime)

    def get_hotline_call_action_with_options(
        self,
        request: aiccs_20191015_models.GetHotlineCallActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineCallActionResponse:
        """
        @summary 查询话务动作结果数据
        
        @param request: GetHotlineCallActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotlineCallActionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.acc):
            body['Acc'] = request.acc
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.act):
            body['Act'] = request.act
        if not UtilClient.is_unset(request.biz):
            body['Biz'] = request.biz
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.from_source):
            body['FromSource'] = request.from_source
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotlineCallAction',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineCallActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotline_call_action_with_options_async(
        self,
        request: aiccs_20191015_models.GetHotlineCallActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineCallActionResponse:
        """
        @summary 查询话务动作结果数据
        
        @param request: GetHotlineCallActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotlineCallActionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.acc):
            body['Acc'] = request.acc
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.act):
            body['Act'] = request.act
        if not UtilClient.is_unset(request.biz):
            body['Biz'] = request.biz
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.from_source):
            body['FromSource'] = request.from_source
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotlineCallAction',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineCallActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotline_call_action(
        self,
        request: aiccs_20191015_models.GetHotlineCallActionRequest,
    ) -> aiccs_20191015_models.GetHotlineCallActionResponse:
        """
        @summary 查询话务动作结果数据
        
        @param request: GetHotlineCallActionRequest
        @return: GetHotlineCallActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_call_action_with_options(request, runtime)

    async def get_hotline_call_action_async(
        self,
        request: aiccs_20191015_models.GetHotlineCallActionRequest,
    ) -> aiccs_20191015_models.GetHotlineCallActionResponse:
        """
        @summary 查询话务动作结果数据
        
        @param request: GetHotlineCallActionRequest
        @return: GetHotlineCallActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_call_action_with_options_async(request, runtime)

    def get_hotline_group_detail_report_with_options(
        self,
        request: aiccs_20191015_models.GetHotlineGroupDetailReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineGroupDetailReportResponse:
        """
        @param request: GetHotlineGroupDetailReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotlineGroupDetailReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dep_ids):
            query['DepIds'] = request.dep_ids
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotlineGroupDetailReport',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineGroupDetailReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotline_group_detail_report_with_options_async(
        self,
        request: aiccs_20191015_models.GetHotlineGroupDetailReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineGroupDetailReportResponse:
        """
        @param request: GetHotlineGroupDetailReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotlineGroupDetailReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dep_ids):
            query['DepIds'] = request.dep_ids
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotlineGroupDetailReport',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineGroupDetailReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotline_group_detail_report(
        self,
        request: aiccs_20191015_models.GetHotlineGroupDetailReportRequest,
    ) -> aiccs_20191015_models.GetHotlineGroupDetailReportResponse:
        """
        @param request: GetHotlineGroupDetailReportRequest
        @return: GetHotlineGroupDetailReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_group_detail_report_with_options(request, runtime)

    async def get_hotline_group_detail_report_async(
        self,
        request: aiccs_20191015_models.GetHotlineGroupDetailReportRequest,
    ) -> aiccs_20191015_models.GetHotlineGroupDetailReportResponse:
        """
        @param request: GetHotlineGroupDetailReportRequest
        @return: GetHotlineGroupDetailReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_group_detail_report_with_options_async(request, runtime)

    def get_hotline_message_log_with_options(
        self,
        request: aiccs_20191015_models.GetHotlineMessageLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineMessageLogResponse:
        """
        @summary 获取热线聊天记录
        
        @param request: GetHotlineMessageLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotlineMessageLogResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotlineMessageLog',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineMessageLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotline_message_log_with_options_async(
        self,
        request: aiccs_20191015_models.GetHotlineMessageLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineMessageLogResponse:
        """
        @summary 获取热线聊天记录
        
        @param request: GetHotlineMessageLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotlineMessageLogResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotlineMessageLog',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineMessageLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotline_message_log(
        self,
        request: aiccs_20191015_models.GetHotlineMessageLogRequest,
    ) -> aiccs_20191015_models.GetHotlineMessageLogResponse:
        """
        @summary 获取热线聊天记录
        
        @param request: GetHotlineMessageLogRequest
        @return: GetHotlineMessageLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_message_log_with_options(request, runtime)

    async def get_hotline_message_log_async(
        self,
        request: aiccs_20191015_models.GetHotlineMessageLogRequest,
    ) -> aiccs_20191015_models.GetHotlineMessageLogResponse:
        """
        @summary 获取热线聊天记录
        
        @param request: GetHotlineMessageLogRequest
        @return: GetHotlineMessageLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_message_log_with_options_async(request, runtime)

    def get_hotline_runtime_info_with_options(
        self,
        request: aiccs_20191015_models.GetHotlineRuntimeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineRuntimeInfoResponse:
        """
        @summary 获取热线当前信息
        
        @param request: GetHotlineRuntimeInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotlineRuntimeInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotlineRuntimeInfo',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineRuntimeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotline_runtime_info_with_options_async(
        self,
        request: aiccs_20191015_models.GetHotlineRuntimeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineRuntimeInfoResponse:
        """
        @summary 获取热线当前信息
        
        @param request: GetHotlineRuntimeInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotlineRuntimeInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotlineRuntimeInfo',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineRuntimeInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotline_runtime_info(
        self,
        request: aiccs_20191015_models.GetHotlineRuntimeInfoRequest,
    ) -> aiccs_20191015_models.GetHotlineRuntimeInfoResponse:
        """
        @summary 获取热线当前信息
        
        @param request: GetHotlineRuntimeInfoRequest
        @return: GetHotlineRuntimeInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_runtime_info_with_options(request, runtime)

    async def get_hotline_runtime_info_async(
        self,
        request: aiccs_20191015_models.GetHotlineRuntimeInfoRequest,
    ) -> aiccs_20191015_models.GetHotlineRuntimeInfoResponse:
        """
        @summary 获取热线当前信息
        
        @param request: GetHotlineRuntimeInfoRequest
        @return: GetHotlineRuntimeInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_runtime_info_with_options_async(request, runtime)

    def get_hotline_service_statistics_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetHotlineServiceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineServiceStatisticsResponse:
        """
        @summary 服务统计量数据
        
        @param tmp_req: GetHotlineServiceStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotlineServiceStatisticsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetHotlineServiceStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotlineServiceStatistics',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineServiceStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotline_service_statistics_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetHotlineServiceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineServiceStatisticsResponse:
        """
        @summary 服务统计量数据
        
        @param tmp_req: GetHotlineServiceStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotlineServiceStatisticsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetHotlineServiceStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotlineServiceStatistics',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineServiceStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotline_service_statistics(
        self,
        request: aiccs_20191015_models.GetHotlineServiceStatisticsRequest,
    ) -> aiccs_20191015_models.GetHotlineServiceStatisticsResponse:
        """
        @summary 服务统计量数据
        
        @param request: GetHotlineServiceStatisticsRequest
        @return: GetHotlineServiceStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_service_statistics_with_options(request, runtime)

    async def get_hotline_service_statistics_async(
        self,
        request: aiccs_20191015_models.GetHotlineServiceStatisticsRequest,
    ) -> aiccs_20191015_models.GetHotlineServiceStatisticsResponse:
        """
        @summary 服务统计量数据
        
        @param request: GetHotlineServiceStatisticsRequest
        @return: GetHotlineServiceStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_service_statistics_with_options_async(request, runtime)

    def get_hotline_waiting_number_with_options(
        self,
        request: aiccs_20191015_models.GetHotlineWaitingNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineWaitingNumberResponse:
        """
        @param request: GetHotlineWaitingNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotlineWaitingNumberResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotlineWaitingNumber',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineWaitingNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotline_waiting_number_with_options_async(
        self,
        request: aiccs_20191015_models.GetHotlineWaitingNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineWaitingNumberResponse:
        """
        @param request: GetHotlineWaitingNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotlineWaitingNumberResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotlineWaitingNumber',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineWaitingNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotline_waiting_number(
        self,
        request: aiccs_20191015_models.GetHotlineWaitingNumberRequest,
    ) -> aiccs_20191015_models.GetHotlineWaitingNumberResponse:
        """
        @param request: GetHotlineWaitingNumberRequest
        @return: GetHotlineWaitingNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_waiting_number_with_options(request, runtime)

    async def get_hotline_waiting_number_async(
        self,
        request: aiccs_20191015_models.GetHotlineWaitingNumberRequest,
    ) -> aiccs_20191015_models.GetHotlineWaitingNumberResponse:
        """
        @param request: GetHotlineWaitingNumberRequest
        @return: GetHotlineWaitingNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_waiting_number_with_options_async(request, runtime)

    def get_index_current_value_with_options(
        self,
        request: aiccs_20191015_models.GetIndexCurrentValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetIndexCurrentValueResponse:
        """
        @param request: GetIndexCurrentValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIndexCurrentValueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dep_ids):
            query['DepIds'] = request.dep_ids
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIndexCurrentValue',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetIndexCurrentValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_index_current_value_with_options_async(
        self,
        request: aiccs_20191015_models.GetIndexCurrentValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetIndexCurrentValueResponse:
        """
        @param request: GetIndexCurrentValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIndexCurrentValueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dep_ids):
            query['DepIds'] = request.dep_ids
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIndexCurrentValue',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetIndexCurrentValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_index_current_value(
        self,
        request: aiccs_20191015_models.GetIndexCurrentValueRequest,
    ) -> aiccs_20191015_models.GetIndexCurrentValueResponse:
        """
        @param request: GetIndexCurrentValueRequest
        @return: GetIndexCurrentValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_index_current_value_with_options(request, runtime)

    async def get_index_current_value_async(
        self,
        request: aiccs_20191015_models.GetIndexCurrentValueRequest,
    ) -> aiccs_20191015_models.GetIndexCurrentValueResponse:
        """
        @param request: GetIndexCurrentValueRequest
        @return: GetIndexCurrentValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_index_current_value_with_options_async(request, runtime)

    def get_instance_list_with_options(
        self,
        request: aiccs_20191015_models.GetInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetInstanceListResponse:
        """
        @param request: GetInstanceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInstanceList',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_list_with_options_async(
        self,
        request: aiccs_20191015_models.GetInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetInstanceListResponse:
        """
        @param request: GetInstanceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInstanceList',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_list(
        self,
        request: aiccs_20191015_models.GetInstanceListRequest,
    ) -> aiccs_20191015_models.GetInstanceListResponse:
        """
        @param request: GetInstanceListRequest
        @return: GetInstanceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_list_with_options(request, runtime)

    async def get_instance_list_async(
        self,
        request: aiccs_20191015_models.GetInstanceListRequest,
    ) -> aiccs_20191015_models.GetInstanceListResponse:
        """
        @param request: GetInstanceListRequest
        @return: GetInstanceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_list_with_options_async(request, runtime)

    def get_mcu_lvs_ip_with_options(
        self,
        request: aiccs_20191015_models.GetMcuLvsIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetMcuLvsIpResponse:
        """
        @summary 热线检测获取mcu ip地址
        
        @param request: GetMcuLvsIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMcuLvsIpResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMcuLvsIp',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetMcuLvsIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mcu_lvs_ip_with_options_async(
        self,
        request: aiccs_20191015_models.GetMcuLvsIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetMcuLvsIpResponse:
        """
        @summary 热线检测获取mcu ip地址
        
        @param request: GetMcuLvsIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMcuLvsIpResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMcuLvsIp',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetMcuLvsIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mcu_lvs_ip(
        self,
        request: aiccs_20191015_models.GetMcuLvsIpRequest,
    ) -> aiccs_20191015_models.GetMcuLvsIpResponse:
        """
        @summary 热线检测获取mcu ip地址
        
        @param request: GetMcuLvsIpRequest
        @return: GetMcuLvsIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_mcu_lvs_ip_with_options(request, runtime)

    async def get_mcu_lvs_ip_async(
        self,
        request: aiccs_20191015_models.GetMcuLvsIpRequest,
    ) -> aiccs_20191015_models.GetMcuLvsIpResponse:
        """
        @summary 热线检测获取mcu ip地址
        
        @param request: GetMcuLvsIpRequest
        @return: GetMcuLvsIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_mcu_lvs_ip_with_options_async(request, runtime)

    def get_num_location_with_options(
        self,
        request: aiccs_20191015_models.GetNumLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetNumLocationResponse:
        """
        @param request: GetNumLocationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNumLocationResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNumLocation',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetNumLocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_num_location_with_options_async(
        self,
        request: aiccs_20191015_models.GetNumLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetNumLocationResponse:
        """
        @param request: GetNumLocationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNumLocationResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNumLocation',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetNumLocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_num_location(
        self,
        request: aiccs_20191015_models.GetNumLocationRequest,
    ) -> aiccs_20191015_models.GetNumLocationResponse:
        """
        @param request: GetNumLocationRequest
        @return: GetNumLocationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_num_location_with_options(request, runtime)

    async def get_num_location_async(
        self,
        request: aiccs_20191015_models.GetNumLocationRequest,
    ) -> aiccs_20191015_models.GetNumLocationResponse:
        """
        @param request: GetNumLocationRequest
        @return: GetNumLocationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_num_location_with_options_async(request, runtime)

    def get_online_seat_information_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetOnlineSeatInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetOnlineSeatInformationResponse:
        """
        @summary 在线坐席信息
        
        @param tmp_req: GetOnlineSeatInformationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOnlineSeatInformationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetOnlineSeatInformationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOnlineSeatInformation',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetOnlineSeatInformationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_online_seat_information_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetOnlineSeatInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetOnlineSeatInformationResponse:
        """
        @summary 在线坐席信息
        
        @param tmp_req: GetOnlineSeatInformationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOnlineSeatInformationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetOnlineSeatInformationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOnlineSeatInformation',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetOnlineSeatInformationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_online_seat_information(
        self,
        request: aiccs_20191015_models.GetOnlineSeatInformationRequest,
    ) -> aiccs_20191015_models.GetOnlineSeatInformationResponse:
        """
        @summary 在线坐席信息
        
        @param request: GetOnlineSeatInformationRequest
        @return: GetOnlineSeatInformationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_online_seat_information_with_options(request, runtime)

    async def get_online_seat_information_async(
        self,
        request: aiccs_20191015_models.GetOnlineSeatInformationRequest,
    ) -> aiccs_20191015_models.GetOnlineSeatInformationResponse:
        """
        @summary 在线坐席信息
        
        @param request: GetOnlineSeatInformationRequest
        @return: GetOnlineSeatInformationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_online_seat_information_with_options_async(request, runtime)

    def get_online_service_volume_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetOnlineServiceVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetOnlineServiceVolumeResponse:
        """
        @summary 在线服务总量
        
        @param tmp_req: GetOnlineServiceVolumeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOnlineServiceVolumeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetOnlineServiceVolumeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOnlineServiceVolume',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetOnlineServiceVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_online_service_volume_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetOnlineServiceVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetOnlineServiceVolumeResponse:
        """
        @summary 在线服务总量
        
        @param tmp_req: GetOnlineServiceVolumeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOnlineServiceVolumeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetOnlineServiceVolumeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOnlineServiceVolume',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetOnlineServiceVolumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_online_service_volume(
        self,
        request: aiccs_20191015_models.GetOnlineServiceVolumeRequest,
    ) -> aiccs_20191015_models.GetOnlineServiceVolumeResponse:
        """
        @summary 在线服务总量
        
        @param request: GetOnlineServiceVolumeRequest
        @return: GetOnlineServiceVolumeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_online_service_volume_with_options(request, runtime)

    async def get_online_service_volume_async(
        self,
        request: aiccs_20191015_models.GetOnlineServiceVolumeRequest,
    ) -> aiccs_20191015_models.GetOnlineServiceVolumeResponse:
        """
        @summary 在线服务总量
        
        @param request: GetOnlineServiceVolumeRequest
        @return: GetOnlineServiceVolumeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_online_service_volume_with_options_async(request, runtime)

    def get_outboun_num_list_with_options(
        self,
        request: aiccs_20191015_models.GetOutbounNumListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetOutbounNumListResponse:
        """
        @param request: GetOutbounNumListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOutbounNumListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOutbounNumList',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetOutbounNumListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_outboun_num_list_with_options_async(
        self,
        request: aiccs_20191015_models.GetOutbounNumListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetOutbounNumListResponse:
        """
        @param request: GetOutbounNumListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOutbounNumListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOutbounNumList',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetOutbounNumListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_outboun_num_list(
        self,
        request: aiccs_20191015_models.GetOutbounNumListRequest,
    ) -> aiccs_20191015_models.GetOutbounNumListResponse:
        """
        @param request: GetOutbounNumListRequest
        @return: GetOutbounNumListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_outboun_num_list_with_options(request, runtime)

    async def get_outboun_num_list_async(
        self,
        request: aiccs_20191015_models.GetOutbounNumListRequest,
    ) -> aiccs_20191015_models.GetOutbounNumListResponse:
        """
        @param request: GetOutbounNumListRequest
        @return: GetOutbounNumListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_outboun_num_list_with_options_async(request, runtime)

    def get_quality_project_detail_with_options(
        self,
        request: aiccs_20191015_models.GetQualityProjectDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityProjectDetailResponse:
        """
        @param request: GetQualityProjectDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQualityProjectDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQualityProjectDetail',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityProjectDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_project_detail_with_options_async(
        self,
        request: aiccs_20191015_models.GetQualityProjectDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityProjectDetailResponse:
        """
        @param request: GetQualityProjectDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQualityProjectDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQualityProjectDetail',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityProjectDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_project_detail(
        self,
        request: aiccs_20191015_models.GetQualityProjectDetailRequest,
    ) -> aiccs_20191015_models.GetQualityProjectDetailResponse:
        """
        @param request: GetQualityProjectDetailRequest
        @return: GetQualityProjectDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_quality_project_detail_with_options(request, runtime)

    async def get_quality_project_detail_async(
        self,
        request: aiccs_20191015_models.GetQualityProjectDetailRequest,
    ) -> aiccs_20191015_models.GetQualityProjectDetailResponse:
        """
        @param request: GetQualityProjectDetailRequest
        @return: GetQualityProjectDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_quality_project_detail_with_options_async(request, runtime)

    def get_quality_project_list_with_options(
        self,
        request: aiccs_20191015_models.GetQualityProjectListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityProjectListResponse:
        """
        @param request: GetQualityProjectListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQualityProjectListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.check_freq_type):
            query['checkFreqType'] = request.check_freq_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQualityProjectList',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityProjectListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_project_list_with_options_async(
        self,
        request: aiccs_20191015_models.GetQualityProjectListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityProjectListResponse:
        """
        @param request: GetQualityProjectListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQualityProjectListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.check_freq_type):
            query['checkFreqType'] = request.check_freq_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQualityProjectList',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityProjectListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_project_list(
        self,
        request: aiccs_20191015_models.GetQualityProjectListRequest,
    ) -> aiccs_20191015_models.GetQualityProjectListResponse:
        """
        @param request: GetQualityProjectListRequest
        @return: GetQualityProjectListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_quality_project_list_with_options(request, runtime)

    async def get_quality_project_list_async(
        self,
        request: aiccs_20191015_models.GetQualityProjectListRequest,
    ) -> aiccs_20191015_models.GetQualityProjectListResponse:
        """
        @param request: GetQualityProjectListRequest
        @return: GetQualityProjectListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_quality_project_list_with_options_async(request, runtime)

    def get_quality_project_log_with_options(
        self,
        request: aiccs_20191015_models.GetQualityProjectLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityProjectLogResponse:
        """
        @param request: GetQualityProjectLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQualityProjectLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQualityProjectLog',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityProjectLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_project_log_with_options_async(
        self,
        request: aiccs_20191015_models.GetQualityProjectLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityProjectLogResponse:
        """
        @param request: GetQualityProjectLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQualityProjectLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQualityProjectLog',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityProjectLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_project_log(
        self,
        request: aiccs_20191015_models.GetQualityProjectLogRequest,
    ) -> aiccs_20191015_models.GetQualityProjectLogResponse:
        """
        @param request: GetQualityProjectLogRequest
        @return: GetQualityProjectLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_quality_project_log_with_options(request, runtime)

    async def get_quality_project_log_async(
        self,
        request: aiccs_20191015_models.GetQualityProjectLogRequest,
    ) -> aiccs_20191015_models.GetQualityProjectLogResponse:
        """
        @param request: GetQualityProjectLogRequest
        @return: GetQualityProjectLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_quality_project_log_with_options_async(request, runtime)

    def get_quality_result_with_options(
        self,
        request: aiccs_20191015_models.GetQualityResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityResultResponse:
        """
        @param request: GetQualityResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQualityResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.hit_status):
            query['HitStatus'] = request.hit_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_ids):
            query['ProjectIds'] = request.project_ids
        if not UtilClient.is_unset(request.quality_rule_ids):
            query['QualityRuleIds'] = request.quality_rule_ids
        if not UtilClient.is_unset(request.touch_end_time):
            query['TouchEndTime'] = request.touch_end_time
        if not UtilClient.is_unset(request.touch_start_time):
            query['TouchStartTime'] = request.touch_start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQualityResult',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_result_with_options_async(
        self,
        request: aiccs_20191015_models.GetQualityResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityResultResponse:
        """
        @param request: GetQualityResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQualityResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.hit_status):
            query['HitStatus'] = request.hit_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_ids):
            query['ProjectIds'] = request.project_ids
        if not UtilClient.is_unset(request.quality_rule_ids):
            query['QualityRuleIds'] = request.quality_rule_ids
        if not UtilClient.is_unset(request.touch_end_time):
            query['TouchEndTime'] = request.touch_end_time
        if not UtilClient.is_unset(request.touch_start_time):
            query['TouchStartTime'] = request.touch_start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQualityResult',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_result(
        self,
        request: aiccs_20191015_models.GetQualityResultRequest,
    ) -> aiccs_20191015_models.GetQualityResultResponse:
        """
        @param request: GetQualityResultRequest
        @return: GetQualityResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_quality_result_with_options(request, runtime)

    async def get_quality_result_async(
        self,
        request: aiccs_20191015_models.GetQualityResultRequest,
    ) -> aiccs_20191015_models.GetQualityResultResponse:
        """
        @param request: GetQualityResultRequest
        @return: GetQualityResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_quality_result_with_options_async(request, runtime)

    def get_quality_rule_detail_with_options(
        self,
        request: aiccs_20191015_models.GetQualityRuleDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityRuleDetailResponse:
        """
        @param request: GetQualityRuleDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQualityRuleDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.quality_rule_id):
            query['QualityRuleId'] = request.quality_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQualityRuleDetail',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityRuleDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_rule_detail_with_options_async(
        self,
        request: aiccs_20191015_models.GetQualityRuleDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityRuleDetailResponse:
        """
        @param request: GetQualityRuleDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQualityRuleDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.quality_rule_id):
            query['QualityRuleId'] = request.quality_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQualityRuleDetail',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityRuleDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_rule_detail(
        self,
        request: aiccs_20191015_models.GetQualityRuleDetailRequest,
    ) -> aiccs_20191015_models.GetQualityRuleDetailResponse:
        """
        @param request: GetQualityRuleDetailRequest
        @return: GetQualityRuleDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_quality_rule_detail_with_options(request, runtime)

    async def get_quality_rule_detail_async(
        self,
        request: aiccs_20191015_models.GetQualityRuleDetailRequest,
    ) -> aiccs_20191015_models.GetQualityRuleDetailResponse:
        """
        @param request: GetQualityRuleDetailRequest
        @return: GetQualityRuleDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_quality_rule_detail_with_options_async(request, runtime)

    def get_quality_rule_list_with_options(
        self,
        request: aiccs_20191015_models.GetQualityRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityRuleListResponse:
        """
        @param request: GetQualityRuleListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQualityRuleListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQualityRuleList',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_rule_list_with_options_async(
        self,
        request: aiccs_20191015_models.GetQualityRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityRuleListResponse:
        """
        @param request: GetQualityRuleListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQualityRuleListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQualityRuleList',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_rule_list(
        self,
        request: aiccs_20191015_models.GetQualityRuleListRequest,
    ) -> aiccs_20191015_models.GetQualityRuleListResponse:
        """
        @param request: GetQualityRuleListRequest
        @return: GetQualityRuleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_quality_rule_list_with_options(request, runtime)

    async def get_quality_rule_list_async(
        self,
        request: aiccs_20191015_models.GetQualityRuleListRequest,
    ) -> aiccs_20191015_models.GetQualityRuleListResponse:
        """
        @param request: GetQualityRuleListRequest
        @return: GetQualityRuleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_quality_rule_list_with_options_async(request, runtime)

    def get_quality_rule_tag_list_with_options(
        self,
        request: aiccs_20191015_models.GetQualityRuleTagListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityRuleTagListResponse:
        """
        @param request: GetQualityRuleTagListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQualityRuleTagListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQualityRuleTagList',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityRuleTagListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_rule_tag_list_with_options_async(
        self,
        request: aiccs_20191015_models.GetQualityRuleTagListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityRuleTagListResponse:
        """
        @param request: GetQualityRuleTagListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQualityRuleTagListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQualityRuleTagList',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityRuleTagListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_rule_tag_list(
        self,
        request: aiccs_20191015_models.GetQualityRuleTagListRequest,
    ) -> aiccs_20191015_models.GetQualityRuleTagListResponse:
        """
        @param request: GetQualityRuleTagListRequest
        @return: GetQualityRuleTagListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_quality_rule_tag_list_with_options(request, runtime)

    async def get_quality_rule_tag_list_async(
        self,
        request: aiccs_20191015_models.GetQualityRuleTagListRequest,
    ) -> aiccs_20191015_models.GetQualityRuleTagListResponse:
        """
        @param request: GetQualityRuleTagListRequest
        @return: GetQualityRuleTagListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_quality_rule_tag_list_with_options_async(request, runtime)

    def get_queue_information_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetQueueInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQueueInformationResponse:
        """
        @summary 技能组纬度队列信息
        
        @param tmp_req: GetQueueInformationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueueInformationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetQueueInformationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueueInformation',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQueueInformationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_queue_information_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetQueueInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQueueInformationResponse:
        """
        @summary 技能组纬度队列信息
        
        @param tmp_req: GetQueueInformationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueueInformationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetQueueInformationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueueInformation',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQueueInformationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_queue_information(
        self,
        request: aiccs_20191015_models.GetQueueInformationRequest,
    ) -> aiccs_20191015_models.GetQueueInformationResponse:
        """
        @summary 技能组纬度队列信息
        
        @param request: GetQueueInformationRequest
        @return: GetQueueInformationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_queue_information_with_options(request, runtime)

    async def get_queue_information_async(
        self,
        request: aiccs_20191015_models.GetQueueInformationRequest,
    ) -> aiccs_20191015_models.GetQueueInformationResponse:
        """
        @summary 技能组纬度队列信息
        
        @param request: GetQueueInformationRequest
        @return: GetQueueInformationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_queue_information_with_options_async(request, runtime)

    def get_record_data_with_options(
        self,
        request: aiccs_20191015_models.GetRecordDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetRecordDataResponse:
        """
        @param request: GetRecordDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRecordDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acid):
            query['Acid'] = request.acid
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRecordData',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetRecordDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_record_data_with_options_async(
        self,
        request: aiccs_20191015_models.GetRecordDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetRecordDataResponse:
        """
        @param request: GetRecordDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRecordDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acid):
            query['Acid'] = request.acid
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRecordData',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetRecordDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_record_data(
        self,
        request: aiccs_20191015_models.GetRecordDataRequest,
    ) -> aiccs_20191015_models.GetRecordDataResponse:
        """
        @param request: GetRecordDataRequest
        @return: GetRecordDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_record_data_with_options(request, runtime)

    async def get_record_data_async(
        self,
        request: aiccs_20191015_models.GetRecordDataRequest,
    ) -> aiccs_20191015_models.GetRecordDataResponse:
        """
        @param request: GetRecordDataRequest
        @return: GetRecordDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_record_data_with_options_async(request, runtime)

    def get_record_url_with_options(
        self,
        request: aiccs_20191015_models.GetRecordUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetRecordUrlResponse:
        """
        @summary 获取录音链接
        
        @param request: GetRecordUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRecordUrlResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRecordUrl',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetRecordUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_record_url_with_options_async(
        self,
        request: aiccs_20191015_models.GetRecordUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetRecordUrlResponse:
        """
        @summary 获取录音链接
        
        @param request: GetRecordUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRecordUrlResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRecordUrl',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetRecordUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_record_url(
        self,
        request: aiccs_20191015_models.GetRecordUrlRequest,
    ) -> aiccs_20191015_models.GetRecordUrlResponse:
        """
        @summary 获取录音链接
        
        @param request: GetRecordUrlRequest
        @return: GetRecordUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_record_url_with_options(request, runtime)

    async def get_record_url_async(
        self,
        request: aiccs_20191015_models.GetRecordUrlRequest,
    ) -> aiccs_20191015_models.GetRecordUrlResponse:
        """
        @summary 获取录音链接
        
        @param request: GetRecordUrlRequest
        @return: GetRecordUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_record_url_with_options_async(request, runtime)

    def get_rtc_token_with_options(
        self,
        request: aiccs_20191015_models.GetRtcTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetRtcTokenResponse:
        """
        @summary 获取RtcToken
        
        @param request: GetRtcTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRtcTokenResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRtcToken',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetRtcTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rtc_token_with_options_async(
        self,
        request: aiccs_20191015_models.GetRtcTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetRtcTokenResponse:
        """
        @summary 获取RtcToken
        
        @param request: GetRtcTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRtcTokenResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRtcToken',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetRtcTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rtc_token(
        self,
        request: aiccs_20191015_models.GetRtcTokenRequest,
    ) -> aiccs_20191015_models.GetRtcTokenResponse:
        """
        @summary 获取RtcToken
        
        @param request: GetRtcTokenRequest
        @return: GetRtcTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_rtc_token_with_options(request, runtime)

    async def get_rtc_token_async(
        self,
        request: aiccs_20191015_models.GetRtcTokenRequest,
    ) -> aiccs_20191015_models.GetRtcTokenResponse:
        """
        @summary 获取RtcToken
        
        @param request: GetRtcTokenRequest
        @return: GetRtcTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_rtc_token_with_options_async(request, runtime)

    def get_seat_information_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetSeatInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSeatInformationResponse:
        """
        @summary 部门纬度坐席信息数据
        
        @param tmp_req: GetSeatInformationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSeatInformationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSeatInformationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'depIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSeatInformation',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSeatInformationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_seat_information_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetSeatInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSeatInformationResponse:
        """
        @summary 部门纬度坐席信息数据
        
        @param tmp_req: GetSeatInformationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSeatInformationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSeatInformationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'depIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSeatInformation',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSeatInformationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_seat_information(
        self,
        request: aiccs_20191015_models.GetSeatInformationRequest,
    ) -> aiccs_20191015_models.GetSeatInformationResponse:
        """
        @summary 部门纬度坐席信息数据
        
        @param request: GetSeatInformationRequest
        @return: GetSeatInformationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_seat_information_with_options(request, runtime)

    async def get_seat_information_async(
        self,
        request: aiccs_20191015_models.GetSeatInformationRequest,
    ) -> aiccs_20191015_models.GetSeatInformationResponse:
        """
        @summary 部门纬度坐席信息数据
        
        @param request: GetSeatInformationRequest
        @return: GetSeatInformationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_seat_information_with_options_async(request, runtime)

    def get_skill_group_agent_status_details_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupAgentStatusDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupAgentStatusDetailsResponse:
        """
        @summary 技能组坐席状态详情
        
        @param tmp_req: GetSkillGroupAgentStatusDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSkillGroupAgentStatusDetailsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupAgentStatusDetailsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSkillGroupAgentStatusDetails',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupAgentStatusDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_group_agent_status_details_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupAgentStatusDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupAgentStatusDetailsResponse:
        """
        @summary 技能组坐席状态详情
        
        @param tmp_req: GetSkillGroupAgentStatusDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSkillGroupAgentStatusDetailsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupAgentStatusDetailsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSkillGroupAgentStatusDetails',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupAgentStatusDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_group_agent_status_details(
        self,
        request: aiccs_20191015_models.GetSkillGroupAgentStatusDetailsRequest,
    ) -> aiccs_20191015_models.GetSkillGroupAgentStatusDetailsResponse:
        """
        @summary 技能组坐席状态详情
        
        @param request: GetSkillGroupAgentStatusDetailsRequest
        @return: GetSkillGroupAgentStatusDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_skill_group_agent_status_details_with_options(request, runtime)

    async def get_skill_group_agent_status_details_async(
        self,
        request: aiccs_20191015_models.GetSkillGroupAgentStatusDetailsRequest,
    ) -> aiccs_20191015_models.GetSkillGroupAgentStatusDetailsResponse:
        """
        @summary 技能组坐席状态详情
        
        @param request: GetSkillGroupAgentStatusDetailsRequest
        @return: GetSkillGroupAgentStatusDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_skill_group_agent_status_details_with_options_async(request, runtime)

    def get_skill_group_and_agent_status_summary_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryResponse:
        """
        @summary 技能组坐席汇总状态量
        
        @param tmp_req: GetSkillGroupAndAgentStatusSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSkillGroupAndAgentStatusSummaryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSkillGroupAndAgentStatusSummary',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_group_and_agent_status_summary_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryResponse:
        """
        @summary 技能组坐席汇总状态量
        
        @param tmp_req: GetSkillGroupAndAgentStatusSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSkillGroupAndAgentStatusSummaryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSkillGroupAndAgentStatusSummary',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_group_and_agent_status_summary(
        self,
        request: aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryRequest,
    ) -> aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryResponse:
        """
        @summary 技能组坐席汇总状态量
        
        @param request: GetSkillGroupAndAgentStatusSummaryRequest
        @return: GetSkillGroupAndAgentStatusSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_skill_group_and_agent_status_summary_with_options(request, runtime)

    async def get_skill_group_and_agent_status_summary_async(
        self,
        request: aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryRequest,
    ) -> aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryResponse:
        """
        @summary 技能组坐席汇总状态量
        
        @param request: GetSkillGroupAndAgentStatusSummaryRequest
        @return: GetSkillGroupAndAgentStatusSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_skill_group_and_agent_status_summary_with_options_async(request, runtime)

    def get_skill_group_latitude_state_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupLatitudeStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupLatitudeStateResponse:
        """
        @summary 技能组纬度状态量
        
        @param tmp_req: GetSkillGroupLatitudeStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSkillGroupLatitudeStateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupLatitudeStateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSkillGroupLatitudeState',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupLatitudeStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_group_latitude_state_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupLatitudeStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupLatitudeStateResponse:
        """
        @summary 技能组纬度状态量
        
        @param tmp_req: GetSkillGroupLatitudeStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSkillGroupLatitudeStateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupLatitudeStateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSkillGroupLatitudeState',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupLatitudeStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_group_latitude_state(
        self,
        request: aiccs_20191015_models.GetSkillGroupLatitudeStateRequest,
    ) -> aiccs_20191015_models.GetSkillGroupLatitudeStateResponse:
        """
        @summary 技能组纬度状态量
        
        @param request: GetSkillGroupLatitudeStateRequest
        @return: GetSkillGroupLatitudeStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_skill_group_latitude_state_with_options(request, runtime)

    async def get_skill_group_latitude_state_async(
        self,
        request: aiccs_20191015_models.GetSkillGroupLatitudeStateRequest,
    ) -> aiccs_20191015_models.GetSkillGroupLatitudeStateResponse:
        """
        @summary 技能组纬度状态量
        
        @param request: GetSkillGroupLatitudeStateRequest
        @return: GetSkillGroupLatitudeStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_skill_group_latitude_state_with_options_async(request, runtime)

    def get_skill_group_service_capability_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupServiceCapabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupServiceCapabilityResponse:
        """
        @summary 技能组纬度服务能力
        
        @param tmp_req: GetSkillGroupServiceCapabilityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSkillGroupServiceCapabilityResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupServiceCapabilityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSkillGroupServiceCapability',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupServiceCapabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_group_service_capability_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupServiceCapabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupServiceCapabilityResponse:
        """
        @summary 技能组纬度服务能力
        
        @param tmp_req: GetSkillGroupServiceCapabilityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSkillGroupServiceCapabilityResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupServiceCapabilityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSkillGroupServiceCapability',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupServiceCapabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_group_service_capability(
        self,
        request: aiccs_20191015_models.GetSkillGroupServiceCapabilityRequest,
    ) -> aiccs_20191015_models.GetSkillGroupServiceCapabilityResponse:
        """
        @summary 技能组纬度服务能力
        
        @param request: GetSkillGroupServiceCapabilityRequest
        @return: GetSkillGroupServiceCapabilityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_skill_group_service_capability_with_options(request, runtime)

    async def get_skill_group_service_capability_async(
        self,
        request: aiccs_20191015_models.GetSkillGroupServiceCapabilityRequest,
    ) -> aiccs_20191015_models.GetSkillGroupServiceCapabilityResponse:
        """
        @summary 技能组纬度服务能力
        
        @param request: GetSkillGroupServiceCapabilityRequest
        @return: GetSkillGroupServiceCapabilityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_skill_group_service_capability_with_options_async(request, runtime)

    def get_skill_group_service_status_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupServiceStatusResponse:
        """
        @summary 技能组服务状态量
        
        @param tmp_req: GetSkillGroupServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSkillGroupServiceStatusResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupServiceStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSkillGroupServiceStatus',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_group_service_status_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupServiceStatusResponse:
        """
        @summary 技能组服务状态量
        
        @param tmp_req: GetSkillGroupServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSkillGroupServiceStatusResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupServiceStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSkillGroupServiceStatus',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_group_service_status(
        self,
        request: aiccs_20191015_models.GetSkillGroupServiceStatusRequest,
    ) -> aiccs_20191015_models.GetSkillGroupServiceStatusResponse:
        """
        @summary 技能组服务状态量
        
        @param request: GetSkillGroupServiceStatusRequest
        @return: GetSkillGroupServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_skill_group_service_status_with_options(request, runtime)

    async def get_skill_group_service_status_async(
        self,
        request: aiccs_20191015_models.GetSkillGroupServiceStatusRequest,
    ) -> aiccs_20191015_models.GetSkillGroupServiceStatusResponse:
        """
        @summary 技能组服务状态量
        
        @param request: GetSkillGroupServiceStatusRequest
        @return: GetSkillGroupServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_skill_group_service_status_with_options_async(request, runtime)

    def get_skill_group_status_total_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupStatusTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupStatusTotalResponse:
        """
        @summary 技能组状态总量
        
        @param tmp_req: GetSkillGroupStatusTotalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSkillGroupStatusTotalResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupStatusTotalShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSkillGroupStatusTotal',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupStatusTotalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_group_status_total_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupStatusTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupStatusTotalResponse:
        """
        @summary 技能组状态总量
        
        @param tmp_req: GetSkillGroupStatusTotalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSkillGroupStatusTotalResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupStatusTotalShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSkillGroupStatusTotal',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupStatusTotalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_group_status_total(
        self,
        request: aiccs_20191015_models.GetSkillGroupStatusTotalRequest,
    ) -> aiccs_20191015_models.GetSkillGroupStatusTotalResponse:
        """
        @summary 技能组状态总量
        
        @param request: GetSkillGroupStatusTotalRequest
        @return: GetSkillGroupStatusTotalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_skill_group_status_total_with_options(request, runtime)

    async def get_skill_group_status_total_async(
        self,
        request: aiccs_20191015_models.GetSkillGroupStatusTotalRequest,
    ) -> aiccs_20191015_models.GetSkillGroupStatusTotalResponse:
        """
        @summary 技能组状态总量
        
        @param request: GetSkillGroupStatusTotalRequest
        @return: GetSkillGroupStatusTotalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_skill_group_status_total_with_options_async(request, runtime)

    def hang_up_double_call_with_options(
        self,
        request: aiccs_20191015_models.HangUpDoubleCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.HangUpDoubleCallResponse:
        """
        @summary 移动端呼叫挂断
        
        @param request: HangUpDoubleCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: HangUpDoubleCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acid):
            query['Acid'] = request.acid
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HangUpDoubleCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HangUpDoubleCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def hang_up_double_call_with_options_async(
        self,
        request: aiccs_20191015_models.HangUpDoubleCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.HangUpDoubleCallResponse:
        """
        @summary 移动端呼叫挂断
        
        @param request: HangUpDoubleCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: HangUpDoubleCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acid):
            query['Acid'] = request.acid
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HangUpDoubleCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HangUpDoubleCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hang_up_double_call(
        self,
        request: aiccs_20191015_models.HangUpDoubleCallRequest,
    ) -> aiccs_20191015_models.HangUpDoubleCallResponse:
        """
        @summary 移动端呼叫挂断
        
        @param request: HangUpDoubleCallRequest
        @return: HangUpDoubleCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.hang_up_double_call_with_options(request, runtime)

    async def hang_up_double_call_async(
        self,
        request: aiccs_20191015_models.HangUpDoubleCallRequest,
    ) -> aiccs_20191015_models.HangUpDoubleCallResponse:
        """
        @summary 移动端呼叫挂断
        
        @param request: HangUpDoubleCallRequest
        @return: HangUpDoubleCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.hang_up_double_call_with_options_async(request, runtime)

    def hangup_call_with_options(
        self,
        request: aiccs_20191015_models.HangupCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.HangupCallResponse:
        """
        @param request: HangupCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: HangupCallResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.call_id):
            body['CallId'] = request.call_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HangupCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HangupCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def hangup_call_with_options_async(
        self,
        request: aiccs_20191015_models.HangupCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.HangupCallResponse:
        """
        @param request: HangupCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: HangupCallResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.call_id):
            body['CallId'] = request.call_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HangupCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HangupCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hangup_call(
        self,
        request: aiccs_20191015_models.HangupCallRequest,
    ) -> aiccs_20191015_models.HangupCallResponse:
        """
        @param request: HangupCallRequest
        @return: HangupCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.hangup_call_with_options(request, runtime)

    async def hangup_call_async(
        self,
        request: aiccs_20191015_models.HangupCallRequest,
    ) -> aiccs_20191015_models.HangupCallResponse:
        """
        @param request: HangupCallRequest
        @return: HangupCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.hangup_call_with_options_async(request, runtime)

    def hangup_operate_with_options(
        self,
        request: aiccs_20191015_models.HangupOperateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.HangupOperateResponse:
        """
        @summary 通信智能引擎中主动挂断通话
        
        @param request: HangupOperateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: HangupOperateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.immediate_hangup):
            query['ImmediateHangup'] = request.immediate_hangup
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HangupOperate',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HangupOperateResponse(),
            self.call_api(params, req, runtime)
        )

    async def hangup_operate_with_options_async(
        self,
        request: aiccs_20191015_models.HangupOperateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.HangupOperateResponse:
        """
        @summary 通信智能引擎中主动挂断通话
        
        @param request: HangupOperateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: HangupOperateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.immediate_hangup):
            query['ImmediateHangup'] = request.immediate_hangup
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HangupOperate',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HangupOperateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hangup_operate(
        self,
        request: aiccs_20191015_models.HangupOperateRequest,
    ) -> aiccs_20191015_models.HangupOperateResponse:
        """
        @summary 通信智能引擎中主动挂断通话
        
        @param request: HangupOperateRequest
        @return: HangupOperateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.hangup_operate_with_options(request, runtime)

    async def hangup_operate_async(
        self,
        request: aiccs_20191015_models.HangupOperateRequest,
    ) -> aiccs_20191015_models.HangupOperateResponse:
        """
        @summary 通信智能引擎中主动挂断通话
        
        @param request: HangupOperateRequest
        @return: HangupOperateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.hangup_operate_with_options_async(request, runtime)

    def hangup_third_call_with_options(
        self,
        request: aiccs_20191015_models.HangupThirdCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.HangupThirdCallResponse:
        """
        @param request: HangupThirdCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: HangupThirdCallResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.call_id):
            body['CallId'] = request.call_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HangupThirdCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HangupThirdCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def hangup_third_call_with_options_async(
        self,
        request: aiccs_20191015_models.HangupThirdCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.HangupThirdCallResponse:
        """
        @param request: HangupThirdCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: HangupThirdCallResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.call_id):
            body['CallId'] = request.call_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HangupThirdCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HangupThirdCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hangup_third_call(
        self,
        request: aiccs_20191015_models.HangupThirdCallRequest,
    ) -> aiccs_20191015_models.HangupThirdCallResponse:
        """
        @param request: HangupThirdCallRequest
        @return: HangupThirdCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.hangup_third_call_with_options(request, runtime)

    async def hangup_third_call_async(
        self,
        request: aiccs_20191015_models.HangupThirdCallRequest,
    ) -> aiccs_20191015_models.HangupThirdCallResponse:
        """
        @param request: HangupThirdCallRequest
        @return: HangupThirdCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.hangup_third_call_with_options_async(request, runtime)

    def hold_call_with_options(
        self,
        request: aiccs_20191015_models.HoldCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.HoldCallResponse:
        """
        @param request: HoldCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: HoldCallResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.call_id):
            body['CallId'] = request.call_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HoldCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HoldCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def hold_call_with_options_async(
        self,
        request: aiccs_20191015_models.HoldCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.HoldCallResponse:
        """
        @param request: HoldCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: HoldCallResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.call_id):
            body['CallId'] = request.call_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HoldCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HoldCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hold_call(
        self,
        request: aiccs_20191015_models.HoldCallRequest,
    ) -> aiccs_20191015_models.HoldCallResponse:
        """
        @param request: HoldCallRequest
        @return: HoldCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.hold_call_with_options(request, runtime)

    async def hold_call_async(
        self,
        request: aiccs_20191015_models.HoldCallRequest,
    ) -> aiccs_20191015_models.HoldCallResponse:
        """
        @param request: HoldCallRequest
        @return: HoldCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.hold_call_with_options_async(request, runtime)

    def hotline_session_query_with_options(
        self,
        request: aiccs_20191015_models.HotlineSessionQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.HotlineSessionQueryResponse:
        """
        @param request: HotlineSessionQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: HotlineSessionQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acid):
            query['Acid'] = request.acid
        if not UtilClient.is_unset(request.acid_list):
            query['AcidList'] = request.acid_list
        if not UtilClient.is_unset(request.call_result):
            query['CallResult'] = request.call_result
        if not UtilClient.is_unset(request.call_result_list):
            query['CallResultList'] = request.call_result_list
        if not UtilClient.is_unset(request.call_type):
            query['CallType'] = request.call_type
        if not UtilClient.is_unset(request.call_type_list):
            query['CallTypeList'] = request.call_type_list
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.called_number_list):
            query['CalledNumberList'] = request.called_number_list
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.calling_number_list):
            query['CallingNumberList'] = request.calling_number_list
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_id_list):
            query['GroupIdList'] = request.group_id_list
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.member_id):
            query['MemberId'] = request.member_id
        if not UtilClient.is_unset(request.member_id_list):
            query['MemberIdList'] = request.member_id_list
        if not UtilClient.is_unset(request.member_name):
            query['MemberName'] = request.member_name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.query_end_time):
            query['QueryEndTime'] = request.query_end_time
        if not UtilClient.is_unset(request.query_start_time):
            query['QueryStartTime'] = request.query_start_time
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.servicer_id):
            query['ServicerId'] = request.servicer_id
        if not UtilClient.is_unset(request.servicer_id_list):
            query['ServicerIdList'] = request.servicer_id_list
        if not UtilClient.is_unset(request.servicer_name):
            query['ServicerName'] = request.servicer_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotlineSessionQuery',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HotlineSessionQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def hotline_session_query_with_options_async(
        self,
        request: aiccs_20191015_models.HotlineSessionQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.HotlineSessionQueryResponse:
        """
        @param request: HotlineSessionQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: HotlineSessionQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acid):
            query['Acid'] = request.acid
        if not UtilClient.is_unset(request.acid_list):
            query['AcidList'] = request.acid_list
        if not UtilClient.is_unset(request.call_result):
            query['CallResult'] = request.call_result
        if not UtilClient.is_unset(request.call_result_list):
            query['CallResultList'] = request.call_result_list
        if not UtilClient.is_unset(request.call_type):
            query['CallType'] = request.call_type
        if not UtilClient.is_unset(request.call_type_list):
            query['CallTypeList'] = request.call_type_list
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.called_number_list):
            query['CalledNumberList'] = request.called_number_list
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.calling_number_list):
            query['CallingNumberList'] = request.calling_number_list
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_id_list):
            query['GroupIdList'] = request.group_id_list
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.member_id):
            query['MemberId'] = request.member_id
        if not UtilClient.is_unset(request.member_id_list):
            query['MemberIdList'] = request.member_id_list
        if not UtilClient.is_unset(request.member_name):
            query['MemberName'] = request.member_name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.query_end_time):
            query['QueryEndTime'] = request.query_end_time
        if not UtilClient.is_unset(request.query_start_time):
            query['QueryStartTime'] = request.query_start_time
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.servicer_id):
            query['ServicerId'] = request.servicer_id
        if not UtilClient.is_unset(request.servicer_id_list):
            query['ServicerIdList'] = request.servicer_id_list
        if not UtilClient.is_unset(request.servicer_name):
            query['ServicerName'] = request.servicer_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotlineSessionQuery',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HotlineSessionQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hotline_session_query(
        self,
        request: aiccs_20191015_models.HotlineSessionQueryRequest,
    ) -> aiccs_20191015_models.HotlineSessionQueryResponse:
        """
        @param request: HotlineSessionQueryRequest
        @return: HotlineSessionQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.hotline_session_query_with_options(request, runtime)

    async def hotline_session_query_async(
        self,
        request: aiccs_20191015_models.HotlineSessionQueryRequest,
    ) -> aiccs_20191015_models.HotlineSessionQueryResponse:
        """
        @param request: HotlineSessionQueryRequest
        @return: HotlineSessionQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.hotline_session_query_with_options_async(request, runtime)

    def import_task_number_datas_with_options(
        self,
        tmp_req: aiccs_20191015_models.ImportTaskNumberDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ImportTaskNumberDatasResponse:
        """
        @summary 导入任务号码数据
        
        @param tmp_req: ImportTaskNumberDatasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportTaskNumberDatasResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.ImportTaskNumberDatasShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.phone_number_list):
            request.phone_number_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phone_number_list, 'PhoneNumberList', 'json')
        query = {}
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.oss_file_name):
            query['OssFileName'] = request.oss_file_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        body = {}
        if not UtilClient.is_unset(request.phone_number_list_shrink):
            body['PhoneNumberList'] = request.phone_number_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportTaskNumberDatas',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ImportTaskNumberDatasResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_task_number_datas_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.ImportTaskNumberDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ImportTaskNumberDatasResponse:
        """
        @summary 导入任务号码数据
        
        @param tmp_req: ImportTaskNumberDatasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportTaskNumberDatasResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.ImportTaskNumberDatasShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.phone_number_list):
            request.phone_number_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phone_number_list, 'PhoneNumberList', 'json')
        query = {}
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.oss_file_name):
            query['OssFileName'] = request.oss_file_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        body = {}
        if not UtilClient.is_unset(request.phone_number_list_shrink):
            body['PhoneNumberList'] = request.phone_number_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportTaskNumberDatas',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ImportTaskNumberDatasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_task_number_datas(
        self,
        request: aiccs_20191015_models.ImportTaskNumberDatasRequest,
    ) -> aiccs_20191015_models.ImportTaskNumberDatasResponse:
        """
        @summary 导入任务号码数据
        
        @param request: ImportTaskNumberDatasRequest
        @return: ImportTaskNumberDatasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_task_number_datas_with_options(request, runtime)

    async def import_task_number_datas_async(
        self,
        request: aiccs_20191015_models.ImportTaskNumberDatasRequest,
    ) -> aiccs_20191015_models.ImportTaskNumberDatasResponse:
        """
        @summary 导入任务号码数据
        
        @param request: ImportTaskNumberDatasRequest
        @return: ImportTaskNumberDatasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_task_number_datas_with_options_async(request, runtime)

    def insert_ai_outbound_phone_nums_with_options(
        self,
        tmp_req: aiccs_20191015_models.InsertAiOutboundPhoneNumsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.InsertAiOutboundPhoneNumsResponse:
        """
        @summary 智能外呼任务导入号码
        
        @param tmp_req: InsertAiOutboundPhoneNumsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertAiOutboundPhoneNumsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.InsertAiOutboundPhoneNumsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.details):
            request.details_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.details, 'Details', 'json')
        query = {}
        if not UtilClient.is_unset(request.batch_version):
            query['BatchVersion'] = request.batch_version
        if not UtilClient.is_unset(request.details_shrink):
            query['Details'] = request.details_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertAiOutboundPhoneNums',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.InsertAiOutboundPhoneNumsResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_ai_outbound_phone_nums_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.InsertAiOutboundPhoneNumsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.InsertAiOutboundPhoneNumsResponse:
        """
        @summary 智能外呼任务导入号码
        
        @param tmp_req: InsertAiOutboundPhoneNumsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertAiOutboundPhoneNumsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.InsertAiOutboundPhoneNumsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.details):
            request.details_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.details, 'Details', 'json')
        query = {}
        if not UtilClient.is_unset(request.batch_version):
            query['BatchVersion'] = request.batch_version
        if not UtilClient.is_unset(request.details_shrink):
            query['Details'] = request.details_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertAiOutboundPhoneNums',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.InsertAiOutboundPhoneNumsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_ai_outbound_phone_nums(
        self,
        request: aiccs_20191015_models.InsertAiOutboundPhoneNumsRequest,
    ) -> aiccs_20191015_models.InsertAiOutboundPhoneNumsResponse:
        """
        @summary 智能外呼任务导入号码
        
        @param request: InsertAiOutboundPhoneNumsRequest
        @return: InsertAiOutboundPhoneNumsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.insert_ai_outbound_phone_nums_with_options(request, runtime)

    async def insert_ai_outbound_phone_nums_async(
        self,
        request: aiccs_20191015_models.InsertAiOutboundPhoneNumsRequest,
    ) -> aiccs_20191015_models.InsertAiOutboundPhoneNumsResponse:
        """
        @summary 智能外呼任务导入号码
        
        @param request: InsertAiOutboundPhoneNumsRequest
        @return: InsertAiOutboundPhoneNumsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.insert_ai_outbound_phone_nums_with_options_async(request, runtime)

    def insert_task_detail_with_options(
        self,
        request: aiccs_20191015_models.InsertTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.InsertTaskDetailResponse:
        """
        @param request: InsertTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertTaskDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_infos):
            query['CallInfos'] = request.call_infos
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.outbound_task_id):
            query['OutboundTaskId'] = request.outbound_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertTaskDetail',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.InsertTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_task_detail_with_options_async(
        self,
        request: aiccs_20191015_models.InsertTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.InsertTaskDetailResponse:
        """
        @param request: InsertTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertTaskDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_infos):
            query['CallInfos'] = request.call_infos
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.outbound_task_id):
            query['OutboundTaskId'] = request.outbound_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertTaskDetail',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.InsertTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_task_detail(
        self,
        request: aiccs_20191015_models.InsertTaskDetailRequest,
    ) -> aiccs_20191015_models.InsertTaskDetailResponse:
        """
        @param request: InsertTaskDetailRequest
        @return: InsertTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.insert_task_detail_with_options(request, runtime)

    async def insert_task_detail_async(
        self,
        request: aiccs_20191015_models.InsertTaskDetailRequest,
    ) -> aiccs_20191015_models.InsertTaskDetailResponse:
        """
        @param request: InsertTaskDetailRequest
        @return: InsertTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.insert_task_detail_with_options_async(request, runtime)

    def join_third_call_with_options(
        self,
        request: aiccs_20191015_models.JoinThirdCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.JoinThirdCallResponse:
        """
        @param request: JoinThirdCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: JoinThirdCallResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.call_id):
            body['CallId'] = request.call_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not UtilClient.is_unset(request.hold_connection_id):
            body['HoldConnectionId'] = request.hold_connection_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='JoinThirdCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.JoinThirdCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def join_third_call_with_options_async(
        self,
        request: aiccs_20191015_models.JoinThirdCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.JoinThirdCallResponse:
        """
        @param request: JoinThirdCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: JoinThirdCallResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.call_id):
            body['CallId'] = request.call_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not UtilClient.is_unset(request.hold_connection_id):
            body['HoldConnectionId'] = request.hold_connection_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='JoinThirdCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.JoinThirdCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def join_third_call(
        self,
        request: aiccs_20191015_models.JoinThirdCallRequest,
    ) -> aiccs_20191015_models.JoinThirdCallResponse:
        """
        @param request: JoinThirdCallRequest
        @return: JoinThirdCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.join_third_call_with_options(request, runtime)

    async def join_third_call_async(
        self,
        request: aiccs_20191015_models.JoinThirdCallRequest,
    ) -> aiccs_20191015_models.JoinThirdCallResponse:
        """
        @param request: JoinThirdCallRequest
        @return: JoinThirdCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.join_third_call_with_options_async(request, runtime)

    def list_agent_by_skill_group_id_with_options(
        self,
        request: aiccs_20191015_models.ListAgentBySkillGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListAgentBySkillGroupIdResponse:
        """
        @param request: ListAgentBySkillGroupIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentBySkillGroupIdResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgentBySkillGroupId',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListAgentBySkillGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_by_skill_group_id_with_options_async(
        self,
        request: aiccs_20191015_models.ListAgentBySkillGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListAgentBySkillGroupIdResponse:
        """
        @param request: ListAgentBySkillGroupIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentBySkillGroupIdResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgentBySkillGroupId',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListAgentBySkillGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_by_skill_group_id(
        self,
        request: aiccs_20191015_models.ListAgentBySkillGroupIdRequest,
    ) -> aiccs_20191015_models.ListAgentBySkillGroupIdResponse:
        """
        @param request: ListAgentBySkillGroupIdRequest
        @return: ListAgentBySkillGroupIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_agent_by_skill_group_id_with_options(request, runtime)

    async def list_agent_by_skill_group_id_async(
        self,
        request: aiccs_20191015_models.ListAgentBySkillGroupIdRequest,
    ) -> aiccs_20191015_models.ListAgentBySkillGroupIdResponse:
        """
        @param request: ListAgentBySkillGroupIdRequest
        @return: ListAgentBySkillGroupIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_agent_by_skill_group_id_with_options_async(request, runtime)

    def list_aiccs_robot_with_options(
        self,
        request: aiccs_20191015_models.ListAiccsRobotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListAiccsRobotResponse:
        """
        @summary 查询所有机器人列表
        
        @param request: ListAiccsRobotRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAiccsRobotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.robot_name):
            query['RobotName'] = request.robot_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAiccsRobot',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListAiccsRobotResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aiccs_robot_with_options_async(
        self,
        request: aiccs_20191015_models.ListAiccsRobotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListAiccsRobotResponse:
        """
        @summary 查询所有机器人列表
        
        @param request: ListAiccsRobotRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAiccsRobotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.robot_name):
            query['RobotName'] = request.robot_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAiccsRobot',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListAiccsRobotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aiccs_robot(
        self,
        request: aiccs_20191015_models.ListAiccsRobotRequest,
    ) -> aiccs_20191015_models.ListAiccsRobotResponse:
        """
        @summary 查询所有机器人列表
        
        @param request: ListAiccsRobotRequest
        @return: ListAiccsRobotResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_aiccs_robot_with_options(request, runtime)

    async def list_aiccs_robot_async(
        self,
        request: aiccs_20191015_models.ListAiccsRobotRequest,
    ) -> aiccs_20191015_models.ListAiccsRobotResponse:
        """
        @summary 查询所有机器人列表
        
        @param request: ListAiccsRobotRequest
        @return: ListAiccsRobotResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_aiccs_robot_with_options_async(request, runtime)

    def list_available_tts_with_options(
        self,
        request: aiccs_20191015_models.ListAvailableTtsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListAvailableTtsResponse:
        """
        @summary 获取tts音色列表
        
        @param request: ListAvailableTtsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAvailableTtsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tts_voice_code):
            query['TtsVoiceCode'] = request.tts_voice_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAvailableTts',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListAvailableTtsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_available_tts_with_options_async(
        self,
        request: aiccs_20191015_models.ListAvailableTtsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListAvailableTtsResponse:
        """
        @summary 获取tts音色列表
        
        @param request: ListAvailableTtsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAvailableTtsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tts_voice_code):
            query['TtsVoiceCode'] = request.tts_voice_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAvailableTts',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListAvailableTtsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_available_tts(
        self,
        request: aiccs_20191015_models.ListAvailableTtsRequest,
    ) -> aiccs_20191015_models.ListAvailableTtsResponse:
        """
        @summary 获取tts音色列表
        
        @param request: ListAvailableTtsRequest
        @return: ListAvailableTtsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_available_tts_with_options(request, runtime)

    async def list_available_tts_async(
        self,
        request: aiccs_20191015_models.ListAvailableTtsRequest,
    ) -> aiccs_20191015_models.ListAvailableTtsResponse:
        """
        @summary 获取tts音色列表
        
        @param request: ListAvailableTtsRequest
        @return: ListAvailableTtsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_available_tts_with_options_async(request, runtime)

    def list_chat_record_detail_with_options(
        self,
        request: aiccs_20191015_models.ListChatRecordDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListChatRecordDetailResponse:
        """
        @summary 根据时间段查询在线会话详情，包含会话内容，时间段范围最长不超过1天
        
        @param request: ListChatRecordDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChatRecordDetailResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChatRecordDetail',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListChatRecordDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chat_record_detail_with_options_async(
        self,
        request: aiccs_20191015_models.ListChatRecordDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListChatRecordDetailResponse:
        """
        @summary 根据时间段查询在线会话详情，包含会话内容，时间段范围最长不超过1天
        
        @param request: ListChatRecordDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChatRecordDetailResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChatRecordDetail',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListChatRecordDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chat_record_detail(
        self,
        request: aiccs_20191015_models.ListChatRecordDetailRequest,
    ) -> aiccs_20191015_models.ListChatRecordDetailResponse:
        """
        @summary 根据时间段查询在线会话详情，包含会话内容，时间段范围最长不超过1天
        
        @param request: ListChatRecordDetailRequest
        @return: ListChatRecordDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_chat_record_detail_with_options(request, runtime)

    async def list_chat_record_detail_async(
        self,
        request: aiccs_20191015_models.ListChatRecordDetailRequest,
    ) -> aiccs_20191015_models.ListChatRecordDetailResponse:
        """
        @summary 根据时间段查询在线会话详情，包含会话内容，时间段范围最长不超过1天
        
        @param request: ListChatRecordDetailRequest
        @return: ListChatRecordDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_chat_record_detail_with_options_async(request, runtime)

    def list_dialog_with_options(
        self,
        request: aiccs_20191015_models.ListDialogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListDialogResponse:
        """
        @summary 查看对话记录
        
        @param request: ListDialogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDialogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called):
            query['Called'] = request.called
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDialog',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListDialogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dialog_with_options_async(
        self,
        request: aiccs_20191015_models.ListDialogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListDialogResponse:
        """
        @summary 查看对话记录
        
        @param request: ListDialogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDialogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called):
            query['Called'] = request.called
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDialog',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListDialogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dialog(
        self,
        request: aiccs_20191015_models.ListDialogRequest,
    ) -> aiccs_20191015_models.ListDialogResponse:
        """
        @summary 查看对话记录
        
        @param request: ListDialogRequest
        @return: ListDialogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dialog_with_options(request, runtime)

    async def list_dialog_async(
        self,
        request: aiccs_20191015_models.ListDialogRequest,
    ) -> aiccs_20191015_models.ListDialogResponse:
        """
        @summary 查看对话记录
        
        @param request: ListDialogRequest
        @return: ListDialogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_dialog_with_options_async(request, runtime)

    def list_hotline_record_with_options(
        self,
        request: aiccs_20191015_models.ListHotlineRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListHotlineRecordResponse:
        """
        @param request: ListHotlineRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotlineRecordResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotlineRecord',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListHotlineRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotline_record_with_options_async(
        self,
        request: aiccs_20191015_models.ListHotlineRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListHotlineRecordResponse:
        """
        @param request: ListHotlineRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotlineRecordResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotlineRecord',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListHotlineRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotline_record(
        self,
        request: aiccs_20191015_models.ListHotlineRecordRequest,
    ) -> aiccs_20191015_models.ListHotlineRecordResponse:
        """
        @param request: ListHotlineRecordRequest
        @return: ListHotlineRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_hotline_record_with_options(request, runtime)

    async def list_hotline_record_async(
        self,
        request: aiccs_20191015_models.ListHotlineRecordRequest,
    ) -> aiccs_20191015_models.ListHotlineRecordResponse:
        """
        @param request: ListHotlineRecordRequest
        @return: ListHotlineRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_hotline_record_with_options_async(request, runtime)

    def list_hotline_record_detail_with_options(
        self,
        request: aiccs_20191015_models.ListHotlineRecordDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListHotlineRecordDetailResponse:
        """
        @summary 根据时间段查询热线详情列表，包含热线通话信息，时间段范围最长不超过1天
        
        @param request: ListHotlineRecordDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotlineRecordDetailResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotlineRecordDetail',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListHotlineRecordDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotline_record_detail_with_options_async(
        self,
        request: aiccs_20191015_models.ListHotlineRecordDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListHotlineRecordDetailResponse:
        """
        @summary 根据时间段查询热线详情列表，包含热线通话信息，时间段范围最长不超过1天
        
        @param request: ListHotlineRecordDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotlineRecordDetailResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotlineRecordDetail',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListHotlineRecordDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotline_record_detail(
        self,
        request: aiccs_20191015_models.ListHotlineRecordDetailRequest,
    ) -> aiccs_20191015_models.ListHotlineRecordDetailResponse:
        """
        @summary 根据时间段查询热线详情列表，包含热线通话信息，时间段范围最长不超过1天
        
        @param request: ListHotlineRecordDetailRequest
        @return: ListHotlineRecordDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_hotline_record_detail_with_options(request, runtime)

    async def list_hotline_record_detail_async(
        self,
        request: aiccs_20191015_models.ListHotlineRecordDetailRequest,
    ) -> aiccs_20191015_models.ListHotlineRecordDetailResponse:
        """
        @summary 根据时间段查询热线详情列表，包含热线通话信息，时间段范围最长不超过1天
        
        @param request: ListHotlineRecordDetailRequest
        @return: ListHotlineRecordDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_hotline_record_detail_with_options_async(request, runtime)

    def list_outbound_phone_number_with_options(
        self,
        request: aiccs_20191015_models.ListOutboundPhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListOutboundPhoneNumberResponse:
        """
        @param request: ListOutboundPhoneNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOutboundPhoneNumberResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOutboundPhoneNumber',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListOutboundPhoneNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_outbound_phone_number_with_options_async(
        self,
        request: aiccs_20191015_models.ListOutboundPhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListOutboundPhoneNumberResponse:
        """
        @param request: ListOutboundPhoneNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOutboundPhoneNumberResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOutboundPhoneNumber',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListOutboundPhoneNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_outbound_phone_number(
        self,
        request: aiccs_20191015_models.ListOutboundPhoneNumberRequest,
    ) -> aiccs_20191015_models.ListOutboundPhoneNumberResponse:
        """
        @param request: ListOutboundPhoneNumberRequest
        @return: ListOutboundPhoneNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_outbound_phone_number_with_options(request, runtime)

    async def list_outbound_phone_number_async(
        self,
        request: aiccs_20191015_models.ListOutboundPhoneNumberRequest,
    ) -> aiccs_20191015_models.ListOutboundPhoneNumberResponse:
        """
        @param request: ListOutboundPhoneNumberRequest
        @return: ListOutboundPhoneNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_outbound_phone_number_with_options_async(request, runtime)

    def list_robot_call_dialog_with_options(
        self,
        request: aiccs_20191015_models.ListRobotCallDialogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListRobotCallDialogResponse:
        """
        @summary 查看对话记录
        
        @param request: ListRobotCallDialogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRobotCallDialogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.create_time):
            query['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRobotCallDialog',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListRobotCallDialogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_robot_call_dialog_with_options_async(
        self,
        request: aiccs_20191015_models.ListRobotCallDialogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListRobotCallDialogResponse:
        """
        @summary 查看对话记录
        
        @param request: ListRobotCallDialogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRobotCallDialogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.create_time):
            query['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRobotCallDialog',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListRobotCallDialogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_robot_call_dialog(
        self,
        request: aiccs_20191015_models.ListRobotCallDialogRequest,
    ) -> aiccs_20191015_models.ListRobotCallDialogResponse:
        """
        @summary 查看对话记录
        
        @param request: ListRobotCallDialogRequest
        @return: ListRobotCallDialogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_robot_call_dialog_with_options(request, runtime)

    async def list_robot_call_dialog_async(
        self,
        request: aiccs_20191015_models.ListRobotCallDialogRequest,
    ) -> aiccs_20191015_models.ListRobotCallDialogResponse:
        """
        @summary 查看对话记录
        
        @param request: ListRobotCallDialogRequest
        @return: ListRobotCallDialogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_robot_call_dialog_with_options_async(request, runtime)

    def list_robot_node_with_options(
        self,
        request: aiccs_20191015_models.ListRobotNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListRobotNodeResponse:
        """
        @summary 查询机器人输出列表
        
        @param request: ListRobotNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRobotNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.robot_id):
            query['RobotId'] = request.robot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRobotNode',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListRobotNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_robot_node_with_options_async(
        self,
        request: aiccs_20191015_models.ListRobotNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListRobotNodeResponse:
        """
        @summary 查询机器人输出列表
        
        @param request: ListRobotNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRobotNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.robot_id):
            query['RobotId'] = request.robot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRobotNode',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListRobotNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_robot_node(
        self,
        request: aiccs_20191015_models.ListRobotNodeRequest,
    ) -> aiccs_20191015_models.ListRobotNodeResponse:
        """
        @summary 查询机器人输出列表
        
        @param request: ListRobotNodeRequest
        @return: ListRobotNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_robot_node_with_options(request, runtime)

    async def list_robot_node_async(
        self,
        request: aiccs_20191015_models.ListRobotNodeRequest,
    ) -> aiccs_20191015_models.ListRobotNodeResponse:
        """
        @summary 查询机器人输出列表
        
        @param request: ListRobotNodeRequest
        @return: ListRobotNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_robot_node_with_options_async(request, runtime)

    def list_robot_params_with_options(
        self,
        request: aiccs_20191015_models.ListRobotParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListRobotParamsResponse:
        """
        @summary 查询参数列表
        
        @param request: ListRobotParamsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRobotParamsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.robot_id):
            query['RobotId'] = request.robot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRobotParams',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListRobotParamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_robot_params_with_options_async(
        self,
        request: aiccs_20191015_models.ListRobotParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListRobotParamsResponse:
        """
        @summary 查询参数列表
        
        @param request: ListRobotParamsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRobotParamsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.robot_id):
            query['RobotId'] = request.robot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRobotParams',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListRobotParamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_robot_params(
        self,
        request: aiccs_20191015_models.ListRobotParamsRequest,
    ) -> aiccs_20191015_models.ListRobotParamsResponse:
        """
        @summary 查询参数列表
        
        @param request: ListRobotParamsRequest
        @return: ListRobotParamsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_robot_params_with_options(request, runtime)

    async def list_robot_params_async(
        self,
        request: aiccs_20191015_models.ListRobotParamsRequest,
    ) -> aiccs_20191015_models.ListRobotParamsResponse:
        """
        @summary 查询参数列表
        
        @param request: ListRobotParamsRequest
        @return: ListRobotParamsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_robot_params_with_options_async(request, runtime)

    def list_roles_with_options(
        self,
        request: aiccs_20191015_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListRolesResponse:
        """
        @summary 获取租户下的所有角色
        
        @param request: ListRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRolesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        request: aiccs_20191015_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListRolesResponse:
        """
        @summary 获取租户下的所有角色
        
        @param request: ListRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRolesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_roles(
        self,
        request: aiccs_20191015_models.ListRolesRequest,
    ) -> aiccs_20191015_models.ListRolesResponse:
        """
        @summary 获取租户下的所有角色
        
        @param request: ListRolesRequest
        @return: ListRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_roles_with_options(request, runtime)

    async def list_roles_async(
        self,
        request: aiccs_20191015_models.ListRolesRequest,
    ) -> aiccs_20191015_models.ListRolesResponse:
        """
        @summary 获取租户下的所有角色
        
        @param request: ListRolesRequest
        @return: ListRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_roles_with_options_async(request, runtime)

    def list_skill_group_with_options(
        self,
        request: aiccs_20191015_models.ListSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListSkillGroupResponse:
        """
        @param request: ListSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSkillGroup',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_skill_group_with_options_async(
        self,
        request: aiccs_20191015_models.ListSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListSkillGroupResponse:
        """
        @param request: ListSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSkillGroup',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_skill_group(
        self,
        request: aiccs_20191015_models.ListSkillGroupRequest,
    ) -> aiccs_20191015_models.ListSkillGroupResponse:
        """
        @param request: ListSkillGroupRequest
        @return: ListSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_skill_group_with_options(request, runtime)

    async def list_skill_group_async(
        self,
        request: aiccs_20191015_models.ListSkillGroupRequest,
    ) -> aiccs_20191015_models.ListSkillGroupResponse:
        """
        @param request: ListSkillGroupRequest
        @return: ListSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_skill_group_with_options_async(request, runtime)

    def list_task_with_options(
        self,
        request: aiccs_20191015_models.ListTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListTaskResponse:
        """
        @summary 查询任务列表
        
        @param request: ListTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.robot_name):
            query['RobotName'] = request.robot_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_with_options_async(
        self,
        request: aiccs_20191015_models.ListTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListTaskResponse:
        """
        @summary 查询任务列表
        
        @param request: ListTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.robot_name):
            query['RobotName'] = request.robot_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task(
        self,
        request: aiccs_20191015_models.ListTaskRequest,
    ) -> aiccs_20191015_models.ListTaskResponse:
        """
        @summary 查询任务列表
        
        @param request: ListTaskRequest
        @return: ListTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_task_with_options(request, runtime)

    async def list_task_async(
        self,
        request: aiccs_20191015_models.ListTaskRequest,
    ) -> aiccs_20191015_models.ListTaskResponse:
        """
        @summary 查询任务列表
        
        @param request: ListTaskRequest
        @return: ListTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_task_with_options_async(request, runtime)

    def list_task_detail_with_options(
        self,
        request: aiccs_20191015_models.ListTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListTaskDetailResponse:
        """
        @summary 任务详情查看通话列表
        
        @param request: ListTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTaskDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called):
            query['Called'] = request.called
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.status_code):
            query['StatusCode'] = request.status_code
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskDetail',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_detail_with_options_async(
        self,
        request: aiccs_20191015_models.ListTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListTaskDetailResponse:
        """
        @summary 任务详情查看通话列表
        
        @param request: ListTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTaskDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called):
            query['Called'] = request.called
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.status_code):
            query['StatusCode'] = request.status_code
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskDetail',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task_detail(
        self,
        request: aiccs_20191015_models.ListTaskDetailRequest,
    ) -> aiccs_20191015_models.ListTaskDetailResponse:
        """
        @summary 任务详情查看通话列表
        
        @param request: ListTaskDetailRequest
        @return: ListTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_task_detail_with_options(request, runtime)

    async def list_task_detail_async(
        self,
        request: aiccs_20191015_models.ListTaskDetailRequest,
    ) -> aiccs_20191015_models.ListTaskDetailResponse:
        """
        @summary 任务详情查看通话列表
        
        @param request: ListTaskDetailRequest
        @return: ListTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_task_detail_with_options_async(request, runtime)

    def llm_smart_call_with_options(
        self,
        tmp_req: aiccs_20191015_models.LlmSmartCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.LlmSmartCallResponse:
        """
        @summary 基于大模型的智能外呼
        
        @param tmp_req: LlmSmartCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LlmSmartCallResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.LlmSmartCallShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_param):
            request.biz_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_param, 'BizParam', 'json')
        if not UtilClient.is_unset(tmp_req.prompt_param):
            request.prompt_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.prompt_param, 'PromptParam', 'json')
        if not UtilClient.is_unset(tmp_req.start_word_param):
            request.start_word_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start_word_param, 'StartWordParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.application_code):
            query['ApplicationCode'] = request.application_code
        if not UtilClient.is_unset(request.biz_param_shrink):
            query['BizParam'] = request.biz_param_shrink
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.caller_number):
            query['CallerNumber'] = request.caller_number
        if not UtilClient.is_unset(request.customer_line_code):
            query['CustomerLineCode'] = request.customer_line_code
        if not UtilClient.is_unset(request.extension):
            query['Extension'] = request.extension
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.prompt_param_shrink):
            query['PromptParam'] = request.prompt_param_shrink
        if not UtilClient.is_unset(request.session_timeout):
            query['SessionTimeout'] = request.session_timeout
        if not UtilClient.is_unset(request.start_word_param_shrink):
            query['StartWordParam'] = request.start_word_param_shrink
        if not UtilClient.is_unset(request.tts_speed):
            query['TtsSpeed'] = request.tts_speed
        if not UtilClient.is_unset(request.tts_voice_code):
            query['TtsVoiceCode'] = request.tts_voice_code
        if not UtilClient.is_unset(request.tts_volume):
            query['TtsVolume'] = request.tts_volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LlmSmartCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.LlmSmartCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def llm_smart_call_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.LlmSmartCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.LlmSmartCallResponse:
        """
        @summary 基于大模型的智能外呼
        
        @param tmp_req: LlmSmartCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LlmSmartCallResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.LlmSmartCallShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_param):
            request.biz_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_param, 'BizParam', 'json')
        if not UtilClient.is_unset(tmp_req.prompt_param):
            request.prompt_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.prompt_param, 'PromptParam', 'json')
        if not UtilClient.is_unset(tmp_req.start_word_param):
            request.start_word_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start_word_param, 'StartWordParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.application_code):
            query['ApplicationCode'] = request.application_code
        if not UtilClient.is_unset(request.biz_param_shrink):
            query['BizParam'] = request.biz_param_shrink
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.caller_number):
            query['CallerNumber'] = request.caller_number
        if not UtilClient.is_unset(request.customer_line_code):
            query['CustomerLineCode'] = request.customer_line_code
        if not UtilClient.is_unset(request.extension):
            query['Extension'] = request.extension
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.prompt_param_shrink):
            query['PromptParam'] = request.prompt_param_shrink
        if not UtilClient.is_unset(request.session_timeout):
            query['SessionTimeout'] = request.session_timeout
        if not UtilClient.is_unset(request.start_word_param_shrink):
            query['StartWordParam'] = request.start_word_param_shrink
        if not UtilClient.is_unset(request.tts_speed):
            query['TtsSpeed'] = request.tts_speed
        if not UtilClient.is_unset(request.tts_voice_code):
            query['TtsVoiceCode'] = request.tts_voice_code
        if not UtilClient.is_unset(request.tts_volume):
            query['TtsVolume'] = request.tts_volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LlmSmartCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.LlmSmartCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def llm_smart_call(
        self,
        request: aiccs_20191015_models.LlmSmartCallRequest,
    ) -> aiccs_20191015_models.LlmSmartCallResponse:
        """
        @summary 基于大模型的智能外呼
        
        @param request: LlmSmartCallRequest
        @return: LlmSmartCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.llm_smart_call_with_options(request, runtime)

    async def llm_smart_call_async(
        self,
        request: aiccs_20191015_models.LlmSmartCallRequest,
    ) -> aiccs_20191015_models.LlmSmartCallResponse:
        """
        @summary 基于大模型的智能外呼
        
        @param request: LlmSmartCallRequest
        @return: LlmSmartCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.llm_smart_call_with_options_async(request, runtime)

    def llm_smart_call_encrypt_with_options(
        self,
        tmp_req: aiccs_20191015_models.LlmSmartCallEncryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.LlmSmartCallEncryptResponse:
        """
        @summary 大模型外呼加密号码接口
        
        @param tmp_req: LlmSmartCallEncryptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LlmSmartCallEncryptResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.LlmSmartCallEncryptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.prompt_param):
            request.prompt_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.prompt_param, 'PromptParam', 'json')
        if not UtilClient.is_unset(tmp_req.start_word_param):
            request.start_word_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start_word_param, 'StartWordParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.application_code):
            query['ApplicationCode'] = request.application_code
        if not UtilClient.is_unset(request.caller_number):
            query['CallerNumber'] = request.caller_number
        if not UtilClient.is_unset(request.encrypt_called_number):
            query['EncryptCalledNumber'] = request.encrypt_called_number
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prompt_param_shrink):
            query['PromptParam'] = request.prompt_param_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_word_param_shrink):
            query['StartWordParam'] = request.start_word_param_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LlmSmartCallEncrypt',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.LlmSmartCallEncryptResponse(),
            self.call_api(params, req, runtime)
        )

    async def llm_smart_call_encrypt_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.LlmSmartCallEncryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.LlmSmartCallEncryptResponse:
        """
        @summary 大模型外呼加密号码接口
        
        @param tmp_req: LlmSmartCallEncryptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LlmSmartCallEncryptResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.LlmSmartCallEncryptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.prompt_param):
            request.prompt_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.prompt_param, 'PromptParam', 'json')
        if not UtilClient.is_unset(tmp_req.start_word_param):
            request.start_word_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start_word_param, 'StartWordParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.application_code):
            query['ApplicationCode'] = request.application_code
        if not UtilClient.is_unset(request.caller_number):
            query['CallerNumber'] = request.caller_number
        if not UtilClient.is_unset(request.encrypt_called_number):
            query['EncryptCalledNumber'] = request.encrypt_called_number
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prompt_param_shrink):
            query['PromptParam'] = request.prompt_param_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_word_param_shrink):
            query['StartWordParam'] = request.start_word_param_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LlmSmartCallEncrypt',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.LlmSmartCallEncryptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def llm_smart_call_encrypt(
        self,
        request: aiccs_20191015_models.LlmSmartCallEncryptRequest,
    ) -> aiccs_20191015_models.LlmSmartCallEncryptResponse:
        """
        @summary 大模型外呼加密号码接口
        
        @param request: LlmSmartCallEncryptRequest
        @return: LlmSmartCallEncryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.llm_smart_call_encrypt_with_options(request, runtime)

    async def llm_smart_call_encrypt_async(
        self,
        request: aiccs_20191015_models.LlmSmartCallEncryptRequest,
    ) -> aiccs_20191015_models.LlmSmartCallEncryptResponse:
        """
        @summary 大模型外呼加密号码接口
        
        @param request: LlmSmartCallEncryptRequest
        @return: LlmSmartCallEncryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.llm_smart_call_encrypt_with_options_async(request, runtime)

    def make_call_with_options(
        self,
        request: aiccs_20191015_models.MakeCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.MakeCallResponse:
        """
        @param request: MakeCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MakeCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.command_code):
            query['CommandCode'] = request.command_code
        if not UtilClient.is_unset(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.outer_account_id):
            query['OuterAccountId'] = request.outer_account_id
        if not UtilClient.is_unset(request.outer_account_type):
            query['OuterAccountType'] = request.outer_account_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MakeCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.MakeCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def make_call_with_options_async(
        self,
        request: aiccs_20191015_models.MakeCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.MakeCallResponse:
        """
        @param request: MakeCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MakeCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.command_code):
            query['CommandCode'] = request.command_code
        if not UtilClient.is_unset(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.outer_account_id):
            query['OuterAccountId'] = request.outer_account_id
        if not UtilClient.is_unset(request.outer_account_type):
            query['OuterAccountType'] = request.outer_account_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MakeCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.MakeCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def make_call(
        self,
        request: aiccs_20191015_models.MakeCallRequest,
    ) -> aiccs_20191015_models.MakeCallResponse:
        """
        @param request: MakeCallRequest
        @return: MakeCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.make_call_with_options(request, runtime)

    async def make_call_async(
        self,
        request: aiccs_20191015_models.MakeCallRequest,
    ) -> aiccs_20191015_models.MakeCallResponse:
        """
        @param request: MakeCallRequest
        @return: MakeCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.make_call_with_options_async(request, runtime)

    def make_double_call_with_options(
        self,
        request: aiccs_20191015_models.MakeDoubleCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.MakeDoubleCallResponse:
        """
        @summary 移动端发起呼叫
        
        @param request: MakeDoubleCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MakeDoubleCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.biz_data):
            query['BizData'] = request.biz_data
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.member_phone):
            query['MemberPhone'] = request.member_phone
        if not UtilClient.is_unset(request.outbound_call_number):
            query['OutboundCallNumber'] = request.outbound_call_number
        if not UtilClient.is_unset(request.servicer_phone):
            query['ServicerPhone'] = request.servicer_phone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MakeDoubleCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.MakeDoubleCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def make_double_call_with_options_async(
        self,
        request: aiccs_20191015_models.MakeDoubleCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.MakeDoubleCallResponse:
        """
        @summary 移动端发起呼叫
        
        @param request: MakeDoubleCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MakeDoubleCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.biz_data):
            query['BizData'] = request.biz_data
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.member_phone):
            query['MemberPhone'] = request.member_phone
        if not UtilClient.is_unset(request.outbound_call_number):
            query['OutboundCallNumber'] = request.outbound_call_number
        if not UtilClient.is_unset(request.servicer_phone):
            query['ServicerPhone'] = request.servicer_phone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MakeDoubleCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.MakeDoubleCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def make_double_call(
        self,
        request: aiccs_20191015_models.MakeDoubleCallRequest,
    ) -> aiccs_20191015_models.MakeDoubleCallResponse:
        """
        @summary 移动端发起呼叫
        
        @param request: MakeDoubleCallRequest
        @return: MakeDoubleCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.make_double_call_with_options(request, runtime)

    async def make_double_call_async(
        self,
        request: aiccs_20191015_models.MakeDoubleCallRequest,
    ) -> aiccs_20191015_models.MakeDoubleCallResponse:
        """
        @summary 移动端发起呼叫
        
        @param request: MakeDoubleCallRequest
        @return: MakeDoubleCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.make_double_call_with_options_async(request, runtime)

    def query_ai_call_detail_page_with_options(
        self,
        request: aiccs_20191015_models.QueryAiCallDetailPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryAiCallDetailPageResponse:
        """
        @summary 查询明细记录
        
        @param request: QueryAiCallDetailPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAiCallDetailPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.call_result):
            query['CallResult'] = request.call_result
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.end_calling_time):
            query['EndCallingTime'] = request.end_calling_time
        if not UtilClient.is_unset(request.end_imported_time):
            query['EndImportedTime'] = request.end_imported_time
        if not UtilClient.is_unset(request.major_intent):
            query['MajorIntent'] = request.major_intent
        if not UtilClient.is_unset(request.max_conversation_duration):
            query['MaxConversationDuration'] = request.max_conversation_duration
        if not UtilClient.is_unset(request.min_conversation_duration):
            query['MinConversationDuration'] = request.min_conversation_duration
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_calling_time):
            query['StartCallingTime'] = request.start_calling_time
        if not UtilClient.is_unset(request.start_imported_time):
            query['StartImportedTime'] = request.start_imported_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAiCallDetailPage',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryAiCallDetailPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ai_call_detail_page_with_options_async(
        self,
        request: aiccs_20191015_models.QueryAiCallDetailPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryAiCallDetailPageResponse:
        """
        @summary 查询明细记录
        
        @param request: QueryAiCallDetailPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAiCallDetailPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.call_result):
            query['CallResult'] = request.call_result
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.end_calling_time):
            query['EndCallingTime'] = request.end_calling_time
        if not UtilClient.is_unset(request.end_imported_time):
            query['EndImportedTime'] = request.end_imported_time
        if not UtilClient.is_unset(request.major_intent):
            query['MajorIntent'] = request.major_intent
        if not UtilClient.is_unset(request.max_conversation_duration):
            query['MaxConversationDuration'] = request.max_conversation_duration
        if not UtilClient.is_unset(request.min_conversation_duration):
            query['MinConversationDuration'] = request.min_conversation_duration
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_calling_time):
            query['StartCallingTime'] = request.start_calling_time
        if not UtilClient.is_unset(request.start_imported_time):
            query['StartImportedTime'] = request.start_imported_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAiCallDetailPage',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryAiCallDetailPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ai_call_detail_page(
        self,
        request: aiccs_20191015_models.QueryAiCallDetailPageRequest,
    ) -> aiccs_20191015_models.QueryAiCallDetailPageResponse:
        """
        @summary 查询明细记录
        
        @param request: QueryAiCallDetailPageRequest
        @return: QueryAiCallDetailPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_ai_call_detail_page_with_options(request, runtime)

    async def query_ai_call_detail_page_async(
        self,
        request: aiccs_20191015_models.QueryAiCallDetailPageRequest,
    ) -> aiccs_20191015_models.QueryAiCallDetailPageResponse:
        """
        @summary 查询明细记录
        
        @param request: QueryAiCallDetailPageRequest
        @return: QueryAiCallDetailPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_ai_call_detail_page_with_options_async(request, runtime)

    def query_ai_call_task_detail_with_options(
        self,
        request: aiccs_20191015_models.QueryAiCallTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryAiCallTaskDetailResponse:
        """
        @summary 查询任务详情
        
        @param request: QueryAiCallTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAiCallTaskDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAiCallTaskDetail',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryAiCallTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ai_call_task_detail_with_options_async(
        self,
        request: aiccs_20191015_models.QueryAiCallTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryAiCallTaskDetailResponse:
        """
        @summary 查询任务详情
        
        @param request: QueryAiCallTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAiCallTaskDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAiCallTaskDetail',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryAiCallTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ai_call_task_detail(
        self,
        request: aiccs_20191015_models.QueryAiCallTaskDetailRequest,
    ) -> aiccs_20191015_models.QueryAiCallTaskDetailResponse:
        """
        @summary 查询任务详情
        
        @param request: QueryAiCallTaskDetailRequest
        @return: QueryAiCallTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_ai_call_task_detail_with_options(request, runtime)

    async def query_ai_call_task_detail_async(
        self,
        request: aiccs_20191015_models.QueryAiCallTaskDetailRequest,
    ) -> aiccs_20191015_models.QueryAiCallTaskDetailResponse:
        """
        @summary 查询任务详情
        
        @param request: QueryAiCallTaskDetailRequest
        @return: QueryAiCallTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_ai_call_task_detail_with_options_async(request, runtime)

    def query_ai_call_task_page_with_options(
        self,
        request: aiccs_20191015_models.QueryAiCallTaskPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryAiCallTaskPageResponse:
        """
        @summary 查询任务列表
        
        @param request: QueryAiCallTaskPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAiCallTaskPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_name):
            query['AgentName'] = request.agent_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAiCallTaskPage',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryAiCallTaskPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ai_call_task_page_with_options_async(
        self,
        request: aiccs_20191015_models.QueryAiCallTaskPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryAiCallTaskPageResponse:
        """
        @summary 查询任务列表
        
        @param request: QueryAiCallTaskPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAiCallTaskPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_name):
            query['AgentName'] = request.agent_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAiCallTaskPage',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryAiCallTaskPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ai_call_task_page(
        self,
        request: aiccs_20191015_models.QueryAiCallTaskPageRequest,
    ) -> aiccs_20191015_models.QueryAiCallTaskPageResponse:
        """
        @summary 查询任务列表
        
        @param request: QueryAiCallTaskPageRequest
        @return: QueryAiCallTaskPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_ai_call_task_page_with_options(request, runtime)

    async def query_ai_call_task_page_async(
        self,
        request: aiccs_20191015_models.QueryAiCallTaskPageRequest,
    ) -> aiccs_20191015_models.QueryAiCallTaskPageResponse:
        """
        @summary 查询任务列表
        
        @param request: QueryAiCallTaskPageRequest
        @return: QueryAiCallTaskPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_ai_call_task_page_with_options_async(request, runtime)

    def query_conversation_detail_info_with_options(
        self,
        request: aiccs_20191015_models.QueryConversationDetailInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryConversationDetailInfoResponse:
        """
        @summary 查询通话详情信息
        
        @param request: QueryConversationDetailInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryConversationDetailInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.detail_id):
            query['DetailId'] = request.detail_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryConversationDetailInfo',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryConversationDetailInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_conversation_detail_info_with_options_async(
        self,
        request: aiccs_20191015_models.QueryConversationDetailInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryConversationDetailInfoResponse:
        """
        @summary 查询通话详情信息
        
        @param request: QueryConversationDetailInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryConversationDetailInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.detail_id):
            query['DetailId'] = request.detail_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryConversationDetailInfo',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryConversationDetailInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_conversation_detail_info(
        self,
        request: aiccs_20191015_models.QueryConversationDetailInfoRequest,
    ) -> aiccs_20191015_models.QueryConversationDetailInfoResponse:
        """
        @summary 查询通话详情信息
        
        @param request: QueryConversationDetailInfoRequest
        @return: QueryConversationDetailInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_conversation_detail_info_with_options(request, runtime)

    async def query_conversation_detail_info_async(
        self,
        request: aiccs_20191015_models.QueryConversationDetailInfoRequest,
    ) -> aiccs_20191015_models.QueryConversationDetailInfoResponse:
        """
        @summary 查询通话详情信息
        
        @param request: QueryConversationDetailInfoRequest
        @return: QueryConversationDetailInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_conversation_detail_info_with_options_async(request, runtime)

    def query_hotline_in_queue_with_options(
        self,
        request: aiccs_20191015_models.QueryHotlineInQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryHotlineInQueueResponse:
        """
        @param request: QueryHotlineInQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryHotlineInQueueResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryHotlineInQueue',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryHotlineInQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_hotline_in_queue_with_options_async(
        self,
        request: aiccs_20191015_models.QueryHotlineInQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryHotlineInQueueResponse:
        """
        @param request: QueryHotlineInQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryHotlineInQueueResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryHotlineInQueue',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryHotlineInQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_hotline_in_queue(
        self,
        request: aiccs_20191015_models.QueryHotlineInQueueRequest,
    ) -> aiccs_20191015_models.QueryHotlineInQueueResponse:
        """
        @param request: QueryHotlineInQueueRequest
        @return: QueryHotlineInQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_hotline_in_queue_with_options(request, runtime)

    async def query_hotline_in_queue_async(
        self,
        request: aiccs_20191015_models.QueryHotlineInQueueRequest,
    ) -> aiccs_20191015_models.QueryHotlineInQueueResponse:
        """
        @param request: QueryHotlineInQueueRequest
        @return: QueryHotlineInQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_hotline_in_queue_with_options_async(request, runtime)

    def query_hotline_number_with_options(
        self,
        tmp_req: aiccs_20191015_models.QueryHotlineNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryHotlineNumberResponse:
        """
        @summary 查询热线号码配置
        
        @param tmp_req: QueryHotlineNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryHotlineNumberResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.QueryHotlineNumberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryHotlineNumber',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryHotlineNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_hotline_number_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.QueryHotlineNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryHotlineNumberResponse:
        """
        @summary 查询热线号码配置
        
        @param tmp_req: QueryHotlineNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryHotlineNumberResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.QueryHotlineNumberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryHotlineNumber',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryHotlineNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_hotline_number(
        self,
        request: aiccs_20191015_models.QueryHotlineNumberRequest,
    ) -> aiccs_20191015_models.QueryHotlineNumberResponse:
        """
        @summary 查询热线号码配置
        
        @param request: QueryHotlineNumberRequest
        @return: QueryHotlineNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_hotline_number_with_options(request, runtime)

    async def query_hotline_number_async(
        self,
        request: aiccs_20191015_models.QueryHotlineNumberRequest,
    ) -> aiccs_20191015_models.QueryHotlineNumberResponse:
        """
        @summary 查询热线号码配置
        
        @param request: QueryHotlineNumberRequest
        @return: QueryHotlineNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_hotline_number_with_options_async(request, runtime)

    def query_outbound_task_with_options(
        self,
        request: aiccs_20191015_models.QueryOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryOutboundTaskResponse:
        """
        @param request: QueryOutboundTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOutboundTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ani):
            query['Ani'] = request.ani
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.skill_group):
            query['SkillGroup'] = request.skill_group
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOutboundTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryOutboundTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_outbound_task_with_options_async(
        self,
        request: aiccs_20191015_models.QueryOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryOutboundTaskResponse:
        """
        @param request: QueryOutboundTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOutboundTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ani):
            query['Ani'] = request.ani
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.skill_group):
            query['SkillGroup'] = request.skill_group
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOutboundTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryOutboundTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_outbound_task(
        self,
        request: aiccs_20191015_models.QueryOutboundTaskRequest,
    ) -> aiccs_20191015_models.QueryOutboundTaskResponse:
        """
        @param request: QueryOutboundTaskRequest
        @return: QueryOutboundTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_outbound_task_with_options(request, runtime)

    async def query_outbound_task_async(
        self,
        request: aiccs_20191015_models.QueryOutboundTaskRequest,
    ) -> aiccs_20191015_models.QueryOutboundTaskResponse:
        """
        @param request: QueryOutboundTaskRequest
        @return: QueryOutboundTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_outbound_task_with_options_async(request, runtime)

    def query_skill_groups_with_options(
        self,
        request: aiccs_20191015_models.QuerySkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QuerySkillGroupsResponse:
        """
        @param request: QuerySkillGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySkillGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySkillGroups',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QuerySkillGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_skill_groups_with_options_async(
        self,
        request: aiccs_20191015_models.QuerySkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QuerySkillGroupsResponse:
        """
        @param request: QuerySkillGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySkillGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySkillGroups',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QuerySkillGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_skill_groups(
        self,
        request: aiccs_20191015_models.QuerySkillGroupsRequest,
    ) -> aiccs_20191015_models.QuerySkillGroupsResponse:
        """
        @param request: QuerySkillGroupsRequest
        @return: QuerySkillGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_skill_groups_with_options(request, runtime)

    async def query_skill_groups_async(
        self,
        request: aiccs_20191015_models.QuerySkillGroupsRequest,
    ) -> aiccs_20191015_models.QuerySkillGroupsResponse:
        """
        @param request: QuerySkillGroupsRequest
        @return: QuerySkillGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_skill_groups_with_options_async(request, runtime)

    def query_task_detail_with_options(
        self,
        request: aiccs_20191015_models.QueryTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryTaskDetailResponse:
        """
        @param request: QueryTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTaskDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ani):
            query['Ani'] = request.ani
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.department_id_list):
            query['DepartmentIdList'] = request.department_id_list
        if not UtilClient.is_unset(request.dnis):
            query['Dnis'] = request.dnis
        if not UtilClient.is_unset(request.end_reason_list):
            query['EndReasonList'] = request.end_reason_list
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.outbound_task_id):
            query['OutboundTaskId'] = request.outbound_task_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.priority_list):
            query['PriorityList'] = request.priority_list
        if not UtilClient.is_unset(request.servicer_id):
            query['ServicerId'] = request.servicer_id
        if not UtilClient.is_unset(request.servicer_name):
            query['ServicerName'] = request.servicer_name
        if not UtilClient.is_unset(request.sid):
            query['Sid'] = request.sid
        if not UtilClient.is_unset(request.skill_group):
            query['SkillGroup'] = request.skill_group
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTaskDetail',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_task_detail_with_options_async(
        self,
        request: aiccs_20191015_models.QueryTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryTaskDetailResponse:
        """
        @param request: QueryTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTaskDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ani):
            query['Ani'] = request.ani
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.department_id_list):
            query['DepartmentIdList'] = request.department_id_list
        if not UtilClient.is_unset(request.dnis):
            query['Dnis'] = request.dnis
        if not UtilClient.is_unset(request.end_reason_list):
            query['EndReasonList'] = request.end_reason_list
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.outbound_task_id):
            query['OutboundTaskId'] = request.outbound_task_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.priority_list):
            query['PriorityList'] = request.priority_list
        if not UtilClient.is_unset(request.servicer_id):
            query['ServicerId'] = request.servicer_id
        if not UtilClient.is_unset(request.servicer_name):
            query['ServicerName'] = request.servicer_name
        if not UtilClient.is_unset(request.sid):
            query['Sid'] = request.sid
        if not UtilClient.is_unset(request.skill_group):
            query['SkillGroup'] = request.skill_group
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTaskDetail',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_task_detail(
        self,
        request: aiccs_20191015_models.QueryTaskDetailRequest,
    ) -> aiccs_20191015_models.QueryTaskDetailResponse:
        """
        @param request: QueryTaskDetailRequest
        @return: QueryTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_task_detail_with_options(request, runtime)

    async def query_task_detail_async(
        self,
        request: aiccs_20191015_models.QueryTaskDetailRequest,
    ) -> aiccs_20191015_models.QueryTaskDetailResponse:
        """
        @param request: QueryTaskDetailRequest
        @return: QueryTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_task_detail_with_options_async(request, runtime)

    def query_tickets_with_options(
        self,
        tmp_req: aiccs_20191015_models.QueryTicketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryTicketsResponse:
        """
        @param tmp_req: QueryTicketsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTicketsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.QueryTicketsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extra):
            request.extra_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra, 'Extra', 'json')
        body = {}
        if not UtilClient.is_unset(request.case_id):
            body['CaseId'] = request.case_id
        if not UtilClient.is_unset(request.case_status):
            body['CaseStatus'] = request.case_status
        if not UtilClient.is_unset(request.case_type):
            body['CaseType'] = request.case_type
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.channel_type):
            body['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.deal_id):
            body['DealId'] = request.deal_id
        if not UtilClient.is_unset(request.extra_shrink):
            body['Extra'] = request.extra_shrink
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sr_type):
            body['SrType'] = request.sr_type
        if not UtilClient.is_unset(request.task_status):
            body['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.touch_id):
            body['TouchId'] = request.touch_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryTickets',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryTicketsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tickets_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.QueryTicketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryTicketsResponse:
        """
        @param tmp_req: QueryTicketsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTicketsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.QueryTicketsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extra):
            request.extra_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra, 'Extra', 'json')
        body = {}
        if not UtilClient.is_unset(request.case_id):
            body['CaseId'] = request.case_id
        if not UtilClient.is_unset(request.case_status):
            body['CaseStatus'] = request.case_status
        if not UtilClient.is_unset(request.case_type):
            body['CaseType'] = request.case_type
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.channel_type):
            body['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.deal_id):
            body['DealId'] = request.deal_id
        if not UtilClient.is_unset(request.extra_shrink):
            body['Extra'] = request.extra_shrink
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sr_type):
            body['SrType'] = request.sr_type
        if not UtilClient.is_unset(request.task_status):
            body['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.touch_id):
            body['TouchId'] = request.touch_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryTickets',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryTicketsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_tickets(
        self,
        request: aiccs_20191015_models.QueryTicketsRequest,
    ) -> aiccs_20191015_models.QueryTicketsResponse:
        """
        @param request: QueryTicketsRequest
        @return: QueryTicketsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_tickets_with_options(request, runtime)

    async def query_tickets_async(
        self,
        request: aiccs_20191015_models.QueryTicketsRequest,
    ) -> aiccs_20191015_models.QueryTicketsResponse:
        """
        @param request: QueryTicketsRequest
        @return: QueryTicketsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_tickets_with_options_async(request, runtime)

    def query_touch_list_with_options(
        self,
        request: aiccs_20191015_models.QueryTouchListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryTouchListResponse:
        """
        @param request: QueryTouchListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTouchListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.channel_type):
            body['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.close_time_end):
            body['CloseTimeEnd'] = request.close_time_end
        if not UtilClient.is_unset(request.close_time_start):
            body['CloseTimeStart'] = request.close_time_start
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.evaluation_level):
            body['EvaluationLevel'] = request.evaluation_level
        if not UtilClient.is_unset(request.evaluation_score):
            body['EvaluationScore'] = request.evaluation_score
        if not UtilClient.is_unset(request.evaluation_status):
            body['EvaluationStatus'] = request.evaluation_status
        if not UtilClient.is_unset(request.first_time_end):
            body['FirstTimeEnd'] = request.first_time_end
        if not UtilClient.is_unset(request.first_time_start):
            body['FirstTimeStart'] = request.first_time_start
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.member_id):
            body['MemberId'] = request.member_id
        if not UtilClient.is_unset(request.member_name):
            body['MemberName'] = request.member_name
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.queue_id):
            body['QueueId'] = request.queue_id
        if not UtilClient.is_unset(request.servicer_id):
            body['ServicerId'] = request.servicer_id
        if not UtilClient.is_unset(request.servicer_name):
            body['ServicerName'] = request.servicer_name
        if not UtilClient.is_unset(request.touch_id):
            body['TouchId'] = request.touch_id
        if not UtilClient.is_unset(request.touch_type):
            body['TouchType'] = request.touch_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryTouchList',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryTouchListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_touch_list_with_options_async(
        self,
        request: aiccs_20191015_models.QueryTouchListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryTouchListResponse:
        """
        @param request: QueryTouchListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTouchListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.channel_type):
            body['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.close_time_end):
            body['CloseTimeEnd'] = request.close_time_end
        if not UtilClient.is_unset(request.close_time_start):
            body['CloseTimeStart'] = request.close_time_start
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.evaluation_level):
            body['EvaluationLevel'] = request.evaluation_level
        if not UtilClient.is_unset(request.evaluation_score):
            body['EvaluationScore'] = request.evaluation_score
        if not UtilClient.is_unset(request.evaluation_status):
            body['EvaluationStatus'] = request.evaluation_status
        if not UtilClient.is_unset(request.first_time_end):
            body['FirstTimeEnd'] = request.first_time_end
        if not UtilClient.is_unset(request.first_time_start):
            body['FirstTimeStart'] = request.first_time_start
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.member_id):
            body['MemberId'] = request.member_id
        if not UtilClient.is_unset(request.member_name):
            body['MemberName'] = request.member_name
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.queue_id):
            body['QueueId'] = request.queue_id
        if not UtilClient.is_unset(request.servicer_id):
            body['ServicerId'] = request.servicer_id
        if not UtilClient.is_unset(request.servicer_name):
            body['ServicerName'] = request.servicer_name
        if not UtilClient.is_unset(request.touch_id):
            body['TouchId'] = request.touch_id
        if not UtilClient.is_unset(request.touch_type):
            body['TouchType'] = request.touch_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryTouchList',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryTouchListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_touch_list(
        self,
        request: aiccs_20191015_models.QueryTouchListRequest,
    ) -> aiccs_20191015_models.QueryTouchListResponse:
        """
        @param request: QueryTouchListRequest
        @return: QueryTouchListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_touch_list_with_options(request, runtime)

    async def query_touch_list_async(
        self,
        request: aiccs_20191015_models.QueryTouchListRequest,
    ) -> aiccs_20191015_models.QueryTouchListResponse:
        """
        @param request: QueryTouchListRequest
        @return: QueryTouchListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_touch_list_with_options_async(request, runtime)

    def remove_agent_from_skill_group_with_options(
        self,
        tmp_req: aiccs_20191015_models.RemoveAgentFromSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.RemoveAgentFromSkillGroupResponse:
        """
        @summary 从技能组中移除坐席
        
        @param tmp_req: RemoveAgentFromSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveAgentFromSkillGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.RemoveAgentFromSkillGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_ids_shrink):
            query['AgentIds'] = request.agent_ids_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAgentFromSkillGroup',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.RemoveAgentFromSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_agent_from_skill_group_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.RemoveAgentFromSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.RemoveAgentFromSkillGroupResponse:
        """
        @summary 从技能组中移除坐席
        
        @param tmp_req: RemoveAgentFromSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveAgentFromSkillGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.RemoveAgentFromSkillGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_ids_shrink):
            query['AgentIds'] = request.agent_ids_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAgentFromSkillGroup',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.RemoveAgentFromSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_agent_from_skill_group(
        self,
        request: aiccs_20191015_models.RemoveAgentFromSkillGroupRequest,
    ) -> aiccs_20191015_models.RemoveAgentFromSkillGroupResponse:
        """
        @summary 从技能组中移除坐席
        
        @param request: RemoveAgentFromSkillGroupRequest
        @return: RemoveAgentFromSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_agent_from_skill_group_with_options(request, runtime)

    async def remove_agent_from_skill_group_async(
        self,
        request: aiccs_20191015_models.RemoveAgentFromSkillGroupRequest,
    ) -> aiccs_20191015_models.RemoveAgentFromSkillGroupResponse:
        """
        @summary 从技能组中移除坐席
        
        @param request: RemoveAgentFromSkillGroupRequest
        @return: RemoveAgentFromSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_agent_from_skill_group_with_options_async(request, runtime)

    def remove_skill_group_with_options(
        self,
        request: aiccs_20191015_models.RemoveSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.RemoveSkillGroupResponse:
        """
        @param request: RemoveSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveSkillGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id):
            body['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveSkillGroup',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.RemoveSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_skill_group_with_options_async(
        self,
        request: aiccs_20191015_models.RemoveSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.RemoveSkillGroupResponse:
        """
        @param request: RemoveSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveSkillGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id):
            body['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveSkillGroup',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.RemoveSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_skill_group(
        self,
        request: aiccs_20191015_models.RemoveSkillGroupRequest,
    ) -> aiccs_20191015_models.RemoveSkillGroupResponse:
        """
        @param request: RemoveSkillGroupRequest
        @return: RemoveSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_skill_group_with_options(request, runtime)

    async def remove_skill_group_async(
        self,
        request: aiccs_20191015_models.RemoveSkillGroupRequest,
    ) -> aiccs_20191015_models.RemoveSkillGroupResponse:
        """
        @param request: RemoveSkillGroupRequest
        @return: RemoveSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_skill_group_with_options_async(request, runtime)

    def reset_hotline_number_with_options(
        self,
        tmp_req: aiccs_20191015_models.ResetHotlineNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ResetHotlineNumberResponse:
        """
        @summary 重置热线号码
        
        @param tmp_req: ResetHotlineNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetHotlineNumberResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.ResetHotlineNumberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.outbound_range_list):
            request.outbound_range_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.outbound_range_list, 'OutboundRangeList', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.enable_inbound):
            body['EnableInbound'] = request.enable_inbound
        if not UtilClient.is_unset(request.enable_inbound_evaluation):
            body['EnableInboundEvaluation'] = request.enable_inbound_evaluation
        if not UtilClient.is_unset(request.enable_outbound):
            body['EnableOutbound'] = request.enable_outbound
        if not UtilClient.is_unset(request.enable_outbound_evaluation):
            body['EnableOutboundEvaluation'] = request.enable_outbound_evaluation
        if not UtilClient.is_unset(request.evaluation_level):
            body['EvaluationLevel'] = request.evaluation_level
        if not UtilClient.is_unset(request.hotline_number):
            body['HotlineNumber'] = request.hotline_number
        if not UtilClient.is_unset(request.inbound_flow_id):
            body['InboundFlowId'] = request.inbound_flow_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.outbound_all_depart):
            body['OutboundAllDepart'] = request.outbound_all_depart
        if not UtilClient.is_unset(request.outbound_range_list_shrink):
            body['OutboundRangeList'] = request.outbound_range_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetHotlineNumber',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ResetHotlineNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_hotline_number_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.ResetHotlineNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ResetHotlineNumberResponse:
        """
        @summary 重置热线号码
        
        @param tmp_req: ResetHotlineNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetHotlineNumberResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.ResetHotlineNumberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.outbound_range_list):
            request.outbound_range_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.outbound_range_list, 'OutboundRangeList', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.enable_inbound):
            body['EnableInbound'] = request.enable_inbound
        if not UtilClient.is_unset(request.enable_inbound_evaluation):
            body['EnableInboundEvaluation'] = request.enable_inbound_evaluation
        if not UtilClient.is_unset(request.enable_outbound):
            body['EnableOutbound'] = request.enable_outbound
        if not UtilClient.is_unset(request.enable_outbound_evaluation):
            body['EnableOutboundEvaluation'] = request.enable_outbound_evaluation
        if not UtilClient.is_unset(request.evaluation_level):
            body['EvaluationLevel'] = request.evaluation_level
        if not UtilClient.is_unset(request.hotline_number):
            body['HotlineNumber'] = request.hotline_number
        if not UtilClient.is_unset(request.inbound_flow_id):
            body['InboundFlowId'] = request.inbound_flow_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.outbound_all_depart):
            body['OutboundAllDepart'] = request.outbound_all_depart
        if not UtilClient.is_unset(request.outbound_range_list_shrink):
            body['OutboundRangeList'] = request.outbound_range_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetHotlineNumber',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ResetHotlineNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_hotline_number(
        self,
        request: aiccs_20191015_models.ResetHotlineNumberRequest,
    ) -> aiccs_20191015_models.ResetHotlineNumberResponse:
        """
        @summary 重置热线号码
        
        @param request: ResetHotlineNumberRequest
        @return: ResetHotlineNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_hotline_number_with_options(request, runtime)

    async def reset_hotline_number_async(
        self,
        request: aiccs_20191015_models.ResetHotlineNumberRequest,
    ) -> aiccs_20191015_models.ResetHotlineNumberResponse:
        """
        @summary 重置热线号码
        
        @param request: ResetHotlineNumberRequest
        @return: ResetHotlineNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_hotline_number_with_options_async(request, runtime)

    def restart_outbound_task_with_options(
        self,
        request: aiccs_20191015_models.RestartOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.RestartOutboundTaskResponse:
        """
        @param request: RestartOutboundTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartOutboundTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.outbound_task_id):
            query['OutboundTaskId'] = request.outbound_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartOutboundTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.RestartOutboundTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_outbound_task_with_options_async(
        self,
        request: aiccs_20191015_models.RestartOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.RestartOutboundTaskResponse:
        """
        @param request: RestartOutboundTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartOutboundTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.outbound_task_id):
            query['OutboundTaskId'] = request.outbound_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartOutboundTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.RestartOutboundTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_outbound_task(
        self,
        request: aiccs_20191015_models.RestartOutboundTaskRequest,
    ) -> aiccs_20191015_models.RestartOutboundTaskResponse:
        """
        @param request: RestartOutboundTaskRequest
        @return: RestartOutboundTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_outbound_task_with_options(request, runtime)

    async def restart_outbound_task_async(
        self,
        request: aiccs_20191015_models.RestartOutboundTaskRequest,
    ) -> aiccs_20191015_models.RestartOutboundTaskResponse:
        """
        @param request: RestartOutboundTaskRequest
        @return: RestartOutboundTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_outbound_task_with_options_async(request, runtime)

    def robot_call_with_options(
        self,
        request: aiccs_20191015_models.RobotCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.RobotCallResponse:
        """
        @param request: RobotCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RobotCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not UtilClient.is_unset(request.early_media_asr):
            query['EarlyMediaAsr'] = request.early_media_asr
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.record_flag):
            query['RecordFlag'] = request.record_flag
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.robot_id):
            query['RobotId'] = request.robot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RobotCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.RobotCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def robot_call_with_options_async(
        self,
        request: aiccs_20191015_models.RobotCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.RobotCallResponse:
        """
        @param request: RobotCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RobotCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not UtilClient.is_unset(request.early_media_asr):
            query['EarlyMediaAsr'] = request.early_media_asr
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.record_flag):
            query['RecordFlag'] = request.record_flag
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.robot_id):
            query['RobotId'] = request.robot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RobotCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.RobotCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def robot_call(
        self,
        request: aiccs_20191015_models.RobotCallRequest,
    ) -> aiccs_20191015_models.RobotCallResponse:
        """
        @param request: RobotCallRequest
        @return: RobotCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.robot_call_with_options(request, runtime)

    async def robot_call_async(
        self,
        request: aiccs_20191015_models.RobotCallRequest,
    ) -> aiccs_20191015_models.RobotCallResponse:
        """
        @param request: RobotCallRequest
        @return: RobotCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.robot_call_with_options_async(request, runtime)

    def send_cco_smart_call_with_options(
        self,
        request: aiccs_20191015_models.SendCcoSmartCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.SendCcoSmartCallResponse:
        """
        @param request: SendCcoSmartCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendCcoSmartCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_code_break):
            query['ActionCodeBreak'] = request.action_code_break
        if not UtilClient.is_unset(request.action_code_time_break):
            query['ActionCodeTimeBreak'] = request.action_code_time_break
        if not UtilClient.is_unset(request.asr_als_am_id):
            query['AsrAlsAmId'] = request.asr_als_am_id
        if not UtilClient.is_unset(request.asr_base_id):
            query['AsrBaseId'] = request.asr_base_id
        if not UtilClient.is_unset(request.asr_model_id):
            query['AsrModelId'] = request.asr_model_id
        if not UtilClient.is_unset(request.asr_vocabulary_id):
            query['AsrVocabularyId'] = request.asr_vocabulary_id
        if not UtilClient.is_unset(request.background_file_code):
            query['BackgroundFileCode'] = request.background_file_code
        if not UtilClient.is_unset(request.background_speed):
            query['BackgroundSpeed'] = request.background_speed
        if not UtilClient.is_unset(request.background_volume):
            query['BackgroundVolume'] = request.background_volume
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not UtilClient.is_unset(request.dynamic_id):
            query['DynamicId'] = request.dynamic_id
        if not UtilClient.is_unset(request.early_media_asr):
            query['EarlyMediaAsr'] = request.early_media_asr
        if not UtilClient.is_unset(request.enable_itn):
            query['EnableITN'] = request.enable_itn
        if not UtilClient.is_unset(request.mute_time):
            query['MuteTime'] = request.mute_time
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pause_time):
            query['PauseTime'] = request.pause_time
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.record_flag):
            query['RecordFlag'] = request.record_flag
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.session_timeout):
            query['SessionTimeout'] = request.session_timeout
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.tts_conf):
            query['TtsConf'] = request.tts_conf
        if not UtilClient.is_unset(request.tts_speed):
            query['TtsSpeed'] = request.tts_speed
        if not UtilClient.is_unset(request.tts_style):
            query['TtsStyle'] = request.tts_style
        if not UtilClient.is_unset(request.tts_volume):
            query['TtsVolume'] = request.tts_volume
        if not UtilClient.is_unset(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not UtilClient.is_unset(request.voice_code_param):
            query['VoiceCodeParam'] = request.voice_code_param
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendCcoSmartCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SendCcoSmartCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_cco_smart_call_with_options_async(
        self,
        request: aiccs_20191015_models.SendCcoSmartCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.SendCcoSmartCallResponse:
        """
        @param request: SendCcoSmartCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendCcoSmartCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_code_break):
            query['ActionCodeBreak'] = request.action_code_break
        if not UtilClient.is_unset(request.action_code_time_break):
            query['ActionCodeTimeBreak'] = request.action_code_time_break
        if not UtilClient.is_unset(request.asr_als_am_id):
            query['AsrAlsAmId'] = request.asr_als_am_id
        if not UtilClient.is_unset(request.asr_base_id):
            query['AsrBaseId'] = request.asr_base_id
        if not UtilClient.is_unset(request.asr_model_id):
            query['AsrModelId'] = request.asr_model_id
        if not UtilClient.is_unset(request.asr_vocabulary_id):
            query['AsrVocabularyId'] = request.asr_vocabulary_id
        if not UtilClient.is_unset(request.background_file_code):
            query['BackgroundFileCode'] = request.background_file_code
        if not UtilClient.is_unset(request.background_speed):
            query['BackgroundSpeed'] = request.background_speed
        if not UtilClient.is_unset(request.background_volume):
            query['BackgroundVolume'] = request.background_volume
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not UtilClient.is_unset(request.dynamic_id):
            query['DynamicId'] = request.dynamic_id
        if not UtilClient.is_unset(request.early_media_asr):
            query['EarlyMediaAsr'] = request.early_media_asr
        if not UtilClient.is_unset(request.enable_itn):
            query['EnableITN'] = request.enable_itn
        if not UtilClient.is_unset(request.mute_time):
            query['MuteTime'] = request.mute_time
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pause_time):
            query['PauseTime'] = request.pause_time
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.record_flag):
            query['RecordFlag'] = request.record_flag
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.session_timeout):
            query['SessionTimeout'] = request.session_timeout
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.tts_conf):
            query['TtsConf'] = request.tts_conf
        if not UtilClient.is_unset(request.tts_speed):
            query['TtsSpeed'] = request.tts_speed
        if not UtilClient.is_unset(request.tts_style):
            query['TtsStyle'] = request.tts_style
        if not UtilClient.is_unset(request.tts_volume):
            query['TtsVolume'] = request.tts_volume
        if not UtilClient.is_unset(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not UtilClient.is_unset(request.voice_code_param):
            query['VoiceCodeParam'] = request.voice_code_param
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendCcoSmartCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SendCcoSmartCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_cco_smart_call(
        self,
        request: aiccs_20191015_models.SendCcoSmartCallRequest,
    ) -> aiccs_20191015_models.SendCcoSmartCallResponse:
        """
        @param request: SendCcoSmartCallRequest
        @return: SendCcoSmartCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_cco_smart_call_with_options(request, runtime)

    async def send_cco_smart_call_async(
        self,
        request: aiccs_20191015_models.SendCcoSmartCallRequest,
    ) -> aiccs_20191015_models.SendCcoSmartCallResponse:
        """
        @param request: SendCcoSmartCallRequest
        @return: SendCcoSmartCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_cco_smart_call_with_options_async(request, runtime)

    def send_cco_smart_call_operate_with_options(
        self,
        request: aiccs_20191015_models.SendCcoSmartCallOperateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.SendCcoSmartCallOperateResponse:
        """
        @param request: SendCcoSmartCallOperateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendCcoSmartCallOperateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendCcoSmartCallOperate',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SendCcoSmartCallOperateResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_cco_smart_call_operate_with_options_async(
        self,
        request: aiccs_20191015_models.SendCcoSmartCallOperateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.SendCcoSmartCallOperateResponse:
        """
        @param request: SendCcoSmartCallOperateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendCcoSmartCallOperateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendCcoSmartCallOperate',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SendCcoSmartCallOperateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_cco_smart_call_operate(
        self,
        request: aiccs_20191015_models.SendCcoSmartCallOperateRequest,
    ) -> aiccs_20191015_models.SendCcoSmartCallOperateResponse:
        """
        @param request: SendCcoSmartCallOperateRequest
        @return: SendCcoSmartCallOperateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_cco_smart_call_operate_with_options(request, runtime)

    async def send_cco_smart_call_operate_async(
        self,
        request: aiccs_20191015_models.SendCcoSmartCallOperateRequest,
    ) -> aiccs_20191015_models.SendCcoSmartCallOperateResponse:
        """
        @param request: SendCcoSmartCallOperateRequest
        @return: SendCcoSmartCallOperateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_cco_smart_call_operate_with_options_async(request, runtime)

    def send_hotline_heart_beat_with_options(
        self,
        request: aiccs_20191015_models.SendHotlineHeartBeatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.SendHotlineHeartBeatResponse:
        """
        @param request: SendHotlineHeartBeatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendHotlineHeartBeatResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendHotlineHeartBeat',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SendHotlineHeartBeatResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_hotline_heart_beat_with_options_async(
        self,
        request: aiccs_20191015_models.SendHotlineHeartBeatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.SendHotlineHeartBeatResponse:
        """
        @param request: SendHotlineHeartBeatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendHotlineHeartBeatResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendHotlineHeartBeat',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SendHotlineHeartBeatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_hotline_heart_beat(
        self,
        request: aiccs_20191015_models.SendHotlineHeartBeatRequest,
    ) -> aiccs_20191015_models.SendHotlineHeartBeatResponse:
        """
        @param request: SendHotlineHeartBeatRequest
        @return: SendHotlineHeartBeatResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_hotline_heart_beat_with_options(request, runtime)

    async def send_hotline_heart_beat_async(
        self,
        request: aiccs_20191015_models.SendHotlineHeartBeatRequest,
    ) -> aiccs_20191015_models.SendHotlineHeartBeatResponse:
        """
        @param request: SendHotlineHeartBeatRequest
        @return: SendHotlineHeartBeatResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_hotline_heart_beat_with_options_async(request, runtime)

    def start_ai_call_task_with_options(
        self,
        request: aiccs_20191015_models.StartAiCallTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartAiCallTaskResponse:
        """
        @summary 启动任务
        
        @param request: StartAiCallTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartAiCallTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartAiCallTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartAiCallTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_ai_call_task_with_options_async(
        self,
        request: aiccs_20191015_models.StartAiCallTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartAiCallTaskResponse:
        """
        @summary 启动任务
        
        @param request: StartAiCallTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartAiCallTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartAiCallTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartAiCallTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_ai_call_task(
        self,
        request: aiccs_20191015_models.StartAiCallTaskRequest,
    ) -> aiccs_20191015_models.StartAiCallTaskResponse:
        """
        @summary 启动任务
        
        @param request: StartAiCallTaskRequest
        @return: StartAiCallTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_ai_call_task_with_options(request, runtime)

    async def start_ai_call_task_async(
        self,
        request: aiccs_20191015_models.StartAiCallTaskRequest,
    ) -> aiccs_20191015_models.StartAiCallTaskResponse:
        """
        @summary 启动任务
        
        @param request: StartAiCallTaskRequest
        @return: StartAiCallTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_ai_call_task_with_options_async(request, runtime)

    def start_ai_outbound_task_with_options(
        self,
        request: aiccs_20191015_models.StartAiOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartAiOutboundTaskResponse:
        """
        @summary 启动智能外呼任务
        
        @param request: StartAiOutboundTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartAiOutboundTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartAiOutboundTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartAiOutboundTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_ai_outbound_task_with_options_async(
        self,
        request: aiccs_20191015_models.StartAiOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartAiOutboundTaskResponse:
        """
        @summary 启动智能外呼任务
        
        @param request: StartAiOutboundTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartAiOutboundTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartAiOutboundTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartAiOutboundTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_ai_outbound_task(
        self,
        request: aiccs_20191015_models.StartAiOutboundTaskRequest,
    ) -> aiccs_20191015_models.StartAiOutboundTaskResponse:
        """
        @summary 启动智能外呼任务
        
        @param request: StartAiOutboundTaskRequest
        @return: StartAiOutboundTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_ai_outbound_task_with_options(request, runtime)

    async def start_ai_outbound_task_async(
        self,
        request: aiccs_20191015_models.StartAiOutboundTaskRequest,
    ) -> aiccs_20191015_models.StartAiOutboundTaskResponse:
        """
        @summary 启动智能外呼任务
        
        @param request: StartAiOutboundTaskRequest
        @return: StartAiOutboundTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_ai_outbound_task_with_options_async(request, runtime)

    def start_call_with_options(
        self,
        request: aiccs_20191015_models.StartCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartCallResponse:
        """
        @param request: StartCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartCallResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.callee):
            body['Callee'] = request.callee
        if not UtilClient.is_unset(request.caller):
            body['Caller'] = request.caller
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_call_with_options_async(
        self,
        request: aiccs_20191015_models.StartCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartCallResponse:
        """
        @param request: StartCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartCallResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.callee):
            body['Callee'] = request.callee
        if not UtilClient.is_unset(request.caller):
            body['Caller'] = request.caller
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartCall',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_call(
        self,
        request: aiccs_20191015_models.StartCallRequest,
    ) -> aiccs_20191015_models.StartCallResponse:
        """
        @param request: StartCallRequest
        @return: StartCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_call_with_options(request, runtime)

    async def start_call_async(
        self,
        request: aiccs_20191015_models.StartCallRequest,
    ) -> aiccs_20191015_models.StartCallResponse:
        """
        @param request: StartCallRequest
        @return: StartCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_call_with_options_async(request, runtime)

    def start_call_v2with_options(
        self,
        request: aiccs_20191015_models.StartCallV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartCallV2Response:
        """
        @param request: StartCallV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartCallV2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.callee):
            body['Callee'] = request.callee
        if not UtilClient.is_unset(request.caller):
            body['Caller'] = request.caller
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartCallV2',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartCallV2Response(),
            self.call_api(params, req, runtime)
        )

    async def start_call_v2with_options_async(
        self,
        request: aiccs_20191015_models.StartCallV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartCallV2Response:
        """
        @param request: StartCallV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartCallV2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.callee):
            body['Callee'] = request.callee
        if not UtilClient.is_unset(request.caller):
            body['Caller'] = request.caller
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartCallV2',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartCallV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def start_call_v2(
        self,
        request: aiccs_20191015_models.StartCallV2Request,
    ) -> aiccs_20191015_models.StartCallV2Response:
        """
        @param request: StartCallV2Request
        @return: StartCallV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.start_call_v2with_options(request, runtime)

    async def start_call_v2_async(
        self,
        request: aiccs_20191015_models.StartCallV2Request,
    ) -> aiccs_20191015_models.StartCallV2Response:
        """
        @param request: StartCallV2Request
        @return: StartCallV2Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_call_v2with_options_async(request, runtime)

    def start_chat_work_with_options(
        self,
        request: aiccs_20191015_models.StartChatWorkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartChatWorkResponse:
        """
        @summary 修改在线客服为上班状态
        
        @param request: StartChatWorkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartChatWorkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartChatWork',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartChatWorkResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_chat_work_with_options_async(
        self,
        request: aiccs_20191015_models.StartChatWorkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartChatWorkResponse:
        """
        @summary 修改在线客服为上班状态
        
        @param request: StartChatWorkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartChatWorkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartChatWork',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartChatWorkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_chat_work(
        self,
        request: aiccs_20191015_models.StartChatWorkRequest,
    ) -> aiccs_20191015_models.StartChatWorkResponse:
        """
        @summary 修改在线客服为上班状态
        
        @param request: StartChatWorkRequest
        @return: StartChatWorkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_chat_work_with_options(request, runtime)

    async def start_chat_work_async(
        self,
        request: aiccs_20191015_models.StartChatWorkRequest,
    ) -> aiccs_20191015_models.StartChatWorkResponse:
        """
        @summary 修改在线客服为上班状态
        
        @param request: StartChatWorkRequest
        @return: StartChatWorkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_chat_work_with_options_async(request, runtime)

    def start_hotline_service_with_options(
        self,
        request: aiccs_20191015_models.StartHotlineServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartHotlineServiceResponse:
        """
        @param request: StartHotlineServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartHotlineServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartHotlineService',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartHotlineServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_hotline_service_with_options_async(
        self,
        request: aiccs_20191015_models.StartHotlineServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartHotlineServiceResponse:
        """
        @param request: StartHotlineServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartHotlineServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartHotlineService',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartHotlineServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_hotline_service(
        self,
        request: aiccs_20191015_models.StartHotlineServiceRequest,
    ) -> aiccs_20191015_models.StartHotlineServiceResponse:
        """
        @param request: StartHotlineServiceRequest
        @return: StartHotlineServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_hotline_service_with_options(request, runtime)

    async def start_hotline_service_async(
        self,
        request: aiccs_20191015_models.StartHotlineServiceRequest,
    ) -> aiccs_20191015_models.StartHotlineServiceResponse:
        """
        @param request: StartHotlineServiceRequest
        @return: StartHotlineServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_hotline_service_with_options_async(request, runtime)

    def start_micro_outbound_with_options(
        self,
        request: aiccs_20191015_models.StartMicroOutboundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartMicroOutboundResponse:
        """
        @param request: StartMicroOutboundRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartMicroOutboundResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.command_code):
            query['CommandCode'] = request.command_code
        if not UtilClient.is_unset(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartMicroOutbound',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartMicroOutboundResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_micro_outbound_with_options_async(
        self,
        request: aiccs_20191015_models.StartMicroOutboundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartMicroOutboundResponse:
        """
        @param request: StartMicroOutboundRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartMicroOutboundResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.command_code):
            query['CommandCode'] = request.command_code
        if not UtilClient.is_unset(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartMicroOutbound',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartMicroOutboundResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_micro_outbound(
        self,
        request: aiccs_20191015_models.StartMicroOutboundRequest,
    ) -> aiccs_20191015_models.StartMicroOutboundResponse:
        """
        @param request: StartMicroOutboundRequest
        @return: StartMicroOutboundResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_micro_outbound_with_options(request, runtime)

    async def start_micro_outbound_async(
        self,
        request: aiccs_20191015_models.StartMicroOutboundRequest,
    ) -> aiccs_20191015_models.StartMicroOutboundResponse:
        """
        @param request: StartMicroOutboundRequest
        @return: StartMicroOutboundResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_micro_outbound_with_options_async(request, runtime)

    def start_task_with_options(
        self,
        request: aiccs_20191015_models.StartTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartTaskResponse:
        """
        @summary 立即或定时启动智能外呼任务
        
        @param request: StartTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_now):
            query['StartNow'] = request.start_now
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_task_with_options_async(
        self,
        request: aiccs_20191015_models.StartTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartTaskResponse:
        """
        @summary 立即或定时启动智能外呼任务
        
        @param request: StartTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_now):
            query['StartNow'] = request.start_now
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_task(
        self,
        request: aiccs_20191015_models.StartTaskRequest,
    ) -> aiccs_20191015_models.StartTaskResponse:
        """
        @summary 立即或定时启动智能外呼任务
        
        @param request: StartTaskRequest
        @return: StartTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_task_with_options(request, runtime)

    async def start_task_async(
        self,
        request: aiccs_20191015_models.StartTaskRequest,
    ) -> aiccs_20191015_models.StartTaskResponse:
        """
        @summary 立即或定时启动智能外呼任务
        
        @param request: StartTaskRequest
        @return: StartTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_task_with_options_async(request, runtime)

    def stop_ai_call_task_with_options(
        self,
        request: aiccs_20191015_models.StopAiCallTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StopAiCallTaskResponse:
        """
        @summary 停止任务
        
        @param request: StopAiCallTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAiCallTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAiCallTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StopAiCallTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_ai_call_task_with_options_async(
        self,
        request: aiccs_20191015_models.StopAiCallTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StopAiCallTaskResponse:
        """
        @summary 停止任务
        
        @param request: StopAiCallTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAiCallTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAiCallTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StopAiCallTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_ai_call_task(
        self,
        request: aiccs_20191015_models.StopAiCallTaskRequest,
    ) -> aiccs_20191015_models.StopAiCallTaskResponse:
        """
        @summary 停止任务
        
        @param request: StopAiCallTaskRequest
        @return: StopAiCallTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_ai_call_task_with_options(request, runtime)

    async def stop_ai_call_task_async(
        self,
        request: aiccs_20191015_models.StopAiCallTaskRequest,
    ) -> aiccs_20191015_models.StopAiCallTaskResponse:
        """
        @summary 停止任务
        
        @param request: StopAiCallTaskRequest
        @return: StopAiCallTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_ai_call_task_with_options_async(request, runtime)

    def stop_ai_outbound_task_with_options(
        self,
        request: aiccs_20191015_models.StopAiOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StopAiOutboundTaskResponse:
        """
        @summary 手动暂停智能外呼任务
        
        @param request: StopAiOutboundTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAiOutboundTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAiOutboundTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StopAiOutboundTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_ai_outbound_task_with_options_async(
        self,
        request: aiccs_20191015_models.StopAiOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StopAiOutboundTaskResponse:
        """
        @summary 手动暂停智能外呼任务
        
        @param request: StopAiOutboundTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAiOutboundTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAiOutboundTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StopAiOutboundTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_ai_outbound_task(
        self,
        request: aiccs_20191015_models.StopAiOutboundTaskRequest,
    ) -> aiccs_20191015_models.StopAiOutboundTaskResponse:
        """
        @summary 手动暂停智能外呼任务
        
        @param request: StopAiOutboundTaskRequest
        @return: StopAiOutboundTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_ai_outbound_task_with_options(request, runtime)

    async def stop_ai_outbound_task_async(
        self,
        request: aiccs_20191015_models.StopAiOutboundTaskRequest,
    ) -> aiccs_20191015_models.StopAiOutboundTaskResponse:
        """
        @summary 手动暂停智能外呼任务
        
        @param request: StopAiOutboundTaskRequest
        @return: StopAiOutboundTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_ai_outbound_task_with_options_async(request, runtime)

    def stop_task_with_options(
        self,
        request: aiccs_20191015_models.StopTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StopTaskResponse:
        """
        @summary 暂停外呼任务
        
        @param request: StopTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StopTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_task_with_options_async(
        self,
        request: aiccs_20191015_models.StopTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StopTaskResponse:
        """
        @summary 暂停外呼任务
        
        @param request: StopTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StopTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_task(
        self,
        request: aiccs_20191015_models.StopTaskRequest,
    ) -> aiccs_20191015_models.StopTaskResponse:
        """
        @summary 暂停外呼任务
        
        @param request: StopTaskRequest
        @return: StopTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_task_with_options(request, runtime)

    async def stop_task_async(
        self,
        request: aiccs_20191015_models.StopTaskRequest,
    ) -> aiccs_20191015_models.StopTaskResponse:
        """
        @summary 暂停外呼任务
        
        @param request: StopTaskRequest
        @return: StopTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_task_with_options_async(request, runtime)

    def suspend_hotline_service_with_options(
        self,
        request: aiccs_20191015_models.SuspendHotlineServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.SuspendHotlineServiceResponse:
        """
        @param request: SuspendHotlineServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendHotlineServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SuspendHotlineService',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SuspendHotlineServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_hotline_service_with_options_async(
        self,
        request: aiccs_20191015_models.SuspendHotlineServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.SuspendHotlineServiceResponse:
        """
        @param request: SuspendHotlineServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendHotlineServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SuspendHotlineService',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SuspendHotlineServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_hotline_service(
        self,
        request: aiccs_20191015_models.SuspendHotlineServiceRequest,
    ) -> aiccs_20191015_models.SuspendHotlineServiceResponse:
        """
        @param request: SuspendHotlineServiceRequest
        @return: SuspendHotlineServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.suspend_hotline_service_with_options(request, runtime)

    async def suspend_hotline_service_async(
        self,
        request: aiccs_20191015_models.SuspendHotlineServiceRequest,
    ) -> aiccs_20191015_models.SuspendHotlineServiceResponse:
        """
        @param request: SuspendHotlineServiceRequest
        @return: SuspendHotlineServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.suspend_hotline_service_with_options_async(request, runtime)

    def suspend_outbound_task_with_options(
        self,
        request: aiccs_20191015_models.SuspendOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.SuspendOutboundTaskResponse:
        """
        @param request: SuspendOutboundTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendOutboundTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.outbound_task_id):
            query['OutboundTaskId'] = request.outbound_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendOutboundTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SuspendOutboundTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_outbound_task_with_options_async(
        self,
        request: aiccs_20191015_models.SuspendOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.SuspendOutboundTaskResponse:
        """
        @param request: SuspendOutboundTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendOutboundTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.outbound_task_id):
            query['OutboundTaskId'] = request.outbound_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendOutboundTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SuspendOutboundTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_outbound_task(
        self,
        request: aiccs_20191015_models.SuspendOutboundTaskRequest,
    ) -> aiccs_20191015_models.SuspendOutboundTaskResponse:
        """
        @param request: SuspendOutboundTaskRequest
        @return: SuspendOutboundTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.suspend_outbound_task_with_options(request, runtime)

    async def suspend_outbound_task_async(
        self,
        request: aiccs_20191015_models.SuspendOutboundTaskRequest,
    ) -> aiccs_20191015_models.SuspendOutboundTaskResponse:
        """
        @param request: SuspendOutboundTaskRequest
        @return: SuspendOutboundTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.suspend_outbound_task_with_options_async(request, runtime)

    def terminate_ai_outbound_task_with_options(
        self,
        request: aiccs_20191015_models.TerminateAiOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.TerminateAiOutboundTaskResponse:
        """
        @summary 终止智能外呼任务
        
        @param request: TerminateAiOutboundTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TerminateAiOutboundTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TerminateAiOutboundTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.TerminateAiOutboundTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def terminate_ai_outbound_task_with_options_async(
        self,
        request: aiccs_20191015_models.TerminateAiOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.TerminateAiOutboundTaskResponse:
        """
        @summary 终止智能外呼任务
        
        @param request: TerminateAiOutboundTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TerminateAiOutboundTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TerminateAiOutboundTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.TerminateAiOutboundTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def terminate_ai_outbound_task(
        self,
        request: aiccs_20191015_models.TerminateAiOutboundTaskRequest,
    ) -> aiccs_20191015_models.TerminateAiOutboundTaskResponse:
        """
        @summary 终止智能外呼任务
        
        @param request: TerminateAiOutboundTaskRequest
        @return: TerminateAiOutboundTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.terminate_ai_outbound_task_with_options(request, runtime)

    async def terminate_ai_outbound_task_async(
        self,
        request: aiccs_20191015_models.TerminateAiOutboundTaskRequest,
    ) -> aiccs_20191015_models.TerminateAiOutboundTaskResponse:
        """
        @summary 终止智能外呼任务
        
        @param request: TerminateAiOutboundTaskRequest
        @return: TerminateAiOutboundTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.terminate_ai_outbound_task_with_options_async(request, runtime)

    def transfer_call_to_skill_group_with_options(
        self,
        request: aiccs_20191015_models.TransferCallToSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.TransferCallToSkillGroupResponse:
        """
        @param request: TransferCallToSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferCallToSkillGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.call_id):
            body['CallId'] = request.call_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not UtilClient.is_unset(request.hold_connection_id):
            body['HoldConnectionId'] = request.hold_connection_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_single_transfer):
            body['IsSingleTransfer'] = request.is_single_transfer
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.skill_group_id):
            body['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TransferCallToSkillGroup',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.TransferCallToSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_call_to_skill_group_with_options_async(
        self,
        request: aiccs_20191015_models.TransferCallToSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.TransferCallToSkillGroupResponse:
        """
        @param request: TransferCallToSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferCallToSkillGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.call_id):
            body['CallId'] = request.call_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_id):
            body['ConnectionId'] = request.connection_id
        if not UtilClient.is_unset(request.hold_connection_id):
            body['HoldConnectionId'] = request.hold_connection_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_single_transfer):
            body['IsSingleTransfer'] = request.is_single_transfer
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.skill_group_id):
            body['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TransferCallToSkillGroup',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.TransferCallToSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_call_to_skill_group(
        self,
        request: aiccs_20191015_models.TransferCallToSkillGroupRequest,
    ) -> aiccs_20191015_models.TransferCallToSkillGroupResponse:
        """
        @param request: TransferCallToSkillGroupRequest
        @return: TransferCallToSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.transfer_call_to_skill_group_with_options(request, runtime)

    async def transfer_call_to_skill_group_async(
        self,
        request: aiccs_20191015_models.TransferCallToSkillGroupRequest,
    ) -> aiccs_20191015_models.TransferCallToSkillGroupResponse:
        """
        @param request: TransferCallToSkillGroupRequest
        @return: TransferCallToSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.transfer_call_to_skill_group_with_options_async(request, runtime)

    def update_agent_with_options(
        self,
        request: aiccs_20191015_models.UpdateAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.UpdateAgentResponse:
        """
        @param request: UpdateAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAgentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id):
            body['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.skill_group_id_list):
            body['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAgent',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='PUT',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.UpdateAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_agent_with_options_async(
        self,
        request: aiccs_20191015_models.UpdateAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.UpdateAgentResponse:
        """
        @param request: UpdateAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAgentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id):
            body['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.skill_group_id_list):
            body['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAgent',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='PUT',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.UpdateAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_agent(
        self,
        request: aiccs_20191015_models.UpdateAgentRequest,
    ) -> aiccs_20191015_models.UpdateAgentResponse:
        """
        @param request: UpdateAgentRequest
        @return: UpdateAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_agent_with_options(request, runtime)

    async def update_agent_async(
        self,
        request: aiccs_20191015_models.UpdateAgentRequest,
    ) -> aiccs_20191015_models.UpdateAgentResponse:
        """
        @param request: UpdateAgentRequest
        @return: UpdateAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_agent_with_options_async(request, runtime)

    def update_ai_call_task_with_options(
        self,
        tmp_req: aiccs_20191015_models.UpdateAiCallTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.UpdateAiCallTaskResponse:
        """
        @summary 更新AI外呼任务配置
        
        @param tmp_req: UpdateAiCallTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAiCallTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.UpdateAiCallTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.call_day):
            request.call_day_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.call_day, 'CallDay', 'json')
        if not UtilClient.is_unset(tmp_req.call_retry_reason):
            request.call_retry_reason_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.call_retry_reason, 'CallRetryReason', 'json')
        if not UtilClient.is_unset(tmp_req.call_time):
            request.call_time_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.call_time, 'CallTime', 'json')
        query = {}
        if not UtilClient.is_unset(request.call_day_shrink):
            query['CallDay'] = request.call_day_shrink
        if not UtilClient.is_unset(request.call_retry_interval):
            query['CallRetryInterval'] = request.call_retry_interval
        if not UtilClient.is_unset(request.call_retry_reason_shrink):
            query['CallRetryReason'] = request.call_retry_reason_shrink
        if not UtilClient.is_unset(request.call_retry_times):
            query['CallRetryTimes'] = request.call_retry_times
        if not UtilClient.is_unset(request.call_time_shrink):
            query['CallTime'] = request.call_time_shrink
        if not UtilClient.is_unset(request.miss_call_retry):
            query['MissCallRetry'] = request.miss_call_retry
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_type):
            query['StartType'] = request.start_type
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_start_time):
            query['TaskStartTime'] = request.task_start_time
        if not UtilClient.is_unset(request.virtual_number):
            query['VirtualNumber'] = request.virtual_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAiCallTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.UpdateAiCallTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ai_call_task_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.UpdateAiCallTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.UpdateAiCallTaskResponse:
        """
        @summary 更新AI外呼任务配置
        
        @param tmp_req: UpdateAiCallTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAiCallTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.UpdateAiCallTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.call_day):
            request.call_day_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.call_day, 'CallDay', 'json')
        if not UtilClient.is_unset(tmp_req.call_retry_reason):
            request.call_retry_reason_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.call_retry_reason, 'CallRetryReason', 'json')
        if not UtilClient.is_unset(tmp_req.call_time):
            request.call_time_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.call_time, 'CallTime', 'json')
        query = {}
        if not UtilClient.is_unset(request.call_day_shrink):
            query['CallDay'] = request.call_day_shrink
        if not UtilClient.is_unset(request.call_retry_interval):
            query['CallRetryInterval'] = request.call_retry_interval
        if not UtilClient.is_unset(request.call_retry_reason_shrink):
            query['CallRetryReason'] = request.call_retry_reason_shrink
        if not UtilClient.is_unset(request.call_retry_times):
            query['CallRetryTimes'] = request.call_retry_times
        if not UtilClient.is_unset(request.call_time_shrink):
            query['CallTime'] = request.call_time_shrink
        if not UtilClient.is_unset(request.miss_call_retry):
            query['MissCallRetry'] = request.miss_call_retry
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_type):
            query['StartType'] = request.start_type
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_start_time):
            query['TaskStartTime'] = request.task_start_time
        if not UtilClient.is_unset(request.virtual_number):
            query['VirtualNumber'] = request.virtual_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAiCallTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.UpdateAiCallTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ai_call_task(
        self,
        request: aiccs_20191015_models.UpdateAiCallTaskRequest,
    ) -> aiccs_20191015_models.UpdateAiCallTaskResponse:
        """
        @summary 更新AI外呼任务配置
        
        @param request: UpdateAiCallTaskRequest
        @return: UpdateAiCallTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_ai_call_task_with_options(request, runtime)

    async def update_ai_call_task_async(
        self,
        request: aiccs_20191015_models.UpdateAiCallTaskRequest,
    ) -> aiccs_20191015_models.UpdateAiCallTaskResponse:
        """
        @summary 更新AI外呼任务配置
        
        @param request: UpdateAiCallTaskRequest
        @return: UpdateAiCallTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_ai_call_task_with_options_async(request, runtime)

    def update_ai_outbound_task_with_options(
        self,
        tmp_req: aiccs_20191015_models.UpdateAiOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.UpdateAiOutboundTaskResponse:
        """
        @summary 更新智能外呼任务（预测式外呼、自动外呼）
        
        @param tmp_req: UpdateAiOutboundTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAiOutboundTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.UpdateAiOutboundTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.outbound_nums):
            request.outbound_nums_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.outbound_nums, 'OutboundNums', 'json')
        if not UtilClient.is_unset(tmp_req.recall_rule):
            request.recall_rule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.recall_rule, 'RecallRule', 'json')
        query = {}
        if not UtilClient.is_unset(request.concurrent_rate):
            query['ConcurrentRate'] = request.concurrent_rate
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execution_time):
            query['ExecutionTime'] = request.execution_time
        if not UtilClient.is_unset(request.forecast_call_rate):
            query['ForecastCallRate'] = request.forecast_call_rate
        if not UtilClient.is_unset(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num_repeated):
            query['NumRepeated'] = request.num_repeated
        if not UtilClient.is_unset(request.outbound_nums_shrink):
            query['OutboundNums'] = request.outbound_nums_shrink
        if not UtilClient.is_unset(request.recall_rule_shrink):
            query['RecallRule'] = request.recall_rule_shrink
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAiOutboundTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.UpdateAiOutboundTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ai_outbound_task_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.UpdateAiOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.UpdateAiOutboundTaskResponse:
        """
        @summary 更新智能外呼任务（预测式外呼、自动外呼）
        
        @param tmp_req: UpdateAiOutboundTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAiOutboundTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.UpdateAiOutboundTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.outbound_nums):
            request.outbound_nums_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.outbound_nums, 'OutboundNums', 'json')
        if not UtilClient.is_unset(tmp_req.recall_rule):
            request.recall_rule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.recall_rule, 'RecallRule', 'json')
        query = {}
        if not UtilClient.is_unset(request.concurrent_rate):
            query['ConcurrentRate'] = request.concurrent_rate
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execution_time):
            query['ExecutionTime'] = request.execution_time
        if not UtilClient.is_unset(request.forecast_call_rate):
            query['ForecastCallRate'] = request.forecast_call_rate
        if not UtilClient.is_unset(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num_repeated):
            query['NumRepeated'] = request.num_repeated
        if not UtilClient.is_unset(request.outbound_nums_shrink):
            query['OutboundNums'] = request.outbound_nums_shrink
        if not UtilClient.is_unset(request.recall_rule_shrink):
            query['RecallRule'] = request.recall_rule_shrink
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAiOutboundTask',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.UpdateAiOutboundTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ai_outbound_task(
        self,
        request: aiccs_20191015_models.UpdateAiOutboundTaskRequest,
    ) -> aiccs_20191015_models.UpdateAiOutboundTaskResponse:
        """
        @summary 更新智能外呼任务（预测式外呼、自动外呼）
        
        @param request: UpdateAiOutboundTaskRequest
        @return: UpdateAiOutboundTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_ai_outbound_task_with_options(request, runtime)

    async def update_ai_outbound_task_async(
        self,
        request: aiccs_20191015_models.UpdateAiOutboundTaskRequest,
    ) -> aiccs_20191015_models.UpdateAiOutboundTaskResponse:
        """
        @summary 更新智能外呼任务（预测式外呼、自动外呼）
        
        @param request: UpdateAiOutboundTaskRequest
        @return: UpdateAiOutboundTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_ai_outbound_task_with_options_async(request, runtime)

    def update_department_with_options(
        self,
        request: aiccs_20191015_models.UpdateDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.UpdateDepartmentResponse:
        """
        @summary 更新部门信息
        
        @param request: UpdateDepartmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDepartmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.department_name):
            query['DepartmentName'] = request.department_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDepartment',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.UpdateDepartmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_department_with_options_async(
        self,
        request: aiccs_20191015_models.UpdateDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.UpdateDepartmentResponse:
        """
        @summary 更新部门信息
        
        @param request: UpdateDepartmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDepartmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.department_name):
            query['DepartmentName'] = request.department_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDepartment',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.UpdateDepartmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_department(
        self,
        request: aiccs_20191015_models.UpdateDepartmentRequest,
    ) -> aiccs_20191015_models.UpdateDepartmentResponse:
        """
        @summary 更新部门信息
        
        @param request: UpdateDepartmentRequest
        @return: UpdateDepartmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_department_with_options(request, runtime)

    async def update_department_async(
        self,
        request: aiccs_20191015_models.UpdateDepartmentRequest,
    ) -> aiccs_20191015_models.UpdateDepartmentResponse:
        """
        @summary 更新部门信息
        
        @param request: UpdateDepartmentRequest
        @return: UpdateDepartmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_department_with_options_async(request, runtime)

    def update_outer_account_with_options(
        self,
        request: aiccs_20191015_models.UpdateOuterAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.UpdateOuterAccountResponse:
        """
        @param request: UpdateOuterAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateOuterAccountResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOuterAccount',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.UpdateOuterAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_outer_account_with_options_async(
        self,
        request: aiccs_20191015_models.UpdateOuterAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.UpdateOuterAccountResponse:
        """
        @param request: UpdateOuterAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateOuterAccountResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOuterAccount',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.UpdateOuterAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_outer_account(
        self,
        request: aiccs_20191015_models.UpdateOuterAccountRequest,
    ) -> aiccs_20191015_models.UpdateOuterAccountResponse:
        """
        @param request: UpdateOuterAccountRequest
        @return: UpdateOuterAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_outer_account_with_options(request, runtime)

    async def update_outer_account_async(
        self,
        request: aiccs_20191015_models.UpdateOuterAccountRequest,
    ) -> aiccs_20191015_models.UpdateOuterAccountResponse:
        """
        @param request: UpdateOuterAccountRequest
        @return: UpdateOuterAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_outer_account_with_options_async(request, runtime)

    def update_skill_group_with_options(
        self,
        request: aiccs_20191015_models.UpdateSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.UpdateSkillGroupResponse:
        """
        @param request: UpdateSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.skill_group_name):
            query['SkillGroupName'] = request.skill_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSkillGroup',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.UpdateSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_skill_group_with_options_async(
        self,
        request: aiccs_20191015_models.UpdateSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.UpdateSkillGroupResponse:
        """
        @param request: UpdateSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.skill_group_name):
            query['SkillGroupName'] = request.skill_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSkillGroup',
            version='2019-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiccs_20191015_models.UpdateSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_skill_group(
        self,
        request: aiccs_20191015_models.UpdateSkillGroupRequest,
    ) -> aiccs_20191015_models.UpdateSkillGroupResponse:
        """
        @param request: UpdateSkillGroupRequest
        @return: UpdateSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_skill_group_with_options(request, runtime)

    async def update_skill_group_async(
        self,
        request: aiccs_20191015_models.UpdateSkillGroupRequest,
    ) -> aiccs_20191015_models.UpdateSkillGroupResponse:
        """
        @param request: UpdateSkillGroupRequest
        @return: UpdateSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_skill_group_with_options_async(request, runtime)
