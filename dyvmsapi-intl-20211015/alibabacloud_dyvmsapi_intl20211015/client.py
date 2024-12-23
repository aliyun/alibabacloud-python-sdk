# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dyvmsapi_intl20211015 import models as dyvmsapi_intl_20211015_models
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
        self._endpoint = self.get_endpoint('dyvmsapi-intl', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def backend_call_group_with_options(
        self,
        tmp_req: dyvmsapi_intl_20211015_models.BackendCallGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.BackendCallGroupResponse:
        """
        @summary Initiates a voice group call to multiple phone numbers. The content of the group call is that of approved templates. You can log on to the VMS console and choose Voice Call Template to view the template ID. This feature enqueues the phone numbers to be called. The time when the phone numbers are called is uncertain.
        
        @param tmp_req: BackendCallGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BackendCallGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dyvmsapi_intl_20211015_models.BackendCallGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.called_number):
            request.called_number_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.called_number, 'CalledNumber', 'json')
        query = {}
        if not UtilClient.is_unset(request.called_number_shrink):
            query['CalledNumber'] = request.called_number_shrink
        if not UtilClient.is_unset(request.caller_id_number):
            query['CallerIdNumber'] = request.caller_id_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_type):
            query['SendType'] = request.send_type
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.timing_start):
            query['TimingStart'] = request.timing_start
        if not UtilClient.is_unset(request.tts_code):
            query['TtsCode'] = request.tts_code
        if not UtilClient.is_unset(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BackendCallGroup',
            version='2021-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_intl_20211015_models.BackendCallGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def backend_call_group_with_options_async(
        self,
        tmp_req: dyvmsapi_intl_20211015_models.BackendCallGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.BackendCallGroupResponse:
        """
        @summary Initiates a voice group call to multiple phone numbers. The content of the group call is that of approved templates. You can log on to the VMS console and choose Voice Call Template to view the template ID. This feature enqueues the phone numbers to be called. The time when the phone numbers are called is uncertain.
        
        @param tmp_req: BackendCallGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BackendCallGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dyvmsapi_intl_20211015_models.BackendCallGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.called_number):
            request.called_number_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.called_number, 'CalledNumber', 'json')
        query = {}
        if not UtilClient.is_unset(request.called_number_shrink):
            query['CalledNumber'] = request.called_number_shrink
        if not UtilClient.is_unset(request.caller_id_number):
            query['CallerIdNumber'] = request.caller_id_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_type):
            query['SendType'] = request.send_type
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.timing_start):
            query['TimingStart'] = request.timing_start
        if not UtilClient.is_unset(request.tts_code):
            query['TtsCode'] = request.tts_code
        if not UtilClient.is_unset(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BackendCallGroup',
            version='2021-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_intl_20211015_models.BackendCallGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def backend_call_group(
        self,
        request: dyvmsapi_intl_20211015_models.BackendCallGroupRequest,
    ) -> dyvmsapi_intl_20211015_models.BackendCallGroupResponse:
        """
        @summary Initiates a voice group call to multiple phone numbers. The content of the group call is that of approved templates. You can log on to the VMS console and choose Voice Call Template to view the template ID. This feature enqueues the phone numbers to be called. The time when the phone numbers are called is uncertain.
        
        @param request: BackendCallGroupRequest
        @return: BackendCallGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.backend_call_group_with_options(request, runtime)

    async def backend_call_group_async(
        self,
        request: dyvmsapi_intl_20211015_models.BackendCallGroupRequest,
    ) -> dyvmsapi_intl_20211015_models.BackendCallGroupResponse:
        """
        @summary Initiates a voice group call to multiple phone numbers. The content of the group call is that of approved templates. You can log on to the VMS console and choose Voice Call Template to view the template ID. This feature enqueues the phone numbers to be called. The time when the phone numbers are called is uncertain.
        
        @param request: BackendCallGroupRequest
        @return: BackendCallGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.backend_call_group_with_options_async(request, runtime)

    def backend_call_signal_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.BackendCallSignalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.BackendCallSignalResponse:
        """
        @summary Sends a voice verification code and voice notification with variables to a phone number.
        
        @param request: BackendCallSignalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BackendCallSignalResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.caller_id_number):
            query['CallerIdNumber'] = request.caller_id_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.tts_code):
            query['TtsCode'] = request.tts_code
        if not UtilClient.is_unset(request.tts_param):
            query['TtsParam'] = request.tts_param
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BackendCallSignal',
            version='2021-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_intl_20211015_models.BackendCallSignalResponse(),
            self.call_api(params, req, runtime)
        )

    async def backend_call_signal_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.BackendCallSignalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.BackendCallSignalResponse:
        """
        @summary Sends a voice verification code and voice notification with variables to a phone number.
        
        @param request: BackendCallSignalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BackendCallSignalResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.caller_id_number):
            query['CallerIdNumber'] = request.caller_id_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.tts_code):
            query['TtsCode'] = request.tts_code
        if not UtilClient.is_unset(request.tts_param):
            query['TtsParam'] = request.tts_param
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BackendCallSignal',
            version='2021-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_intl_20211015_models.BackendCallSignalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def backend_call_signal(
        self,
        request: dyvmsapi_intl_20211015_models.BackendCallSignalRequest,
    ) -> dyvmsapi_intl_20211015_models.BackendCallSignalResponse:
        """
        @summary Sends a voice verification code and voice notification with variables to a phone number.
        
        @param request: BackendCallSignalRequest
        @return: BackendCallSignalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.backend_call_signal_with_options(request, runtime)

    async def backend_call_signal_async(
        self,
        request: dyvmsapi_intl_20211015_models.BackendCallSignalRequest,
    ) -> dyvmsapi_intl_20211015_models.BackendCallSignalResponse:
        """
        @summary Sends a voice verification code and voice notification with variables to a phone number.
        
        @param request: BackendCallSignalRequest
        @return: BackendCallSignalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.backend_call_signal_with_options_async(request, runtime)

    def group_call_with_options(
        self,
        tmp_req: dyvmsapi_intl_20211015_models.GroupCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.GroupCallResponse:
        """
        @summary 向指定号码发送语音验证码和带参数变量的语音通知，支持语音文件模板或文本转语音模板
        
        @param tmp_req: GroupCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GroupCallResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dyvmsapi_intl_20211015_models.GroupCallShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.called_number):
            request.called_number_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.called_number, 'CalledNumber', 'json')
        query = {}
        if not UtilClient.is_unset(request.called_number_shrink):
            query['CalledNumber'] = request.called_number_shrink
        if not UtilClient.is_unset(request.caller_id_number):
            query['CallerIdNumber'] = request.caller_id_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_type):
            query['SendType'] = request.send_type
        if not UtilClient.is_unset(request.signature):
            query['Signature'] = request.signature
        if not UtilClient.is_unset(request.signature_nonce):
            query['SignatureNonce'] = request.signature_nonce
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.timestamp):
            query['Timestamp'] = request.timestamp
        if not UtilClient.is_unset(request.timing_start):
            query['TimingStart'] = request.timing_start
        if not UtilClient.is_unset(request.tts_code):
            query['TtsCode'] = request.tts_code
        if not UtilClient.is_unset(request.tts_param):
            query['TtsParam'] = request.tts_param
        if not UtilClient.is_unset(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GroupCall',
            version='2021-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_intl_20211015_models.GroupCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def group_call_with_options_async(
        self,
        tmp_req: dyvmsapi_intl_20211015_models.GroupCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.GroupCallResponse:
        """
        @summary 向指定号码发送语音验证码和带参数变量的语音通知，支持语音文件模板或文本转语音模板
        
        @param tmp_req: GroupCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GroupCallResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dyvmsapi_intl_20211015_models.GroupCallShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.called_number):
            request.called_number_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.called_number, 'CalledNumber', 'json')
        query = {}
        if not UtilClient.is_unset(request.called_number_shrink):
            query['CalledNumber'] = request.called_number_shrink
        if not UtilClient.is_unset(request.caller_id_number):
            query['CallerIdNumber'] = request.caller_id_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_type):
            query['SendType'] = request.send_type
        if not UtilClient.is_unset(request.signature):
            query['Signature'] = request.signature
        if not UtilClient.is_unset(request.signature_nonce):
            query['SignatureNonce'] = request.signature_nonce
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.timestamp):
            query['Timestamp'] = request.timestamp
        if not UtilClient.is_unset(request.timing_start):
            query['TimingStart'] = request.timing_start
        if not UtilClient.is_unset(request.tts_code):
            query['TtsCode'] = request.tts_code
        if not UtilClient.is_unset(request.tts_param):
            query['TtsParam'] = request.tts_param
        if not UtilClient.is_unset(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GroupCall',
            version='2021-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_intl_20211015_models.GroupCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def group_call(
        self,
        request: dyvmsapi_intl_20211015_models.GroupCallRequest,
    ) -> dyvmsapi_intl_20211015_models.GroupCallResponse:
        """
        @summary 向指定号码发送语音验证码和带参数变量的语音通知，支持语音文件模板或文本转语音模板
        
        @param request: GroupCallRequest
        @return: GroupCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.group_call_with_options(request, runtime)

    async def group_call_async(
        self,
        request: dyvmsapi_intl_20211015_models.GroupCallRequest,
    ) -> dyvmsapi_intl_20211015_models.GroupCallResponse:
        """
        @summary 向指定号码发送语音验证码和带参数变量的语音通知，支持语音文件模板或文本转语音模板
        
        @param request: GroupCallRequest
        @return: GroupCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.group_call_with_options_async(request, runtime)

    def signal_call_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.SignalCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.SignalCallResponse:
        """
        @summary 向指定号码发送语音验证码和带参数变量的语音通知，支持语音文件模板或文本转语音模板
        
        @param request: SignalCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SignalCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.caller_id_number):
            query['CallerIdNumber'] = request.caller_id_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_type):
            query['SendType'] = request.send_type
        if not UtilClient.is_unset(request.signature):
            query['Signature'] = request.signature
        if not UtilClient.is_unset(request.signature_nonce):
            query['SignatureNonce'] = request.signature_nonce
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.timestamp):
            query['Timestamp'] = request.timestamp
        if not UtilClient.is_unset(request.timing_start):
            query['TimingStart'] = request.timing_start
        if not UtilClient.is_unset(request.tts_code):
            query['TtsCode'] = request.tts_code
        if not UtilClient.is_unset(request.tts_param):
            query['TtsParam'] = request.tts_param
        if not UtilClient.is_unset(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SignalCall',
            version='2021-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_intl_20211015_models.SignalCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def signal_call_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.SignalCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.SignalCallResponse:
        """
        @summary 向指定号码发送语音验证码和带参数变量的语音通知，支持语音文件模板或文本转语音模板
        
        @param request: SignalCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SignalCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.caller_id_number):
            query['CallerIdNumber'] = request.caller_id_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_type):
            query['SendType'] = request.send_type
        if not UtilClient.is_unset(request.signature):
            query['Signature'] = request.signature
        if not UtilClient.is_unset(request.signature_nonce):
            query['SignatureNonce'] = request.signature_nonce
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.timestamp):
            query['Timestamp'] = request.timestamp
        if not UtilClient.is_unset(request.timing_start):
            query['TimingStart'] = request.timing_start
        if not UtilClient.is_unset(request.tts_code):
            query['TtsCode'] = request.tts_code
        if not UtilClient.is_unset(request.tts_param):
            query['TtsParam'] = request.tts_param
        if not UtilClient.is_unset(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SignalCall',
            version='2021-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_intl_20211015_models.SignalCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def signal_call(
        self,
        request: dyvmsapi_intl_20211015_models.SignalCallRequest,
    ) -> dyvmsapi_intl_20211015_models.SignalCallResponse:
        """
        @summary 向指定号码发送语音验证码和带参数变量的语音通知，支持语音文件模板或文本转语音模板
        
        @param request: SignalCallRequest
        @return: SignalCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.signal_call_with_options(request, runtime)

    async def signal_call_async(
        self,
        request: dyvmsapi_intl_20211015_models.SignalCallRequest,
    ) -> dyvmsapi_intl_20211015_models.SignalCallResponse:
        """
        @summary 向指定号码发送语音验证码和带参数变量的语音通知，支持语音文件模板或文本转语音模板
        
        @param request: SignalCallRequest
        @return: SignalCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.signal_call_with_options_async(request, runtime)

    def voice_group_call_with_options(
        self,
        tmp_req: dyvmsapi_intl_20211015_models.VoiceGroupCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.VoiceGroupCallResponse:
        """
        @summary 国际语音api-语音群呼
        
        @param tmp_req: VoiceGroupCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceGroupCallResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dyvmsapi_intl_20211015_models.VoiceGroupCallShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.called_number):
            request.called_number_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.called_number, 'CalledNumber', 'json')
        query = {}
        if not UtilClient.is_unset(request.called_number_shrink):
            query['CalledNumber'] = request.called_number_shrink
        if not UtilClient.is_unset(request.caller_id_number):
            query['CallerIdNumber'] = request.caller_id_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_type):
            query['SendType'] = request.send_type
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.timing_start):
            query['TimingStart'] = request.timing_start
        if not UtilClient.is_unset(request.tts_code):
            query['TtsCode'] = request.tts_code
        if not UtilClient.is_unset(request.tts_param):
            query['TtsParam'] = request.tts_param
        if not UtilClient.is_unset(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceGroupCall',
            version='2021-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_intl_20211015_models.VoiceGroupCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def voice_group_call_with_options_async(
        self,
        tmp_req: dyvmsapi_intl_20211015_models.VoiceGroupCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.VoiceGroupCallResponse:
        """
        @summary 国际语音api-语音群呼
        
        @param tmp_req: VoiceGroupCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceGroupCallResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dyvmsapi_intl_20211015_models.VoiceGroupCallShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.called_number):
            request.called_number_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.called_number, 'CalledNumber', 'json')
        query = {}
        if not UtilClient.is_unset(request.called_number_shrink):
            query['CalledNumber'] = request.called_number_shrink
        if not UtilClient.is_unset(request.caller_id_number):
            query['CallerIdNumber'] = request.caller_id_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_type):
            query['SendType'] = request.send_type
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.timing_start):
            query['TimingStart'] = request.timing_start
        if not UtilClient.is_unset(request.tts_code):
            query['TtsCode'] = request.tts_code
        if not UtilClient.is_unset(request.tts_param):
            query['TtsParam'] = request.tts_param
        if not UtilClient.is_unset(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceGroupCall',
            version='2021-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_intl_20211015_models.VoiceGroupCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def voice_group_call(
        self,
        request: dyvmsapi_intl_20211015_models.VoiceGroupCallRequest,
    ) -> dyvmsapi_intl_20211015_models.VoiceGroupCallResponse:
        """
        @summary 国际语音api-语音群呼
        
        @param request: VoiceGroupCallRequest
        @return: VoiceGroupCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.voice_group_call_with_options(request, runtime)

    async def voice_group_call_async(
        self,
        request: dyvmsapi_intl_20211015_models.VoiceGroupCallRequest,
    ) -> dyvmsapi_intl_20211015_models.VoiceGroupCallResponse:
        """
        @summary 国际语音api-语音群呼
        
        @param request: VoiceGroupCallRequest
        @return: VoiceGroupCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.voice_group_call_with_options_async(request, runtime)

    def voice_single_call_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.VoiceSingleCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.VoiceSingleCallResponse:
        """
        @summary 国际语音api-语音单呼
        
        @param request: VoiceSingleCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceSingleCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.caller_id_number):
            query['CallerIdNumber'] = request.caller_id_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_type):
            query['SendType'] = request.send_type
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.timing_start):
            query['TimingStart'] = request.timing_start
        if not UtilClient.is_unset(request.tts_code):
            query['TtsCode'] = request.tts_code
        if not UtilClient.is_unset(request.tts_param):
            query['TtsParam'] = request.tts_param
        if not UtilClient.is_unset(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceSingleCall',
            version='2021-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_intl_20211015_models.VoiceSingleCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def voice_single_call_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.VoiceSingleCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.VoiceSingleCallResponse:
        """
        @summary 国际语音api-语音单呼
        
        @param request: VoiceSingleCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceSingleCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.caller_id_number):
            query['CallerIdNumber'] = request.caller_id_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_type):
            query['SendType'] = request.send_type
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.timing_start):
            query['TimingStart'] = request.timing_start
        if not UtilClient.is_unset(request.tts_code):
            query['TtsCode'] = request.tts_code
        if not UtilClient.is_unset(request.tts_param):
            query['TtsParam'] = request.tts_param
        if not UtilClient.is_unset(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceSingleCall',
            version='2021-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_intl_20211015_models.VoiceSingleCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def voice_single_call(
        self,
        request: dyvmsapi_intl_20211015_models.VoiceSingleCallRequest,
    ) -> dyvmsapi_intl_20211015_models.VoiceSingleCallResponse:
        """
        @summary 国际语音api-语音单呼
        
        @param request: VoiceSingleCallRequest
        @return: VoiceSingleCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.voice_single_call_with_options(request, runtime)

    async def voice_single_call_async(
        self,
        request: dyvmsapi_intl_20211015_models.VoiceSingleCallRequest,
    ) -> dyvmsapi_intl_20211015_models.VoiceSingleCallResponse:
        """
        @summary 国际语音api-语音单呼
        
        @param request: VoiceSingleCallRequest
        @return: VoiceSingleCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.voice_single_call_with_options_async(request, runtime)
