# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_maasqiservice20260831 import models as main_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('maasqiservice', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def aigc_chat_completion_stream_with_sse(
        self,
        request: main_models.AigcChatCompletionStreamRequest,
        headers: main_models.AigcChatCompletionStreamHeaders,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.AigcChatCompletionStreamResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.metadata):
            body['metadata'] = request.metadata
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.stream_options):
            body['streamOptions'] = request.stream_options
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_qiagent_api_key):
            real_headers['X-QI-Agent-Api-Key'] = str(headers.x_qiagent_api_key)
        if not DaraCore.is_null(headers.x_qiinstance_id):
            real_headers['X-QI-Instance-Id'] = str(headers.x_qiinstance_id)
        if not DaraCore.is_null(headers.x_qisession_id):
            real_headers['X-QI-Session-Id'] = str(headers.x_qisession_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AigcChatCompletionStream',
            version = '2026-08-31',
            protocol = 'HTTPS',
            pathname = f'/aigc/v1/chat/completions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.AigcChatCompletionStreamResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def aigc_chat_completion_stream_with_sse_async(
        self,
        request: main_models.AigcChatCompletionStreamRequest,
        headers: main_models.AigcChatCompletionStreamHeaders,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.AigcChatCompletionStreamResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.metadata):
            body['metadata'] = request.metadata
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.stream_options):
            body['streamOptions'] = request.stream_options
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_qiagent_api_key):
            real_headers['X-QI-Agent-Api-Key'] = str(headers.x_qiagent_api_key)
        if not DaraCore.is_null(headers.x_qiinstance_id):
            real_headers['X-QI-Instance-Id'] = str(headers.x_qiinstance_id)
        if not DaraCore.is_null(headers.x_qisession_id):
            real_headers['X-QI-Session-Id'] = str(headers.x_qisession_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AigcChatCompletionStream',
            version = '2026-08-31',
            protocol = 'HTTPS',
            pathname = f'/aigc/v1/chat/completions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.AigcChatCompletionStreamResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def aigc_chat_completion_stream_with_options(
        self,
        request: main_models.AigcChatCompletionStreamRequest,
        headers: main_models.AigcChatCompletionStreamHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AigcChatCompletionStreamResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.metadata):
            body['metadata'] = request.metadata
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.stream_options):
            body['streamOptions'] = request.stream_options
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_qiagent_api_key):
            real_headers['X-QI-Agent-Api-Key'] = str(headers.x_qiagent_api_key)
        if not DaraCore.is_null(headers.x_qiinstance_id):
            real_headers['X-QI-Instance-Id'] = str(headers.x_qiinstance_id)
        if not DaraCore.is_null(headers.x_qisession_id):
            real_headers['X-QI-Session-Id'] = str(headers.x_qisession_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AigcChatCompletionStream',
            version = '2026-08-31',
            protocol = 'HTTPS',
            pathname = f'/aigc/v1/chat/completions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AigcChatCompletionStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def aigc_chat_completion_stream_with_options_async(
        self,
        request: main_models.AigcChatCompletionStreamRequest,
        headers: main_models.AigcChatCompletionStreamHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AigcChatCompletionStreamResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.metadata):
            body['metadata'] = request.metadata
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.stream_options):
            body['streamOptions'] = request.stream_options
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_qiagent_api_key):
            real_headers['X-QI-Agent-Api-Key'] = str(headers.x_qiagent_api_key)
        if not DaraCore.is_null(headers.x_qiinstance_id):
            real_headers['X-QI-Instance-Id'] = str(headers.x_qiinstance_id)
        if not DaraCore.is_null(headers.x_qisession_id):
            real_headers['X-QI-Session-Id'] = str(headers.x_qisession_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AigcChatCompletionStream',
            version = '2026-08-31',
            protocol = 'HTTPS',
            pathname = f'/aigc/v1/chat/completions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AigcChatCompletionStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def aigc_chat_completion_stream(
        self,
        request: main_models.AigcChatCompletionStreamRequest,
    ) -> main_models.AigcChatCompletionStreamResponse:
        runtime = RuntimeOptions()
        headers = main_models.AigcChatCompletionStreamHeaders()
        return self.aigc_chat_completion_stream_with_options(request, headers, runtime)

    async def aigc_chat_completion_stream_async(
        self,
        request: main_models.AigcChatCompletionStreamRequest,
    ) -> main_models.AigcChatCompletionStreamResponse:
        runtime = RuntimeOptions()
        headers = main_models.AigcChatCompletionStreamHeaders()
        return await self.aigc_chat_completion_stream_with_options_async(request, headers, runtime)

    def gui_chat_completion_stream_with_sse(
        self,
        request: main_models.GuiChatCompletionStreamRequest,
        headers: main_models.GuiChatCompletionStreamHeaders,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.GuiChatCompletionStreamResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.allowed_token_ids):
            body['allowedTokenIds'] = request.allowed_token_ids
        if not DaraCore.is_null(request.bad_words):
            body['badWords'] = request.bad_words
        if not DaraCore.is_null(request.chat_template_kwargs):
            body['chatTemplateKwargs'] = request.chat_template_kwargs
        if not DaraCore.is_null(request.frequency_penalty):
            body['frequencyPenalty'] = request.frequency_penalty
        if not DaraCore.is_null(request.ignore_eos):
            body['ignoreEos'] = request.ignore_eos
        if not DaraCore.is_null(request.include_reasoning):
            body['includeReasoning'] = request.include_reasoning
        if not DaraCore.is_null(request.logprobs):
            body['logprobs'] = request.logprobs
        if not DaraCore.is_null(request.max_completion_tokens):
            body['maxCompletionTokens'] = request.max_completion_tokens
        if not DaraCore.is_null(request.max_tokens):
            body['maxTokens'] = request.max_tokens
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.metadata):
            body['metadata'] = request.metadata
        if not DaraCore.is_null(request.min_p):
            body['minP'] = request.min_p
        if not DaraCore.is_null(request.min_tokens):
            body['minTokens'] = request.min_tokens
        if not DaraCore.is_null(request.mm_processor_kwargs):
            body['mmProcessorKwargs'] = request.mm_processor_kwargs
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.n):
            body['n'] = request.n
        if not DaraCore.is_null(request.parallel_tool_calls):
            body['parallelToolCalls'] = request.parallel_tool_calls
        if not DaraCore.is_null(request.presence_penalty):
            body['presencePenalty'] = request.presence_penalty
        if not DaraCore.is_null(request.prompt_logprobs):
            body['promptLogprobs'] = request.prompt_logprobs
        if not DaraCore.is_null(request.reasoning_effort):
            body['reasoningEffort'] = request.reasoning_effort
        if not DaraCore.is_null(request.repetition_penalty):
            body['repetitionPenalty'] = request.repetition_penalty
        if not DaraCore.is_null(request.response_format):
            body['responseFormat'] = request.response_format
        if not DaraCore.is_null(request.seed):
            body['seed'] = request.seed
        if not DaraCore.is_null(request.skip_special_tokens):
            body['skipSpecialTokens'] = request.skip_special_tokens
        if not DaraCore.is_null(request.stop):
            body['stop'] = request.stop
        if not DaraCore.is_null(request.stop_token_ids):
            body['stopTokenIds'] = request.stop_token_ids
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.stream_options):
            body['streamOptions'] = request.stream_options
        if not DaraCore.is_null(request.structured_outputs):
            body['structuredOutputs'] = request.structured_outputs
        if not DaraCore.is_null(request.temperature):
            body['temperature'] = request.temperature
        if not DaraCore.is_null(request.top_k):
            body['topK'] = request.top_k
        if not DaraCore.is_null(request.top_logprobs):
            body['topLogprobs'] = request.top_logprobs
        if not DaraCore.is_null(request.top_p):
            body['topP'] = request.top_p
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_qiagent_api_key):
            real_headers['X-QI-Agent-Api-Key'] = str(headers.x_qiagent_api_key)
        if not DaraCore.is_null(headers.x_qiinstance_id):
            real_headers['X-QI-Instance-Id'] = str(headers.x_qiinstance_id)
        if not DaraCore.is_null(headers.x_qisession_id):
            real_headers['X-QI-Session-Id'] = str(headers.x_qisession_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GuiChatCompletionStream',
            version = '2026-08-31',
            protocol = 'HTTPS',
            pathname = f'/gui/v1/chat/completions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.GuiChatCompletionStreamResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def gui_chat_completion_stream_with_sse_async(
        self,
        request: main_models.GuiChatCompletionStreamRequest,
        headers: main_models.GuiChatCompletionStreamHeaders,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.GuiChatCompletionStreamResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.allowed_token_ids):
            body['allowedTokenIds'] = request.allowed_token_ids
        if not DaraCore.is_null(request.bad_words):
            body['badWords'] = request.bad_words
        if not DaraCore.is_null(request.chat_template_kwargs):
            body['chatTemplateKwargs'] = request.chat_template_kwargs
        if not DaraCore.is_null(request.frequency_penalty):
            body['frequencyPenalty'] = request.frequency_penalty
        if not DaraCore.is_null(request.ignore_eos):
            body['ignoreEos'] = request.ignore_eos
        if not DaraCore.is_null(request.include_reasoning):
            body['includeReasoning'] = request.include_reasoning
        if not DaraCore.is_null(request.logprobs):
            body['logprobs'] = request.logprobs
        if not DaraCore.is_null(request.max_completion_tokens):
            body['maxCompletionTokens'] = request.max_completion_tokens
        if not DaraCore.is_null(request.max_tokens):
            body['maxTokens'] = request.max_tokens
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.metadata):
            body['metadata'] = request.metadata
        if not DaraCore.is_null(request.min_p):
            body['minP'] = request.min_p
        if not DaraCore.is_null(request.min_tokens):
            body['minTokens'] = request.min_tokens
        if not DaraCore.is_null(request.mm_processor_kwargs):
            body['mmProcessorKwargs'] = request.mm_processor_kwargs
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.n):
            body['n'] = request.n
        if not DaraCore.is_null(request.parallel_tool_calls):
            body['parallelToolCalls'] = request.parallel_tool_calls
        if not DaraCore.is_null(request.presence_penalty):
            body['presencePenalty'] = request.presence_penalty
        if not DaraCore.is_null(request.prompt_logprobs):
            body['promptLogprobs'] = request.prompt_logprobs
        if not DaraCore.is_null(request.reasoning_effort):
            body['reasoningEffort'] = request.reasoning_effort
        if not DaraCore.is_null(request.repetition_penalty):
            body['repetitionPenalty'] = request.repetition_penalty
        if not DaraCore.is_null(request.response_format):
            body['responseFormat'] = request.response_format
        if not DaraCore.is_null(request.seed):
            body['seed'] = request.seed
        if not DaraCore.is_null(request.skip_special_tokens):
            body['skipSpecialTokens'] = request.skip_special_tokens
        if not DaraCore.is_null(request.stop):
            body['stop'] = request.stop
        if not DaraCore.is_null(request.stop_token_ids):
            body['stopTokenIds'] = request.stop_token_ids
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.stream_options):
            body['streamOptions'] = request.stream_options
        if not DaraCore.is_null(request.structured_outputs):
            body['structuredOutputs'] = request.structured_outputs
        if not DaraCore.is_null(request.temperature):
            body['temperature'] = request.temperature
        if not DaraCore.is_null(request.top_k):
            body['topK'] = request.top_k
        if not DaraCore.is_null(request.top_logprobs):
            body['topLogprobs'] = request.top_logprobs
        if not DaraCore.is_null(request.top_p):
            body['topP'] = request.top_p
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_qiagent_api_key):
            real_headers['X-QI-Agent-Api-Key'] = str(headers.x_qiagent_api_key)
        if not DaraCore.is_null(headers.x_qiinstance_id):
            real_headers['X-QI-Instance-Id'] = str(headers.x_qiinstance_id)
        if not DaraCore.is_null(headers.x_qisession_id):
            real_headers['X-QI-Session-Id'] = str(headers.x_qisession_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GuiChatCompletionStream',
            version = '2026-08-31',
            protocol = 'HTTPS',
            pathname = f'/gui/v1/chat/completions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.GuiChatCompletionStreamResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def gui_chat_completion_stream_with_options(
        self,
        request: main_models.GuiChatCompletionStreamRequest,
        headers: main_models.GuiChatCompletionStreamHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GuiChatCompletionStreamResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.allowed_token_ids):
            body['allowedTokenIds'] = request.allowed_token_ids
        if not DaraCore.is_null(request.bad_words):
            body['badWords'] = request.bad_words
        if not DaraCore.is_null(request.chat_template_kwargs):
            body['chatTemplateKwargs'] = request.chat_template_kwargs
        if not DaraCore.is_null(request.frequency_penalty):
            body['frequencyPenalty'] = request.frequency_penalty
        if not DaraCore.is_null(request.ignore_eos):
            body['ignoreEos'] = request.ignore_eos
        if not DaraCore.is_null(request.include_reasoning):
            body['includeReasoning'] = request.include_reasoning
        if not DaraCore.is_null(request.logprobs):
            body['logprobs'] = request.logprobs
        if not DaraCore.is_null(request.max_completion_tokens):
            body['maxCompletionTokens'] = request.max_completion_tokens
        if not DaraCore.is_null(request.max_tokens):
            body['maxTokens'] = request.max_tokens
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.metadata):
            body['metadata'] = request.metadata
        if not DaraCore.is_null(request.min_p):
            body['minP'] = request.min_p
        if not DaraCore.is_null(request.min_tokens):
            body['minTokens'] = request.min_tokens
        if not DaraCore.is_null(request.mm_processor_kwargs):
            body['mmProcessorKwargs'] = request.mm_processor_kwargs
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.n):
            body['n'] = request.n
        if not DaraCore.is_null(request.parallel_tool_calls):
            body['parallelToolCalls'] = request.parallel_tool_calls
        if not DaraCore.is_null(request.presence_penalty):
            body['presencePenalty'] = request.presence_penalty
        if not DaraCore.is_null(request.prompt_logprobs):
            body['promptLogprobs'] = request.prompt_logprobs
        if not DaraCore.is_null(request.reasoning_effort):
            body['reasoningEffort'] = request.reasoning_effort
        if not DaraCore.is_null(request.repetition_penalty):
            body['repetitionPenalty'] = request.repetition_penalty
        if not DaraCore.is_null(request.response_format):
            body['responseFormat'] = request.response_format
        if not DaraCore.is_null(request.seed):
            body['seed'] = request.seed
        if not DaraCore.is_null(request.skip_special_tokens):
            body['skipSpecialTokens'] = request.skip_special_tokens
        if not DaraCore.is_null(request.stop):
            body['stop'] = request.stop
        if not DaraCore.is_null(request.stop_token_ids):
            body['stopTokenIds'] = request.stop_token_ids
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.stream_options):
            body['streamOptions'] = request.stream_options
        if not DaraCore.is_null(request.structured_outputs):
            body['structuredOutputs'] = request.structured_outputs
        if not DaraCore.is_null(request.temperature):
            body['temperature'] = request.temperature
        if not DaraCore.is_null(request.top_k):
            body['topK'] = request.top_k
        if not DaraCore.is_null(request.top_logprobs):
            body['topLogprobs'] = request.top_logprobs
        if not DaraCore.is_null(request.top_p):
            body['topP'] = request.top_p
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_qiagent_api_key):
            real_headers['X-QI-Agent-Api-Key'] = str(headers.x_qiagent_api_key)
        if not DaraCore.is_null(headers.x_qiinstance_id):
            real_headers['X-QI-Instance-Id'] = str(headers.x_qiinstance_id)
        if not DaraCore.is_null(headers.x_qisession_id):
            real_headers['X-QI-Session-Id'] = str(headers.x_qisession_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GuiChatCompletionStream',
            version = '2026-08-31',
            protocol = 'HTTPS',
            pathname = f'/gui/v1/chat/completions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GuiChatCompletionStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def gui_chat_completion_stream_with_options_async(
        self,
        request: main_models.GuiChatCompletionStreamRequest,
        headers: main_models.GuiChatCompletionStreamHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GuiChatCompletionStreamResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.allowed_token_ids):
            body['allowedTokenIds'] = request.allowed_token_ids
        if not DaraCore.is_null(request.bad_words):
            body['badWords'] = request.bad_words
        if not DaraCore.is_null(request.chat_template_kwargs):
            body['chatTemplateKwargs'] = request.chat_template_kwargs
        if not DaraCore.is_null(request.frequency_penalty):
            body['frequencyPenalty'] = request.frequency_penalty
        if not DaraCore.is_null(request.ignore_eos):
            body['ignoreEos'] = request.ignore_eos
        if not DaraCore.is_null(request.include_reasoning):
            body['includeReasoning'] = request.include_reasoning
        if not DaraCore.is_null(request.logprobs):
            body['logprobs'] = request.logprobs
        if not DaraCore.is_null(request.max_completion_tokens):
            body['maxCompletionTokens'] = request.max_completion_tokens
        if not DaraCore.is_null(request.max_tokens):
            body['maxTokens'] = request.max_tokens
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.metadata):
            body['metadata'] = request.metadata
        if not DaraCore.is_null(request.min_p):
            body['minP'] = request.min_p
        if not DaraCore.is_null(request.min_tokens):
            body['minTokens'] = request.min_tokens
        if not DaraCore.is_null(request.mm_processor_kwargs):
            body['mmProcessorKwargs'] = request.mm_processor_kwargs
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.n):
            body['n'] = request.n
        if not DaraCore.is_null(request.parallel_tool_calls):
            body['parallelToolCalls'] = request.parallel_tool_calls
        if not DaraCore.is_null(request.presence_penalty):
            body['presencePenalty'] = request.presence_penalty
        if not DaraCore.is_null(request.prompt_logprobs):
            body['promptLogprobs'] = request.prompt_logprobs
        if not DaraCore.is_null(request.reasoning_effort):
            body['reasoningEffort'] = request.reasoning_effort
        if not DaraCore.is_null(request.repetition_penalty):
            body['repetitionPenalty'] = request.repetition_penalty
        if not DaraCore.is_null(request.response_format):
            body['responseFormat'] = request.response_format
        if not DaraCore.is_null(request.seed):
            body['seed'] = request.seed
        if not DaraCore.is_null(request.skip_special_tokens):
            body['skipSpecialTokens'] = request.skip_special_tokens
        if not DaraCore.is_null(request.stop):
            body['stop'] = request.stop
        if not DaraCore.is_null(request.stop_token_ids):
            body['stopTokenIds'] = request.stop_token_ids
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.stream_options):
            body['streamOptions'] = request.stream_options
        if not DaraCore.is_null(request.structured_outputs):
            body['structuredOutputs'] = request.structured_outputs
        if not DaraCore.is_null(request.temperature):
            body['temperature'] = request.temperature
        if not DaraCore.is_null(request.top_k):
            body['topK'] = request.top_k
        if not DaraCore.is_null(request.top_logprobs):
            body['topLogprobs'] = request.top_logprobs
        if not DaraCore.is_null(request.top_p):
            body['topP'] = request.top_p
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_qiagent_api_key):
            real_headers['X-QI-Agent-Api-Key'] = str(headers.x_qiagent_api_key)
        if not DaraCore.is_null(headers.x_qiinstance_id):
            real_headers['X-QI-Instance-Id'] = str(headers.x_qiinstance_id)
        if not DaraCore.is_null(headers.x_qisession_id):
            real_headers['X-QI-Session-Id'] = str(headers.x_qisession_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GuiChatCompletionStream',
            version = '2026-08-31',
            protocol = 'HTTPS',
            pathname = f'/gui/v1/chat/completions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GuiChatCompletionStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def gui_chat_completion_stream(
        self,
        request: main_models.GuiChatCompletionStreamRequest,
    ) -> main_models.GuiChatCompletionStreamResponse:
        runtime = RuntimeOptions()
        headers = main_models.GuiChatCompletionStreamHeaders()
        return self.gui_chat_completion_stream_with_options(request, headers, runtime)

    async def gui_chat_completion_stream_async(
        self,
        request: main_models.GuiChatCompletionStreamRequest,
    ) -> main_models.GuiChatCompletionStreamResponse:
        runtime = RuntimeOptions()
        headers = main_models.GuiChatCompletionStreamHeaders()
        return await self.gui_chat_completion_stream_with_options_async(request, headers, runtime)

    def pa_chat_completion_stream_with_sse(
        self,
        request: main_models.PaChatCompletionStreamRequest,
        headers: main_models.PaChatCompletionStreamHeaders,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.PaChatCompletionStreamResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.allowed_token_ids):
            body['allowedTokenIds'] = request.allowed_token_ids
        if not DaraCore.is_null(request.bad_words):
            body['badWords'] = request.bad_words
        if not DaraCore.is_null(request.chat_template_kwargs):
            body['chatTemplateKwargs'] = request.chat_template_kwargs
        if not DaraCore.is_null(request.frequency_penalty):
            body['frequencyPenalty'] = request.frequency_penalty
        if not DaraCore.is_null(request.ignore_eos):
            body['ignoreEos'] = request.ignore_eos
        if not DaraCore.is_null(request.include_reasoning):
            body['includeReasoning'] = request.include_reasoning
        if not DaraCore.is_null(request.logprobs):
            body['logprobs'] = request.logprobs
        if not DaraCore.is_null(request.max_completion_tokens):
            body['maxCompletionTokens'] = request.max_completion_tokens
        if not DaraCore.is_null(request.max_tokens):
            body['maxTokens'] = request.max_tokens
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.min_p):
            body['minP'] = request.min_p
        if not DaraCore.is_null(request.min_tokens):
            body['minTokens'] = request.min_tokens
        if not DaraCore.is_null(request.mm_processor_kwargs):
            body['mmProcessorKwargs'] = request.mm_processor_kwargs
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.n):
            body['n'] = request.n
        if not DaraCore.is_null(request.parallel_tool_calls):
            body['parallelToolCalls'] = request.parallel_tool_calls
        if not DaraCore.is_null(request.presence_penalty):
            body['presencePenalty'] = request.presence_penalty
        if not DaraCore.is_null(request.prompt_logprobs):
            body['promptLogprobs'] = request.prompt_logprobs
        if not DaraCore.is_null(request.reasoning_effort):
            body['reasoningEffort'] = request.reasoning_effort
        if not DaraCore.is_null(request.repetition_penalty):
            body['repetitionPenalty'] = request.repetition_penalty
        if not DaraCore.is_null(request.response_format):
            body['responseFormat'] = request.response_format
        if not DaraCore.is_null(request.seed):
            body['seed'] = request.seed
        if not DaraCore.is_null(request.skip_special_tokens):
            body['skipSpecialTokens'] = request.skip_special_tokens
        if not DaraCore.is_null(request.stop):
            body['stop'] = request.stop
        if not DaraCore.is_null(request.stop_token_ids):
            body['stopTokenIds'] = request.stop_token_ids
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.stream_options):
            body['streamOptions'] = request.stream_options
        if not DaraCore.is_null(request.structured_outputs):
            body['structuredOutputs'] = request.structured_outputs
        if not DaraCore.is_null(request.temperature):
            body['temperature'] = request.temperature
        if not DaraCore.is_null(request.tool_choice):
            body['toolChoice'] = request.tool_choice
        if not DaraCore.is_null(request.tools):
            body['tools'] = request.tools
        if not DaraCore.is_null(request.top_k):
            body['topK'] = request.top_k
        if not DaraCore.is_null(request.top_logprobs):
            body['topLogprobs'] = request.top_logprobs
        if not DaraCore.is_null(request.top_p):
            body['topP'] = request.top_p
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_qiagent_api_key):
            real_headers['X-QI-Agent-Api-Key'] = str(headers.x_qiagent_api_key)
        if not DaraCore.is_null(headers.x_qiinstance_id):
            real_headers['X-QI-Instance-Id'] = str(headers.x_qiinstance_id)
        if not DaraCore.is_null(headers.x_qisession_id):
            real_headers['X-QI-Session-Id'] = str(headers.x_qisession_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PaChatCompletionStream',
            version = '2026-08-31',
            protocol = 'HTTPS',
            pathname = f'/pa/v1/chat/completions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.PaChatCompletionStreamResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def pa_chat_completion_stream_with_sse_async(
        self,
        request: main_models.PaChatCompletionStreamRequest,
        headers: main_models.PaChatCompletionStreamHeaders,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.PaChatCompletionStreamResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.allowed_token_ids):
            body['allowedTokenIds'] = request.allowed_token_ids
        if not DaraCore.is_null(request.bad_words):
            body['badWords'] = request.bad_words
        if not DaraCore.is_null(request.chat_template_kwargs):
            body['chatTemplateKwargs'] = request.chat_template_kwargs
        if not DaraCore.is_null(request.frequency_penalty):
            body['frequencyPenalty'] = request.frequency_penalty
        if not DaraCore.is_null(request.ignore_eos):
            body['ignoreEos'] = request.ignore_eos
        if not DaraCore.is_null(request.include_reasoning):
            body['includeReasoning'] = request.include_reasoning
        if not DaraCore.is_null(request.logprobs):
            body['logprobs'] = request.logprobs
        if not DaraCore.is_null(request.max_completion_tokens):
            body['maxCompletionTokens'] = request.max_completion_tokens
        if not DaraCore.is_null(request.max_tokens):
            body['maxTokens'] = request.max_tokens
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.min_p):
            body['minP'] = request.min_p
        if not DaraCore.is_null(request.min_tokens):
            body['minTokens'] = request.min_tokens
        if not DaraCore.is_null(request.mm_processor_kwargs):
            body['mmProcessorKwargs'] = request.mm_processor_kwargs
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.n):
            body['n'] = request.n
        if not DaraCore.is_null(request.parallel_tool_calls):
            body['parallelToolCalls'] = request.parallel_tool_calls
        if not DaraCore.is_null(request.presence_penalty):
            body['presencePenalty'] = request.presence_penalty
        if not DaraCore.is_null(request.prompt_logprobs):
            body['promptLogprobs'] = request.prompt_logprobs
        if not DaraCore.is_null(request.reasoning_effort):
            body['reasoningEffort'] = request.reasoning_effort
        if not DaraCore.is_null(request.repetition_penalty):
            body['repetitionPenalty'] = request.repetition_penalty
        if not DaraCore.is_null(request.response_format):
            body['responseFormat'] = request.response_format
        if not DaraCore.is_null(request.seed):
            body['seed'] = request.seed
        if not DaraCore.is_null(request.skip_special_tokens):
            body['skipSpecialTokens'] = request.skip_special_tokens
        if not DaraCore.is_null(request.stop):
            body['stop'] = request.stop
        if not DaraCore.is_null(request.stop_token_ids):
            body['stopTokenIds'] = request.stop_token_ids
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.stream_options):
            body['streamOptions'] = request.stream_options
        if not DaraCore.is_null(request.structured_outputs):
            body['structuredOutputs'] = request.structured_outputs
        if not DaraCore.is_null(request.temperature):
            body['temperature'] = request.temperature
        if not DaraCore.is_null(request.tool_choice):
            body['toolChoice'] = request.tool_choice
        if not DaraCore.is_null(request.tools):
            body['tools'] = request.tools
        if not DaraCore.is_null(request.top_k):
            body['topK'] = request.top_k
        if not DaraCore.is_null(request.top_logprobs):
            body['topLogprobs'] = request.top_logprobs
        if not DaraCore.is_null(request.top_p):
            body['topP'] = request.top_p
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_qiagent_api_key):
            real_headers['X-QI-Agent-Api-Key'] = str(headers.x_qiagent_api_key)
        if not DaraCore.is_null(headers.x_qiinstance_id):
            real_headers['X-QI-Instance-Id'] = str(headers.x_qiinstance_id)
        if not DaraCore.is_null(headers.x_qisession_id):
            real_headers['X-QI-Session-Id'] = str(headers.x_qisession_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PaChatCompletionStream',
            version = '2026-08-31',
            protocol = 'HTTPS',
            pathname = f'/pa/v1/chat/completions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.PaChatCompletionStreamResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def pa_chat_completion_stream_with_options(
        self,
        request: main_models.PaChatCompletionStreamRequest,
        headers: main_models.PaChatCompletionStreamHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PaChatCompletionStreamResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.allowed_token_ids):
            body['allowedTokenIds'] = request.allowed_token_ids
        if not DaraCore.is_null(request.bad_words):
            body['badWords'] = request.bad_words
        if not DaraCore.is_null(request.chat_template_kwargs):
            body['chatTemplateKwargs'] = request.chat_template_kwargs
        if not DaraCore.is_null(request.frequency_penalty):
            body['frequencyPenalty'] = request.frequency_penalty
        if not DaraCore.is_null(request.ignore_eos):
            body['ignoreEos'] = request.ignore_eos
        if not DaraCore.is_null(request.include_reasoning):
            body['includeReasoning'] = request.include_reasoning
        if not DaraCore.is_null(request.logprobs):
            body['logprobs'] = request.logprobs
        if not DaraCore.is_null(request.max_completion_tokens):
            body['maxCompletionTokens'] = request.max_completion_tokens
        if not DaraCore.is_null(request.max_tokens):
            body['maxTokens'] = request.max_tokens
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.min_p):
            body['minP'] = request.min_p
        if not DaraCore.is_null(request.min_tokens):
            body['minTokens'] = request.min_tokens
        if not DaraCore.is_null(request.mm_processor_kwargs):
            body['mmProcessorKwargs'] = request.mm_processor_kwargs
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.n):
            body['n'] = request.n
        if not DaraCore.is_null(request.parallel_tool_calls):
            body['parallelToolCalls'] = request.parallel_tool_calls
        if not DaraCore.is_null(request.presence_penalty):
            body['presencePenalty'] = request.presence_penalty
        if not DaraCore.is_null(request.prompt_logprobs):
            body['promptLogprobs'] = request.prompt_logprobs
        if not DaraCore.is_null(request.reasoning_effort):
            body['reasoningEffort'] = request.reasoning_effort
        if not DaraCore.is_null(request.repetition_penalty):
            body['repetitionPenalty'] = request.repetition_penalty
        if not DaraCore.is_null(request.response_format):
            body['responseFormat'] = request.response_format
        if not DaraCore.is_null(request.seed):
            body['seed'] = request.seed
        if not DaraCore.is_null(request.skip_special_tokens):
            body['skipSpecialTokens'] = request.skip_special_tokens
        if not DaraCore.is_null(request.stop):
            body['stop'] = request.stop
        if not DaraCore.is_null(request.stop_token_ids):
            body['stopTokenIds'] = request.stop_token_ids
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.stream_options):
            body['streamOptions'] = request.stream_options
        if not DaraCore.is_null(request.structured_outputs):
            body['structuredOutputs'] = request.structured_outputs
        if not DaraCore.is_null(request.temperature):
            body['temperature'] = request.temperature
        if not DaraCore.is_null(request.tool_choice):
            body['toolChoice'] = request.tool_choice
        if not DaraCore.is_null(request.tools):
            body['tools'] = request.tools
        if not DaraCore.is_null(request.top_k):
            body['topK'] = request.top_k
        if not DaraCore.is_null(request.top_logprobs):
            body['topLogprobs'] = request.top_logprobs
        if not DaraCore.is_null(request.top_p):
            body['topP'] = request.top_p
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_qiagent_api_key):
            real_headers['X-QI-Agent-Api-Key'] = str(headers.x_qiagent_api_key)
        if not DaraCore.is_null(headers.x_qiinstance_id):
            real_headers['X-QI-Instance-Id'] = str(headers.x_qiinstance_id)
        if not DaraCore.is_null(headers.x_qisession_id):
            real_headers['X-QI-Session-Id'] = str(headers.x_qisession_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PaChatCompletionStream',
            version = '2026-08-31',
            protocol = 'HTTPS',
            pathname = f'/pa/v1/chat/completions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PaChatCompletionStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def pa_chat_completion_stream_with_options_async(
        self,
        request: main_models.PaChatCompletionStreamRequest,
        headers: main_models.PaChatCompletionStreamHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PaChatCompletionStreamResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.allowed_token_ids):
            body['allowedTokenIds'] = request.allowed_token_ids
        if not DaraCore.is_null(request.bad_words):
            body['badWords'] = request.bad_words
        if not DaraCore.is_null(request.chat_template_kwargs):
            body['chatTemplateKwargs'] = request.chat_template_kwargs
        if not DaraCore.is_null(request.frequency_penalty):
            body['frequencyPenalty'] = request.frequency_penalty
        if not DaraCore.is_null(request.ignore_eos):
            body['ignoreEos'] = request.ignore_eos
        if not DaraCore.is_null(request.include_reasoning):
            body['includeReasoning'] = request.include_reasoning
        if not DaraCore.is_null(request.logprobs):
            body['logprobs'] = request.logprobs
        if not DaraCore.is_null(request.max_completion_tokens):
            body['maxCompletionTokens'] = request.max_completion_tokens
        if not DaraCore.is_null(request.max_tokens):
            body['maxTokens'] = request.max_tokens
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.min_p):
            body['minP'] = request.min_p
        if not DaraCore.is_null(request.min_tokens):
            body['minTokens'] = request.min_tokens
        if not DaraCore.is_null(request.mm_processor_kwargs):
            body['mmProcessorKwargs'] = request.mm_processor_kwargs
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.n):
            body['n'] = request.n
        if not DaraCore.is_null(request.parallel_tool_calls):
            body['parallelToolCalls'] = request.parallel_tool_calls
        if not DaraCore.is_null(request.presence_penalty):
            body['presencePenalty'] = request.presence_penalty
        if not DaraCore.is_null(request.prompt_logprobs):
            body['promptLogprobs'] = request.prompt_logprobs
        if not DaraCore.is_null(request.reasoning_effort):
            body['reasoningEffort'] = request.reasoning_effort
        if not DaraCore.is_null(request.repetition_penalty):
            body['repetitionPenalty'] = request.repetition_penalty
        if not DaraCore.is_null(request.response_format):
            body['responseFormat'] = request.response_format
        if not DaraCore.is_null(request.seed):
            body['seed'] = request.seed
        if not DaraCore.is_null(request.skip_special_tokens):
            body['skipSpecialTokens'] = request.skip_special_tokens
        if not DaraCore.is_null(request.stop):
            body['stop'] = request.stop
        if not DaraCore.is_null(request.stop_token_ids):
            body['stopTokenIds'] = request.stop_token_ids
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.stream_options):
            body['streamOptions'] = request.stream_options
        if not DaraCore.is_null(request.structured_outputs):
            body['structuredOutputs'] = request.structured_outputs
        if not DaraCore.is_null(request.temperature):
            body['temperature'] = request.temperature
        if not DaraCore.is_null(request.tool_choice):
            body['toolChoice'] = request.tool_choice
        if not DaraCore.is_null(request.tools):
            body['tools'] = request.tools
        if not DaraCore.is_null(request.top_k):
            body['topK'] = request.top_k
        if not DaraCore.is_null(request.top_logprobs):
            body['topLogprobs'] = request.top_logprobs
        if not DaraCore.is_null(request.top_p):
            body['topP'] = request.top_p
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_qiagent_api_key):
            real_headers['X-QI-Agent-Api-Key'] = str(headers.x_qiagent_api_key)
        if not DaraCore.is_null(headers.x_qiinstance_id):
            real_headers['X-QI-Instance-Id'] = str(headers.x_qiinstance_id)
        if not DaraCore.is_null(headers.x_qisession_id):
            real_headers['X-QI-Session-Id'] = str(headers.x_qisession_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PaChatCompletionStream',
            version = '2026-08-31',
            protocol = 'HTTPS',
            pathname = f'/pa/v1/chat/completions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PaChatCompletionStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pa_chat_completion_stream(
        self,
        request: main_models.PaChatCompletionStreamRequest,
    ) -> main_models.PaChatCompletionStreamResponse:
        runtime = RuntimeOptions()
        headers = main_models.PaChatCompletionStreamHeaders()
        return self.pa_chat_completion_stream_with_options(request, headers, runtime)

    async def pa_chat_completion_stream_async(
        self,
        request: main_models.PaChatCompletionStreamRequest,
    ) -> main_models.PaChatCompletionStreamResponse:
        runtime = RuntimeOptions()
        headers = main_models.PaChatCompletionStreamHeaders()
        return await self.pa_chat_completion_stream_with_options_async(request, headers, runtime)
