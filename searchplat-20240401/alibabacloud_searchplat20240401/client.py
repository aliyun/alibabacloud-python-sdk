# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_searchplat20240401 import models as main_models
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
            'eu-central-1': 'searchplat.eu-central-1.aliyuncs.com',
            'cn-shanghai': 'searchplat.cn-shanghai.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('searchplat', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cease_function_instance_with_options(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.CeaseFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CeaseFunctionInstanceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CeaseFunctionInstance',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}/actions/cease',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CeaseFunctionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def cease_function_instance_with_options_async(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.CeaseFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CeaseFunctionInstanceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CeaseFunctionInstance',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}/actions/cease',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CeaseFunctionInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cease_function_instance(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.CeaseFunctionInstanceRequest,
    ) -> main_models.CeaseFunctionInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.cease_function_instance_with_options(workspace_name, function_name, instance_name, request, headers, runtime)

    async def cease_function_instance_async(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.CeaseFunctionInstanceRequest,
    ) -> main_models.CeaseFunctionInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.cease_function_instance_with_options_async(workspace_name, function_name, instance_name, request, headers, runtime)

    def create_async_task_with_options(
        self,
        workspace_name: str,
        request: main_models.CreateAsyncTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.data_id):
            body['dataId'] = request.data_id
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.service_id):
            body['serviceId'] = request.service_id
        if not DaraCore.is_null(request.service_type):
            body['serviceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAsyncTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/async-tasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_async_task_with_options_async(
        self,
        workspace_name: str,
        request: main_models.CreateAsyncTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.data_id):
            body['dataId'] = request.data_id
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.service_id):
            body['serviceId'] = request.service_id
        if not DaraCore.is_null(request.service_type):
            body['serviceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAsyncTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/async-tasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_async_task(
        self,
        workspace_name: str,
        request: main_models.CreateAsyncTaskRequest,
    ) -> main_models.CreateAsyncTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_async_task_with_options(workspace_name, request, headers, runtime)

    async def create_async_task_async(
        self,
        workspace_name: str,
        request: main_models.CreateAsyncTaskRequest,
    ) -> main_models.CreateAsyncTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_async_task_with_options_async(workspace_name, request, headers, runtime)

    def create_capability_with_options(
        self,
        workspace_name: str,
        item_category: str,
        request: main_models.CreateCapabilityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCapabilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.item_desc):
            body['itemDesc'] = request.item_desc
        if not DaraCore.is_null(request.item_name):
            body['itemName'] = request.item_name
        if not DaraCore.is_null(request.item_value):
            body['itemValue'] = request.item_value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCapability',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/capabilities/{DaraURL.percent_encode(item_category)}/items',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCapabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_capability_with_options_async(
        self,
        workspace_name: str,
        item_category: str,
        request: main_models.CreateCapabilityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCapabilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.item_desc):
            body['itemDesc'] = request.item_desc
        if not DaraCore.is_null(request.item_name):
            body['itemName'] = request.item_name
        if not DaraCore.is_null(request.item_value):
            body['itemValue'] = request.item_value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCapability',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/capabilities/{DaraURL.percent_encode(item_category)}/items',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCapabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_capability(
        self,
        workspace_name: str,
        item_category: str,
        request: main_models.CreateCapabilityRequest,
    ) -> main_models.CreateCapabilityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_capability_with_options(workspace_name, item_category, request, headers, runtime)

    async def create_capability_async(
        self,
        workspace_name: str,
        item_category: str,
        request: main_models.CreateCapabilityRequest,
    ) -> main_models.CreateCapabilityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_capability_with_options_async(workspace_name, item_category, request, headers, runtime)

    def create_config_with_options(
        self,
        workspace_name: str,
        config_type: str,
        request: main_models.CreateConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.config_data):
            body['configData'] = request.config_data
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConfig',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/configs/{DaraURL.percent_encode(config_type)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_config_with_options_async(
        self,
        workspace_name: str,
        config_type: str,
        request: main_models.CreateConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.config_data):
            body['configData'] = request.config_data
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConfig',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/configs/{DaraURL.percent_encode(config_type)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_config(
        self,
        workspace_name: str,
        config_type: str,
        request: main_models.CreateConfigRequest,
    ) -> main_models.CreateConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_config_with_options(workspace_name, config_type, request, headers, runtime)

    async def create_config_async(
        self,
        workspace_name: str,
        config_type: str,
        request: main_models.CreateConfigRequest,
    ) -> main_models.CreateConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_config_with_options_async(workspace_name, config_type, request, headers, runtime)

    def create_credentials_with_options(
        self,
        workspace_name: str,
        request: main_models.CreateCredentialsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCredentials',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/credentials',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_credentials_with_options_async(
        self,
        workspace_name: str,
        request: main_models.CreateCredentialsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCredentials',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/credentials',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_credentials(
        self,
        workspace_name: str,
        request: main_models.CreateCredentialsRequest,
    ) -> main_models.CreateCredentialsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_credentials_with_options(workspace_name, request, headers, runtime)

    async def create_credentials_async(
        self,
        workspace_name: str,
        request: main_models.CreateCredentialsRequest,
    ) -> main_models.CreateCredentialsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_credentials_with_options_async(workspace_name, request, headers, runtime)

    def create_experience_data_with_options(
        self,
        workspace_name: str,
        request: main_models.CreateExperienceDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateExperienceDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.content_type):
            body['contentType'] = request.content_type
        if not DaraCore.is_null(request.data_size):
            body['dataSize'] = request.data_size
        if not DaraCore.is_null(request.data_type):
            body['dataType'] = request.data_type
        if not DaraCore.is_null(request.data_value):
            body['dataValue'] = request.data_value
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.service_type):
            body['serviceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExperienceData',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/experience-data',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExperienceDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_experience_data_with_options_async(
        self,
        workspace_name: str,
        request: main_models.CreateExperienceDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateExperienceDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.content_type):
            body['contentType'] = request.content_type
        if not DaraCore.is_null(request.data_size):
            body['dataSize'] = request.data_size
        if not DaraCore.is_null(request.data_type):
            body['dataType'] = request.data_type
        if not DaraCore.is_null(request.data_value):
            body['dataValue'] = request.data_value
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.service_type):
            body['serviceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExperienceData',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/experience-data',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExperienceDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_experience_data(
        self,
        workspace_name: str,
        request: main_models.CreateExperienceDataRequest,
    ) -> main_models.CreateExperienceDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_experience_data_with_options(workspace_name, request, headers, runtime)

    async def create_experience_data_async(
        self,
        workspace_name: str,
        request: main_models.CreateExperienceDataRequest,
    ) -> main_models.CreateExperienceDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_experience_data_with_options_async(workspace_name, request, headers, runtime)

    def create_function_instance_with_options(
        self,
        workspace_name: str,
        function_name: str,
        request: main_models.CreateFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFunctionInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.create_parameters):
            body['createParameters'] = request.create_parameters
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.function_type):
            body['functionType'] = request.function_type
        if not DaraCore.is_null(request.instance_name):
            body['instanceName'] = request.instance_name
        if not DaraCore.is_null(request.model_type):
            body['modelType'] = request.model_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFunctionInstance',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/functions/{DaraURL.percent_encode(function_name)}/instances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFunctionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_function_instance_with_options_async(
        self,
        workspace_name: str,
        function_name: str,
        request: main_models.CreateFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFunctionInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.create_parameters):
            body['createParameters'] = request.create_parameters
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.function_type):
            body['functionType'] = request.function_type
        if not DaraCore.is_null(request.instance_name):
            body['instanceName'] = request.instance_name
        if not DaraCore.is_null(request.model_type):
            body['modelType'] = request.model_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFunctionInstance',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/functions/{DaraURL.percent_encode(function_name)}/instances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFunctionInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_function_instance(
        self,
        workspace_name: str,
        function_name: str,
        request: main_models.CreateFunctionInstanceRequest,
    ) -> main_models.CreateFunctionInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_function_instance_with_options(workspace_name, function_name, request, headers, runtime)

    async def create_function_instance_async(
        self,
        workspace_name: str,
        function_name: str,
        request: main_models.CreateFunctionInstanceRequest,
    ) -> main_models.CreateFunctionInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_function_instance_with_options_async(workspace_name, function_name, request, headers, runtime)

    def create_function_task_with_options(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.CreateFunctionTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFunctionTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CreateFunctionTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}/tasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFunctionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_function_task_with_options_async(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.CreateFunctionTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFunctionTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CreateFunctionTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}/tasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFunctionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_function_task(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.CreateFunctionTaskRequest,
    ) -> main_models.CreateFunctionTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_function_task_with_options(workspace_name, function_name, instance_name, request, headers, runtime)

    async def create_function_task_async(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.CreateFunctionTaskRequest,
    ) -> main_models.CreateFunctionTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_function_task_with_options_async(workspace_name, function_name, instance_name, request, headers, runtime)

    def create_offline_task_with_options(
        self,
        workspace_name: str,
        type: str,
        request: main_models.CreateOfflineTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateOfflineTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.draft):
            query['draft'] = request.draft
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.meta):
            body['meta'] = request.meta
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        if not DaraCore.is_null(request.processors):
            body['processors'] = request.processors
        if not DaraCore.is_null(request.sink):
            body['sink'] = request.sink
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOfflineTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/offline-tasks/{DaraURL.percent_encode(type)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOfflineTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_offline_task_with_options_async(
        self,
        workspace_name: str,
        type: str,
        request: main_models.CreateOfflineTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateOfflineTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.draft):
            query['draft'] = request.draft
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.meta):
            body['meta'] = request.meta
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        if not DaraCore.is_null(request.processors):
            body['processors'] = request.processors
        if not DaraCore.is_null(request.sink):
            body['sink'] = request.sink
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOfflineTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/offline-tasks/{DaraURL.percent_encode(type)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOfflineTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_offline_task(
        self,
        workspace_name: str,
        type: str,
        request: main_models.CreateOfflineTaskRequest,
    ) -> main_models.CreateOfflineTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_offline_task_with_options(workspace_name, type, request, headers, runtime)

    async def create_offline_task_async(
        self,
        workspace_name: str,
        type: str,
        request: main_models.CreateOfflineTaskRequest,
    ) -> main_models.CreateOfflineTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_offline_task_with_options_async(workspace_name, type, request, headers, runtime)

    def create_rag_evaluator_task_with_options(
        self,
        workspace_name: str,
        request: main_models.CreateRagEvaluatorTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRagEvaluatorTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['app_name'] = request.app_name
        if not DaraCore.is_null(request.data):
            body['data'] = request.data
        if not DaraCore.is_null(request.data_source_config):
            body['data_source_config'] = request.data_source_config
        if not DaraCore.is_null(request.emails):
            body['emails'] = request.emails
        if not DaraCore.is_null(request.evaluate_config):
            body['evaluate_config'] = request.evaluate_config
        if not DaraCore.is_null(request.has_data_source):
            body['has_data_source'] = request.has_data_source
        if not DaraCore.is_null(request.metrics):
            body['metrics'] = request.metrics
        if not DaraCore.is_null(request.task_name):
            body['task_name'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRagEvaluatorTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/rag-evaluator/v1/api/task',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRagEvaluatorTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rag_evaluator_task_with_options_async(
        self,
        workspace_name: str,
        request: main_models.CreateRagEvaluatorTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRagEvaluatorTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['app_name'] = request.app_name
        if not DaraCore.is_null(request.data):
            body['data'] = request.data
        if not DaraCore.is_null(request.data_source_config):
            body['data_source_config'] = request.data_source_config
        if not DaraCore.is_null(request.emails):
            body['emails'] = request.emails
        if not DaraCore.is_null(request.evaluate_config):
            body['evaluate_config'] = request.evaluate_config
        if not DaraCore.is_null(request.has_data_source):
            body['has_data_source'] = request.has_data_source
        if not DaraCore.is_null(request.metrics):
            body['metrics'] = request.metrics
        if not DaraCore.is_null(request.task_name):
            body['task_name'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRagEvaluatorTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/rag-evaluator/v1/api/task',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRagEvaluatorTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rag_evaluator_task(
        self,
        workspace_name: str,
        request: main_models.CreateRagEvaluatorTaskRequest,
    ) -> main_models.CreateRagEvaluatorTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_rag_evaluator_task_with_options(workspace_name, request, headers, runtime)

    async def create_rag_evaluator_task_async(
        self,
        workspace_name: str,
        request: main_models.CreateRagEvaluatorTaskRequest,
    ) -> main_models.CreateRagEvaluatorTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_rag_evaluator_task_with_options_async(workspace_name, request, headers, runtime)

    def create_workspace_with_options(
        self,
        request: main_models.CreateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkspaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.charge_type):
            body['chargeType'] = request.charge_type
        if not DaraCore.is_null(request.engine_type):
            body['engineType'] = request.engine_type
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.quota):
            body['quota'] = request.quota
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkspace',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workspace_with_options_async(
        self,
        request: main_models.CreateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkspaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.charge_type):
            body['chargeType'] = request.charge_type
        if not DaraCore.is_null(request.engine_type):
            body['engineType'] = request.engine_type
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.quota):
            body['quota'] = request.quota
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkspace',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workspace(
        self,
        request: main_models.CreateWorkspaceRequest,
    ) -> main_models.CreateWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_workspace_with_options(request, headers, runtime)

    async def create_workspace_async(
        self,
        request: main_models.CreateWorkspaceRequest,
    ) -> main_models.CreateWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_workspace_with_options_async(request, headers, runtime)

    def delete_capability_with_options(
        self,
        workspace_name: str,
        item_category: str,
        item_name: str,
        request: main_models.DeleteCapabilityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCapabilityResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteCapability',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/capabilities/{DaraURL.percent_encode(item_category)}/items/{DaraURL.percent_encode(item_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCapabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_capability_with_options_async(
        self,
        workspace_name: str,
        item_category: str,
        item_name: str,
        request: main_models.DeleteCapabilityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCapabilityResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteCapability',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/capabilities/{DaraURL.percent_encode(item_category)}/items/{DaraURL.percent_encode(item_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCapabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_capability(
        self,
        workspace_name: str,
        item_category: str,
        item_name: str,
        request: main_models.DeleteCapabilityRequest,
    ) -> main_models.DeleteCapabilityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_capability_with_options(workspace_name, item_category, item_name, request, headers, runtime)

    async def delete_capability_async(
        self,
        workspace_name: str,
        item_category: str,
        item_name: str,
        request: main_models.DeleteCapabilityRequest,
    ) -> main_models.DeleteCapabilityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_capability_with_options_async(workspace_name, item_category, item_name, request, headers, runtime)

    def delete_config_with_options(
        self,
        workspace_name: str,
        config_type: str,
        id: str,
        request: main_models.DeleteConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConfigResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConfig',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/configs/{DaraURL.percent_encode(config_type)}/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_config_with_options_async(
        self,
        workspace_name: str,
        config_type: str,
        id: str,
        request: main_models.DeleteConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConfigResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConfig',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/configs/{DaraURL.percent_encode(config_type)}/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_config(
        self,
        workspace_name: str,
        config_type: str,
        id: str,
        request: main_models.DeleteConfigRequest,
    ) -> main_models.DeleteConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_config_with_options(workspace_name, config_type, id, request, headers, runtime)

    async def delete_config_async(
        self,
        workspace_name: str,
        config_type: str,
        id: str,
        request: main_models.DeleteConfigRequest,
    ) -> main_models.DeleteConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_config_with_options_async(workspace_name, config_type, id, request, headers, runtime)

    def delete_credentials_with_options(
        self,
        token: str,
        workspace_name: str,
        request: main_models.DeleteCredentialsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCredentialsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteCredentials',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/credentials/{DaraURL.percent_encode(token)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_credentials_with_options_async(
        self,
        token: str,
        workspace_name: str,
        request: main_models.DeleteCredentialsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCredentialsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteCredentials',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/credentials/{DaraURL.percent_encode(token)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_credentials(
        self,
        token: str,
        workspace_name: str,
        request: main_models.DeleteCredentialsRequest,
    ) -> main_models.DeleteCredentialsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_credentials_with_options(token, workspace_name, request, headers, runtime)

    async def delete_credentials_async(
        self,
        token: str,
        workspace_name: str,
        request: main_models.DeleteCredentialsRequest,
    ) -> main_models.DeleteCredentialsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_credentials_with_options_async(token, workspace_name, request, headers, runtime)

    def delete_experience_data_with_options(
        self,
        id: str,
        workspace_name: str,
        request: main_models.DeleteExperienceDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExperienceDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExperienceData',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/experience-data/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExperienceDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_experience_data_with_options_async(
        self,
        id: str,
        workspace_name: str,
        request: main_models.DeleteExperienceDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExperienceDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExperienceData',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/experience-data/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExperienceDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_experience_data(
        self,
        id: str,
        workspace_name: str,
        request: main_models.DeleteExperienceDataRequest,
    ) -> main_models.DeleteExperienceDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_experience_data_with_options(id, workspace_name, request, headers, runtime)

    async def delete_experience_data_async(
        self,
        id: str,
        workspace_name: str,
        request: main_models.DeleteExperienceDataRequest,
    ) -> main_models.DeleteExperienceDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_experience_data_with_options_async(id, workspace_name, request, headers, runtime)

    def delete_function_instance_with_options(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.DeleteFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFunctionInstanceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteFunctionInstance',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFunctionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_function_instance_with_options_async(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.DeleteFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFunctionInstanceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteFunctionInstance',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFunctionInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_function_instance(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.DeleteFunctionInstanceRequest,
    ) -> main_models.DeleteFunctionInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_function_instance_with_options(workspace_name, function_name, instance_name, request, headers, runtime)

    async def delete_function_instance_async(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.DeleteFunctionInstanceRequest,
    ) -> main_models.DeleteFunctionInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_function_instance_with_options_async(workspace_name, function_name, instance_name, request, headers, runtime)

    def delete_offline_task_with_options(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.DeleteOfflineTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOfflineTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOfflineTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/offline-tasks/{DaraURL.percent_encode(type)}/{DaraURL.percent_encode(task_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOfflineTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_offline_task_with_options_async(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.DeleteOfflineTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOfflineTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOfflineTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/offline-tasks/{DaraURL.percent_encode(type)}/{DaraURL.percent_encode(task_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOfflineTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_offline_task(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.DeleteOfflineTaskRequest,
    ) -> main_models.DeleteOfflineTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_offline_task_with_options(workspace_name, type, task_name, request, headers, runtime)

    async def delete_offline_task_async(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.DeleteOfflineTaskRequest,
    ) -> main_models.DeleteOfflineTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_offline_task_with_options_async(workspace_name, type, task_name, request, headers, runtime)

    def delete_rag_evaluator_task_with_options(
        self,
        workspace_name: str,
        task_id: str,
        request: main_models.DeleteRagEvaluatorTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRagEvaluatorTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteRagEvaluatorTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/rag-evaluator/v1/api/task/{DaraURL.percent_encode(task_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRagEvaluatorTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rag_evaluator_task_with_options_async(
        self,
        workspace_name: str,
        task_id: str,
        request: main_models.DeleteRagEvaluatorTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRagEvaluatorTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteRagEvaluatorTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/rag-evaluator/v1/api/task/{DaraURL.percent_encode(task_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRagEvaluatorTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rag_evaluator_task(
        self,
        workspace_name: str,
        task_id: str,
        request: main_models.DeleteRagEvaluatorTaskRequest,
    ) -> main_models.DeleteRagEvaluatorTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_rag_evaluator_task_with_options(workspace_name, task_id, request, headers, runtime)

    async def delete_rag_evaluator_task_async(
        self,
        workspace_name: str,
        task_id: str,
        request: main_models.DeleteRagEvaluatorTaskRequest,
    ) -> main_models.DeleteRagEvaluatorTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_rag_evaluator_task_with_options_async(workspace_name, task_id, request, headers, runtime)

    def delete_workspace_with_options(
        self,
        workspace_name: str,
        request: main_models.DeleteWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkspaceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkspace',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workspace_with_options_async(
        self,
        workspace_name: str,
        request: main_models.DeleteWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkspaceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkspace',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workspace(
        self,
        workspace_name: str,
        request: main_models.DeleteWorkspaceRequest,
    ) -> main_models.DeleteWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_workspace_with_options(workspace_name, request, headers, runtime)

    async def delete_workspace_async(
        self,
        workspace_name: str,
        request: main_models.DeleteWorkspaceRequest,
    ) -> main_models.DeleteWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_workspace_with_options_async(workspace_name, request, headers, runtime)

    def describe_capability_with_options(
        self,
        workspace_name: str,
        item_category: str,
        item_name: str,
        request: main_models.DescribeCapabilityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCapabilityResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeCapability',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/capabilities/{DaraURL.percent_encode(item_category)}/items/{DaraURL.percent_encode(item_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCapabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_capability_with_options_async(
        self,
        workspace_name: str,
        item_category: str,
        item_name: str,
        request: main_models.DescribeCapabilityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCapabilityResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeCapability',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/capabilities/{DaraURL.percent_encode(item_category)}/items/{DaraURL.percent_encode(item_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCapabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_capability(
        self,
        workspace_name: str,
        item_category: str,
        item_name: str,
        request: main_models.DescribeCapabilityRequest,
    ) -> main_models.DescribeCapabilityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_capability_with_options(workspace_name, item_category, item_name, request, headers, runtime)

    async def describe_capability_async(
        self,
        workspace_name: str,
        item_category: str,
        item_name: str,
        request: main_models.DescribeCapabilityRequest,
    ) -> main_models.DescribeCapabilityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_capability_with_options_async(workspace_name, item_category, item_name, request, headers, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/regions',
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
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/regions',
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

    def get_async_task_with_options(
        self,
        workspace_name: str,
        id: str,
        request: main_models.GetAsyncTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAsyncTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/async-tasks/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_task_with_options_async(
        self,
        workspace_name: str,
        id: str,
        request: main_models.GetAsyncTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAsyncTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/async-tasks/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_task(
        self,
        workspace_name: str,
        id: str,
        request: main_models.GetAsyncTaskRequest,
    ) -> main_models.GetAsyncTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_async_task_with_options(workspace_name, id, request, headers, runtime)

    async def get_async_task_async(
        self,
        workspace_name: str,
        id: str,
        request: main_models.GetAsyncTaskRequest,
    ) -> main_models.GetAsyncTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_async_task_with_options_async(workspace_name, id, request, headers, runtime)

    def get_config_with_options(
        self,
        workspace_name: str,
        config_type: str,
        id: str,
        request: main_models.GetConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConfig',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/configs/{DaraURL.percent_encode(config_type)}/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_config_with_options_async(
        self,
        workspace_name: str,
        config_type: str,
        id: str,
        request: main_models.GetConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConfig',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/configs/{DaraURL.percent_encode(config_type)}/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_config(
        self,
        workspace_name: str,
        config_type: str,
        id: str,
        request: main_models.GetConfigRequest,
    ) -> main_models.GetConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_config_with_options(workspace_name, config_type, id, request, headers, runtime)

    async def get_config_async(
        self,
        workspace_name: str,
        config_type: str,
        id: str,
        request: main_models.GetConfigRequest,
    ) -> main_models.GetConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_config_with_options_async(workspace_name, config_type, id, request, headers, runtime)

    def get_credentials_with_options(
        self,
        token: str,
        workspace_name: str,
        request: main_models.GetCredentialsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCredentialsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCredentials',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/credentials/{DaraURL.percent_encode(token)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_credentials_with_options_async(
        self,
        token: str,
        workspace_name: str,
        request: main_models.GetCredentialsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCredentialsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCredentials',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/credentials/{DaraURL.percent_encode(token)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_credentials(
        self,
        token: str,
        workspace_name: str,
        request: main_models.GetCredentialsRequest,
    ) -> main_models.GetCredentialsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_credentials_with_options(token, workspace_name, request, headers, runtime)

    async def get_credentials_async(
        self,
        token: str,
        workspace_name: str,
        request: main_models.GetCredentialsRequest,
    ) -> main_models.GetCredentialsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_credentials_with_options_async(token, workspace_name, request, headers, runtime)

    def get_experience_data_with_options(
        self,
        workspace_name: str,
        id: str,
        request: main_models.GetExperienceDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetExperienceDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExperienceData',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/experience-data/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExperienceDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_experience_data_with_options_async(
        self,
        workspace_name: str,
        id: str,
        request: main_models.GetExperienceDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetExperienceDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExperienceData',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/experience-data/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExperienceDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_experience_data(
        self,
        workspace_name: str,
        id: str,
        request: main_models.GetExperienceDataRequest,
    ) -> main_models.GetExperienceDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_experience_data_with_options(workspace_name, id, request, headers, runtime)

    async def get_experience_data_async(
        self,
        workspace_name: str,
        id: str,
        request: main_models.GetExperienceDataRequest,
    ) -> main_models.GetExperienceDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_experience_data_with_options_async(workspace_name, id, request, headers, runtime)

    def get_function_instance_with_options(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.GetFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFunctionInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.output):
            query['output'] = request.output
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFunctionInstance',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFunctionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_instance_with_options_async(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.GetFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFunctionInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.output):
            query['output'] = request.output
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFunctionInstance',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFunctionInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function_instance(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.GetFunctionInstanceRequest,
    ) -> main_models.GetFunctionInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_function_instance_with_options(workspace_name, function_name, instance_name, request, headers, runtime)

    async def get_function_instance_async(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.GetFunctionInstanceRequest,
    ) -> main_models.GetFunctionInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_function_instance_with_options_async(workspace_name, function_name, instance_name, request, headers, runtime)

    def get_offline_task_with_options(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.GetOfflineTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOfflineTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOfflineTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/offline-tasks/{DaraURL.percent_encode(type)}/{DaraURL.percent_encode(task_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOfflineTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_offline_task_with_options_async(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.GetOfflineTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOfflineTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOfflineTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/offline-tasks/{DaraURL.percent_encode(type)}/{DaraURL.percent_encode(task_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOfflineTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_offline_task(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.GetOfflineTaskRequest,
    ) -> main_models.GetOfflineTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_offline_task_with_options(workspace_name, type, task_name, request, headers, runtime)

    async def get_offline_task_async(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.GetOfflineTaskRequest,
    ) -> main_models.GetOfflineTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_offline_task_with_options_async(workspace_name, type, task_name, request, headers, runtime)

    def get_offline_task_log_with_options(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.GetOfflineTaskLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOfflineTaskLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOfflineTaskLog',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/offline-tasks/{DaraURL.percent_encode(type)}/{DaraURL.percent_encode(task_name)}/log',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOfflineTaskLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_offline_task_log_with_options_async(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.GetOfflineTaskLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOfflineTaskLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOfflineTaskLog',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/offline-tasks/{DaraURL.percent_encode(type)}/{DaraURL.percent_encode(task_name)}/log',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOfflineTaskLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_offline_task_log(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.GetOfflineTaskLogRequest,
    ) -> main_models.GetOfflineTaskLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_offline_task_log_with_options(workspace_name, type, task_name, request, headers, runtime)

    async def get_offline_task_log_async(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.GetOfflineTaskLogRequest,
    ) -> main_models.GetOfflineTaskLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_offline_task_log_with_options_async(workspace_name, type, task_name, request, headers, runtime)

    def get_rag_evaluator_task_with_options(
        self,
        workspace_name: str,
        task_id: str,
        request: main_models.GetRagEvaluatorTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRagEvaluatorTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRagEvaluatorTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/rag-evaluator/v1/api/task/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRagEvaluatorTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rag_evaluator_task_with_options_async(
        self,
        workspace_name: str,
        task_id: str,
        request: main_models.GetRagEvaluatorTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRagEvaluatorTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRagEvaluatorTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/rag-evaluator/v1/api/task/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRagEvaluatorTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rag_evaluator_task(
        self,
        workspace_name: str,
        task_id: str,
        request: main_models.GetRagEvaluatorTaskRequest,
    ) -> main_models.GetRagEvaluatorTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_rag_evaluator_task_with_options(workspace_name, task_id, request, headers, runtime)

    async def get_rag_evaluator_task_async(
        self,
        workspace_name: str,
        task_id: str,
        request: main_models.GetRagEvaluatorTaskRequest,
    ) -> main_models.GetRagEvaluatorTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_rag_evaluator_task_with_options_async(workspace_name, task_id, request, headers, runtime)

    def get_table_columns_with_options(
        self,
        workspace_name: str,
        data_source_type: str,
        request: main_models.GetTableColumnsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTableColumnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.params):
            query['params'] = request.params
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTableColumns',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/data-sources/{DaraURL.percent_encode(data_source_type)}/columns',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_columns_with_options_async(
        self,
        workspace_name: str,
        data_source_type: str,
        request: main_models.GetTableColumnsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTableColumnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.params):
            query['params'] = request.params
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTableColumns',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/data-sources/{DaraURL.percent_encode(data_source_type)}/columns',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableColumnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_columns(
        self,
        workspace_name: str,
        data_source_type: str,
        request: main_models.GetTableColumnsRequest,
    ) -> main_models.GetTableColumnsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_table_columns_with_options(workspace_name, data_source_type, request, headers, runtime)

    async def get_table_columns_async(
        self,
        workspace_name: str,
        data_source_type: str,
        request: main_models.GetTableColumnsRequest,
    ) -> main_models.GetTableColumnsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_table_columns_with_options_async(workspace_name, data_source_type, request, headers, runtime)

    def get_table_fields_with_options(
        self,
        workspace_name: str,
        data_source_type: str,
        request: main_models.GetTableFieldsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTableFieldsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.params):
            query['params'] = request.params
        if not DaraCore.is_null(request.raw_type):
            query['rawType'] = request.raw_type
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTableFields',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/data-sources/{DaraURL.percent_encode(data_source_type)}/fields',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_fields_with_options_async(
        self,
        workspace_name: str,
        data_source_type: str,
        request: main_models.GetTableFieldsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTableFieldsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.params):
            query['params'] = request.params
        if not DaraCore.is_null(request.raw_type):
            query['rawType'] = request.raw_type
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTableFields',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/data-sources/{DaraURL.percent_encode(data_source_type)}/fields',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableFieldsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_fields(
        self,
        workspace_name: str,
        data_source_type: str,
        request: main_models.GetTableFieldsRequest,
    ) -> main_models.GetTableFieldsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_table_fields_with_options(workspace_name, data_source_type, request, headers, runtime)

    async def get_table_fields_async(
        self,
        workspace_name: str,
        data_source_type: str,
        request: main_models.GetTableFieldsRequest,
    ) -> main_models.GetTableFieldsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_table_fields_with_options_async(workspace_name, data_source_type, request, headers, runtime)

    def get_tables_with_options(
        self,
        workspace_name: str,
        data_source_type: str,
        request: main_models.GetTablesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.params):
            query['params'] = request.params
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTables',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/data-sources/{DaraURL.percent_encode(data_source_type)}/tables',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tables_with_options_async(
        self,
        workspace_name: str,
        data_source_type: str,
        request: main_models.GetTablesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.params):
            query['params'] = request.params
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTables',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/data-sources/{DaraURL.percent_encode(data_source_type)}/tables',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tables(
        self,
        workspace_name: str,
        data_source_type: str,
        request: main_models.GetTablesRequest,
    ) -> main_models.GetTablesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_tables_with_options(workspace_name, data_source_type, request, headers, runtime)

    async def get_tables_async(
        self,
        workspace_name: str,
        data_source_type: str,
        request: main_models.GetTablesRequest,
    ) -> main_models.GetTablesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_tables_with_options_async(workspace_name, data_source_type, request, headers, runtime)

    def get_workspace_with_options(
        self,
        workspace_name: str,
        request: main_models.GetWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkspaceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetWorkspace',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workspace_with_options_async(
        self,
        workspace_name: str,
        request: main_models.GetWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkspaceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetWorkspace',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workspace(
        self,
        workspace_name: str,
        request: main_models.GetWorkspaceRequest,
    ) -> main_models.GetWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_workspace_with_options(workspace_name, request, headers, runtime)

    async def get_workspace_async(
        self,
        workspace_name: str,
        request: main_models.GetWorkspaceRequest,
    ) -> main_models.GetWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_workspace_with_options_async(workspace_name, request, headers, runtime)

    def list_async_tasks_with_options(
        self,
        workspace_name: str,
        request: main_models.ListAsyncTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAsyncTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_id):
            query['dataId'] = request.data_id
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.service_type):
            query['serviceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAsyncTasks',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/async-tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAsyncTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_async_tasks_with_options_async(
        self,
        workspace_name: str,
        request: main_models.ListAsyncTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAsyncTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_id):
            query['dataId'] = request.data_id
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.service_type):
            query['serviceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAsyncTasks',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/async-tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAsyncTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_async_tasks(
        self,
        workspace_name: str,
        request: main_models.ListAsyncTasksRequest,
    ) -> main_models.ListAsyncTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_async_tasks_with_options(workspace_name, request, headers, runtime)

    async def list_async_tasks_async(
        self,
        workspace_name: str,
        request: main_models.ListAsyncTasksRequest,
    ) -> main_models.ListAsyncTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_async_tasks_with_options_async(workspace_name, request, headers, runtime)

    def list_capabilities_with_options(
        self,
        workspace_name: str,
        item_category: str,
        request: main_models.ListCapabilitiesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCapabilitiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCapabilities',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/capabilities/{DaraURL.percent_encode(item_category)}/items',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCapabilitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_capabilities_with_options_async(
        self,
        workspace_name: str,
        item_category: str,
        request: main_models.ListCapabilitiesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCapabilitiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCapabilities',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/capabilities/{DaraURL.percent_encode(item_category)}/items',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCapabilitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_capabilities(
        self,
        workspace_name: str,
        item_category: str,
        request: main_models.ListCapabilitiesRequest,
    ) -> main_models.ListCapabilitiesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_capabilities_with_options(workspace_name, item_category, request, headers, runtime)

    async def list_capabilities_async(
        self,
        workspace_name: str,
        item_category: str,
        request: main_models.ListCapabilitiesRequest,
    ) -> main_models.ListCapabilitiesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_capabilities_with_options_async(workspace_name, item_category, request, headers, runtime)

    def list_configs_with_options(
        self,
        workspace_name: str,
        config_type: str,
        request: main_models.ListConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConfigs',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/configs/{DaraURL.percent_encode(config_type)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_configs_with_options_async(
        self,
        workspace_name: str,
        config_type: str,
        request: main_models.ListConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConfigs',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/configs/{DaraURL.percent_encode(config_type)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_configs(
        self,
        workspace_name: str,
        config_type: str,
        request: main_models.ListConfigsRequest,
    ) -> main_models.ListConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_configs_with_options(workspace_name, config_type, request, headers, runtime)

    async def list_configs_async(
        self,
        workspace_name: str,
        config_type: str,
        request: main_models.ListConfigsRequest,
    ) -> main_models.ListConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_configs_with_options_async(workspace_name, config_type, request, headers, runtime)

    def list_credentials_with_options(
        self,
        workspace_name: str,
        request: main_models.ListCredentialsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCredentials',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/credentials',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_credentials_with_options_async(
        self,
        workspace_name: str,
        request: main_models.ListCredentialsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCredentials',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/credentials',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_credentials(
        self,
        workspace_name: str,
        request: main_models.ListCredentialsRequest,
    ) -> main_models.ListCredentialsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_credentials_with_options(workspace_name, request, headers, runtime)

    async def list_credentials_async(
        self,
        workspace_name: str,
        request: main_models.ListCredentialsRequest,
    ) -> main_models.ListCredentialsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_credentials_with_options_async(workspace_name, request, headers, runtime)

    def list_experience_data_with_options(
        self,
        workspace_name: str,
        request: main_models.ListExperienceDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExperienceDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_type):
            query['dataType'] = request.data_type
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.service_type):
            query['serviceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExperienceData',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/experience-data',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExperienceDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_experience_data_with_options_async(
        self,
        workspace_name: str,
        request: main_models.ListExperienceDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExperienceDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_type):
            query['dataType'] = request.data_type
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.service_type):
            query['serviceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExperienceData',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/experience-data',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExperienceDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_experience_data(
        self,
        workspace_name: str,
        request: main_models.ListExperienceDataRequest,
    ) -> main_models.ListExperienceDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_experience_data_with_options(workspace_name, request, headers, runtime)

    async def list_experience_data_async(
        self,
        workspace_name: str,
        request: main_models.ListExperienceDataRequest,
    ) -> main_models.ListExperienceDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_experience_data_with_options_async(workspace_name, request, headers, runtime)

    def list_function_instances_with_options(
        self,
        workspace_name: str,
        function_name: str,
        request: main_models.ListFunctionInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFunctionInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.function_type):
            query['functionType'] = request.function_type
        if not DaraCore.is_null(request.model_type):
            query['modelType'] = request.model_type
        if not DaraCore.is_null(request.output):
            query['output'] = request.output
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFunctionInstances',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/functions/{DaraURL.percent_encode(function_name)}/instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFunctionInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_function_instances_with_options_async(
        self,
        workspace_name: str,
        function_name: str,
        request: main_models.ListFunctionInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFunctionInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.function_type):
            query['functionType'] = request.function_type
        if not DaraCore.is_null(request.model_type):
            query['modelType'] = request.model_type
        if not DaraCore.is_null(request.output):
            query['output'] = request.output
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFunctionInstances',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/functions/{DaraURL.percent_encode(function_name)}/instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFunctionInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_function_instances(
        self,
        workspace_name: str,
        function_name: str,
        request: main_models.ListFunctionInstancesRequest,
    ) -> main_models.ListFunctionInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_function_instances_with_options(workspace_name, function_name, request, headers, runtime)

    async def list_function_instances_async(
        self,
        workspace_name: str,
        function_name: str,
        request: main_models.ListFunctionInstancesRequest,
    ) -> main_models.ListFunctionInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_function_instances_with_options_async(workspace_name, function_name, request, headers, runtime)

    def list_function_restrictions_with_options(
        self,
        workspace_name: str,
        function_name: str,
        restriction_name: str,
        request: main_models.ListFunctionRestrictionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFunctionRestrictionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.model_type):
            query['modelType'] = request.model_type
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFunctionRestrictions',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/functions/{DaraURL.percent_encode(function_name)}/restrictions/{DaraURL.percent_encode(restriction_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFunctionRestrictionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_function_restrictions_with_options_async(
        self,
        workspace_name: str,
        function_name: str,
        restriction_name: str,
        request: main_models.ListFunctionRestrictionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFunctionRestrictionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.model_type):
            query['modelType'] = request.model_type
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFunctionRestrictions',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/functions/{DaraURL.percent_encode(function_name)}/restrictions/{DaraURL.percent_encode(restriction_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFunctionRestrictionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_function_restrictions(
        self,
        workspace_name: str,
        function_name: str,
        restriction_name: str,
        request: main_models.ListFunctionRestrictionsRequest,
    ) -> main_models.ListFunctionRestrictionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_function_restrictions_with_options(workspace_name, function_name, restriction_name, request, headers, runtime)

    async def list_function_restrictions_async(
        self,
        workspace_name: str,
        function_name: str,
        restriction_name: str,
        request: main_models.ListFunctionRestrictionsRequest,
    ) -> main_models.ListFunctionRestrictionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_function_restrictions_with_options_async(workspace_name, function_name, restriction_name, request, headers, runtime)

    def list_offline_task_with_options(
        self,
        workspace_name: str,
        type: str,
        tmp_req: main_models.ListOfflineTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListOfflineTaskResponse:
        tmp_req.validate()
        request = main_models.ListOfflineTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.labels):
            request.labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.labels, 'labels', 'json')
        if not DaraCore.is_null(tmp_req.task_status):
            request.task_status_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_status, 'taskStatus', 'json')
        query = {}
        if not DaraCore.is_null(request.labels_shrink):
            query['labels'] = request.labels_shrink
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.task_name):
            query['taskName'] = request.task_name
        if not DaraCore.is_null(request.task_status_shrink):
            query['taskStatus'] = request.task_status_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOfflineTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/offline-tasks/{DaraURL.percent_encode(type)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOfflineTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_offline_task_with_options_async(
        self,
        workspace_name: str,
        type: str,
        tmp_req: main_models.ListOfflineTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListOfflineTaskResponse:
        tmp_req.validate()
        request = main_models.ListOfflineTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.labels):
            request.labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.labels, 'labels', 'json')
        if not DaraCore.is_null(tmp_req.task_status):
            request.task_status_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_status, 'taskStatus', 'json')
        query = {}
        if not DaraCore.is_null(request.labels_shrink):
            query['labels'] = request.labels_shrink
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.task_name):
            query['taskName'] = request.task_name
        if not DaraCore.is_null(request.task_status_shrink):
            query['taskStatus'] = request.task_status_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOfflineTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/offline-tasks/{DaraURL.percent_encode(type)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOfflineTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_offline_task(
        self,
        workspace_name: str,
        type: str,
        request: main_models.ListOfflineTaskRequest,
    ) -> main_models.ListOfflineTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_offline_task_with_options(workspace_name, type, request, headers, runtime)

    async def list_offline_task_async(
        self,
        workspace_name: str,
        type: str,
        request: main_models.ListOfflineTaskRequest,
    ) -> main_models.ListOfflineTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_offline_task_with_options_async(workspace_name, type, request, headers, runtime)

    def list_offline_task_error_logs_with_options(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.ListOfflineTaskErrorLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListOfflineTaskErrorLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.page_num):
            query['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOfflineTaskErrorLogs',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/offline-tasks/{DaraURL.percent_encode(type)}/{DaraURL.percent_encode(task_name)}/error-logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOfflineTaskErrorLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_offline_task_error_logs_with_options_async(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.ListOfflineTaskErrorLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListOfflineTaskErrorLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.page_num):
            query['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOfflineTaskErrorLogs',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/offline-tasks/{DaraURL.percent_encode(type)}/{DaraURL.percent_encode(task_name)}/error-logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOfflineTaskErrorLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_offline_task_error_logs(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.ListOfflineTaskErrorLogsRequest,
    ) -> main_models.ListOfflineTaskErrorLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_offline_task_error_logs_with_options(workspace_name, type, task_name, request, headers, runtime)

    async def list_offline_task_error_logs_async(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.ListOfflineTaskErrorLogsRequest,
    ) -> main_models.ListOfflineTaskErrorLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_offline_task_error_logs_with_options_async(workspace_name, type, task_name, request, headers, runtime)

    def list_rag_evaluator_tasks_with_options(
        self,
        workspace_name: str,
        request: main_models.ListRagEvaluatorTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRagEvaluatorTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRagEvaluatorTasks',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/rag-evaluator/v1/api/tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRagEvaluatorTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rag_evaluator_tasks_with_options_async(
        self,
        workspace_name: str,
        request: main_models.ListRagEvaluatorTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRagEvaluatorTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRagEvaluatorTasks',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/rag-evaluator/v1/api/tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRagEvaluatorTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rag_evaluator_tasks(
        self,
        workspace_name: str,
        request: main_models.ListRagEvaluatorTasksRequest,
    ) -> main_models.ListRagEvaluatorTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_rag_evaluator_tasks_with_options(workspace_name, request, headers, runtime)

    async def list_rag_evaluator_tasks_async(
        self,
        workspace_name: str,
        request: main_models.ListRagEvaluatorTasksRequest,
    ) -> main_models.ListRagEvaluatorTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_rag_evaluator_tasks_with_options_async(workspace_name, request, headers, runtime)

    def list_services_with_options(
        self,
        workspace_name: str,
        request: main_models.ListServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.model_type):
            query['modelType'] = request.model_type
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.service_id):
            query['serviceId'] = request.service_id
        if not DaraCore.is_null(request.service_type):
            query['serviceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServices',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/services',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_services_with_options_async(
        self,
        workspace_name: str,
        request: main_models.ListServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.model_type):
            query['modelType'] = request.model_type
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.service_id):
            query['serviceId'] = request.service_id
        if not DaraCore.is_null(request.service_type):
            query['serviceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServices',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/services',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_services(
        self,
        workspace_name: str,
        request: main_models.ListServicesRequest,
    ) -> main_models.ListServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_services_with_options(workspace_name, request, headers, runtime)

    async def list_services_async(
        self,
        workspace_name: str,
        request: main_models.ListServicesRequest,
    ) -> main_models.ListServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_services_with_options_async(workspace_name, request, headers, runtime)

    def list_workspaces_with_options(
        self,
        request: main_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sort_by):
            query['sortBy'] = request.sort_by
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaces',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspaces_with_options_async(
        self,
        request: main_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sort_by):
            query['sortBy'] = request.sort_by
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaces',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspaces(
        self,
        request: main_models.ListWorkspacesRequest,
    ) -> main_models.ListWorkspacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_workspaces_with_options(request, headers, runtime)

    async def list_workspaces_async(
        self,
        request: main_models.ListWorkspacesRequest,
    ) -> main_models.ListWorkspacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_workspaces_with_options_async(request, headers, runtime)

    def modify_offline_task_with_options(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.ModifyOfflineTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyOfflineTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.meta):
            body['meta'] = request.meta
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        if not DaraCore.is_null(request.processors):
            body['processors'] = request.processors
        if not DaraCore.is_null(request.sink):
            body['sink'] = request.sink
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyOfflineTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/offline-tasks/{DaraURL.percent_encode(type)}/{DaraURL.percent_encode(task_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyOfflineTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_offline_task_with_options_async(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.ModifyOfflineTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyOfflineTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.meta):
            body['meta'] = request.meta
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        if not DaraCore.is_null(request.processors):
            body['processors'] = request.processors
        if not DaraCore.is_null(request.sink):
            body['sink'] = request.sink
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyOfflineTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/offline-tasks/{DaraURL.percent_encode(type)}/{DaraURL.percent_encode(task_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyOfflineTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_offline_task(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.ModifyOfflineTaskRequest,
    ) -> main_models.ModifyOfflineTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_offline_task_with_options(workspace_name, type, task_name, request, headers, runtime)

    async def modify_offline_task_async(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.ModifyOfflineTaskRequest,
    ) -> main_models.ModifyOfflineTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_offline_task_with_options_async(workspace_name, type, task_name, request, headers, runtime)

    def modify_offline_task_log_with_options(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.ModifyOfflineTaskLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyOfflineTaskLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.network):
            body['network'] = request.network
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyOfflineTaskLog',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/offline-tasks/{DaraURL.percent_encode(type)}/{DaraURL.percent_encode(task_name)}/log',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyOfflineTaskLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_offline_task_log_with_options_async(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.ModifyOfflineTaskLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyOfflineTaskLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.network):
            body['network'] = request.network
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyOfflineTaskLog',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/offline-tasks/{DaraURL.percent_encode(type)}/{DaraURL.percent_encode(task_name)}/log',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyOfflineTaskLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_offline_task_log(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.ModifyOfflineTaskLogRequest,
    ) -> main_models.ModifyOfflineTaskLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_offline_task_log_with_options(workspace_name, type, task_name, request, headers, runtime)

    async def modify_offline_task_log_async(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.ModifyOfflineTaskLogRequest,
    ) -> main_models.ModifyOfflineTaskLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_offline_task_log_with_options_async(workspace_name, type, task_name, request, headers, runtime)

    def resume_function_instance_with_options(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.ResumeFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResumeFunctionInstanceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ResumeFunctionInstance',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}/actions/resume',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeFunctionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_function_instance_with_options_async(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.ResumeFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResumeFunctionInstanceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ResumeFunctionInstance',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}/actions/resume',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeFunctionInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_function_instance(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.ResumeFunctionInstanceRequest,
    ) -> main_models.ResumeFunctionInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.resume_function_instance_with_options(workspace_name, function_name, instance_name, request, headers, runtime)

    async def resume_function_instance_async(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.ResumeFunctionInstanceRequest,
    ) -> main_models.ResumeFunctionInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.resume_function_instance_with_options_async(workspace_name, function_name, instance_name, request, headers, runtime)

    def start_offline_task_with_options(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.StartOfflineTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartOfflineTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.parallelism):
            body['parallelism'] = request.parallelism
        if not DaraCore.is_null(request.timestamp):
            body['timestamp'] = request.timestamp
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartOfflineTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/offline-tasks/{DaraURL.percent_encode(type)}/{DaraURL.percent_encode(task_name)}/actions/start',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartOfflineTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_offline_task_with_options_async(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.StartOfflineTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartOfflineTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.parallelism):
            body['parallelism'] = request.parallelism
        if not DaraCore.is_null(request.timestamp):
            body['timestamp'] = request.timestamp
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartOfflineTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/offline-tasks/{DaraURL.percent_encode(type)}/{DaraURL.percent_encode(task_name)}/actions/start',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartOfflineTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_offline_task(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.StartOfflineTaskRequest,
    ) -> main_models.StartOfflineTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_offline_task_with_options(workspace_name, type, task_name, request, headers, runtime)

    async def start_offline_task_async(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.StartOfflineTaskRequest,
    ) -> main_models.StartOfflineTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_offline_task_with_options_async(workspace_name, type, task_name, request, headers, runtime)

    def stop_offline_task_with_options(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.StopOfflineTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopOfflineTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.parallelism):
            body['parallelism'] = request.parallelism
        if not DaraCore.is_null(request.timestamp):
            body['timestamp'] = request.timestamp
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopOfflineTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/offline-tasks/{DaraURL.percent_encode(type)}/{DaraURL.percent_encode(task_name)}/actions/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopOfflineTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_offline_task_with_options_async(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.StopOfflineTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopOfflineTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.parallelism):
            body['parallelism'] = request.parallelism
        if not DaraCore.is_null(request.timestamp):
            body['timestamp'] = request.timestamp
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopOfflineTask',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/offline-tasks/{DaraURL.percent_encode(type)}/{DaraURL.percent_encode(task_name)}/actions/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopOfflineTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_offline_task(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.StopOfflineTaskRequest,
    ) -> main_models.StopOfflineTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_offline_task_with_options(workspace_name, type, task_name, request, headers, runtime)

    async def stop_offline_task_async(
        self,
        workspace_name: str,
        type: str,
        task_name: str,
        request: main_models.StopOfflineTaskRequest,
    ) -> main_models.StopOfflineTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_offline_task_with_options_async(workspace_name, type, task_name, request, headers, runtime)

    def update_capability_with_options(
        self,
        workspace_name: str,
        item_category: str,
        item_name: str,
        request: main_models.UpdateCapabilityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCapabilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.item_desc):
            body['itemDesc'] = request.item_desc
        if not DaraCore.is_null(request.item_value):
            body['itemValue'] = request.item_value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCapability',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/capabilities/{DaraURL.percent_encode(item_category)}/items/{DaraURL.percent_encode(item_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCapabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_capability_with_options_async(
        self,
        workspace_name: str,
        item_category: str,
        item_name: str,
        request: main_models.UpdateCapabilityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCapabilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.item_desc):
            body['itemDesc'] = request.item_desc
        if not DaraCore.is_null(request.item_value):
            body['itemValue'] = request.item_value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCapability',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/capabilities/{DaraURL.percent_encode(item_category)}/items/{DaraURL.percent_encode(item_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCapabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_capability(
        self,
        workspace_name: str,
        item_category: str,
        item_name: str,
        request: main_models.UpdateCapabilityRequest,
    ) -> main_models.UpdateCapabilityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_capability_with_options(workspace_name, item_category, item_name, request, headers, runtime)

    async def update_capability_async(
        self,
        workspace_name: str,
        item_category: str,
        item_name: str,
        request: main_models.UpdateCapabilityRequest,
    ) -> main_models.UpdateCapabilityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_capability_with_options_async(workspace_name, item_category, item_name, request, headers, runtime)

    def update_config_with_options(
        self,
        workspace_name: str,
        config_type: str,
        request: main_models.UpdateConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.config_data):
            body['configData'] = request.config_data
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConfig',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/configs/{DaraURL.percent_encode(config_type)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_config_with_options_async(
        self,
        workspace_name: str,
        config_type: str,
        request: main_models.UpdateConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.config_data):
            body['configData'] = request.config_data
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConfig',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/configs/{DaraURL.percent_encode(config_type)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_config(
        self,
        workspace_name: str,
        config_type: str,
        request: main_models.UpdateConfigRequest,
    ) -> main_models.UpdateConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_config_with_options(workspace_name, config_type, request, headers, runtime)

    async def update_config_async(
        self,
        workspace_name: str,
        config_type: str,
        request: main_models.UpdateConfigRequest,
    ) -> main_models.UpdateConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_config_with_options_async(workspace_name, config_type, request, headers, runtime)

    def update_credentials_with_options(
        self,
        token: str,
        workspace_name: str,
        request: main_models.UpdateCredentialsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.enabled):
            body['enabled'] = request.enabled
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCredentials',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/credentials/{DaraURL.percent_encode(token)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_credentials_with_options_async(
        self,
        token: str,
        workspace_name: str,
        request: main_models.UpdateCredentialsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.enabled):
            body['enabled'] = request.enabled
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCredentials',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/credentials/{DaraURL.percent_encode(token)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_credentials(
        self,
        token: str,
        workspace_name: str,
        request: main_models.UpdateCredentialsRequest,
    ) -> main_models.UpdateCredentialsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_credentials_with_options(token, workspace_name, request, headers, runtime)

    async def update_credentials_async(
        self,
        token: str,
        workspace_name: str,
        request: main_models.UpdateCredentialsRequest,
    ) -> main_models.UpdateCredentialsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_credentials_with_options_async(token, workspace_name, request, headers, runtime)

    def update_function_instance_with_options(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.UpdateFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFunctionInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.create_parameters):
            body['createParameters'] = request.create_parameters
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFunctionInstance',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFunctionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_function_instance_with_options_async(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.UpdateFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFunctionInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.create_parameters):
            body['createParameters'] = request.create_parameters
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFunctionInstance',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFunctionInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_function_instance(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.UpdateFunctionInstanceRequest,
    ) -> main_models.UpdateFunctionInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_function_instance_with_options(workspace_name, function_name, instance_name, request, headers, runtime)

    async def update_function_instance_async(
        self,
        workspace_name: str,
        function_name: str,
        instance_name: str,
        request: main_models.UpdateFunctionInstanceRequest,
    ) -> main_models.UpdateFunctionInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_function_instance_with_options_async(workspace_name, function_name, instance_name, request, headers, runtime)

    def update_workspace_with_options(
        self,
        workspace_name: str,
        request: main_models.UpdateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkspaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkspace',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workspace_with_options_async(
        self,
        workspace_name: str,
        request: main_models.UpdateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkspaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkspace',
            version = '2024-04-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/platform/workspaces/{DaraURL.percent_encode(workspace_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workspace(
        self,
        workspace_name: str,
        request: main_models.UpdateWorkspaceRequest,
    ) -> main_models.UpdateWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_workspace_with_options(workspace_name, request, headers, runtime)

    async def update_workspace_async(
        self,
        workspace_name: str,
        request: main_models.UpdateWorkspaceRequest,
    ) -> main_models.UpdateWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_workspace_with_options_async(workspace_name, request, headers, runtime)
