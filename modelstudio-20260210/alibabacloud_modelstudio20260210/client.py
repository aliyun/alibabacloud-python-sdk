# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_modelstudio20260210 import models as main_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('modelstudio', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_api_key_with_options(
        self,
        request: main_models.CreateApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateApiKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApiKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_key_with_options_async(
        self,
        request: main_models.CreateApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateApiKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApiKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api_key(
        self,
        request: main_models.CreateApiKeyRequest,
    ) -> main_models.CreateApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_api_key_with_options(request, headers, runtime)

    async def create_api_key_async(
        self,
        request: main_models.CreateApiKeyRequest,
    ) -> main_models.CreateApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_api_key_with_options_async(request, headers, runtime)

    def create_workspace_with_options(
        self,
        request: main_models.CreateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service_site):
            query['serviceSite'] = request.service_site
        if not DaraCore.is_null(request.workspace_name):
            query['workspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkspace',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/workspaces',
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
        query = {}
        if not DaraCore.is_null(request.service_site):
            query['serviceSite'] = request.service_site
        if not DaraCore.is_null(request.workspace_name):
            query['workspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkspace',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/workspaces',
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

    def delete_api_key_with_options(
        self,
        api_key_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApiKeyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteApiKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys/{DaraURL.percent_encode(api_key_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_api_key_with_options_async(
        self,
        api_key_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApiKeyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteApiKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys/{DaraURL.percent_encode(api_key_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_api_key(
        self,
        api_key_id: str,
    ) -> main_models.DeleteApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_api_key_with_options(api_key_id, headers, runtime)

    async def delete_api_key_async(
        self,
        api_key_id: str,
    ) -> main_models.DeleteApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_api_key_with_options_async(api_key_id, headers, runtime)

    def get_api_key_with_options(
        self,
        api_key_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetApiKeyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetApiKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys/{DaraURL.percent_encode(api_key_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_api_key_with_options_async(
        self,
        api_key_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetApiKeyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetApiKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys/{DaraURL.percent_encode(api_key_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_api_key(
        self,
        api_key_id: str,
    ) -> main_models.GetApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_api_key_with_options(api_key_id, headers, runtime)

    async def get_api_key_async(
        self,
        api_key_id: str,
    ) -> main_models.GetApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_api_key_with_options_async(api_key_id, headers, runtime)

    def list_api_keys_with_options(
        self,
        request: main_models.ListApiKeysRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApiKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_key_id):
            query['apiKeyId'] = request.api_key_id
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiKeys',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_api_keys_with_options_async(
        self,
        request: main_models.ListApiKeysRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApiKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_key_id):
            query['apiKeyId'] = request.api_key_id
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiKeys',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_api_keys(
        self,
        request: main_models.ListApiKeysRequest,
    ) -> main_models.ListApiKeysResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_api_keys_with_options(request, headers, runtime)

    async def list_api_keys_async(
        self,
        request: main_models.ListApiKeysRequest,
    ) -> main_models.ListApiKeysResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_api_keys_with_options_async(request, headers, runtime)

    def list_workspaces_with_options(
        self,
        request: main_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.workspace_name):
            query['workspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaces',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/workspaces',
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
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.workspace_name):
            query['workspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaces',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/workspaces',
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

    def update_api_key_with_options(
        self,
        api_key_id: str,
        request: main_models.UpdateApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApiKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApiKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys/{DaraURL.percent_encode(api_key_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_api_key_with_options_async(
        self,
        api_key_id: str,
        request: main_models.UpdateApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApiKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApiKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys/{DaraURL.percent_encode(api_key_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_api_key(
        self,
        api_key_id: str,
        request: main_models.UpdateApiKeyRequest,
    ) -> main_models.UpdateApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_api_key_with_options(api_key_id, request, headers, runtime)

    async def update_api_key_async(
        self,
        api_key_id: str,
        request: main_models.UpdateApiKeyRequest,
    ) -> main_models.UpdateApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_api_key_with_options_async(api_key_id, request, headers, runtime)
