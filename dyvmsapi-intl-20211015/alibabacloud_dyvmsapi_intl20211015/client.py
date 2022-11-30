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
        runtime = util_models.RuntimeOptions()
        return self.backend_call_group_with_options(request, runtime)

    async def backend_call_group_async(
        self,
        request: dyvmsapi_intl_20211015_models.BackendCallGroupRequest,
    ) -> dyvmsapi_intl_20211015_models.BackendCallGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.backend_call_group_with_options_async(request, runtime)

    def backend_call_signal_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.BackendCallSignalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.BackendCallSignalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.caller_id_number):
            query['CallerIdNumber'] = request.caller_id_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.caller_id_number):
            query['CallerIdNumber'] = request.caller_id_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
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
        runtime = util_models.RuntimeOptions()
        return self.backend_call_signal_with_options(request, runtime)

    async def backend_call_signal_async(
        self,
        request: dyvmsapi_intl_20211015_models.BackendCallSignalRequest,
    ) -> dyvmsapi_intl_20211015_models.BackendCallSignalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.backend_call_signal_with_options_async(request, runtime)

    def cancle_group_call_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.CancleGroupCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.CancleGroupCallResponse:
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
            action='CancleGroupCall',
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
            dyvmsapi_intl_20211015_models.CancleGroupCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancle_group_call_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.CancleGroupCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.CancleGroupCallResponse:
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
            action='CancleGroupCall',
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
            dyvmsapi_intl_20211015_models.CancleGroupCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancle_group_call(
        self,
        request: dyvmsapi_intl_20211015_models.CancleGroupCallRequest,
    ) -> dyvmsapi_intl_20211015_models.CancleGroupCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancle_group_call_with_options(request, runtime)

    async def cancle_group_call_async(
        self,
        request: dyvmsapi_intl_20211015_models.CancleGroupCallRequest,
    ) -> dyvmsapi_intl_20211015_models.CancleGroupCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancle_group_call_with_options_async(request, runtime)

    def delete_apply_number_record_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.DeleteApplyNumberRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.DeleteApplyNumberRecordResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplyNumberRecord',
            version='2021-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_intl_20211015_models.DeleteApplyNumberRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_apply_number_record_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.DeleteApplyNumberRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.DeleteApplyNumberRecordResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplyNumberRecord',
            version='2021-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_intl_20211015_models.DeleteApplyNumberRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_apply_number_record(
        self,
        request: dyvmsapi_intl_20211015_models.DeleteApplyNumberRecordRequest,
    ) -> dyvmsapi_intl_20211015_models.DeleteApplyNumberRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_apply_number_record_with_options(request, runtime)

    async def delete_apply_number_record_async(
        self,
        request: dyvmsapi_intl_20211015_models.DeleteApplyNumberRecordRequest,
    ) -> dyvmsapi_intl_20211015_models.DeleteApplyNumberRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_apply_number_record_with_options_async(request, runtime)

    def delete_qualification_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.DeleteQualificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.DeleteQualificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQualification',
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
            dyvmsapi_intl_20211015_models.DeleteQualificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_qualification_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.DeleteQualificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.DeleteQualificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQualification',
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
            dyvmsapi_intl_20211015_models.DeleteQualificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_qualification(
        self,
        request: dyvmsapi_intl_20211015_models.DeleteQualificationRequest,
    ) -> dyvmsapi_intl_20211015_models.DeleteQualificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_qualification_with_options(request, runtime)

    async def delete_qualification_async(
        self,
        request: dyvmsapi_intl_20211015_models.DeleteQualificationRequest,
    ) -> dyvmsapi_intl_20211015_models.DeleteQualificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_qualification_with_options_async(request, runtime)

    def delete_sip_trunk_apply_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.DeleteSipTrunkApplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.DeleteSipTrunkApplyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['ApplyId'] = request.apply_id
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
            action='DeleteSipTrunkApply',
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
            dyvmsapi_intl_20211015_models.DeleteSipTrunkApplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sip_trunk_apply_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.DeleteSipTrunkApplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.DeleteSipTrunkApplyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['ApplyId'] = request.apply_id
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
            action='DeleteSipTrunkApply',
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
            dyvmsapi_intl_20211015_models.DeleteSipTrunkApplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sip_trunk_apply(
        self,
        request: dyvmsapi_intl_20211015_models.DeleteSipTrunkApplyRequest,
    ) -> dyvmsapi_intl_20211015_models.DeleteSipTrunkApplyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sip_trunk_apply_with_options(request, runtime)

    async def delete_sip_trunk_apply_async(
        self,
        request: dyvmsapi_intl_20211015_models.DeleteSipTrunkApplyRequest,
    ) -> dyvmsapi_intl_20211015_models.DeleteSipTrunkApplyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sip_trunk_apply_with_options_async(request, runtime)

    def delete_voice_file_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.DeleteVoiceFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.DeleteVoiceFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
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
            action='DeleteVoiceFile',
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
            dyvmsapi_intl_20211015_models.DeleteVoiceFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_voice_file_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.DeleteVoiceFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.DeleteVoiceFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
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
            action='DeleteVoiceFile',
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
            dyvmsapi_intl_20211015_models.DeleteVoiceFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_voice_file(
        self,
        request: dyvmsapi_intl_20211015_models.DeleteVoiceFileRequest,
    ) -> dyvmsapi_intl_20211015_models.DeleteVoiceFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_voice_file_with_options(request, runtime)

    async def delete_voice_file_async(
        self,
        request: dyvmsapi_intl_20211015_models.DeleteVoiceFileRequest,
    ) -> dyvmsapi_intl_20211015_models.DeleteVoiceFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_voice_file_with_options_async(request, runtime)

    def delete_voice_tts_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.DeleteVoiceTtsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.DeleteVoiceTtsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVoiceTts',
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
            dyvmsapi_intl_20211015_models.DeleteVoiceTtsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_voice_tts_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.DeleteVoiceTtsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.DeleteVoiceTtsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVoiceTts',
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
            dyvmsapi_intl_20211015_models.DeleteVoiceTtsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_voice_tts(
        self,
        request: dyvmsapi_intl_20211015_models.DeleteVoiceTtsRequest,
    ) -> dyvmsapi_intl_20211015_models.DeleteVoiceTtsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_voice_tts_with_options(request, runtime)

    async def delete_voice_tts_async(
        self,
        request: dyvmsapi_intl_20211015_models.DeleteVoiceTtsRequest,
    ) -> dyvmsapi_intl_20211015_models.DeleteVoiceTtsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_voice_tts_with_options_async(request, runtime)

    def download_template_file_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.DownloadTemplateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.DownloadTemplateFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_type):
            query['FileType'] = request.file_type
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
            action='DownloadTemplateFile',
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
            dyvmsapi_intl_20211015_models.DownloadTemplateFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_template_file_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.DownloadTemplateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.DownloadTemplateFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_type):
            query['FileType'] = request.file_type
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
            action='DownloadTemplateFile',
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
            dyvmsapi_intl_20211015_models.DownloadTemplateFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_template_file(
        self,
        request: dyvmsapi_intl_20211015_models.DownloadTemplateFileRequest,
    ) -> dyvmsapi_intl_20211015_models.DownloadTemplateFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_template_file_with_options(request, runtime)

    async def download_template_file_async(
        self,
        request: dyvmsapi_intl_20211015_models.DownloadTemplateFileRequest,
    ) -> dyvmsapi_intl_20211015_models.DownloadTemplateFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_template_file_with_options_async(request, runtime)

    def get_intl_voice_open_status_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.GetIntlVoiceOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.GetIntlVoiceOpenStatusResponse:
        UtilClient.validate_model(request)
        query = {}
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
            action='GetIntlVoiceOpenStatus',
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
            dyvmsapi_intl_20211015_models.GetIntlVoiceOpenStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_intl_voice_open_status_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.GetIntlVoiceOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.GetIntlVoiceOpenStatusResponse:
        UtilClient.validate_model(request)
        query = {}
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
            action='GetIntlVoiceOpenStatus',
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
            dyvmsapi_intl_20211015_models.GetIntlVoiceOpenStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_intl_voice_open_status(
        self,
        request: dyvmsapi_intl_20211015_models.GetIntlVoiceOpenStatusRequest,
    ) -> dyvmsapi_intl_20211015_models.GetIntlVoiceOpenStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_intl_voice_open_status_with_options(request, runtime)

    async def get_intl_voice_open_status_async(
        self,
        request: dyvmsapi_intl_20211015_models.GetIntlVoiceOpenStatusRequest,
    ) -> dyvmsapi_intl_20211015_models.GetIntlVoiceOpenStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_intl_voice_open_status_with_options_async(request, runtime)

    def get_oss_info_for_upload_file_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.GetOssInfoForUploadFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.GetOssInfoForUploadFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
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
            action='GetOssInfoForUploadFile',
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
            dyvmsapi_intl_20211015_models.GetOssInfoForUploadFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_info_for_upload_file_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.GetOssInfoForUploadFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.GetOssInfoForUploadFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
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
            action='GetOssInfoForUploadFile',
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
            dyvmsapi_intl_20211015_models.GetOssInfoForUploadFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_info_for_upload_file(
        self,
        request: dyvmsapi_intl_20211015_models.GetOssInfoForUploadFileRequest,
    ) -> dyvmsapi_intl_20211015_models.GetOssInfoForUploadFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oss_info_for_upload_file_with_options(request, runtime)

    async def get_oss_info_for_upload_file_async(
        self,
        request: dyvmsapi_intl_20211015_models.GetOssInfoForUploadFileRequest,
    ) -> dyvmsapi_intl_20211015_models.GetOssInfoForUploadFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oss_info_for_upload_file_with_options_async(request, runtime)

    def home_start_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.HomeStartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.HomeStartResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HomeStart',
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
            dyvmsapi_intl_20211015_models.HomeStartResponse(),
            self.call_api(params, req, runtime)
        )

    async def home_start_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.HomeStartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.HomeStartResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HomeStart',
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
            dyvmsapi_intl_20211015_models.HomeStartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def home_start(
        self,
        request: dyvmsapi_intl_20211015_models.HomeStartRequest,
    ) -> dyvmsapi_intl_20211015_models.HomeStartResponse:
        runtime = util_models.RuntimeOptions()
        return self.home_start_with_options(request, runtime)

    async def home_start_async(
        self,
        request: dyvmsapi_intl_20211015_models.HomeStartRequest,
    ) -> dyvmsapi_intl_20211015_models.HomeStartResponse:
        runtime = util_models.RuntimeOptions()
        return await self.home_start_with_options_async(request, runtime)

    def list_apply_number_record_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.ListApplyNumberRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListApplyNumberRecordResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplyNumberRecord',
            version='2021-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_intl_20211015_models.ListApplyNumberRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_apply_number_record_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListApplyNumberRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListApplyNumberRecordResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplyNumberRecord',
            version='2021-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_intl_20211015_models.ListApplyNumberRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_apply_number_record(
        self,
        request: dyvmsapi_intl_20211015_models.ListApplyNumberRecordRequest,
    ) -> dyvmsapi_intl_20211015_models.ListApplyNumberRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_apply_number_record_with_options(request, runtime)

    async def list_apply_number_record_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListApplyNumberRecordRequest,
    ) -> dyvmsapi_intl_20211015_models.ListApplyNumberRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_apply_number_record_with_options_async(request, runtime)

    def list_number_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.ListNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListNumberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['ApplyId'] = request.apply_id
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        if not UtilClient.is_unset(request.number_name):
            query['NumberName'] = request.number_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_type):
            query['PhoneType'] = request.phone_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNumber',
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
            dyvmsapi_intl_20211015_models.ListNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_number_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListNumberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['ApplyId'] = request.apply_id
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        if not UtilClient.is_unset(request.number_name):
            query['NumberName'] = request.number_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_type):
            query['PhoneType'] = request.phone_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNumber',
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
            dyvmsapi_intl_20211015_models.ListNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_number(
        self,
        request: dyvmsapi_intl_20211015_models.ListNumberRequest,
    ) -> dyvmsapi_intl_20211015_models.ListNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_number_with_options(request, runtime)

    async def list_number_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListNumberRequest,
    ) -> dyvmsapi_intl_20211015_models.ListNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_number_with_options_async(request, runtime)

    def list_qualification_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.ListQualificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListQualificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.company_name):
            query['CompanyName'] = request.company_name
        if not UtilClient.is_unset(request.contact_phone):
            query['ContactPhone'] = request.contact_phone
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQualification',
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
            dyvmsapi_intl_20211015_models.ListQualificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_qualification_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListQualificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListQualificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.company_name):
            query['CompanyName'] = request.company_name
        if not UtilClient.is_unset(request.contact_phone):
            query['ContactPhone'] = request.contact_phone
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQualification',
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
            dyvmsapi_intl_20211015_models.ListQualificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_qualification(
        self,
        request: dyvmsapi_intl_20211015_models.ListQualificationRequest,
    ) -> dyvmsapi_intl_20211015_models.ListQualificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_qualification_with_options(request, runtime)

    async def list_qualification_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListQualificationRequest,
    ) -> dyvmsapi_intl_20211015_models.ListQualificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_qualification_with_options_async(request, runtime)

    def list_receipt_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.ListReceiptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListReceiptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListReceipt',
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
            dyvmsapi_intl_20211015_models.ListReceiptResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_receipt_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListReceiptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListReceiptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListReceipt',
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
            dyvmsapi_intl_20211015_models.ListReceiptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_receipt(
        self,
        request: dyvmsapi_intl_20211015_models.ListReceiptRequest,
    ) -> dyvmsapi_intl_20211015_models.ListReceiptResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_receipt_with_options(request, runtime)

    async def list_receipt_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListReceiptRequest,
    ) -> dyvmsapi_intl_20211015_models.ListReceiptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_receipt_with_options_async(request, runtime)

    def list_sip_trunk_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.ListSipTrunkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListSipTrunkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSipTrunk',
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
            dyvmsapi_intl_20211015_models.ListSipTrunkResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sip_trunk_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListSipTrunkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListSipTrunkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSipTrunk',
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
            dyvmsapi_intl_20211015_models.ListSipTrunkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sip_trunk(
        self,
        request: dyvmsapi_intl_20211015_models.ListSipTrunkRequest,
    ) -> dyvmsapi_intl_20211015_models.ListSipTrunkResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_sip_trunk_with_options(request, runtime)

    async def list_sip_trunk_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListSipTrunkRequest,
    ) -> dyvmsapi_intl_20211015_models.ListSipTrunkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_sip_trunk_with_options_async(request, runtime)

    def list_sip_trunk_detail_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.ListSipTrunkDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListSipTrunkDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSipTrunkDetail',
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
            dyvmsapi_intl_20211015_models.ListSipTrunkDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sip_trunk_detail_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListSipTrunkDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListSipTrunkDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSipTrunkDetail',
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
            dyvmsapi_intl_20211015_models.ListSipTrunkDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sip_trunk_detail(
        self,
        request: dyvmsapi_intl_20211015_models.ListSipTrunkDetailRequest,
    ) -> dyvmsapi_intl_20211015_models.ListSipTrunkDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_sip_trunk_detail_with_options(request, runtime)

    async def list_sip_trunk_detail_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListSipTrunkDetailRequest,
    ) -> dyvmsapi_intl_20211015_models.ListSipTrunkDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_sip_trunk_detail_with_options_async(request, runtime)

    def list_sip_trunk_stat_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.ListSipTrunkStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListSipTrunkStatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSipTrunkStat',
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
            dyvmsapi_intl_20211015_models.ListSipTrunkStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sip_trunk_stat_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListSipTrunkStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListSipTrunkStatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSipTrunkStat',
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
            dyvmsapi_intl_20211015_models.ListSipTrunkStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sip_trunk_stat(
        self,
        request: dyvmsapi_intl_20211015_models.ListSipTrunkStatRequest,
    ) -> dyvmsapi_intl_20211015_models.ListSipTrunkStatResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_sip_trunk_stat_with_options(request, runtime)

    async def list_sip_trunk_stat_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListSipTrunkStatRequest,
    ) -> dyvmsapi_intl_20211015_models.ListSipTrunkStatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_sip_trunk_stat_with_options_async(request, runtime)

    def list_voice_call_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.ListVoiceCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListVoiceCallResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_type):
            query['SendType'] = request.send_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
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
            action='ListVoiceCall',
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
            dyvmsapi_intl_20211015_models.ListVoiceCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_voice_call_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListVoiceCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListVoiceCallResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_type):
            query['SendType'] = request.send_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
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
            action='ListVoiceCall',
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
            dyvmsapi_intl_20211015_models.ListVoiceCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_voice_call(
        self,
        request: dyvmsapi_intl_20211015_models.ListVoiceCallRequest,
    ) -> dyvmsapi_intl_20211015_models.ListVoiceCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_voice_call_with_options(request, runtime)

    async def list_voice_call_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListVoiceCallRequest,
    ) -> dyvmsapi_intl_20211015_models.ListVoiceCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_voice_call_with_options_async(request, runtime)

    def list_voice_call_detail_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.ListVoiceCallDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListVoiceCallDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.hangup_type):
            query['HangupType'] = request.hangup_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
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
            action='ListVoiceCallDetail',
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
            dyvmsapi_intl_20211015_models.ListVoiceCallDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_voice_call_detail_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListVoiceCallDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListVoiceCallDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.hangup_type):
            query['HangupType'] = request.hangup_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
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
            action='ListVoiceCallDetail',
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
            dyvmsapi_intl_20211015_models.ListVoiceCallDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_voice_call_detail(
        self,
        request: dyvmsapi_intl_20211015_models.ListVoiceCallDetailRequest,
    ) -> dyvmsapi_intl_20211015_models.ListVoiceCallDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_voice_call_detail_with_options(request, runtime)

    async def list_voice_call_detail_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListVoiceCallDetailRequest,
    ) -> dyvmsapi_intl_20211015_models.ListVoiceCallDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_voice_call_detail_with_options_async(request, runtime)

    def list_voice_call_stat_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.ListVoiceCallStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListVoiceCallStatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVoiceCallStat',
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
            dyvmsapi_intl_20211015_models.ListVoiceCallStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_voice_call_stat_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListVoiceCallStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListVoiceCallStatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVoiceCallStat',
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
            dyvmsapi_intl_20211015_models.ListVoiceCallStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_voice_call_stat(
        self,
        request: dyvmsapi_intl_20211015_models.ListVoiceCallStatRequest,
    ) -> dyvmsapi_intl_20211015_models.ListVoiceCallStatResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_voice_call_stat_with_options(request, runtime)

    async def list_voice_call_stat_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListVoiceCallStatRequest,
    ) -> dyvmsapi_intl_20211015_models.ListVoiceCallStatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_voice_call_stat_with_options_async(request, runtime)

    def list_voice_file_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.ListVoiceFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListVoiceFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVoiceFile',
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
            dyvmsapi_intl_20211015_models.ListVoiceFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_voice_file_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListVoiceFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListVoiceFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVoiceFile',
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
            dyvmsapi_intl_20211015_models.ListVoiceFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_voice_file(
        self,
        request: dyvmsapi_intl_20211015_models.ListVoiceFileRequest,
    ) -> dyvmsapi_intl_20211015_models.ListVoiceFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_voice_file_with_options(request, runtime)

    async def list_voice_file_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListVoiceFileRequest,
    ) -> dyvmsapi_intl_20211015_models.ListVoiceFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_voice_file_with_options_async(request, runtime)

    def list_voice_tts_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.ListVoiceTtsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListVoiceTtsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVoiceTts',
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
            dyvmsapi_intl_20211015_models.ListVoiceTtsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_voice_tts_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListVoiceTtsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.ListVoiceTtsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVoiceTts',
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
            dyvmsapi_intl_20211015_models.ListVoiceTtsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_voice_tts(
        self,
        request: dyvmsapi_intl_20211015_models.ListVoiceTtsRequest,
    ) -> dyvmsapi_intl_20211015_models.ListVoiceTtsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_voice_tts_with_options(request, runtime)

    async def list_voice_tts_async(
        self,
        request: dyvmsapi_intl_20211015_models.ListVoiceTtsRequest,
    ) -> dyvmsapi_intl_20211015_models.ListVoiceTtsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_voice_tts_with_options_async(request, runtime)

    def number_enable_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.NumberEnableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.NumberEnableResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NumberEnable',
            version='2021-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_intl_20211015_models.NumberEnableResponse(),
            self.call_api(params, req, runtime)
        )

    async def number_enable_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.NumberEnableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.NumberEnableResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NumberEnable',
            version='2021-10-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_intl_20211015_models.NumberEnableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def number_enable(
        self,
        request: dyvmsapi_intl_20211015_models.NumberEnableRequest,
    ) -> dyvmsapi_intl_20211015_models.NumberEnableResponse:
        runtime = util_models.RuntimeOptions()
        return self.number_enable_with_options(request, runtime)

    async def number_enable_async(
        self,
        request: dyvmsapi_intl_20211015_models.NumberEnableRequest,
    ) -> dyvmsapi_intl_20211015_models.NumberEnableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.number_enable_with_options_async(request, runtime)

    def open_intl_voice_service_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.OpenIntlVoiceServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.OpenIntlVoiceServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
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
            action='OpenIntlVoiceService',
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
            dyvmsapi_intl_20211015_models.OpenIntlVoiceServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_intl_voice_service_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.OpenIntlVoiceServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.OpenIntlVoiceServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
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
            action='OpenIntlVoiceService',
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
            dyvmsapi_intl_20211015_models.OpenIntlVoiceServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_intl_voice_service(
        self,
        request: dyvmsapi_intl_20211015_models.OpenIntlVoiceServiceRequest,
    ) -> dyvmsapi_intl_20211015_models.OpenIntlVoiceServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_intl_voice_service_with_options(request, runtime)

    async def open_intl_voice_service_async(
        self,
        request: dyvmsapi_intl_20211015_models.OpenIntlVoiceServiceRequest,
    ) -> dyvmsapi_intl_20211015_models.OpenIntlVoiceServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_intl_voice_service_with_options_async(request, runtime)

    def osw_test_1with_options(
        self,
        request: dyvmsapi_intl_20211015_models.OswTest1Request,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.OswTest1Response:
        UtilClient.validate_model(request)
        query = {}
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
            action='OswTest1',
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
            dyvmsapi_intl_20211015_models.OswTest1Response(),
            self.call_api(params, req, runtime)
        )

    async def osw_test_1with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.OswTest1Request,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.OswTest1Response:
        UtilClient.validate_model(request)
        query = {}
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
            action='OswTest1',
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
            dyvmsapi_intl_20211015_models.OswTest1Response(),
            await self.call_api_async(params, req, runtime)
        )

    def osw_test_1(
        self,
        request: dyvmsapi_intl_20211015_models.OswTest1Request,
    ) -> dyvmsapi_intl_20211015_models.OswTest1Response:
        runtime = util_models.RuntimeOptions()
        return self.osw_test_1with_options(request, runtime)

    async def osw_test_1_async(
        self,
        request: dyvmsapi_intl_20211015_models.OswTest1Request,
    ) -> dyvmsapi_intl_20211015_models.OswTest1Response:
        runtime = util_models.RuntimeOptions()
        return await self.osw_test_1with_options_async(request, runtime)

    def query_file_oss_url_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.QueryFileOssUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.QueryFileOssUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.file_key):
            query['FileKey'] = request.file_key
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
            action='QueryFileOssUrl',
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
            dyvmsapi_intl_20211015_models.QueryFileOssUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_file_oss_url_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.QueryFileOssUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.QueryFileOssUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.file_key):
            query['FileKey'] = request.file_key
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
            action='QueryFileOssUrl',
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
            dyvmsapi_intl_20211015_models.QueryFileOssUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_file_oss_url(
        self,
        request: dyvmsapi_intl_20211015_models.QueryFileOssUrlRequest,
    ) -> dyvmsapi_intl_20211015_models.QueryFileOssUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_file_oss_url_with_options(request, runtime)

    async def query_file_oss_url_async(
        self,
        request: dyvmsapi_intl_20211015_models.QueryFileOssUrlRequest,
    ) -> dyvmsapi_intl_20211015_models.QueryFileOssUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_file_oss_url_with_options_async(request, runtime)

    def query_home_stat_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.QueryHomeStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.QueryHomeStatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryHomeStat',
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
            dyvmsapi_intl_20211015_models.QueryHomeStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_home_stat_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.QueryHomeStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.QueryHomeStatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryHomeStat',
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
            dyvmsapi_intl_20211015_models.QueryHomeStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_home_stat(
        self,
        request: dyvmsapi_intl_20211015_models.QueryHomeStatRequest,
    ) -> dyvmsapi_intl_20211015_models.QueryHomeStatResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_home_stat_with_options(request, runtime)

    async def query_home_stat_async(
        self,
        request: dyvmsapi_intl_20211015_models.QueryHomeStatRequest,
    ) -> dyvmsapi_intl_20211015_models.QueryHomeStatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_home_stat_with_options_async(request, runtime)

    def query_recording_enable_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.QueryRecordingEnableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.QueryRecordingEnableResponse:
        UtilClient.validate_model(request)
        query = {}
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
            action='QueryRecordingEnable',
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
            dyvmsapi_intl_20211015_models.QueryRecordingEnableResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_recording_enable_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.QueryRecordingEnableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.QueryRecordingEnableResponse:
        UtilClient.validate_model(request)
        query = {}
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
            action='QueryRecordingEnable',
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
            dyvmsapi_intl_20211015_models.QueryRecordingEnableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_recording_enable(
        self,
        request: dyvmsapi_intl_20211015_models.QueryRecordingEnableRequest,
    ) -> dyvmsapi_intl_20211015_models.QueryRecordingEnableResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_recording_enable_with_options(request, runtime)

    async def query_recording_enable_async(
        self,
        request: dyvmsapi_intl_20211015_models.QueryRecordingEnableRequest,
    ) -> dyvmsapi_intl_20211015_models.QueryRecordingEnableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_recording_enable_with_options_async(request, runtime)

    def query_service_enable_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.QueryServiceEnableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.QueryServiceEnableResponse:
        UtilClient.validate_model(request)
        query = {}
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
            action='QueryServiceEnable',
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
            dyvmsapi_intl_20211015_models.QueryServiceEnableResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_service_enable_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.QueryServiceEnableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.QueryServiceEnableResponse:
        UtilClient.validate_model(request)
        query = {}
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
            action='QueryServiceEnable',
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
            dyvmsapi_intl_20211015_models.QueryServiceEnableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_service_enable(
        self,
        request: dyvmsapi_intl_20211015_models.QueryServiceEnableRequest,
    ) -> dyvmsapi_intl_20211015_models.QueryServiceEnableResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_service_enable_with_options(request, runtime)

    async def query_service_enable_async(
        self,
        request: dyvmsapi_intl_20211015_models.QueryServiceEnableRequest,
    ) -> dyvmsapi_intl_20211015_models.QueryServiceEnableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_service_enable_with_options_async(request, runtime)

    def recording_enable_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.RecordingEnableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.RecordingEnableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
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
            action='RecordingEnable',
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
            dyvmsapi_intl_20211015_models.RecordingEnableResponse(),
            self.call_api(params, req, runtime)
        )

    async def recording_enable_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.RecordingEnableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.RecordingEnableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
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
            action='RecordingEnable',
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
            dyvmsapi_intl_20211015_models.RecordingEnableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recording_enable(
        self,
        request: dyvmsapi_intl_20211015_models.RecordingEnableRequest,
    ) -> dyvmsapi_intl_20211015_models.RecordingEnableResponse:
        runtime = util_models.RuntimeOptions()
        return self.recording_enable_with_options(request, runtime)

    async def recording_enable_async(
        self,
        request: dyvmsapi_intl_20211015_models.RecordingEnableRequest,
    ) -> dyvmsapi_intl_20211015_models.RecordingEnableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recording_enable_with_options_async(request, runtime)

    def set_receipt_url_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.SetReceiptUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.SetReceiptUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdr_dr_url):
            query['CdrDrUrl'] = request.cdr_dr_url
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
            action='SetReceiptUrl',
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
            dyvmsapi_intl_20211015_models.SetReceiptUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_receipt_url_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.SetReceiptUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.SetReceiptUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdr_dr_url):
            query['CdrDrUrl'] = request.cdr_dr_url
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
            action='SetReceiptUrl',
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
            dyvmsapi_intl_20211015_models.SetReceiptUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_receipt_url(
        self,
        request: dyvmsapi_intl_20211015_models.SetReceiptUrlRequest,
    ) -> dyvmsapi_intl_20211015_models.SetReceiptUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_receipt_url_with_options(request, runtime)

    async def set_receipt_url_async(
        self,
        request: dyvmsapi_intl_20211015_models.SetReceiptUrlRequest,
    ) -> dyvmsapi_intl_20211015_models.SetReceiptUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_receipt_url_with_options_async(request, runtime)

    def sip_trunk_detail_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.SipTrunkDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.SipTrunkDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SipTrunkDetail',
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
            dyvmsapi_intl_20211015_models.SipTrunkDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def sip_trunk_detail_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.SipTrunkDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.SipTrunkDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SipTrunkDetail',
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
            dyvmsapi_intl_20211015_models.SipTrunkDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sip_trunk_detail(
        self,
        request: dyvmsapi_intl_20211015_models.SipTrunkDetailRequest,
    ) -> dyvmsapi_intl_20211015_models.SipTrunkDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.sip_trunk_detail_with_options(request, runtime)

    async def sip_trunk_detail_async(
        self,
        request: dyvmsapi_intl_20211015_models.SipTrunkDetailRequest,
    ) -> dyvmsapi_intl_20211015_models.SipTrunkDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sip_trunk_detail_with_options_async(request, runtime)

    def submit_group_call_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.SubmitGroupCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.SubmitGroupCallResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.caller_id_number):
            query['CallerIdNumber'] = request.caller_id_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.file_key):
            query['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.group_call_type):
            query['GroupCallType'] = request.group_call_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_type):
            query['SendType'] = request.send_type
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.timing_start):
            query['TimingStart'] = request.timing_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitGroupCall',
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
            dyvmsapi_intl_20211015_models.SubmitGroupCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_group_call_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.SubmitGroupCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.SubmitGroupCallResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.caller_id_number):
            query['CallerIdNumber'] = request.caller_id_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.file_key):
            query['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.group_call_type):
            query['GroupCallType'] = request.group_call_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_type):
            query['SendType'] = request.send_type
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.timing_start):
            query['TimingStart'] = request.timing_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitGroupCall',
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
            dyvmsapi_intl_20211015_models.SubmitGroupCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_group_call(
        self,
        request: dyvmsapi_intl_20211015_models.SubmitGroupCallRequest,
    ) -> dyvmsapi_intl_20211015_models.SubmitGroupCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_group_call_with_options(request, runtime)

    async def submit_group_call_async(
        self,
        request: dyvmsapi_intl_20211015_models.SubmitGroupCallRequest,
    ) -> dyvmsapi_intl_20211015_models.SubmitGroupCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_group_call_with_options_async(request, runtime)

    def submit_number_with_options(
        self,
        tmp_req: dyvmsapi_intl_20211015_models.SubmitNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.SubmitNumberResponse:
        UtilClient.validate_model(tmp_req)
        request = dyvmsapi_intl_20211015_models.SubmitNumberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.number_list):
            request.number_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.number_list, 'NumberList', 'json')
        query = {}
        if not UtilClient.is_unset(request.apply_note):
            query['ApplyNote'] = request.apply_note
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.number_list_shrink):
            query['NumberList'] = request.number_list_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitNumber',
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
            dyvmsapi_intl_20211015_models.SubmitNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_number_with_options_async(
        self,
        tmp_req: dyvmsapi_intl_20211015_models.SubmitNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.SubmitNumberResponse:
        UtilClient.validate_model(tmp_req)
        request = dyvmsapi_intl_20211015_models.SubmitNumberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.number_list):
            request.number_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.number_list, 'NumberList', 'json')
        query = {}
        if not UtilClient.is_unset(request.apply_note):
            query['ApplyNote'] = request.apply_note
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.number_list_shrink):
            query['NumberList'] = request.number_list_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitNumber',
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
            dyvmsapi_intl_20211015_models.SubmitNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_number(
        self,
        request: dyvmsapi_intl_20211015_models.SubmitNumberRequest,
    ) -> dyvmsapi_intl_20211015_models.SubmitNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_number_with_options(request, runtime)

    async def submit_number_async(
        self,
        request: dyvmsapi_intl_20211015_models.SubmitNumberRequest,
    ) -> dyvmsapi_intl_20211015_models.SubmitNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_number_with_options_async(request, runtime)

    def submit_qualification_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.SubmitQualificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.SubmitQualificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.business_license_file_key):
            query['BusinessLicenseFileKey'] = request.business_license_file_key
        if not UtilClient.is_unset(request.company_name):
            query['CompanyName'] = request.company_name
        if not UtilClient.is_unset(request.contact_email):
            query['ContactEmail'] = request.contact_email
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.contact_phone):
            query['ContactPhone'] = request.contact_phone
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.legal_id):
            query['LegalId'] = request.legal_id
        if not UtilClient.is_unset(request.legal_license_file_key):
            query['LegalLicenseFileKey'] = request.legal_license_file_key
        if not UtilClient.is_unset(request.legal_name):
            query['LegalName'] = request.legal_name
        if not UtilClient.is_unset(request.network_access_file_key):
            query['NetworkAccessFileKey'] = request.network_access_file_key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.unified_code):
            query['UnifiedCode'] = request.unified_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitQualification',
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
            dyvmsapi_intl_20211015_models.SubmitQualificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_qualification_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.SubmitQualificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.SubmitQualificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.business_license_file_key):
            query['BusinessLicenseFileKey'] = request.business_license_file_key
        if not UtilClient.is_unset(request.company_name):
            query['CompanyName'] = request.company_name
        if not UtilClient.is_unset(request.contact_email):
            query['ContactEmail'] = request.contact_email
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.contact_phone):
            query['ContactPhone'] = request.contact_phone
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.legal_id):
            query['LegalId'] = request.legal_id
        if not UtilClient.is_unset(request.legal_license_file_key):
            query['LegalLicenseFileKey'] = request.legal_license_file_key
        if not UtilClient.is_unset(request.legal_name):
            query['LegalName'] = request.legal_name
        if not UtilClient.is_unset(request.network_access_file_key):
            query['NetworkAccessFileKey'] = request.network_access_file_key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.unified_code):
            query['UnifiedCode'] = request.unified_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitQualification',
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
            dyvmsapi_intl_20211015_models.SubmitQualificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_qualification(
        self,
        request: dyvmsapi_intl_20211015_models.SubmitQualificationRequest,
    ) -> dyvmsapi_intl_20211015_models.SubmitQualificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_qualification_with_options(request, runtime)

    async def submit_qualification_async(
        self,
        request: dyvmsapi_intl_20211015_models.SubmitQualificationRequest,
    ) -> dyvmsapi_intl_20211015_models.SubmitQualificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_qualification_with_options_async(request, runtime)

    def submit_sip_trunk_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.SubmitSipTrunkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.SubmitSipTrunkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_note):
            query['ApplyNote'] = request.apply_note
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.inbound_ip_ports):
            query['InboundIpPorts'] = request.inbound_ip_ports
        if not UtilClient.is_unset(request.outbound_ips):
            query['OutboundIps'] = request.outbound_ips
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSipTrunk',
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
            dyvmsapi_intl_20211015_models.SubmitSipTrunkResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_sip_trunk_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.SubmitSipTrunkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.SubmitSipTrunkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_note):
            query['ApplyNote'] = request.apply_note
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.inbound_ip_ports):
            query['InboundIpPorts'] = request.inbound_ip_ports
        if not UtilClient.is_unset(request.outbound_ips):
            query['OutboundIps'] = request.outbound_ips
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSipTrunk',
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
            dyvmsapi_intl_20211015_models.SubmitSipTrunkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_sip_trunk(
        self,
        request: dyvmsapi_intl_20211015_models.SubmitSipTrunkRequest,
    ) -> dyvmsapi_intl_20211015_models.SubmitSipTrunkResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_sip_trunk_with_options(request, runtime)

    async def submit_sip_trunk_async(
        self,
        request: dyvmsapi_intl_20211015_models.SubmitSipTrunkRequest,
    ) -> dyvmsapi_intl_20211015_models.SubmitSipTrunkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_sip_trunk_with_options_async(request, runtime)

    def submit_voice_file_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.SubmitVoiceFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.SubmitVoiceFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.file_key):
            query['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitVoiceFile',
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
            dyvmsapi_intl_20211015_models.SubmitVoiceFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_voice_file_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.SubmitVoiceFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.SubmitVoiceFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.file_key):
            query['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitVoiceFile',
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
            dyvmsapi_intl_20211015_models.SubmitVoiceFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_voice_file(
        self,
        request: dyvmsapi_intl_20211015_models.SubmitVoiceFileRequest,
    ) -> dyvmsapi_intl_20211015_models.SubmitVoiceFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_voice_file_with_options(request, runtime)

    async def submit_voice_file_async(
        self,
        request: dyvmsapi_intl_20211015_models.SubmitVoiceFileRequest,
    ) -> dyvmsapi_intl_20211015_models.SubmitVoiceFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_voice_file_with_options_async(request, runtime)

    def submit_voice_tts_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.SubmitVoiceTtsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.SubmitVoiceTtsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_text):
            query['TemplateText'] = request.template_text
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitVoiceTts',
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
            dyvmsapi_intl_20211015_models.SubmitVoiceTtsResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_voice_tts_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.SubmitVoiceTtsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.SubmitVoiceTtsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_text):
            query['TemplateText'] = request.template_text
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitVoiceTts',
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
            dyvmsapi_intl_20211015_models.SubmitVoiceTtsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_voice_tts(
        self,
        request: dyvmsapi_intl_20211015_models.SubmitVoiceTtsRequest,
    ) -> dyvmsapi_intl_20211015_models.SubmitVoiceTtsResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_voice_tts_with_options(request, runtime)

    async def submit_voice_tts_async(
        self,
        request: dyvmsapi_intl_20211015_models.SubmitVoiceTtsRequest,
    ) -> dyvmsapi_intl_20211015_models.SubmitVoiceTtsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_voice_tts_with_options_async(request, runtime)

    def update_number_with_options(
        self,
        request: dyvmsapi_intl_20211015_models.UpdateNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.UpdateNumberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
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
            action='UpdateNumber',
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
            dyvmsapi_intl_20211015_models.UpdateNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_number_with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.UpdateNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.UpdateNumberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
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
            action='UpdateNumber',
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
            dyvmsapi_intl_20211015_models.UpdateNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_number(
        self,
        request: dyvmsapi_intl_20211015_models.UpdateNumberRequest,
    ) -> dyvmsapi_intl_20211015_models.UpdateNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_number_with_options(request, runtime)

    async def update_number_async(
        self,
        request: dyvmsapi_intl_20211015_models.UpdateNumberRequest,
    ) -> dyvmsapi_intl_20211015_models.UpdateNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_number_with_options_async(request, runtime)

    def test_02with_options(
        self,
        request: dyvmsapi_intl_20211015_models.Test02Request,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.Test02Response:
        UtilClient.validate_model(request)
        query = {}
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
            action='test02',
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
            dyvmsapi_intl_20211015_models.Test02Response(),
            self.call_api(params, req, runtime)
        )

    async def test_02with_options_async(
        self,
        request: dyvmsapi_intl_20211015_models.Test02Request,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_intl_20211015_models.Test02Response:
        UtilClient.validate_model(request)
        query = {}
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
            action='test02',
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
            dyvmsapi_intl_20211015_models.Test02Response(),
            await self.call_api_async(params, req, runtime)
        )

    def test_02(
        self,
        request: dyvmsapi_intl_20211015_models.Test02Request,
    ) -> dyvmsapi_intl_20211015_models.Test02Response:
        runtime = util_models.RuntimeOptions()
        return self.test_02with_options(request, runtime)

    async def test_02_async(
        self,
        request: dyvmsapi_intl_20211015_models.Test02Request,
    ) -> dyvmsapi_intl_20211015_models.Test02Response:
        runtime = util_models.RuntimeOptions()
        return await self.test_02with_options_async(request, runtime)
