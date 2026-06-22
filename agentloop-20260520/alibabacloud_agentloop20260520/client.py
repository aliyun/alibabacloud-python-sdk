# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agentloop20260520 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-zhangjiakou': 'agentloop.cn-zhangjiakou.aliyuncs.com',
            'cn-shanghai': 'agentloop.cn-shanghai.aliyuncs.com',
            'cn-hongkong': 'agentloop.cn-hongkong.aliyuncs.com',
            'cn-hangzhou': 'agentloop.cn-hangzhou.aliyuncs.com',
            'cn-beijing': 'agentloop.cn-beijing.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('agentloop', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_dataset_data_with_options(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.AddDatasetDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddDatasetDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.data_array):
            body['dataArray'] = request.data_array
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddDatasetData',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset/{DaraURL.percent_encode(dataset_name)}/rows',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDatasetDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_dataset_data_with_options_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.AddDatasetDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddDatasetDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.data_array):
            body['dataArray'] = request.data_array
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddDatasetData',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset/{DaraURL.percent_encode(dataset_name)}/rows',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDatasetDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_dataset_data(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.AddDatasetDataRequest,
    ) -> main_models.AddDatasetDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_dataset_data_with_options(agent_space, dataset_name, request, headers, runtime)

    async def add_dataset_data_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.AddDatasetDataRequest,
    ) -> main_models.AddDatasetDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_dataset_data_with_options_async(agent_space, dataset_name, request, headers, runtime)

    def create_agent_space_with_options(
        self,
        request: main_models.CreateAgentSpaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentSpaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.agent_space):
            body['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.cms_workspace):
            body['cmsWorkspace'] = request.cms_workspace
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentSpace',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_agent_space_with_options_async(
        self,
        request: main_models.CreateAgentSpaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentSpaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.agent_space):
            body['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.cms_workspace):
            body['cmsWorkspace'] = request.cms_workspace
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentSpace',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentSpaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_agent_space(
        self,
        request: main_models.CreateAgentSpaceRequest,
    ) -> main_models.CreateAgentSpaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_agent_space_with_options(request, headers, runtime)

    async def create_agent_space_async(
        self,
        request: main_models.CreateAgentSpaceRequest,
    ) -> main_models.CreateAgentSpaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_agent_space_with_options_async(request, headers, runtime)

    def create_context_store_with_options(
        self,
        agent_space: str,
        request: main_models.CreateContextStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateContextStoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.context_store_name):
            body['contextStoreName'] = request.context_store_name
        if not DaraCore.is_null(request.context_type):
            body['contextType'] = request.context_type
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateContextStore',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateContextStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_context_store_with_options_async(
        self,
        agent_space: str,
        request: main_models.CreateContextStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateContextStoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.context_store_name):
            body['contextStoreName'] = request.context_store_name
        if not DaraCore.is_null(request.context_type):
            body['contextType'] = request.context_type
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateContextStore',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateContextStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_context_store(
        self,
        agent_space: str,
        request: main_models.CreateContextStoreRequest,
    ) -> main_models.CreateContextStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_context_store_with_options(agent_space, request, headers, runtime)

    async def create_context_store_async(
        self,
        agent_space: str,
        request: main_models.CreateContextStoreRequest,
    ) -> main_models.CreateContextStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_context_store_with_options_async(agent_space, request, headers, runtime)

    def create_context_store_apikey_with_options(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.CreateContextStoreAPIKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateContextStoreAPIKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateContextStoreAPIKey',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/apikey',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateContextStoreAPIKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_context_store_apikey_with_options_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.CreateContextStoreAPIKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateContextStoreAPIKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateContextStoreAPIKey',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/apikey',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateContextStoreAPIKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_context_store_apikey(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.CreateContextStoreAPIKeyRequest,
    ) -> main_models.CreateContextStoreAPIKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_context_store_apikey_with_options(agent_space, context_store_name, request, headers, runtime)

    async def create_context_store_apikey_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.CreateContextStoreAPIKeyRequest,
    ) -> main_models.CreateContextStoreAPIKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_context_store_apikey_with_options_async(agent_space, context_store_name, request, headers, runtime)

    def create_dataset_with_options(
        self,
        agent_space: str,
        request: main_models.CreateDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.dataset_name):
            body['datasetName'] = request.dataset_name
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.schema):
            body['schema'] = request.schema
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataset',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_with_options_async(
        self,
        agent_space: str,
        request: main_models.CreateDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.dataset_name):
            body['datasetName'] = request.dataset_name
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.schema):
            body['schema'] = request.schema
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataset',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset(
        self,
        agent_space: str,
        request: main_models.CreateDatasetRequest,
    ) -> main_models.CreateDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_dataset_with_options(agent_space, request, headers, runtime)

    async def create_dataset_async(
        self,
        agent_space: str,
        request: main_models.CreateDatasetRequest,
    ) -> main_models.CreateDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_dataset_with_options_async(agent_space, request, headers, runtime)

    def delete_agent_space_with_options(
        self,
        agent_space: str,
        request: main_models.DeleteAgentSpaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentSpaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_cms_workspace):
            query['deleteCmsWorkspace'] = request.delete_cms_workspace
        if not DaraCore.is_null(request.delete_mse_namespace):
            query['deleteMseNamespace'] = request.delete_mse_namespace
        if not DaraCore.is_null(request.delete_sls_project):
            query['deleteSlsProject'] = request.delete_sls_project
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgentSpace',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_agent_space_with_options_async(
        self,
        agent_space: str,
        request: main_models.DeleteAgentSpaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentSpaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_cms_workspace):
            query['deleteCmsWorkspace'] = request.delete_cms_workspace
        if not DaraCore.is_null(request.delete_mse_namespace):
            query['deleteMseNamespace'] = request.delete_mse_namespace
        if not DaraCore.is_null(request.delete_sls_project):
            query['deleteSlsProject'] = request.delete_sls_project
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgentSpace',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentSpaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_agent_space(
        self,
        agent_space: str,
        request: main_models.DeleteAgentSpaceRequest,
    ) -> main_models.DeleteAgentSpaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_agent_space_with_options(agent_space, request, headers, runtime)

    async def delete_agent_space_async(
        self,
        agent_space: str,
        request: main_models.DeleteAgentSpaceRequest,
    ) -> main_models.DeleteAgentSpaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_agent_space_with_options_async(agent_space, request, headers, runtime)

    def delete_context_store_with_options(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.DeleteContextStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContextStoreResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteContextStore',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContextStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_context_store_with_options_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.DeleteContextStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContextStoreResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteContextStore',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContextStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_context_store(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.DeleteContextStoreRequest,
    ) -> main_models.DeleteContextStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_context_store_with_options(agent_space, context_store_name, request, headers, runtime)

    async def delete_context_store_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.DeleteContextStoreRequest,
    ) -> main_models.DeleteContextStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_context_store_with_options_async(agent_space, context_store_name, request, headers, runtime)

    def delete_context_store_apikey_with_options(
        self,
        agent_space: str,
        context_store_name: str,
        name: str,
        request: main_models.DeleteContextStoreAPIKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContextStoreAPIKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteContextStoreAPIKey',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/apikey/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContextStoreAPIKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_context_store_apikey_with_options_async(
        self,
        agent_space: str,
        context_store_name: str,
        name: str,
        request: main_models.DeleteContextStoreAPIKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContextStoreAPIKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteContextStoreAPIKey',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/apikey/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContextStoreAPIKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_context_store_apikey(
        self,
        agent_space: str,
        context_store_name: str,
        name: str,
        request: main_models.DeleteContextStoreAPIKeyRequest,
    ) -> main_models.DeleteContextStoreAPIKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_context_store_apikey_with_options(agent_space, context_store_name, name, request, headers, runtime)

    async def delete_context_store_apikey_async(
        self,
        agent_space: str,
        context_store_name: str,
        name: str,
        request: main_models.DeleteContextStoreAPIKeyRequest,
    ) -> main_models.DeleteContextStoreAPIKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_context_store_apikey_with_options_async(agent_space, context_store_name, name, request, headers, runtime)

    def delete_dataset_with_options(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.DeleteDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataset',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset/{DaraURL.percent_encode(dataset_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_with_options_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.DeleteDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataset',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset/{DaraURL.percent_encode(dataset_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.DeleteDatasetRequest,
    ) -> main_models.DeleteDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_dataset_with_options(agent_space, dataset_name, request, headers, runtime)

    async def delete_dataset_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.DeleteDatasetRequest,
    ) -> main_models.DeleteDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_dataset_with_options_async(agent_space, dataset_name, request, headers, runtime)

    def delete_pipeline_with_options(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.DeletePipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePipelineResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePipeline',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/pipeline/{DaraURL.percent_encode(pipeline_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pipeline_with_options_async(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.DeletePipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePipelineResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePipeline',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/pipeline/{DaraURL.percent_encode(pipeline_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pipeline(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.DeletePipelineRequest,
    ) -> main_models.DeletePipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_pipeline_with_options(agent_space, pipeline_name, request, headers, runtime)

    async def delete_pipeline_async(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.DeletePipelineRequest,
    ) -> main_models.DeletePipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_pipeline_with_options_async(agent_space, pipeline_name, request, headers, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/regions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/regions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(request, headers, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(request, headers, runtime)

    def execute_query_with_options(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.ExecuteQueryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteQueryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteQuery',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset/{DaraURL.percent_encode(dataset_name)}/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_query_with_options_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.ExecuteQueryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteQueryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteQuery',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset/{DaraURL.percent_encode(dataset_name)}/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_query(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.ExecuteQueryRequest,
    ) -> main_models.ExecuteQueryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_query_with_options(agent_space, dataset_name, request, headers, runtime)

    async def execute_query_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.ExecuteQueryRequest,
    ) -> main_models.ExecuteQueryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_query_with_options_async(agent_space, dataset_name, request, headers, runtime)

    def get_agent_space_with_options(
        self,
        agent_space: str,
        request: main_models.GetAgentSpaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentSpaceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAgentSpace',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_space_with_options_async(
        self,
        agent_space: str,
        request: main_models.GetAgentSpaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentSpaceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAgentSpace',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentSpaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_space(
        self,
        agent_space: str,
        request: main_models.GetAgentSpaceRequest,
    ) -> main_models.GetAgentSpaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_agent_space_with_options(agent_space, request, headers, runtime)

    async def get_agent_space_async(
        self,
        agent_space: str,
        request: main_models.GetAgentSpaceRequest,
    ) -> main_models.GetAgentSpaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_agent_space_with_options_async(agent_space, request, headers, runtime)

    def get_context_store_with_options(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.GetContextStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetContextStoreResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetContextStore',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetContextStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_context_store_with_options_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.GetContextStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetContextStoreResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetContextStore',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetContextStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_context_store(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.GetContextStoreRequest,
    ) -> main_models.GetContextStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_context_store_with_options(agent_space, context_store_name, request, headers, runtime)

    async def get_context_store_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.GetContextStoreRequest,
    ) -> main_models.GetContextStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_context_store_with_options_async(agent_space, context_store_name, request, headers, runtime)

    def get_context_store_apikey_with_options(
        self,
        agent_space: str,
        context_store_name: str,
        name: str,
        request: main_models.GetContextStoreAPIKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetContextStoreAPIKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetContextStoreAPIKey',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/apikey/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetContextStoreAPIKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_context_store_apikey_with_options_async(
        self,
        agent_space: str,
        context_store_name: str,
        name: str,
        request: main_models.GetContextStoreAPIKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetContextStoreAPIKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetContextStoreAPIKey',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/apikey/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetContextStoreAPIKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_context_store_apikey(
        self,
        agent_space: str,
        context_store_name: str,
        name: str,
        request: main_models.GetContextStoreAPIKeyRequest,
    ) -> main_models.GetContextStoreAPIKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_context_store_apikey_with_options(agent_space, context_store_name, name, request, headers, runtime)

    async def get_context_store_apikey_async(
        self,
        agent_space: str,
        context_store_name: str,
        name: str,
        request: main_models.GetContextStoreAPIKeyRequest,
    ) -> main_models.GetContextStoreAPIKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_context_store_apikey_with_options_async(agent_space, context_store_name, name, request, headers, runtime)

    def get_dataset_with_options(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.GetDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDataset',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset/{DaraURL.percent_encode(dataset_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_with_options_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.GetDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDataset',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset/{DaraURL.percent_encode(dataset_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.GetDatasetRequest,
    ) -> main_models.GetDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_dataset_with_options(agent_space, dataset_name, request, headers, runtime)

    async def get_dataset_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.GetDatasetRequest,
    ) -> main_models.GetDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_dataset_with_options_async(agent_space, dataset_name, request, headers, runtime)

    def get_pipeline_with_options(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.GetPipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPipelineResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPipeline',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/pipeline/{DaraURL.percent_encode(pipeline_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_with_options_async(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.GetPipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPipelineResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPipeline',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/pipeline/{DaraURL.percent_encode(pipeline_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.GetPipelineRequest,
    ) -> main_models.GetPipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_pipeline_with_options(agent_space, pipeline_name, request, headers, runtime)

    async def get_pipeline_async(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.GetPipelineRequest,
    ) -> main_models.GetPipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_pipeline_with_options_async(agent_space, pipeline_name, request, headers, runtime)

    def list_agent_spaces_with_options(
        self,
        request: main_models.ListAgentSpacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentSpacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentSpaces',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentSpacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_spaces_with_options_async(
        self,
        request: main_models.ListAgentSpacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentSpacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentSpaces',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentSpacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_spaces(
        self,
        request: main_models.ListAgentSpacesRequest,
    ) -> main_models.ListAgentSpacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_agent_spaces_with_options(request, headers, runtime)

    async def list_agent_spaces_async(
        self,
        request: main_models.ListAgentSpacesRequest,
    ) -> main_models.ListAgentSpacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_agent_spaces_with_options_async(request, headers, runtime)

    def list_context_store_apikeys_with_options(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.ListContextStoreAPIKeysRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListContextStoreAPIKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListContextStoreAPIKeys',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/apikey',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListContextStoreAPIKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_context_store_apikeys_with_options_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.ListContextStoreAPIKeysRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListContextStoreAPIKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListContextStoreAPIKeys',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/apikey',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListContextStoreAPIKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_context_store_apikeys(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.ListContextStoreAPIKeysRequest,
    ) -> main_models.ListContextStoreAPIKeysResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_context_store_apikeys_with_options(agent_space, context_store_name, request, headers, runtime)

    async def list_context_store_apikeys_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.ListContextStoreAPIKeysRequest,
    ) -> main_models.ListContextStoreAPIKeysResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_context_store_apikeys_with_options_async(agent_space, context_store_name, request, headers, runtime)

    def list_context_stores_with_options(
        self,
        agent_space: str,
        request: main_models.ListContextStoresRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListContextStoresResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.context_store_name):
            query['contextStoreName'] = request.context_store_name
        if not DaraCore.is_null(request.context_type):
            query['contextType'] = request.context_type
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListContextStores',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListContextStoresResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_context_stores_with_options_async(
        self,
        agent_space: str,
        request: main_models.ListContextStoresRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListContextStoresResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.context_store_name):
            query['contextStoreName'] = request.context_store_name
        if not DaraCore.is_null(request.context_type):
            query['contextType'] = request.context_type
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListContextStores',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListContextStoresResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_context_stores(
        self,
        agent_space: str,
        request: main_models.ListContextStoresRequest,
    ) -> main_models.ListContextStoresResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_context_stores_with_options(agent_space, request, headers, runtime)

    async def list_context_stores_async(
        self,
        agent_space: str,
        request: main_models.ListContextStoresRequest,
    ) -> main_models.ListContextStoresResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_context_stores_with_options_async(agent_space, request, headers, runtime)

    def list_datasets_with_options(
        self,
        agent_space: str,
        request: main_models.ListDatasetsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['datasetName'] = request.dataset_name
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasets',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_datasets_with_options_async(
        self,
        agent_space: str,
        request: main_models.ListDatasetsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['datasetName'] = request.dataset_name
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasets',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_datasets(
        self,
        agent_space: str,
        request: main_models.ListDatasetsRequest,
    ) -> main_models.ListDatasetsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_datasets_with_options(agent_space, request, headers, runtime)

    async def list_datasets_async(
        self,
        agent_space: str,
        request: main_models.ListDatasetsRequest,
    ) -> main_models.ListDatasetsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_datasets_with_options_async(agent_space, request, headers, runtime)

    def list_pipelines_with_options(
        self,
        agent_space: str,
        request: main_models.ListPipelinesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPipelinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPipelines',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/pipeline',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipelines_with_options_async(
        self,
        agent_space: str,
        request: main_models.ListPipelinesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPipelinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPipelines',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/pipeline',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPipelinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipelines(
        self,
        agent_space: str,
        request: main_models.ListPipelinesRequest,
    ) -> main_models.ListPipelinesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_pipelines_with_options(agent_space, request, headers, runtime)

    async def list_pipelines_async(
        self,
        agent_space: str,
        request: main_models.ListPipelinesRequest,
    ) -> main_models.ListPipelinesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_pipelines_with_options_async(agent_space, request, headers, runtime)

    def search_context_with_options(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.SearchContextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchContextResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.filter):
            body['filter'] = request.filter
        if not DaraCore.is_null(request.formatted):
            body['formatted'] = request.formatted
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.retrieval_option):
            body['retrievalOption'] = request.retrieval_option
        if not DaraCore.is_null(request.threshold):
            body['threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchContext',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/context/search',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchContextResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_context_with_options_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.SearchContextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchContextResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.filter):
            body['filter'] = request.filter
        if not DaraCore.is_null(request.formatted):
            body['formatted'] = request.formatted
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.retrieval_option):
            body['retrievalOption'] = request.retrieval_option
        if not DaraCore.is_null(request.threshold):
            body['threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchContext',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/context/search',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchContextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_context(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.SearchContextRequest,
    ) -> main_models.SearchContextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.search_context_with_options(agent_space, context_store_name, request, headers, runtime)

    async def search_context_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.SearchContextRequest,
    ) -> main_models.SearchContextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.search_context_with_options_async(agent_space, context_store_name, request, headers, runtime)

    def update_agent_space_with_options(
        self,
        agent_space: str,
        request: main_models.UpdateAgentSpaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentSpaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.cms_workspace):
            body['cmsWorkspace'] = request.cms_workspace
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgentSpace',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_agent_space_with_options_async(
        self,
        agent_space: str,
        request: main_models.UpdateAgentSpaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentSpaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.cms_workspace):
            body['cmsWorkspace'] = request.cms_workspace
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgentSpace',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentSpaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_agent_space(
        self,
        agent_space: str,
        request: main_models.UpdateAgentSpaceRequest,
    ) -> main_models.UpdateAgentSpaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_agent_space_with_options(agent_space, request, headers, runtime)

    async def update_agent_space_async(
        self,
        agent_space: str,
        request: main_models.UpdateAgentSpaceRequest,
    ) -> main_models.UpdateAgentSpaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_agent_space_with_options_async(agent_space, request, headers, runtime)

    def update_context_store_with_options(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.UpdateContextStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateContextStoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.context_type):
            body['contextType'] = request.context_type
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateContextStore',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateContextStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_context_store_with_options_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.UpdateContextStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateContextStoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.context_type):
            body['contextType'] = request.context_type
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateContextStore',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateContextStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_context_store(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.UpdateContextStoreRequest,
    ) -> main_models.UpdateContextStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_context_store_with_options(agent_space, context_store_name, request, headers, runtime)

    async def update_context_store_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.UpdateContextStoreRequest,
    ) -> main_models.UpdateContextStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_context_store_with_options_async(agent_space, context_store_name, request, headers, runtime)

    def update_dataset_with_options(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.UpdateDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.schema):
            body['schema'] = request.schema
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataset',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset/{DaraURL.percent_encode(dataset_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dataset_with_options_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.UpdateDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.schema):
            body['schema'] = request.schema
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataset',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset/{DaraURL.percent_encode(dataset_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dataset(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.UpdateDatasetRequest,
    ) -> main_models.UpdateDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_dataset_with_options(agent_space, dataset_name, request, headers, runtime)

    async def update_dataset_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.UpdateDatasetRequest,
    ) -> main_models.UpdateDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_dataset_with_options_async(agent_space, dataset_name, request, headers, runtime)

    def update_pipeline_with_options(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.UpdatePipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePipelineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.execute_policy):
            body['executePolicy'] = request.execute_policy
        if not DaraCore.is_null(request.pipeline):
            body['pipeline'] = request.pipeline
        if not DaraCore.is_null(request.sink):
            body['sink'] = request.sink
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePipeline',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/pipeline/{DaraURL.percent_encode(pipeline_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pipeline_with_options_async(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.UpdatePipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePipelineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.execute_policy):
            body['executePolicy'] = request.execute_policy
        if not DaraCore.is_null(request.pipeline):
            body['pipeline'] = request.pipeline
        if not DaraCore.is_null(request.sink):
            body['sink'] = request.sink
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePipeline',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/pipeline/{DaraURL.percent_encode(pipeline_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pipeline(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.UpdatePipelineRequest,
    ) -> main_models.UpdatePipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_pipeline_with_options(agent_space, pipeline_name, request, headers, runtime)

    async def update_pipeline_async(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.UpdatePipelineRequest,
    ) -> main_models.UpdatePipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_pipeline_with_options_async(agent_space, pipeline_name, request, headers, runtime)
