# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agentcore20260804 import models as main_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('agentcore', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def batch_delete_models_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.BatchDeleteModelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteModelsResponse:
        tmp_req.validate()
        request = main_models.BatchDeleteModelsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteModels',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models/actions/batch-delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_models_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.BatchDeleteModelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteModelsResponse:
        tmp_req.validate()
        request = main_models.BatchDeleteModelsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteModels',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models/actions/batch-delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_models(
        self,
        workspace_id: str,
        request: main_models.BatchDeleteModelsRequest,
    ) -> main_models.BatchDeleteModelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_delete_models_with_options(workspace_id, request, headers, runtime)

    async def batch_delete_models_async(
        self,
        workspace_id: str,
        request: main_models.BatchDeleteModelsRequest,
    ) -> main_models.BatchDeleteModelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_delete_models_with_options_async(workspace_id, request, headers, runtime)

    def create_credential_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateCredentialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCredentialResponse:
        tmp_req.validate()
        request = main_models.CreateCredentialShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCredential',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/credentials',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_credential_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateCredentialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCredentialResponse:
        tmp_req.validate()
        request = main_models.CreateCredentialShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCredential',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/credentials',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_credential(
        self,
        workspace_id: str,
        request: main_models.CreateCredentialRequest,
    ) -> main_models.CreateCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_credential_with_options(workspace_id, request, headers, runtime)

    async def create_credential_async(
        self,
        workspace_id: str,
        request: main_models.CreateCredentialRequest,
    ) -> main_models.CreateCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_credential_with_options_async(workspace_id, request, headers, runtime)

    def create_identity_provider_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateIdentityProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIdentityProviderResponse:
        tmp_req.validate()
        request = main_models.CreateIdentityProviderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIdentityProvider',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/identity-providers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_identity_provider_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateIdentityProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIdentityProviderResponse:
        tmp_req.validate()
        request = main_models.CreateIdentityProviderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIdentityProvider',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/identity-providers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_identity_provider(
        self,
        workspace_id: str,
        request: main_models.CreateIdentityProviderRequest,
    ) -> main_models.CreateIdentityProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_identity_provider_with_options(workspace_id, request, headers, runtime)

    async def create_identity_provider_async(
        self,
        workspace_id: str,
        request: main_models.CreateIdentityProviderRequest,
    ) -> main_models.CreateIdentityProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_identity_provider_with_options_async(workspace_id, request, headers, runtime)

    def create_managed_agent_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateManagedAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateManagedAgentResponse:
        tmp_req.validate()
        request = main_models.CreateManagedAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateManagedAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/managed-agents',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateManagedAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_managed_agent_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateManagedAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateManagedAgentResponse:
        tmp_req.validate()
        request = main_models.CreateManagedAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateManagedAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/managed-agents',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateManagedAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_managed_agent(
        self,
        workspace_id: str,
        request: main_models.CreateManagedAgentRequest,
    ) -> main_models.CreateManagedAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_managed_agent_with_options(workspace_id, request, headers, runtime)

    async def create_managed_agent_async(
        self,
        workspace_id: str,
        request: main_models.CreateManagedAgentRequest,
    ) -> main_models.CreateManagedAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_managed_agent_with_options_async(workspace_id, request, headers, runtime)

    def create_model_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelResponse:
        tmp_req.validate()
        request = main_models.CreateModelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelResponse:
        tmp_req.validate()
        request = main_models.CreateModelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model(
        self,
        workspace_id: str,
        request: main_models.CreateModelRequest,
    ) -> main_models.CreateModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_model_with_options(workspace_id, request, headers, runtime)

    async def create_model_async(
        self,
        workspace_id: str,
        request: main_models.CreateModelRequest,
    ) -> main_models.CreateModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_model_with_options_async(workspace_id, request, headers, runtime)

    def create_model_connection_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateModelConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelConnectionResponse:
        tmp_req.validate()
        request = main_models.CreateModelConnectionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModelConnection',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/model-connections',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_connection_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateModelConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelConnectionResponse:
        tmp_req.validate()
        request = main_models.CreateModelConnectionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModelConnection',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/model-connections',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model_connection(
        self,
        workspace_id: str,
        request: main_models.CreateModelConnectionRequest,
    ) -> main_models.CreateModelConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_model_connection_with_options(workspace_id, request, headers, runtime)

    async def create_model_connection_async(
        self,
        workspace_id: str,
        request: main_models.CreateModelConnectionRequest,
    ) -> main_models.CreateModelConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_model_connection_with_options_async(workspace_id, request, headers, runtime)

    def create_team_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTeamResponse:
        tmp_req.validate()
        request = main_models.CreateTeamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTeam',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/teams',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTeamResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_team_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTeamResponse:
        tmp_req.validate()
        request = main_models.CreateTeamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTeam',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/teams',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTeamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_team(
        self,
        workspace_id: str,
        request: main_models.CreateTeamRequest,
    ) -> main_models.CreateTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_team_with_options(workspace_id, request, headers, runtime)

    async def create_team_async(
        self,
        workspace_id: str,
        request: main_models.CreateTeamRequest,
    ) -> main_models.CreateTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_team_with_options_async(workspace_id, request, headers, runtime)

    def create_user_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        tmp_req.validate()
        request = main_models.CreateUserShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        tmp_req.validate()
        request = main_models.CreateUserShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user(
        self,
        workspace_id: str,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_user_with_options(workspace_id, request, headers, runtime)

    async def create_user_async(
        self,
        workspace_id: str,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_user_with_options_async(workspace_id, request, headers, runtime)

    def create_workspace_with_options(
        self,
        tmp_req: main_models.CreateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkspaceResponse:
        tmp_req.validate()
        request = main_models.CreateWorkspaceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkspace',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workspace_with_options_async(
        self,
        tmp_req: main_models.CreateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkspaceResponse:
        tmp_req.validate()
        request = main_models.CreateWorkspaceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkspace',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
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

    def debug_model_with_options(
        self,
        workspace_id: str,
        model_id: str,
        tmp_req: main_models.DebugModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DebugModelResponse:
        tmp_req.validate()
        request = main_models.DebugModelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DebugModel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models/{DaraURL.percent_encode(model_id)}/actions/debug',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DebugModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def debug_model_with_options_async(
        self,
        workspace_id: str,
        model_id: str,
        tmp_req: main_models.DebugModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DebugModelResponse:
        tmp_req.validate()
        request = main_models.DebugModelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DebugModel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models/{DaraURL.percent_encode(model_id)}/actions/debug',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DebugModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def debug_model(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.DebugModelRequest,
    ) -> main_models.DebugModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.debug_model_with_options(workspace_id, model_id, request, headers, runtime)

    async def debug_model_async(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.DebugModelRequest,
    ) -> main_models.DebugModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.debug_model_with_options_async(workspace_id, model_id, request, headers, runtime)

    def delete_credential_with_options(
        self,
        workspace_id: str,
        credential_id: str,
        request: main_models.DeleteCredentialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCredential',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/credentials/{DaraURL.percent_encode(credential_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_credential_with_options_async(
        self,
        workspace_id: str,
        credential_id: str,
        request: main_models.DeleteCredentialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCredential',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/credentials/{DaraURL.percent_encode(credential_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_credential(
        self,
        workspace_id: str,
        credential_id: str,
        request: main_models.DeleteCredentialRequest,
    ) -> main_models.DeleteCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_credential_with_options(workspace_id, credential_id, request, headers, runtime)

    async def delete_credential_async(
        self,
        workspace_id: str,
        credential_id: str,
        request: main_models.DeleteCredentialRequest,
    ) -> main_models.DeleteCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_credential_with_options_async(workspace_id, credential_id, request, headers, runtime)

    def delete_identity_provider_with_options(
        self,
        workspace_id: str,
        identity_provider_type: str,
        request: main_models.DeleteIdentityProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIdentityProvider',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/identity-providers/{DaraURL.percent_encode(identity_provider_type)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_identity_provider_with_options_async(
        self,
        workspace_id: str,
        identity_provider_type: str,
        request: main_models.DeleteIdentityProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIdentityProvider',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/identity-providers/{DaraURL.percent_encode(identity_provider_type)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_identity_provider(
        self,
        workspace_id: str,
        identity_provider_type: str,
        request: main_models.DeleteIdentityProviderRequest,
    ) -> main_models.DeleteIdentityProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_identity_provider_with_options(workspace_id, identity_provider_type, request, headers, runtime)

    async def delete_identity_provider_async(
        self,
        workspace_id: str,
        identity_provider_type: str,
        request: main_models.DeleteIdentityProviderRequest,
    ) -> main_models.DeleteIdentityProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_identity_provider_with_options_async(workspace_id, identity_provider_type, request, headers, runtime)

    def delete_managed_agent_with_options(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.DeleteManagedAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteManagedAgentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteManagedAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/managed-agents/{DaraURL.percent_encode(agent_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteManagedAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_managed_agent_with_options_async(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.DeleteManagedAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteManagedAgentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteManagedAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/managed-agents/{DaraURL.percent_encode(agent_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteManagedAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_managed_agent(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.DeleteManagedAgentRequest,
    ) -> main_models.DeleteManagedAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_managed_agent_with_options(workspace_id, agent_id, request, headers, runtime)

    async def delete_managed_agent_async(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.DeleteManagedAgentRequest,
    ) -> main_models.DeleteManagedAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_managed_agent_with_options_async(workspace_id, agent_id, request, headers, runtime)

    def delete_model_with_options(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.DeleteModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteModel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models/{DaraURL.percent_encode(model_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_with_options_async(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.DeleteModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteModel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models/{DaraURL.percent_encode(model_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.DeleteModelRequest,
    ) -> main_models.DeleteModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_model_with_options(workspace_id, model_id, request, headers, runtime)

    async def delete_model_async(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.DeleteModelRequest,
    ) -> main_models.DeleteModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_model_with_options_async(workspace_id, model_id, request, headers, runtime)

    def delete_model_connection_with_options(
        self,
        workspace_id: str,
        connection_id: str,
        request: main_models.DeleteModelConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteModelConnection',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/model-connections/{DaraURL.percent_encode(connection_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_connection_with_options_async(
        self,
        workspace_id: str,
        connection_id: str,
        request: main_models.DeleteModelConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteModelConnection',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/model-connections/{DaraURL.percent_encode(connection_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model_connection(
        self,
        workspace_id: str,
        connection_id: str,
        request: main_models.DeleteModelConnectionRequest,
    ) -> main_models.DeleteModelConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_model_connection_with_options(workspace_id, connection_id, request, headers, runtime)

    async def delete_model_connection_async(
        self,
        workspace_id: str,
        connection_id: str,
        request: main_models.DeleteModelConnectionRequest,
    ) -> main_models.DeleteModelConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_model_connection_with_options_async(workspace_id, connection_id, request, headers, runtime)

    def delete_team_with_options(
        self,
        workspace_id: str,
        team_id: str,
        request: main_models.DeleteTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTeamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTeam',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/teams/{DaraURL.percent_encode(team_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTeamResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_team_with_options_async(
        self,
        workspace_id: str,
        team_id: str,
        request: main_models.DeleteTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTeamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTeam',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/teams/{DaraURL.percent_encode(team_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTeamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_team(
        self,
        workspace_id: str,
        team_id: str,
        request: main_models.DeleteTeamRequest,
    ) -> main_models.DeleteTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_team_with_options(workspace_id, team_id, request, headers, runtime)

    async def delete_team_async(
        self,
        workspace_id: str,
        team_id: str,
        request: main_models.DeleteTeamRequest,
    ) -> main_models.DeleteTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_team_with_options_async(workspace_id, team_id, request, headers, runtime)

    def delete_user_with_options(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        request: main_models.DeleteUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users/{DaraURL.percent_encode(agent_core_user_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        request: main_models.DeleteUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users/{DaraURL.percent_encode(agent_core_user_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        request: main_models.DeleteUserRequest,
    ) -> main_models.DeleteUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_user_with_options(workspace_id, agent_core_user_id, request, headers, runtime)

    async def delete_user_async(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        request: main_models.DeleteUserRequest,
    ) -> main_models.DeleteUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_user_with_options_async(workspace_id, agent_core_user_id, request, headers, runtime)

    def delete_workspace_with_options(
        self,
        workspace_id: str,
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
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}',
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
        workspace_id: str,
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
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}',
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
        workspace_id: str,
        request: main_models.DeleteWorkspaceRequest,
    ) -> main_models.DeleteWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_workspace_with_options(workspace_id, request, headers, runtime)

    async def delete_workspace_async(
        self,
        workspace_id: str,
        request: main_models.DeleteWorkspaceRequest,
    ) -> main_models.DeleteWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_workspace_with_options_async(workspace_id, request, headers, runtime)

    def get_credential_with_options(
        self,
        workspace_id: str,
        credential_id: str,
        request: main_models.GetCredentialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCredentialResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCredential',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/credentials/{DaraURL.percent_encode(credential_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_credential_with_options_async(
        self,
        workspace_id: str,
        credential_id: str,
        request: main_models.GetCredentialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCredentialResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCredential',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/credentials/{DaraURL.percent_encode(credential_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_credential(
        self,
        workspace_id: str,
        credential_id: str,
        request: main_models.GetCredentialRequest,
    ) -> main_models.GetCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_credential_with_options(workspace_id, credential_id, request, headers, runtime)

    async def get_credential_async(
        self,
        workspace_id: str,
        credential_id: str,
        request: main_models.GetCredentialRequest,
    ) -> main_models.GetCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_credential_with_options_async(workspace_id, credential_id, request, headers, runtime)

    def get_identity_provider_with_options(
        self,
        workspace_id: str,
        identity_provider_type: str,
        request: main_models.GetIdentityProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIdentityProviderResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetIdentityProvider',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/identity-providers/{DaraURL.percent_encode(identity_provider_type)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_identity_provider_with_options_async(
        self,
        workspace_id: str,
        identity_provider_type: str,
        request: main_models.GetIdentityProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIdentityProviderResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetIdentityProvider',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/identity-providers/{DaraURL.percent_encode(identity_provider_type)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_identity_provider(
        self,
        workspace_id: str,
        identity_provider_type: str,
        request: main_models.GetIdentityProviderRequest,
    ) -> main_models.GetIdentityProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_identity_provider_with_options(workspace_id, identity_provider_type, request, headers, runtime)

    async def get_identity_provider_async(
        self,
        workspace_id: str,
        identity_provider_type: str,
        request: main_models.GetIdentityProviderRequest,
    ) -> main_models.GetIdentityProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_identity_provider_with_options_async(workspace_id, identity_provider_type, request, headers, runtime)

    def get_managed_agent_with_options(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.GetManagedAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetManagedAgentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetManagedAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/managed-agents/{DaraURL.percent_encode(agent_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetManagedAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_managed_agent_with_options_async(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.GetManagedAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetManagedAgentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetManagedAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/managed-agents/{DaraURL.percent_encode(agent_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetManagedAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_managed_agent(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.GetManagedAgentRequest,
    ) -> main_models.GetManagedAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_managed_agent_with_options(workspace_id, agent_id, request, headers, runtime)

    async def get_managed_agent_async(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.GetManagedAgentRequest,
    ) -> main_models.GetManagedAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_managed_agent_with_options_async(workspace_id, agent_id, request, headers, runtime)

    def get_model_with_options(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.GetModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModelResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models/{DaraURL.percent_encode(model_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_with_options_async(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.GetModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModelResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models/{DaraURL.percent_encode(model_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.GetModelRequest,
    ) -> main_models.GetModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_model_with_options(workspace_id, model_id, request, headers, runtime)

    async def get_model_async(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.GetModelRequest,
    ) -> main_models.GetModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_model_with_options_async(workspace_id, model_id, request, headers, runtime)

    def get_model_connection_with_options(
        self,
        workspace_id: str,
        connection_id: str,
        request: main_models.GetModelConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModelConnectionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModelConnection',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/model-connections/{DaraURL.percent_encode(connection_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_connection_with_options_async(
        self,
        workspace_id: str,
        connection_id: str,
        request: main_models.GetModelConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModelConnectionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModelConnection',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/model-connections/{DaraURL.percent_encode(connection_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model_connection(
        self,
        workspace_id: str,
        connection_id: str,
        request: main_models.GetModelConnectionRequest,
    ) -> main_models.GetModelConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_model_connection_with_options(workspace_id, connection_id, request, headers, runtime)

    async def get_model_connection_async(
        self,
        workspace_id: str,
        connection_id: str,
        request: main_models.GetModelConnectionRequest,
    ) -> main_models.GetModelConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_model_connection_with_options_async(workspace_id, connection_id, request, headers, runtime)

    def get_team_with_options(
        self,
        workspace_id: str,
        team_id: str,
        request: main_models.GetTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTeamResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTeam',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/teams/{DaraURL.percent_encode(team_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTeamResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_team_with_options_async(
        self,
        workspace_id: str,
        team_id: str,
        request: main_models.GetTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTeamResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTeam',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/teams/{DaraURL.percent_encode(team_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTeamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_team(
        self,
        workspace_id: str,
        team_id: str,
        request: main_models.GetTeamRequest,
    ) -> main_models.GetTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_team_with_options(workspace_id, team_id, request, headers, runtime)

    async def get_team_async(
        self,
        workspace_id: str,
        team_id: str,
        request: main_models.GetTeamRequest,
    ) -> main_models.GetTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_team_with_options_async(workspace_id, team_id, request, headers, runtime)

    def get_user_with_options(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        request: main_models.GetUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users/{DaraURL.percent_encode(agent_core_user_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        request: main_models.GetUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users/{DaraURL.percent_encode(agent_core_user_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        request: main_models.GetUserRequest,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_user_with_options(workspace_id, agent_core_user_id, request, headers, runtime)

    async def get_user_async(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        request: main_models.GetUserRequest,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_user_with_options_async(workspace_id, agent_core_user_id, request, headers, runtime)

    def get_workspace_with_options(
        self,
        workspace_id: str,
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
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}',
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
        workspace_id: str,
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
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}',
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
        workspace_id: str,
        request: main_models.GetWorkspaceRequest,
    ) -> main_models.GetWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_workspace_with_options(workspace_id, request, headers, runtime)

    async def get_workspace_async(
        self,
        workspace_id: str,
        request: main_models.GetWorkspaceRequest,
    ) -> main_models.GetWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_workspace_with_options_async(workspace_id, request, headers, runtime)

    def list_credentials_with_options(
        self,
        workspace_id: str,
        request: main_models.ListCredentialsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.credential_type):
            query['credentialType'] = request.credential_type
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCredentials',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/credentials',
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
        workspace_id: str,
        request: main_models.ListCredentialsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.credential_type):
            query['credentialType'] = request.credential_type
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCredentials',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/credentials',
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
        workspace_id: str,
        request: main_models.ListCredentialsRequest,
    ) -> main_models.ListCredentialsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_credentials_with_options(workspace_id, request, headers, runtime)

    async def list_credentials_async(
        self,
        workspace_id: str,
        request: main_models.ListCredentialsRequest,
    ) -> main_models.ListCredentialsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_credentials_with_options_async(workspace_id, request, headers, runtime)

    def list_identity_providers_with_options(
        self,
        workspace_id: str,
        request: main_models.ListIdentityProvidersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIdentityProvidersResponse:
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
            action = 'ListIdentityProviders',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/identity-providers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIdentityProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_identity_providers_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListIdentityProvidersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIdentityProvidersResponse:
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
            action = 'ListIdentityProviders',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/identity-providers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIdentityProvidersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_identity_providers(
        self,
        workspace_id: str,
        request: main_models.ListIdentityProvidersRequest,
    ) -> main_models.ListIdentityProvidersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_identity_providers_with_options(workspace_id, request, headers, runtime)

    async def list_identity_providers_async(
        self,
        workspace_id: str,
        request: main_models.ListIdentityProvidersRequest,
    ) -> main_models.ListIdentityProvidersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_identity_providers_with_options_async(workspace_id, request, headers, runtime)

    def list_managed_agents_with_options(
        self,
        workspace_id: str,
        request: main_models.ListManagedAgentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListManagedAgentsResponse:
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
            action = 'ListManagedAgents',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/managed-agents',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListManagedAgentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_managed_agents_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListManagedAgentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListManagedAgentsResponse:
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
            action = 'ListManagedAgents',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/managed-agents',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListManagedAgentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_managed_agents(
        self,
        workspace_id: str,
        request: main_models.ListManagedAgentsRequest,
    ) -> main_models.ListManagedAgentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_managed_agents_with_options(workspace_id, request, headers, runtime)

    async def list_managed_agents_async(
        self,
        workspace_id: str,
        request: main_models.ListManagedAgentsRequest,
    ) -> main_models.ListManagedAgentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_managed_agents_with_options_async(workspace_id, request, headers, runtime)

    def list_model_connections_with_options(
        self,
        workspace_id: str,
        request: main_models.ListModelConnectionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelConnectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_models):
            query['includeModels'] = request.include_models
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.protocol):
            query['protocol'] = request.protocol
        if not DaraCore.is_null(request.provider_type):
            query['providerType'] = request.provider_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelConnections',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/model-connections',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_model_connections_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListModelConnectionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelConnectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_models):
            query['includeModels'] = request.include_models
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.protocol):
            query['protocol'] = request.protocol
        if not DaraCore.is_null(request.provider_type):
            query['providerType'] = request.provider_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelConnections',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/model-connections',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelConnectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_model_connections(
        self,
        workspace_id: str,
        request: main_models.ListModelConnectionsRequest,
    ) -> main_models.ListModelConnectionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_model_connections_with_options(workspace_id, request, headers, runtime)

    async def list_model_connections_async(
        self,
        workspace_id: str,
        request: main_models.ListModelConnectionsRequest,
    ) -> main_models.ListModelConnectionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_model_connections_with_options_async(workspace_id, request, headers, runtime)

    def list_models_with_options(
        self,
        workspace_id: str,
        request: main_models.ListModelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_id):
            query['connectionId'] = request.connection_id
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.model_name):
            query['modelName'] = request.model_name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModels',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_models_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListModelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_id):
            query['connectionId'] = request.connection_id
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.model_name):
            query['modelName'] = request.model_name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModels',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_models(
        self,
        workspace_id: str,
        request: main_models.ListModelsRequest,
    ) -> main_models.ListModelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_models_with_options(workspace_id, request, headers, runtime)

    async def list_models_async(
        self,
        workspace_id: str,
        request: main_models.ListModelsRequest,
    ) -> main_models.ListModelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_models_with_options_async(workspace_id, request, headers, runtime)

    def list_predefined_model_providers_with_options(
        self,
        request: main_models.ListPredefinedModelProvidersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPredefinedModelProvidersResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListPredefinedModelProviders',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/model-catalog/providers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPredefinedModelProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_predefined_model_providers_with_options_async(
        self,
        request: main_models.ListPredefinedModelProvidersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPredefinedModelProvidersResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListPredefinedModelProviders',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/model-catalog/providers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPredefinedModelProvidersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_predefined_model_providers(
        self,
        request: main_models.ListPredefinedModelProvidersRequest,
    ) -> main_models.ListPredefinedModelProvidersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_predefined_model_providers_with_options(request, headers, runtime)

    async def list_predefined_model_providers_async(
        self,
        request: main_models.ListPredefinedModelProvidersRequest,
    ) -> main_models.ListPredefinedModelProvidersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_predefined_model_providers_with_options_async(request, headers, runtime)

    def list_predefined_models_with_options(
        self,
        provider_type: str,
        request: main_models.ListPredefinedModelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPredefinedModelsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListPredefinedModels',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/model-catalog/providers/{DaraURL.percent_encode(provider_type)}/models',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPredefinedModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_predefined_models_with_options_async(
        self,
        provider_type: str,
        request: main_models.ListPredefinedModelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPredefinedModelsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListPredefinedModels',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/model-catalog/providers/{DaraURL.percent_encode(provider_type)}/models',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPredefinedModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_predefined_models(
        self,
        provider_type: str,
        request: main_models.ListPredefinedModelsRequest,
    ) -> main_models.ListPredefinedModelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_predefined_models_with_options(provider_type, request, headers, runtime)

    async def list_predefined_models_async(
        self,
        provider_type: str,
        request: main_models.ListPredefinedModelsRequest,
    ) -> main_models.ListPredefinedModelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_predefined_models_with_options_async(provider_type, request, headers, runtime)

    def list_teams_with_options(
        self,
        workspace_id: str,
        request: main_models.ListTeamsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTeamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTeams',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/teams',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTeamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_teams_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListTeamsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTeamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTeams',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/teams',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTeamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_teams(
        self,
        workspace_id: str,
        request: main_models.ListTeamsRequest,
    ) -> main_models.ListTeamsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_teams_with_options(workspace_id, request, headers, runtime)

    async def list_teams_async(
        self,
        workspace_id: str,
        request: main_models.ListTeamsRequest,
    ) -> main_models.ListTeamsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_teams_with_options_async(workspace_id, request, headers, runtime)

    def list_users_with_options(
        self,
        workspace_id: str,
        request: main_models.ListUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        workspace_id: str,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_users_with_options(workspace_id, request, headers, runtime)

    async def list_users_async(
        self,
        workspace_id: str,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_users_with_options_async(workspace_id, request, headers, runtime)

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
        if not DaraCore.is_null(request.skip):
            query['skip'] = request.skip
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaces',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces',
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
        if not DaraCore.is_null(request.skip):
            query['skip'] = request.skip
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaces',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces',
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

    def reset_user_password_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.ResetUserPasswordRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResetUserPasswordResponse:
        tmp_req.validate()
        request = main_models.ResetUserPasswordShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetUserPassword',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users/actions/reset-password',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_user_password_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.ResetUserPasswordRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResetUserPasswordResponse:
        tmp_req.validate()
        request = main_models.ResetUserPasswordShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetUserPassword',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users/actions/reset-password',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_user_password(
        self,
        workspace_id: str,
        request: main_models.ResetUserPasswordRequest,
    ) -> main_models.ResetUserPasswordResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.reset_user_password_with_options(workspace_id, request, headers, runtime)

    async def reset_user_password_async(
        self,
        workspace_id: str,
        request: main_models.ResetUserPasswordRequest,
    ) -> main_models.ResetUserPasswordResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.reset_user_password_with_options_async(workspace_id, request, headers, runtime)

    def update_credential_with_options(
        self,
        workspace_id: str,
        credential_id: str,
        tmp_req: main_models.UpdateCredentialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCredentialResponse:
        tmp_req.validate()
        request = main_models.UpdateCredentialShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCredential',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/credentials/{DaraURL.percent_encode(credential_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_credential_with_options_async(
        self,
        workspace_id: str,
        credential_id: str,
        tmp_req: main_models.UpdateCredentialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCredentialResponse:
        tmp_req.validate()
        request = main_models.UpdateCredentialShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCredential',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/credentials/{DaraURL.percent_encode(credential_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_credential(
        self,
        workspace_id: str,
        credential_id: str,
        request: main_models.UpdateCredentialRequest,
    ) -> main_models.UpdateCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_credential_with_options(workspace_id, credential_id, request, headers, runtime)

    async def update_credential_async(
        self,
        workspace_id: str,
        credential_id: str,
        request: main_models.UpdateCredentialRequest,
    ) -> main_models.UpdateCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_credential_with_options_async(workspace_id, credential_id, request, headers, runtime)

    def update_identity_provider_with_options(
        self,
        workspace_id: str,
        identity_provider_type: str,
        tmp_req: main_models.UpdateIdentityProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIdentityProviderResponse:
        tmp_req.validate()
        request = main_models.UpdateIdentityProviderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIdentityProvider',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/identity-providers/{DaraURL.percent_encode(identity_provider_type)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_identity_provider_with_options_async(
        self,
        workspace_id: str,
        identity_provider_type: str,
        tmp_req: main_models.UpdateIdentityProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIdentityProviderResponse:
        tmp_req.validate()
        request = main_models.UpdateIdentityProviderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIdentityProvider',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/identity-providers/{DaraURL.percent_encode(identity_provider_type)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_identity_provider(
        self,
        workspace_id: str,
        identity_provider_type: str,
        request: main_models.UpdateIdentityProviderRequest,
    ) -> main_models.UpdateIdentityProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_identity_provider_with_options(workspace_id, identity_provider_type, request, headers, runtime)

    async def update_identity_provider_async(
        self,
        workspace_id: str,
        identity_provider_type: str,
        request: main_models.UpdateIdentityProviderRequest,
    ) -> main_models.UpdateIdentityProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_identity_provider_with_options_async(workspace_id, identity_provider_type, request, headers, runtime)

    def update_managed_agent_with_options(
        self,
        workspace_id: str,
        agent_id: str,
        tmp_req: main_models.UpdateManagedAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateManagedAgentResponse:
        tmp_req.validate()
        request = main_models.UpdateManagedAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateManagedAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/managed-agents/{DaraURL.percent_encode(agent_id)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateManagedAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_managed_agent_with_options_async(
        self,
        workspace_id: str,
        agent_id: str,
        tmp_req: main_models.UpdateManagedAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateManagedAgentResponse:
        tmp_req.validate()
        request = main_models.UpdateManagedAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateManagedAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/managed-agents/{DaraURL.percent_encode(agent_id)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateManagedAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_managed_agent(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.UpdateManagedAgentRequest,
    ) -> main_models.UpdateManagedAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_managed_agent_with_options(workspace_id, agent_id, request, headers, runtime)

    async def update_managed_agent_async(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.UpdateManagedAgentRequest,
    ) -> main_models.UpdateManagedAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_managed_agent_with_options_async(workspace_id, agent_id, request, headers, runtime)

    def update_model_with_options(
        self,
        workspace_id: str,
        model_id: str,
        tmp_req: main_models.UpdateModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelResponse:
        tmp_req.validate()
        request = main_models.UpdateModelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models/{DaraURL.percent_encode(model_id)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_model_with_options_async(
        self,
        workspace_id: str,
        model_id: str,
        tmp_req: main_models.UpdateModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelResponse:
        tmp_req.validate()
        request = main_models.UpdateModelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models/{DaraURL.percent_encode(model_id)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_model(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.UpdateModelRequest,
    ) -> main_models.UpdateModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_model_with_options(workspace_id, model_id, request, headers, runtime)

    async def update_model_async(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.UpdateModelRequest,
    ) -> main_models.UpdateModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_model_with_options_async(workspace_id, model_id, request, headers, runtime)

    def update_model_connection_with_options(
        self,
        workspace_id: str,
        connection_id: str,
        tmp_req: main_models.UpdateModelConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelConnectionResponse:
        tmp_req.validate()
        request = main_models.UpdateModelConnectionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModelConnection',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/model-connections/{DaraURL.percent_encode(connection_id)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_model_connection_with_options_async(
        self,
        workspace_id: str,
        connection_id: str,
        tmp_req: main_models.UpdateModelConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelConnectionResponse:
        tmp_req.validate()
        request = main_models.UpdateModelConnectionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModelConnection',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/model-connections/{DaraURL.percent_encode(connection_id)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_model_connection(
        self,
        workspace_id: str,
        connection_id: str,
        request: main_models.UpdateModelConnectionRequest,
    ) -> main_models.UpdateModelConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_model_connection_with_options(workspace_id, connection_id, request, headers, runtime)

    async def update_model_connection_async(
        self,
        workspace_id: str,
        connection_id: str,
        request: main_models.UpdateModelConnectionRequest,
    ) -> main_models.UpdateModelConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_model_connection_with_options_async(workspace_id, connection_id, request, headers, runtime)

    def update_team_with_options(
        self,
        workspace_id: str,
        team_id: str,
        tmp_req: main_models.UpdateTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTeamResponse:
        tmp_req.validate()
        request = main_models.UpdateTeamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTeam',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/teams/{DaraURL.percent_encode(team_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTeamResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_team_with_options_async(
        self,
        workspace_id: str,
        team_id: str,
        tmp_req: main_models.UpdateTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTeamResponse:
        tmp_req.validate()
        request = main_models.UpdateTeamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTeam',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/teams/{DaraURL.percent_encode(team_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTeamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_team(
        self,
        workspace_id: str,
        team_id: str,
        request: main_models.UpdateTeamRequest,
    ) -> main_models.UpdateTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_team_with_options(workspace_id, team_id, request, headers, runtime)

    async def update_team_async(
        self,
        workspace_id: str,
        team_id: str,
        request: main_models.UpdateTeamRequest,
    ) -> main_models.UpdateTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_team_with_options_async(workspace_id, team_id, request, headers, runtime)

    def update_user_with_options(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        tmp_req: main_models.UpdateUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        tmp_req.validate()
        request = main_models.UpdateUserShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users/{DaraURL.percent_encode(agent_core_user_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        tmp_req: main_models.UpdateUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        tmp_req.validate()
        request = main_models.UpdateUserShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users/{DaraURL.percent_encode(agent_core_user_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        request: main_models.UpdateUserRequest,
    ) -> main_models.UpdateUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_user_with_options(workspace_id, agent_core_user_id, request, headers, runtime)

    async def update_user_async(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        request: main_models.UpdateUserRequest,
    ) -> main_models.UpdateUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_user_with_options_async(workspace_id, agent_core_user_id, request, headers, runtime)

    def update_workspace_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.UpdateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkspaceResponse:
        tmp_req.validate()
        request = main_models.UpdateWorkspaceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkspace',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workspace_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.UpdateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkspaceResponse:
        tmp_req.validate()
        request = main_models.UpdateWorkspaceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkspace',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workspace(
        self,
        workspace_id: str,
        request: main_models.UpdateWorkspaceRequest,
    ) -> main_models.UpdateWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_workspace_with_options(workspace_id, request, headers, runtime)

    async def update_workspace_async(
        self,
        workspace_id: str,
        request: main_models.UpdateWorkspaceRequest,
    ) -> main_models.UpdateWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_workspace_with_options_async(workspace_id, request, headers, runtime)
