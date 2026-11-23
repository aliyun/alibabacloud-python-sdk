# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_gateway_pop.client import Client as GatewayClientClient
from alibabacloud_qwenb2bmed20261121 import models as main_models
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
        self._product_id = 'QwenB2BMed'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('qwenb2bmed', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def medical_agent_chat_with_sse(
        self,
        request: main_models.MedicalAgentChatRequest,
        headers: main_models.MedicalAgentChatHeaders,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.MedicalAgentChatResponse, None, None]:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_dash_scope_sse):
            real_headers['X-DashScope-SSE'] = str(headers.x_dash_scope_sse)
        if not DaraCore.is_null(headers.x_gwaccess):
            real_headers['X-GW-Access'] = str(headers.x_gwaccess)
        if not DaraCore.is_null(headers.x_gwnonce):
            real_headers['X-GW-Nonce'] = str(headers.x_gwnonce)
        if not DaraCore.is_null(headers.x_gwprotocol):
            real_headers['X-GW-Protocol'] = str(headers.x_gwprotocol)
        if not DaraCore.is_null(headers.x_gwsignature):
            real_headers['X-GW-Signature'] = str(headers.x_gwsignature)
        if not DaraCore.is_null(headers.x_gwtimestamp):
            real_headers['X-GW-Timestamp'] = str(headers.x_gwtimestamp)
        if not DaraCore.is_null(headers.x_request_id):
            real_headers['X-Request-Id'] = str(headers.x_request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'MedicalAgentChat',
            version = '2026-11-21',
            protocol = 'HTTPS',
            pathname = f'/v1/api/medicalQa',
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
                    main_models.MedicalAgentChatResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def medical_agent_chat_with_sse_async(
        self,
        request: main_models.MedicalAgentChatRequest,
        headers: main_models.MedicalAgentChatHeaders,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.MedicalAgentChatResponse, None, None]:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_dash_scope_sse):
            real_headers['X-DashScope-SSE'] = str(headers.x_dash_scope_sse)
        if not DaraCore.is_null(headers.x_gwaccess):
            real_headers['X-GW-Access'] = str(headers.x_gwaccess)
        if not DaraCore.is_null(headers.x_gwnonce):
            real_headers['X-GW-Nonce'] = str(headers.x_gwnonce)
        if not DaraCore.is_null(headers.x_gwprotocol):
            real_headers['X-GW-Protocol'] = str(headers.x_gwprotocol)
        if not DaraCore.is_null(headers.x_gwsignature):
            real_headers['X-GW-Signature'] = str(headers.x_gwsignature)
        if not DaraCore.is_null(headers.x_gwtimestamp):
            real_headers['X-GW-Timestamp'] = str(headers.x_gwtimestamp)
        if not DaraCore.is_null(headers.x_request_id):
            real_headers['X-Request-Id'] = str(headers.x_request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'MedicalAgentChat',
            version = '2026-11-21',
            protocol = 'HTTPS',
            pathname = f'/v1/api/medicalQa',
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
                    main_models.MedicalAgentChatResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def medical_agent_chat_with_options(
        self,
        request: main_models.MedicalAgentChatRequest,
        headers: main_models.MedicalAgentChatHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.MedicalAgentChatResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_dash_scope_sse):
            real_headers['X-DashScope-SSE'] = str(headers.x_dash_scope_sse)
        if not DaraCore.is_null(headers.x_gwaccess):
            real_headers['X-GW-Access'] = str(headers.x_gwaccess)
        if not DaraCore.is_null(headers.x_gwnonce):
            real_headers['X-GW-Nonce'] = str(headers.x_gwnonce)
        if not DaraCore.is_null(headers.x_gwprotocol):
            real_headers['X-GW-Protocol'] = str(headers.x_gwprotocol)
        if not DaraCore.is_null(headers.x_gwsignature):
            real_headers['X-GW-Signature'] = str(headers.x_gwsignature)
        if not DaraCore.is_null(headers.x_gwtimestamp):
            real_headers['X-GW-Timestamp'] = str(headers.x_gwtimestamp)
        if not DaraCore.is_null(headers.x_request_id):
            real_headers['X-Request-Id'] = str(headers.x_request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'MedicalAgentChat',
            version = '2026-11-21',
            protocol = 'HTTPS',
            pathname = f'/v1/api/medicalQa',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MedicalAgentChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def medical_agent_chat_with_options_async(
        self,
        request: main_models.MedicalAgentChatRequest,
        headers: main_models.MedicalAgentChatHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.MedicalAgentChatResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_dash_scope_sse):
            real_headers['X-DashScope-SSE'] = str(headers.x_dash_scope_sse)
        if not DaraCore.is_null(headers.x_gwaccess):
            real_headers['X-GW-Access'] = str(headers.x_gwaccess)
        if not DaraCore.is_null(headers.x_gwnonce):
            real_headers['X-GW-Nonce'] = str(headers.x_gwnonce)
        if not DaraCore.is_null(headers.x_gwprotocol):
            real_headers['X-GW-Protocol'] = str(headers.x_gwprotocol)
        if not DaraCore.is_null(headers.x_gwsignature):
            real_headers['X-GW-Signature'] = str(headers.x_gwsignature)
        if not DaraCore.is_null(headers.x_gwtimestamp):
            real_headers['X-GW-Timestamp'] = str(headers.x_gwtimestamp)
        if not DaraCore.is_null(headers.x_request_id):
            real_headers['X-Request-Id'] = str(headers.x_request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'MedicalAgentChat',
            version = '2026-11-21',
            protocol = 'HTTPS',
            pathname = f'/v1/api/medicalQa',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MedicalAgentChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def medical_agent_chat(
        self,
        request: main_models.MedicalAgentChatRequest,
    ) -> main_models.MedicalAgentChatResponse:
        runtime = RuntimeOptions()
        headers = main_models.MedicalAgentChatHeaders()
        return self.medical_agent_chat_with_options(request, headers, runtime)

    async def medical_agent_chat_async(
        self,
        request: main_models.MedicalAgentChatRequest,
    ) -> main_models.MedicalAgentChatResponse:
        runtime = RuntimeOptions()
        headers = main_models.MedicalAgentChatHeaders()
        return await self.medical_agent_chat_with_options_async(request, headers, runtime)

    def medical_model_inference_with_sse(
        self,
        request: main_models.MedicalModelInferenceRequest,
        headers: main_models.MedicalModelInferenceHeaders,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.MedicalModelInferenceResponse, None, None]:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_dash_scope_sse):
            real_headers['X-DashScope-SSE'] = str(headers.x_dash_scope_sse)
        if not DaraCore.is_null(headers.x_gwaccess):
            real_headers['X-GW-Access'] = str(headers.x_gwaccess)
        if not DaraCore.is_null(headers.x_gwnonce):
            real_headers['X-GW-Nonce'] = str(headers.x_gwnonce)
        if not DaraCore.is_null(headers.x_gwprotocol):
            real_headers['X-GW-Protocol'] = str(headers.x_gwprotocol)
        if not DaraCore.is_null(headers.x_gwsignature):
            real_headers['X-GW-Signature'] = str(headers.x_gwsignature)
        if not DaraCore.is_null(headers.x_gwtimestamp):
            real_headers['X-GW-Timestamp'] = str(headers.x_gwtimestamp)
        if not DaraCore.is_null(headers.x_request_id):
            real_headers['X-Request-Id'] = str(headers.x_request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'MedicalModelInference',
            version = '2026-11-21',
            protocol = 'HTTPS',
            pathname = f'/v1/api/directModel',
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
                    main_models.MedicalModelInferenceResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def medical_model_inference_with_sse_async(
        self,
        request: main_models.MedicalModelInferenceRequest,
        headers: main_models.MedicalModelInferenceHeaders,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.MedicalModelInferenceResponse, None, None]:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_dash_scope_sse):
            real_headers['X-DashScope-SSE'] = str(headers.x_dash_scope_sse)
        if not DaraCore.is_null(headers.x_gwaccess):
            real_headers['X-GW-Access'] = str(headers.x_gwaccess)
        if not DaraCore.is_null(headers.x_gwnonce):
            real_headers['X-GW-Nonce'] = str(headers.x_gwnonce)
        if not DaraCore.is_null(headers.x_gwprotocol):
            real_headers['X-GW-Protocol'] = str(headers.x_gwprotocol)
        if not DaraCore.is_null(headers.x_gwsignature):
            real_headers['X-GW-Signature'] = str(headers.x_gwsignature)
        if not DaraCore.is_null(headers.x_gwtimestamp):
            real_headers['X-GW-Timestamp'] = str(headers.x_gwtimestamp)
        if not DaraCore.is_null(headers.x_request_id):
            real_headers['X-Request-Id'] = str(headers.x_request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'MedicalModelInference',
            version = '2026-11-21',
            protocol = 'HTTPS',
            pathname = f'/v1/api/directModel',
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
                    main_models.MedicalModelInferenceResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def medical_model_inference_with_options(
        self,
        request: main_models.MedicalModelInferenceRequest,
        headers: main_models.MedicalModelInferenceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.MedicalModelInferenceResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_dash_scope_sse):
            real_headers['X-DashScope-SSE'] = str(headers.x_dash_scope_sse)
        if not DaraCore.is_null(headers.x_gwaccess):
            real_headers['X-GW-Access'] = str(headers.x_gwaccess)
        if not DaraCore.is_null(headers.x_gwnonce):
            real_headers['X-GW-Nonce'] = str(headers.x_gwnonce)
        if not DaraCore.is_null(headers.x_gwprotocol):
            real_headers['X-GW-Protocol'] = str(headers.x_gwprotocol)
        if not DaraCore.is_null(headers.x_gwsignature):
            real_headers['X-GW-Signature'] = str(headers.x_gwsignature)
        if not DaraCore.is_null(headers.x_gwtimestamp):
            real_headers['X-GW-Timestamp'] = str(headers.x_gwtimestamp)
        if not DaraCore.is_null(headers.x_request_id):
            real_headers['X-Request-Id'] = str(headers.x_request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'MedicalModelInference',
            version = '2026-11-21',
            protocol = 'HTTPS',
            pathname = f'/v1/api/directModel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MedicalModelInferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def medical_model_inference_with_options_async(
        self,
        request: main_models.MedicalModelInferenceRequest,
        headers: main_models.MedicalModelInferenceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.MedicalModelInferenceResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_dash_scope_sse):
            real_headers['X-DashScope-SSE'] = str(headers.x_dash_scope_sse)
        if not DaraCore.is_null(headers.x_gwaccess):
            real_headers['X-GW-Access'] = str(headers.x_gwaccess)
        if not DaraCore.is_null(headers.x_gwnonce):
            real_headers['X-GW-Nonce'] = str(headers.x_gwnonce)
        if not DaraCore.is_null(headers.x_gwprotocol):
            real_headers['X-GW-Protocol'] = str(headers.x_gwprotocol)
        if not DaraCore.is_null(headers.x_gwsignature):
            real_headers['X-GW-Signature'] = str(headers.x_gwsignature)
        if not DaraCore.is_null(headers.x_gwtimestamp):
            real_headers['X-GW-Timestamp'] = str(headers.x_gwtimestamp)
        if not DaraCore.is_null(headers.x_request_id):
            real_headers['X-Request-Id'] = str(headers.x_request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'MedicalModelInference',
            version = '2026-11-21',
            protocol = 'HTTPS',
            pathname = f'/v1/api/directModel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MedicalModelInferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def medical_model_inference(
        self,
        request: main_models.MedicalModelInferenceRequest,
    ) -> main_models.MedicalModelInferenceResponse:
        runtime = RuntimeOptions()
        headers = main_models.MedicalModelInferenceHeaders()
        return self.medical_model_inference_with_options(request, headers, runtime)

    async def medical_model_inference_async(
        self,
        request: main_models.MedicalModelInferenceRequest,
    ) -> main_models.MedicalModelInferenceResponse:
        runtime = RuntimeOptions()
        headers = main_models.MedicalModelInferenceHeaders()
        return await self.medical_model_inference_with_options_async(request, headers, runtime)

    def open_service_with_options(
        self,
        request: main_models.OpenServiceRequest,
        headers: main_models.OpenServiceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.OpenServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.communication):
            body['communication'] = request.communication
        if not DaraCore.is_null(request.open_benefits):
            body['openBenefits'] = request.open_benefits
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_gwaccess):
            real_headers['X-GW-Access'] = str(headers.x_gwaccess)
        if not DaraCore.is_null(headers.x_gwnonce):
            real_headers['X-GW-Nonce'] = str(headers.x_gwnonce)
        if not DaraCore.is_null(headers.x_gwsignature):
            real_headers['X-GW-Signature'] = str(headers.x_gwsignature)
        if not DaraCore.is_null(headers.x_gwtimestamp):
            real_headers['X-GW-Timestamp'] = str(headers.x_gwtimestamp)
        if not DaraCore.is_null(headers.x_request_id):
            real_headers['X-Request-Id'] = str(headers.x_request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OpenService',
            version = '2026-11-21',
            protocol = 'HTTPS',
            pathname = f'/v1/api/medical/openService',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_service_with_options_async(
        self,
        request: main_models.OpenServiceRequest,
        headers: main_models.OpenServiceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.OpenServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.communication):
            body['communication'] = request.communication
        if not DaraCore.is_null(request.open_benefits):
            body['openBenefits'] = request.open_benefits
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_gwaccess):
            real_headers['X-GW-Access'] = str(headers.x_gwaccess)
        if not DaraCore.is_null(headers.x_gwnonce):
            real_headers['X-GW-Nonce'] = str(headers.x_gwnonce)
        if not DaraCore.is_null(headers.x_gwsignature):
            real_headers['X-GW-Signature'] = str(headers.x_gwsignature)
        if not DaraCore.is_null(headers.x_gwtimestamp):
            real_headers['X-GW-Timestamp'] = str(headers.x_gwtimestamp)
        if not DaraCore.is_null(headers.x_request_id):
            real_headers['X-Request-Id'] = str(headers.x_request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OpenService',
            version = '2026-11-21',
            protocol = 'HTTPS',
            pathname = f'/v1/api/medical/openService',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_service(
        self,
        request: main_models.OpenServiceRequest,
    ) -> main_models.OpenServiceResponse:
        runtime = RuntimeOptions()
        headers = main_models.OpenServiceHeaders()
        return self.open_service_with_options(request, headers, runtime)

    async def open_service_async(
        self,
        request: main_models.OpenServiceRequest,
    ) -> main_models.OpenServiceResponse:
        runtime = RuntimeOptions()
        headers = main_models.OpenServiceHeaders()
        return await self.open_service_with_options_async(request, headers, runtime)
