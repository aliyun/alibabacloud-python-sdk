# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tingwu20230930 import models as tingwu_20230930_models
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
        self._endpoint = self.get_endpoint('tingwu', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_task_with_options(
        self,
        request: tingwu_20230930_models.CreateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tingwu_20230930_models.CreateTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation):
            query['operation'] = request.operation
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.input):
            body['Input'] = request.input
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/openapi/tingwu/v2/tasks',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20230930_models.CreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_task_with_options_async(
        self,
        request: tingwu_20230930_models.CreateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tingwu_20230930_models.CreateTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation):
            query['operation'] = request.operation
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.input):
            body['Input'] = request.input
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/openapi/tingwu/v2/tasks',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20230930_models.CreateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_task(
        self,
        request: tingwu_20230930_models.CreateTaskRequest,
    ) -> tingwu_20230930_models.CreateTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_task_with_options(request, headers, runtime)

    async def create_task_async(
        self,
        request: tingwu_20230930_models.CreateTaskRequest,
    ) -> tingwu_20230930_models.CreateTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_task_with_options_async(request, headers, runtime)

    def create_transcription_phrases_with_options(
        self,
        request: tingwu_20230930_models.CreateTranscriptionPhrasesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tingwu_20230930_models.CreateTranscriptionPhrasesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.word_weights):
            body['WordWeights'] = request.word_weights
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTranscriptionPhrases',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/openapi/tingwu/v2/resources/phrases',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20230930_models.CreateTranscriptionPhrasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transcription_phrases_with_options_async(
        self,
        request: tingwu_20230930_models.CreateTranscriptionPhrasesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tingwu_20230930_models.CreateTranscriptionPhrasesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.word_weights):
            body['WordWeights'] = request.word_weights
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTranscriptionPhrases',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/openapi/tingwu/v2/resources/phrases',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20230930_models.CreateTranscriptionPhrasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transcription_phrases(
        self,
        request: tingwu_20230930_models.CreateTranscriptionPhrasesRequest,
    ) -> tingwu_20230930_models.CreateTranscriptionPhrasesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_transcription_phrases_with_options(request, headers, runtime)

    async def create_transcription_phrases_async(
        self,
        request: tingwu_20230930_models.CreateTranscriptionPhrasesRequest,
    ) -> tingwu_20230930_models.CreateTranscriptionPhrasesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_transcription_phrases_with_options_async(request, headers, runtime)

    def delete_transcription_phrases_with_options(
        self,
        phrase_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tingwu_20230930_models.DeleteTranscriptionPhrasesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTranscriptionPhrases',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/openapi/tingwu/v2/resources/phrases/{OpenApiUtilClient.get_encode_param(phrase_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20230930_models.DeleteTranscriptionPhrasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transcription_phrases_with_options_async(
        self,
        phrase_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tingwu_20230930_models.DeleteTranscriptionPhrasesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTranscriptionPhrases',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/openapi/tingwu/v2/resources/phrases/{OpenApiUtilClient.get_encode_param(phrase_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20230930_models.DeleteTranscriptionPhrasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transcription_phrases(
        self,
        phrase_id: str,
    ) -> tingwu_20230930_models.DeleteTranscriptionPhrasesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_transcription_phrases_with_options(phrase_id, headers, runtime)

    async def delete_transcription_phrases_async(
        self,
        phrase_id: str,
    ) -> tingwu_20230930_models.DeleteTranscriptionPhrasesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_transcription_phrases_with_options_async(phrase_id, headers, runtime)

    def get_task_info_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tingwu_20230930_models.GetTaskInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskInfo',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/openapi/tingwu/v2/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20230930_models.GetTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_info_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tingwu_20230930_models.GetTaskInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskInfo',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/openapi/tingwu/v2/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20230930_models.GetTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_info(
        self,
        task_id: str,
    ) -> tingwu_20230930_models.GetTaskInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_info_with_options(task_id, headers, runtime)

    async def get_task_info_async(
        self,
        task_id: str,
    ) -> tingwu_20230930_models.GetTaskInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_info_with_options_async(task_id, headers, runtime)

    def get_transcription_phrases_with_options(
        self,
        phrase_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tingwu_20230930_models.GetTranscriptionPhrasesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTranscriptionPhrases',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/openapi/tingwu/v2/resources/phrases/{OpenApiUtilClient.get_encode_param(phrase_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20230930_models.GetTranscriptionPhrasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_transcription_phrases_with_options_async(
        self,
        phrase_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tingwu_20230930_models.GetTranscriptionPhrasesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTranscriptionPhrases',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/openapi/tingwu/v2/resources/phrases/{OpenApiUtilClient.get_encode_param(phrase_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20230930_models.GetTranscriptionPhrasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_transcription_phrases(
        self,
        phrase_id: str,
    ) -> tingwu_20230930_models.GetTranscriptionPhrasesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_transcription_phrases_with_options(phrase_id, headers, runtime)

    async def get_transcription_phrases_async(
        self,
        phrase_id: str,
    ) -> tingwu_20230930_models.GetTranscriptionPhrasesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_transcription_phrases_with_options_async(phrase_id, headers, runtime)

    def list_transcription_phrases_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tingwu_20230930_models.ListTranscriptionPhrasesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListTranscriptionPhrases',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/openapi/tingwu/v2/resources/phrases',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20230930_models.ListTranscriptionPhrasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transcription_phrases_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tingwu_20230930_models.ListTranscriptionPhrasesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListTranscriptionPhrases',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/openapi/tingwu/v2/resources/phrases',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20230930_models.ListTranscriptionPhrasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transcription_phrases(self) -> tingwu_20230930_models.ListTranscriptionPhrasesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_transcription_phrases_with_options(headers, runtime)

    async def list_transcription_phrases_async(self) -> tingwu_20230930_models.ListTranscriptionPhrasesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_transcription_phrases_with_options_async(headers, runtime)

    def update_transcription_phrases_with_options(
        self,
        phrase_id: str,
        request: tingwu_20230930_models.UpdateTranscriptionPhrasesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tingwu_20230930_models.UpdateTranscriptionPhrasesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.word_weights):
            body['WordWeights'] = request.word_weights
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTranscriptionPhrases',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/openapi/tingwu/v2/resources/phrases/{OpenApiUtilClient.get_encode_param(phrase_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20230930_models.UpdateTranscriptionPhrasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_transcription_phrases_with_options_async(
        self,
        phrase_id: str,
        request: tingwu_20230930_models.UpdateTranscriptionPhrasesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tingwu_20230930_models.UpdateTranscriptionPhrasesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.word_weights):
            body['WordWeights'] = request.word_weights
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTranscriptionPhrases',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/openapi/tingwu/v2/resources/phrases/{OpenApiUtilClient.get_encode_param(phrase_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20230930_models.UpdateTranscriptionPhrasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_transcription_phrases(
        self,
        phrase_id: str,
        request: tingwu_20230930_models.UpdateTranscriptionPhrasesRequest,
    ) -> tingwu_20230930_models.UpdateTranscriptionPhrasesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_transcription_phrases_with_options(phrase_id, request, headers, runtime)

    async def update_transcription_phrases_async(
        self,
        phrase_id: str,
        request: tingwu_20230930_models.UpdateTranscriptionPhrasesRequest,
    ) -> tingwu_20230930_models.UpdateTranscriptionPhrasesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_transcription_phrases_with_options_async(phrase_id, request, headers, runtime)
