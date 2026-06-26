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
        self._endpoint_rule = 'regional'
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

    def add_samlidentity_provider_certificate_with_options(
        self,
        request: main_models.AddSAMLIdentityProviderCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSAMLIdentityProviderCertificateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        if not DaraCore.is_null(request.x_509certificate):
            body['X509Certificate'] = request.x_509certificate
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddSAMLIdentityProviderCertificate',
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
            main_models.AddSAMLIdentityProviderCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_samlidentity_provider_certificate_with_options_async(
        self,
        request: main_models.AddSAMLIdentityProviderCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSAMLIdentityProviderCertificateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        if not DaraCore.is_null(request.x_509certificate):
            body['X509Certificate'] = request.x_509certificate
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddSAMLIdentityProviderCertificate',
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
            main_models.AddSAMLIdentityProviderCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_samlidentity_provider_certificate(
        self,
        request: main_models.AddSAMLIdentityProviderCertificateRequest,
    ) -> main_models.AddSAMLIdentityProviderCertificateResponse:
        runtime = RuntimeOptions()
        return self.add_samlidentity_provider_certificate_with_options(request, runtime)

    async def add_samlidentity_provider_certificate_async(
        self,
        request: main_models.AddSAMLIdentityProviderCertificateRequest,
    ) -> main_models.AddSAMLIdentityProviderCertificateResponse:
        runtime = RuntimeOptions()
        return await self.add_samlidentity_provider_certificate_with_options_async(request, runtime)

    def attach_policy_set_to_gateway_with_options(
        self,
        request: main_models.AttachPolicySetToGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachPolicySetToGatewayResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enforcement_mode):
            body['EnforcementMode'] = request.enforcement_mode
        if not DaraCore.is_null(request.gateway_arn):
            body['GatewayArn'] = request.gateway_arn
        if not DaraCore.is_null(request.gateway_type):
            body['GatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AttachPolicySetToGateway',
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
            main_models.AttachPolicySetToGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_policy_set_to_gateway_with_options_async(
        self,
        request: main_models.AttachPolicySetToGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachPolicySetToGatewayResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enforcement_mode):
            body['EnforcementMode'] = request.enforcement_mode
        if not DaraCore.is_null(request.gateway_arn):
            body['GatewayArn'] = request.gateway_arn
        if not DaraCore.is_null(request.gateway_type):
            body['GatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AttachPolicySetToGateway',
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
            main_models.AttachPolicySetToGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_policy_set_to_gateway(
        self,
        request: main_models.AttachPolicySetToGatewayRequest,
    ) -> main_models.AttachPolicySetToGatewayResponse:
        runtime = RuntimeOptions()
        return self.attach_policy_set_to_gateway_with_options(request, runtime)

    async def attach_policy_set_to_gateway_async(
        self,
        request: main_models.AttachPolicySetToGatewayRequest,
    ) -> main_models.AttachPolicySetToGatewayResponse:
        runtime = RuntimeOptions()
        return await self.attach_policy_set_to_gateway_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
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
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
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

    def create_client_secret_with_options(
        self,
        request: main_models.CreateClientSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClientSecretResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_name):
            body['ClientName'] = request.client_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateClientSecret',
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
            main_models.CreateClientSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_client_secret_with_options_async(
        self,
        request: main_models.CreateClientSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClientSecretResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_name):
            body['ClientName'] = request.client_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateClientSecret',
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
            main_models.CreateClientSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_client_secret(
        self,
        request: main_models.CreateClientSecretRequest,
    ) -> main_models.CreateClientSecretResponse:
        runtime = RuntimeOptions()
        return self.create_client_secret_with_options(request, runtime)

    async def create_client_secret_async(
        self,
        request: main_models.CreateClientSecretRequest,
    ) -> main_models.CreateClientSecretResponse:
        runtime = RuntimeOptions()
        return await self.create_client_secret_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
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
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
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

    def create_policy_with_options(
        self,
        tmp_req: main_models.CreatePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyResponse:
        tmp_req.validate()
        request = main_models.CreatePolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.definition):
            request.definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.definition, 'Definition', 'json')
        body = {}
        if not DaraCore.is_null(request.definition_shrink):
            body['Definition'] = request.definition_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicy',
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
            main_models.CreatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_with_options_async(
        self,
        tmp_req: main_models.CreatePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyResponse:
        tmp_req.validate()
        request = main_models.CreatePolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.definition):
            request.definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.definition, 'Definition', 'json')
        body = {}
        if not DaraCore.is_null(request.definition_shrink):
            body['Definition'] = request.definition_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicy',
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
            main_models.CreatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy(
        self,
        request: main_models.CreatePolicyRequest,
    ) -> main_models.CreatePolicyResponse:
        runtime = RuntimeOptions()
        return self.create_policy_with_options(request, runtime)

    async def create_policy_async(
        self,
        request: main_models.CreatePolicyRequest,
    ) -> main_models.CreatePolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_policy_with_options_async(request, runtime)

    def create_policy_set_with_options(
        self,
        request: main_models.CreatePolicySetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicySetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicySet',
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
            main_models.CreatePolicySetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_set_with_options_async(
        self,
        request: main_models.CreatePolicySetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicySetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicySet',
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
            main_models.CreatePolicySetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy_set(
        self,
        request: main_models.CreatePolicySetRequest,
    ) -> main_models.CreatePolicySetResponse:
        runtime = RuntimeOptions()
        return self.create_policy_set_with_options(request, runtime)

    async def create_policy_set_async(
        self,
        request: main_models.CreatePolicySetRequest,
    ) -> main_models.CreatePolicySetResponse:
        runtime = RuntimeOptions()
        return await self.create_policy_set_with_options_async(request, runtime)

    def create_role_with_options(
        self,
        request: main_models.CreateRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.role_name):
            body['RoleName'] = request.role_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRole',
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
            main_models.CreateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_role_with_options_async(
        self,
        request: main_models.CreateRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.role_name):
            body['RoleName'] = request.role_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRole',
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
            main_models.CreateRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_role(
        self,
        request: main_models.CreateRoleRequest,
    ) -> main_models.CreateRoleResponse:
        runtime = RuntimeOptions()
        return self.create_role_with_options(request, runtime)

    async def create_role_async(
        self,
        request: main_models.CreateRoleRequest,
    ) -> main_models.CreateRoleResponse:
        runtime = RuntimeOptions()
        return await self.create_role_with_options_async(request, runtime)

    def create_role_assignment_with_options(
        self,
        request: main_models.CreateRoleAssignmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRoleAssignmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.principal_name):
            body['PrincipalName'] = request.principal_name
        if not DaraCore.is_null(request.principal_type):
            body['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.role_name):
            body['RoleName'] = request.role_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRoleAssignment',
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
            main_models.CreateRoleAssignmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_role_assignment_with_options_async(
        self,
        request: main_models.CreateRoleAssignmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRoleAssignmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.principal_name):
            body['PrincipalName'] = request.principal_name
        if not DaraCore.is_null(request.principal_type):
            body['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.role_name):
            body['RoleName'] = request.role_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRoleAssignment',
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
            main_models.CreateRoleAssignmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_role_assignment(
        self,
        request: main_models.CreateRoleAssignmentRequest,
    ) -> main_models.CreateRoleAssignmentResponse:
        runtime = RuntimeOptions()
        return self.create_role_assignment_with_options(request, runtime)

    async def create_role_assignment_async(
        self,
        request: main_models.CreateRoleAssignmentRequest,
    ) -> main_models.CreateRoleAssignmentResponse:
        runtime = RuntimeOptions()
        return await self.create_role_assignment_with_options_async(request, runtime)

    def create_token_vault_with_options(
        self,
        tmp_req: main_models.CreateTokenVaultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTokenVaultResponse:
        tmp_req.validate()
        request = main_models.CreateTokenVaultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.encryption_config):
            request.encryption_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.encryption_config, 'EncryptionConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.encryption_config_shrink):
            body['EncryptionConfig'] = request.encryption_config_shrink
        if not DaraCore.is_null(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTokenVault',
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
            main_models.CreateTokenVaultResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_token_vault_with_options_async(
        self,
        tmp_req: main_models.CreateTokenVaultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTokenVaultResponse:
        tmp_req.validate()
        request = main_models.CreateTokenVaultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.encryption_config):
            request.encryption_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.encryption_config, 'EncryptionConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.encryption_config_shrink):
            body['EncryptionConfig'] = request.encryption_config_shrink
        if not DaraCore.is_null(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTokenVault',
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
            main_models.CreateTokenVaultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_token_vault(
        self,
        request: main_models.CreateTokenVaultRequest,
    ) -> main_models.CreateTokenVaultResponse:
        runtime = RuntimeOptions()
        return self.create_token_vault_with_options(request, runtime)

    async def create_token_vault_async(
        self,
        request: main_models.CreateTokenVaultRequest,
    ) -> main_models.CreateTokenVaultResponse:
        runtime = RuntimeOptions()
        return await self.create_token_vault_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: main_models.CreateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            body['Email'] = request.email
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
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
            main_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: main_models.CreateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            body['Email'] = request.email
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
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
            main_models.CreateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user(
        self,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    async def create_user_async(
        self,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        return await self.create_user_with_options_async(request, runtime)

    def create_user_pool_with_options(
        self,
        request: main_models.CreateUserPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserPoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserPool',
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
            main_models.CreateUserPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_pool_with_options_async(
        self,
        request: main_models.CreateUserPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserPoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserPool',
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
            main_models.CreateUserPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_pool(
        self,
        request: main_models.CreateUserPoolRequest,
    ) -> main_models.CreateUserPoolResponse:
        runtime = RuntimeOptions()
        return self.create_user_pool_with_options(request, runtime)

    async def create_user_pool_async(
        self,
        request: main_models.CreateUserPoolRequest,
    ) -> main_models.CreateUserPoolResponse:
        runtime = RuntimeOptions()
        return await self.create_user_pool_with_options_async(request, runtime)

    def create_user_pool_client_with_options(
        self,
        tmp_req: main_models.CreateUserPoolClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserPoolClientResponse:
        tmp_req.validate()
        request = main_models.CreateUserPoolClientShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.redirect_uris):
            request.redirect_uris_shrink = Utils.array_to_string_with_specified_style(tmp_req.redirect_uris, 'RedirectURIs', 'json')
        body = {}
        if not DaraCore.is_null(request.access_token_validity):
            body['AccessTokenValidity'] = request.access_token_validity
        if not DaraCore.is_null(request.client_name):
            body['ClientName'] = request.client_name
        if not DaraCore.is_null(request.enforce_pkce):
            body['EnforcePKCE'] = request.enforce_pkce
        if not DaraCore.is_null(request.redirect_uris_shrink):
            body['RedirectURIs'] = request.redirect_uris_shrink
        if not DaraCore.is_null(request.refresh_token_validity):
            body['RefreshTokenValidity'] = request.refresh_token_validity
        if not DaraCore.is_null(request.secret_required):
            body['SecretRequired'] = request.secret_required
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserPoolClient',
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
            main_models.CreateUserPoolClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_pool_client_with_options_async(
        self,
        tmp_req: main_models.CreateUserPoolClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserPoolClientResponse:
        tmp_req.validate()
        request = main_models.CreateUserPoolClientShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.redirect_uris):
            request.redirect_uris_shrink = Utils.array_to_string_with_specified_style(tmp_req.redirect_uris, 'RedirectURIs', 'json')
        body = {}
        if not DaraCore.is_null(request.access_token_validity):
            body['AccessTokenValidity'] = request.access_token_validity
        if not DaraCore.is_null(request.client_name):
            body['ClientName'] = request.client_name
        if not DaraCore.is_null(request.enforce_pkce):
            body['EnforcePKCE'] = request.enforce_pkce
        if not DaraCore.is_null(request.redirect_uris_shrink):
            body['RedirectURIs'] = request.redirect_uris_shrink
        if not DaraCore.is_null(request.refresh_token_validity):
            body['RefreshTokenValidity'] = request.refresh_token_validity
        if not DaraCore.is_null(request.secret_required):
            body['SecretRequired'] = request.secret_required
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserPoolClient',
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
            main_models.CreateUserPoolClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_pool_client(
        self,
        request: main_models.CreateUserPoolClientRequest,
    ) -> main_models.CreateUserPoolClientResponse:
        runtime = RuntimeOptions()
        return self.create_user_pool_client_with_options(request, runtime)

    async def create_user_pool_client_async(
        self,
        request: main_models.CreateUserPoolClientRequest,
    ) -> main_models.CreateUserPoolClientResponse:
        runtime = RuntimeOptions()
        return await self.create_user_pool_client_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.create_ramrole):
            body['CreateRAMRole'] = request.create_ramrole
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.identity_provider_name):
            body['IdentityProviderName'] = request.identity_provider_name
        if not DaraCore.is_null(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not DaraCore.is_null(request.session_binding_enabled):
            body['SessionBindingEnabled'] = request.session_binding_enabled
        if not DaraCore.is_null(request.source_agent_arn):
            body['SourceAgentArn'] = request.source_agent_arn
        if not DaraCore.is_null(request.source_platform):
            body['SourcePlatform'] = request.source_platform
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
        if not DaraCore.is_null(request.create_ramrole):
            body['CreateRAMRole'] = request.create_ramrole
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.identity_provider_name):
            body['IdentityProviderName'] = request.identity_provider_name
        if not DaraCore.is_null(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not DaraCore.is_null(request.session_binding_enabled):
            body['SessionBindingEnabled'] = request.session_binding_enabled
        if not DaraCore.is_null(request.source_agent_arn):
            body['SourceAgentArn'] = request.source_agent_arn
        if not DaraCore.is_null(request.source_platform):
            body['SourcePlatform'] = request.source_platform
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
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
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
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
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

    def delete_client_secret_with_options(
        self,
        request: main_models.DeleteClientSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClientSecretResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_name):
            body['ClientName'] = request.client_name
        if not DaraCore.is_null(request.client_secret_id):
            body['ClientSecretId'] = request.client_secret_id
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteClientSecret',
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
            main_models.DeleteClientSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_client_secret_with_options_async(
        self,
        request: main_models.DeleteClientSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClientSecretResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_name):
            body['ClientName'] = request.client_name
        if not DaraCore.is_null(request.client_secret_id):
            body['ClientSecretId'] = request.client_secret_id
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteClientSecret',
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
            main_models.DeleteClientSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_client_secret(
        self,
        request: main_models.DeleteClientSecretRequest,
    ) -> main_models.DeleteClientSecretResponse:
        runtime = RuntimeOptions()
        return self.delete_client_secret_with_options(request, runtime)

    async def delete_client_secret_async(
        self,
        request: main_models.DeleteClientSecretRequest,
    ) -> main_models.DeleteClientSecretResponse:
        runtime = RuntimeOptions()
        return await self.delete_client_secret_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
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
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
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

    def delete_policy_with_options(
        self,
        request: main_models.DeletePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicy',
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
            main_models.DeletePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_with_options_async(
        self,
        request: main_models.DeletePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicy',
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
            main_models.DeletePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy(
        self,
        request: main_models.DeletePolicyRequest,
    ) -> main_models.DeletePolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_policy_with_options(request, runtime)

    async def delete_policy_async(
        self,
        request: main_models.DeletePolicyRequest,
    ) -> main_models.DeletePolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_policy_with_options_async(request, runtime)

    def delete_policy_set_with_options(
        self,
        request: main_models.DeletePolicySetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicySetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicySet',
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
            main_models.DeletePolicySetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_set_with_options_async(
        self,
        request: main_models.DeletePolicySetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicySetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicySet',
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
            main_models.DeletePolicySetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy_set(
        self,
        request: main_models.DeletePolicySetRequest,
    ) -> main_models.DeletePolicySetResponse:
        runtime = RuntimeOptions()
        return self.delete_policy_set_with_options(request, runtime)

    async def delete_policy_set_async(
        self,
        request: main_models.DeletePolicySetRequest,
    ) -> main_models.DeletePolicySetResponse:
        runtime = RuntimeOptions()
        return await self.delete_policy_set_with_options_async(request, runtime)

    def delete_role_with_options(
        self,
        request: main_models.DeleteRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.role_name):
            body['RoleName'] = request.role_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRole',
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
            main_models.DeleteRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_role_with_options_async(
        self,
        request: main_models.DeleteRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.role_name):
            body['RoleName'] = request.role_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRole',
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
            main_models.DeleteRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_role(
        self,
        request: main_models.DeleteRoleRequest,
    ) -> main_models.DeleteRoleResponse:
        runtime = RuntimeOptions()
        return self.delete_role_with_options(request, runtime)

    async def delete_role_async(
        self,
        request: main_models.DeleteRoleRequest,
    ) -> main_models.DeleteRoleResponse:
        runtime = RuntimeOptions()
        return await self.delete_role_with_options_async(request, runtime)

    def delete_role_assignment_with_options(
        self,
        request: main_models.DeleteRoleAssignmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRoleAssignmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.principal_name):
            body['PrincipalName'] = request.principal_name
        if not DaraCore.is_null(request.principal_type):
            body['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.role_name):
            body['RoleName'] = request.role_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRoleAssignment',
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
            main_models.DeleteRoleAssignmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_role_assignment_with_options_async(
        self,
        request: main_models.DeleteRoleAssignmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRoleAssignmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.principal_name):
            body['PrincipalName'] = request.principal_name
        if not DaraCore.is_null(request.principal_type):
            body['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.role_name):
            body['RoleName'] = request.role_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRoleAssignment',
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
            main_models.DeleteRoleAssignmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_role_assignment(
        self,
        request: main_models.DeleteRoleAssignmentRequest,
    ) -> main_models.DeleteRoleAssignmentResponse:
        runtime = RuntimeOptions()
        return self.delete_role_assignment_with_options(request, runtime)

    async def delete_role_assignment_async(
        self,
        request: main_models.DeleteRoleAssignmentRequest,
    ) -> main_models.DeleteRoleAssignmentResponse:
        runtime = RuntimeOptions()
        return await self.delete_role_assignment_with_options_async(request, runtime)

    def delete_samlidentity_provider_certificate_with_options(
        self,
        request: main_models.DeleteSAMLIdentityProviderCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSAMLIdentityProviderCertificateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.certificate_id):
            body['CertificateId'] = request.certificate_id
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSAMLIdentityProviderCertificate',
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
            main_models.DeleteSAMLIdentityProviderCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_samlidentity_provider_certificate_with_options_async(
        self,
        request: main_models.DeleteSAMLIdentityProviderCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSAMLIdentityProviderCertificateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.certificate_id):
            body['CertificateId'] = request.certificate_id
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSAMLIdentityProviderCertificate',
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
            main_models.DeleteSAMLIdentityProviderCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_samlidentity_provider_certificate(
        self,
        request: main_models.DeleteSAMLIdentityProviderCertificateRequest,
    ) -> main_models.DeleteSAMLIdentityProviderCertificateResponse:
        runtime = RuntimeOptions()
        return self.delete_samlidentity_provider_certificate_with_options(request, runtime)

    async def delete_samlidentity_provider_certificate_async(
        self,
        request: main_models.DeleteSAMLIdentityProviderCertificateRequest,
    ) -> main_models.DeleteSAMLIdentityProviderCertificateResponse:
        runtime = RuntimeOptions()
        return await self.delete_samlidentity_provider_certificate_with_options_async(request, runtime)

    def delete_token_vault_with_options(
        self,
        request: main_models.DeleteTokenVaultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTokenVaultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTokenVault',
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
            main_models.DeleteTokenVaultResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_token_vault_with_options_async(
        self,
        request: main_models.DeleteTokenVaultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTokenVaultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTokenVault',
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
            main_models.DeleteTokenVaultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_token_vault(
        self,
        request: main_models.DeleteTokenVaultRequest,
    ) -> main_models.DeleteTokenVaultResponse:
        runtime = RuntimeOptions()
        return self.delete_token_vault_with_options(request, runtime)

    async def delete_token_vault_async(
        self,
        request: main_models.DeleteTokenVaultRequest,
    ) -> main_models.DeleteTokenVaultResponse:
        runtime = RuntimeOptions()
        return await self.delete_token_vault_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: main_models.DeleteUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
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
            main_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: main_models.DeleteUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
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
            main_models.DeleteUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user(
        self,
        request: main_models.DeleteUserRequest,
    ) -> main_models.DeleteUserResponse:
        runtime = RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: main_models.DeleteUserRequest,
    ) -> main_models.DeleteUserResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def delete_user_pool_with_options(
        self,
        request: main_models.DeleteUserPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserPoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserPool',
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
            main_models.DeleteUserPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_pool_with_options_async(
        self,
        request: main_models.DeleteUserPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserPoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserPool',
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
            main_models.DeleteUserPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_pool(
        self,
        request: main_models.DeleteUserPoolRequest,
    ) -> main_models.DeleteUserPoolResponse:
        runtime = RuntimeOptions()
        return self.delete_user_pool_with_options(request, runtime)

    async def delete_user_pool_async(
        self,
        request: main_models.DeleteUserPoolRequest,
    ) -> main_models.DeleteUserPoolResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_pool_with_options_async(request, runtime)

    def delete_user_pool_client_with_options(
        self,
        request: main_models.DeleteUserPoolClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserPoolClientResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_name):
            body['ClientName'] = request.client_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserPoolClient',
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
            main_models.DeleteUserPoolClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_pool_client_with_options_async(
        self,
        request: main_models.DeleteUserPoolClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserPoolClientResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_name):
            body['ClientName'] = request.client_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserPoolClient',
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
            main_models.DeleteUserPoolClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_pool_client(
        self,
        request: main_models.DeleteUserPoolClientRequest,
    ) -> main_models.DeleteUserPoolClientResponse:
        runtime = RuntimeOptions()
        return self.delete_user_pool_client_with_options(request, runtime)

    async def delete_user_pool_client_async(
        self,
        request: main_models.DeleteUserPoolClientRequest,
    ) -> main_models.DeleteUserPoolClientResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_pool_client_with_options_async(request, runtime)

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

    def detach_policy_set_from_gateway_with_options(
        self,
        request: main_models.DetachPolicySetFromGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachPolicySetFromGatewayResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.gateway_arn):
            body['GatewayArn'] = request.gateway_arn
        if not DaraCore.is_null(request.gateway_type):
            body['GatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DetachPolicySetFromGateway',
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
            main_models.DetachPolicySetFromGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_policy_set_from_gateway_with_options_async(
        self,
        request: main_models.DetachPolicySetFromGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachPolicySetFromGatewayResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.gateway_arn):
            body['GatewayArn'] = request.gateway_arn
        if not DaraCore.is_null(request.gateway_type):
            body['GatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DetachPolicySetFromGateway',
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
            main_models.DetachPolicySetFromGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_policy_set_from_gateway(
        self,
        request: main_models.DetachPolicySetFromGatewayRequest,
    ) -> main_models.DetachPolicySetFromGatewayResponse:
        runtime = RuntimeOptions()
        return self.detach_policy_set_from_gateway_with_options(request, runtime)

    async def detach_policy_set_from_gateway_async(
        self,
        request: main_models.DetachPolicySetFromGatewayRequest,
    ) -> main_models.DetachPolicySetFromGatewayResponse:
        runtime = RuntimeOptions()
        return await self.detach_policy_set_from_gateway_with_options_async(request, runtime)

    def get_apikey_credential_provider_with_options(
        self,
        request: main_models.GetAPIKeyCredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAPIKeyCredentialProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.apikey_credential_provider_name):
            body['APIKeyCredentialProviderName'] = request.apikey_credential_provider_name
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
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
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
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

    def get_gateway_policy_config_with_options(
        self,
        request: main_models.GetGatewayPolicyConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayPolicyConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.gateway_arn):
            body['GatewayArn'] = request.gateway_arn
        if not DaraCore.is_null(request.gateway_type):
            body['GatewayType'] = request.gateway_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGatewayPolicyConfig',
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
            main_models.GetGatewayPolicyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gateway_policy_config_with_options_async(
        self,
        request: main_models.GetGatewayPolicyConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayPolicyConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.gateway_arn):
            body['GatewayArn'] = request.gateway_arn
        if not DaraCore.is_null(request.gateway_type):
            body['GatewayType'] = request.gateway_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGatewayPolicyConfig',
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
            main_models.GetGatewayPolicyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gateway_policy_config(
        self,
        request: main_models.GetGatewayPolicyConfigRequest,
    ) -> main_models.GetGatewayPolicyConfigResponse:
        runtime = RuntimeOptions()
        return self.get_gateway_policy_config_with_options(request, runtime)

    async def get_gateway_policy_config_async(
        self,
        request: main_models.GetGatewayPolicyConfigRequest,
    ) -> main_models.GetGatewayPolicyConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_gateway_policy_config_with_options_async(request, runtime)

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

    def get_login_preference_with_options(
        self,
        request: main_models.GetLoginPreferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLoginPreferenceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLoginPreference',
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
            main_models.GetLoginPreferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_login_preference_with_options_async(
        self,
        request: main_models.GetLoginPreferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLoginPreferenceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLoginPreference',
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
            main_models.GetLoginPreferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_login_preference(
        self,
        request: main_models.GetLoginPreferenceRequest,
    ) -> main_models.GetLoginPreferenceResponse:
        runtime = RuntimeOptions()
        return self.get_login_preference_with_options(request, runtime)

    async def get_login_preference_async(
        self,
        request: main_models.GetLoginPreferenceRequest,
    ) -> main_models.GetLoginPreferenceResponse:
        runtime = RuntimeOptions()
        return await self.get_login_preference_with_options_async(request, runtime)

    def get_oauth2_credential_provider_with_options(
        self,
        request: main_models.GetOAuth2CredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOAuth2CredentialProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.oauth2_credential_provider_name):
            body['OAuth2CredentialProviderName'] = request.oauth2_credential_provider_name
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
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
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
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

    def get_policy_with_options(
        self,
        request: main_models.GetPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPolicy',
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
            main_models.GetPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_with_options_async(
        self,
        request: main_models.GetPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPolicy',
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
            main_models.GetPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy(
        self,
        request: main_models.GetPolicyRequest,
    ) -> main_models.GetPolicyResponse:
        runtime = RuntimeOptions()
        return self.get_policy_with_options(request, runtime)

    async def get_policy_async(
        self,
        request: main_models.GetPolicyRequest,
    ) -> main_models.GetPolicyResponse:
        runtime = RuntimeOptions()
        return await self.get_policy_with_options_async(request, runtime)

    def get_policy_set_with_options(
        self,
        request: main_models.GetPolicySetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicySetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPolicySet',
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
            main_models.GetPolicySetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_set_with_options_async(
        self,
        request: main_models.GetPolicySetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicySetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPolicySet',
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
            main_models.GetPolicySetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy_set(
        self,
        request: main_models.GetPolicySetRequest,
    ) -> main_models.GetPolicySetResponse:
        runtime = RuntimeOptions()
        return self.get_policy_set_with_options(request, runtime)

    async def get_policy_set_async(
        self,
        request: main_models.GetPolicySetRequest,
    ) -> main_models.GetPolicySetResponse:
        runtime = RuntimeOptions()
        return await self.get_policy_set_with_options_async(request, runtime)

    def get_role_with_options(
        self,
        request: main_models.GetRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.role_name):
            body['RoleName'] = request.role_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetRole',
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
            main_models.GetRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_role_with_options_async(
        self,
        request: main_models.GetRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.role_name):
            body['RoleName'] = request.role_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetRole',
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
            main_models.GetRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_role(
        self,
        request: main_models.GetRoleRequest,
    ) -> main_models.GetRoleResponse:
        runtime = RuntimeOptions()
        return self.get_role_with_options(request, runtime)

    async def get_role_async(
        self,
        request: main_models.GetRoleRequest,
    ) -> main_models.GetRoleResponse:
        runtime = RuntimeOptions()
        return await self.get_role_with_options_async(request, runtime)

    def get_samlidentity_provider_with_options(
        self,
        request: main_models.GetSAMLIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSAMLIdentityProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSAMLIdentityProvider',
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
            main_models.GetSAMLIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_samlidentity_provider_with_options_async(
        self,
        request: main_models.GetSAMLIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSAMLIdentityProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSAMLIdentityProvider',
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
            main_models.GetSAMLIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_samlidentity_provider(
        self,
        request: main_models.GetSAMLIdentityProviderRequest,
    ) -> main_models.GetSAMLIdentityProviderResponse:
        runtime = RuntimeOptions()
        return self.get_samlidentity_provider_with_options(request, runtime)

    async def get_samlidentity_provider_async(
        self,
        request: main_models.GetSAMLIdentityProviderRequest,
    ) -> main_models.GetSAMLIdentityProviderResponse:
        runtime = RuntimeOptions()
        return await self.get_samlidentity_provider_with_options_async(request, runtime)

    def get_samlservice_provider_info_with_options(
        self,
        request: main_models.GetSAMLServiceProviderInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSAMLServiceProviderInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSAMLServiceProviderInfo',
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
            main_models.GetSAMLServiceProviderInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_samlservice_provider_info_with_options_async(
        self,
        request: main_models.GetSAMLServiceProviderInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSAMLServiceProviderInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSAMLServiceProviderInfo',
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
            main_models.GetSAMLServiceProviderInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_samlservice_provider_info(
        self,
        request: main_models.GetSAMLServiceProviderInfoRequest,
    ) -> main_models.GetSAMLServiceProviderInfoResponse:
        runtime = RuntimeOptions()
        return self.get_samlservice_provider_info_with_options(request, runtime)

    async def get_samlservice_provider_info_async(
        self,
        request: main_models.GetSAMLServiceProviderInfoRequest,
    ) -> main_models.GetSAMLServiceProviderInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_samlservice_provider_info_with_options_async(request, runtime)

    def get_specific_identity_provider_with_options(
        self,
        request: main_models.GetSpecificIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSpecificIdentityProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identity_provider_type):
            body['IdentityProviderType'] = request.identity_provider_type
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSpecificIdentityProvider',
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
            main_models.GetSpecificIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_specific_identity_provider_with_options_async(
        self,
        request: main_models.GetSpecificIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSpecificIdentityProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identity_provider_type):
            body['IdentityProviderType'] = request.identity_provider_type
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSpecificIdentityProvider',
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
            main_models.GetSpecificIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_specific_identity_provider(
        self,
        request: main_models.GetSpecificIdentityProviderRequest,
    ) -> main_models.GetSpecificIdentityProviderResponse:
        runtime = RuntimeOptions()
        return self.get_specific_identity_provider_with_options(request, runtime)

    async def get_specific_identity_provider_async(
        self,
        request: main_models.GetSpecificIdentityProviderRequest,
    ) -> main_models.GetSpecificIdentityProviderResponse:
        runtime = RuntimeOptions()
        return await self.get_specific_identity_provider_with_options_async(request, runtime)

    def get_token_vault_with_options(
        self,
        request: main_models.GetTokenVaultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenVaultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTokenVault',
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
            main_models.GetTokenVaultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_token_vault_with_options_async(
        self,
        request: main_models.GetTokenVaultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenVaultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTokenVault',
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
            main_models.GetTokenVaultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_token_vault(
        self,
        request: main_models.GetTokenVaultRequest,
    ) -> main_models.GetTokenVaultResponse:
        runtime = RuntimeOptions()
        return self.get_token_vault_with_options(request, runtime)

    async def get_token_vault_async(
        self,
        request: main_models.GetTokenVaultRequest,
    ) -> main_models.GetTokenVaultResponse:
        runtime = RuntimeOptions()
        return await self.get_token_vault_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        request: main_models.GetUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
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
            main_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: main_models.GetUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
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
            main_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        request: main_models.GetUserRequest,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    async def get_user_async(
        self,
        request: main_models.GetUserRequest,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        return await self.get_user_with_options_async(request, runtime)

    def get_user_pool_with_options(
        self,
        request: main_models.GetUserPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserPoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUserPool',
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
            main_models.GetUserPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_pool_with_options_async(
        self,
        request: main_models.GetUserPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserPoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUserPool',
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
            main_models.GetUserPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_pool(
        self,
        request: main_models.GetUserPoolRequest,
    ) -> main_models.GetUserPoolResponse:
        runtime = RuntimeOptions()
        return self.get_user_pool_with_options(request, runtime)

    async def get_user_pool_async(
        self,
        request: main_models.GetUserPoolRequest,
    ) -> main_models.GetUserPoolResponse:
        runtime = RuntimeOptions()
        return await self.get_user_pool_with_options_async(request, runtime)

    def get_user_pool_client_with_options(
        self,
        request: main_models.GetUserPoolClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserPoolClientResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_name):
            body['ClientName'] = request.client_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUserPoolClient',
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
            main_models.GetUserPoolClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_pool_client_with_options_async(
        self,
        request: main_models.GetUserPoolClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserPoolClientResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_name):
            body['ClientName'] = request.client_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUserPoolClient',
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
            main_models.GetUserPoolClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_pool_client(
        self,
        request: main_models.GetUserPoolClientRequest,
    ) -> main_models.GetUserPoolClientResponse:
        runtime = RuntimeOptions()
        return self.get_user_pool_client_with_options(request, runtime)

    async def get_user_pool_client_async(
        self,
        request: main_models.GetUserPoolClientRequest,
    ) -> main_models.GetUserPoolClientResponse:
        runtime = RuntimeOptions()
        return await self.get_user_pool_client_with_options_async(request, runtime)

    def get_user_pool_sync_job_with_options(
        self,
        request: main_models.GetUserPoolSyncJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserPoolSyncJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.synchronization_job_id):
            body['SynchronizationJobId'] = request.synchronization_job_id
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUserPoolSyncJob',
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
            main_models.GetUserPoolSyncJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_pool_sync_job_with_options_async(
        self,
        request: main_models.GetUserPoolSyncJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserPoolSyncJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.synchronization_job_id):
            body['SynchronizationJobId'] = request.synchronization_job_id
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUserPoolSyncJob',
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
            main_models.GetUserPoolSyncJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_pool_sync_job(
        self,
        request: main_models.GetUserPoolSyncJobRequest,
    ) -> main_models.GetUserPoolSyncJobResponse:
        runtime = RuntimeOptions()
        return self.get_user_pool_sync_job_with_options(request, runtime)

    async def get_user_pool_sync_job_async(
        self,
        request: main_models.GetUserPoolSyncJobRequest,
    ) -> main_models.GetUserPoolSyncJobResponse:
        runtime = RuntimeOptions()
        return await self.get_user_pool_sync_job_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
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
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
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

    def list_client_secrets_with_options(
        self,
        request: main_models.ListClientSecretsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClientSecretsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_name):
            body['ClientName'] = request.client_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListClientSecrets',
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
            main_models.ListClientSecretsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_client_secrets_with_options_async(
        self,
        request: main_models.ListClientSecretsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClientSecretsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_name):
            body['ClientName'] = request.client_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListClientSecrets',
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
            main_models.ListClientSecretsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_client_secrets(
        self,
        request: main_models.ListClientSecretsRequest,
    ) -> main_models.ListClientSecretsResponse:
        runtime = RuntimeOptions()
        return self.list_client_secrets_with_options(request, runtime)

    async def list_client_secrets_async(
        self,
        request: main_models.ListClientSecretsRequest,
    ) -> main_models.ListClientSecretsResponse:
        runtime = RuntimeOptions()
        return await self.list_client_secrets_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
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
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
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

    def list_policies_with_options(
        self,
        request: main_models.ListPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicies',
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
            main_models.ListPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_with_options_async(
        self,
        request: main_models.ListPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicies',
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
            main_models.ListPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policies(
        self,
        request: main_models.ListPoliciesRequest,
    ) -> main_models.ListPoliciesResponse:
        runtime = RuntimeOptions()
        return self.list_policies_with_options(request, runtime)

    async def list_policies_async(
        self,
        request: main_models.ListPoliciesRequest,
    ) -> main_models.ListPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.list_policies_with_options_async(request, runtime)

    def list_policy_set_attached_gateways_with_options(
        self,
        request: main_models.ListPolicySetAttachedGatewaysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicySetAttachedGatewaysResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.gateway_type):
            body['GatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicySetAttachedGateways',
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
            main_models.ListPolicySetAttachedGatewaysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policy_set_attached_gateways_with_options_async(
        self,
        request: main_models.ListPolicySetAttachedGatewaysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicySetAttachedGatewaysResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.gateway_type):
            body['GatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicySetAttachedGateways',
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
            main_models.ListPolicySetAttachedGatewaysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policy_set_attached_gateways(
        self,
        request: main_models.ListPolicySetAttachedGatewaysRequest,
    ) -> main_models.ListPolicySetAttachedGatewaysResponse:
        runtime = RuntimeOptions()
        return self.list_policy_set_attached_gateways_with_options(request, runtime)

    async def list_policy_set_attached_gateways_async(
        self,
        request: main_models.ListPolicySetAttachedGatewaysRequest,
    ) -> main_models.ListPolicySetAttachedGatewaysResponse:
        runtime = RuntimeOptions()
        return await self.list_policy_set_attached_gateways_with_options_async(request, runtime)

    def list_policy_sets_with_options(
        self,
        request: main_models.ListPolicySetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicySetsResponse:
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
            action = 'ListPolicySets',
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
            main_models.ListPolicySetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policy_sets_with_options_async(
        self,
        request: main_models.ListPolicySetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicySetsResponse:
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
            action = 'ListPolicySets',
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
            main_models.ListPolicySetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policy_sets(
        self,
        request: main_models.ListPolicySetsRequest,
    ) -> main_models.ListPolicySetsResponse:
        runtime = RuntimeOptions()
        return self.list_policy_sets_with_options(request, runtime)

    async def list_policy_sets_async(
        self,
        request: main_models.ListPolicySetsRequest,
    ) -> main_models.ListPolicySetsResponse:
        runtime = RuntimeOptions()
        return await self.list_policy_sets_with_options_async(request, runtime)

    def list_role_assignments_with_options(
        self,
        request: main_models.ListRoleAssignmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRoleAssignmentsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.principal_name):
            body['PrincipalName'] = request.principal_name
        if not DaraCore.is_null(request.principal_type):
            body['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.role_name):
            body['RoleName'] = request.role_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRoleAssignments',
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
            main_models.ListRoleAssignmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_role_assignments_with_options_async(
        self,
        request: main_models.ListRoleAssignmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRoleAssignmentsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.principal_name):
            body['PrincipalName'] = request.principal_name
        if not DaraCore.is_null(request.principal_type):
            body['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.role_name):
            body['RoleName'] = request.role_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRoleAssignments',
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
            main_models.ListRoleAssignmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_role_assignments(
        self,
        request: main_models.ListRoleAssignmentsRequest,
    ) -> main_models.ListRoleAssignmentsResponse:
        runtime = RuntimeOptions()
        return self.list_role_assignments_with_options(request, runtime)

    async def list_role_assignments_async(
        self,
        request: main_models.ListRoleAssignmentsRequest,
    ) -> main_models.ListRoleAssignmentsResponse:
        runtime = RuntimeOptions()
        return await self.list_role_assignments_with_options_async(request, runtime)

    def list_roles_with_options(
        self,
        request: main_models.ListRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRolesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRoles',
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
            main_models.ListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        request: main_models.ListRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRolesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRoles',
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
            main_models.ListRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_roles(
        self,
        request: main_models.ListRolesRequest,
    ) -> main_models.ListRolesResponse:
        runtime = RuntimeOptions()
        return self.list_roles_with_options(request, runtime)

    async def list_roles_async(
        self,
        request: main_models.ListRolesRequest,
    ) -> main_models.ListRolesResponse:
        runtime = RuntimeOptions()
        return await self.list_roles_with_options_async(request, runtime)

    def list_samlidentity_provider_certificates_with_options(
        self,
        request: main_models.ListSAMLIdentityProviderCertificatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSAMLIdentityProviderCertificatesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSAMLIdentityProviderCertificates',
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
            main_models.ListSAMLIdentityProviderCertificatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_samlidentity_provider_certificates_with_options_async(
        self,
        request: main_models.ListSAMLIdentityProviderCertificatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSAMLIdentityProviderCertificatesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSAMLIdentityProviderCertificates',
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
            main_models.ListSAMLIdentityProviderCertificatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_samlidentity_provider_certificates(
        self,
        request: main_models.ListSAMLIdentityProviderCertificatesRequest,
    ) -> main_models.ListSAMLIdentityProviderCertificatesResponse:
        runtime = RuntimeOptions()
        return self.list_samlidentity_provider_certificates_with_options(request, runtime)

    async def list_samlidentity_provider_certificates_async(
        self,
        request: main_models.ListSAMLIdentityProviderCertificatesRequest,
    ) -> main_models.ListSAMLIdentityProviderCertificatesResponse:
        runtime = RuntimeOptions()
        return await self.list_samlidentity_provider_certificates_with_options_async(request, runtime)

    def list_token_vaults_with_options(
        self,
        request: main_models.ListTokenVaultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTokenVaultsResponse:
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
            action = 'ListTokenVaults',
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
            main_models.ListTokenVaultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_token_vaults_with_options_async(
        self,
        request: main_models.ListTokenVaultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTokenVaultsResponse:
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
            action = 'ListTokenVaults',
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
            main_models.ListTokenVaultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_token_vaults(
        self,
        request: main_models.ListTokenVaultsRequest,
    ) -> main_models.ListTokenVaultsResponse:
        runtime = RuntimeOptions()
        return self.list_token_vaults_with_options(request, runtime)

    async def list_token_vaults_async(
        self,
        request: main_models.ListTokenVaultsRequest,
    ) -> main_models.ListTokenVaultsResponse:
        runtime = RuntimeOptions()
        return await self.list_token_vaults_with_options_async(request, runtime)

    def list_user_pool_clients_with_options(
        self,
        request: main_models.ListUserPoolClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserPoolClientsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUserPoolClients',
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
            main_models.ListUserPoolClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_pool_clients_with_options_async(
        self,
        request: main_models.ListUserPoolClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserPoolClientsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUserPoolClients',
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
            main_models.ListUserPoolClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_pool_clients(
        self,
        request: main_models.ListUserPoolClientsRequest,
    ) -> main_models.ListUserPoolClientsResponse:
        runtime = RuntimeOptions()
        return self.list_user_pool_clients_with_options(request, runtime)

    async def list_user_pool_clients_async(
        self,
        request: main_models.ListUserPoolClientsRequest,
    ) -> main_models.ListUserPoolClientsResponse:
        runtime = RuntimeOptions()
        return await self.list_user_pool_clients_with_options_async(request, runtime)

    def list_user_pool_sync_jobs_with_options(
        self,
        request: main_models.ListUserPoolSyncJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserPoolSyncJobsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUserPoolSyncJobs',
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
            main_models.ListUserPoolSyncJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_pool_sync_jobs_with_options_async(
        self,
        request: main_models.ListUserPoolSyncJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserPoolSyncJobsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUserPoolSyncJobs',
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
            main_models.ListUserPoolSyncJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_pool_sync_jobs(
        self,
        request: main_models.ListUserPoolSyncJobsRequest,
    ) -> main_models.ListUserPoolSyncJobsResponse:
        runtime = RuntimeOptions()
        return self.list_user_pool_sync_jobs_with_options(request, runtime)

    async def list_user_pool_sync_jobs_async(
        self,
        request: main_models.ListUserPoolSyncJobsRequest,
    ) -> main_models.ListUserPoolSyncJobsResponse:
        runtime = RuntimeOptions()
        return await self.list_user_pool_sync_jobs_with_options_async(request, runtime)

    def list_user_pools_with_options(
        self,
        request: main_models.ListUserPoolsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserPoolsResponse:
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
            action = 'ListUserPools',
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
            main_models.ListUserPoolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_pools_with_options_async(
        self,
        request: main_models.ListUserPoolsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserPoolsResponse:
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
            action = 'ListUserPools',
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
            main_models.ListUserPoolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_pools(
        self,
        request: main_models.ListUserPoolsRequest,
    ) -> main_models.ListUserPoolsResponse:
        runtime = RuntimeOptions()
        return self.list_user_pools_with_options(request, runtime)

    async def list_user_pools_async(
        self,
        request: main_models.ListUserPoolsRequest,
    ) -> main_models.ListUserPoolsResponse:
        runtime = RuntimeOptions()
        return await self.list_user_pools_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: main_models.ListUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
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
            main_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: main_models.ListUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
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
            main_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

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

    def run_user_pool_sync_job_with_options(
        self,
        request: main_models.RunUserPoolSyncJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunUserPoolSyncJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identity_provider_type):
            body['IdentityProviderType'] = request.identity_provider_type
        if not DaraCore.is_null(request.max_sync_users):
            body['MaxSyncUsers'] = request.max_sync_users
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunUserPoolSyncJob',
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
            main_models.RunUserPoolSyncJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_user_pool_sync_job_with_options_async(
        self,
        request: main_models.RunUserPoolSyncJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunUserPoolSyncJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identity_provider_type):
            body['IdentityProviderType'] = request.identity_provider_type
        if not DaraCore.is_null(request.max_sync_users):
            body['MaxSyncUsers'] = request.max_sync_users
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunUserPoolSyncJob',
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
            main_models.RunUserPoolSyncJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_user_pool_sync_job(
        self,
        request: main_models.RunUserPoolSyncJobRequest,
    ) -> main_models.RunUserPoolSyncJobResponse:
        runtime = RuntimeOptions()
        return self.run_user_pool_sync_job_with_options(request, runtime)

    async def run_user_pool_sync_job_async(
        self,
        request: main_models.RunUserPoolSyncJobRequest,
    ) -> main_models.RunUserPoolSyncJobResponse:
        runtime = RuntimeOptions()
        return await self.run_user_pool_sync_job_with_options_async(request, runtime)

    def set_samlidentity_provider_with_options(
        self,
        tmp_req: main_models.SetSAMLIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSAMLIdentityProviderResponse:
        tmp_req.validate()
        request = main_models.SetSAMLIdentityProviderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.x_509certificates):
            request.x_509certificates_shrink = Utils.array_to_string_with_specified_style(tmp_req.x_509certificates, 'X509Certificates', 'json')
        body = {}
        if not DaraCore.is_null(request.entity_id):
            body['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.jitprovision_status):
            body['JITProvisionStatus'] = request.jitprovision_status
        if not DaraCore.is_null(request.jitupdate_status):
            body['JITUpdateStatus'] = request.jitupdate_status
        if not DaraCore.is_null(request.login_url):
            body['LoginURL'] = request.login_url
        if not DaraCore.is_null(request.samlbinding_type):
            body['SAMLBindingType'] = request.samlbinding_type
        if not DaraCore.is_null(request.ssostatus):
            body['SSOStatus'] = request.ssostatus
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        if not DaraCore.is_null(request.x_509certificates_shrink):
            body['X509Certificates'] = request.x_509certificates_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetSAMLIdentityProvider',
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
            main_models.SetSAMLIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_samlidentity_provider_with_options_async(
        self,
        tmp_req: main_models.SetSAMLIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSAMLIdentityProviderResponse:
        tmp_req.validate()
        request = main_models.SetSAMLIdentityProviderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.x_509certificates):
            request.x_509certificates_shrink = Utils.array_to_string_with_specified_style(tmp_req.x_509certificates, 'X509Certificates', 'json')
        body = {}
        if not DaraCore.is_null(request.entity_id):
            body['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.jitprovision_status):
            body['JITProvisionStatus'] = request.jitprovision_status
        if not DaraCore.is_null(request.jitupdate_status):
            body['JITUpdateStatus'] = request.jitupdate_status
        if not DaraCore.is_null(request.login_url):
            body['LoginURL'] = request.login_url
        if not DaraCore.is_null(request.samlbinding_type):
            body['SAMLBindingType'] = request.samlbinding_type
        if not DaraCore.is_null(request.ssostatus):
            body['SSOStatus'] = request.ssostatus
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        if not DaraCore.is_null(request.x_509certificates_shrink):
            body['X509Certificates'] = request.x_509certificates_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetSAMLIdentityProvider',
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
            main_models.SetSAMLIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_samlidentity_provider(
        self,
        request: main_models.SetSAMLIdentityProviderRequest,
    ) -> main_models.SetSAMLIdentityProviderResponse:
        runtime = RuntimeOptions()
        return self.set_samlidentity_provider_with_options(request, runtime)

    async def set_samlidentity_provider_async(
        self,
        request: main_models.SetSAMLIdentityProviderRequest,
    ) -> main_models.SetSAMLIdentityProviderResponse:
        runtime = RuntimeOptions()
        return await self.set_samlidentity_provider_with_options_async(request, runtime)

    def set_specific_identity_provider_with_options(
        self,
        request: main_models.SetSpecificIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSpecificIdentityProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.idpmetadata):
            body['IDPMetadata'] = request.idpmetadata
        if not DaraCore.is_null(request.identity_provider_type):
            body['IdentityProviderType'] = request.identity_provider_type
        if not DaraCore.is_null(request.ssostatus):
            body['SSOStatus'] = request.ssostatus
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetSpecificIdentityProvider',
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
            main_models.SetSpecificIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_specific_identity_provider_with_options_async(
        self,
        request: main_models.SetSpecificIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSpecificIdentityProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.idpmetadata):
            body['IDPMetadata'] = request.idpmetadata
        if not DaraCore.is_null(request.identity_provider_type):
            body['IdentityProviderType'] = request.identity_provider_type
        if not DaraCore.is_null(request.ssostatus):
            body['SSOStatus'] = request.ssostatus
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetSpecificIdentityProvider',
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
            main_models.SetSpecificIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_specific_identity_provider(
        self,
        request: main_models.SetSpecificIdentityProviderRequest,
    ) -> main_models.SetSpecificIdentityProviderResponse:
        runtime = RuntimeOptions()
        return self.set_specific_identity_provider_with_options(request, runtime)

    async def set_specific_identity_provider_async(
        self,
        request: main_models.SetSpecificIdentityProviderRequest,
    ) -> main_models.SetSpecificIdentityProviderResponse:
        runtime = RuntimeOptions()
        return await self.set_specific_identity_provider_with_options_async(request, runtime)

    def set_user_password_with_options(
        self,
        request: main_models.SetUserPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetUserPasswordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.generate_random_password):
            body['GenerateRandomPassword'] = request.generate_random_password
        if not DaraCore.is_null(request.password):
            body['Password'] = request.password
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetUserPassword',
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
            main_models.SetUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_user_password_with_options_async(
        self,
        request: main_models.SetUserPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetUserPasswordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.generate_random_password):
            body['GenerateRandomPassword'] = request.generate_random_password
        if not DaraCore.is_null(request.password):
            body['Password'] = request.password
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetUserPassword',
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
            main_models.SetUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_user_password(
        self,
        request: main_models.SetUserPasswordRequest,
    ) -> main_models.SetUserPasswordResponse:
        runtime = RuntimeOptions()
        return self.set_user_password_with_options(request, runtime)

    async def set_user_password_async(
        self,
        request: main_models.SetUserPasswordRequest,
    ) -> main_models.SetUserPasswordResponse:
        runtime = RuntimeOptions()
        return await self.set_user_password_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
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
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
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

    def update_gateway_policy_config_with_options(
        self,
        request: main_models.UpdateGatewayPolicyConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayPolicyConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enforcement_mode):
            body['EnforcementMode'] = request.enforcement_mode
        if not DaraCore.is_null(request.gateway_arn):
            body['GatewayArn'] = request.gateway_arn
        if not DaraCore.is_null(request.gateway_type):
            body['GatewayType'] = request.gateway_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayPolicyConfig',
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
            main_models.UpdateGatewayPolicyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_policy_config_with_options_async(
        self,
        request: main_models.UpdateGatewayPolicyConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayPolicyConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enforcement_mode):
            body['EnforcementMode'] = request.enforcement_mode
        if not DaraCore.is_null(request.gateway_arn):
            body['GatewayArn'] = request.gateway_arn
        if not DaraCore.is_null(request.gateway_type):
            body['GatewayType'] = request.gateway_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayPolicyConfig',
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
            main_models.UpdateGatewayPolicyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_policy_config(
        self,
        request: main_models.UpdateGatewayPolicyConfigRequest,
    ) -> main_models.UpdateGatewayPolicyConfigResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_policy_config_with_options(request, runtime)

    async def update_gateway_policy_config_async(
        self,
        request: main_models.UpdateGatewayPolicyConfigRequest,
    ) -> main_models.UpdateGatewayPolicyConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_policy_config_with_options_async(request, runtime)

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

    def update_login_preference_with_options(
        self,
        tmp_req: main_models.UpdateLoginPreferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLoginPreferenceResponse:
        tmp_req.validate()
        request = main_models.UpdateLoginPreferenceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.login_preference):
            request.login_preference_shrink = Utils.array_to_string_with_specified_style(tmp_req.login_preference, 'LoginPreference', 'json')
        query = {}
        if not DaraCore.is_null(request.login_preference_shrink):
            query['LoginPreference'] = request.login_preference_shrink
        body = {}
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoginPreference',
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
            main_models.UpdateLoginPreferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_login_preference_with_options_async(
        self,
        tmp_req: main_models.UpdateLoginPreferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLoginPreferenceResponse:
        tmp_req.validate()
        request = main_models.UpdateLoginPreferenceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.login_preference):
            request.login_preference_shrink = Utils.array_to_string_with_specified_style(tmp_req.login_preference, 'LoginPreference', 'json')
        query = {}
        if not DaraCore.is_null(request.login_preference_shrink):
            query['LoginPreference'] = request.login_preference_shrink
        body = {}
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoginPreference',
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
            main_models.UpdateLoginPreferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_login_preference(
        self,
        request: main_models.UpdateLoginPreferenceRequest,
    ) -> main_models.UpdateLoginPreferenceResponse:
        runtime = RuntimeOptions()
        return self.update_login_preference_with_options(request, runtime)

    async def update_login_preference_async(
        self,
        request: main_models.UpdateLoginPreferenceRequest,
    ) -> main_models.UpdateLoginPreferenceResponse:
        runtime = RuntimeOptions()
        return await self.update_login_preference_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
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
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
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

    def update_policy_with_options(
        self,
        tmp_req: main_models.UpdatePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePolicyResponse:
        tmp_req.validate()
        request = main_models.UpdatePolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.definition):
            request.definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.definition, 'Definition', 'json')
        body = {}
        if not DaraCore.is_null(request.definition_shrink):
            body['Definition'] = request.definition_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePolicy',
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
            main_models.UpdatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_policy_with_options_async(
        self,
        tmp_req: main_models.UpdatePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePolicyResponse:
        tmp_req.validate()
        request = main_models.UpdatePolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.definition):
            request.definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.definition, 'Definition', 'json')
        body = {}
        if not DaraCore.is_null(request.definition_shrink):
            body['Definition'] = request.definition_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePolicy',
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
            main_models.UpdatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_policy(
        self,
        request: main_models.UpdatePolicyRequest,
    ) -> main_models.UpdatePolicyResponse:
        runtime = RuntimeOptions()
        return self.update_policy_with_options(request, runtime)

    async def update_policy_async(
        self,
        request: main_models.UpdatePolicyRequest,
    ) -> main_models.UpdatePolicyResponse:
        runtime = RuntimeOptions()
        return await self.update_policy_with_options_async(request, runtime)

    def update_policy_set_with_options(
        self,
        request: main_models.UpdatePolicySetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePolicySetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePolicySet',
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
            main_models.UpdatePolicySetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_policy_set_with_options_async(
        self,
        request: main_models.UpdatePolicySetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePolicySetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.policy_set_name):
            body['PolicySetName'] = request.policy_set_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePolicySet',
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
            main_models.UpdatePolicySetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_policy_set(
        self,
        request: main_models.UpdatePolicySetRequest,
    ) -> main_models.UpdatePolicySetResponse:
        runtime = RuntimeOptions()
        return self.update_policy_set_with_options(request, runtime)

    async def update_policy_set_async(
        self,
        request: main_models.UpdatePolicySetRequest,
    ) -> main_models.UpdatePolicySetResponse:
        runtime = RuntimeOptions()
        return await self.update_policy_set_with_options_async(request, runtime)

    def update_role_with_options(
        self,
        request: main_models.UpdateRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.role_name):
            body['RoleName'] = request.role_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRole',
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
            main_models.UpdateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_role_with_options_async(
        self,
        request: main_models.UpdateRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.role_name):
            body['RoleName'] = request.role_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRole',
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
            main_models.UpdateRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_role(
        self,
        request: main_models.UpdateRoleRequest,
    ) -> main_models.UpdateRoleResponse:
        runtime = RuntimeOptions()
        return self.update_role_with_options(request, runtime)

    async def update_role_async(
        self,
        request: main_models.UpdateRoleRequest,
    ) -> main_models.UpdateRoleResponse:
        runtime = RuntimeOptions()
        return await self.update_role_with_options_async(request, runtime)

    def update_token_vault_with_options(
        self,
        request: main_models.UpdateTokenVaultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTokenVaultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTokenVault',
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
            main_models.UpdateTokenVaultResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_token_vault_with_options_async(
        self,
        request: main_models.UpdateTokenVaultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTokenVaultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not DaraCore.is_null(request.token_vault_name):
            body['TokenVaultName'] = request.token_vault_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTokenVault',
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
            main_models.UpdateTokenVaultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_token_vault(
        self,
        request: main_models.UpdateTokenVaultRequest,
    ) -> main_models.UpdateTokenVaultResponse:
        runtime = RuntimeOptions()
        return self.update_token_vault_with_options(request, runtime)

    async def update_token_vault_async(
        self,
        request: main_models.UpdateTokenVaultRequest,
    ) -> main_models.UpdateTokenVaultResponse:
        runtime = RuntimeOptions()
        return await self.update_token_vault_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: main_models.UpdateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            body['Email'] = request.email
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
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
            main_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: main_models.UpdateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            body['Email'] = request.email
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
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
            main_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user(
        self,
        request: main_models.UpdateUserRequest,
    ) -> main_models.UpdateUserResponse:
        runtime = RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: main_models.UpdateUserRequest,
    ) -> main_models.UpdateUserResponse:
        runtime = RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)

    def update_user_pool_with_options(
        self,
        request: main_models.UpdateUserPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserPoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserPool',
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
            main_models.UpdateUserPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_pool_with_options_async(
        self,
        request: main_models.UpdateUserPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserPoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserPool',
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
            main_models.UpdateUserPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_pool(
        self,
        request: main_models.UpdateUserPoolRequest,
    ) -> main_models.UpdateUserPoolResponse:
        runtime = RuntimeOptions()
        return self.update_user_pool_with_options(request, runtime)

    async def update_user_pool_async(
        self,
        request: main_models.UpdateUserPoolRequest,
    ) -> main_models.UpdateUserPoolResponse:
        runtime = RuntimeOptions()
        return await self.update_user_pool_with_options_async(request, runtime)

    def update_user_pool_client_with_options(
        self,
        tmp_req: main_models.UpdateUserPoolClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserPoolClientResponse:
        tmp_req.validate()
        request = main_models.UpdateUserPoolClientShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.redirect_uris):
            request.redirect_uris_shrink = Utils.array_to_string_with_specified_style(tmp_req.redirect_uris, 'RedirectURIs', 'json')
        body = {}
        if not DaraCore.is_null(request.access_token_validity):
            body['AccessTokenValidity'] = request.access_token_validity
        if not DaraCore.is_null(request.client_name):
            body['ClientName'] = request.client_name
        if not DaraCore.is_null(request.enforce_pkce):
            body['EnforcePKCE'] = request.enforce_pkce
        if not DaraCore.is_null(request.redirect_uris_shrink):
            body['RedirectURIs'] = request.redirect_uris_shrink
        if not DaraCore.is_null(request.refresh_token_validity):
            body['RefreshTokenValidity'] = request.refresh_token_validity
        if not DaraCore.is_null(request.secret_required):
            body['SecretRequired'] = request.secret_required
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserPoolClient',
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
            main_models.UpdateUserPoolClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_pool_client_with_options_async(
        self,
        tmp_req: main_models.UpdateUserPoolClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserPoolClientResponse:
        tmp_req.validate()
        request = main_models.UpdateUserPoolClientShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.redirect_uris):
            request.redirect_uris_shrink = Utils.array_to_string_with_specified_style(tmp_req.redirect_uris, 'RedirectURIs', 'json')
        body = {}
        if not DaraCore.is_null(request.access_token_validity):
            body['AccessTokenValidity'] = request.access_token_validity
        if not DaraCore.is_null(request.client_name):
            body['ClientName'] = request.client_name
        if not DaraCore.is_null(request.enforce_pkce):
            body['EnforcePKCE'] = request.enforce_pkce
        if not DaraCore.is_null(request.redirect_uris_shrink):
            body['RedirectURIs'] = request.redirect_uris_shrink
        if not DaraCore.is_null(request.refresh_token_validity):
            body['RefreshTokenValidity'] = request.refresh_token_validity
        if not DaraCore.is_null(request.secret_required):
            body['SecretRequired'] = request.secret_required
        if not DaraCore.is_null(request.user_pool_name):
            body['UserPoolName'] = request.user_pool_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserPoolClient',
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
            main_models.UpdateUserPoolClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_pool_client(
        self,
        request: main_models.UpdateUserPoolClientRequest,
    ) -> main_models.UpdateUserPoolClientResponse:
        runtime = RuntimeOptions()
        return self.update_user_pool_client_with_options(request, runtime)

    async def update_user_pool_client_async(
        self,
        request: main_models.UpdateUserPoolClientRequest,
    ) -> main_models.UpdateUserPoolClientResponse:
        runtime = RuntimeOptions()
        return await self.update_user_pool_client_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.session_binding_enabled):
            body['SessionBindingEnabled'] = request.session_binding_enabled
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
        if not DaraCore.is_null(request.session_binding_enabled):
            body['SessionBindingEnabled'] = request.session_binding_enabled
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
