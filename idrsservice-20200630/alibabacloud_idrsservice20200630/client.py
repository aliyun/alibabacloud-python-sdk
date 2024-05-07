# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_idrsservice20200630 import models as idrsservice_20200630_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-1': 'idrsservice.aliyuncs.com',
            'ap-northeast-2-pop': 'idrsservice.aliyuncs.com',
            'ap-south-1': 'idrsservice.aliyuncs.com',
            'ap-southeast-1': 'idrsservice.aliyuncs.com',
            'ap-southeast-2': 'idrsservice.aliyuncs.com',
            'ap-southeast-3': 'idrsservice.aliyuncs.com',
            'ap-southeast-5': 'idrsservice.aliyuncs.com',
            'cn-beijing': 'idrsservice.aliyuncs.com',
            'cn-beijing-finance-1': 'idrsservice.aliyuncs.com',
            'cn-beijing-finance-pop': 'idrsservice.aliyuncs.com',
            'cn-beijing-gov-1': 'idrsservice.aliyuncs.com',
            'cn-beijing-nu16-b01': 'idrsservice.aliyuncs.com',
            'cn-chengdu': 'idrsservice.aliyuncs.com',
            'cn-edge-1': 'idrsservice.aliyuncs.com',
            'cn-fujian': 'idrsservice.aliyuncs.com',
            'cn-haidian-cm12-c01': 'idrsservice.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'idrsservice.aliyuncs.com',
            'cn-hangzhou-finance': 'idrsservice.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'idrsservice.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'idrsservice.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'idrsservice.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'idrsservice.aliyuncs.com',
            'cn-hangzhou-test-306': 'idrsservice.aliyuncs.com',
            'cn-hongkong': 'idrsservice.aliyuncs.com',
            'cn-hongkong-finance-pop': 'idrsservice.aliyuncs.com',
            'cn-huhehaote': 'idrsservice.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'idrsservice.aliyuncs.com',
            'cn-north-2-gov-1': 'idrsservice.aliyuncs.com',
            'cn-qingdao': 'idrsservice.aliyuncs.com',
            'cn-qingdao-nebula': 'idrsservice.aliyuncs.com',
            'cn-shanghai': 'idrsservice.aliyuncs.com',
            'cn-shanghai-et15-b01': 'idrsservice.aliyuncs.com',
            'cn-shanghai-et2-b01': 'idrsservice.aliyuncs.com',
            'cn-shanghai-inner': 'idrsservice.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'idrsservice.aliyuncs.com',
            'cn-shenzhen': 'idrsservice.aliyuncs.com',
            'cn-shenzhen-finance-1': 'idrsservice.aliyuncs.com',
            'cn-shenzhen-inner': 'idrsservice.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'idrsservice.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'idrsservice.aliyuncs.com',
            'cn-wuhan': 'idrsservice.aliyuncs.com',
            'cn-wulanchabu': 'idrsservice.aliyuncs.com',
            'cn-yushanfang': 'idrsservice.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'idrsservice.aliyuncs.com',
            'cn-zhangjiakou': 'idrsservice.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'idrsservice.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'idrsservice.aliyuncs.com',
            'eu-central-1': 'idrsservice.aliyuncs.com',
            'eu-west-1': 'idrsservice.aliyuncs.com',
            'eu-west-1-oxs': 'idrsservice.aliyuncs.com',
            'me-east-1': 'idrsservice.aliyuncs.com',
            'rus-west-1-pop': 'idrsservice.aliyuncs.com',
            'us-east-1': 'idrsservice.aliyuncs.com',
            'us-west-1': 'idrsservice.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('idrsservice', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def asr_realtime_with_options(
        self,
        request: idrsservice_20200630_models.AsrRealtimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.AsrRealtimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.customization_id):
            query['CustomizationId'] = request.customization_id
        if not UtilClient.is_unset(request.disfluency):
            query['Disfluency'] = request.disfluency
        if not UtilClient.is_unset(request.enable_ignore_sentence_timeout):
            query['EnableIgnoreSentenceTimeout'] = request.enable_ignore_sentence_timeout
        if not UtilClient.is_unset(request.enable_intermediate_result):
            query['EnableIntermediateResult'] = request.enable_intermediate_result
        if not UtilClient.is_unset(request.enable_inverse_text_normalization):
            query['EnableInverseTextNormalization'] = request.enable_inverse_text_normalization
        if not UtilClient.is_unset(request.enable_punctuation_prediction):
            query['EnablePunctuationPrediction'] = request.enable_punctuation_prediction
        if not UtilClient.is_unset(request.enable_semantic_sentence_detection):
            query['EnableSemanticSentenceDetection'] = request.enable_semantic_sentence_detection
        if not UtilClient.is_unset(request.enable_words):
            query['EnableWords'] = request.enable_words
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.format):
            query['Format'] = request.format
        if not UtilClient.is_unset(request.max_sentence_silence):
            query['MaxSentenceSilence'] = request.max_sentence_silence
        if not UtilClient.is_unset(request.sample_rate):
            query['SampleRate'] = request.sample_rate
        if not UtilClient.is_unset(request.speech_noise_threshold):
            query['SpeechNoiseThreshold'] = request.speech_noise_threshold
        if not UtilClient.is_unset(request.vocabulary_id):
            query['VocabularyId'] = request.vocabulary_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AsrRealtime',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.AsrRealtimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def asr_realtime_with_options_async(
        self,
        request: idrsservice_20200630_models.AsrRealtimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.AsrRealtimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.customization_id):
            query['CustomizationId'] = request.customization_id
        if not UtilClient.is_unset(request.disfluency):
            query['Disfluency'] = request.disfluency
        if not UtilClient.is_unset(request.enable_ignore_sentence_timeout):
            query['EnableIgnoreSentenceTimeout'] = request.enable_ignore_sentence_timeout
        if not UtilClient.is_unset(request.enable_intermediate_result):
            query['EnableIntermediateResult'] = request.enable_intermediate_result
        if not UtilClient.is_unset(request.enable_inverse_text_normalization):
            query['EnableInverseTextNormalization'] = request.enable_inverse_text_normalization
        if not UtilClient.is_unset(request.enable_punctuation_prediction):
            query['EnablePunctuationPrediction'] = request.enable_punctuation_prediction
        if not UtilClient.is_unset(request.enable_semantic_sentence_detection):
            query['EnableSemanticSentenceDetection'] = request.enable_semantic_sentence_detection
        if not UtilClient.is_unset(request.enable_words):
            query['EnableWords'] = request.enable_words
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.format):
            query['Format'] = request.format
        if not UtilClient.is_unset(request.max_sentence_silence):
            query['MaxSentenceSilence'] = request.max_sentence_silence
        if not UtilClient.is_unset(request.sample_rate):
            query['SampleRate'] = request.sample_rate
        if not UtilClient.is_unset(request.speech_noise_threshold):
            query['SpeechNoiseThreshold'] = request.speech_noise_threshold
        if not UtilClient.is_unset(request.vocabulary_id):
            query['VocabularyId'] = request.vocabulary_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AsrRealtime',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.AsrRealtimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def asr_realtime(
        self,
        request: idrsservice_20200630_models.AsrRealtimeRequest,
    ) -> idrsservice_20200630_models.AsrRealtimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.asr_realtime_with_options(request, runtime)

    async def asr_realtime_async(
        self,
        request: idrsservice_20200630_models.AsrRealtimeRequest,
    ) -> idrsservice_20200630_models.AsrRealtimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.asr_realtime_with_options_async(request, runtime)

    def asr_sentence_with_options(
        self,
        tmp_req: idrsservice_20200630_models.AsrSentenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.AsrSentenceResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.AsrSentenceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.asr_request):
            request.asr_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.asr_request, 'AsrRequest', 'json')
        body = {}
        if not UtilClient.is_unset(request.asr_request_shrink):
            body['AsrRequest'] = request.asr_request_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AsrSentence',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.AsrSentenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def asr_sentence_with_options_async(
        self,
        tmp_req: idrsservice_20200630_models.AsrSentenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.AsrSentenceResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.AsrSentenceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.asr_request):
            request.asr_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.asr_request, 'AsrRequest', 'json')
        body = {}
        if not UtilClient.is_unset(request.asr_request_shrink):
            body['AsrRequest'] = request.asr_request_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AsrSentence',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.AsrSentenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def asr_sentence(
        self,
        request: idrsservice_20200630_models.AsrSentenceRequest,
    ) -> idrsservice_20200630_models.AsrSentenceResponse:
        runtime = util_models.RuntimeOptions()
        return self.asr_sentence_with_options(request, runtime)

    async def asr_sentence_async(
        self,
        request: idrsservice_20200630_models.AsrSentenceRequest,
    ) -> idrsservice_20200630_models.AsrSentenceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.asr_sentence_with_options_async(request, runtime)

    def asr_task_with_options(
        self,
        tmp_req: idrsservice_20200630_models.AsrTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.AsrTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.AsrTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AsrTask',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.AsrTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def asr_task_with_options_async(
        self,
        tmp_req: idrsservice_20200630_models.AsrTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.AsrTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.AsrTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AsrTask',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.AsrTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def asr_task(
        self,
        request: idrsservice_20200630_models.AsrTaskRequest,
    ) -> idrsservice_20200630_models.AsrTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.asr_task_with_options(request, runtime)

    async def asr_task_async(
        self,
        request: idrsservice_20200630_models.AsrTaskRequest,
    ) -> idrsservice_20200630_models.AsrTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.asr_task_with_options_async(request, runtime)

    def associate_room_with_options(
        self,
        request: idrsservice_20200630_models.AssociateRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.AssociateRoomResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateRoom',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.AssociateRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_room_with_options_async(
        self,
        request: idrsservice_20200630_models.AssociateRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.AssociateRoomResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateRoom',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.AssociateRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_room(
        self,
        request: idrsservice_20200630_models.AssociateRoomRequest,
    ) -> idrsservice_20200630_models.AssociateRoomResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_room_with_options(request, runtime)

    async def associate_room_async(
        self,
        request: idrsservice_20200630_models.AssociateRoomRequest,
    ) -> idrsservice_20200630_models.AssociateRoomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_room_with_options_async(request, runtime)

    def create_app_with_options(
        self,
        request: idrsservice_20200630_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.package_name):
            query['PackageName'] = request.package_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_with_options_async(
        self,
        request: idrsservice_20200630_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.package_name):
            query['PackageName'] = request.package_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app(
        self,
        request: idrsservice_20200630_models.CreateAppRequest,
    ) -> idrsservice_20200630_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    async def create_app_async(
        self,
        request: idrsservice_20200630_models.CreateAppRequest,
    ) -> idrsservice_20200630_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_with_options_async(request, runtime)

    def create_department_with_options(
        self,
        request: idrsservice_20200630_models.CreateDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateDepartmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDepartment',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateDepartmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_department_with_options_async(
        self,
        request: idrsservice_20200630_models.CreateDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateDepartmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDepartment',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateDepartmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_department(
        self,
        request: idrsservice_20200630_models.CreateDepartmentRequest,
    ) -> idrsservice_20200630_models.CreateDepartmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_department_with_options(request, runtime)

    async def create_department_async(
        self,
        request: idrsservice_20200630_models.CreateDepartmentRequest,
    ) -> idrsservice_20200630_models.CreateDepartmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_department_with_options_async(request, runtime)

    def create_detect_process_with_options(
        self,
        request: idrsservice_20200630_models.CreateDetectProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateDetectProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.draft):
            query['Draft'] = request.draft
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDetectProcess',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateDetectProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_detect_process_with_options_async(
        self,
        request: idrsservice_20200630_models.CreateDetectProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateDetectProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.draft):
            query['Draft'] = request.draft
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDetectProcess',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateDetectProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_detect_process(
        self,
        request: idrsservice_20200630_models.CreateDetectProcessRequest,
    ) -> idrsservice_20200630_models.CreateDetectProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_detect_process_with_options(request, runtime)

    async def create_detect_process_async(
        self,
        request: idrsservice_20200630_models.CreateDetectProcessRequest,
    ) -> idrsservice_20200630_models.CreateDetectProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_detect_process_with_options_async(request, runtime)

    def create_rule_with_options(
        self,
        request: idrsservice_20200630_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRule',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rule_with_options_async(
        self,
        request: idrsservice_20200630_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRule',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rule(
        self,
        request: idrsservice_20200630_models.CreateRuleRequest,
    ) -> idrsservice_20200630_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    async def create_rule_async(
        self,
        request: idrsservice_20200630_models.CreateRuleRequest,
    ) -> idrsservice_20200630_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_rule_with_options_async(request, runtime)

    def create_signature_with_options(
        self,
        request: idrsservice_20200630_models.CreateSignatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateSignatureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSignature',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_signature_with_options_async(
        self,
        request: idrsservice_20200630_models.CreateSignatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateSignatureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSignature',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateSignatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_signature(
        self,
        request: idrsservice_20200630_models.CreateSignatureRequest,
    ) -> idrsservice_20200630_models.CreateSignatureResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_signature_with_options(request, runtime)

    async def create_signature_async(
        self,
        request: idrsservice_20200630_models.CreateSignatureRequest,
    ) -> idrsservice_20200630_models.CreateSignatureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_signature_with_options_async(request, runtime)

    def create_task_group_with_options(
        self,
        request: idrsservice_20200630_models.CreateTaskGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateTaskGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.day):
            query['Day'] = request.day
        if not UtilClient.is_unset(request.expire_at):
            query['ExpireAt'] = request.expire_at
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.runnable_time_from):
            query['RunnableTimeFrom'] = request.runnable_time_from
        if not UtilClient.is_unset(request.runnable_time_to):
            query['RunnableTimeTo'] = request.runnable_time_to
        if not UtilClient.is_unset(request.trigger_period):
            query['TriggerPeriod'] = request.trigger_period
        if not UtilClient.is_unset(request.video_info):
            query['VideoInfo'] = request.video_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTaskGroup',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateTaskGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_task_group_with_options_async(
        self,
        request: idrsservice_20200630_models.CreateTaskGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateTaskGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.day):
            query['Day'] = request.day
        if not UtilClient.is_unset(request.expire_at):
            query['ExpireAt'] = request.expire_at
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.runnable_time_from):
            query['RunnableTimeFrom'] = request.runnable_time_from
        if not UtilClient.is_unset(request.runnable_time_to):
            query['RunnableTimeTo'] = request.runnable_time_to
        if not UtilClient.is_unset(request.trigger_period):
            query['TriggerPeriod'] = request.trigger_period
        if not UtilClient.is_unset(request.video_info):
            query['VideoInfo'] = request.video_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTaskGroup',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateTaskGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_task_group(
        self,
        request: idrsservice_20200630_models.CreateTaskGroupRequest,
    ) -> idrsservice_20200630_models.CreateTaskGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_task_group_with_options(request, runtime)

    async def create_task_group_async(
        self,
        request: idrsservice_20200630_models.CreateTaskGroupRequest,
    ) -> idrsservice_20200630_models.CreateTaskGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_task_group_with_options_async(request, runtime)

    def create_tts_question_with_options(
        self,
        tmp_req: idrsservice_20200630_models.CreateTtsQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateTtsQuestionResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.CreateTtsQuestionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTtsQuestion',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateTtsQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tts_question_with_options_async(
        self,
        tmp_req: idrsservice_20200630_models.CreateTtsQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateTtsQuestionResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.CreateTtsQuestionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTtsQuestion',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateTtsQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tts_question(
        self,
        request: idrsservice_20200630_models.CreateTtsQuestionRequest,
    ) -> idrsservice_20200630_models.CreateTtsQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_tts_question_with_options(request, runtime)

    async def create_tts_question_async(
        self,
        request: idrsservice_20200630_models.CreateTtsQuestionRequest,
    ) -> idrsservice_20200630_models.CreateTtsQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_tts_question_with_options_async(request, runtime)

    def create_tts_question_group_with_options(
        self,
        tmp_req: idrsservice_20200630_models.CreateTtsQuestionGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateTtsQuestionGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.CreateTtsQuestionGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTtsQuestionGroup',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateTtsQuestionGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tts_question_group_with_options_async(
        self,
        tmp_req: idrsservice_20200630_models.CreateTtsQuestionGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateTtsQuestionGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.CreateTtsQuestionGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTtsQuestionGroup',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateTtsQuestionGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tts_question_group(
        self,
        request: idrsservice_20200630_models.CreateTtsQuestionGroupRequest,
    ) -> idrsservice_20200630_models.CreateTtsQuestionGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_tts_question_group_with_options(request, runtime)

    async def create_tts_question_group_async(
        self,
        request: idrsservice_20200630_models.CreateTtsQuestionGroupRequest,
    ) -> idrsservice_20200630_models.CreateTtsQuestionGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_tts_question_group_with_options_async(request, runtime)

    def create_user_departments_with_options(
        self,
        request: idrsservice_20200630_models.CreateUserDepartmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateUserDepartmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserDepartments',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateUserDepartmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_departments_with_options_async(
        self,
        request: idrsservice_20200630_models.CreateUserDepartmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateUserDepartmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserDepartments',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateUserDepartmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_departments(
        self,
        request: idrsservice_20200630_models.CreateUserDepartmentsRequest,
    ) -> idrsservice_20200630_models.CreateUserDepartmentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_departments_with_options(request, runtime)

    async def create_user_departments_async(
        self,
        request: idrsservice_20200630_models.CreateUserDepartmentsRequest,
    ) -> idrsservice_20200630_models.CreateUserDepartmentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_departments_with_options_async(request, runtime)

    def create_video_merge_task_with_options(
        self,
        tmp_req: idrsservice_20200630_models.CreateVideoMergeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateVideoMergeTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.CreateVideoMergeTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.video_merge_request):
            request.video_merge_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_merge_request, 'VideoMergeRequest', 'json')
        body = {}
        if not UtilClient.is_unset(request.video_merge_request_shrink):
            body['VideoMergeRequest'] = request.video_merge_request_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVideoMergeTask',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateVideoMergeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_video_merge_task_with_options_async(
        self,
        tmp_req: idrsservice_20200630_models.CreateVideoMergeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateVideoMergeTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.CreateVideoMergeTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.video_merge_request):
            request.video_merge_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_merge_request, 'VideoMergeRequest', 'json')
        body = {}
        if not UtilClient.is_unset(request.video_merge_request_shrink):
            body['VideoMergeRequest'] = request.video_merge_request_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVideoMergeTask',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateVideoMergeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_video_merge_task(
        self,
        request: idrsservice_20200630_models.CreateVideoMergeTaskRequest,
    ) -> idrsservice_20200630_models.CreateVideoMergeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_video_merge_task_with_options(request, runtime)

    async def create_video_merge_task_async(
        self,
        request: idrsservice_20200630_models.CreateVideoMergeTaskRequest,
    ) -> idrsservice_20200630_models.CreateVideoMergeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_video_merge_task_with_options_async(request, runtime)

    def create_watermark_with_options(
        self,
        request: idrsservice_20200630_models.CreateWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateWatermarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWatermark',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_watermark_with_options_async(
        self,
        request: idrsservice_20200630_models.CreateWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateWatermarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWatermark',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateWatermarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_watermark(
        self,
        request: idrsservice_20200630_models.CreateWatermarkRequest,
    ) -> idrsservice_20200630_models.CreateWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_watermark_with_options(request, runtime)

    async def create_watermark_async(
        self,
        request: idrsservice_20200630_models.CreateWatermarkRequest,
    ) -> idrsservice_20200630_models.CreateWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_watermark_with_options_async(request, runtime)

    def delete_app_with_options(
        self,
        request: idrsservice_20200630_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_with_options_async(
        self,
        request: idrsservice_20200630_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app(
        self,
        request: idrsservice_20200630_models.DeleteAppRequest,
    ) -> idrsservice_20200630_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    async def delete_app_async(
        self,
        request: idrsservice_20200630_models.DeleteAppRequest,
    ) -> idrsservice_20200630_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_with_options_async(request, runtime)

    def delete_department_with_options(
        self,
        request: idrsservice_20200630_models.DeleteDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteDepartmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDepartment',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteDepartmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_department_with_options_async(
        self,
        request: idrsservice_20200630_models.DeleteDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteDepartmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDepartment',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteDepartmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_department(
        self,
        request: idrsservice_20200630_models.DeleteDepartmentRequest,
    ) -> idrsservice_20200630_models.DeleteDepartmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_department_with_options(request, runtime)

    async def delete_department_async(
        self,
        request: idrsservice_20200630_models.DeleteDepartmentRequest,
    ) -> idrsservice_20200630_models.DeleteDepartmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_department_with_options_async(request, runtime)

    def delete_detect_process_with_options(
        self,
        request: idrsservice_20200630_models.DeleteDetectProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteDetectProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDetectProcess',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteDetectProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_detect_process_with_options_async(
        self,
        request: idrsservice_20200630_models.DeleteDetectProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteDetectProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDetectProcess',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteDetectProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_detect_process(
        self,
        request: idrsservice_20200630_models.DeleteDetectProcessRequest,
    ) -> idrsservice_20200630_models.DeleteDetectProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_detect_process_with_options(request, runtime)

    async def delete_detect_process_async(
        self,
        request: idrsservice_20200630_models.DeleteDetectProcessRequest,
    ) -> idrsservice_20200630_models.DeleteDetectProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_detect_process_with_options_async(request, runtime)

    def delete_rule_with_options(
        self,
        request: idrsservice_20200630_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRule',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rule_with_options_async(
        self,
        request: idrsservice_20200630_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRule',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rule(
        self,
        request: idrsservice_20200630_models.DeleteRuleRequest,
    ) -> idrsservice_20200630_models.DeleteRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    async def delete_rule_async(
        self,
        request: idrsservice_20200630_models.DeleteRuleRequest,
    ) -> idrsservice_20200630_models.DeleteRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_rule_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: idrsservice_20200630_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: idrsservice_20200630_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user(
        self,
        request: idrsservice_20200630_models.DeleteUserRequest,
    ) -> idrsservice_20200630_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: idrsservice_20200630_models.DeleteUserRequest,
    ) -> idrsservice_20200630_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def delete_user_departments_with_options(
        self,
        request: idrsservice_20200630_models.DeleteUserDepartmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteUserDepartmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUserDepartments',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteUserDepartmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_departments_with_options_async(
        self,
        request: idrsservice_20200630_models.DeleteUserDepartmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteUserDepartmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUserDepartments',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteUserDepartmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_departments(
        self,
        request: idrsservice_20200630_models.DeleteUserDepartmentsRequest,
    ) -> idrsservice_20200630_models.DeleteUserDepartmentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_departments_with_options(request, runtime)

    async def delete_user_departments_async(
        self,
        request: idrsservice_20200630_models.DeleteUserDepartmentsRequest,
    ) -> idrsservice_20200630_models.DeleteUserDepartmentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_departments_with_options_async(request, runtime)

    def delete_watermark_with_options(
        self,
        request: idrsservice_20200630_models.DeleteWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteWatermarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.watermark_id):
            query['WatermarkId'] = request.watermark_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWatermark',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_watermark_with_options_async(
        self,
        request: idrsservice_20200630_models.DeleteWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteWatermarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.watermark_id):
            query['WatermarkId'] = request.watermark_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWatermark',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteWatermarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_watermark(
        self,
        request: idrsservice_20200630_models.DeleteWatermarkRequest,
    ) -> idrsservice_20200630_models.DeleteWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_watermark_with_options(request, runtime)

    async def delete_watermark_async(
        self,
        request: idrsservice_20200630_models.DeleteWatermarkRequest,
    ) -> idrsservice_20200630_models.DeleteWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_watermark_with_options_async(request, runtime)

    def face_compare_with_options(
        self,
        tmp_req: idrsservice_20200630_models.FaceCompareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.FaceCompareResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.FaceCompareShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.face_request):
            request.face_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.face_request, 'FaceRequest', 'json')
        body = {}
        if not UtilClient.is_unset(request.face_request_shrink):
            body['FaceRequest'] = request.face_request_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FaceCompare',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.FaceCompareResponse(),
            self.call_api(params, req, runtime)
        )

    async def face_compare_with_options_async(
        self,
        tmp_req: idrsservice_20200630_models.FaceCompareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.FaceCompareResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.FaceCompareShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.face_request):
            request.face_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.face_request, 'FaceRequest', 'json')
        body = {}
        if not UtilClient.is_unset(request.face_request_shrink):
            body['FaceRequest'] = request.face_request_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FaceCompare',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.FaceCompareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def face_compare(
        self,
        request: idrsservice_20200630_models.FaceCompareRequest,
    ) -> idrsservice_20200630_models.FaceCompareResponse:
        runtime = util_models.RuntimeOptions()
        return self.face_compare_with_options(request, runtime)

    async def face_compare_async(
        self,
        request: idrsservice_20200630_models.FaceCompareRequest,
    ) -> idrsservice_20200630_models.FaceCompareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.face_compare_with_options_async(request, runtime)

    def face_liveness_with_options(
        self,
        tmp_req: idrsservice_20200630_models.FaceLivenessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.FaceLivenessResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.FaceLivenessShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.face_request):
            request.face_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.face_request, 'FaceRequest', 'json')
        body = {}
        if not UtilClient.is_unset(request.face_request_shrink):
            body['FaceRequest'] = request.face_request_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FaceLiveness',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.FaceLivenessResponse(),
            self.call_api(params, req, runtime)
        )

    async def face_liveness_with_options_async(
        self,
        tmp_req: idrsservice_20200630_models.FaceLivenessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.FaceLivenessResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.FaceLivenessShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.face_request):
            request.face_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.face_request, 'FaceRequest', 'json')
        body = {}
        if not UtilClient.is_unset(request.face_request_shrink):
            body['FaceRequest'] = request.face_request_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FaceLiveness',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.FaceLivenessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def face_liveness(
        self,
        request: idrsservice_20200630_models.FaceLivenessRequest,
    ) -> idrsservice_20200630_models.FaceLivenessResponse:
        runtime = util_models.RuntimeOptions()
        return self.face_liveness_with_options(request, runtime)

    async def face_liveness_async(
        self,
        request: idrsservice_20200630_models.FaceLivenessRequest,
    ) -> idrsservice_20200630_models.FaceLivenessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.face_liveness_with_options_async(request, runtime)

    def face_recognize_with_options(
        self,
        tmp_req: idrsservice_20200630_models.FaceRecognizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.FaceRecognizeResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.FaceRecognizeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.face_request):
            request.face_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.face_request, 'FaceRequest', 'json')
        body = {}
        if not UtilClient.is_unset(request.face_request_shrink):
            body['FaceRequest'] = request.face_request_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FaceRecognize',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.FaceRecognizeResponse(),
            self.call_api(params, req, runtime)
        )

    async def face_recognize_with_options_async(
        self,
        tmp_req: idrsservice_20200630_models.FaceRecognizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.FaceRecognizeResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.FaceRecognizeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.face_request):
            request.face_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.face_request, 'FaceRequest', 'json')
        body = {}
        if not UtilClient.is_unset(request.face_request_shrink):
            body['FaceRequest'] = request.face_request_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FaceRecognize',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.FaceRecognizeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def face_recognize(
        self,
        request: idrsservice_20200630_models.FaceRecognizeRequest,
    ) -> idrsservice_20200630_models.FaceRecognizeResponse:
        runtime = util_models.RuntimeOptions()
        return self.face_recognize_with_options(request, runtime)

    async def face_recognize_async(
        self,
        request: idrsservice_20200630_models.FaceRecognizeRequest,
    ) -> idrsservice_20200630_models.FaceRecognizeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.face_recognize_with_options_async(request, runtime)

    def get_app_with_options(
        self,
        request: idrsservice_20200630_models.GetAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.package_name):
            query['PackageName'] = request.package_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApp',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_with_options_async(
        self,
        request: idrsservice_20200630_models.GetAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.package_name):
            query['PackageName'] = request.package_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApp',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app(
        self,
        request: idrsservice_20200630_models.GetAppRequest,
    ) -> idrsservice_20200630_models.GetAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_app_with_options(request, runtime)

    async def get_app_async(
        self,
        request: idrsservice_20200630_models.GetAppRequest,
    ) -> idrsservice_20200630_models.GetAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_app_with_options_async(request, runtime)

    def get_asr_result_with_options(
        self,
        request: idrsservice_20200630_models.GetAsrResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetAsrResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asr_task_id):
            query['AsrTaskId'] = request.asr_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsrResult',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetAsrResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_asr_result_with_options_async(
        self,
        request: idrsservice_20200630_models.GetAsrResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetAsrResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asr_task_id):
            query['AsrTaskId'] = request.asr_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsrResult',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetAsrResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_asr_result(
        self,
        request: idrsservice_20200630_models.GetAsrResultRequest,
    ) -> idrsservice_20200630_models.GetAsrResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_asr_result_with_options(request, runtime)

    async def get_asr_result_async(
        self,
        request: idrsservice_20200630_models.GetAsrResultRequest,
    ) -> idrsservice_20200630_models.GetAsrResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_asr_result_with_options_async(request, runtime)

    def get_department_with_options(
        self,
        request: idrsservice_20200630_models.GetDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetDepartmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDepartment',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetDepartmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_department_with_options_async(
        self,
        request: idrsservice_20200630_models.GetDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetDepartmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDepartment',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetDepartmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_department(
        self,
        request: idrsservice_20200630_models.GetDepartmentRequest,
    ) -> idrsservice_20200630_models.GetDepartmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_department_with_options(request, runtime)

    async def get_department_async(
        self,
        request: idrsservice_20200630_models.GetDepartmentRequest,
    ) -> idrsservice_20200630_models.GetDepartmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_department_with_options_async(request, runtime)

    def get_detect_process_with_options(
        self,
        request: idrsservice_20200630_models.GetDetectProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetDetectProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDetectProcess',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetDetectProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_detect_process_with_options_async(
        self,
        request: idrsservice_20200630_models.GetDetectProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetDetectProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDetectProcess',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetDetectProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_detect_process(
        self,
        request: idrsservice_20200630_models.GetDetectProcessRequest,
    ) -> idrsservice_20200630_models.GetDetectProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_detect_process_with_options(request, runtime)

    async def get_detect_process_async(
        self,
        request: idrsservice_20200630_models.GetDetectProcessRequest,
    ) -> idrsservice_20200630_models.GetDetectProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_detect_process_with_options_async(request, runtime)

    def get_detect_process_json_file_with_options(
        self,
        request: idrsservice_20200630_models.GetDetectProcessJsonFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetDetectProcessJsonFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDetectProcessJsonFile',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetDetectProcessJsonFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_detect_process_json_file_with_options_async(
        self,
        request: idrsservice_20200630_models.GetDetectProcessJsonFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetDetectProcessJsonFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDetectProcessJsonFile',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetDetectProcessJsonFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_detect_process_json_file(
        self,
        request: idrsservice_20200630_models.GetDetectProcessJsonFileRequest,
    ) -> idrsservice_20200630_models.GetDetectProcessJsonFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_detect_process_json_file_with_options(request, runtime)

    async def get_detect_process_json_file_async(
        self,
        request: idrsservice_20200630_models.GetDetectProcessJsonFileRequest,
    ) -> idrsservice_20200630_models.GetDetectProcessJsonFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_detect_process_json_file_with_options_async(request, runtime)

    def get_detection_with_options(
        self,
        request: idrsservice_20200630_models.GetDetectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetDetectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDetection',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetDetectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_detection_with_options_async(
        self,
        request: idrsservice_20200630_models.GetDetectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetDetectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDetection',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetDetectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_detection(
        self,
        request: idrsservice_20200630_models.GetDetectionRequest,
    ) -> idrsservice_20200630_models.GetDetectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_detection_with_options(request, runtime)

    async def get_detection_async(
        self,
        request: idrsservice_20200630_models.GetDetectionRequest,
    ) -> idrsservice_20200630_models.GetDetectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_detection_with_options_async(request, runtime)

    def get_pre_signed_url_with_options(
        self,
        request: idrsservice_20200630_models.GetPreSignedUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetPreSignedUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        body = {}
        if not UtilClient.is_unset(request.prefix):
            body['Prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPreSignedUrl',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetPreSignedUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pre_signed_url_with_options_async(
        self,
        request: idrsservice_20200630_models.GetPreSignedUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetPreSignedUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        body = {}
        if not UtilClient.is_unset(request.prefix):
            body['Prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPreSignedUrl',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetPreSignedUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pre_signed_url(
        self,
        request: idrsservice_20200630_models.GetPreSignedUrlRequest,
    ) -> idrsservice_20200630_models.GetPreSignedUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_pre_signed_url_with_options(request, runtime)

    async def get_pre_signed_url_async(
        self,
        request: idrsservice_20200630_models.GetPreSignedUrlRequest,
    ) -> idrsservice_20200630_models.GetPreSignedUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_pre_signed_url_with_options_async(request, runtime)

    def get_record_result_with_options(
        self,
        request: idrsservice_20200630_models.GetRecordResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetRecordResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRecordResult',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetRecordResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_record_result_with_options_async(
        self,
        request: idrsservice_20200630_models.GetRecordResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetRecordResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRecordResult',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetRecordResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_record_result(
        self,
        request: idrsservice_20200630_models.GetRecordResultRequest,
    ) -> idrsservice_20200630_models.GetRecordResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_record_result_with_options(request, runtime)

    async def get_record_result_async(
        self,
        request: idrsservice_20200630_models.GetRecordResultRequest,
    ) -> idrsservice_20200630_models.GetRecordResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_record_result_with_options_async(request, runtime)

    def get_records_by_fee_id_with_options(
        self,
        request: idrsservice_20200630_models.GetRecordsByFeeIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetRecordsByFeeIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fee_id):
            body['FeeId'] = request.fee_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRecordsByFeeId',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetRecordsByFeeIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_records_by_fee_id_with_options_async(
        self,
        request: idrsservice_20200630_models.GetRecordsByFeeIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetRecordsByFeeIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fee_id):
            body['FeeId'] = request.fee_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRecordsByFeeId',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetRecordsByFeeIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_records_by_fee_id(
        self,
        request: idrsservice_20200630_models.GetRecordsByFeeIdRequest,
    ) -> idrsservice_20200630_models.GetRecordsByFeeIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_records_by_fee_id_with_options(request, runtime)

    async def get_records_by_fee_id_async(
        self,
        request: idrsservice_20200630_models.GetRecordsByFeeIdRequest,
    ) -> idrsservice_20200630_models.GetRecordsByFeeIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_records_by_fee_id_with_options_async(request, runtime)

    def get_records_by_outer_business_id_with_options(
        self,
        request: idrsservice_20200630_models.GetRecordsByOuterBusinessIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetRecordsByOuterBusinessIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.outer_business_id):
            query['OuterBusinessId'] = request.outer_business_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRecordsByOuterBusinessId',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetRecordsByOuterBusinessIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_records_by_outer_business_id_with_options_async(
        self,
        request: idrsservice_20200630_models.GetRecordsByOuterBusinessIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetRecordsByOuterBusinessIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.outer_business_id):
            query['OuterBusinessId'] = request.outer_business_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRecordsByOuterBusinessId',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetRecordsByOuterBusinessIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_records_by_outer_business_id(
        self,
        request: idrsservice_20200630_models.GetRecordsByOuterBusinessIdRequest,
    ) -> idrsservice_20200630_models.GetRecordsByOuterBusinessIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_records_by_outer_business_id_with_options(request, runtime)

    async def get_records_by_outer_business_id_async(
        self,
        request: idrsservice_20200630_models.GetRecordsByOuterBusinessIdRequest,
    ) -> idrsservice_20200630_models.GetRecordsByOuterBusinessIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_records_by_outer_business_id_with_options_async(request, runtime)

    def get_rule_with_options(
        self,
        request: idrsservice_20200630_models.GetRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRule',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rule_with_options_async(
        self,
        request: idrsservice_20200630_models.GetRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRule',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rule(
        self,
        request: idrsservice_20200630_models.GetRuleRequest,
    ) -> idrsservice_20200630_models.GetRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_rule_with_options(request, runtime)

    async def get_rule_async(
        self,
        request: idrsservice_20200630_models.GetRuleRequest,
    ) -> idrsservice_20200630_models.GetRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_rule_with_options_async(request, runtime)

    def get_statistics_records_by_fee_id_with_options(
        self,
        request: idrsservice_20200630_models.GetStatisticsRecordsByFeeIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetStatisticsRecordsByFeeIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fee_id):
            body['FeeId'] = request.fee_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetStatisticsRecordsByFeeId',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetStatisticsRecordsByFeeIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_statistics_records_by_fee_id_with_options_async(
        self,
        request: idrsservice_20200630_models.GetStatisticsRecordsByFeeIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetStatisticsRecordsByFeeIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fee_id):
            body['FeeId'] = request.fee_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetStatisticsRecordsByFeeId',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetStatisticsRecordsByFeeIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_statistics_records_by_fee_id(
        self,
        request: idrsservice_20200630_models.GetStatisticsRecordsByFeeIdRequest,
    ) -> idrsservice_20200630_models.GetStatisticsRecordsByFeeIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_statistics_records_by_fee_id_with_options(request, runtime)

    async def get_statistics_records_by_fee_id_async(
        self,
        request: idrsservice_20200630_models.GetStatisticsRecordsByFeeIdRequest,
    ) -> idrsservice_20200630_models.GetStatisticsRecordsByFeeIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_statistics_records_by_fee_id_with_options_async(request, runtime)

    def get_task_with_options(
        self,
        request: idrsservice_20200630_models.GetTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        request: idrsservice_20200630_models.GetTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        request: idrsservice_20200630_models.GetTaskRequest,
    ) -> idrsservice_20200630_models.GetTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_with_options(request, runtime)

    async def get_task_async(
        self,
        request: idrsservice_20200630_models.GetTaskRequest,
    ) -> idrsservice_20200630_models.GetTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_with_options_async(request, runtime)

    def get_task_group_with_options(
        self,
        request: idrsservice_20200630_models.GetTaskGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetTaskGroupResponse:
        """
        *1**\
        
        @param request: GetTaskGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskGroup',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetTaskGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_group_with_options_async(
        self,
        request: idrsservice_20200630_models.GetTaskGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetTaskGroupResponse:
        """
        *1**\
        
        @param request: GetTaskGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskGroup',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetTaskGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_group(
        self,
        request: idrsservice_20200630_models.GetTaskGroupRequest,
    ) -> idrsservice_20200630_models.GetTaskGroupResponse:
        """
        *1**\
        
        @param request: GetTaskGroupRequest
        @return: GetTaskGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_task_group_with_options(request, runtime)

    async def get_task_group_async(
        self,
        request: idrsservice_20200630_models.GetTaskGroupRequest,
    ) -> idrsservice_20200630_models.GetTaskGroupResponse:
        """
        *1**\
        
        @param request: GetTaskGroupRequest
        @return: GetTaskGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_task_group_with_options_async(request, runtime)

    def get_tts_question_by_group_id_with_options(
        self,
        request: idrsservice_20200630_models.GetTtsQuestionByGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetTtsQuestionByGroupIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTtsQuestionByGroupId',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetTtsQuestionByGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tts_question_by_group_id_with_options_async(
        self,
        request: idrsservice_20200630_models.GetTtsQuestionByGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetTtsQuestionByGroupIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTtsQuestionByGroupId',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetTtsQuestionByGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tts_question_by_group_id(
        self,
        request: idrsservice_20200630_models.GetTtsQuestionByGroupIdRequest,
    ) -> idrsservice_20200630_models.GetTtsQuestionByGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_tts_question_by_group_id_with_options(request, runtime)

    async def get_tts_question_by_group_id_async(
        self,
        request: idrsservice_20200630_models.GetTtsQuestionByGroupIdRequest,
    ) -> idrsservice_20200630_models.GetTtsQuestionByGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_tts_question_by_group_id_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        request: idrsservice_20200630_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: idrsservice_20200630_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        request: idrsservice_20200630_models.GetUserRequest,
    ) -> idrsservice_20200630_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    async def get_user_async(
        self,
        request: idrsservice_20200630_models.GetUserRequest,
    ) -> idrsservice_20200630_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_with_options_async(request, runtime)

    def get_video_merge_task_with_options(
        self,
        request: idrsservice_20200630_models.GetVideoMergeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetVideoMergeTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVideoMergeTask',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetVideoMergeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_merge_task_with_options_async(
        self,
        request: idrsservice_20200630_models.GetVideoMergeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetVideoMergeTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVideoMergeTask',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetVideoMergeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_merge_task(
        self,
        request: idrsservice_20200630_models.GetVideoMergeTaskRequest,
    ) -> idrsservice_20200630_models.GetVideoMergeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_video_merge_task_with_options(request, runtime)

    async def get_video_merge_task_async(
        self,
        request: idrsservice_20200630_models.GetVideoMergeTaskRequest,
    ) -> idrsservice_20200630_models.GetVideoMergeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_video_merge_task_with_options_async(request, runtime)

    def get_watermark_with_options(
        self,
        request: idrsservice_20200630_models.GetWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetWatermarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.watermark_id):
            query['WatermarkId'] = request.watermark_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWatermark',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_watermark_with_options_async(
        self,
        request: idrsservice_20200630_models.GetWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetWatermarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.watermark_id):
            query['WatermarkId'] = request.watermark_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWatermark',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetWatermarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_watermark(
        self,
        request: idrsservice_20200630_models.GetWatermarkRequest,
    ) -> idrsservice_20200630_models.GetWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_watermark_with_options(request, runtime)

    async def get_watermark_async(
        self,
        request: idrsservice_20200630_models.GetWatermarkRequest,
    ) -> idrsservice_20200630_models.GetWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_watermark_with_options_async(request, runtime)

    def join_room_with_options(
        self,
        request: idrsservice_20200630_models.JoinRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.JoinRoomResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.room_token):
            query['RoomToken'] = request.room_token
        if not UtilClient.is_unset(request.stream_id):
            query['StreamId'] = request.stream_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='JoinRoom',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.JoinRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def join_room_with_options_async(
        self,
        request: idrsservice_20200630_models.JoinRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.JoinRoomResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.room_token):
            query['RoomToken'] = request.room_token
        if not UtilClient.is_unset(request.stream_id):
            query['StreamId'] = request.stream_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='JoinRoom',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.JoinRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def join_room(
        self,
        request: idrsservice_20200630_models.JoinRoomRequest,
    ) -> idrsservice_20200630_models.JoinRoomResponse:
        runtime = util_models.RuntimeOptions()
        return self.join_room_with_options(request, runtime)

    async def join_room_async(
        self,
        request: idrsservice_20200630_models.JoinRoomRequest,
    ) -> idrsservice_20200630_models.JoinRoomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.join_room_with_options_async(request, runtime)

    def leave_room_with_options(
        self,
        request: idrsservice_20200630_models.LeaveRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.LeaveRoomResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LeaveRoom',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.LeaveRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def leave_room_with_options_async(
        self,
        request: idrsservice_20200630_models.LeaveRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.LeaveRoomResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LeaveRoom',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.LeaveRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def leave_room(
        self,
        request: idrsservice_20200630_models.LeaveRoomRequest,
    ) -> idrsservice_20200630_models.LeaveRoomResponse:
        runtime = util_models.RuntimeOptions()
        return self.leave_room_with_options(request, runtime)

    async def leave_room_async(
        self,
        request: idrsservice_20200630_models.LeaveRoomRequest,
    ) -> idrsservice_20200630_models.LeaveRoomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.leave_room_with_options_async(request, runtime)

    def list_apps_with_options(
        self,
        request: idrsservice_20200630_models.ListAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApps',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_apps_with_options_async(
        self,
        request: idrsservice_20200630_models.ListAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApps',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_apps(
        self,
        request: idrsservice_20200630_models.ListAppsRequest,
    ) -> idrsservice_20200630_models.ListAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_apps_with_options(request, runtime)

    async def list_apps_async(
        self,
        request: idrsservice_20200630_models.ListAppsRequest,
    ) -> idrsservice_20200630_models.ListAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_apps_with_options_async(request, runtime)

    def list_departments_with_options(
        self,
        request: idrsservice_20200630_models.ListDepartmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListDepartmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDepartments',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListDepartmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_departments_with_options_async(
        self,
        request: idrsservice_20200630_models.ListDepartmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListDepartmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDepartments',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListDepartmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_departments(
        self,
        request: idrsservice_20200630_models.ListDepartmentsRequest,
    ) -> idrsservice_20200630_models.ListDepartmentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_departments_with_options(request, runtime)

    async def list_departments_async(
        self,
        request: idrsservice_20200630_models.ListDepartmentsRequest,
    ) -> idrsservice_20200630_models.ListDepartmentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_departments_with_options_async(request, runtime)

    def list_detect_processes_with_options(
        self,
        request: idrsservice_20200630_models.ListDetectProcessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListDetectProcessesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.publish_status):
            query['PublishStatus'] = request.publish_status
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.sort_key):
            query['SortKey'] = request.sort_key
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDetectProcesses',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListDetectProcessesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_detect_processes_with_options_async(
        self,
        request: idrsservice_20200630_models.ListDetectProcessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListDetectProcessesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.publish_status):
            query['PublishStatus'] = request.publish_status
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.sort_key):
            query['SortKey'] = request.sort_key
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDetectProcesses',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListDetectProcessesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_detect_processes(
        self,
        request: idrsservice_20200630_models.ListDetectProcessesRequest,
    ) -> idrsservice_20200630_models.ListDetectProcessesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_detect_processes_with_options(request, runtime)

    async def list_detect_processes_async(
        self,
        request: idrsservice_20200630_models.ListDetectProcessesRequest,
    ) -> idrsservice_20200630_models.ListDetectProcessesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_detect_processes_with_options_async(request, runtime)

    def list_detections_with_options(
        self,
        request: idrsservice_20200630_models.ListDetectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListDetectionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_date_from):
            query['CreateDateFrom'] = request.create_date_from
        if not UtilClient.is_unset(request.create_date_to):
            query['CreateDateTo'] = request.create_date_to
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.recording_type):
            query['RecordingType'] = request.recording_type
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDetections',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListDetectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_detections_with_options_async(
        self,
        request: idrsservice_20200630_models.ListDetectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListDetectionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_date_from):
            query['CreateDateFrom'] = request.create_date_from
        if not UtilClient.is_unset(request.create_date_to):
            query['CreateDateTo'] = request.create_date_to
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.recording_type):
            query['RecordingType'] = request.recording_type
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDetections',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListDetectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_detections(
        self,
        request: idrsservice_20200630_models.ListDetectionsRequest,
    ) -> idrsservice_20200630_models.ListDetectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_detections_with_options(request, runtime)

    async def list_detections_async(
        self,
        request: idrsservice_20200630_models.ListDetectionsRequest,
    ) -> idrsservice_20200630_models.ListDetectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_detections_with_options_async(request, runtime)

    def list_files_with_options(
        self,
        request: idrsservice_20200630_models.ListFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFiles',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_files_with_options_async(
        self,
        request: idrsservice_20200630_models.ListFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFiles',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_files(
        self,
        request: idrsservice_20200630_models.ListFilesRequest,
    ) -> idrsservice_20200630_models.ListFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_files_with_options(request, runtime)

    async def list_files_async(
        self,
        request: idrsservice_20200630_models.ListFilesRequest,
    ) -> idrsservice_20200630_models.ListFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_files_with_options_async(request, runtime)

    def list_record_results_with_options(
        self,
        request: idrsservice_20200630_models.ListRecordResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListRecordResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_date_from):
            query['CreateDateFrom'] = request.create_date_from
        if not UtilClient.is_unset(request.create_date_to):
            query['CreateDateTo'] = request.create_date_to
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.outer_business_id):
            query['OuterBusinessId'] = request.outer_business_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRecordResults',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListRecordResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_record_results_with_options_async(
        self,
        request: idrsservice_20200630_models.ListRecordResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListRecordResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_date_from):
            query['CreateDateFrom'] = request.create_date_from
        if not UtilClient.is_unset(request.create_date_to):
            query['CreateDateTo'] = request.create_date_to
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.outer_business_id):
            query['OuterBusinessId'] = request.outer_business_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRecordResults',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListRecordResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_record_results(
        self,
        request: idrsservice_20200630_models.ListRecordResultsRequest,
    ) -> idrsservice_20200630_models.ListRecordResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_record_results_with_options(request, runtime)

    async def list_record_results_async(
        self,
        request: idrsservice_20200630_models.ListRecordResultsRequest,
    ) -> idrsservice_20200630_models.ListRecordResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_record_results_with_options_async(request, runtime)

    def list_rules_with_options(
        self,
        request: idrsservice_20200630_models.ListRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRules',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rules_with_options_async(
        self,
        request: idrsservice_20200630_models.ListRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRules',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rules(
        self,
        request: idrsservice_20200630_models.ListRulesRequest,
    ) -> idrsservice_20200630_models.ListRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_rules_with_options(request, runtime)

    async def list_rules_async(
        self,
        request: idrsservice_20200630_models.ListRulesRequest,
    ) -> idrsservice_20200630_models.ListRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_rules_with_options_async(request, runtime)

    def list_task_groups_with_options(
        self,
        request: idrsservice_20200630_models.ListTaskGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListTaskGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskGroups',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListTaskGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_groups_with_options_async(
        self,
        request: idrsservice_20200630_models.ListTaskGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListTaskGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskGroups',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListTaskGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task_groups(
        self,
        request: idrsservice_20200630_models.ListTaskGroupsRequest,
    ) -> idrsservice_20200630_models.ListTaskGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_task_groups_with_options(request, runtime)

    async def list_task_groups_async(
        self,
        request: idrsservice_20200630_models.ListTaskGroupsRequest,
    ) -> idrsservice_20200630_models.ListTaskGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_task_groups_with_options_async(request, runtime)

    def list_task_items_with_options(
        self,
        request: idrsservice_20200630_models.ListTaskItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListTaskItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskItems',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListTaskItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_items_with_options_async(
        self,
        request: idrsservice_20200630_models.ListTaskItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListTaskItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskItems',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListTaskItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task_items(
        self,
        request: idrsservice_20200630_models.ListTaskItemsRequest,
    ) -> idrsservice_20200630_models.ListTaskItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_task_items_with_options(request, runtime)

    async def list_task_items_async(
        self,
        request: idrsservice_20200630_models.ListTaskItemsRequest,
    ) -> idrsservice_20200630_models.ListTaskItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_task_items_with_options_async(request, runtime)

    def list_tasks_with_options(
        self,
        request: idrsservice_20200630_models.ListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_group_id):
            query['TaskGroupId'] = request.task_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        request: idrsservice_20200630_models.ListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_group_id):
            query['TaskGroupId'] = request.task_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        request: idrsservice_20200630_models.ListTasksRequest,
    ) -> idrsservice_20200630_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tasks_with_options(request, runtime)

    async def list_tasks_async(
        self,
        request: idrsservice_20200630_models.ListTasksRequest,
    ) -> idrsservice_20200630_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tasks_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: idrsservice_20200630_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: idrsservice_20200630_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: idrsservice_20200630_models.ListUsersRequest,
    ) -> idrsservice_20200630_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: idrsservice_20200630_models.ListUsersRequest,
    ) -> idrsservice_20200630_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def list_watermarks_with_options(
        self,
        request: idrsservice_20200630_models.ListWatermarksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListWatermarksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWatermarks',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListWatermarksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_watermarks_with_options_async(
        self,
        request: idrsservice_20200630_models.ListWatermarksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListWatermarksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWatermarks',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListWatermarksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_watermarks(
        self,
        request: idrsservice_20200630_models.ListWatermarksRequest,
    ) -> idrsservice_20200630_models.ListWatermarksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_watermarks_with_options(request, runtime)

    async def list_watermarks_async(
        self,
        request: idrsservice_20200630_models.ListWatermarksRequest,
    ) -> idrsservice_20200630_models.ListWatermarksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_watermarks_with_options_async(request, runtime)

    def rename_detect_process_with_options(
        self,
        request: idrsservice_20200630_models.RenameDetectProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.RenameDetectProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenameDetectProcess',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.RenameDetectProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_detect_process_with_options_async(
        self,
        request: idrsservice_20200630_models.RenameDetectProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.RenameDetectProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenameDetectProcess',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.RenameDetectProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_detect_process(
        self,
        request: idrsservice_20200630_models.RenameDetectProcessRequest,
    ) -> idrsservice_20200630_models.RenameDetectProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.rename_detect_process_with_options(request, runtime)

    async def rename_detect_process_async(
        self,
        request: idrsservice_20200630_models.RenameDetectProcessRequest,
    ) -> idrsservice_20200630_models.RenameDetectProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rename_detect_process_with_options_async(request, runtime)

    def tts_common_with_options(
        self,
        tmp_req: idrsservice_20200630_models.TtsCommonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.TtsCommonResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.TtsCommonShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tts_request):
            request.tts_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tts_request, 'TtsRequest', 'json')
        body = {}
        if not UtilClient.is_unset(request.tts_request_shrink):
            body['TtsRequest'] = request.tts_request_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TtsCommon',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.TtsCommonResponse(),
            self.call_api(params, req, runtime)
        )

    async def tts_common_with_options_async(
        self,
        tmp_req: idrsservice_20200630_models.TtsCommonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.TtsCommonResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.TtsCommonShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tts_request):
            request.tts_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tts_request, 'TtsRequest', 'json')
        body = {}
        if not UtilClient.is_unset(request.tts_request_shrink):
            body['TtsRequest'] = request.tts_request_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TtsCommon',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.TtsCommonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tts_common(
        self,
        request: idrsservice_20200630_models.TtsCommonRequest,
    ) -> idrsservice_20200630_models.TtsCommonResponse:
        runtime = util_models.RuntimeOptions()
        return self.tts_common_with_options(request, runtime)

    async def tts_common_async(
        self,
        request: idrsservice_20200630_models.TtsCommonRequest,
    ) -> idrsservice_20200630_models.TtsCommonResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tts_common_with_options_async(request, runtime)

    def tts_task_with_options(
        self,
        tmp_req: idrsservice_20200630_models.TtsTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.TtsTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.TtsTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TtsTask',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.TtsTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def tts_task_with_options_async(
        self,
        tmp_req: idrsservice_20200630_models.TtsTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.TtsTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.TtsTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TtsTask',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.TtsTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tts_task(
        self,
        request: idrsservice_20200630_models.TtsTaskRequest,
    ) -> idrsservice_20200630_models.TtsTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.tts_task_with_options(request, runtime)

    async def tts_task_async(
        self,
        request: idrsservice_20200630_models.TtsTaskRequest,
    ) -> idrsservice_20200630_models.TtsTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tts_task_with_options_async(request, runtime)

    def update_app_with_options(
        self,
        request: idrsservice_20200630_models.UpdateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.disabled):
            query['Disabled'] = request.disabled
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.package_name):
            query['PackageName'] = request.package_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApp',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_with_options_async(
        self,
        request: idrsservice_20200630_models.UpdateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.disabled):
            query['Disabled'] = request.disabled
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.package_name):
            query['PackageName'] = request.package_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApp',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app(
        self,
        request: idrsservice_20200630_models.UpdateAppRequest,
    ) -> idrsservice_20200630_models.UpdateAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_with_options(request, runtime)

    async def update_app_async(
        self,
        request: idrsservice_20200630_models.UpdateAppRequest,
    ) -> idrsservice_20200630_models.UpdateAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_with_options_async(request, runtime)

    def update_department_with_options(
        self,
        request: idrsservice_20200630_models.UpdateDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateDepartmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDepartment',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateDepartmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_department_with_options_async(
        self,
        request: idrsservice_20200630_models.UpdateDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateDepartmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDepartment',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateDepartmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_department(
        self,
        request: idrsservice_20200630_models.UpdateDepartmentRequest,
    ) -> idrsservice_20200630_models.UpdateDepartmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_department_with_options(request, runtime)

    async def update_department_async(
        self,
        request: idrsservice_20200630_models.UpdateDepartmentRequest,
    ) -> idrsservice_20200630_models.UpdateDepartmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_department_with_options_async(request, runtime)

    def update_detect_process_with_options(
        self,
        request: idrsservice_20200630_models.UpdateDetectProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateDetectProcessResponse:
        """
        *******\
        
        @param request: UpdateDetectProcessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDetectProcessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.draft):
            query['Draft'] = request.draft
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDetectProcess',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateDetectProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_detect_process_with_options_async(
        self,
        request: idrsservice_20200630_models.UpdateDetectProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateDetectProcessResponse:
        """
        *******\
        
        @param request: UpdateDetectProcessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDetectProcessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.draft):
            query['Draft'] = request.draft
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDetectProcess',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateDetectProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_detect_process(
        self,
        request: idrsservice_20200630_models.UpdateDetectProcessRequest,
    ) -> idrsservice_20200630_models.UpdateDetectProcessResponse:
        """
        *******\
        
        @param request: UpdateDetectProcessRequest
        @return: UpdateDetectProcessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_detect_process_with_options(request, runtime)

    async def update_detect_process_async(
        self,
        request: idrsservice_20200630_models.UpdateDetectProcessRequest,
    ) -> idrsservice_20200630_models.UpdateDetectProcessResponse:
        """
        *******\
        
        @param request: UpdateDetectProcessRequest
        @return: UpdateDetectProcessResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_detect_process_with_options_async(request, runtime)

    def update_rule_with_options(
        self,
        request: idrsservice_20200630_models.UpdateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRule',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rule_with_options_async(
        self,
        request: idrsservice_20200630_models.UpdateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRule',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rule(
        self,
        request: idrsservice_20200630_models.UpdateRuleRequest,
    ) -> idrsservice_20200630_models.UpdateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_rule_with_options(request, runtime)

    async def update_rule_async(
        self,
        request: idrsservice_20200630_models.UpdateRuleRequest,
    ) -> idrsservice_20200630_models.UpdateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_rule_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: idrsservice_20200630_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: idrsservice_20200630_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user(
        self,
        request: idrsservice_20200630_models.UpdateUserRequest,
    ) -> idrsservice_20200630_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: idrsservice_20200630_models.UpdateUserRequest,
    ) -> idrsservice_20200630_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)

    def update_watermark_with_options(
        self,
        request: idrsservice_20200630_models.UpdateWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateWatermarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        if not UtilClient.is_unset(request.watermark_id):
            query['WatermarkId'] = request.watermark_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWatermark',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_watermark_with_options_async(
        self,
        request: idrsservice_20200630_models.UpdateWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateWatermarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        if not UtilClient.is_unset(request.watermark_id):
            query['WatermarkId'] = request.watermark_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWatermark',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateWatermarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_watermark(
        self,
        request: idrsservice_20200630_models.UpdateWatermarkRequest,
    ) -> idrsservice_20200630_models.UpdateWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_watermark_with_options(request, runtime)

    async def update_watermark_async(
        self,
        request: idrsservice_20200630_models.UpdateWatermarkRequest,
    ) -> idrsservice_20200630_models.UpdateWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_watermark_with_options_async(request, runtime)

    def upload_report_with_options(
        self,
        request: idrsservice_20200630_models.UploadReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UploadReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.detect_process_id):
            query['DetectProcessId'] = request.detect_process_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.fee_id):
            query['FeeId'] = request.fee_id
        if not UtilClient.is_unset(request.meta_url):
            query['MetaUrl'] = request.meta_url
        if not UtilClient.is_unset(request.outer_business_id):
            query['OuterBusinessId'] = request.outer_business_id
        if not UtilClient.is_unset(request.record_at):
            query['RecordAt'] = request.record_at
        if not UtilClient.is_unset(request.result_url):
            query['ResultUrl'] = request.result_url
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.rtc_record_id):
            query['RtcRecordId'] = request.rtc_record_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.video_type):
            query['VideoType'] = request.video_type
        if not UtilClient.is_unset(request.video_url):
            query['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadReport',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UploadReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_report_with_options_async(
        self,
        request: idrsservice_20200630_models.UploadReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UploadReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_base_param):
            query['ClientBaseParam'] = request.client_base_param
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.detect_process_id):
            query['DetectProcessId'] = request.detect_process_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.fee_id):
            query['FeeId'] = request.fee_id
        if not UtilClient.is_unset(request.meta_url):
            query['MetaUrl'] = request.meta_url
        if not UtilClient.is_unset(request.outer_business_id):
            query['OuterBusinessId'] = request.outer_business_id
        if not UtilClient.is_unset(request.record_at):
            query['RecordAt'] = request.record_at
        if not UtilClient.is_unset(request.result_url):
            query['ResultUrl'] = request.result_url
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.rtc_record_id):
            query['RtcRecordId'] = request.rtc_record_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.video_type):
            query['VideoType'] = request.video_type
        if not UtilClient.is_unset(request.video_url):
            query['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadReport',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UploadReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_report(
        self,
        request: idrsservice_20200630_models.UploadReportRequest,
    ) -> idrsservice_20200630_models.UploadReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_report_with_options(request, runtime)

    async def upload_report_async(
        self,
        request: idrsservice_20200630_models.UploadReportRequest,
    ) -> idrsservice_20200630_models.UploadReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_report_with_options_async(request, runtime)
