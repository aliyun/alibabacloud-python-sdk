# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agentidentitydata20251127 import models as main_models
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
        self._endpoint = self.get_endpoint('agentidentitydata', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def assume_role_for_workload_identity_with_options(
        self,
        request: main_models.AssumeRoleForWorkloadIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssumeRoleForWorkloadIdentityResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.duration_seconds):
            body['DurationSeconds'] = request.duration_seconds
        if not DaraCore.is_null(request.policy):
            body['Policy'] = request.policy
        if not DaraCore.is_null(request.role_session_name):
            body['RoleSessionName'] = request.role_session_name
        if not DaraCore.is_null(request.workload_access_token):
            body['WorkloadAccessToken'] = request.workload_access_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssumeRoleForWorkloadIdentity',
            version = '2025-11-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssumeRoleForWorkloadIdentityResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def assume_role_for_workload_identity_with_options_async(
        self,
        request: main_models.AssumeRoleForWorkloadIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssumeRoleForWorkloadIdentityResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.duration_seconds):
            body['DurationSeconds'] = request.duration_seconds
        if not DaraCore.is_null(request.policy):
            body['Policy'] = request.policy
        if not DaraCore.is_null(request.role_session_name):
            body['RoleSessionName'] = request.role_session_name
        if not DaraCore.is_null(request.workload_access_token):
            body['WorkloadAccessToken'] = request.workload_access_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssumeRoleForWorkloadIdentity',
            version = '2025-11-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssumeRoleForWorkloadIdentityResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def assume_role_for_workload_identity(
        self,
        request: main_models.AssumeRoleForWorkloadIdentityRequest,
    ) -> main_models.AssumeRoleForWorkloadIdentityResponse:
        runtime = RuntimeOptions()
        return self.assume_role_for_workload_identity_with_options(request, runtime)

    async def assume_role_for_workload_identity_async(
        self,
        request: main_models.AssumeRoleForWorkloadIdentityRequest,
    ) -> main_models.AssumeRoleForWorkloadIdentityResponse:
        runtime = RuntimeOptions()
        return await self.assume_role_for_workload_identity_with_options_async(request, runtime)

    def complete_resource_token_auth_with_options(
        self,
        tmp_req: main_models.CompleteResourceTokenAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompleteResourceTokenAuthResponse:
        tmp_req.validate()
        request = main_models.CompleteResourceTokenAuthShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_identifier):
            request.user_identifier_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_identifier, 'UserIdentifier', 'json')
        body = {}
        if not DaraCore.is_null(request.session_uri):
            body['SessionURI'] = request.session_uri
        if not DaraCore.is_null(request.user_identifier_shrink):
            body['UserIdentifier'] = request.user_identifier_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CompleteResourceTokenAuth',
            version = '2025-11-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompleteResourceTokenAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def complete_resource_token_auth_with_options_async(
        self,
        tmp_req: main_models.CompleteResourceTokenAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompleteResourceTokenAuthResponse:
        tmp_req.validate()
        request = main_models.CompleteResourceTokenAuthShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_identifier):
            request.user_identifier_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_identifier, 'UserIdentifier', 'json')
        body = {}
        if not DaraCore.is_null(request.session_uri):
            body['SessionURI'] = request.session_uri
        if not DaraCore.is_null(request.user_identifier_shrink):
            body['UserIdentifier'] = request.user_identifier_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CompleteResourceTokenAuth',
            version = '2025-11-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompleteResourceTokenAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def complete_resource_token_auth(
        self,
        request: main_models.CompleteResourceTokenAuthRequest,
    ) -> main_models.CompleteResourceTokenAuthResponse:
        runtime = RuntimeOptions()
        return self.complete_resource_token_auth_with_options(request, runtime)

    async def complete_resource_token_auth_async(
        self,
        request: main_models.CompleteResourceTokenAuthRequest,
    ) -> main_models.CompleteResourceTokenAuthResponse:
        runtime = RuntimeOptions()
        return await self.complete_resource_token_auth_with_options_async(request, runtime)

    def get_resource_apikey_with_options(
        self,
        request: main_models.GetResourceAPIKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceAPIKeyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_credential_provider_name):
            body['ResourceCredentialProviderName'] = request.resource_credential_provider_name
        if not DaraCore.is_null(request.workload_access_token):
            body['WorkloadAccessToken'] = request.workload_access_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceAPIKey',
            version = '2025-11-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceAPIKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_apikey_with_options_async(
        self,
        request: main_models.GetResourceAPIKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceAPIKeyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_credential_provider_name):
            body['ResourceCredentialProviderName'] = request.resource_credential_provider_name
        if not DaraCore.is_null(request.workload_access_token):
            body['WorkloadAccessToken'] = request.workload_access_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceAPIKey',
            version = '2025-11-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceAPIKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_apikey(
        self,
        request: main_models.GetResourceAPIKeyRequest,
    ) -> main_models.GetResourceAPIKeyResponse:
        runtime = RuntimeOptions()
        return self.get_resource_apikey_with_options(request, runtime)

    async def get_resource_apikey_async(
        self,
        request: main_models.GetResourceAPIKeyRequest,
    ) -> main_models.GetResourceAPIKeyResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_apikey_with_options_async(request, runtime)

    def get_resource_oauth2_token_with_options(
        self,
        tmp_req: main_models.GetResourceOAuth2TokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceOAuth2TokenResponse:
        tmp_req.validate()
        request = main_models.GetResourceOAuth2TokenShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_parameters):
            request.custom_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_parameters, 'CustomParameters', 'json')
        if not DaraCore.is_null(tmp_req.scopes):
            request.scopes_shrink = Utils.array_to_string_with_specified_style(tmp_req.scopes, 'Scopes', 'json')
        body = {}
        if not DaraCore.is_null(request.custom_parameters_shrink):
            body['CustomParameters'] = request.custom_parameters_shrink
        if not DaraCore.is_null(request.custom_state):
            body['CustomState'] = request.custom_state
        if not DaraCore.is_null(request.force_authentication):
            body['ForceAuthentication'] = request.force_authentication
        if not DaraCore.is_null(request.oauth2_flow):
            body['OAuth2Flow'] = request.oauth2_flow
        if not DaraCore.is_null(request.resource_credential_provider_name):
            body['ResourceCredentialProviderName'] = request.resource_credential_provider_name
        if not DaraCore.is_null(request.resource_oauth2_return_url):
            body['ResourceOAuth2ReturnURL'] = request.resource_oauth2_return_url
        if not DaraCore.is_null(request.scopes_shrink):
            body['Scopes'] = request.scopes_shrink
        if not DaraCore.is_null(request.session_uri):
            body['SessionURI'] = request.session_uri
        if not DaraCore.is_null(request.workload_access_token):
            body['WorkloadAccessToken'] = request.workload_access_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceOAuth2Token',
            version = '2025-11-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceOAuth2TokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_oauth2_token_with_options_async(
        self,
        tmp_req: main_models.GetResourceOAuth2TokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceOAuth2TokenResponse:
        tmp_req.validate()
        request = main_models.GetResourceOAuth2TokenShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_parameters):
            request.custom_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_parameters, 'CustomParameters', 'json')
        if not DaraCore.is_null(tmp_req.scopes):
            request.scopes_shrink = Utils.array_to_string_with_specified_style(tmp_req.scopes, 'Scopes', 'json')
        body = {}
        if not DaraCore.is_null(request.custom_parameters_shrink):
            body['CustomParameters'] = request.custom_parameters_shrink
        if not DaraCore.is_null(request.custom_state):
            body['CustomState'] = request.custom_state
        if not DaraCore.is_null(request.force_authentication):
            body['ForceAuthentication'] = request.force_authentication
        if not DaraCore.is_null(request.oauth2_flow):
            body['OAuth2Flow'] = request.oauth2_flow
        if not DaraCore.is_null(request.resource_credential_provider_name):
            body['ResourceCredentialProviderName'] = request.resource_credential_provider_name
        if not DaraCore.is_null(request.resource_oauth2_return_url):
            body['ResourceOAuth2ReturnURL'] = request.resource_oauth2_return_url
        if not DaraCore.is_null(request.scopes_shrink):
            body['Scopes'] = request.scopes_shrink
        if not DaraCore.is_null(request.session_uri):
            body['SessionURI'] = request.session_uri
        if not DaraCore.is_null(request.workload_access_token):
            body['WorkloadAccessToken'] = request.workload_access_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceOAuth2Token',
            version = '2025-11-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceOAuth2TokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_oauth2_token(
        self,
        request: main_models.GetResourceOAuth2TokenRequest,
    ) -> main_models.GetResourceOAuth2TokenResponse:
        runtime = RuntimeOptions()
        return self.get_resource_oauth2_token_with_options(request, runtime)

    async def get_resource_oauth2_token_async(
        self,
        request: main_models.GetResourceOAuth2TokenRequest,
    ) -> main_models.GetResourceOAuth2TokenResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_oauth2_token_with_options_async(request, runtime)

    def get_workload_access_token_with_options(
        self,
        request: main_models.GetWorkloadAccessTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkloadAccessTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.workload_identity_name):
            body['WorkloadIdentityName'] = request.workload_identity_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkloadAccessToken',
            version = '2025-11-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkloadAccessTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workload_access_token_with_options_async(
        self,
        request: main_models.GetWorkloadAccessTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkloadAccessTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.workload_identity_name):
            body['WorkloadIdentityName'] = request.workload_identity_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkloadAccessToken',
            version = '2025-11-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkloadAccessTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workload_access_token(
        self,
        request: main_models.GetWorkloadAccessTokenRequest,
    ) -> main_models.GetWorkloadAccessTokenResponse:
        runtime = RuntimeOptions()
        return self.get_workload_access_token_with_options(request, runtime)

    async def get_workload_access_token_async(
        self,
        request: main_models.GetWorkloadAccessTokenRequest,
    ) -> main_models.GetWorkloadAccessTokenResponse:
        runtime = RuntimeOptions()
        return await self.get_workload_access_token_with_options_async(request, runtime)

    def get_workload_access_token_for_jwt_with_options(
        self,
        request: main_models.GetWorkloadAccessTokenForJWTRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkloadAccessTokenForJWTResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_token):
            body['UserToken'] = request.user_token
        if not DaraCore.is_null(request.workload_identity_name):
            body['WorkloadIdentityName'] = request.workload_identity_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkloadAccessTokenForJWT',
            version = '2025-11-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkloadAccessTokenForJWTResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workload_access_token_for_jwt_with_options_async(
        self,
        request: main_models.GetWorkloadAccessTokenForJWTRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkloadAccessTokenForJWTResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_token):
            body['UserToken'] = request.user_token
        if not DaraCore.is_null(request.workload_identity_name):
            body['WorkloadIdentityName'] = request.workload_identity_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkloadAccessTokenForJWT',
            version = '2025-11-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkloadAccessTokenForJWTResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workload_access_token_for_jwt(
        self,
        request: main_models.GetWorkloadAccessTokenForJWTRequest,
    ) -> main_models.GetWorkloadAccessTokenForJWTResponse:
        runtime = RuntimeOptions()
        return self.get_workload_access_token_for_jwt_with_options(request, runtime)

    async def get_workload_access_token_for_jwt_async(
        self,
        request: main_models.GetWorkloadAccessTokenForJWTRequest,
    ) -> main_models.GetWorkloadAccessTokenForJWTResponse:
        runtime = RuntimeOptions()
        return await self.get_workload_access_token_for_jwt_with_options_async(request, runtime)

    def get_workload_access_token_for_user_id_with_options(
        self,
        request: main_models.GetWorkloadAccessTokenForUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkloadAccessTokenForUserIdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        if not DaraCore.is_null(request.workload_identity_name):
            body['WorkloadIdentityName'] = request.workload_identity_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkloadAccessTokenForUserId',
            version = '2025-11-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkloadAccessTokenForUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workload_access_token_for_user_id_with_options_async(
        self,
        request: main_models.GetWorkloadAccessTokenForUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkloadAccessTokenForUserIdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        if not DaraCore.is_null(request.workload_identity_name):
            body['WorkloadIdentityName'] = request.workload_identity_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkloadAccessTokenForUserId',
            version = '2025-11-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkloadAccessTokenForUserIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workload_access_token_for_user_id(
        self,
        request: main_models.GetWorkloadAccessTokenForUserIdRequest,
    ) -> main_models.GetWorkloadAccessTokenForUserIdResponse:
        runtime = RuntimeOptions()
        return self.get_workload_access_token_for_user_id_with_options(request, runtime)

    async def get_workload_access_token_for_user_id_async(
        self,
        request: main_models.GetWorkloadAccessTokenForUserIdRequest,
    ) -> main_models.GetWorkloadAccessTokenForUserIdResponse:
        runtime = RuntimeOptions()
        return await self.get_workload_access_token_for_user_id_with_options_async(request, runtime)
