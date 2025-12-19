# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agentidentity20250901 import models as main_models
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
        self._endpoint = self.get_endpoint('agentidentity', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_apikey_credential_provider_with_options(
        self,
        request: main_models.CreateAPIKeyCredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAPIKeyCredentialProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.apikey):
            body['APIKey'] = request.apikey
        if not DaraCore.is_null(request.apikey_credential_provider_name):
            body['APIKeyCredentialProviderName'] = request.apikey_credential_provider_name
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAPIKeyCredentialProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAPIKeyCredentialProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_apikey_credential_provider_with_options_async(
        self,
        request: main_models.CreateAPIKeyCredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAPIKeyCredentialProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.apikey):
            body['APIKey'] = request.apikey
        if not DaraCore.is_null(request.apikey_credential_provider_name):
            body['APIKeyCredentialProviderName'] = request.apikey_credential_provider_name
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAPIKeyCredentialProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAPIKeyCredentialProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_apikey_credential_provider(
        self,
        request: main_models.CreateAPIKeyCredentialProviderRequest,
    ) -> main_models.CreateAPIKeyCredentialProviderResponse:
        runtime = RuntimeOptions()
        return self.create_apikey_credential_provider_with_options(request, runtime)

    async def create_apikey_credential_provider_async(
        self,
        request: main_models.CreateAPIKeyCredentialProviderRequest,
    ) -> main_models.CreateAPIKeyCredentialProviderResponse:
        runtime = RuntimeOptions()
        return await self.create_apikey_credential_provider_with_options_async(request, runtime)

    def create_identity_provider_with_options(
        self,
        tmp_req: main_models.CreateIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIdentityProviderResponse:
        tmp_req.validate()
        request = main_models.CreateIdentityProviderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.allowed_audience):
            request.allowed_audience_shrink = Utils.array_to_string_with_specified_style(tmp_req.allowed_audience, 'AllowedAudience', 'json')
        body = {}
        if not DaraCore.is_null(request.allowed_audience_shrink):
            body['AllowedAudience'] = request.allowed_audience_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.discovery_url):
            body['DiscoveryURL'] = request.discovery_url
        if not DaraCore.is_null(request.identity_provider_name):
            body['IdentityProviderName'] = request.identity_provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIdentityProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_identity_provider_with_options_async(
        self,
        tmp_req: main_models.CreateIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIdentityProviderResponse:
        tmp_req.validate()
        request = main_models.CreateIdentityProviderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.allowed_audience):
            request.allowed_audience_shrink = Utils.array_to_string_with_specified_style(tmp_req.allowed_audience, 'AllowedAudience', 'json')
        body = {}
        if not DaraCore.is_null(request.allowed_audience_shrink):
            body['AllowedAudience'] = request.allowed_audience_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.discovery_url):
            body['DiscoveryURL'] = request.discovery_url
        if not DaraCore.is_null(request.identity_provider_name):
            body['IdentityProviderName'] = request.identity_provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIdentityProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_identity_provider(
        self,
        request: main_models.CreateIdentityProviderRequest,
    ) -> main_models.CreateIdentityProviderResponse:
        runtime = RuntimeOptions()
        return self.create_identity_provider_with_options(request, runtime)

    async def create_identity_provider_async(
        self,
        request: main_models.CreateIdentityProviderRequest,
    ) -> main_models.CreateIdentityProviderResponse:
        runtime = RuntimeOptions()
        return await self.create_identity_provider_with_options_async(request, runtime)

    def create_oauth2_credential_provider_with_options(
        self,
        tmp_req: main_models.CreateOAuth2CredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOAuth2CredentialProviderResponse:
        tmp_req.validate()
        request = main_models.CreateOAuth2CredentialProviderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.oauth2_provider_config):
            request.oauth2_provider_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.oauth2_provider_config, 'OAuth2ProviderConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.callback_url):
            body['CallbackURL'] = request.callback_url
        if not DaraCore.is_null(request.credential_provider_vendor):
            body['CredentialProviderVendor'] = request.credential_provider_vendor
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.oauth2_credential_provider_name):
            body['OAuth2CredentialProviderName'] = request.oauth2_credential_provider_name
        if not DaraCore.is_null(request.oauth2_provider_config_shrink):
            body['OAuth2ProviderConfig'] = request.oauth2_provider_config_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOAuth2CredentialProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOAuth2CredentialProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_oauth2_credential_provider_with_options_async(
        self,
        tmp_req: main_models.CreateOAuth2CredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOAuth2CredentialProviderResponse:
        tmp_req.validate()
        request = main_models.CreateOAuth2CredentialProviderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.oauth2_provider_config):
            request.oauth2_provider_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.oauth2_provider_config, 'OAuth2ProviderConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.callback_url):
            body['CallbackURL'] = request.callback_url
        if not DaraCore.is_null(request.credential_provider_vendor):
            body['CredentialProviderVendor'] = request.credential_provider_vendor
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.oauth2_credential_provider_name):
            body['OAuth2CredentialProviderName'] = request.oauth2_credential_provider_name
        if not DaraCore.is_null(request.oauth2_provider_config_shrink):
            body['OAuth2ProviderConfig'] = request.oauth2_provider_config_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOAuth2CredentialProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOAuth2CredentialProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_oauth2_credential_provider(
        self,
        request: main_models.CreateOAuth2CredentialProviderRequest,
    ) -> main_models.CreateOAuth2CredentialProviderResponse:
        runtime = RuntimeOptions()
        return self.create_oauth2_credential_provider_with_options(request, runtime)

    async def create_oauth2_credential_provider_async(
        self,
        request: main_models.CreateOAuth2CredentialProviderRequest,
    ) -> main_models.CreateOAuth2CredentialProviderResponse:
        runtime = RuntimeOptions()
        return await self.create_oauth2_credential_provider_with_options_async(request, runtime)

    def create_workload_identity_with_options(
        self,
        tmp_req: main_models.CreateWorkloadIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkloadIdentityResponse:
        tmp_req.validate()
        request = main_models.CreateWorkloadIdentityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.allowed_resource_oauth2_return_urls):
            request.allowed_resource_oauth2_return_urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.allowed_resource_oauth2_return_urls, 'AllowedResourceOAuth2ReturnURLs', 'json')
        body = {}
        if not DaraCore.is_null(request.allowed_resource_oauth2_return_urls_shrink):
            body['AllowedResourceOAuth2ReturnURLs'] = request.allowed_resource_oauth2_return_urls_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.identity_provider_name):
            body['IdentityProviderName'] = request.identity_provider_name
        if not DaraCore.is_null(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not DaraCore.is_null(request.workload_identity_name):
            body['WorkloadIdentityName'] = request.workload_identity_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkloadIdentity',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkloadIdentityResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workload_identity_with_options_async(
        self,
        tmp_req: main_models.CreateWorkloadIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkloadIdentityResponse:
        tmp_req.validate()
        request = main_models.CreateWorkloadIdentityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.allowed_resource_oauth2_return_urls):
            request.allowed_resource_oauth2_return_urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.allowed_resource_oauth2_return_urls, 'AllowedResourceOAuth2ReturnURLs', 'json')
        body = {}
        if not DaraCore.is_null(request.allowed_resource_oauth2_return_urls_shrink):
            body['AllowedResourceOAuth2ReturnURLs'] = request.allowed_resource_oauth2_return_urls_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.identity_provider_name):
            body['IdentityProviderName'] = request.identity_provider_name
        if not DaraCore.is_null(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not DaraCore.is_null(request.workload_identity_name):
            body['WorkloadIdentityName'] = request.workload_identity_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkloadIdentity',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkloadIdentityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workload_identity(
        self,
        request: main_models.CreateWorkloadIdentityRequest,
    ) -> main_models.CreateWorkloadIdentityResponse:
        runtime = RuntimeOptions()
        return self.create_workload_identity_with_options(request, runtime)

    async def create_workload_identity_async(
        self,
        request: main_models.CreateWorkloadIdentityRequest,
    ) -> main_models.CreateWorkloadIdentityResponse:
        runtime = RuntimeOptions()
        return await self.create_workload_identity_with_options_async(request, runtime)

    def delete_apikey_credential_provider_with_options(
        self,
        request: main_models.DeleteAPIKeyCredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAPIKeyCredentialProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.apikey_credential_provider_name):
            body['APIKeyCredentialProviderName'] = request.apikey_credential_provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAPIKeyCredentialProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAPIKeyCredentialProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_apikey_credential_provider_with_options_async(
        self,
        request: main_models.DeleteAPIKeyCredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAPIKeyCredentialProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.apikey_credential_provider_name):
            body['APIKeyCredentialProviderName'] = request.apikey_credential_provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAPIKeyCredentialProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAPIKeyCredentialProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_apikey_credential_provider(
        self,
        request: main_models.DeleteAPIKeyCredentialProviderRequest,
    ) -> main_models.DeleteAPIKeyCredentialProviderResponse:
        runtime = RuntimeOptions()
        return self.delete_apikey_credential_provider_with_options(request, runtime)

    async def delete_apikey_credential_provider_async(
        self,
        request: main_models.DeleteAPIKeyCredentialProviderRequest,
    ) -> main_models.DeleteAPIKeyCredentialProviderResponse:
        runtime = RuntimeOptions()
        return await self.delete_apikey_credential_provider_with_options_async(request, runtime)

    def delete_identity_provider_with_options(
        self,
        request: main_models.DeleteIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIdentityProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identity_provider_name):
            body['IdentityProviderName'] = request.identity_provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIdentityProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_identity_provider_with_options_async(
        self,
        request: main_models.DeleteIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIdentityProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identity_provider_name):
            body['IdentityProviderName'] = request.identity_provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIdentityProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_identity_provider(
        self,
        request: main_models.DeleteIdentityProviderRequest,
    ) -> main_models.DeleteIdentityProviderResponse:
        runtime = RuntimeOptions()
        return self.delete_identity_provider_with_options(request, runtime)

    async def delete_identity_provider_async(
        self,
        request: main_models.DeleteIdentityProviderRequest,
    ) -> main_models.DeleteIdentityProviderResponse:
        runtime = RuntimeOptions()
        return await self.delete_identity_provider_with_options_async(request, runtime)

    def delete_oauth2_credential_provider_with_options(
        self,
        request: main_models.DeleteOAuth2CredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOAuth2CredentialProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.oauth2_credential_provider_name):
            body['OAuth2CredentialProviderName'] = request.oauth2_credential_provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOAuth2CredentialProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOAuth2CredentialProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_oauth2_credential_provider_with_options_async(
        self,
        request: main_models.DeleteOAuth2CredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOAuth2CredentialProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.oauth2_credential_provider_name):
            body['OAuth2CredentialProviderName'] = request.oauth2_credential_provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOAuth2CredentialProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOAuth2CredentialProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_oauth2_credential_provider(
        self,
        request: main_models.DeleteOAuth2CredentialProviderRequest,
    ) -> main_models.DeleteOAuth2CredentialProviderResponse:
        runtime = RuntimeOptions()
        return self.delete_oauth2_credential_provider_with_options(request, runtime)

    async def delete_oauth2_credential_provider_async(
        self,
        request: main_models.DeleteOAuth2CredentialProviderRequest,
    ) -> main_models.DeleteOAuth2CredentialProviderResponse:
        runtime = RuntimeOptions()
        return await self.delete_oauth2_credential_provider_with_options_async(request, runtime)

    def delete_workload_identity_with_options(
        self,
        request: main_models.DeleteWorkloadIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkloadIdentityResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.workload_identity_name):
            body['WorkloadIdentityName'] = request.workload_identity_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkloadIdentity',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkloadIdentityResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workload_identity_with_options_async(
        self,
        request: main_models.DeleteWorkloadIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkloadIdentityResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.workload_identity_name):
            body['WorkloadIdentityName'] = request.workload_identity_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkloadIdentity',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkloadIdentityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workload_identity(
        self,
        request: main_models.DeleteWorkloadIdentityRequest,
    ) -> main_models.DeleteWorkloadIdentityResponse:
        runtime = RuntimeOptions()
        return self.delete_workload_identity_with_options(request, runtime)

    async def delete_workload_identity_async(
        self,
        request: main_models.DeleteWorkloadIdentityRequest,
    ) -> main_models.DeleteWorkloadIdentityResponse:
        runtime = RuntimeOptions()
        return await self.delete_workload_identity_with_options_async(request, runtime)

    def get_apikey_credential_provider_with_options(
        self,
        request: main_models.GetAPIKeyCredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAPIKeyCredentialProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.apikey_credential_provider_name):
            body['APIKeyCredentialProviderName'] = request.apikey_credential_provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAPIKeyCredentialProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAPIKeyCredentialProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_apikey_credential_provider_with_options_async(
        self,
        request: main_models.GetAPIKeyCredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAPIKeyCredentialProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.apikey_credential_provider_name):
            body['APIKeyCredentialProviderName'] = request.apikey_credential_provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAPIKeyCredentialProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAPIKeyCredentialProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_apikey_credential_provider(
        self,
        request: main_models.GetAPIKeyCredentialProviderRequest,
    ) -> main_models.GetAPIKeyCredentialProviderResponse:
        runtime = RuntimeOptions()
        return self.get_apikey_credential_provider_with_options(request, runtime)

    async def get_apikey_credential_provider_async(
        self,
        request: main_models.GetAPIKeyCredentialProviderRequest,
    ) -> main_models.GetAPIKeyCredentialProviderResponse:
        runtime = RuntimeOptions()
        return await self.get_apikey_credential_provider_with_options_async(request, runtime)

    def get_identity_provider_with_options(
        self,
        request: main_models.GetIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIdentityProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identity_provider_name):
            body['IdentityProviderName'] = request.identity_provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetIdentityProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_identity_provider_with_options_async(
        self,
        request: main_models.GetIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIdentityProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identity_provider_name):
            body['IdentityProviderName'] = request.identity_provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetIdentityProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_identity_provider(
        self,
        request: main_models.GetIdentityProviderRequest,
    ) -> main_models.GetIdentityProviderResponse:
        runtime = RuntimeOptions()
        return self.get_identity_provider_with_options(request, runtime)

    async def get_identity_provider_async(
        self,
        request: main_models.GetIdentityProviderRequest,
    ) -> main_models.GetIdentityProviderResponse:
        runtime = RuntimeOptions()
        return await self.get_identity_provider_with_options_async(request, runtime)

    def get_oauth2_credential_provider_with_options(
        self,
        request: main_models.GetOAuth2CredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOAuth2CredentialProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.oauth2_credential_provider_name):
            body['OAuth2CredentialProviderName'] = request.oauth2_credential_provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetOAuth2CredentialProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOAuth2CredentialProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oauth2_credential_provider_with_options_async(
        self,
        request: main_models.GetOAuth2CredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOAuth2CredentialProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.oauth2_credential_provider_name):
            body['OAuth2CredentialProviderName'] = request.oauth2_credential_provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetOAuth2CredentialProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOAuth2CredentialProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oauth2_credential_provider(
        self,
        request: main_models.GetOAuth2CredentialProviderRequest,
    ) -> main_models.GetOAuth2CredentialProviderResponse:
        runtime = RuntimeOptions()
        return self.get_oauth2_credential_provider_with_options(request, runtime)

    async def get_oauth2_credential_provider_async(
        self,
        request: main_models.GetOAuth2CredentialProviderRequest,
    ) -> main_models.GetOAuth2CredentialProviderResponse:
        runtime = RuntimeOptions()
        return await self.get_oauth2_credential_provider_with_options_async(request, runtime)

    def get_workload_identity_with_options(
        self,
        request: main_models.GetWorkloadIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkloadIdentityResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.workload_identity_name):
            body['WorkloadIdentityName'] = request.workload_identity_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkloadIdentity',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkloadIdentityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workload_identity_with_options_async(
        self,
        request: main_models.GetWorkloadIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkloadIdentityResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.workload_identity_name):
            body['WorkloadIdentityName'] = request.workload_identity_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkloadIdentity',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkloadIdentityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workload_identity(
        self,
        request: main_models.GetWorkloadIdentityRequest,
    ) -> main_models.GetWorkloadIdentityResponse:
        runtime = RuntimeOptions()
        return self.get_workload_identity_with_options(request, runtime)

    async def get_workload_identity_async(
        self,
        request: main_models.GetWorkloadIdentityRequest,
    ) -> main_models.GetWorkloadIdentityResponse:
        runtime = RuntimeOptions()
        return await self.get_workload_identity_with_options_async(request, runtime)

    def list_apikey_credential_providers_with_options(
        self,
        request: main_models.ListAPIKeyCredentialProvidersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAPIKeyCredentialProvidersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAPIKeyCredentialProviders',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAPIKeyCredentialProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_apikey_credential_providers_with_options_async(
        self,
        request: main_models.ListAPIKeyCredentialProvidersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAPIKeyCredentialProvidersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAPIKeyCredentialProviders',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAPIKeyCredentialProvidersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_apikey_credential_providers(
        self,
        request: main_models.ListAPIKeyCredentialProvidersRequest,
    ) -> main_models.ListAPIKeyCredentialProvidersResponse:
        runtime = RuntimeOptions()
        return self.list_apikey_credential_providers_with_options(request, runtime)

    async def list_apikey_credential_providers_async(
        self,
        request: main_models.ListAPIKeyCredentialProvidersRequest,
    ) -> main_models.ListAPIKeyCredentialProvidersResponse:
        runtime = RuntimeOptions()
        return await self.list_apikey_credential_providers_with_options_async(request, runtime)

    def list_identity_providers_with_options(
        self,
        request: main_models.ListIdentityProvidersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIdentityProvidersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListIdentityProviders',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIdentityProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_identity_providers_with_options_async(
        self,
        request: main_models.ListIdentityProvidersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIdentityProvidersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListIdentityProviders',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIdentityProvidersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_identity_providers(
        self,
        request: main_models.ListIdentityProvidersRequest,
    ) -> main_models.ListIdentityProvidersResponse:
        runtime = RuntimeOptions()
        return self.list_identity_providers_with_options(request, runtime)

    async def list_identity_providers_async(
        self,
        request: main_models.ListIdentityProvidersRequest,
    ) -> main_models.ListIdentityProvidersResponse:
        runtime = RuntimeOptions()
        return await self.list_identity_providers_with_options_async(request, runtime)

    def list_oauth2_credential_providers_with_options(
        self,
        request: main_models.ListOAuth2CredentialProvidersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOAuth2CredentialProvidersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListOAuth2CredentialProviders',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOAuth2CredentialProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_oauth2_credential_providers_with_options_async(
        self,
        request: main_models.ListOAuth2CredentialProvidersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOAuth2CredentialProvidersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListOAuth2CredentialProviders',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOAuth2CredentialProvidersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_oauth2_credential_providers(
        self,
        request: main_models.ListOAuth2CredentialProvidersRequest,
    ) -> main_models.ListOAuth2CredentialProvidersResponse:
        runtime = RuntimeOptions()
        return self.list_oauth2_credential_providers_with_options(request, runtime)

    async def list_oauth2_credential_providers_async(
        self,
        request: main_models.ListOAuth2CredentialProvidersRequest,
    ) -> main_models.ListOAuth2CredentialProvidersResponse:
        runtime = RuntimeOptions()
        return await self.list_oauth2_credential_providers_with_options_async(request, runtime)

    def list_workload_identities_with_options(
        self,
        request: main_models.ListWorkloadIdentitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkloadIdentitiesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkloadIdentities',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkloadIdentitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workload_identities_with_options_async(
        self,
        request: main_models.ListWorkloadIdentitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkloadIdentitiesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkloadIdentities',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkloadIdentitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workload_identities(
        self,
        request: main_models.ListWorkloadIdentitiesRequest,
    ) -> main_models.ListWorkloadIdentitiesResponse:
        runtime = RuntimeOptions()
        return self.list_workload_identities_with_options(request, runtime)

    async def list_workload_identities_async(
        self,
        request: main_models.ListWorkloadIdentitiesRequest,
    ) -> main_models.ListWorkloadIdentitiesResponse:
        runtime = RuntimeOptions()
        return await self.list_workload_identities_with_options_async(request, runtime)

    def update_apikey_credential_provider_with_options(
        self,
        request: main_models.UpdateAPIKeyCredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAPIKeyCredentialProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.apikey):
            body['APIKey'] = request.apikey
        if not DaraCore.is_null(request.apikey_credential_provider_name):
            body['APIKeyCredentialProviderName'] = request.apikey_credential_provider_name
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAPIKeyCredentialProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAPIKeyCredentialProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_apikey_credential_provider_with_options_async(
        self,
        request: main_models.UpdateAPIKeyCredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAPIKeyCredentialProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.apikey):
            body['APIKey'] = request.apikey
        if not DaraCore.is_null(request.apikey_credential_provider_name):
            body['APIKeyCredentialProviderName'] = request.apikey_credential_provider_name
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAPIKeyCredentialProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAPIKeyCredentialProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_apikey_credential_provider(
        self,
        request: main_models.UpdateAPIKeyCredentialProviderRequest,
    ) -> main_models.UpdateAPIKeyCredentialProviderResponse:
        runtime = RuntimeOptions()
        return self.update_apikey_credential_provider_with_options(request, runtime)

    async def update_apikey_credential_provider_async(
        self,
        request: main_models.UpdateAPIKeyCredentialProviderRequest,
    ) -> main_models.UpdateAPIKeyCredentialProviderResponse:
        runtime = RuntimeOptions()
        return await self.update_apikey_credential_provider_with_options_async(request, runtime)

    def update_identity_provider_with_options(
        self,
        tmp_req: main_models.UpdateIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIdentityProviderResponse:
        tmp_req.validate()
        request = main_models.UpdateIdentityProviderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.allowed_audience):
            request.allowed_audience_shrink = Utils.array_to_string_with_specified_style(tmp_req.allowed_audience, 'AllowedAudience', 'json')
        body = {}
        if not DaraCore.is_null(request.allowed_audience_shrink):
            body['AllowedAudience'] = request.allowed_audience_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.discovery_url):
            body['DiscoveryURL'] = request.discovery_url
        if not DaraCore.is_null(request.identity_provider_name):
            body['IdentityProviderName'] = request.identity_provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIdentityProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_identity_provider_with_options_async(
        self,
        tmp_req: main_models.UpdateIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIdentityProviderResponse:
        tmp_req.validate()
        request = main_models.UpdateIdentityProviderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.allowed_audience):
            request.allowed_audience_shrink = Utils.array_to_string_with_specified_style(tmp_req.allowed_audience, 'AllowedAudience', 'json')
        body = {}
        if not DaraCore.is_null(request.allowed_audience_shrink):
            body['AllowedAudience'] = request.allowed_audience_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.discovery_url):
            body['DiscoveryURL'] = request.discovery_url
        if not DaraCore.is_null(request.identity_provider_name):
            body['IdentityProviderName'] = request.identity_provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIdentityProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_identity_provider(
        self,
        request: main_models.UpdateIdentityProviderRequest,
    ) -> main_models.UpdateIdentityProviderResponse:
        runtime = RuntimeOptions()
        return self.update_identity_provider_with_options(request, runtime)

    async def update_identity_provider_async(
        self,
        request: main_models.UpdateIdentityProviderRequest,
    ) -> main_models.UpdateIdentityProviderResponse:
        runtime = RuntimeOptions()
        return await self.update_identity_provider_with_options_async(request, runtime)

    def update_oauth2_credential_provider_with_options(
        self,
        tmp_req: main_models.UpdateOAuth2CredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOAuth2CredentialProviderResponse:
        tmp_req.validate()
        request = main_models.UpdateOAuth2CredentialProviderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.oauth2_provider_config):
            request.oauth2_provider_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.oauth2_provider_config, 'OAuth2ProviderConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.callback_url):
            body['CallbackURL'] = request.callback_url
        if not DaraCore.is_null(request.credential_provider_vendor):
            body['CredentialProviderVendor'] = request.credential_provider_vendor
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.oauth2_credential_provider_name):
            body['OAuth2CredentialProviderName'] = request.oauth2_credential_provider_name
        if not DaraCore.is_null(request.oauth2_provider_config_shrink):
            body['OAuth2ProviderConfig'] = request.oauth2_provider_config_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOAuth2CredentialProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOAuth2CredentialProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_oauth2_credential_provider_with_options_async(
        self,
        tmp_req: main_models.UpdateOAuth2CredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOAuth2CredentialProviderResponse:
        tmp_req.validate()
        request = main_models.UpdateOAuth2CredentialProviderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.oauth2_provider_config):
            request.oauth2_provider_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.oauth2_provider_config, 'OAuth2ProviderConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.callback_url):
            body['CallbackURL'] = request.callback_url
        if not DaraCore.is_null(request.credential_provider_vendor):
            body['CredentialProviderVendor'] = request.credential_provider_vendor
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.oauth2_credential_provider_name):
            body['OAuth2CredentialProviderName'] = request.oauth2_credential_provider_name
        if not DaraCore.is_null(request.oauth2_provider_config_shrink):
            body['OAuth2ProviderConfig'] = request.oauth2_provider_config_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOAuth2CredentialProvider',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOAuth2CredentialProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_oauth2_credential_provider(
        self,
        request: main_models.UpdateOAuth2CredentialProviderRequest,
    ) -> main_models.UpdateOAuth2CredentialProviderResponse:
        runtime = RuntimeOptions()
        return self.update_oauth2_credential_provider_with_options(request, runtime)

    async def update_oauth2_credential_provider_async(
        self,
        request: main_models.UpdateOAuth2CredentialProviderRequest,
    ) -> main_models.UpdateOAuth2CredentialProviderResponse:
        runtime = RuntimeOptions()
        return await self.update_oauth2_credential_provider_with_options_async(request, runtime)

    def update_workload_identity_with_options(
        self,
        tmp_req: main_models.UpdateWorkloadIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkloadIdentityResponse:
        tmp_req.validate()
        request = main_models.UpdateWorkloadIdentityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.allowed_resource_oauth2_return_urls):
            request.allowed_resource_oauth2_return_urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.allowed_resource_oauth2_return_urls, 'AllowedResourceOAuth2ReturnURLs', 'json')
        body = {}
        if not DaraCore.is_null(request.allowed_resource_oauth2_return_urls_shrink):
            body['AllowedResourceOAuth2ReturnURLs'] = request.allowed_resource_oauth2_return_urls_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.identity_provider_name):
            body['IdentityProviderName'] = request.identity_provider_name
        if not DaraCore.is_null(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not DaraCore.is_null(request.workload_identity_name):
            body['WorkloadIdentityName'] = request.workload_identity_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkloadIdentity',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkloadIdentityResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workload_identity_with_options_async(
        self,
        tmp_req: main_models.UpdateWorkloadIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkloadIdentityResponse:
        tmp_req.validate()
        request = main_models.UpdateWorkloadIdentityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.allowed_resource_oauth2_return_urls):
            request.allowed_resource_oauth2_return_urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.allowed_resource_oauth2_return_urls, 'AllowedResourceOAuth2ReturnURLs', 'json')
        body = {}
        if not DaraCore.is_null(request.allowed_resource_oauth2_return_urls_shrink):
            body['AllowedResourceOAuth2ReturnURLs'] = request.allowed_resource_oauth2_return_urls_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.identity_provider_name):
            body['IdentityProviderName'] = request.identity_provider_name
        if not DaraCore.is_null(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not DaraCore.is_null(request.workload_identity_name):
            body['WorkloadIdentityName'] = request.workload_identity_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkloadIdentity',
            version = '2025-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkloadIdentityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workload_identity(
        self,
        request: main_models.UpdateWorkloadIdentityRequest,
    ) -> main_models.UpdateWorkloadIdentityResponse:
        runtime = RuntimeOptions()
        return self.update_workload_identity_with_options(request, runtime)

    async def update_workload_identity_async(
        self,
        request: main_models.UpdateWorkloadIdentityRequest,
    ) -> main_models.UpdateWorkloadIdentityResponse:
        runtime = RuntimeOptions()
        return await self.update_workload_identity_with_options_async(request, runtime)
