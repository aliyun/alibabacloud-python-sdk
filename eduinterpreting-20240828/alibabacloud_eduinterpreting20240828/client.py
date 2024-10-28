# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eduinterpreting20240828 import models as edu_interpreting_20240828_models
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
        self._endpoint = self.get_endpoint('eduinterpreting', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def recognize_audio_with_options(
        self,
        request: edu_interpreting_20240828_models.RecognizeAudioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_interpreting_20240828_models.RecognizeAudioResponse:
        """
        @summary 英语口译语音文件识别成英文内容
        
        @param request: RecognizeAudioRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeAudioResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_call_back):
            query['EnableCallBack'] = request.enable_call_back
        body = {}
        if not UtilClient.is_unset(request.audio_file_url):
            body['AudioFileUrl'] = request.audio_file_url
        if not UtilClient.is_unset(request.callback_url):
            body['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.outer_biz_id):
            body['OuterBizId'] = request.outer_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeAudio',
            version='2024-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_interpreting_20240828_models.RecognizeAudioResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_audio_with_options_async(
        self,
        request: edu_interpreting_20240828_models.RecognizeAudioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_interpreting_20240828_models.RecognizeAudioResponse:
        """
        @summary 英语口译语音文件识别成英文内容
        
        @param request: RecognizeAudioRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeAudioResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_call_back):
            query['EnableCallBack'] = request.enable_call_back
        body = {}
        if not UtilClient.is_unset(request.audio_file_url):
            body['AudioFileUrl'] = request.audio_file_url
        if not UtilClient.is_unset(request.callback_url):
            body['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.outer_biz_id):
            body['OuterBizId'] = request.outer_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeAudio',
            version='2024-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_interpreting_20240828_models.RecognizeAudioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_audio(
        self,
        request: edu_interpreting_20240828_models.RecognizeAudioRequest,
    ) -> edu_interpreting_20240828_models.RecognizeAudioResponse:
        """
        @summary 英语口译语音文件识别成英文内容
        
        @param request: RecognizeAudioRequest
        @return: RecognizeAudioResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_audio_with_options(request, runtime)

    async def recognize_audio_async(
        self,
        request: edu_interpreting_20240828_models.RecognizeAudioRequest,
    ) -> edu_interpreting_20240828_models.RecognizeAudioResponse:
        """
        @summary 英语口译语音文件识别成英文内容
        
        @param request: RecognizeAudioRequest
        @return: RecognizeAudioResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_audio_with_options_async(request, runtime)

    def submit_evaluation_task_with_options(
        self,
        request: edu_interpreting_20240828_models.SubmitEvaluationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_interpreting_20240828_models.SubmitEvaluationTaskResponse:
        """
        @summary 口译评测任务
        
        @param request: SubmitEvaluationTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitEvaluationTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.audio_url):
            body['AudioUrl'] = request.audio_url
        if not UtilClient.is_unset(request.callback_url):
            body['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.material_text):
            body['MaterialText'] = request.material_text
        if not UtilClient.is_unset(request.outer_biz_id):
            body['OuterBizId'] = request.outer_biz_id
        if not UtilClient.is_unset(request.suggested_answer):
            body['SuggestedAnswer'] = request.suggested_answer
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitEvaluationTask',
            version='2024-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_interpreting_20240828_models.SubmitEvaluationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_evaluation_task_with_options_async(
        self,
        request: edu_interpreting_20240828_models.SubmitEvaluationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edu_interpreting_20240828_models.SubmitEvaluationTaskResponse:
        """
        @summary 口译评测任务
        
        @param request: SubmitEvaluationTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitEvaluationTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.audio_url):
            body['AudioUrl'] = request.audio_url
        if not UtilClient.is_unset(request.callback_url):
            body['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.material_text):
            body['MaterialText'] = request.material_text
        if not UtilClient.is_unset(request.outer_biz_id):
            body['OuterBizId'] = request.outer_biz_id
        if not UtilClient.is_unset(request.suggested_answer):
            body['SuggestedAnswer'] = request.suggested_answer
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitEvaluationTask',
            version='2024-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_interpreting_20240828_models.SubmitEvaluationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_evaluation_task(
        self,
        request: edu_interpreting_20240828_models.SubmitEvaluationTaskRequest,
    ) -> edu_interpreting_20240828_models.SubmitEvaluationTaskResponse:
        """
        @summary 口译评测任务
        
        @param request: SubmitEvaluationTaskRequest
        @return: SubmitEvaluationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_evaluation_task_with_options(request, runtime)

    async def submit_evaluation_task_async(
        self,
        request: edu_interpreting_20240828_models.SubmitEvaluationTaskRequest,
    ) -> edu_interpreting_20240828_models.SubmitEvaluationTaskResponse:
        """
        @summary 口译评测任务
        
        @param request: SubmitEvaluationTaskRequest
        @return: SubmitEvaluationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_evaluation_task_with_options_async(request, runtime)
