# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agentteams20260605 import models as main_models
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
        self._endpoint = self.get_endpoint('agentteams', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def bind_identity_provider_with_options(
        self,
        request: main_models.BindIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_type):
            query['IdentityProviderType'] = request.identity_provider_type
        if not DaraCore.is_null(request.idp_metadata):
            query['IdpMetadata'] = request.idp_metadata
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.login_enabled):
            query['LoginEnabled'] = request.login_enabled
        if not DaraCore.is_null(request.sync_enabled):
            query['SyncEnabled'] = request.sync_enabled
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BindIdentityProvider',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_identity_provider_with_options_async(
        self,
        request: main_models.BindIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_type):
            query['IdentityProviderType'] = request.identity_provider_type
        if not DaraCore.is_null(request.idp_metadata):
            query['IdpMetadata'] = request.idp_metadata
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.login_enabled):
            query['LoginEnabled'] = request.login_enabled
        if not DaraCore.is_null(request.sync_enabled):
            query['SyncEnabled'] = request.sync_enabled
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BindIdentityProvider',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_identity_provider(
        self,
        request: main_models.BindIdentityProviderRequest,
    ) -> main_models.BindIdentityProviderResponse:
        runtime = RuntimeOptions()
        return self.bind_identity_provider_with_options(request, runtime)

    async def bind_identity_provider_async(
        self,
        request: main_models.BindIdentityProviderRequest,
    ) -> main_models.BindIdentityProviderResponse:
        runtime = RuntimeOptions()
        return await self.bind_identity_provider_with_options_async(request, runtime)

    def configure_nat_gateway_with_options(
        self,
        request: main_models.ConfigureNatGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureNatGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.eip_allocation_id):
            query['EipAllocationId'] = request.eip_allocation_id
        if not DaraCore.is_null(request.eip_bandwidth):
            query['EipBandwidth'] = request.eip_bandwidth
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nat_gateway_instance_id):
            query['NatGatewayInstanceId'] = request.nat_gateway_instance_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureNatGateway',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureNatGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_nat_gateway_with_options_async(
        self,
        request: main_models.ConfigureNatGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureNatGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.eip_allocation_id):
            query['EipAllocationId'] = request.eip_allocation_id
        if not DaraCore.is_null(request.eip_bandwidth):
            query['EipBandwidth'] = request.eip_bandwidth
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nat_gateway_instance_id):
            query['NatGatewayInstanceId'] = request.nat_gateway_instance_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureNatGateway',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureNatGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_nat_gateway(
        self,
        request: main_models.ConfigureNatGatewayRequest,
    ) -> main_models.ConfigureNatGatewayResponse:
        runtime = RuntimeOptions()
        return self.configure_nat_gateway_with_options(request, runtime)

    async def configure_nat_gateway_async(
        self,
        request: main_models.ConfigureNatGatewayRequest,
    ) -> main_models.ConfigureNatGatewayResponse:
        runtime = RuntimeOptions()
        return await self.configure_nat_gateway_with_options_async(request, runtime)

    def create_credential_with_options(
        self,
        request: main_models.CreateCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['ApiKey'] = request.api_key
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCredential',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_credential_with_options_async(
        self,
        request: main_models.CreateCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['ApiKey'] = request.api_key
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCredential',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_credential(
        self,
        request: main_models.CreateCredentialRequest,
    ) -> main_models.CreateCredentialResponse:
        runtime = RuntimeOptions()
        return self.create_credential_with_options(request, runtime)

    async def create_credential_async(
        self,
        request: main_models.CreateCredentialRequest,
    ) -> main_models.CreateCredentialResponse:
        runtime = RuntimeOptions()
        return await self.create_credential_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        tmp_req: main_models.CreateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        tmp_req.validate()
        request = main_models.CreateInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.zones):
            request.zones_shrink = Utils.array_to_string_with_specified_style(tmp_req.zones, 'Zones', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zones_shrink):
            query['Zones'] = request.zones_shrink
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.payment_type):
            body['PaymentType'] = request.payment_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        tmp_req: main_models.CreateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        tmp_req.validate()
        request = main_models.CreateInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.zones):
            request.zones_shrink = Utils.array_to_string_with_specified_style(tmp_req.zones, 'Zones', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zones_shrink):
            query['Zones'] = request.zones_shrink
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.payment_type):
            body['PaymentType'] = request.payment_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_mcp_with_options(
        self,
        tmp_req: main_models.CreateMcpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcpResponse:
        tmp_req.validate()
        request = main_models.CreateMcpShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.addresses):
            request.addresses_shrink = Utils.array_to_string_with_specified_style(tmp_req.addresses, 'Addresses', 'json')
        query = {}
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        body = {}
        if not DaraCore.is_null(request.addresses_shrink):
            body['Addresses'] = request.addresses_shrink
        if not DaraCore.is_null(request.auth_config):
            body['AuthConfig'] = request.auth_config
        if not DaraCore.is_null(request.auth_enabled):
            body['AuthEnabled'] = request.auth_enabled
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.create_type):
            body['CreateType'] = request.create_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.swagger_config):
            body['SwaggerConfig'] = request.swagger_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcp',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcpResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcp_with_options_async(
        self,
        tmp_req: main_models.CreateMcpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcpResponse:
        tmp_req.validate()
        request = main_models.CreateMcpShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.addresses):
            request.addresses_shrink = Utils.array_to_string_with_specified_style(tmp_req.addresses, 'Addresses', 'json')
        query = {}
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        body = {}
        if not DaraCore.is_null(request.addresses_shrink):
            body['Addresses'] = request.addresses_shrink
        if not DaraCore.is_null(request.auth_config):
            body['AuthConfig'] = request.auth_config
        if not DaraCore.is_null(request.auth_enabled):
            body['AuthEnabled'] = request.auth_enabled
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.create_type):
            body['CreateType'] = request.create_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.swagger_config):
            body['SwaggerConfig'] = request.swagger_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcp',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcp(
        self,
        request: main_models.CreateMcpRequest,
    ) -> main_models.CreateMcpResponse:
        runtime = RuntimeOptions()
        return self.create_mcp_with_options(request, runtime)

    async def create_mcp_async(
        self,
        request: main_models.CreateMcpRequest,
    ) -> main_models.CreateMcpResponse:
        runtime = RuntimeOptions()
        return await self.create_mcp_with_options_async(request, runtime)

    def create_model_with_options(
        self,
        tmp_req: main_models.CreateModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelResponse:
        tmp_req.validate()
        request = main_models.CreateModelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.protocols):
            request.protocols_shrink = Utils.array_to_string_with_specified_style(tmp_req.protocols, 'Protocols', 'json')
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.protocols_shrink):
            body['Protocols'] = request.protocols_shrink
        if not DaraCore.is_null(request.provider):
            body['Provider'] = request.provider
        if not DaraCore.is_null(request.provider_id):
            body['ProviderId'] = request.provider_id
        if not DaraCore.is_null(request.provider_name):
            body['ProviderName'] = request.provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModel',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_with_options_async(
        self,
        tmp_req: main_models.CreateModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelResponse:
        tmp_req.validate()
        request = main_models.CreateModelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.protocols):
            request.protocols_shrink = Utils.array_to_string_with_specified_style(tmp_req.protocols, 'Protocols', 'json')
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.protocols_shrink):
            body['Protocols'] = request.protocols_shrink
        if not DaraCore.is_null(request.provider):
            body['Provider'] = request.provider
        if not DaraCore.is_null(request.provider_id):
            body['ProviderId'] = request.provider_id
        if not DaraCore.is_null(request.provider_name):
            body['ProviderName'] = request.provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModel',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model(
        self,
        request: main_models.CreateModelRequest,
    ) -> main_models.CreateModelResponse:
        runtime = RuntimeOptions()
        return self.create_model_with_options(request, runtime)

    async def create_model_async(
        self,
        request: main_models.CreateModelRequest,
    ) -> main_models.CreateModelResponse:
        runtime = RuntimeOptions()
        return await self.create_model_with_options_async(request, runtime)

    def create_model_provider_with_options(
        self,
        tmp_req: main_models.CreateModelProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelProviderResponse:
        tmp_req.validate()
        request = main_models.CreateModelProviderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.api_keys):
            request.api_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.api_keys, 'ApiKeys', 'json')
        if not DaraCore.is_null(tmp_req.protocols):
            request.protocols_shrink = Utils.array_to_string_with_specified_style(tmp_req.protocols, 'Protocols', 'json')
        body = {}
        if not DaraCore.is_null(request.address):
            body['Address'] = request.address
        if not DaraCore.is_null(request.api_keys_shrink):
            body['ApiKeys'] = request.api_keys_shrink
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.protocols_shrink):
            body['Protocols'] = request.protocols_shrink
        if not DaraCore.is_null(request.provider):
            body['Provider'] = request.provider
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModelProvider',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_provider_with_options_async(
        self,
        tmp_req: main_models.CreateModelProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelProviderResponse:
        tmp_req.validate()
        request = main_models.CreateModelProviderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.api_keys):
            request.api_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.api_keys, 'ApiKeys', 'json')
        if not DaraCore.is_null(tmp_req.protocols):
            request.protocols_shrink = Utils.array_to_string_with_specified_style(tmp_req.protocols, 'Protocols', 'json')
        body = {}
        if not DaraCore.is_null(request.address):
            body['Address'] = request.address
        if not DaraCore.is_null(request.api_keys_shrink):
            body['ApiKeys'] = request.api_keys_shrink
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.protocols_shrink):
            body['Protocols'] = request.protocols_shrink
        if not DaraCore.is_null(request.provider):
            body['Provider'] = request.provider
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModelProvider',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model_provider(
        self,
        request: main_models.CreateModelProviderRequest,
    ) -> main_models.CreateModelProviderResponse:
        runtime = RuntimeOptions()
        return self.create_model_provider_with_options(request, runtime)

    async def create_model_provider_async(
        self,
        request: main_models.CreateModelProviderRequest,
    ) -> main_models.CreateModelProviderResponse:
        runtime = RuntimeOptions()
        return await self.create_model_provider_with_options_async(request, runtime)

    def create_service_endpoint_with_options(
        self,
        request: main_models.CreateServiceEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.component):
            query['Component'] = request.component
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceEndpoint',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_endpoint_with_options_async(
        self,
        request: main_models.CreateServiceEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.component):
            query['Component'] = request.component
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceEndpoint',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_endpoint(
        self,
        request: main_models.CreateServiceEndpointRequest,
    ) -> main_models.CreateServiceEndpointResponse:
        runtime = RuntimeOptions()
        return self.create_service_endpoint_with_options(request, runtime)

    async def create_service_endpoint_async(
        self,
        request: main_models.CreateServiceEndpointRequest,
    ) -> main_models.CreateServiceEndpointResponse:
        runtime = RuntimeOptions()
        return await self.create_service_endpoint_with_options_async(request, runtime)

    def create_team_with_options(
        self,
        tmp_req: main_models.CreateTeamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTeamResponse:
        tmp_req.validate()
        request = main_models.CreateTeamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.team_members):
            request.team_members_shrink = Utils.array_to_string_with_specified_style(tmp_req.team_members, 'TeamMembers', 'json')
        query = {}
        if not DaraCore.is_null(request.admin_name):
            query['AdminName'] = request.admin_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.team_members_shrink):
            query['TeamMembers'] = request.team_members_shrink
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTeam',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTeamResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_team_with_options_async(
        self,
        tmp_req: main_models.CreateTeamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTeamResponse:
        tmp_req.validate()
        request = main_models.CreateTeamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.team_members):
            request.team_members_shrink = Utils.array_to_string_with_specified_style(tmp_req.team_members, 'TeamMembers', 'json')
        query = {}
        if not DaraCore.is_null(request.admin_name):
            query['AdminName'] = request.admin_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.team_members_shrink):
            query['TeamMembers'] = request.team_members_shrink
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTeam',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTeamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_team(
        self,
        request: main_models.CreateTeamRequest,
    ) -> main_models.CreateTeamResponse:
        runtime = RuntimeOptions()
        return self.create_team_with_options(request, runtime)

    async def create_team_async(
        self,
        request: main_models.CreateTeamRequest,
    ) -> main_models.CreateTeamResponse:
        runtime = RuntimeOptions()
        return await self.create_team_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: main_models.CreateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_method):
            query['AuthMethod'] = request.auth_method
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2026-06-05',
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
        query = {}
        if not DaraCore.is_null(request.auth_method):
            query['AuthMethod'] = request.auth_method
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2026-06-05',
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

    def create_worker_with_options(
        self,
        tmp_req: main_models.CreateWorkerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkerResponse:
        tmp_req.validate()
        request = main_models.CreateWorkerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.channels):
            request.channels_shrink = Utils.array_to_string_with_specified_style(tmp_req.channels, 'Channels', 'json')
        if not DaraCore.is_null(tmp_req.credentials):
            request.credentials_shrink = Utils.array_to_string_with_specified_style(tmp_req.credentials, 'Credentials', 'json')
        if not DaraCore.is_null(tmp_req.groups):
            request.groups_shrink = Utils.array_to_string_with_specified_style(tmp_req.groups, 'Groups', 'json')
        if not DaraCore.is_null(tmp_req.limit_config):
            request.limit_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.limit_config, 'LimitConfig', 'json')
        if not DaraCore.is_null(tmp_req.mcp_servers):
            request.mcp_servers_shrink = Utils.array_to_string_with_specified_style(tmp_req.mcp_servers, 'McpServers', 'json')
        if not DaraCore.is_null(tmp_req.model):
            request.model_shrink = Utils.array_to_string_with_specified_style(tmp_req.model, 'Model', 'json')
        if not DaraCore.is_null(tmp_req.skills):
            request.skills_shrink = Utils.array_to_string_with_specified_style(tmp_req.skills, 'Skills', 'json')
        if not DaraCore.is_null(tmp_req.subagents):
            request.subagents_shrink = Utils.array_to_string_with_specified_style(tmp_req.subagents, 'Subagents', 'json')
        if not DaraCore.is_null(tmp_req.template):
            request.template_shrink = Utils.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_type):
            query['AgentType'] = request.agent_type
        if not DaraCore.is_null(request.agents):
            query['Agents'] = request.agents
        if not DaraCore.is_null(request.channels_shrink):
            query['Channels'] = request.channels_shrink
        if not DaraCore.is_null(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not DaraCore.is_null(request.groups_shrink):
            query['Groups'] = request.groups_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.limit_config_shrink):
            query['LimitConfig'] = request.limit_config_shrink
        if not DaraCore.is_null(request.mcp_servers_shrink):
            query['McpServers'] = request.mcp_servers_shrink
        if not DaraCore.is_null(request.model_shrink):
            query['Model'] = request.model_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.skills_shrink):
            query['Skills'] = request.skills_shrink
        if not DaraCore.is_null(request.soul):
            query['Soul'] = request.soul
        if not DaraCore.is_null(request.subagents_shrink):
            query['Subagents'] = request.subagents_shrink
        if not DaraCore.is_null(request.template_shrink):
            query['Template'] = request.template_shrink
        if not DaraCore.is_null(request.version_code):
            query['VersionCode'] = request.version_code
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.credentials_shrink):
            body['Credentials'] = request.credentials_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorker',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_worker_with_options_async(
        self,
        tmp_req: main_models.CreateWorkerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkerResponse:
        tmp_req.validate()
        request = main_models.CreateWorkerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.channels):
            request.channels_shrink = Utils.array_to_string_with_specified_style(tmp_req.channels, 'Channels', 'json')
        if not DaraCore.is_null(tmp_req.credentials):
            request.credentials_shrink = Utils.array_to_string_with_specified_style(tmp_req.credentials, 'Credentials', 'json')
        if not DaraCore.is_null(tmp_req.groups):
            request.groups_shrink = Utils.array_to_string_with_specified_style(tmp_req.groups, 'Groups', 'json')
        if not DaraCore.is_null(tmp_req.limit_config):
            request.limit_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.limit_config, 'LimitConfig', 'json')
        if not DaraCore.is_null(tmp_req.mcp_servers):
            request.mcp_servers_shrink = Utils.array_to_string_with_specified_style(tmp_req.mcp_servers, 'McpServers', 'json')
        if not DaraCore.is_null(tmp_req.model):
            request.model_shrink = Utils.array_to_string_with_specified_style(tmp_req.model, 'Model', 'json')
        if not DaraCore.is_null(tmp_req.skills):
            request.skills_shrink = Utils.array_to_string_with_specified_style(tmp_req.skills, 'Skills', 'json')
        if not DaraCore.is_null(tmp_req.subagents):
            request.subagents_shrink = Utils.array_to_string_with_specified_style(tmp_req.subagents, 'Subagents', 'json')
        if not DaraCore.is_null(tmp_req.template):
            request.template_shrink = Utils.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_type):
            query['AgentType'] = request.agent_type
        if not DaraCore.is_null(request.agents):
            query['Agents'] = request.agents
        if not DaraCore.is_null(request.channels_shrink):
            query['Channels'] = request.channels_shrink
        if not DaraCore.is_null(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not DaraCore.is_null(request.groups_shrink):
            query['Groups'] = request.groups_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.limit_config_shrink):
            query['LimitConfig'] = request.limit_config_shrink
        if not DaraCore.is_null(request.mcp_servers_shrink):
            query['McpServers'] = request.mcp_servers_shrink
        if not DaraCore.is_null(request.model_shrink):
            query['Model'] = request.model_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.skills_shrink):
            query['Skills'] = request.skills_shrink
        if not DaraCore.is_null(request.soul):
            query['Soul'] = request.soul
        if not DaraCore.is_null(request.subagents_shrink):
            query['Subagents'] = request.subagents_shrink
        if not DaraCore.is_null(request.template_shrink):
            query['Template'] = request.template_shrink
        if not DaraCore.is_null(request.version_code):
            query['VersionCode'] = request.version_code
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.credentials_shrink):
            body['Credentials'] = request.credentials_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorker',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_worker(
        self,
        request: main_models.CreateWorkerRequest,
    ) -> main_models.CreateWorkerResponse:
        runtime = RuntimeOptions()
        return self.create_worker_with_options(request, runtime)

    async def create_worker_async(
        self,
        request: main_models.CreateWorkerRequest,
    ) -> main_models.CreateWorkerResponse:
        runtime = RuntimeOptions()
        return await self.create_worker_with_options_async(request, runtime)

    def create_worker_bootstrap_token_with_options(
        self,
        request: main_models.CreateWorkerBootstrapTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkerBootstrapTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkerBootstrapToken',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkerBootstrapTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_worker_bootstrap_token_with_options_async(
        self,
        request: main_models.CreateWorkerBootstrapTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkerBootstrapTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkerBootstrapToken',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkerBootstrapTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_worker_bootstrap_token(
        self,
        request: main_models.CreateWorkerBootstrapTokenRequest,
    ) -> main_models.CreateWorkerBootstrapTokenResponse:
        runtime = RuntimeOptions()
        return self.create_worker_bootstrap_token_with_options(request, runtime)

    async def create_worker_bootstrap_token_async(
        self,
        request: main_models.CreateWorkerBootstrapTokenRequest,
    ) -> main_models.CreateWorkerBootstrapTokenResponse:
        runtime = RuntimeOptions()
        return await self.create_worker_bootstrap_token_with_options_async(request, runtime)

    def delete_credential_with_options(
        self,
        request: main_models.DeleteCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCredential',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_credential_with_options_async(
        self,
        request: main_models.DeleteCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCredential',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_credential(
        self,
        request: main_models.DeleteCredentialRequest,
    ) -> main_models.DeleteCredentialResponse:
        runtime = RuntimeOptions()
        return self.delete_credential_with_options(request, runtime)

    async def delete_credential_async(
        self,
        request: main_models.DeleteCredentialRequest,
    ) -> main_models.DeleteCredentialResponse:
        runtime = RuntimeOptions()
        return await self.delete_credential_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: main_models.DeleteInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: main_models.DeleteInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_mcp_with_options(
        self,
        request: main_models.DeleteMcpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcpResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMcp',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcpResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mcp_with_options_async(
        self,
        request: main_models.DeleteMcpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcpResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMcp',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mcp(
        self,
        request: main_models.DeleteMcpRequest,
    ) -> main_models.DeleteMcpResponse:
        runtime = RuntimeOptions()
        return self.delete_mcp_with_options(request, runtime)

    async def delete_mcp_async(
        self,
        request: main_models.DeleteMcpRequest,
    ) -> main_models.DeleteMcpResponse:
        runtime = RuntimeOptions()
        return await self.delete_mcp_with_options_async(request, runtime)

    def delete_model_with_options(
        self,
        request: main_models.DeleteModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.provider_id):
            body['ProviderId'] = request.provider_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteModel',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_with_options_async(
        self,
        request: main_models.DeleteModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.provider_id):
            body['ProviderId'] = request.provider_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteModel',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model(
        self,
        request: main_models.DeleteModelRequest,
    ) -> main_models.DeleteModelResponse:
        runtime = RuntimeOptions()
        return self.delete_model_with_options(request, runtime)

    async def delete_model_async(
        self,
        request: main_models.DeleteModelRequest,
    ) -> main_models.DeleteModelResponse:
        runtime = RuntimeOptions()
        return await self.delete_model_with_options_async(request, runtime)

    def delete_model_provider_with_options(
        self,
        request: main_models.DeleteModelProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteModelProvider',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_provider_with_options_async(
        self,
        request: main_models.DeleteModelProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteModelProvider',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model_provider(
        self,
        request: main_models.DeleteModelProviderRequest,
    ) -> main_models.DeleteModelProviderResponse:
        runtime = RuntimeOptions()
        return self.delete_model_provider_with_options(request, runtime)

    async def delete_model_provider_async(
        self,
        request: main_models.DeleteModelProviderRequest,
    ) -> main_models.DeleteModelProviderResponse:
        runtime = RuntimeOptions()
        return await self.delete_model_provider_with_options_async(request, runtime)

    def delete_service_endpoint_with_options(
        self,
        request: main_models.DeleteServiceEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceEndpoint',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_endpoint_with_options_async(
        self,
        request: main_models.DeleteServiceEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceEndpoint',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_endpoint(
        self,
        request: main_models.DeleteServiceEndpointRequest,
    ) -> main_models.DeleteServiceEndpointResponse:
        runtime = RuntimeOptions()
        return self.delete_service_endpoint_with_options(request, runtime)

    async def delete_service_endpoint_async(
        self,
        request: main_models.DeleteServiceEndpointRequest,
    ) -> main_models.DeleteServiceEndpointResponse:
        runtime = RuntimeOptions()
        return await self.delete_service_endpoint_with_options_async(request, runtime)

    def delete_team_with_options(
        self,
        request: main_models.DeleteTeamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTeamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTeam',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTeamResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_team_with_options_async(
        self,
        request: main_models.DeleteTeamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTeamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTeam',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTeamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_team(
        self,
        request: main_models.DeleteTeamRequest,
    ) -> main_models.DeleteTeamResponse:
        runtime = RuntimeOptions()
        return self.delete_team_with_options(request, runtime)

    async def delete_team_async(
        self,
        request: main_models.DeleteTeamRequest,
    ) -> main_models.DeleteTeamResponse:
        runtime = RuntimeOptions()
        return await self.delete_team_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: main_models.DeleteUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2026-06-05',
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
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2026-06-05',
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

    def delete_worker_with_options(
        self,
        request: main_models.DeleteWorkerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorker',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_worker_with_options_async(
        self,
        request: main_models.DeleteWorkerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorker',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_worker(
        self,
        request: main_models.DeleteWorkerRequest,
    ) -> main_models.DeleteWorkerResponse:
        runtime = RuntimeOptions()
        return self.delete_worker_with_options(request, runtime)

    async def delete_worker_async(
        self,
        request: main_models.DeleteWorkerRequest,
    ) -> main_models.DeleteWorkerResponse:
        runtime = RuntimeOptions()
        return await self.delete_worker_with_options_async(request, runtime)

    def get_credential_with_options(
        self,
        request: main_models.GetCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCredential',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_credential_with_options_async(
        self,
        request: main_models.GetCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCredential',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_credential(
        self,
        request: main_models.GetCredentialRequest,
    ) -> main_models.GetCredentialResponse:
        runtime = RuntimeOptions()
        return self.get_credential_with_options(request, runtime)

    async def get_credential_async(
        self,
        request: main_models.GetCredentialRequest,
    ) -> main_models.GetCredentialResponse:
        runtime = RuntimeOptions()
        return await self.get_credential_with_options_async(request, runtime)

    def get_identity_provider_with_options(
        self,
        request: main_models.GetIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_type):
            query['IdentityProviderType'] = request.identity_provider_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIdentityProvider',
            version = '2026-06-05',
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
        query = {}
        if not DaraCore.is_null(request.identity_provider_type):
            query['IdentityProviderType'] = request.identity_provider_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIdentityProvider',
            version = '2026-06-05',
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

    def get_instance_with_options(
        self,
        request: main_models.GetInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        request: main_models.GetInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        request: main_models.GetInstanceRequest,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    async def get_instance_async(
        self,
        request: main_models.GetInstanceRequest,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_with_options_async(request, runtime)

    def get_instance_async_task_with_options(
        self,
        request: main_models.GetInstanceAsyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_code):
            query['TaskCode'] = request.task_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceAsyncTask',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_async_task_with_options_async(
        self,
        request: main_models.GetInstanceAsyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_code):
            query['TaskCode'] = request.task_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceAsyncTask',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_async_task(
        self,
        request: main_models.GetInstanceAsyncTaskRequest,
    ) -> main_models.GetInstanceAsyncTaskResponse:
        runtime = RuntimeOptions()
        return self.get_instance_async_task_with_options(request, runtime)

    async def get_instance_async_task_async(
        self,
        request: main_models.GetInstanceAsyncTaskRequest,
    ) -> main_models.GetInstanceAsyncTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_async_task_with_options_async(request, runtime)

    def get_instance_oss_mount_ram_authorize_url_with_options(
        self,
        request: main_models.GetInstanceOssMountRamAuthorizeUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceOssMountRamAuthorizeUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceOssMountRamAuthorizeUrl',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceOssMountRamAuthorizeUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_oss_mount_ram_authorize_url_with_options_async(
        self,
        request: main_models.GetInstanceOssMountRamAuthorizeUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceOssMountRamAuthorizeUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceOssMountRamAuthorizeUrl',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceOssMountRamAuthorizeUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_oss_mount_ram_authorize_url(
        self,
        request: main_models.GetInstanceOssMountRamAuthorizeUrlRequest,
    ) -> main_models.GetInstanceOssMountRamAuthorizeUrlResponse:
        runtime = RuntimeOptions()
        return self.get_instance_oss_mount_ram_authorize_url_with_options(request, runtime)

    async def get_instance_oss_mount_ram_authorize_url_async(
        self,
        request: main_models.GetInstanceOssMountRamAuthorizeUrlRequest,
    ) -> main_models.GetInstanceOssMountRamAuthorizeUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_oss_mount_ram_authorize_url_with_options_async(request, runtime)

    def get_mcp_with_options(
        self,
        request: main_models.GetMcpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMcpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMcp',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMcpResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mcp_with_options_async(
        self,
        request: main_models.GetMcpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMcpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMcp',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMcpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mcp(
        self,
        request: main_models.GetMcpRequest,
    ) -> main_models.GetMcpResponse:
        runtime = RuntimeOptions()
        return self.get_mcp_with_options(request, runtime)

    async def get_mcp_async(
        self,
        request: main_models.GetMcpRequest,
    ) -> main_models.GetMcpResponse:
        runtime = RuntimeOptions()
        return await self.get_mcp_with_options_async(request, runtime)

    def get_model_invocation_summary_with_options(
        self,
        request: main_models.GetModelInvocationSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetModelInvocationSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetModelInvocationSummary',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelInvocationSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_invocation_summary_with_options_async(
        self,
        request: main_models.GetModelInvocationSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetModelInvocationSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetModelInvocationSummary',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelInvocationSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model_invocation_summary(
        self,
        request: main_models.GetModelInvocationSummaryRequest,
    ) -> main_models.GetModelInvocationSummaryResponse:
        runtime = RuntimeOptions()
        return self.get_model_invocation_summary_with_options(request, runtime)

    async def get_model_invocation_summary_async(
        self,
        request: main_models.GetModelInvocationSummaryRequest,
    ) -> main_models.GetModelInvocationSummaryResponse:
        runtime = RuntimeOptions()
        return await self.get_model_invocation_summary_with_options_async(request, runtime)

    def get_model_provider_with_options(
        self,
        request: main_models.GetModelProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetModelProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetModelProvider',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_provider_with_options_async(
        self,
        request: main_models.GetModelProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetModelProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetModelProvider',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model_provider(
        self,
        request: main_models.GetModelProviderRequest,
    ) -> main_models.GetModelProviderResponse:
        runtime = RuntimeOptions()
        return self.get_model_provider_with_options(request, runtime)

    async def get_model_provider_async(
        self,
        request: main_models.GetModelProviderRequest,
    ) -> main_models.GetModelProviderResponse:
        runtime = RuntimeOptions()
        return await self.get_model_provider_with_options_async(request, runtime)

    def get_nat_gateway_status_with_options(
        self,
        request: main_models.GetNatGatewayStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNatGatewayStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNatGatewayStatus',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNatGatewayStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_nat_gateway_status_with_options_async(
        self,
        request: main_models.GetNatGatewayStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNatGatewayStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNatGatewayStatus',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNatGatewayStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_nat_gateway_status(
        self,
        request: main_models.GetNatGatewayStatusRequest,
    ) -> main_models.GetNatGatewayStatusResponse:
        runtime = RuntimeOptions()
        return self.get_nat_gateway_status_with_options(request, runtime)

    async def get_nat_gateway_status_async(
        self,
        request: main_models.GetNatGatewayStatusRequest,
    ) -> main_models.GetNatGatewayStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_nat_gateway_status_with_options_async(request, runtime)

    def get_service_endpoint_with_options(
        self,
        request: main_models.GetServiceEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceEndpoint',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_endpoint_with_options_async(
        self,
        request: main_models.GetServiceEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceEndpoint',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_endpoint(
        self,
        request: main_models.GetServiceEndpointRequest,
    ) -> main_models.GetServiceEndpointResponse:
        runtime = RuntimeOptions()
        return self.get_service_endpoint_with_options(request, runtime)

    async def get_service_endpoint_async(
        self,
        request: main_models.GetServiceEndpointRequest,
    ) -> main_models.GetServiceEndpointResponse:
        runtime = RuntimeOptions()
        return await self.get_service_endpoint_with_options_async(request, runtime)

    def get_task_stats_summary_with_options(
        self,
        request: main_models.GetTaskStatsSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskStatsSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskStatsSummary',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskStatsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_stats_summary_with_options_async(
        self,
        request: main_models.GetTaskStatsSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskStatsSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskStatsSummary',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskStatsSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_stats_summary(
        self,
        request: main_models.GetTaskStatsSummaryRequest,
    ) -> main_models.GetTaskStatsSummaryResponse:
        runtime = RuntimeOptions()
        return self.get_task_stats_summary_with_options(request, runtime)

    async def get_task_stats_summary_async(
        self,
        request: main_models.GetTaskStatsSummaryRequest,
    ) -> main_models.GetTaskStatsSummaryResponse:
        runtime = RuntimeOptions()
        return await self.get_task_stats_summary_with_options_async(request, runtime)

    def get_team_with_options(
        self,
        request: main_models.GetTeamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTeamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTeam',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTeamResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_team_with_options_async(
        self,
        request: main_models.GetTeamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTeamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTeam',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTeamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_team(
        self,
        request: main_models.GetTeamRequest,
    ) -> main_models.GetTeamResponse:
        runtime = RuntimeOptions()
        return self.get_team_with_options(request, runtime)

    async def get_team_async(
        self,
        request: main_models.GetTeamRequest,
    ) -> main_models.GetTeamResponse:
        runtime = RuntimeOptions()
        return await self.get_team_with_options_async(request, runtime)

    def get_token_trend_with_options(
        self,
        request: main_models.GetTokenTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_by):
            query['GroupBy'] = request.group_by
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTokenTrend',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTokenTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_token_trend_with_options_async(
        self,
        request: main_models.GetTokenTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_by):
            query['GroupBy'] = request.group_by
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTokenTrend',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTokenTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_token_trend(
        self,
        request: main_models.GetTokenTrendRequest,
    ) -> main_models.GetTokenTrendResponse:
        runtime = RuntimeOptions()
        return self.get_token_trend_with_options(request, runtime)

    async def get_token_trend_async(
        self,
        request: main_models.GetTokenTrendRequest,
    ) -> main_models.GetTokenTrendResponse:
        runtime = RuntimeOptions()
        return await self.get_token_trend_with_options_async(request, runtime)

    def get_tool_call_distribution_with_options(
        self,
        request: main_models.GetToolCallDistributionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetToolCallDistributionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetToolCallDistribution',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetToolCallDistributionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tool_call_distribution_with_options_async(
        self,
        request: main_models.GetToolCallDistributionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetToolCallDistributionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetToolCallDistribution',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetToolCallDistributionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tool_call_distribution(
        self,
        request: main_models.GetToolCallDistributionRequest,
    ) -> main_models.GetToolCallDistributionResponse:
        runtime = RuntimeOptions()
        return self.get_tool_call_distribution_with_options(request, runtime)

    async def get_tool_call_distribution_async(
        self,
        request: main_models.GetToolCallDistributionRequest,
    ) -> main_models.GetToolCallDistributionResponse:
        runtime = RuntimeOptions()
        return await self.get_tool_call_distribution_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        request: main_models.GetUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2026-06-05',
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
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2026-06-05',
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

    def get_user_password_with_options(
        self,
        request: main_models.GetUserPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserPassword',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_password_with_options_async(
        self,
        request: main_models.GetUserPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserPassword',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_password(
        self,
        request: main_models.GetUserPasswordRequest,
    ) -> main_models.GetUserPasswordResponse:
        runtime = RuntimeOptions()
        return self.get_user_password_with_options(request, runtime)

    async def get_user_password_async(
        self,
        request: main_models.GetUserPasswordRequest,
    ) -> main_models.GetUserPasswordResponse:
        runtime = RuntimeOptions()
        return await self.get_user_password_with_options_async(request, runtime)

    def get_worker_with_options(
        self,
        request: main_models.GetWorkerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorker',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_worker_with_options_async(
        self,
        request: main_models.GetWorkerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorker',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_worker(
        self,
        request: main_models.GetWorkerRequest,
    ) -> main_models.GetWorkerResponse:
        runtime = RuntimeOptions()
        return self.get_worker_with_options(request, runtime)

    async def get_worker_async(
        self,
        request: main_models.GetWorkerRequest,
    ) -> main_models.GetWorkerResponse:
        runtime = RuntimeOptions()
        return await self.get_worker_with_options_async(request, runtime)

    def get_worker_bootstrap_options_with_options(
        self,
        request: main_models.GetWorkerBootstrapOptionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkerBootstrapOptionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkerBootstrapOptions',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkerBootstrapOptionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_worker_bootstrap_options_with_options_async(
        self,
        request: main_models.GetWorkerBootstrapOptionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkerBootstrapOptionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkerBootstrapOptions',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkerBootstrapOptionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_worker_bootstrap_options(
        self,
        request: main_models.GetWorkerBootstrapOptionsRequest,
    ) -> main_models.GetWorkerBootstrapOptionsResponse:
        runtime = RuntimeOptions()
        return self.get_worker_bootstrap_options_with_options(request, runtime)

    async def get_worker_bootstrap_options_async(
        self,
        request: main_models.GetWorkerBootstrapOptionsRequest,
    ) -> main_models.GetWorkerBootstrapOptionsResponse:
        runtime = RuntimeOptions()
        return await self.get_worker_bootstrap_options_with_options_async(request, runtime)

    def get_worker_max_version_with_options(
        self,
        request: main_models.GetWorkerMaxVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkerMaxVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkerMaxVersion',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkerMaxVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_worker_max_version_with_options_async(
        self,
        request: main_models.GetWorkerMaxVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkerMaxVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkerMaxVersion',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkerMaxVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_worker_max_version(
        self,
        request: main_models.GetWorkerMaxVersionRequest,
    ) -> main_models.GetWorkerMaxVersionResponse:
        runtime = RuntimeOptions()
        return self.get_worker_max_version_with_options(request, runtime)

    async def get_worker_max_version_async(
        self,
        request: main_models.GetWorkerMaxVersionRequest,
    ) -> main_models.GetWorkerMaxVersionResponse:
        runtime = RuntimeOptions()
        return await self.get_worker_max_version_with_options_async(request, runtime)

    def get_worker_stats_summary_with_options(
        self,
        request: main_models.GetWorkerStatsSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkerStatsSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkerStatsSummary',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkerStatsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_worker_stats_summary_with_options_async(
        self,
        request: main_models.GetWorkerStatsSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkerStatsSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkerStatsSummary',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkerStatsSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_worker_stats_summary(
        self,
        request: main_models.GetWorkerStatsSummaryRequest,
    ) -> main_models.GetWorkerStatsSummaryResponse:
        runtime = RuntimeOptions()
        return self.get_worker_stats_summary_with_options(request, runtime)

    async def get_worker_stats_summary_async(
        self,
        request: main_models.GetWorkerStatsSummaryRequest,
    ) -> main_models.GetWorkerStatsSummaryResponse:
        runtime = RuntimeOptions()
        return await self.get_worker_stats_summary_with_options_async(request, runtime)

    def list_credentials_with_options(
        self,
        request: main_models.ListCredentialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name_like):
            query['NameLike'] = request.name_like
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCredentials',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_credentials_with_options_async(
        self,
        request: main_models.ListCredentialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name_like):
            query['NameLike'] = request.name_like
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCredentials',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_credentials(
        self,
        request: main_models.ListCredentialsRequest,
    ) -> main_models.ListCredentialsResponse:
        runtime = RuntimeOptions()
        return self.list_credentials_with_options(request, runtime)

    async def list_credentials_async(
        self,
        request: main_models.ListCredentialsRequest,
    ) -> main_models.ListCredentialsResponse:
        runtime = RuntimeOptions()
        return await self.list_credentials_with_options_async(request, runtime)

    def list_identity_providers_with_options(
        self,
        request: main_models.ListIdentityProvidersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIdentityProvidersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIdentityProviders',
            version = '2026-06-05',
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
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIdentityProviders',
            version = '2026-06-05',
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

    def list_instances_with_options(
        self,
        request: main_models.ListInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.skip):
            query['Skip'] = request.skip
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: main_models.ListInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.skip):
            query['Skip'] = request.skip
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
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
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def list_mcp_tools_with_options(
        self,
        request: main_models.ListMcpToolsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcpToolsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMcpTools',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcpToolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcp_tools_with_options_async(
        self,
        request: main_models.ListMcpToolsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcpToolsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMcpTools',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcpToolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcp_tools(
        self,
        request: main_models.ListMcpToolsRequest,
    ) -> main_models.ListMcpToolsResponse:
        runtime = RuntimeOptions()
        return self.list_mcp_tools_with_options(request, runtime)

    async def list_mcp_tools_async(
        self,
        request: main_models.ListMcpToolsRequest,
    ) -> main_models.ListMcpToolsResponse:
        runtime = RuntimeOptions()
        return await self.list_mcp_tools_with_options_async(request, runtime)

    def list_mcps_with_options(
        self,
        request: main_models.ListMcpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMcps',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcps_with_options_async(
        self,
        request: main_models.ListMcpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMcps',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcps(
        self,
        request: main_models.ListMcpsRequest,
    ) -> main_models.ListMcpsResponse:
        runtime = RuntimeOptions()
        return self.list_mcps_with_options(request, runtime)

    async def list_mcps_async(
        self,
        request: main_models.ListMcpsRequest,
    ) -> main_models.ListMcpsResponse:
        runtime = RuntimeOptions()
        return await self.list_mcps_with_options_async(request, runtime)

    def list_model_providers_with_options(
        self,
        request: main_models.ListModelProvidersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListModelProvidersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelProviders',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_model_providers_with_options_async(
        self,
        request: main_models.ListModelProvidersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListModelProvidersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelProviders',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelProvidersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_model_providers(
        self,
        request: main_models.ListModelProvidersRequest,
    ) -> main_models.ListModelProvidersResponse:
        runtime = RuntimeOptions()
        return self.list_model_providers_with_options(request, runtime)

    async def list_model_providers_async(
        self,
        request: main_models.ListModelProvidersRequest,
    ) -> main_models.ListModelProvidersResponse:
        runtime = RuntimeOptions()
        return await self.list_model_providers_with_options_async(request, runtime)

    def list_models_with_options(
        self,
        request: main_models.ListModelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListModelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.provider_name):
            query['ProviderName'] = request.provider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModels',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_models_with_options_async(
        self,
        request: main_models.ListModelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListModelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.provider_name):
            query['ProviderName'] = request.provider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModels',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_models(
        self,
        request: main_models.ListModelsRequest,
    ) -> main_models.ListModelsResponse:
        runtime = RuntimeOptions()
        return self.list_models_with_options(request, runtime)

    async def list_models_async(
        self,
        request: main_models.ListModelsRequest,
    ) -> main_models.ListModelsResponse:
        runtime = RuntimeOptions()
        return await self.list_models_with_options_async(request, runtime)

    def list_service_endpoints_with_options(
        self,
        request: main_models.ListServiceEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.component):
            query['Component'] = request.component
        if not DaraCore.is_null(request.domain_type):
            query['DomainType'] = request.domain_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.skip):
            query['Skip'] = request.skip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceEndpoints',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_endpoints_with_options_async(
        self,
        request: main_models.ListServiceEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.component):
            query['Component'] = request.component
        if not DaraCore.is_null(request.domain_type):
            query['DomainType'] = request.domain_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.skip):
            query['Skip'] = request.skip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceEndpoints',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_endpoints(
        self,
        request: main_models.ListServiceEndpointsRequest,
    ) -> main_models.ListServiceEndpointsResponse:
        runtime = RuntimeOptions()
        return self.list_service_endpoints_with_options(request, runtime)

    async def list_service_endpoints_async(
        self,
        request: main_models.ListServiceEndpointsRequest,
    ) -> main_models.ListServiceEndpointsResponse:
        runtime = RuntimeOptions()
        return await self.list_service_endpoints_with_options_async(request, runtime)

    def list_ssl_certs_with_options(
        self,
        request: main_models.ListSslCertsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSslCertsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSslCerts',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSslCertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ssl_certs_with_options_async(
        self,
        request: main_models.ListSslCertsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSslCertsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSslCerts',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSslCertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ssl_certs(
        self,
        request: main_models.ListSslCertsRequest,
    ) -> main_models.ListSslCertsResponse:
        runtime = RuntimeOptions()
        return self.list_ssl_certs_with_options(request, runtime)

    async def list_ssl_certs_async(
        self,
        request: main_models.ListSslCertsRequest,
    ) -> main_models.ListSslCertsResponse:
        runtime = RuntimeOptions()
        return await self.list_ssl_certs_with_options_async(request, runtime)

    def list_team_details_with_options(
        self,
        request: main_models.ListTeamDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTeamDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTeamDetails',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTeamDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_team_details_with_options_async(
        self,
        request: main_models.ListTeamDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTeamDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTeamDetails',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTeamDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_team_details(
        self,
        request: main_models.ListTeamDetailsRequest,
    ) -> main_models.ListTeamDetailsResponse:
        runtime = RuntimeOptions()
        return self.list_team_details_with_options(request, runtime)

    async def list_team_details_async(
        self,
        request: main_models.ListTeamDetailsRequest,
    ) -> main_models.ListTeamDetailsResponse:
        runtime = RuntimeOptions()
        return await self.list_team_details_with_options_async(request, runtime)

    def list_team_tasks_with_options(
        self,
        request: main_models.ListTeamTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTeamTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.team):
            query['Team'] = request.team
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTeamTasks',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTeamTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_team_tasks_with_options_async(
        self,
        request: main_models.ListTeamTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTeamTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.team):
            query['Team'] = request.team
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTeamTasks',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTeamTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_team_tasks(
        self,
        request: main_models.ListTeamTasksRequest,
    ) -> main_models.ListTeamTasksResponse:
        runtime = RuntimeOptions()
        return self.list_team_tasks_with_options(request, runtime)

    async def list_team_tasks_async(
        self,
        request: main_models.ListTeamTasksRequest,
    ) -> main_models.ListTeamTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_team_tasks_with_options_async(request, runtime)

    def list_teams_with_options(
        self,
        request: main_models.ListTeamsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTeamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name_like):
            query['NameLike'] = request.name_like
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTeams',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTeamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_teams_with_options_async(
        self,
        request: main_models.ListTeamsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTeamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name_like):
            query['NameLike'] = request.name_like
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTeams',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTeamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_teams(
        self,
        request: main_models.ListTeamsRequest,
    ) -> main_models.ListTeamsResponse:
        runtime = RuntimeOptions()
        return self.list_teams_with_options(request, runtime)

    async def list_teams_async(
        self,
        request: main_models.ListTeamsRequest,
    ) -> main_models.ListTeamsResponse:
        runtime = RuntimeOptions()
        return await self.list_teams_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: main_models.ListUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name_like):
            query['NameLike'] = request.name_like
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2026-06-05',
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
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name_like):
            query['NameLike'] = request.name_like
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2026-06-05',
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

    def list_worker_stats_details_with_options(
        self,
        request: main_models.ListWorkerStatsDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkerStatsDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkerStatsDetails',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkerStatsDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_worker_stats_details_with_options_async(
        self,
        request: main_models.ListWorkerStatsDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkerStatsDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkerStatsDetails',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkerStatsDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_worker_stats_details(
        self,
        request: main_models.ListWorkerStatsDetailsRequest,
    ) -> main_models.ListWorkerStatsDetailsResponse:
        runtime = RuntimeOptions()
        return self.list_worker_stats_details_with_options(request, runtime)

    async def list_worker_stats_details_async(
        self,
        request: main_models.ListWorkerStatsDetailsRequest,
    ) -> main_models.ListWorkerStatsDetailsResponse:
        runtime = RuntimeOptions()
        return await self.list_worker_stats_details_with_options_async(request, runtime)

    def list_workers_with_options(
        self,
        tmp_req: main_models.ListWorkersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkersResponse:
        tmp_req.validate()
        request = main_models.ListWorkersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.group):
            request.group_shrink = Utils.array_to_string_with_specified_style(tmp_req.group, 'Group', 'json')
        if not DaraCore.is_null(tmp_req.template):
            request.template_shrink = Utils.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_type):
            query['AgentType'] = request.agent_type
        if not DaraCore.is_null(request.credential):
            query['Credential'] = request.credential
        if not DaraCore.is_null(request.group_shrink):
            query['Group'] = request.group_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.mcp):
            query['Mcp'] = request.mcp
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.model_provider):
            query['ModelProvider'] = request.model_provider
        if not DaraCore.is_null(request.name_like):
            query['NameLike'] = request.name_like
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.template_shrink):
            query['Template'] = request.template_shrink
        if not DaraCore.is_null(request.version_code):
            query['VersionCode'] = request.version_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkers',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workers_with_options_async(
        self,
        tmp_req: main_models.ListWorkersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkersResponse:
        tmp_req.validate()
        request = main_models.ListWorkersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.group):
            request.group_shrink = Utils.array_to_string_with_specified_style(tmp_req.group, 'Group', 'json')
        if not DaraCore.is_null(tmp_req.template):
            request.template_shrink = Utils.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_type):
            query['AgentType'] = request.agent_type
        if not DaraCore.is_null(request.credential):
            query['Credential'] = request.credential
        if not DaraCore.is_null(request.group_shrink):
            query['Group'] = request.group_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.mcp):
            query['Mcp'] = request.mcp
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.model_provider):
            query['ModelProvider'] = request.model_provider
        if not DaraCore.is_null(request.name_like):
            query['NameLike'] = request.name_like
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.template_shrink):
            query['Template'] = request.template_shrink
        if not DaraCore.is_null(request.version_code):
            query['VersionCode'] = request.version_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkers',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workers(
        self,
        request: main_models.ListWorkersRequest,
    ) -> main_models.ListWorkersResponse:
        runtime = RuntimeOptions()
        return self.list_workers_with_options(request, runtime)

    async def list_workers_async(
        self,
        request: main_models.ListWorkersRequest,
    ) -> main_models.ListWorkersResponse:
        runtime = RuntimeOptions()
        return await self.list_workers_with_options_async(request, runtime)

    def put_cms_workspace_with_options(
        self,
        request: main_models.PutCmsWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutCmsWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutCmsWorkspace',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutCmsWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_cms_workspace_with_options_async(
        self,
        request: main_models.PutCmsWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutCmsWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutCmsWorkspace',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutCmsWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_cms_workspace(
        self,
        request: main_models.PutCmsWorkspaceRequest,
    ) -> main_models.PutCmsWorkspaceResponse:
        runtime = RuntimeOptions()
        return self.put_cms_workspace_with_options(request, runtime)

    async def put_cms_workspace_async(
        self,
        request: main_models.PutCmsWorkspaceRequest,
    ) -> main_models.PutCmsWorkspaceResponse:
        runtime = RuntimeOptions()
        return await self.put_cms_workspace_with_options_async(request, runtime)

    def query_features_with_options(
        self,
        request: main_models.QueryFeaturesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFeaturesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.target_scope):
            query['TargetScope'] = request.target_scope
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFeatures',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFeaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_features_with_options_async(
        self,
        request: main_models.QueryFeaturesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFeaturesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.target_scope):
            query['TargetScope'] = request.target_scope
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFeatures',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFeaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_features(
        self,
        request: main_models.QueryFeaturesRequest,
    ) -> main_models.QueryFeaturesResponse:
        runtime = RuntimeOptions()
        return self.query_features_with_options(request, runtime)

    async def query_features_async(
        self,
        request: main_models.QueryFeaturesRequest,
    ) -> main_models.QueryFeaturesResponse:
        runtime = RuntimeOptions()
        return await self.query_features_with_options_async(request, runtime)

    def query_supported_zones_with_options(
        self,
        request: main_models.QuerySupportedZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySupportedZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySupportedZones',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySupportedZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_supported_zones_with_options_async(
        self,
        request: main_models.QuerySupportedZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySupportedZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySupportedZones',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySupportedZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_supported_zones(
        self,
        request: main_models.QuerySupportedZonesRequest,
    ) -> main_models.QuerySupportedZonesResponse:
        runtime = RuntimeOptions()
        return self.query_supported_zones_with_options(request, runtime)

    async def query_supported_zones_async(
        self,
        request: main_models.QuerySupportedZonesRequest,
    ) -> main_models.QuerySupportedZonesResponse:
        runtime = RuntimeOptions()
        return await self.query_supported_zones_with_options_async(request, runtime)

    def reset_user_password_with_options(
        self,
        request: main_models.ResetUserPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetUserPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetUserPassword',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_user_password_with_options_async(
        self,
        request: main_models.ResetUserPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetUserPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetUserPassword',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_user_password(
        self,
        request: main_models.ResetUserPasswordRequest,
    ) -> main_models.ResetUserPasswordResponse:
        runtime = RuntimeOptions()
        return self.reset_user_password_with_options(request, runtime)

    async def reset_user_password_async(
        self,
        request: main_models.ResetUserPasswordRequest,
    ) -> main_models.ResetUserPasswordResponse:
        runtime = RuntimeOptions()
        return await self.reset_user_password_with_options_async(request, runtime)

    def test_model_provider_with_options(
        self,
        request: main_models.TestModelProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TestModelProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.provider_id):
            body['ProviderId'] = request.provider_id
        if not DaraCore.is_null(request.provider_name):
            body['ProviderName'] = request.provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TestModelProvider',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TestModelProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def test_model_provider_with_options_async(
        self,
        request: main_models.TestModelProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TestModelProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.provider_id):
            body['ProviderId'] = request.provider_id
        if not DaraCore.is_null(request.provider_name):
            body['ProviderName'] = request.provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TestModelProvider',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TestModelProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def test_model_provider(
        self,
        request: main_models.TestModelProviderRequest,
    ) -> main_models.TestModelProviderResponse:
        runtime = RuntimeOptions()
        return self.test_model_provider_with_options(request, runtime)

    async def test_model_provider_async(
        self,
        request: main_models.TestModelProviderRequest,
    ) -> main_models.TestModelProviderResponse:
        runtime = RuntimeOptions()
        return await self.test_model_provider_with_options_async(request, runtime)

    def unbind_identity_provider_with_options(
        self,
        request: main_models.UnbindIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_type):
            query['IdentityProviderType'] = request.identity_provider_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindIdentityProvider',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_identity_provider_with_options_async(
        self,
        request: main_models.UnbindIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_type):
            query['IdentityProviderType'] = request.identity_provider_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindIdentityProvider',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_identity_provider(
        self,
        request: main_models.UnbindIdentityProviderRequest,
    ) -> main_models.UnbindIdentityProviderResponse:
        runtime = RuntimeOptions()
        return self.unbind_identity_provider_with_options(request, runtime)

    async def unbind_identity_provider_async(
        self,
        request: main_models.UnbindIdentityProviderRequest,
    ) -> main_models.UnbindIdentityProviderResponse:
        runtime = RuntimeOptions()
        return await self.unbind_identity_provider_with_options_async(request, runtime)

    def update_credential_with_options(
        self,
        request: main_models.UpdateCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['ApiKey'] = request.api_key
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCredential',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_credential_with_options_async(
        self,
        request: main_models.UpdateCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['ApiKey'] = request.api_key
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCredential',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_credential(
        self,
        request: main_models.UpdateCredentialRequest,
    ) -> main_models.UpdateCredentialResponse:
        runtime = RuntimeOptions()
        return self.update_credential_with_options(request, runtime)

    async def update_credential_async(
        self,
        request: main_models.UpdateCredentialRequest,
    ) -> main_models.UpdateCredentialResponse:
        runtime = RuntimeOptions()
        return await self.update_credential_with_options_async(request, runtime)

    def update_identity_provider_with_options(
        self,
        request: main_models.UpdateIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_type):
            query['IdentityProviderType'] = request.identity_provider_type
        if not DaraCore.is_null(request.idp_metadata):
            query['IdpMetadata'] = request.idp_metadata
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.login_enabled):
            query['LoginEnabled'] = request.login_enabled
        if not DaraCore.is_null(request.sync_enabled):
            query['SyncEnabled'] = request.sync_enabled
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIdentityProvider',
            version = '2026-06-05',
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
        request: main_models.UpdateIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_type):
            query['IdentityProviderType'] = request.identity_provider_type
        if not DaraCore.is_null(request.idp_metadata):
            query['IdpMetadata'] = request.idp_metadata
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.login_enabled):
            query['LoginEnabled'] = request.login_enabled
        if not DaraCore.is_null(request.sync_enabled):
            query['SyncEnabled'] = request.sync_enabled
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIdentityProvider',
            version = '2026-06-05',
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

    def update_instance_with_options(
        self,
        tmp_req: main_models.UpdateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        tmp_req.validate()
        request = main_models.UpdateInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.zones):
            request.zones_shrink = Utils.array_to_string_with_specified_style(tmp_req.zones, 'Zones', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.zones_shrink):
            query['Zones'] = request.zones_shrink
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        tmp_req: main_models.UpdateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        tmp_req.validate()
        request = main_models.UpdateInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.zones):
            request.zones_shrink = Utils.array_to_string_with_specified_style(tmp_req.zones, 'Zones', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.zones_shrink):
            query['Zones'] = request.zones_shrink
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance(
        self,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        return self.update_instance_with_options(request, runtime)

    async def update_instance_async(
        self,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        return await self.update_instance_with_options_async(request, runtime)

    def update_instance_async_task_with_options(
        self,
        request: main_models.UpdateInstanceAsyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_resume):
            query['IsResume'] = request.is_resume
        if not DaraCore.is_null(request.task_code):
            query['TaskCode'] = request.task_code
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceAsyncTask',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_async_task_with_options_async(
        self,
        request: main_models.UpdateInstanceAsyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_resume):
            query['IsResume'] = request.is_resume
        if not DaraCore.is_null(request.task_code):
            query['TaskCode'] = request.task_code
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceAsyncTask',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_async_task(
        self,
        request: main_models.UpdateInstanceAsyncTaskRequest,
    ) -> main_models.UpdateInstanceAsyncTaskResponse:
        runtime = RuntimeOptions()
        return self.update_instance_async_task_with_options(request, runtime)

    async def update_instance_async_task_async(
        self,
        request: main_models.UpdateInstanceAsyncTaskRequest,
    ) -> main_models.UpdateInstanceAsyncTaskResponse:
        runtime = RuntimeOptions()
        return await self.update_instance_async_task_with_options_async(request, runtime)

    def update_mcp_with_options(
        self,
        tmp_req: main_models.UpdateMcpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMcpResponse:
        tmp_req.validate()
        request = main_models.UpdateMcpShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.addresses):
            request.addresses_shrink = Utils.array_to_string_with_specified_style(tmp_req.addresses, 'Addresses', 'json')
        body = {}
        if not DaraCore.is_null(request.addresses_shrink):
            body['Addresses'] = request.addresses_shrink
        if not DaraCore.is_null(request.auth_config):
            body['AuthConfig'] = request.auth_config
        if not DaraCore.is_null(request.auth_enabled):
            body['AuthEnabled'] = request.auth_enabled
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.create_type):
            body['CreateType'] = request.create_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.swagger_config):
            body['SwaggerConfig'] = request.swagger_config
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMcp',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMcpResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mcp_with_options_async(
        self,
        tmp_req: main_models.UpdateMcpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMcpResponse:
        tmp_req.validate()
        request = main_models.UpdateMcpShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.addresses):
            request.addresses_shrink = Utils.array_to_string_with_specified_style(tmp_req.addresses, 'Addresses', 'json')
        body = {}
        if not DaraCore.is_null(request.addresses_shrink):
            body['Addresses'] = request.addresses_shrink
        if not DaraCore.is_null(request.auth_config):
            body['AuthConfig'] = request.auth_config
        if not DaraCore.is_null(request.auth_enabled):
            body['AuthEnabled'] = request.auth_enabled
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.create_type):
            body['CreateType'] = request.create_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.swagger_config):
            body['SwaggerConfig'] = request.swagger_config
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMcp',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMcpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mcp(
        self,
        request: main_models.UpdateMcpRequest,
    ) -> main_models.UpdateMcpResponse:
        runtime = RuntimeOptions()
        return self.update_mcp_with_options(request, runtime)

    async def update_mcp_async(
        self,
        request: main_models.UpdateMcpRequest,
    ) -> main_models.UpdateMcpResponse:
        runtime = RuntimeOptions()
        return await self.update_mcp_with_options_async(request, runtime)

    def update_model_with_options(
        self,
        request: main_models.UpdateModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModel',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_model_with_options_async(
        self,
        request: main_models.UpdateModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModel',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_model(
        self,
        request: main_models.UpdateModelRequest,
    ) -> main_models.UpdateModelResponse:
        runtime = RuntimeOptions()
        return self.update_model_with_options(request, runtime)

    async def update_model_async(
        self,
        request: main_models.UpdateModelRequest,
    ) -> main_models.UpdateModelResponse:
        runtime = RuntimeOptions()
        return await self.update_model_with_options_async(request, runtime)

    def update_model_provider_with_options(
        self,
        tmp_req: main_models.UpdateModelProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelProviderResponse:
        tmp_req.validate()
        request = main_models.UpdateModelProviderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.api_keys):
            request.api_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.api_keys, 'ApiKeys', 'json')
        if not DaraCore.is_null(tmp_req.protocols):
            request.protocols_shrink = Utils.array_to_string_with_specified_style(tmp_req.protocols, 'Protocols', 'json')
        body = {}
        if not DaraCore.is_null(request.address):
            body['Address'] = request.address
        if not DaraCore.is_null(request.api_keys_shrink):
            body['ApiKeys'] = request.api_keys_shrink
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.protocols_shrink):
            body['Protocols'] = request.protocols_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModelProvider',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_model_provider_with_options_async(
        self,
        tmp_req: main_models.UpdateModelProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelProviderResponse:
        tmp_req.validate()
        request = main_models.UpdateModelProviderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.api_keys):
            request.api_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.api_keys, 'ApiKeys', 'json')
        if not DaraCore.is_null(tmp_req.protocols):
            request.protocols_shrink = Utils.array_to_string_with_specified_style(tmp_req.protocols, 'Protocols', 'json')
        body = {}
        if not DaraCore.is_null(request.address):
            body['Address'] = request.address
        if not DaraCore.is_null(request.api_keys_shrink):
            body['ApiKeys'] = request.api_keys_shrink
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.protocols_shrink):
            body['Protocols'] = request.protocols_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModelProvider',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_model_provider(
        self,
        request: main_models.UpdateModelProviderRequest,
    ) -> main_models.UpdateModelProviderResponse:
        runtime = RuntimeOptions()
        return self.update_model_provider_with_options(request, runtime)

    async def update_model_provider_async(
        self,
        request: main_models.UpdateModelProviderRequest,
    ) -> main_models.UpdateModelProviderResponse:
        runtime = RuntimeOptions()
        return await self.update_model_provider_with_options_async(request, runtime)

    def update_service_endpoint_with_options(
        self,
        request: main_models.UpdateServiceEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceEndpoint',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_endpoint_with_options_async(
        self,
        request: main_models.UpdateServiceEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceEndpoint',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_endpoint(
        self,
        request: main_models.UpdateServiceEndpointRequest,
    ) -> main_models.UpdateServiceEndpointResponse:
        runtime = RuntimeOptions()
        return self.update_service_endpoint_with_options(request, runtime)

    async def update_service_endpoint_async(
        self,
        request: main_models.UpdateServiceEndpointRequest,
    ) -> main_models.UpdateServiceEndpointResponse:
        runtime = RuntimeOptions()
        return await self.update_service_endpoint_with_options_async(request, runtime)

    def update_team_with_options(
        self,
        tmp_req: main_models.UpdateTeamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTeamResponse:
        tmp_req.validate()
        request = main_models.UpdateTeamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.team_members):
            request.team_members_shrink = Utils.array_to_string_with_specified_style(tmp_req.team_members, 'TeamMembers', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.team_members_shrink):
            query['TeamMembers'] = request.team_members_shrink
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTeam',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTeamResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_team_with_options_async(
        self,
        tmp_req: main_models.UpdateTeamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTeamResponse:
        tmp_req.validate()
        request = main_models.UpdateTeamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.team_members):
            request.team_members_shrink = Utils.array_to_string_with_specified_style(tmp_req.team_members, 'TeamMembers', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.team_members_shrink):
            query['TeamMembers'] = request.team_members_shrink
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTeam',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTeamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_team(
        self,
        request: main_models.UpdateTeamRequest,
    ) -> main_models.UpdateTeamResponse:
        runtime = RuntimeOptions()
        return self.update_team_with_options(request, runtime)

    async def update_team_async(
        self,
        request: main_models.UpdateTeamRequest,
    ) -> main_models.UpdateTeamResponse:
        runtime = RuntimeOptions()
        return await self.update_team_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: main_models.UpdateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_method):
            query['AuthMethod'] = request.auth_method
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2026-06-05',
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
        query = {}
        if not DaraCore.is_null(request.auth_method):
            query['AuthMethod'] = request.auth_method
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2026-06-05',
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

    def update_worker_with_options(
        self,
        tmp_req: main_models.UpdateWorkerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkerResponse:
        tmp_req.validate()
        request = main_models.UpdateWorkerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.channels):
            request.channels_shrink = Utils.array_to_string_with_specified_style(tmp_req.channels, 'Channels', 'json')
        if not DaraCore.is_null(tmp_req.credentials):
            request.credentials_shrink = Utils.array_to_string_with_specified_style(tmp_req.credentials, 'Credentials', 'json')
        if not DaraCore.is_null(tmp_req.limit_config):
            request.limit_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.limit_config, 'LimitConfig', 'json')
        if not DaraCore.is_null(tmp_req.mcp_servers):
            request.mcp_servers_shrink = Utils.array_to_string_with_specified_style(tmp_req.mcp_servers, 'McpServers', 'json')
        if not DaraCore.is_null(tmp_req.model):
            request.model_shrink = Utils.array_to_string_with_specified_style(tmp_req.model, 'Model', 'json')
        if not DaraCore.is_null(tmp_req.skills):
            request.skills_shrink = Utils.array_to_string_with_specified_style(tmp_req.skills, 'Skills', 'json')
        if not DaraCore.is_null(tmp_req.template):
            request.template_shrink = Utils.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not DaraCore.is_null(request.agents):
            query['Agents'] = request.agents
        if not DaraCore.is_null(request.channels_shrink):
            query['Channels'] = request.channels_shrink
        if not DaraCore.is_null(request.credentials_shrink):
            query['Credentials'] = request.credentials_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.limit_config_shrink):
            query['LimitConfig'] = request.limit_config_shrink
        if not DaraCore.is_null(request.mcp_servers_shrink):
            query['McpServers'] = request.mcp_servers_shrink
        if not DaraCore.is_null(request.model_shrink):
            query['Model'] = request.model_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.skills_shrink):
            query['Skills'] = request.skills_shrink
        if not DaraCore.is_null(request.soul):
            query['Soul'] = request.soul
        if not DaraCore.is_null(request.template_shrink):
            query['Template'] = request.template_shrink
        if not DaraCore.is_null(request.version_code):
            query['VersionCode'] = request.version_code
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorker',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_worker_with_options_async(
        self,
        tmp_req: main_models.UpdateWorkerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkerResponse:
        tmp_req.validate()
        request = main_models.UpdateWorkerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.channels):
            request.channels_shrink = Utils.array_to_string_with_specified_style(tmp_req.channels, 'Channels', 'json')
        if not DaraCore.is_null(tmp_req.credentials):
            request.credentials_shrink = Utils.array_to_string_with_specified_style(tmp_req.credentials, 'Credentials', 'json')
        if not DaraCore.is_null(tmp_req.limit_config):
            request.limit_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.limit_config, 'LimitConfig', 'json')
        if not DaraCore.is_null(tmp_req.mcp_servers):
            request.mcp_servers_shrink = Utils.array_to_string_with_specified_style(tmp_req.mcp_servers, 'McpServers', 'json')
        if not DaraCore.is_null(tmp_req.model):
            request.model_shrink = Utils.array_to_string_with_specified_style(tmp_req.model, 'Model', 'json')
        if not DaraCore.is_null(tmp_req.skills):
            request.skills_shrink = Utils.array_to_string_with_specified_style(tmp_req.skills, 'Skills', 'json')
        if not DaraCore.is_null(tmp_req.template):
            request.template_shrink = Utils.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not DaraCore.is_null(request.agents):
            query['Agents'] = request.agents
        if not DaraCore.is_null(request.channels_shrink):
            query['Channels'] = request.channels_shrink
        if not DaraCore.is_null(request.credentials_shrink):
            query['Credentials'] = request.credentials_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.limit_config_shrink):
            query['LimitConfig'] = request.limit_config_shrink
        if not DaraCore.is_null(request.mcp_servers_shrink):
            query['McpServers'] = request.mcp_servers_shrink
        if not DaraCore.is_null(request.model_shrink):
            query['Model'] = request.model_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.skills_shrink):
            query['Skills'] = request.skills_shrink
        if not DaraCore.is_null(request.soul):
            query['Soul'] = request.soul
        if not DaraCore.is_null(request.template_shrink):
            query['Template'] = request.template_shrink
        if not DaraCore.is_null(request.version_code):
            query['VersionCode'] = request.version_code
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorker',
            version = '2026-06-05',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_worker(
        self,
        request: main_models.UpdateWorkerRequest,
    ) -> main_models.UpdateWorkerResponse:
        runtime = RuntimeOptions()
        return self.update_worker_with_options(request, runtime)

    async def update_worker_async(
        self,
        request: main_models.UpdateWorkerRequest,
    ) -> main_models.UpdateWorkerResponse:
        runtime = RuntimeOptions()
        return await self.update_worker_with_options_async(request, runtime)
