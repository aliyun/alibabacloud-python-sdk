# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_sysom20231230 import models as main_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('sysom', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def auth_diagnosis_with_options(
        self,
        request: main_models.AuthDiagnosisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AuthDiagnosisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_create_role):
            body['autoCreateRole'] = request.auto_create_role
        if not DaraCore.is_null(request.auto_install_agent):
            body['autoInstallAgent'] = request.auto_install_agent
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AuthDiagnosis',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/diagnosis/auth',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def auth_diagnosis_with_options_async(
        self,
        request: main_models.AuthDiagnosisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AuthDiagnosisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_create_role):
            body['autoCreateRole'] = request.auto_create_role
        if not DaraCore.is_null(request.auto_install_agent):
            body['autoInstallAgent'] = request.auto_install_agent
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AuthDiagnosis',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/diagnosis/auth',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def auth_diagnosis(
        self,
        request: main_models.AuthDiagnosisRequest,
    ) -> main_models.AuthDiagnosisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.auth_diagnosis_with_options(request, headers, runtime)

    async def auth_diagnosis_async(
        self,
        request: main_models.AuthDiagnosisRequest,
    ) -> main_models.AuthDiagnosisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.auth_diagnosis_with_options_async(request, headers, runtime)

    def check_agent_config_supported_with_options(
        self,
        request: main_models.CheckAgentConfigSupportedRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckAgentConfigSupportedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['agentId'] = request.agent_id
        if not DaraCore.is_null(request.check_type):
            query['checkType'] = request.check_type
        if not DaraCore.is_null(request.clusters):
            query['clusters'] = request.clusters
        if not DaraCore.is_null(request.config_id):
            query['configId'] = request.config_id
        if not DaraCore.is_null(request.content):
            query['content'] = request.content
        if not DaraCore.is_null(request.instances):
            query['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckAgentConfigSupported',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/checkAgentConfigSupported',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckAgentConfigSupportedResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_agent_config_supported_with_options_async(
        self,
        request: main_models.CheckAgentConfigSupportedRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckAgentConfigSupportedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['agentId'] = request.agent_id
        if not DaraCore.is_null(request.check_type):
            query['checkType'] = request.check_type
        if not DaraCore.is_null(request.clusters):
            query['clusters'] = request.clusters
        if not DaraCore.is_null(request.config_id):
            query['configId'] = request.config_id
        if not DaraCore.is_null(request.content):
            query['content'] = request.content
        if not DaraCore.is_null(request.instances):
            query['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckAgentConfigSupported',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/checkAgentConfigSupported',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckAgentConfigSupportedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_agent_config_supported(
        self,
        request: main_models.CheckAgentConfigSupportedRequest,
    ) -> main_models.CheckAgentConfigSupportedResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.check_agent_config_supported_with_options(request, headers, runtime)

    async def check_agent_config_supported_async(
        self,
        request: main_models.CheckAgentConfigSupportedRequest,
    ) -> main_models.CheckAgentConfigSupportedResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.check_agent_config_supported_with_options_async(request, headers, runtime)

    def check_instance_support_with_options(
        self,
        request: main_models.CheckInstanceSupportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckInstanceSupportResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        if not DaraCore.is_null(request.region):
            body['region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckInstanceSupport',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/supportInstanceList/checkInstanceSupport',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckInstanceSupportResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_instance_support_with_options_async(
        self,
        request: main_models.CheckInstanceSupportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckInstanceSupportResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        if not DaraCore.is_null(request.region):
            body['region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckInstanceSupport',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/supportInstanceList/checkInstanceSupport',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckInstanceSupportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_instance_support(
        self,
        request: main_models.CheckInstanceSupportRequest,
    ) -> main_models.CheckInstanceSupportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.check_instance_support_with_options(request, headers, runtime)

    async def check_instance_support_async(
        self,
        request: main_models.CheckInstanceSupportRequest,
    ) -> main_models.CheckInstanceSupportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.check_instance_support_with_options_async(request, headers, runtime)

    def cpu_high_agent_stream_response_with_sse(
        self,
        request: main_models.CpuHighAgentStreamResponseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.CpuHighAgentStreamResponseResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.llm_param_string):
            body['llmParamString'] = request.llm_param_string
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CpuHighAgentStreamResponse',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/highCpuAgent/streamResponse',
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
                    main_models.CpuHighAgentStreamResponseResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def cpu_high_agent_stream_response_with_sse_async(
        self,
        request: main_models.CpuHighAgentStreamResponseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.CpuHighAgentStreamResponseResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.llm_param_string):
            body['llmParamString'] = request.llm_param_string
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CpuHighAgentStreamResponse',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/highCpuAgent/streamResponse',
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
                    main_models.CpuHighAgentStreamResponseResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def cpu_high_agent_stream_response_with_options(
        self,
        request: main_models.CpuHighAgentStreamResponseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CpuHighAgentStreamResponseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.llm_param_string):
            body['llmParamString'] = request.llm_param_string
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CpuHighAgentStreamResponse',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/highCpuAgent/streamResponse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CpuHighAgentStreamResponseResponse(),
            self.call_api(params, req, runtime)
        )

    async def cpu_high_agent_stream_response_with_options_async(
        self,
        request: main_models.CpuHighAgentStreamResponseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CpuHighAgentStreamResponseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.llm_param_string):
            body['llmParamString'] = request.llm_param_string
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CpuHighAgentStreamResponse',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/highCpuAgent/streamResponse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CpuHighAgentStreamResponseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cpu_high_agent_stream_response(
        self,
        request: main_models.CpuHighAgentStreamResponseRequest,
    ) -> main_models.CpuHighAgentStreamResponseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.cpu_high_agent_stream_response_with_options(request, headers, runtime)

    async def cpu_high_agent_stream_response_async(
        self,
        request: main_models.CpuHighAgentStreamResponseRequest,
    ) -> main_models.CpuHighAgentStreamResponseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.cpu_high_agent_stream_response_with_options_async(request, headers, runtime)

    def create_agent_config_with_options(
        self,
        request: main_models.CreateAgentConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.config_name):
            body['configName'] = request.config_name
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentConfig',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/createAgentConfig',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_agent_config_with_options_async(
        self,
        request: main_models.CreateAgentConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.config_name):
            body['configName'] = request.config_name
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentConfig',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/createAgentConfig',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_agent_config(
        self,
        request: main_models.CreateAgentConfigRequest,
    ) -> main_models.CreateAgentConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_agent_config_with_options(request, headers, runtime)

    async def create_agent_config_async(
        self,
        request: main_models.CreateAgentConfigRequest,
    ) -> main_models.CreateAgentConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_agent_config_with_options_async(request, headers, runtime)

    def create_alert_destination_with_options(
        self,
        request: main_models.CreateAlertDestinationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAlertDestinationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['app_id'] = request.app_id
        if not DaraCore.is_null(request.app_secret):
            body['app_secret'] = request.app_secret
        if not DaraCore.is_null(request.group_id):
            body['group_id'] = request.group_id
        if not DaraCore.is_null(request.imbot):
            body['imbot'] = request.imbot
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        if not DaraCore.is_null(request.target):
            body['target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlertDestination',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/createDestination',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAlertDestinationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alert_destination_with_options_async(
        self,
        request: main_models.CreateAlertDestinationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAlertDestinationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['app_id'] = request.app_id
        if not DaraCore.is_null(request.app_secret):
            body['app_secret'] = request.app_secret
        if not DaraCore.is_null(request.group_id):
            body['group_id'] = request.group_id
        if not DaraCore.is_null(request.imbot):
            body['imbot'] = request.imbot
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        if not DaraCore.is_null(request.target):
            body['target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlertDestination',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/createDestination',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAlertDestinationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alert_destination(
        self,
        request: main_models.CreateAlertDestinationRequest,
    ) -> main_models.CreateAlertDestinationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_alert_destination_with_options(request, headers, runtime)

    async def create_alert_destination_async(
        self,
        request: main_models.CreateAlertDestinationRequest,
    ) -> main_models.CreateAlertDestinationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_alert_destination_with_options_async(request, headers, runtime)

    def create_alert_strategy_with_options(
        self,
        request: main_models.CreateAlertStrategyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAlertStrategyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enabled):
            body['enabled'] = request.enabled
        if not DaraCore.is_null(request.k_8s_label):
            body['k8sLabel'] = request.k_8s_label
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.strategy):
            body['strategy'] = request.strategy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlertStrategy',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/createStrategy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAlertStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alert_strategy_with_options_async(
        self,
        request: main_models.CreateAlertStrategyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAlertStrategyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enabled):
            body['enabled'] = request.enabled
        if not DaraCore.is_null(request.k_8s_label):
            body['k8sLabel'] = request.k_8s_label
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.strategy):
            body['strategy'] = request.strategy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlertStrategy',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/createStrategy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAlertStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alert_strategy(
        self,
        request: main_models.CreateAlertStrategyRequest,
    ) -> main_models.CreateAlertStrategyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_alert_strategy_with_options(request, headers, runtime)

    async def create_alert_strategy_async(
        self,
        request: main_models.CreateAlertStrategyRequest,
    ) -> main_models.CreateAlertStrategyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_alert_strategy_with_options_async(request, headers, runtime)

    def create_cluster_vpc_endpoint_connection_with_options(
        self,
        request: main_models.CreateClusterVpcEndpointConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateClusterVpcEndpointConnectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['clusterId'] = request.cluster_id
        if not DaraCore.is_null(request.dry_run):
            body['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.region):
            body['region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateClusterVpcEndpointConnection',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/k8sProxy/access/createClusterVpcEndpointConnection',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClusterVpcEndpointConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_vpc_endpoint_connection_with_options_async(
        self,
        request: main_models.CreateClusterVpcEndpointConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateClusterVpcEndpointConnectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['clusterId'] = request.cluster_id
        if not DaraCore.is_null(request.dry_run):
            body['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.region):
            body['region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateClusterVpcEndpointConnection',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/k8sProxy/access/createClusterVpcEndpointConnection',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClusterVpcEndpointConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster_vpc_endpoint_connection(
        self,
        request: main_models.CreateClusterVpcEndpointConnectionRequest,
    ) -> main_models.CreateClusterVpcEndpointConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_cluster_vpc_endpoint_connection_with_options(request, headers, runtime)

    async def create_cluster_vpc_endpoint_connection_async(
        self,
        request: main_models.CreateClusterVpcEndpointConnectionRequest,
    ) -> main_models.CreateClusterVpcEndpointConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_cluster_vpc_endpoint_connection_with_options_async(request, headers, runtime)

    def create_instance_inspection_with_options(
        self,
        request: main_models.CreateInstanceInspectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceInspectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance):
            body['instance'] = request.instance
        if not DaraCore.is_null(request.items):
            body['items'] = request.items
        if not DaraCore.is_null(request.metric_source):
            body['metricSource'] = request.metric_source
        if not DaraCore.is_null(request.region):
            body['region'] = request.region
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceInspection',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/inspection/createInstanceInspection',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceInspectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_inspection_with_options_async(
        self,
        request: main_models.CreateInstanceInspectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceInspectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance):
            body['instance'] = request.instance
        if not DaraCore.is_null(request.items):
            body['items'] = request.items
        if not DaraCore.is_null(request.metric_source):
            body['metricSource'] = request.metric_source
        if not DaraCore.is_null(request.region):
            body['region'] = request.region
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceInspection',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/inspection/createInstanceInspection',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceInspectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_inspection(
        self,
        request: main_models.CreateInstanceInspectionRequest,
    ) -> main_models.CreateInstanceInspectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_instance_inspection_with_options(request, headers, runtime)

    async def create_instance_inspection_async(
        self,
        request: main_models.CreateInstanceInspectionRequest,
    ) -> main_models.CreateInstanceInspectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_instance_inspection_with_options_async(request, headers, runtime)

    def create_vmcore_diagnosis_task_with_options(
        self,
        request: main_models.CreateVmcoreDiagnosisTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateVmcoreDiagnosisTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.debuginfo_common_url):
            body['debuginfoCommonUrl'] = request.debuginfo_common_url
        if not DaraCore.is_null(request.debuginfo_url):
            body['debuginfoUrl'] = request.debuginfo_url
        if not DaraCore.is_null(request.dmesg_url):
            body['dmesgUrl'] = request.dmesg_url
        if not DaraCore.is_null(request.task_type):
            body['taskType'] = request.task_type
        if not DaraCore.is_null(request.vmcore_url):
            body['vmcoreUrl'] = request.vmcore_url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVmcoreDiagnosisTask',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crashAgent/diagnosis/createDiagnosisTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVmcoreDiagnosisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vmcore_diagnosis_task_with_options_async(
        self,
        request: main_models.CreateVmcoreDiagnosisTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateVmcoreDiagnosisTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.debuginfo_common_url):
            body['debuginfoCommonUrl'] = request.debuginfo_common_url
        if not DaraCore.is_null(request.debuginfo_url):
            body['debuginfoUrl'] = request.debuginfo_url
        if not DaraCore.is_null(request.dmesg_url):
            body['dmesgUrl'] = request.dmesg_url
        if not DaraCore.is_null(request.task_type):
            body['taskType'] = request.task_type
        if not DaraCore.is_null(request.vmcore_url):
            body['vmcoreUrl'] = request.vmcore_url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVmcoreDiagnosisTask',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crashAgent/diagnosis/createDiagnosisTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVmcoreDiagnosisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vmcore_diagnosis_task(
        self,
        request: main_models.CreateVmcoreDiagnosisTaskRequest,
    ) -> main_models.CreateVmcoreDiagnosisTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_vmcore_diagnosis_task_with_options(request, headers, runtime)

    async def create_vmcore_diagnosis_task_async(
        self,
        request: main_models.CreateVmcoreDiagnosisTaskRequest,
    ) -> main_models.CreateVmcoreDiagnosisTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_vmcore_diagnosis_task_with_options_async(request, headers, runtime)

    def delete_agent_config_with_options(
        self,
        request: main_models.DeleteAgentConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['agentId'] = request.agent_id
        if not DaraCore.is_null(request.config_id):
            query['configId'] = request.config_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgentConfig',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/deleteAgentConfig',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_agent_config_with_options_async(
        self,
        request: main_models.DeleteAgentConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['agentId'] = request.agent_id
        if not DaraCore.is_null(request.config_id):
            query['configId'] = request.config_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgentConfig',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/deleteAgentConfig',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_agent_config(
        self,
        request: main_models.DeleteAgentConfigRequest,
    ) -> main_models.DeleteAgentConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_agent_config_with_options(request, headers, runtime)

    async def delete_agent_config_async(
        self,
        request: main_models.DeleteAgentConfigRequest,
    ) -> main_models.DeleteAgentConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_agent_config_with_options_async(request, headers, runtime)

    def delete_alert_destination_with_options(
        self,
        request: main_models.DeleteAlertDestinationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlertDestinationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlertDestination',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/deleteDestination',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlertDestinationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_destination_with_options_async(
        self,
        request: main_models.DeleteAlertDestinationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlertDestinationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlertDestination',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/deleteDestination',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlertDestinationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_destination(
        self,
        request: main_models.DeleteAlertDestinationRequest,
    ) -> main_models.DeleteAlertDestinationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_alert_destination_with_options(request, headers, runtime)

    async def delete_alert_destination_async(
        self,
        request: main_models.DeleteAlertDestinationRequest,
    ) -> main_models.DeleteAlertDestinationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_alert_destination_with_options_async(request, headers, runtime)

    def delete_alert_strategy_with_options(
        self,
        request: main_models.DeleteAlertStrategyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlertStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlertStrategy',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/deleteStrategy',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlertStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_strategy_with_options_async(
        self,
        request: main_models.DeleteAlertStrategyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlertStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlertStrategy',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/deleteStrategy',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlertStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_strategy(
        self,
        request: main_models.DeleteAlertStrategyRequest,
    ) -> main_models.DeleteAlertStrategyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_alert_strategy_with_options(request, headers, runtime)

    async def delete_alert_strategy_async(
        self,
        request: main_models.DeleteAlertStrategyRequest,
    ) -> main_models.DeleteAlertStrategyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_alert_strategy_with_options_async(request, headers, runtime)

    def describe_metric_list_with_options(
        self,
        request: main_models.DescribeMetricListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.metric_name):
            query['metricName'] = request.metric_name
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricList',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/proxy/get/describeMetricList',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_list_with_options_async(
        self,
        request: main_models.DescribeMetricListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.metric_name):
            query['metricName'] = request.metric_name
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricList',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/proxy/get/describeMetricList',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_list(
        self,
        request: main_models.DescribeMetricListRequest,
    ) -> main_models.DescribeMetricListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_metric_list_with_options(request, headers, runtime)

    async def describe_metric_list_async(
        self,
        request: main_models.DescribeMetricListRequest,
    ) -> main_models.DescribeMetricListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_metric_list_with_options_async(request, headers, runtime)

    def generate_copilot_response_with_options(
        self,
        request: main_models.GenerateCopilotResponseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateCopilotResponseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.llm_param_string):
            body['llmParamString'] = request.llm_param_string
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateCopilotResponse',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/copilot/generate_copilot_response',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateCopilotResponseResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_copilot_response_with_options_async(
        self,
        request: main_models.GenerateCopilotResponseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateCopilotResponseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.llm_param_string):
            body['llmParamString'] = request.llm_param_string
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateCopilotResponse',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/copilot/generate_copilot_response',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateCopilotResponseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_copilot_response(
        self,
        request: main_models.GenerateCopilotResponseRequest,
    ) -> main_models.GenerateCopilotResponseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.generate_copilot_response_with_options(request, headers, runtime)

    async def generate_copilot_response_async(
        self,
        request: main_models.GenerateCopilotResponseRequest,
    ) -> main_models.GenerateCopilotResponseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.generate_copilot_response_with_options_async(request, headers, runtime)

    def generate_copilot_stream_response_with_sse(
        self,
        request: main_models.GenerateCopilotStreamResponseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.GenerateCopilotStreamResponseResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.llm_param_string):
            body['llmParamString'] = request.llm_param_string
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateCopilotStreamResponse',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/copilot/generate_copilot_stream_response',
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
                    main_models.GenerateCopilotStreamResponseResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def generate_copilot_stream_response_with_sse_async(
        self,
        request: main_models.GenerateCopilotStreamResponseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.GenerateCopilotStreamResponseResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.llm_param_string):
            body['llmParamString'] = request.llm_param_string
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateCopilotStreamResponse',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/copilot/generate_copilot_stream_response',
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
                    main_models.GenerateCopilotStreamResponseResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def generate_copilot_stream_response_with_options(
        self,
        request: main_models.GenerateCopilotStreamResponseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateCopilotStreamResponseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.llm_param_string):
            body['llmParamString'] = request.llm_param_string
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateCopilotStreamResponse',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/copilot/generate_copilot_stream_response',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateCopilotStreamResponseResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_copilot_stream_response_with_options_async(
        self,
        request: main_models.GenerateCopilotStreamResponseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateCopilotStreamResponseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.llm_param_string):
            body['llmParamString'] = request.llm_param_string
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateCopilotStreamResponse',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/copilot/generate_copilot_stream_response',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateCopilotStreamResponseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_copilot_stream_response(
        self,
        request: main_models.GenerateCopilotStreamResponseRequest,
    ) -> main_models.GenerateCopilotStreamResponseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.generate_copilot_stream_response_with_options(request, headers, runtime)

    async def generate_copilot_stream_response_async(
        self,
        request: main_models.GenerateCopilotStreamResponseRequest,
    ) -> main_models.GenerateCopilotStreamResponseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.generate_copilot_stream_response_with_options_async(request, headers, runtime)

    def get_aiquery_result_with_options(
        self,
        request: main_models.GetAIQueryResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAIQueryResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.analysis_id):
            body['analysisId'] = request.analysis_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAIQueryResult',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/app_observ/aiAnalysis/query_result',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAIQueryResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aiquery_result_with_options_async(
        self,
        request: main_models.GetAIQueryResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAIQueryResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.analysis_id):
            body['analysisId'] = request.analysis_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAIQueryResult',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/app_observ/aiAnalysis/query_result',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAIQueryResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aiquery_result(
        self,
        request: main_models.GetAIQueryResultRequest,
    ) -> main_models.GetAIQueryResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_aiquery_result_with_options(request, headers, runtime)

    async def get_aiquery_result_async(
        self,
        request: main_models.GetAIQueryResultRequest,
    ) -> main_models.GetAIQueryResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_aiquery_result_with_options_async(request, headers, runtime)

    def get_abnormal_events_count_with_options(
        self,
        request: main_models.GetAbnormalEventsCountRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAbnormalEventsCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster):
            query['cluster'] = request.cluster
        if not DaraCore.is_null(request.end):
            query['end'] = request.end
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.level):
            query['level'] = request.level
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        if not DaraCore.is_null(request.pod):
            query['pod'] = request.pod
        if not DaraCore.is_null(request.show_pod):
            query['showPod'] = request.show_pod
        if not DaraCore.is_null(request.start):
            query['start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAbnormalEventsCount',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/cluster_health/range/abnormaly_events_count',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAbnormalEventsCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_abnormal_events_count_with_options_async(
        self,
        request: main_models.GetAbnormalEventsCountRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAbnormalEventsCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster):
            query['cluster'] = request.cluster
        if not DaraCore.is_null(request.end):
            query['end'] = request.end
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.level):
            query['level'] = request.level
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        if not DaraCore.is_null(request.pod):
            query['pod'] = request.pod
        if not DaraCore.is_null(request.show_pod):
            query['showPod'] = request.show_pod
        if not DaraCore.is_null(request.start):
            query['start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAbnormalEventsCount',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/cluster_health/range/abnormaly_events_count',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAbnormalEventsCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_abnormal_events_count(
        self,
        request: main_models.GetAbnormalEventsCountRequest,
    ) -> main_models.GetAbnormalEventsCountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_abnormal_events_count_with_options(request, headers, runtime)

    async def get_abnormal_events_count_async(
        self,
        request: main_models.GetAbnormalEventsCountRequest,
    ) -> main_models.GetAbnormalEventsCountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_abnormal_events_count_with_options_async(request, headers, runtime)

    def get_agent_with_options(
        self,
        request: main_models.GetAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['agent_id'] = request.agent_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgent',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/get_agent',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_with_options_async(
        self,
        request: main_models.GetAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['agent_id'] = request.agent_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgent',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/get_agent',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.get_agent_with_options(request, headers, runtime)

    async def get_agent_async(
        self,
        request: main_models.GetAgentRequest,
    ) -> main_models.GetAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_agent_with_options_async(request, headers, runtime)

    def get_agent_config_with_options(
        self,
        request: main_models.GetAgentConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['agentId'] = request.agent_id
        if not DaraCore.is_null(request.config_id):
            query['configId'] = request.config_id
        if not DaraCore.is_null(request.config_name):
            query['configName'] = request.config_name
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentConfig',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/getAgentConfig',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_config_with_options_async(
        self,
        request: main_models.GetAgentConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['agentId'] = request.agent_id
        if not DaraCore.is_null(request.config_id):
            query['configId'] = request.config_id
        if not DaraCore.is_null(request.config_name):
            query['configName'] = request.config_name
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentConfig',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/getAgentConfig',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_config(
        self,
        request: main_models.GetAgentConfigRequest,
    ) -> main_models.GetAgentConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_agent_config_with_options(request, headers, runtime)

    async def get_agent_config_async(
        self,
        request: main_models.GetAgentConfigRequest,
    ) -> main_models.GetAgentConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_agent_config_with_options_async(request, headers, runtime)

    def get_agent_task_with_options(
        self,
        request: main_models.GetAgentTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentTask',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/get_agent_task',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_task_with_options_async(
        self,
        request: main_models.GetAgentTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentTask',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/get_agent_task',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_task(
        self,
        request: main_models.GetAgentTaskRequest,
    ) -> main_models.GetAgentTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_agent_task_with_options(request, headers, runtime)

    async def get_agent_task_async(
        self,
        request: main_models.GetAgentTaskRequest,
    ) -> main_models.GetAgentTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_agent_task_with_options_async(request, headers, runtime)

    def get_aifg_result_with_options(
        self,
        request: main_models.GetAifgResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAifgResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAifgResult',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aifg/getAifgResult',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAifgResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aifg_result_with_options_async(
        self,
        request: main_models.GetAifgResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAifgResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAifgResult',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aifg/getAifgResult',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAifgResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aifg_result(
        self,
        request: main_models.GetAifgResultRequest,
    ) -> main_models.GetAifgResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_aifg_result_with_options(request, headers, runtime)

    async def get_aifg_result_async(
        self,
        request: main_models.GetAifgResultRequest,
    ) -> main_models.GetAifgResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_aifg_result_with_options_async(request, headers, runtime)

    def get_aifg_url_with_options(
        self,
        request: main_models.GetAifgUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAifgUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAifgUrl',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aifg/getAifgUrl',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAifgUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aifg_url_with_options_async(
        self,
        request: main_models.GetAifgUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAifgUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAifgUrl',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aifg/getAifgUrl',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAifgUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aifg_url(
        self,
        request: main_models.GetAifgUrlRequest,
    ) -> main_models.GetAifgUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_aifg_url_with_options(request, headers, runtime)

    async def get_aifg_url_async(
        self,
        request: main_models.GetAifgUrlRequest,
    ) -> main_models.GetAifgUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_aifg_url_with_options_async(request, headers, runtime)

    def get_alert_destination_with_options(
        self,
        request: main_models.GetAlertDestinationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAlertDestinationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAlertDestination',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/getDestination',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlertDestinationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alert_destination_with_options_async(
        self,
        request: main_models.GetAlertDestinationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAlertDestinationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAlertDestination',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/getDestination',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlertDestinationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alert_destination(
        self,
        request: main_models.GetAlertDestinationRequest,
    ) -> main_models.GetAlertDestinationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_alert_destination_with_options(request, headers, runtime)

    async def get_alert_destination_async(
        self,
        request: main_models.GetAlertDestinationRequest,
    ) -> main_models.GetAlertDestinationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_alert_destination_with_options_async(request, headers, runtime)

    def get_alert_strategy_with_options(
        self,
        request: main_models.GetAlertStrategyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAlertStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAlertStrategy',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/getStrategy',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlertStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alert_strategy_with_options_async(
        self,
        request: main_models.GetAlertStrategyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAlertStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAlertStrategy',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/getStrategy',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlertStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alert_strategy(
        self,
        request: main_models.GetAlertStrategyRequest,
    ) -> main_models.GetAlertStrategyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_alert_strategy_with_options(request, headers, runtime)

    async def get_alert_strategy_async(
        self,
        request: main_models.GetAlertStrategyRequest,
    ) -> main_models.GetAlertStrategyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_alert_strategy_with_options_async(request, headers, runtime)

    def get_config_by_name_with_options(
        self,
        request: main_models.GetConfigByNameRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigByNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_name):
            query['configName'] = request.config_name
        if not DaraCore.is_null(request.config_type):
            query['configType'] = request.config_type
        if not DaraCore.is_null(request.entity_id):
            query['entityId'] = request.entity_id
        if not DaraCore.is_null(request.use_global_uid):
            query['useGlobalUid'] = request.use_global_uid
        if not DaraCore.is_null(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConfigByName',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/configManage/config/getConfigByName',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigByNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_config_by_name_with_options_async(
        self,
        request: main_models.GetConfigByNameRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigByNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_name):
            query['configName'] = request.config_name
        if not DaraCore.is_null(request.config_type):
            query['configType'] = request.config_type
        if not DaraCore.is_null(request.entity_id):
            query['entityId'] = request.entity_id
        if not DaraCore.is_null(request.use_global_uid):
            query['useGlobalUid'] = request.use_global_uid
        if not DaraCore.is_null(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConfigByName',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/configManage/config/getConfigByName',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigByNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_config_by_name(
        self,
        request: main_models.GetConfigByNameRequest,
    ) -> main_models.GetConfigByNameResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_config_by_name_with_options(request, headers, runtime)

    async def get_config_by_name_async(
        self,
        request: main_models.GetConfigByNameRequest,
    ) -> main_models.GetConfigByNameResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_config_by_name_with_options_async(request, headers, runtime)

    def get_copilot_history_with_options(
        self,
        request: main_models.GetCopilotHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCopilotHistoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.count):
            body['count'] = request.count
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCopilotHistory',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/copilot/get_copilot_history',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCopilotHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_copilot_history_with_options_async(
        self,
        request: main_models.GetCopilotHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCopilotHistoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.count):
            body['count'] = request.count
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCopilotHistory',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/copilot/get_copilot_history',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCopilotHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_copilot_history(
        self,
        request: main_models.GetCopilotHistoryRequest,
    ) -> main_models.GetCopilotHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_copilot_history_with_options(request, headers, runtime)

    async def get_copilot_history_async(
        self,
        request: main_models.GetCopilotHistoryRequest,
    ) -> main_models.GetCopilotHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_copilot_history_with_options_async(request, headers, runtime)

    def get_cve_hotfix_with_options(
        self,
        request: main_models.GetCveHotfixRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCveHotfixResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cve_ids):
            body['cveIds'] = request.cve_ids
        if not DaraCore.is_null(request.kernel_versions):
            body['kernelVersions'] = request.kernel_versions
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCveHotfix',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/hotfixManager/hotfixes/cve',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCveHotfixResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cve_hotfix_with_options_async(
        self,
        request: main_models.GetCveHotfixRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCveHotfixResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cve_ids):
            body['cveIds'] = request.cve_ids
        if not DaraCore.is_null(request.kernel_versions):
            body['kernelVersions'] = request.kernel_versions
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCveHotfix',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/hotfixManager/hotfixes/cve',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCveHotfixResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cve_hotfix(
        self,
        request: main_models.GetCveHotfixRequest,
    ) -> main_models.GetCveHotfixResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_cve_hotfix_with_options(request, headers, runtime)

    async def get_cve_hotfix_async(
        self,
        request: main_models.GetCveHotfixRequest,
    ) -> main_models.GetCveHotfixResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_cve_hotfix_with_options_async(request, headers, runtime)

    def get_diagnosis_result_with_options(
        self,
        request: main_models.GetDiagnosisResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDiagnosisResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDiagnosisResult',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/diagnosis/get_diagnosis_results',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDiagnosisResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_diagnosis_result_with_options_async(
        self,
        request: main_models.GetDiagnosisResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDiagnosisResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDiagnosisResult',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/diagnosis/get_diagnosis_results',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDiagnosisResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_diagnosis_result(
        self,
        request: main_models.GetDiagnosisResultRequest,
    ) -> main_models.GetDiagnosisResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_diagnosis_result_with_options(request, headers, runtime)

    async def get_diagnosis_result_async(
        self,
        request: main_models.GetDiagnosisResultRequest,
    ) -> main_models.GetDiagnosisResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_diagnosis_result_with_options_async(request, headers, runtime)

    def get_gpu_cluster_args_options_with_options(
        self,
        request: main_models.GetGpuClusterArgsOptionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGpuClusterArgsOptionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter_type):
            query['filterType'] = request.filter_type
        if not DaraCore.is_null(request.filter_values):
            query['filterValues'] = request.filter_values
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGpuClusterArgsOptions',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiTopology/topology/listClusterTopologyOptions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGpuClusterArgsOptionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gpu_cluster_args_options_with_options_async(
        self,
        request: main_models.GetGpuClusterArgsOptionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGpuClusterArgsOptionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter_type):
            query['filterType'] = request.filter_type
        if not DaraCore.is_null(request.filter_values):
            query['filterValues'] = request.filter_values
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGpuClusterArgsOptions',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiTopology/topology/listClusterTopologyOptions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGpuClusterArgsOptionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gpu_cluster_args_options(
        self,
        request: main_models.GetGpuClusterArgsOptionsRequest,
    ) -> main_models.GetGpuClusterArgsOptionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_gpu_cluster_args_options_with_options(request, headers, runtime)

    async def get_gpu_cluster_args_options_async(
        self,
        request: main_models.GetGpuClusterArgsOptionsRequest,
    ) -> main_models.GetGpuClusterArgsOptionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_gpu_cluster_args_options_with_options_async(request, headers, runtime)

    def get_gpu_cluster_list_alarm_record_with_options(
        self,
        request: main_models.GetGpuClusterListAlarmRecordRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGpuClusterListAlarmRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_cluster):
            query['alarmCluster'] = request.alarm_cluster
        if not DaraCore.is_null(request.alarm_ext_info):
            query['alarmExtInfo'] = request.alarm_ext_info
        if not DaraCore.is_null(request.alarm_task):
            query['alarmTask'] = request.alarm_task
        if not DaraCore.is_null(request.alarm_time):
            query['alarmTime'] = request.alarm_time
        if not DaraCore.is_null(request.alarm_type):
            query['alarmType'] = request.alarm_type
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGpuClusterListAlarmRecord',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiTopology/topology/listAlarmRecord',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGpuClusterListAlarmRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gpu_cluster_list_alarm_record_with_options_async(
        self,
        request: main_models.GetGpuClusterListAlarmRecordRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGpuClusterListAlarmRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_cluster):
            query['alarmCluster'] = request.alarm_cluster
        if not DaraCore.is_null(request.alarm_ext_info):
            query['alarmExtInfo'] = request.alarm_ext_info
        if not DaraCore.is_null(request.alarm_task):
            query['alarmTask'] = request.alarm_task
        if not DaraCore.is_null(request.alarm_time):
            query['alarmTime'] = request.alarm_time
        if not DaraCore.is_null(request.alarm_type):
            query['alarmType'] = request.alarm_type
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGpuClusterListAlarmRecord',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiTopology/topology/listAlarmRecord',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGpuClusterListAlarmRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gpu_cluster_list_alarm_record(
        self,
        request: main_models.GetGpuClusterListAlarmRecordRequest,
    ) -> main_models.GetGpuClusterListAlarmRecordResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_gpu_cluster_list_alarm_record_with_options(request, headers, runtime)

    async def get_gpu_cluster_list_alarm_record_async(
        self,
        request: main_models.GetGpuClusterListAlarmRecordRequest,
    ) -> main_models.GetGpuClusterListAlarmRecordResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_gpu_cluster_list_alarm_record_with_options_async(request, headers, runtime)

    def get_gpu_cluster_topology_with_options(
        self,
        request: main_models.GetGpuClusterTopologyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGpuClusterTopologyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['channelId'] = request.channel_id
        if not DaraCore.is_null(request.cluster_id):
            query['clusterId'] = request.cluster_id
        if not DaraCore.is_null(request.communication_id):
            query['communicationId'] = request.communication_id
        if not DaraCore.is_null(request.instance_id_list):
            query['instanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.pod_list):
            query['podList'] = request.pod_list
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.task_id_list):
            query['taskIdList'] = request.task_id_list
        if not DaraCore.is_null(request.topo_type):
            query['topoType'] = request.topo_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGpuClusterTopology',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiTopology/topology/clusterTopology',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGpuClusterTopologyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gpu_cluster_topology_with_options_async(
        self,
        request: main_models.GetGpuClusterTopologyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGpuClusterTopologyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['channelId'] = request.channel_id
        if not DaraCore.is_null(request.cluster_id):
            query['clusterId'] = request.cluster_id
        if not DaraCore.is_null(request.communication_id):
            query['communicationId'] = request.communication_id
        if not DaraCore.is_null(request.instance_id_list):
            query['instanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.pod_list):
            query['podList'] = request.pod_list
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.task_id_list):
            query['taskIdList'] = request.task_id_list
        if not DaraCore.is_null(request.topo_type):
            query['topoType'] = request.topo_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGpuClusterTopology',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiTopology/topology/clusterTopology',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGpuClusterTopologyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gpu_cluster_topology(
        self,
        request: main_models.GetGpuClusterTopologyRequest,
    ) -> main_models.GetGpuClusterTopologyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_gpu_cluster_topology_with_options(request, headers, runtime)

    async def get_gpu_cluster_topology_async(
        self,
        request: main_models.GetGpuClusterTopologyRequest,
    ) -> main_models.GetGpuClusterTopologyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_gpu_cluster_topology_with_options_async(request, headers, runtime)

    def get_health_percentage_with_options(
        self,
        request: main_models.GetHealthPercentageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHealthPercentageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster):
            query['cluster'] = request.cluster
        if not DaraCore.is_null(request.end):
            query['end'] = request.end
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.start):
            query['start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHealthPercentage',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/cluster_health/range/health_percentage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHealthPercentageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_health_percentage_with_options_async(
        self,
        request: main_models.GetHealthPercentageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHealthPercentageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster):
            query['cluster'] = request.cluster
        if not DaraCore.is_null(request.end):
            query['end'] = request.end
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.start):
            query['start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHealthPercentage',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/cluster_health/range/health_percentage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHealthPercentageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_health_percentage(
        self,
        request: main_models.GetHealthPercentageRequest,
    ) -> main_models.GetHealthPercentageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_health_percentage_with_options(request, headers, runtime)

    async def get_health_percentage_async(
        self,
        request: main_models.GetHealthPercentageRequest,
    ) -> main_models.GetHealthPercentageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_health_percentage_with_options_async(request, headers, runtime)

    def get_host_count_with_options(
        self,
        request: main_models.GetHostCountRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHostCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster):
            query['cluster'] = request.cluster
        if not DaraCore.is_null(request.end):
            query['end'] = request.end
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.start):
            query['start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHostCount',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/cluster_health/range/host_count',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHostCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_host_count_with_options_async(
        self,
        request: main_models.GetHostCountRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHostCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster):
            query['cluster'] = request.cluster
        if not DaraCore.is_null(request.end):
            query['end'] = request.end
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.start):
            query['start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHostCount',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/cluster_health/range/host_count',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHostCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_host_count(
        self,
        request: main_models.GetHostCountRequest,
    ) -> main_models.GetHostCountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_host_count_with_options(request, headers, runtime)

    async def get_host_count_async(
        self,
        request: main_models.GetHostCountRequest,
    ) -> main_models.GetHostCountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_host_count_with_options_async(request, headers, runtime)

    def get_hot_spot_uniq_list_with_options(
        self,
        request: main_models.GetHotSpotUniqListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHotSpotUniqListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.beg_end):
            body['beg_end'] = request.beg_end
        if not DaraCore.is_null(request.beg_start):
            body['beg_start'] = request.beg_start
        if not DaraCore.is_null(request.instance):
            body['instance'] = request.instance
        if not DaraCore.is_null(request.pid):
            body['pid'] = request.pid
        if not DaraCore.is_null(request.table):
            body['table'] = request.table
        if not DaraCore.is_null(request.uniq):
            body['uniq'] = request.uniq
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotSpotUniqList',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/livetrace_proxy/hotspot_uniq_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotSpotUniqListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hot_spot_uniq_list_with_options_async(
        self,
        request: main_models.GetHotSpotUniqListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHotSpotUniqListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.beg_end):
            body['beg_end'] = request.beg_end
        if not DaraCore.is_null(request.beg_start):
            body['beg_start'] = request.beg_start
        if not DaraCore.is_null(request.instance):
            body['instance'] = request.instance
        if not DaraCore.is_null(request.pid):
            body['pid'] = request.pid
        if not DaraCore.is_null(request.table):
            body['table'] = request.table
        if not DaraCore.is_null(request.uniq):
            body['uniq'] = request.uniq
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotSpotUniqList',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/livetrace_proxy/hotspot_uniq_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotSpotUniqListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hot_spot_uniq_list(
        self,
        request: main_models.GetHotSpotUniqListRequest,
    ) -> main_models.GetHotSpotUniqListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_hot_spot_uniq_list_with_options(request, headers, runtime)

    async def get_hot_spot_uniq_list_async(
        self,
        request: main_models.GetHotSpotUniqListRequest,
    ) -> main_models.GetHotSpotUniqListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_hot_spot_uniq_list_with_options_async(request, headers, runtime)

    def get_hotfix_task_with_options(
        self,
        request: main_models.GetHotfixTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHotfixTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotfixTask',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/hotfix_manager/task/get',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotfixTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotfix_task_with_options_async(
        self,
        request: main_models.GetHotfixTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHotfixTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotfixTask',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/hotfix_manager/task/get',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotfixTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotfix_task(
        self,
        request: main_models.GetHotfixTaskRequest,
    ) -> main_models.GetHotfixTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_hotfix_task_with_options(request, headers, runtime)

    async def get_hotfix_task_async(
        self,
        request: main_models.GetHotfixTaskRequest,
    ) -> main_models.GetHotfixTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_hotfix_task_with_options_async(request, headers, runtime)

    def get_hotspot_analysis_with_options(
        self,
        request: main_models.GetHotspotAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHotspotAnalysisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_type):
            body['appType'] = request.app_type
        if not DaraCore.is_null(request.beg_end):
            body['beg_end'] = request.beg_end
        if not DaraCore.is_null(request.beg_start):
            body['beg_start'] = request.beg_start
        if not DaraCore.is_null(request.instance):
            body['instance'] = request.instance
        if not DaraCore.is_null(request.pid):
            body['pid'] = request.pid
        if not DaraCore.is_null(request.table):
            body['table'] = request.table
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotspotAnalysis',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/proxy/post/livetrace_hotspot_analysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotspotAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotspot_analysis_with_options_async(
        self,
        request: main_models.GetHotspotAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHotspotAnalysisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_type):
            body['appType'] = request.app_type
        if not DaraCore.is_null(request.beg_end):
            body['beg_end'] = request.beg_end
        if not DaraCore.is_null(request.beg_start):
            body['beg_start'] = request.beg_start
        if not DaraCore.is_null(request.instance):
            body['instance'] = request.instance
        if not DaraCore.is_null(request.pid):
            body['pid'] = request.pid
        if not DaraCore.is_null(request.table):
            body['table'] = request.table
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotspotAnalysis',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/proxy/post/livetrace_hotspot_analysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotspotAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotspot_analysis(
        self,
        request: main_models.GetHotspotAnalysisRequest,
    ) -> main_models.GetHotspotAnalysisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_hotspot_analysis_with_options(request, headers, runtime)

    async def get_hotspot_analysis_async(
        self,
        request: main_models.GetHotspotAnalysisRequest,
    ) -> main_models.GetHotspotAnalysisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_hotspot_analysis_with_options_async(request, headers, runtime)

    def get_hotspot_compare_with_options(
        self,
        request: main_models.GetHotspotCompareRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHotspotCompareResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.beg_1end):
            body['beg1_end'] = request.beg_1end
        if not DaraCore.is_null(request.beg_1start):
            body['beg1_start'] = request.beg_1start
        if not DaraCore.is_null(request.beg_2end):
            body['beg2_end'] = request.beg_2end
        if not DaraCore.is_null(request.beg_2start):
            body['beg2_start'] = request.beg_2start
        if not DaraCore.is_null(request.hot_type):
            body['hot_type'] = request.hot_type
        if not DaraCore.is_null(request.instance_1):
            body['instance1'] = request.instance_1
        if not DaraCore.is_null(request.instance_2):
            body['instance2'] = request.instance_2
        if not DaraCore.is_null(request.pid_1):
            body['pid1'] = request.pid_1
        if not DaraCore.is_null(request.pid_2):
            body['pid2'] = request.pid_2
        if not DaraCore.is_null(request.table):
            body['table'] = request.table
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotspotCompare',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/proxy/post/livetrace_hotspot_compare',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotspotCompareResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotspot_compare_with_options_async(
        self,
        request: main_models.GetHotspotCompareRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHotspotCompareResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.beg_1end):
            body['beg1_end'] = request.beg_1end
        if not DaraCore.is_null(request.beg_1start):
            body['beg1_start'] = request.beg_1start
        if not DaraCore.is_null(request.beg_2end):
            body['beg2_end'] = request.beg_2end
        if not DaraCore.is_null(request.beg_2start):
            body['beg2_start'] = request.beg_2start
        if not DaraCore.is_null(request.hot_type):
            body['hot_type'] = request.hot_type
        if not DaraCore.is_null(request.instance_1):
            body['instance1'] = request.instance_1
        if not DaraCore.is_null(request.instance_2):
            body['instance2'] = request.instance_2
        if not DaraCore.is_null(request.pid_1):
            body['pid1'] = request.pid_1
        if not DaraCore.is_null(request.pid_2):
            body['pid2'] = request.pid_2
        if not DaraCore.is_null(request.table):
            body['table'] = request.table
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotspotCompare',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/proxy/post/livetrace_hotspot_compare',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotspotCompareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotspot_compare(
        self,
        request: main_models.GetHotspotCompareRequest,
    ) -> main_models.GetHotspotCompareResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_hotspot_compare_with_options(request, headers, runtime)

    async def get_hotspot_compare_async(
        self,
        request: main_models.GetHotspotCompareRequest,
    ) -> main_models.GetHotspotCompareResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_hotspot_compare_with_options_async(request, headers, runtime)

    def get_hotspot_instance_list_with_options(
        self,
        request: main_models.GetHotspotInstanceListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHotspotInstanceListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.beg_end):
            body['beg_end'] = request.beg_end
        if not DaraCore.is_null(request.beg_start):
            body['beg_start'] = request.beg_start
        if not DaraCore.is_null(request.table):
            body['table'] = request.table
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotspotInstanceList',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/proxy/post/livetrace_hotspot_instance_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotspotInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotspot_instance_list_with_options_async(
        self,
        request: main_models.GetHotspotInstanceListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHotspotInstanceListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.beg_end):
            body['beg_end'] = request.beg_end
        if not DaraCore.is_null(request.beg_start):
            body['beg_start'] = request.beg_start
        if not DaraCore.is_null(request.table):
            body['table'] = request.table
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotspotInstanceList',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/proxy/post/livetrace_hotspot_instance_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotspotInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotspot_instance_list(
        self,
        request: main_models.GetHotspotInstanceListRequest,
    ) -> main_models.GetHotspotInstanceListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_hotspot_instance_list_with_options(request, headers, runtime)

    async def get_hotspot_instance_list_async(
        self,
        request: main_models.GetHotspotInstanceListRequest,
    ) -> main_models.GetHotspotInstanceListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_hotspot_instance_list_with_options_async(request, headers, runtime)

    def get_hotspot_pid_list_with_options(
        self,
        request: main_models.GetHotspotPidListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHotspotPidListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.beg_end):
            body['beg_end'] = request.beg_end
        if not DaraCore.is_null(request.beg_start):
            body['beg_start'] = request.beg_start
        if not DaraCore.is_null(request.instance):
            body['instance'] = request.instance
        if not DaraCore.is_null(request.table):
            body['table'] = request.table
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotspotPidList',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/proxy/post/livetrace_hotspot_pid_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotspotPidListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotspot_pid_list_with_options_async(
        self,
        request: main_models.GetHotspotPidListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHotspotPidListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.beg_end):
            body['beg_end'] = request.beg_end
        if not DaraCore.is_null(request.beg_start):
            body['beg_start'] = request.beg_start
        if not DaraCore.is_null(request.instance):
            body['instance'] = request.instance
        if not DaraCore.is_null(request.table):
            body['table'] = request.table
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotspotPidList',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/proxy/post/livetrace_hotspot_pid_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotspotPidListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotspot_pid_list(
        self,
        request: main_models.GetHotspotPidListRequest,
    ) -> main_models.GetHotspotPidListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_hotspot_pid_list_with_options(request, headers, runtime)

    async def get_hotspot_pid_list_async(
        self,
        request: main_models.GetHotspotPidListRequest,
    ) -> main_models.GetHotspotPidListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_hotspot_pid_list_with_options_async(request, headers, runtime)

    def get_hotspot_tracking_with_options(
        self,
        request: main_models.GetHotspotTrackingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHotspotTrackingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.beg_end):
            body['beg_end'] = request.beg_end
        if not DaraCore.is_null(request.beg_start):
            body['beg_start'] = request.beg_start
        if not DaraCore.is_null(request.hot_type):
            body['hot_type'] = request.hot_type
        if not DaraCore.is_null(request.instance):
            body['instance'] = request.instance
        if not DaraCore.is_null(request.pid):
            body['pid'] = request.pid
        if not DaraCore.is_null(request.table):
            body['table'] = request.table
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotspotTracking',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/proxy/post/livetrace_hotspot_tracking',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotspotTrackingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotspot_tracking_with_options_async(
        self,
        request: main_models.GetHotspotTrackingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHotspotTrackingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.beg_end):
            body['beg_end'] = request.beg_end
        if not DaraCore.is_null(request.beg_start):
            body['beg_start'] = request.beg_start
        if not DaraCore.is_null(request.hot_type):
            body['hot_type'] = request.hot_type
        if not DaraCore.is_null(request.instance):
            body['instance'] = request.instance
        if not DaraCore.is_null(request.pid):
            body['pid'] = request.pid
        if not DaraCore.is_null(request.table):
            body['table'] = request.table
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotspotTracking',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/proxy/post/livetrace_hotspot_tracking',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotspotTrackingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotspot_tracking(
        self,
        request: main_models.GetHotspotTrackingRequest,
    ) -> main_models.GetHotspotTrackingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_hotspot_tracking_with_options(request, headers, runtime)

    async def get_hotspot_tracking_async(
        self,
        request: main_models.GetHotspotTrackingRequest,
    ) -> main_models.GetHotspotTrackingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_hotspot_tracking_with_options_async(request, headers, runtime)

    def get_inspection_report_with_options(
        self,
        request: main_models.GetInspectionReportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInspectionReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.report_id):
            query['reportId'] = request.report_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInspectionReport',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/inspection/getInspectionReport',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInspectionReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_inspection_report_with_options_async(
        self,
        request: main_models.GetInspectionReportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInspectionReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.report_id):
            query['reportId'] = request.report_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInspectionReport',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/inspection/getInspectionReport',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInspectionReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_inspection_report(
        self,
        request: main_models.GetInspectionReportRequest,
    ) -> main_models.GetInspectionReportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_inspection_report_with_options(request, headers, runtime)

    async def get_inspection_report_async(
        self,
        request: main_models.GetInspectionReportRequest,
    ) -> main_models.GetInspectionReportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_inspection_report_with_options_async(request, headers, runtime)

    def get_instant_score_with_options(
        self,
        request: main_models.GetInstantScoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstantScoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster):
            query['cluster'] = request.cluster
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstantScore',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/cluster_health/instant/score',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstantScoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instant_score_with_options_async(
        self,
        request: main_models.GetInstantScoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstantScoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster):
            query['cluster'] = request.cluster
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstantScore',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/cluster_health/instant/score',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstantScoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instant_score(
        self,
        request: main_models.GetInstantScoreRequest,
    ) -> main_models.GetInstantScoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_instant_score_with_options(request, headers, runtime)

    async def get_instant_score_async(
        self,
        request: main_models.GetInstantScoreRequest,
    ) -> main_models.GetInstantScoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_instant_score_with_options_async(request, headers, runtime)

    def get_list_gpu_cluster_with_options(
        self,
        request: main_models.GetListGpuClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetListGpuClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.time_region):
            query['timeRegion'] = request.time_region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetListGpuCluster',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiTopology/topology/listCluster',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetListGpuClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_list_gpu_cluster_with_options_async(
        self,
        request: main_models.GetListGpuClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetListGpuClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.time_region):
            query['timeRegion'] = request.time_region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetListGpuCluster',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiTopology/topology/listCluster',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetListGpuClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_list_gpu_cluster(
        self,
        request: main_models.GetListGpuClusterRequest,
    ) -> main_models.GetListGpuClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_list_gpu_cluster_with_options(request, headers, runtime)

    async def get_list_gpu_cluster_async(
        self,
        request: main_models.GetListGpuClusterRequest,
    ) -> main_models.GetListGpuClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_list_gpu_cluster_with_options_async(request, headers, runtime)

    def get_list_record_with_options(
        self,
        request: main_models.GetListRecordRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetListRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.analysis_id):
            query['analysisId'] = request.analysis_id
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.custom_id):
            query['customId'] = request.custom_id
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetListRecord',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/app_observ/aiAnalysis/list_record',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetListRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_list_record_with_options_async(
        self,
        request: main_models.GetListRecordRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetListRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.analysis_id):
            query['analysisId'] = request.analysis_id
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.custom_id):
            query['customId'] = request.custom_id
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetListRecord',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/app_observ/aiAnalysis/list_record',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetListRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_list_record(
        self,
        request: main_models.GetListRecordRequest,
    ) -> main_models.GetListRecordResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_list_record_with_options(request, headers, runtime)

    async def get_list_record_async(
        self,
        request: main_models.GetListRecordRequest,
    ) -> main_models.GetListRecordResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_list_record_with_options_async(request, headers, runtime)

    def get_problem_percentage_with_options(
        self,
        request: main_models.GetProblemPercentageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProblemPercentageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster):
            query['cluster'] = request.cluster
        if not DaraCore.is_null(request.end):
            query['end'] = request.end
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.start):
            query['start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProblemPercentage',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/cluster_health/range/problem_percentage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProblemPercentageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_problem_percentage_with_options_async(
        self,
        request: main_models.GetProblemPercentageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProblemPercentageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster):
            query['cluster'] = request.cluster
        if not DaraCore.is_null(request.end):
            query['end'] = request.end
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.start):
            query['start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProblemPercentage',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/cluster_health/range/problem_percentage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProblemPercentageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_problem_percentage(
        self,
        request: main_models.GetProblemPercentageRequest,
    ) -> main_models.GetProblemPercentageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_problem_percentage_with_options(request, headers, runtime)

    async def get_problem_percentage_async(
        self,
        request: main_models.GetProblemPercentageRequest,
    ) -> main_models.GetProblemPercentageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_problem_percentage_with_options_async(request, headers, runtime)

    def get_range_score_with_options(
        self,
        request: main_models.GetRangeScoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRangeScoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster):
            query['cluster'] = request.cluster
        if not DaraCore.is_null(request.end):
            query['end'] = request.end
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.start):
            query['start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRangeScore',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/cluster_health/range/score',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRangeScoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_range_score_with_options_async(
        self,
        request: main_models.GetRangeScoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRangeScoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster):
            query['cluster'] = request.cluster
        if not DaraCore.is_null(request.end):
            query['end'] = request.end
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.start):
            query['start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRangeScore',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/cluster_health/range/score',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRangeScoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_range_score(
        self,
        request: main_models.GetRangeScoreRequest,
    ) -> main_models.GetRangeScoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_range_score_with_options(request, headers, runtime)

    async def get_range_score_async(
        self,
        request: main_models.GetRangeScoreRequest,
    ) -> main_models.GetRangeScoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_range_score_with_options_async(request, headers, runtime)

    def get_resources_with_options(
        self,
        request: main_models.GetResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster):
            query['cluster'] = request.cluster
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResources',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/cluster_health/instant/resource',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resources_with_options_async(
        self,
        request: main_models.GetResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster):
            query['cluster'] = request.cluster
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResources',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/cluster_health/instant/resource',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resources(
        self,
        request: main_models.GetResourcesRequest,
    ) -> main_models.GetResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_resources_with_options(request, headers, runtime)

    async def get_resources_async(
        self,
        request: main_models.GetResourcesRequest,
    ) -> main_models.GetResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_resources_with_options_async(request, headers, runtime)

    def get_service_func_status_with_options(
        self,
        tmp_req: main_models.GetServiceFuncStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceFuncStatusResponse:
        tmp_req.validate()
        request = main_models.GetServiceFuncStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'params', 'json')
        query = {}
        if not DaraCore.is_null(request.channel):
            query['channel'] = request.channel
        if not DaraCore.is_null(request.params_shrink):
            query['params'] = request.params_shrink
        if not DaraCore.is_null(request.service_name):
            query['service_name'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceFuncStatus',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/func-switch/get-service-func-status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceFuncStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_func_status_with_options_async(
        self,
        tmp_req: main_models.GetServiceFuncStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceFuncStatusResponse:
        tmp_req.validate()
        request = main_models.GetServiceFuncStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'params', 'json')
        query = {}
        if not DaraCore.is_null(request.channel):
            query['channel'] = request.channel
        if not DaraCore.is_null(request.params_shrink):
            query['params'] = request.params_shrink
        if not DaraCore.is_null(request.service_name):
            query['service_name'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceFuncStatus',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/func-switch/get-service-func-status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceFuncStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_func_status(
        self,
        request: main_models.GetServiceFuncStatusRequest,
    ) -> main_models.GetServiceFuncStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_service_func_status_with_options(request, headers, runtime)

    async def get_service_func_status_async(
        self,
        request: main_models.GetServiceFuncStatusRequest,
    ) -> main_models.GetServiceFuncStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_service_func_status_with_options_async(request, headers, runtime)

    def get_vmcore_diagnosis_task_with_options(
        self,
        request: main_models.GetVmcoreDiagnosisTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVmcoreDiagnosisTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVmcoreDiagnosisTask',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crashAgent/diagnosis/queryTask',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVmcoreDiagnosisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vmcore_diagnosis_task_with_options_async(
        self,
        request: main_models.GetVmcoreDiagnosisTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVmcoreDiagnosisTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVmcoreDiagnosisTask',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crashAgent/diagnosis/queryTask',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVmcoreDiagnosisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vmcore_diagnosis_task(
        self,
        request: main_models.GetVmcoreDiagnosisTaskRequest,
    ) -> main_models.GetVmcoreDiagnosisTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_vmcore_diagnosis_task_with_options(request, headers, runtime)

    async def get_vmcore_diagnosis_task_async(
        self,
        request: main_models.GetVmcoreDiagnosisTaskRequest,
    ) -> main_models.GetVmcoreDiagnosisTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_vmcore_diagnosis_task_with_options_async(request, headers, runtime)

    def initial_sysom_with_options(
        self,
        request: main_models.InitialSysomRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InitialSysomResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_only):
            body['check_only'] = request.check_only
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InitialSysom',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/initial',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitialSysomResponse(),
            self.call_api(params, req, runtime)
        )

    async def initial_sysom_with_options_async(
        self,
        request: main_models.InitialSysomRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InitialSysomResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_only):
            body['check_only'] = request.check_only
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InitialSysom',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/initial',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitialSysomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initial_sysom(
        self,
        request: main_models.InitialSysomRequest,
    ) -> main_models.InitialSysomResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.initial_sysom_with_options(request, headers, runtime)

    async def initial_sysom_async(
        self,
        request: main_models.InitialSysomRequest,
    ) -> main_models.InitialSysomResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.initial_sysom_with_options_async(request, headers, runtime)

    def install_agent_with_options(
        self,
        request: main_models.InstallAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agent_id'] = request.agent_id
        if not DaraCore.is_null(request.agent_version):
            body['agent_version'] = request.agent_version
        if not DaraCore.is_null(request.install_type):
            body['install_type'] = request.install_type
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InstallAgent',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/install_agent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_agent_with_options_async(
        self,
        request: main_models.InstallAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agent_id'] = request.agent_id
        if not DaraCore.is_null(request.agent_version):
            body['agent_version'] = request.agent_version
        if not DaraCore.is_null(request.install_type):
            body['install_type'] = request.install_type
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InstallAgent',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/install_agent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_agent(
        self,
        request: main_models.InstallAgentRequest,
    ) -> main_models.InstallAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.install_agent_with_options(request, headers, runtime)

    async def install_agent_async(
        self,
        request: main_models.InstallAgentRequest,
    ) -> main_models.InstallAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.install_agent_with_options_async(request, headers, runtime)

    def install_agent_for_cluster_with_options(
        self,
        request: main_models.InstallAgentForClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallAgentForClusterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agent_id'] = request.agent_id
        if not DaraCore.is_null(request.agent_version):
            body['agent_version'] = request.agent_version
        if not DaraCore.is_null(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.config_id):
            body['config_id'] = request.config_id
        if not DaraCore.is_null(request.grayscale_config):
            body['grayscale_config'] = request.grayscale_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InstallAgentForCluster',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/install_agent_by_cluster',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallAgentForClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_agent_for_cluster_with_options_async(
        self,
        request: main_models.InstallAgentForClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallAgentForClusterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agent_id'] = request.agent_id
        if not DaraCore.is_null(request.agent_version):
            body['agent_version'] = request.agent_version
        if not DaraCore.is_null(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.config_id):
            body['config_id'] = request.config_id
        if not DaraCore.is_null(request.grayscale_config):
            body['grayscale_config'] = request.grayscale_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InstallAgentForCluster',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/install_agent_by_cluster',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallAgentForClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_agent_for_cluster(
        self,
        request: main_models.InstallAgentForClusterRequest,
    ) -> main_models.InstallAgentForClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.install_agent_for_cluster_with_options(request, headers, runtime)

    async def install_agent_for_cluster_async(
        self,
        request: main_models.InstallAgentForClusterRequest,
    ) -> main_models.InstallAgentForClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.install_agent_for_cluster_with_options_async(request, headers, runtime)

    def install_agent_with_type_with_options(
        self,
        request: main_models.InstallAgentWithTypeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallAgentWithTypeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_version):
            body['agentVersion'] = request.agent_version
        if not DaraCore.is_null(request.config_id):
            body['configId'] = request.config_id
        if not DaraCore.is_null(request.instance_type):
            body['instanceType'] = request.instance_type
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InstallAgentWithType',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/installAgent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallAgentWithTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_agent_with_type_with_options_async(
        self,
        request: main_models.InstallAgentWithTypeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallAgentWithTypeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_version):
            body['agentVersion'] = request.agent_version
        if not DaraCore.is_null(request.config_id):
            body['configId'] = request.config_id
        if not DaraCore.is_null(request.instance_type):
            body['instanceType'] = request.instance_type
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InstallAgentWithType',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/installAgent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallAgentWithTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_agent_with_type(
        self,
        request: main_models.InstallAgentWithTypeRequest,
    ) -> main_models.InstallAgentWithTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.install_agent_with_type_with_options(request, headers, runtime)

    async def install_agent_with_type_async(
        self,
        request: main_models.InstallAgentWithTypeRequest,
    ) -> main_models.InstallAgentWithTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.install_agent_with_type_with_options_async(request, headers, runtime)

    def install_hotfix_with_options(
        self,
        request: main_models.InstallHotfixRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallHotfixResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cve_id):
            body['cveId'] = request.cve_id
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InstallHotfix',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/hotfix_manager/hotfix/install',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallHotfixResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_hotfix_with_options_async(
        self,
        request: main_models.InstallHotfixRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallHotfixResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cve_id):
            body['cveId'] = request.cve_id
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InstallHotfix',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/hotfix_manager/hotfix/install',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallHotfixResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_hotfix(
        self,
        request: main_models.InstallHotfixRequest,
    ) -> main_models.InstallHotfixResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.install_hotfix_with_options(request, headers, runtime)

    async def install_hotfix_async(
        self,
        request: main_models.InstallHotfixRequest,
    ) -> main_models.InstallHotfixResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.install_hotfix_with_options_async(request, headers, runtime)

    def invoke_anomaly_diagnosis_with_options(
        self,
        request: main_models.InvokeAnomalyDiagnosisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InvokeAnomalyDiagnosisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.uuid):
            query['uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InvokeAnomalyDiagnosis',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/cluster_health/diagnosis/invoke_anomaly_diagnose',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvokeAnomalyDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoke_anomaly_diagnosis_with_options_async(
        self,
        request: main_models.InvokeAnomalyDiagnosisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InvokeAnomalyDiagnosisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.uuid):
            query['uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InvokeAnomalyDiagnosis',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/cluster_health/diagnosis/invoke_anomaly_diagnose',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvokeAnomalyDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invoke_anomaly_diagnosis(
        self,
        request: main_models.InvokeAnomalyDiagnosisRequest,
    ) -> main_models.InvokeAnomalyDiagnosisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.invoke_anomaly_diagnosis_with_options(request, headers, runtime)

    async def invoke_anomaly_diagnosis_async(
        self,
        request: main_models.InvokeAnomalyDiagnosisRequest,
    ) -> main_models.InvokeAnomalyDiagnosisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.invoke_anomaly_diagnosis_with_options_async(request, headers, runtime)

    def invoke_diagnosis_with_options(
        self,
        request: main_models.InvokeDiagnosisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InvokeDiagnosisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channel):
            body['channel'] = request.channel
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        if not DaraCore.is_null(request.service_name):
            body['service_name'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InvokeDiagnosis',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/diagnosis/invoke_diagnosis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvokeDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoke_diagnosis_with_options_async(
        self,
        request: main_models.InvokeDiagnosisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InvokeDiagnosisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channel):
            body['channel'] = request.channel
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        if not DaraCore.is_null(request.service_name):
            body['service_name'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InvokeDiagnosis',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/diagnosis/invoke_diagnosis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvokeDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invoke_diagnosis(
        self,
        request: main_models.InvokeDiagnosisRequest,
    ) -> main_models.InvokeDiagnosisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.invoke_diagnosis_with_options(request, headers, runtime)

    async def invoke_diagnosis_async(
        self,
        request: main_models.InvokeDiagnosisRequest,
    ) -> main_models.InvokeDiagnosisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.invoke_diagnosis_with_options_async(request, headers, runtime)

    def list_abnormaly_events_with_options(
        self,
        request: main_models.ListAbnormalyEventsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAbnormalyEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster):
            query['cluster'] = request.cluster
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.end):
            query['end'] = request.end
        if not DaraCore.is_null(request.event):
            query['event'] = request.event
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.level):
            query['level'] = request.level
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.pod):
            query['pod'] = request.pod
        if not DaraCore.is_null(request.show_pod):
            query['showPod'] = request.show_pod
        if not DaraCore.is_null(request.start):
            query['start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAbnormalyEvents',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/cluster_health/range/abnormaly_events',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAbnormalyEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_abnormaly_events_with_options_async(
        self,
        request: main_models.ListAbnormalyEventsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAbnormalyEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster):
            query['cluster'] = request.cluster
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.end):
            query['end'] = request.end
        if not DaraCore.is_null(request.event):
            query['event'] = request.event
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.level):
            query['level'] = request.level
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.pod):
            query['pod'] = request.pod
        if not DaraCore.is_null(request.show_pod):
            query['showPod'] = request.show_pod
        if not DaraCore.is_null(request.start):
            query['start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAbnormalyEvents',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/cluster_health/range/abnormaly_events',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAbnormalyEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_abnormaly_events(
        self,
        request: main_models.ListAbnormalyEventsRequest,
    ) -> main_models.ListAbnormalyEventsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_abnormaly_events_with_options(request, headers, runtime)

    async def list_abnormaly_events_async(
        self,
        request: main_models.ListAbnormalyEventsRequest,
    ) -> main_models.ListAbnormalyEventsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_abnormaly_events_with_options_async(request, headers, runtime)

    def list_agent_install_records_with_options(
        self,
        request: main_models.ListAgentInstallRecordsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentInstallRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.instance_id):
            query['instance_id'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.plugin_id):
            query['plugin_id'] = request.plugin_id
        if not DaraCore.is_null(request.plugin_version):
            query['plugin_version'] = request.plugin_version
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentInstallRecords',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/list_agent_install_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentInstallRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_install_records_with_options_async(
        self,
        request: main_models.ListAgentInstallRecordsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentInstallRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.instance_id):
            query['instance_id'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.plugin_id):
            query['plugin_id'] = request.plugin_id
        if not DaraCore.is_null(request.plugin_version):
            query['plugin_version'] = request.plugin_version
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentInstallRecords',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/list_agent_install_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentInstallRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_install_records(
        self,
        request: main_models.ListAgentInstallRecordsRequest,
    ) -> main_models.ListAgentInstallRecordsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_agent_install_records_with_options(request, headers, runtime)

    async def list_agent_install_records_async(
        self,
        request: main_models.ListAgentInstallRecordsRequest,
    ) -> main_models.ListAgentInstallRecordsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_agent_install_records_with_options_async(request, headers, runtime)

    def list_agents_with_options(
        self,
        request: main_models.ListAgentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgents',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/list_agents',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agents_with_options_async(
        self,
        request: main_models.ListAgentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgents',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/list_agents',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agents(
        self,
        request: main_models.ListAgentsRequest,
    ) -> main_models.ListAgentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_agents_with_options(request, headers, runtime)

    async def list_agents_async(
        self,
        request: main_models.ListAgentsRequest,
    ) -> main_models.ListAgentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_agents_with_options_async(request, headers, runtime)

    def list_aifg_jobs_with_options(
        self,
        request: main_models.ListAifgJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAifgJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.service_name):
            query['serviceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAifgJobs',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aifg/listAifgJobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAifgJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aifg_jobs_with_options_async(
        self,
        request: main_models.ListAifgJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAifgJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.service_name):
            query['serviceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAifgJobs',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aifg/listAifgJobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAifgJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aifg_jobs(
        self,
        request: main_models.ListAifgJobsRequest,
    ) -> main_models.ListAifgJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_aifg_jobs_with_options(request, headers, runtime)

    async def list_aifg_jobs_async(
        self,
        request: main_models.ListAifgJobsRequest,
    ) -> main_models.ListAifgJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_aifg_jobs_with_options_async(request, headers, runtime)

    def list_alert_destinations_with_options(
        self,
        request: main_models.ListAlertDestinationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAlertDestinationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlertDestinations',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/listDestinations',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlertDestinationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alert_destinations_with_options_async(
        self,
        request: main_models.ListAlertDestinationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAlertDestinationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlertDestinations',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/listDestinations',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlertDestinationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alert_destinations(
        self,
        request: main_models.ListAlertDestinationsRequest,
    ) -> main_models.ListAlertDestinationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_alert_destinations_with_options(request, headers, runtime)

    async def list_alert_destinations_async(
        self,
        request: main_models.ListAlertDestinationsRequest,
    ) -> main_models.ListAlertDestinationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_alert_destinations_with_options_async(request, headers, runtime)

    def list_alert_items_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAlertItemsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListAlertItems',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/listItems',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlertItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alert_items_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAlertItemsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListAlertItems',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/listItems',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlertItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alert_items(self) -> main_models.ListAlertItemsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_alert_items_with_options(headers, runtime)

    async def list_alert_items_async(self) -> main_models.ListAlertItemsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_alert_items_with_options_async(headers, runtime)

    def list_alert_strategies_with_options(
        self,
        request: main_models.ListAlertStrategiesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAlertStrategiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlertStrategies',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/listStrategies',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlertStrategiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alert_strategies_with_options_async(
        self,
        request: main_models.ListAlertStrategiesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAlertStrategiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlertStrategies',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/listStrategies',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlertStrategiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alert_strategies(
        self,
        request: main_models.ListAlertStrategiesRequest,
    ) -> main_models.ListAlertStrategiesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_alert_strategies_with_options(request, headers, runtime)

    async def list_alert_strategies_async(
        self,
        request: main_models.ListAlertStrategiesRequest,
    ) -> main_models.ListAlertStrategiesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_alert_strategies_with_options_async(request, headers, runtime)

    def list_all_instances_with_options(
        self,
        request: main_models.ListAllInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAllInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.filters):
            query['filters'] = request.filters
        if not DaraCore.is_null(request.instance_type):
            query['instanceType'] = request.instance_type
        if not DaraCore.is_null(request.managed_type):
            query['managedType'] = request.managed_type
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.plugin_id):
            query['pluginId'] = request.plugin_id
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAllInstances',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/instance/listAllInstances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAllInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_instances_with_options_async(
        self,
        request: main_models.ListAllInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAllInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.filters):
            query['filters'] = request.filters
        if not DaraCore.is_null(request.instance_type):
            query['instanceType'] = request.instance_type
        if not DaraCore.is_null(request.managed_type):
            query['managedType'] = request.managed_type
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.plugin_id):
            query['pluginId'] = request.plugin_id
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAllInstances',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/instance/listAllInstances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAllInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_instances(
        self,
        request: main_models.ListAllInstancesRequest,
    ) -> main_models.ListAllInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_all_instances_with_options(request, headers, runtime)

    async def list_all_instances_async(
        self,
        request: main_models.ListAllInstancesRequest,
    ) -> main_models.ListAllInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_all_instances_with_options_async(request, headers, runtime)

    def list_cluster_agent_install_records_with_options(
        self,
        request: main_models.ListClusterAgentInstallRecordsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterAgentInstallRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_config_id):
            query['agent_config_id'] = request.agent_config_id
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.plugin_id):
            query['plugin_id'] = request.plugin_id
        if not DaraCore.is_null(request.plugin_version):
            query['plugin_version'] = request.plugin_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterAgentInstallRecords',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/list_cluster_agent_install_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterAgentInstallRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_agent_install_records_with_options_async(
        self,
        request: main_models.ListClusterAgentInstallRecordsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterAgentInstallRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_config_id):
            query['agent_config_id'] = request.agent_config_id
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.plugin_id):
            query['plugin_id'] = request.plugin_id
        if not DaraCore.is_null(request.plugin_version):
            query['plugin_version'] = request.plugin_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterAgentInstallRecords',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/list_cluster_agent_install_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterAgentInstallRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_agent_install_records(
        self,
        request: main_models.ListClusterAgentInstallRecordsRequest,
    ) -> main_models.ListClusterAgentInstallRecordsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_cluster_agent_install_records_with_options(request, headers, runtime)

    async def list_cluster_agent_install_records_async(
        self,
        request: main_models.ListClusterAgentInstallRecordsRequest,
    ) -> main_models.ListClusterAgentInstallRecordsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_cluster_agent_install_records_with_options_async(request, headers, runtime)

    def list_clusters_with_options(
        self,
        request: main_models.ListClustersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_status):
            query['cluster_status'] = request.cluster_status
        if not DaraCore.is_null(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusters',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/cluster/list_clusters',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        request: main_models.ListClustersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_status):
            query['cluster_status'] = request.cluster_status
        if not DaraCore.is_null(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusters',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/cluster/list_clusters',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_clusters(
        self,
        request: main_models.ListClustersRequest,
    ) -> main_models.ListClustersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_clusters_with_options(request, headers, runtime)

    async def list_clusters_async(
        self,
        request: main_models.ListClustersRequest,
    ) -> main_models.ListClustersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_clusters_with_options_async(request, headers, runtime)

    def list_diagnosis_with_options(
        self,
        request: main_models.ListDiagnosisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDiagnosisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.params):
            query['params'] = request.params
        if not DaraCore.is_null(request.service_name):
            query['service_name'] = request.service_name
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDiagnosis',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/diagnosis/list_diagnosis',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_diagnosis_with_options_async(
        self,
        request: main_models.ListDiagnosisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDiagnosisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.params):
            query['params'] = request.params
        if not DaraCore.is_null(request.service_name):
            query['service_name'] = request.service_name
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDiagnosis',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/diagnosis/list_diagnosis',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_diagnosis(
        self,
        request: main_models.ListDiagnosisRequest,
    ) -> main_models.ListDiagnosisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_diagnosis_with_options(request, headers, runtime)

    async def list_diagnosis_async(
        self,
        request: main_models.ListDiagnosisRequest,
    ) -> main_models.ListDiagnosisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_diagnosis_with_options_async(request, headers, runtime)

    def list_instance_health_with_options(
        self,
        request: main_models.ListInstanceHealthRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceHealthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster):
            query['cluster'] = request.cluster
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.end):
            query['end'] = request.end
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start):
            query['start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceHealth',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/cluster_health/range/instance_health_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceHealthResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_health_with_options_async(
        self,
        request: main_models.ListInstanceHealthRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceHealthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster):
            query['cluster'] = request.cluster
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.end):
            query['end'] = request.end
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start):
            query['start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceHealth',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/cluster_health/range/instance_health_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceHealthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_health(
        self,
        request: main_models.ListInstanceHealthRequest,
    ) -> main_models.ListInstanceHealthResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_instance_health_with_options(request, headers, runtime)

    async def list_instance_health_async(
        self,
        request: main_models.ListInstanceHealthRequest,
    ) -> main_models.ListInstanceHealthResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_instance_health_with_options_async(request, headers, runtime)

    def list_instance_info_with_options(
        self,
        request: main_models.ListInstanceInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.info_type):
            query['infoType'] = request.info_type
        if not DaraCore.is_null(request.instance_type):
            query['instanceType'] = request.instance_type
        if not DaraCore.is_null(request.managed_type):
            query['managedType'] = request.managed_type
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.plugin_id):
            query['pluginId'] = request.plugin_id
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceInfo',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/instance/listInstanceInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_info_with_options_async(
        self,
        request: main_models.ListInstanceInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.info_type):
            query['infoType'] = request.info_type
        if not DaraCore.is_null(request.instance_type):
            query['instanceType'] = request.instance_type
        if not DaraCore.is_null(request.managed_type):
            query['managedType'] = request.managed_type
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.plugin_id):
            query['pluginId'] = request.plugin_id
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceInfo',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/instance/listInstanceInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_info(
        self,
        request: main_models.ListInstanceInfoRequest,
    ) -> main_models.ListInstanceInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_instance_info_with_options(request, headers, runtime)

    async def list_instance_info_async(
        self,
        request: main_models.ListInstanceInfoRequest,
    ) -> main_models.ListInstanceInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_instance_info_with_options_async(request, headers, runtime)

    def list_instance_status_with_options(
        self,
        request: main_models.ListInstanceStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceStatus',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/instance/list_instance_status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_status_with_options_async(
        self,
        request: main_models.ListInstanceStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceStatus',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/instance/list_instance_status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_status(
        self,
        request: main_models.ListInstanceStatusRequest,
    ) -> main_models.ListInstanceStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_instance_status_with_options(request, headers, runtime)

    async def list_instance_status_async(
        self,
        request: main_models.ListInstanceStatusRequest,
    ) -> main_models.ListInstanceStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_instance_status_with_options_async(request, headers, runtime)

    def list_instances_with_options(
        self,
        request: main_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/instance/list_instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: main_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/instance/list_instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def list_instances_ecs_info_list_with_options(
        self,
        request: main_models.ListInstancesEcsInfoListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesEcsInfoListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.info_type):
            query['info_type'] = request.info_type
        if not DaraCore.is_null(request.instance_id):
            query['instance_id'] = request.instance_id
        if not DaraCore.is_null(request.managed_type):
            query['managed_type'] = request.managed_type
        if not DaraCore.is_null(request.plugin_id):
            query['plugin_id'] = request.plugin_id
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstancesEcsInfoList',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/instance/listInstancesEcsInfoList',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesEcsInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_ecs_info_list_with_options_async(
        self,
        request: main_models.ListInstancesEcsInfoListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesEcsInfoListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.info_type):
            query['info_type'] = request.info_type
        if not DaraCore.is_null(request.instance_id):
            query['instance_id'] = request.instance_id
        if not DaraCore.is_null(request.managed_type):
            query['managed_type'] = request.managed_type
        if not DaraCore.is_null(request.plugin_id):
            query['plugin_id'] = request.plugin_id
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstancesEcsInfoList',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/instance/listInstancesEcsInfoList',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesEcsInfoListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances_ecs_info_list(
        self,
        request: main_models.ListInstancesEcsInfoListRequest,
    ) -> main_models.ListInstancesEcsInfoListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_instances_ecs_info_list_with_options(request, headers, runtime)

    async def list_instances_ecs_info_list_async(
        self,
        request: main_models.ListInstancesEcsInfoListRequest,
    ) -> main_models.ListInstancesEcsInfoListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_instances_ecs_info_list_with_options_async(request, headers, runtime)

    def list_instances_with_ecs_info_with_options(
        self,
        tmp_req: main_models.ListInstancesWithEcsInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesWithEcsInfoResponse:
        tmp_req.validate()
        request = main_models.ListInstancesWithEcsInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_tag):
            request.instance_tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_tag, 'instance_tag', 'json')
        query = {}
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.health_status):
            query['health_status'] = request.health_status
        if not DaraCore.is_null(request.instance_id):
            query['instance_id'] = request.instance_id
        if not DaraCore.is_null(request.instance_id_name):
            query['instance_id_name'] = request.instance_id_name
        if not DaraCore.is_null(request.instance_name):
            query['instance_name'] = request.instance_name
        if not DaraCore.is_null(request.instance_tag_shrink):
            query['instance_tag'] = request.instance_tag_shrink
        if not DaraCore.is_null(request.is_managed):
            query['is_managed'] = request.is_managed
        if not DaraCore.is_null(request.os_name):
            query['os_name'] = request.os_name
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.private_ip):
            query['private_ip'] = request.private_ip
        if not DaraCore.is_null(request.public_ip):
            query['public_ip'] = request.public_ip
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.resource_group_id):
            query['resource_group_id'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_group_id_name):
            query['resource_group_id_name'] = request.resource_group_id_name
        if not DaraCore.is_null(request.resource_group_name):
            query['resource_group_name'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstancesWithEcsInfo',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/instance/listInstancesWithEcsInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesWithEcsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_ecs_info_with_options_async(
        self,
        tmp_req: main_models.ListInstancesWithEcsInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesWithEcsInfoResponse:
        tmp_req.validate()
        request = main_models.ListInstancesWithEcsInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_tag):
            request.instance_tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_tag, 'instance_tag', 'json')
        query = {}
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.health_status):
            query['health_status'] = request.health_status
        if not DaraCore.is_null(request.instance_id):
            query['instance_id'] = request.instance_id
        if not DaraCore.is_null(request.instance_id_name):
            query['instance_id_name'] = request.instance_id_name
        if not DaraCore.is_null(request.instance_name):
            query['instance_name'] = request.instance_name
        if not DaraCore.is_null(request.instance_tag_shrink):
            query['instance_tag'] = request.instance_tag_shrink
        if not DaraCore.is_null(request.is_managed):
            query['is_managed'] = request.is_managed
        if not DaraCore.is_null(request.os_name):
            query['os_name'] = request.os_name
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.private_ip):
            query['private_ip'] = request.private_ip
        if not DaraCore.is_null(request.public_ip):
            query['public_ip'] = request.public_ip
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.resource_group_id):
            query['resource_group_id'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_group_id_name):
            query['resource_group_id_name'] = request.resource_group_id_name
        if not DaraCore.is_null(request.resource_group_name):
            query['resource_group_name'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstancesWithEcsInfo',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/instance/listInstancesWithEcsInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesWithEcsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances_with_ecs_info(
        self,
        request: main_models.ListInstancesWithEcsInfoRequest,
    ) -> main_models.ListInstancesWithEcsInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_instances_with_ecs_info_with_options(request, headers, runtime)

    async def list_instances_with_ecs_info_async(
        self,
        request: main_models.ListInstancesWithEcsInfoRequest,
    ) -> main_models.ListInstancesWithEcsInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_instances_with_ecs_info_with_options_async(request, headers, runtime)

    def list_plugins_instances_with_options(
        self,
        request: main_models.ListPluginsInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPluginsInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.instance_id_name):
            query['instance_id_name'] = request.instance_id_name
        if not DaraCore.is_null(request.instance_tag):
            query['instance_tag'] = request.instance_tag
        if not DaraCore.is_null(request.operation_type):
            query['operation_type'] = request.operation_type
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.plugin_id):
            query['plugin_id'] = request.plugin_id
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPluginsInstances',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/listPluginsInstances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPluginsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_plugins_instances_with_options_async(
        self,
        request: main_models.ListPluginsInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPluginsInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.instance_id_name):
            query['instance_id_name'] = request.instance_id_name
        if not DaraCore.is_null(request.instance_tag):
            query['instance_tag'] = request.instance_tag
        if not DaraCore.is_null(request.operation_type):
            query['operation_type'] = request.operation_type
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.plugin_id):
            query['plugin_id'] = request.plugin_id
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPluginsInstances',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/listPluginsInstances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPluginsInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_plugins_instances(
        self,
        request: main_models.ListPluginsInstancesRequest,
    ) -> main_models.ListPluginsInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_plugins_instances_with_options(request, headers, runtime)

    async def list_plugins_instances_async(
        self,
        request: main_models.ListPluginsInstancesRequest,
    ) -> main_models.ListPluginsInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_plugins_instances_with_options_async(request, headers, runtime)

    def list_pods_of_instance_with_options(
        self,
        request: main_models.ListPodsOfInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPodsOfInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPodsOfInstance',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/instance/list_pod_of_instance',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPodsOfInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pods_of_instance_with_options_async(
        self,
        request: main_models.ListPodsOfInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPodsOfInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.current):
            query['current'] = request.current
        if not DaraCore.is_null(request.instance):
            query['instance'] = request.instance
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPodsOfInstance',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/instance/list_pod_of_instance',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPodsOfInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pods_of_instance(
        self,
        request: main_models.ListPodsOfInstanceRequest,
    ) -> main_models.ListPodsOfInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_pods_of_instance_with_options(request, headers, runtime)

    async def list_pods_of_instance_async(
        self,
        request: main_models.ListPodsOfInstanceRequest,
    ) -> main_models.ListPodsOfInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_pods_of_instance_with_options_async(request, headers, runtime)

    def list_regions_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRegionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListRegions',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/instance/list_regions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRegionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListRegions',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/instance/list_regions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(self) -> main_models.ListRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_regions_with_options(headers, runtime)

    async def list_regions_async(self) -> main_models.ListRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_regions_with_options_async(headers, runtime)

    def list_vmcore_diagnosis_task_with_options(
        self,
        request: main_models.ListVmcoreDiagnosisTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListVmcoreDiagnosisTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.days):
            query['days'] = request.days
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVmcoreDiagnosisTask',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crashAgent/diagnosis/queryTaskList',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVmcoreDiagnosisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vmcore_diagnosis_task_with_options_async(
        self,
        request: main_models.ListVmcoreDiagnosisTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListVmcoreDiagnosisTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.days):
            query['days'] = request.days
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVmcoreDiagnosisTask',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crashAgent/diagnosis/queryTaskList',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVmcoreDiagnosisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vmcore_diagnosis_task(
        self,
        request: main_models.ListVmcoreDiagnosisTaskRequest,
    ) -> main_models.ListVmcoreDiagnosisTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_vmcore_diagnosis_task_with_options(request, headers, runtime)

    async def list_vmcore_diagnosis_task_async(
        self,
        request: main_models.ListVmcoreDiagnosisTaskRequest,
    ) -> main_models.ListVmcoreDiagnosisTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_vmcore_diagnosis_task_with_options_async(request, headers, runtime)

    def query_hotfix_status_with_options(
        self,
        request: main_models.QueryHotfixStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryHotfixStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cve_id):
            body['cveId'] = request.cve_id
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryHotfixStatus',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/hotfix_manager/hotfix/query_status',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryHotfixStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_hotfix_status_with_options_async(
        self,
        request: main_models.QueryHotfixStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryHotfixStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cve_id):
            body['cveId'] = request.cve_id
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryHotfixStatus',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/hotfix_manager/hotfix/query_status',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryHotfixStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_hotfix_status(
        self,
        request: main_models.QueryHotfixStatusRequest,
    ) -> main_models.QueryHotfixStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_hotfix_status_with_options(request, headers, runtime)

    async def query_hotfix_status_async(
        self,
        request: main_models.QueryHotfixStatusRequest,
    ) -> main_models.QueryHotfixStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_hotfix_status_with_options_async(request, headers, runtime)

    def start_aianalysis_with_options(
        self,
        request: main_models.StartAIAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartAIAnalysisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.analysis_tool):
            body['analysisTool'] = request.analysis_tool
        if not DaraCore.is_null(request.analysis_params):
            body['analysis_params'] = request.analysis_params
        if not DaraCore.is_null(request.channel):
            body['channel'] = request.channel
        if not DaraCore.is_null(request.comms):
            body['comms'] = request.comms
        if not DaraCore.is_null(request.created_by):
            body['created_by'] = request.created_by
        if not DaraCore.is_null(request.instance):
            body['instance'] = request.instance
        if not DaraCore.is_null(request.instance_type):
            body['instance_type'] = request.instance_type
        if not DaraCore.is_null(request.iteration_func):
            body['iteration_func'] = request.iteration_func
        if not DaraCore.is_null(request.iteration_mod):
            body['iteration_mod'] = request.iteration_mod
        if not DaraCore.is_null(request.iteration_range):
            body['iteration_range'] = request.iteration_range
        if not DaraCore.is_null(request.pids):
            body['pids'] = request.pids
        if not DaraCore.is_null(request.region):
            body['region'] = request.region
        if not DaraCore.is_null(request.timeout):
            body['timeout'] = request.timeout
        if not DaraCore.is_null(request.uid):
            body['uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartAIAnalysis',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/proxy/post/start_ai_analysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAIAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_aianalysis_with_options_async(
        self,
        request: main_models.StartAIAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartAIAnalysisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.analysis_tool):
            body['analysisTool'] = request.analysis_tool
        if not DaraCore.is_null(request.analysis_params):
            body['analysis_params'] = request.analysis_params
        if not DaraCore.is_null(request.channel):
            body['channel'] = request.channel
        if not DaraCore.is_null(request.comms):
            body['comms'] = request.comms
        if not DaraCore.is_null(request.created_by):
            body['created_by'] = request.created_by
        if not DaraCore.is_null(request.instance):
            body['instance'] = request.instance
        if not DaraCore.is_null(request.instance_type):
            body['instance_type'] = request.instance_type
        if not DaraCore.is_null(request.iteration_func):
            body['iteration_func'] = request.iteration_func
        if not DaraCore.is_null(request.iteration_mod):
            body['iteration_mod'] = request.iteration_mod
        if not DaraCore.is_null(request.iteration_range):
            body['iteration_range'] = request.iteration_range
        if not DaraCore.is_null(request.pids):
            body['pids'] = request.pids
        if not DaraCore.is_null(request.region):
            body['region'] = request.region
        if not DaraCore.is_null(request.timeout):
            body['timeout'] = request.timeout
        if not DaraCore.is_null(request.uid):
            body['uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartAIAnalysis',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/proxy/post/start_ai_analysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAIAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_aianalysis(
        self,
        request: main_models.StartAIAnalysisRequest,
    ) -> main_models.StartAIAnalysisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_aianalysis_with_options(request, headers, runtime)

    async def start_aianalysis_async(
        self,
        request: main_models.StartAIAnalysisRequest,
    ) -> main_models.StartAIAnalysisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_aianalysis_with_options_async(request, headers, runtime)

    def start_aidiff_analysis_with_options(
        self,
        request: main_models.StartAIDiffAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartAIDiffAnalysisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_1):
            body['task1'] = request.task_1
        if not DaraCore.is_null(request.task_2):
            body['task2'] = request.task_2
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartAIDiffAnalysis',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/appObserv/aiAnalysis/diffAnalysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAIDiffAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_aidiff_analysis_with_options_async(
        self,
        request: main_models.StartAIDiffAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartAIDiffAnalysisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_1):
            body['task1'] = request.task_1
        if not DaraCore.is_null(request.task_2):
            body['task2'] = request.task_2
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartAIDiffAnalysis',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/appObserv/aiAnalysis/diffAnalysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAIDiffAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_aidiff_analysis(
        self,
        request: main_models.StartAIDiffAnalysisRequest,
    ) -> main_models.StartAIDiffAnalysisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_aidiff_analysis_with_options(request, headers, runtime)

    async def start_aidiff_analysis_async(
        self,
        request: main_models.StartAIDiffAnalysisRequest,
    ) -> main_models.StartAIDiffAnalysisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_aidiff_analysis_with_options_async(request, headers, runtime)

    def start_aifg_analysis_with_options(
        self,
        request: main_models.StartAifgAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartAifgAnalysisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channel):
            body['channel'] = request.channel
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        if not DaraCore.is_null(request.region):
            body['region'] = request.region
        if not DaraCore.is_null(request.service_name):
            body['serviceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartAifgAnalysis',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aifg/startAifgAnalysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAifgAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_aifg_analysis_with_options_async(
        self,
        request: main_models.StartAifgAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartAifgAnalysisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channel):
            body['channel'] = request.channel
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        if not DaraCore.is_null(request.region):
            body['region'] = request.region
        if not DaraCore.is_null(request.service_name):
            body['serviceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartAifgAnalysis',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aifg/startAifgAnalysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAifgAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_aifg_analysis(
        self,
        request: main_models.StartAifgAnalysisRequest,
    ) -> main_models.StartAifgAnalysisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_aifg_analysis_with_options(request, headers, runtime)

    async def start_aifg_analysis_async(
        self,
        request: main_models.StartAifgAnalysisRequest,
    ) -> main_models.StartAifgAnalysisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_aifg_analysis_with_options_async(request, headers, runtime)

    def uninstall_agent_with_options(
        self,
        request: main_models.UninstallAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UninstallAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agent_id'] = request.agent_id
        if not DaraCore.is_null(request.agent_version):
            body['agent_version'] = request.agent_version
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UninstallAgent',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/uninstall_agent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_agent_with_options_async(
        self,
        request: main_models.UninstallAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UninstallAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agent_id'] = request.agent_id
        if not DaraCore.is_null(request.agent_version):
            body['agent_version'] = request.agent_version
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UninstallAgent',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/uninstall_agent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_agent(
        self,
        request: main_models.UninstallAgentRequest,
    ) -> main_models.UninstallAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.uninstall_agent_with_options(request, headers, runtime)

    async def uninstall_agent_async(
        self,
        request: main_models.UninstallAgentRequest,
    ) -> main_models.UninstallAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.uninstall_agent_with_options_async(request, headers, runtime)

    def uninstall_agent_for_cluster_with_options(
        self,
        request: main_models.UninstallAgentForClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UninstallAgentForClusterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agent_id'] = request.agent_id
        if not DaraCore.is_null(request.agent_version):
            body['agent_version'] = request.agent_version
        if not DaraCore.is_null(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UninstallAgentForCluster',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/uninstall_agent_by_cluster',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallAgentForClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_agent_for_cluster_with_options_async(
        self,
        request: main_models.UninstallAgentForClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UninstallAgentForClusterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agent_id'] = request.agent_id
        if not DaraCore.is_null(request.agent_version):
            body['agent_version'] = request.agent_version
        if not DaraCore.is_null(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UninstallAgentForCluster',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/uninstall_agent_by_cluster',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallAgentForClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_agent_for_cluster(
        self,
        request: main_models.UninstallAgentForClusterRequest,
    ) -> main_models.UninstallAgentForClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.uninstall_agent_for_cluster_with_options(request, headers, runtime)

    async def uninstall_agent_for_cluster_async(
        self,
        request: main_models.UninstallAgentForClusterRequest,
    ) -> main_models.UninstallAgentForClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.uninstall_agent_for_cluster_with_options_async(request, headers, runtime)

    def uninstall_agent_with_type_with_options(
        self,
        request: main_models.UninstallAgentWithTypeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UninstallAgentWithTypeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_version):
            body['agentVersion'] = request.agent_version
        if not DaraCore.is_null(request.instance_type):
            body['instanceType'] = request.instance_type
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UninstallAgentWithType',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/uninstallAgent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallAgentWithTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_agent_with_type_with_options_async(
        self,
        request: main_models.UninstallAgentWithTypeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UninstallAgentWithTypeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_version):
            body['agentVersion'] = request.agent_version
        if not DaraCore.is_null(request.instance_type):
            body['instanceType'] = request.instance_type
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UninstallAgentWithType',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/uninstallAgent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallAgentWithTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_agent_with_type(
        self,
        request: main_models.UninstallAgentWithTypeRequest,
    ) -> main_models.UninstallAgentWithTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.uninstall_agent_with_type_with_options(request, headers, runtime)

    async def uninstall_agent_with_type_async(
        self,
        request: main_models.UninstallAgentWithTypeRequest,
    ) -> main_models.UninstallAgentWithTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.uninstall_agent_with_type_with_options_async(request, headers, runtime)

    def uninstall_hotfix_with_options(
        self,
        request: main_models.UninstallHotfixRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UninstallHotfixResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cve_id):
            body['cveId'] = request.cve_id
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UninstallHotfix',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/hotfix_manager/hotfix/uninstall',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallHotfixResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_hotfix_with_options_async(
        self,
        request: main_models.UninstallHotfixRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UninstallHotfixResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cve_id):
            body['cveId'] = request.cve_id
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UninstallHotfix',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/hotfix_manager/hotfix/uninstall',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallHotfixResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_hotfix(
        self,
        request: main_models.UninstallHotfixRequest,
    ) -> main_models.UninstallHotfixResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.uninstall_hotfix_with_options(request, headers, runtime)

    async def uninstall_hotfix_async(
        self,
        request: main_models.UninstallHotfixRequest,
    ) -> main_models.UninstallHotfixResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.uninstall_hotfix_with_options_async(request, headers, runtime)

    def update_agent_config_with_options(
        self,
        request: main_models.UpdateAgentConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.config_id):
            body['configId'] = request.config_id
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgentConfig',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/updateAgentConfig',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_agent_config_with_options_async(
        self,
        request: main_models.UpdateAgentConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.config_id):
            body['configId'] = request.config_id
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgentConfig',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/updateAgentConfig',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_agent_config(
        self,
        request: main_models.UpdateAgentConfigRequest,
    ) -> main_models.UpdateAgentConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_agent_config_with_options(request, headers, runtime)

    async def update_agent_config_async(
        self,
        request: main_models.UpdateAgentConfigRequest,
    ) -> main_models.UpdateAgentConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_agent_config_with_options_async(request, headers, runtime)

    def update_alert_destination_with_options(
        self,
        request: main_models.UpdateAlertDestinationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlertDestinationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['app_id'] = request.app_id
        if not DaraCore.is_null(request.app_secret):
            body['app_secret'] = request.app_secret
        if not DaraCore.is_null(request.group_id):
            body['group_id'] = request.group_id
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.imbot):
            body['imbot'] = request.imbot
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        if not DaraCore.is_null(request.target):
            body['target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlertDestination',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/updateDestination',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAlertDestinationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alert_destination_with_options_async(
        self,
        request: main_models.UpdateAlertDestinationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlertDestinationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['app_id'] = request.app_id
        if not DaraCore.is_null(request.app_secret):
            body['app_secret'] = request.app_secret
        if not DaraCore.is_null(request.group_id):
            body['group_id'] = request.group_id
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.imbot):
            body['imbot'] = request.imbot
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        if not DaraCore.is_null(request.target):
            body['target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlertDestination',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/updateDestination',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAlertDestinationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alert_destination(
        self,
        request: main_models.UpdateAlertDestinationRequest,
    ) -> main_models.UpdateAlertDestinationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_alert_destination_with_options(request, headers, runtime)

    async def update_alert_destination_async(
        self,
        request: main_models.UpdateAlertDestinationRequest,
    ) -> main_models.UpdateAlertDestinationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_alert_destination_with_options_async(request, headers, runtime)

    def update_alert_enabled_with_options(
        self,
        request: main_models.UpdateAlertEnabledRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlertEnabledResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enabled):
            body['enabled'] = request.enabled
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlertEnabled',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/updateEnabled',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAlertEnabledResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alert_enabled_with_options_async(
        self,
        request: main_models.UpdateAlertEnabledRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlertEnabledResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enabled):
            body['enabled'] = request.enabled
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlertEnabled',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/updateEnabled',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAlertEnabledResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alert_enabled(
        self,
        request: main_models.UpdateAlertEnabledRequest,
    ) -> main_models.UpdateAlertEnabledResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_alert_enabled_with_options(request, headers, runtime)

    async def update_alert_enabled_async(
        self,
        request: main_models.UpdateAlertEnabledRequest,
    ) -> main_models.UpdateAlertEnabledResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_alert_enabled_with_options_async(request, headers, runtime)

    def update_alert_strategy_with_options(
        self,
        request: main_models.UpdateAlertStrategyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlertStrategyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enabled):
            body['enabled'] = request.enabled
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.k_8s_label):
            body['k8sLabel'] = request.k_8s_label
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.strategy):
            body['strategy'] = request.strategy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlertStrategy',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/updateStrategy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAlertStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alert_strategy_with_options_async(
        self,
        request: main_models.UpdateAlertStrategyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlertStrategyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enabled):
            body['enabled'] = request.enabled
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.k_8s_label):
            body['k8sLabel'] = request.k_8s_label
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.strategy):
            body['strategy'] = request.strategy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlertStrategy',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/alertPusher/alert/updateStrategy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAlertStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alert_strategy(
        self,
        request: main_models.UpdateAlertStrategyRequest,
    ) -> main_models.UpdateAlertStrategyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_alert_strategy_with_options(request, headers, runtime)

    async def update_alert_strategy_async(
        self,
        request: main_models.UpdateAlertStrategyRequest,
    ) -> main_models.UpdateAlertStrategyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_alert_strategy_with_options_async(request, headers, runtime)

    def update_cluster_agent_config_with_options(
        self,
        request: main_models.UpdateClusterAgentConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClusterAgentConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.cluster_id):
            body['clusterId'] = request.cluster_id
        if not DaraCore.is_null(request.config_id):
            body['configId'] = request.config_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateClusterAgentConfig',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/updateClusterAgentConfig',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClusterAgentConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cluster_agent_config_with_options_async(
        self,
        request: main_models.UpdateClusterAgentConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClusterAgentConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.cluster_id):
            body['clusterId'] = request.cluster_id
        if not DaraCore.is_null(request.config_id):
            body['configId'] = request.config_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateClusterAgentConfig',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/updateClusterAgentConfig',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClusterAgentConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cluster_agent_config(
        self,
        request: main_models.UpdateClusterAgentConfigRequest,
    ) -> main_models.UpdateClusterAgentConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_cluster_agent_config_with_options(request, headers, runtime)

    async def update_cluster_agent_config_async(
        self,
        request: main_models.UpdateClusterAgentConfigRequest,
    ) -> main_models.UpdateClusterAgentConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_cluster_agent_config_with_options_async(request, headers, runtime)

    def update_events_attention_with_options(
        self,
        request: main_models.UpdateEventsAttentionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEventsAttentionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.mode):
            body['mode'] = request.mode
        if not DaraCore.is_null(request.range):
            body['range'] = request.range
        if not DaraCore.is_null(request.uuid):
            body['uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEventsAttention',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/proxy/post/cluster_update_events_attention',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEventsAttentionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_events_attention_with_options_async(
        self,
        request: main_models.UpdateEventsAttentionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEventsAttentionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.mode):
            body['mode'] = request.mode
        if not DaraCore.is_null(request.range):
            body['range'] = request.range
        if not DaraCore.is_null(request.uuid):
            body['uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEventsAttention',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/openapi/proxy/post/cluster_update_events_attention',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEventsAttentionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_events_attention(
        self,
        request: main_models.UpdateEventsAttentionRequest,
    ) -> main_models.UpdateEventsAttentionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_events_attention_with_options(request, headers, runtime)

    async def update_events_attention_async(
        self,
        request: main_models.UpdateEventsAttentionRequest,
    ) -> main_models.UpdateEventsAttentionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_events_attention_with_options_async(request, headers, runtime)

    def update_func_switch_record_with_options(
        self,
        tmp_req: main_models.UpdateFuncSwitchRecordRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFuncSwitchRecordResponse:
        tmp_req.validate()
        request = main_models.UpdateFuncSwitchRecordShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'params', 'json')
        query = {}
        if not DaraCore.is_null(request.channel):
            query['channel'] = request.channel
        if not DaraCore.is_null(request.params_shrink):
            query['params'] = request.params_shrink
        if not DaraCore.is_null(request.service_name):
            query['service_name'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFuncSwitchRecord',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/func-switch/update-service-func-switch',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFuncSwitchRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_func_switch_record_with_options_async(
        self,
        tmp_req: main_models.UpdateFuncSwitchRecordRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFuncSwitchRecordResponse:
        tmp_req.validate()
        request = main_models.UpdateFuncSwitchRecordShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'params', 'json')
        query = {}
        if not DaraCore.is_null(request.channel):
            query['channel'] = request.channel
        if not DaraCore.is_null(request.params_shrink):
            query['params'] = request.params_shrink
        if not DaraCore.is_null(request.service_name):
            query['service_name'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFuncSwitchRecord',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/func-switch/update-service-func-switch',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFuncSwitchRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_func_switch_record(
        self,
        request: main_models.UpdateFuncSwitchRecordRequest,
    ) -> main_models.UpdateFuncSwitchRecordResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_func_switch_record_with_options(request, headers, runtime)

    async def update_func_switch_record_async(
        self,
        request: main_models.UpdateFuncSwitchRecordRequest,
    ) -> main_models.UpdateFuncSwitchRecordResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_func_switch_record_with_options_async(request, headers, runtime)

    def update_instance_agent_config_with_options(
        self,
        request: main_models.UpdateInstanceAgentConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceAgentConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.config_id):
            body['configId'] = request.config_id
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceAgentConfig',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/updateInstanceAgentConfig',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceAgentConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_agent_config_with_options_async(
        self,
        request: main_models.UpdateInstanceAgentConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceAgentConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.config_id):
            body['configId'] = request.config_id
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceAgentConfig',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/updateInstanceAgentConfig',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceAgentConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_agent_config(
        self,
        request: main_models.UpdateInstanceAgentConfigRequest,
    ) -> main_models.UpdateInstanceAgentConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_instance_agent_config_with_options(request, headers, runtime)

    async def update_instance_agent_config_async(
        self,
        request: main_models.UpdateInstanceAgentConfigRequest,
    ) -> main_models.UpdateInstanceAgentConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_instance_agent_config_with_options_async(request, headers, runtime)

    def upgrade_agent_with_options(
        self,
        request: main_models.UpgradeAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agent_id'] = request.agent_id
        if not DaraCore.is_null(request.agent_version):
            body['agent_version'] = request.agent_version
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeAgent',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/upgrade_agent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_agent_with_options_async(
        self,
        request: main_models.UpgradeAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agent_id'] = request.agent_id
        if not DaraCore.is_null(request.agent_version):
            body['agent_version'] = request.agent_version
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeAgent',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/upgrade_agent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_agent(
        self,
        request: main_models.UpgradeAgentRequest,
    ) -> main_models.UpgradeAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.upgrade_agent_with_options(request, headers, runtime)

    async def upgrade_agent_async(
        self,
        request: main_models.UpgradeAgentRequest,
    ) -> main_models.UpgradeAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.upgrade_agent_with_options_async(request, headers, runtime)

    def upgrade_agent_for_cluster_with_options(
        self,
        request: main_models.UpgradeAgentForClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeAgentForClusterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agent_id'] = request.agent_id
        if not DaraCore.is_null(request.agent_version):
            body['agent_version'] = request.agent_version
        if not DaraCore.is_null(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeAgentForCluster',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/upgrade_agent_by_cluster',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeAgentForClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_agent_for_cluster_with_options_async(
        self,
        request: main_models.UpgradeAgentForClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeAgentForClusterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agent_id'] = request.agent_id
        if not DaraCore.is_null(request.agent_version):
            body['agent_version'] = request.agent_version
        if not DaraCore.is_null(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeAgentForCluster',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/upgrade_agent_by_cluster',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeAgentForClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_agent_for_cluster(
        self,
        request: main_models.UpgradeAgentForClusterRequest,
    ) -> main_models.UpgradeAgentForClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.upgrade_agent_for_cluster_with_options(request, headers, runtime)

    async def upgrade_agent_for_cluster_async(
        self,
        request: main_models.UpgradeAgentForClusterRequest,
    ) -> main_models.UpgradeAgentForClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.upgrade_agent_for_cluster_with_options_async(request, headers, runtime)

    def upgrade_agent_with_type_with_options(
        self,
        request: main_models.UpgradeAgentWithTypeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeAgentWithTypeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_version):
            body['agentVersion'] = request.agent_version
        if not DaraCore.is_null(request.instance_type):
            body['instanceType'] = request.instance_type
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeAgentWithType',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/upgradeAgent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeAgentWithTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_agent_with_type_with_options_async(
        self,
        request: main_models.UpgradeAgentWithTypeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeAgentWithTypeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_version):
            body['agentVersion'] = request.agent_version
        if not DaraCore.is_null(request.instance_type):
            body['instanceType'] = request.instance_type
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeAgentWithType',
            version = '2023-12-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/am/agent/upgradeAgent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeAgentWithTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_agent_with_type(
        self,
        request: main_models.UpgradeAgentWithTypeRequest,
    ) -> main_models.UpgradeAgentWithTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.upgrade_agent_with_type_with_options(request, headers, runtime)

    async def upgrade_agent_with_type_async(
        self,
        request: main_models.UpgradeAgentWithTypeRequest,
    ) -> main_models.UpgradeAgentWithTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.upgrade_agent_with_type_with_options_async(request, headers, runtime)
