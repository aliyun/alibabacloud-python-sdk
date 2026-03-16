# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_tingwu20230930 import models as main_models
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_task_with_options(
        self,
        request: main_models.CreateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.operation):
            query['operation'] = request.operation
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.input):
            body['Input'] = request.input
        if not DaraCore.is_null(request.parameters):
            body['Parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTask',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/openapi/tingwu/v2/tasks',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_task_with_options_async(
        self,
        request: main_models.CreateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.operation):
            query['operation'] = request.operation
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.input):
            body['Input'] = request.input
        if not DaraCore.is_null(request.parameters):
            body['Parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTask',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/openapi/tingwu/v2/tasks',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.create_task_with_options(request, headers, runtime)

    async def create_task_async(
        self,
        request: main_models.CreateTaskRequest,
    ) -> main_models.CreateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_task_with_options_async(request, headers, runtime)

    def create_transcription_phrases_with_options(
        self,
        request: main_models.CreateTranscriptionPhrasesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTranscriptionPhrasesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.word_weights):
            body['WordWeights'] = request.word_weights
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTranscriptionPhrases',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/openapi/tingwu/v2/resources/phrases',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTranscriptionPhrasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transcription_phrases_with_options_async(
        self,
        request: main_models.CreateTranscriptionPhrasesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTranscriptionPhrasesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.word_weights):
            body['WordWeights'] = request.word_weights
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTranscriptionPhrases',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/openapi/tingwu/v2/resources/phrases',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTranscriptionPhrasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transcription_phrases(
        self,
        request: main_models.CreateTranscriptionPhrasesRequest,
    ) -> main_models.CreateTranscriptionPhrasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_transcription_phrases_with_options(request, headers, runtime)

    async def create_transcription_phrases_async(
        self,
        request: main_models.CreateTranscriptionPhrasesRequest,
    ) -> main_models.CreateTranscriptionPhrasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_transcription_phrases_with_options_async(request, headers, runtime)

    def delete_transcription_phrases_with_options(
        self,
        phrase_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTranscriptionPhrasesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTranscriptionPhrases',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/openapi/tingwu/v2/resources/phrases/{DaraURL.percent_encode(phrase_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTranscriptionPhrasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transcription_phrases_with_options_async(
        self,
        phrase_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTranscriptionPhrasesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTranscriptionPhrases',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/openapi/tingwu/v2/resources/phrases/{DaraURL.percent_encode(phrase_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTranscriptionPhrasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transcription_phrases(
        self,
        phrase_id: str,
    ) -> main_models.DeleteTranscriptionPhrasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_transcription_phrases_with_options(phrase_id, headers, runtime)

    async def delete_transcription_phrases_async(
        self,
        phrase_id: str,
    ) -> main_models.DeleteTranscriptionPhrasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_transcription_phrases_with_options_async(phrase_id, headers, runtime)

    def get_task_info_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskInfoResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTaskInfo',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/openapi/tingwu/v2/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_info_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskInfoResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTaskInfo',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/openapi/tingwu/v2/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_info(
        self,
        task_id: str,
    ) -> main_models.GetTaskInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_task_info_with_options(task_id, headers, runtime)

    async def get_task_info_async(
        self,
        task_id: str,
    ) -> main_models.GetTaskInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_task_info_with_options_async(task_id, headers, runtime)

    def get_transcription_phrases_with_options(
        self,
        phrase_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTranscriptionPhrasesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTranscriptionPhrases',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/openapi/tingwu/v2/resources/phrases/{DaraURL.percent_encode(phrase_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTranscriptionPhrasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_transcription_phrases_with_options_async(
        self,
        phrase_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTranscriptionPhrasesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTranscriptionPhrases',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/openapi/tingwu/v2/resources/phrases/{DaraURL.percent_encode(phrase_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTranscriptionPhrasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_transcription_phrases(
        self,
        phrase_id: str,
    ) -> main_models.GetTranscriptionPhrasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_transcription_phrases_with_options(phrase_id, headers, runtime)

    async def get_transcription_phrases_async(
        self,
        phrase_id: str,
    ) -> main_models.GetTranscriptionPhrasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_transcription_phrases_with_options_async(phrase_id, headers, runtime)

    def list_transcription_phrases_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTranscriptionPhrasesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListTranscriptionPhrases',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/openapi/tingwu/v2/resources/phrases',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTranscriptionPhrasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transcription_phrases_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTranscriptionPhrasesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListTranscriptionPhrases',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/openapi/tingwu/v2/resources/phrases',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTranscriptionPhrasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transcription_phrases(self) -> main_models.ListTranscriptionPhrasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_transcription_phrases_with_options(headers, runtime)

    async def list_transcription_phrases_async(self) -> main_models.ListTranscriptionPhrasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_transcription_phrases_with_options_async(headers, runtime)

    def update_transcription_phrases_with_options(
        self,
        phrase_id: str,
        request: main_models.UpdateTranscriptionPhrasesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTranscriptionPhrasesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.word_weights):
            body['WordWeights'] = request.word_weights
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTranscriptionPhrases',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/openapi/tingwu/v2/resources/phrases/{DaraURL.percent_encode(phrase_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTranscriptionPhrasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_transcription_phrases_with_options_async(
        self,
        phrase_id: str,
        request: main_models.UpdateTranscriptionPhrasesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTranscriptionPhrasesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.word_weights):
            body['WordWeights'] = request.word_weights
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTranscriptionPhrases',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/openapi/tingwu/v2/resources/phrases/{DaraURL.percent_encode(phrase_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTranscriptionPhrasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_transcription_phrases(
        self,
        phrase_id: str,
        request: main_models.UpdateTranscriptionPhrasesRequest,
    ) -> main_models.UpdateTranscriptionPhrasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_transcription_phrases_with_options(phrase_id, request, headers, runtime)

    async def update_transcription_phrases_async(
        self,
        phrase_id: str,
        request: main_models.UpdateTranscriptionPhrasesRequest,
    ) -> main_models.UpdateTranscriptionPhrasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_transcription_phrases_with_options_async(phrase_id, request, headers, runtime)
