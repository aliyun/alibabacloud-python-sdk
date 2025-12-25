# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_apig20240327 import models as main_models
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
        self._endpoint = self.get_endpoint('apig', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_gateway_security_group_rule_with_options(
        self,
        gateway_id: str,
        request: main_models.AddGatewaySecurityGroupRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddGatewaySecurityGroupRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.port_ranges):
            body['portRanges'] = request.port_ranges
        if not DaraCore.is_null(request.security_group_id):
            body['securityGroupId'] = request.security_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddGatewaySecurityGroupRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/security-group-rules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGatewaySecurityGroupRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_gateway_security_group_rule_with_options_async(
        self,
        gateway_id: str,
        request: main_models.AddGatewaySecurityGroupRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddGatewaySecurityGroupRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.port_ranges):
            body['portRanges'] = request.port_ranges
        if not DaraCore.is_null(request.security_group_id):
            body['securityGroupId'] = request.security_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddGatewaySecurityGroupRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/security-group-rules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGatewaySecurityGroupRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_gateway_security_group_rule(
        self,
        gateway_id: str,
        request: main_models.AddGatewaySecurityGroupRuleRequest,
    ) -> main_models.AddGatewaySecurityGroupRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_gateway_security_group_rule_with_options(gateway_id, request, headers, runtime)

    async def add_gateway_security_group_rule_async(
        self,
        gateway_id: str,
        request: main_models.AddGatewaySecurityGroupRuleRequest,
    ) -> main_models.AddGatewaySecurityGroupRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_gateway_security_group_rule_with_options_async(gateway_id, request, headers, runtime)

    def batch_delete_consumer_authorization_rule_with_options(
        self,
        request: main_models.BatchDeleteConsumerAuthorizationRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteConsumerAuthorizationRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_authorization_rule_ids):
            query['consumerAuthorizationRuleIds'] = request.consumer_authorization_rule_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/authorization-rules',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteConsumerAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_consumer_authorization_rule_with_options_async(
        self,
        request: main_models.BatchDeleteConsumerAuthorizationRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteConsumerAuthorizationRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_authorization_rule_ids):
            query['consumerAuthorizationRuleIds'] = request.consumer_authorization_rule_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/authorization-rules',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteConsumerAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_consumer_authorization_rule(
        self,
        request: main_models.BatchDeleteConsumerAuthorizationRuleRequest,
    ) -> main_models.BatchDeleteConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_delete_consumer_authorization_rule_with_options(request, headers, runtime)

    async def batch_delete_consumer_authorization_rule_async(
        self,
        request: main_models.BatchDeleteConsumerAuthorizationRuleRequest,
    ) -> main_models.BatchDeleteConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_delete_consumer_authorization_rule_with_options_async(request, headers, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/move-resource-group',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/move-resource-group',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.change_resource_group_with_options(request, headers, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.change_resource_group_with_options_async(request, headers, runtime)

    def create_and_attach_policy_with_options(
        self,
        request: main_models.CreateAndAttachPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAndAttachPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not DaraCore.is_null(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.class_name):
            body['className'] = request.class_name
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAndAttachPolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policies',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAndAttachPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_and_attach_policy_with_options_async(
        self,
        request: main_models.CreateAndAttachPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAndAttachPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not DaraCore.is_null(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.class_name):
            body['className'] = request.class_name
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAndAttachPolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policies',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAndAttachPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_and_attach_policy(
        self,
        request: main_models.CreateAndAttachPolicyRequest,
    ) -> main_models.CreateAndAttachPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_and_attach_policy_with_options(request, headers, runtime)

    async def create_and_attach_policy_async(
        self,
        request: main_models.CreateAndAttachPolicyRequest,
    ) -> main_models.CreateAndAttachPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_and_attach_policy_with_options_async(request, headers, runtime)

    def create_consumer_with_options(
        self,
        request: main_models.CreateConsumerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ak_sk_identity_configs):
            body['akSkIdentityConfigs'] = request.ak_sk_identity_configs
        if not DaraCore.is_null(request.apikey_identity_config):
            body['apikeyIdentityConfig'] = request.apikey_identity_config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.jwt_identity_config):
            body['jwtIdentityConfig'] = request.jwt_identity_config
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConsumerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_consumer_with_options_async(
        self,
        request: main_models.CreateConsumerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ak_sk_identity_configs):
            body['akSkIdentityConfigs'] = request.ak_sk_identity_configs
        if not DaraCore.is_null(request.apikey_identity_config):
            body['apikeyIdentityConfig'] = request.apikey_identity_config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.jwt_identity_config):
            body['jwtIdentityConfig'] = request.jwt_identity_config
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConsumerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_consumer(
        self,
        request: main_models.CreateConsumerRequest,
    ) -> main_models.CreateConsumerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_consumer_with_options(request, headers, runtime)

    async def create_consumer_async(
        self,
        request: main_models.CreateConsumerRequest,
    ) -> main_models.CreateConsumerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_consumer_with_options_async(request, headers, runtime)

    def create_consumer_authorization_rule_with_options(
        self,
        consumer_id: str,
        request: main_models.CreateConsumerAuthorizationRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerAuthorizationRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.authorization_resource_infos):
            body['authorizationResourceInfos'] = request.authorization_resource_infos
        if not DaraCore.is_null(request.expire_mode):
            body['expireMode'] = request.expire_mode
        if not DaraCore.is_null(request.expire_timestamp):
            body['expireTimestamp'] = request.expire_timestamp
        if not DaraCore.is_null(request.parent_resource_type):
            body['parentResourceType'] = request.parent_resource_type
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}/authorization-rules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConsumerAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_consumer_authorization_rule_with_options_async(
        self,
        consumer_id: str,
        request: main_models.CreateConsumerAuthorizationRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerAuthorizationRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.authorization_resource_infos):
            body['authorizationResourceInfos'] = request.authorization_resource_infos
        if not DaraCore.is_null(request.expire_mode):
            body['expireMode'] = request.expire_mode
        if not DaraCore.is_null(request.expire_timestamp):
            body['expireTimestamp'] = request.expire_timestamp
        if not DaraCore.is_null(request.parent_resource_type):
            body['parentResourceType'] = request.parent_resource_type
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}/authorization-rules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConsumerAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_consumer_authorization_rule(
        self,
        consumer_id: str,
        request: main_models.CreateConsumerAuthorizationRuleRequest,
    ) -> main_models.CreateConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_consumer_authorization_rule_with_options(consumer_id, request, headers, runtime)

    async def create_consumer_authorization_rule_async(
        self,
        consumer_id: str,
        request: main_models.CreateConsumerAuthorizationRuleRequest,
    ) -> main_models.CreateConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_consumer_authorization_rule_with_options_async(consumer_id, request, headers, runtime)

    def create_consumer_authorization_rules_with_options(
        self,
        request: main_models.CreateConsumerAuthorizationRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerAuthorizationRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.authorization_rules):
            body['authorizationRules'] = request.authorization_rules
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumerAuthorizationRules',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/authorization-rules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConsumerAuthorizationRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_consumer_authorization_rules_with_options_async(
        self,
        request: main_models.CreateConsumerAuthorizationRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerAuthorizationRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.authorization_rules):
            body['authorizationRules'] = request.authorization_rules
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumerAuthorizationRules',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/authorization-rules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConsumerAuthorizationRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_consumer_authorization_rules(
        self,
        request: main_models.CreateConsumerAuthorizationRulesRequest,
    ) -> main_models.CreateConsumerAuthorizationRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_consumer_authorization_rules_with_options(request, headers, runtime)

    async def create_consumer_authorization_rules_async(
        self,
        request: main_models.CreateConsumerAuthorizationRulesRequest,
    ) -> main_models.CreateConsumerAuthorizationRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_consumer_authorization_rules_with_options_async(request, headers, runtime)

    def create_domain_with_options(
        self,
        request: main_models.CreateDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDomainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ca_cert_identifier):
            body['caCertIdentifier'] = request.ca_cert_identifier
        if not DaraCore.is_null(request.cert_identifier):
            body['certIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.client_cacert):
            body['clientCACert'] = request.client_cacert
        if not DaraCore.is_null(request.force_https):
            body['forceHttps'] = request.force_https
        if not DaraCore.is_null(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.http_2option):
            body['http2Option'] = request.http_2option
        if not DaraCore.is_null(request.m_tlsenabled):
            body['mTLSEnabled'] = request.m_tlsenabled
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.protocol):
            body['protocol'] = request.protocol
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tls_cipher_suites_config):
            body['tlsCipherSuitesConfig'] = request.tls_cipher_suites_config
        if not DaraCore.is_null(request.tls_max):
            body['tlsMax'] = request.tls_max
        if not DaraCore.is_null(request.tls_min):
            body['tlsMin'] = request.tls_min
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDomain',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/domains',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_domain_with_options_async(
        self,
        request: main_models.CreateDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDomainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ca_cert_identifier):
            body['caCertIdentifier'] = request.ca_cert_identifier
        if not DaraCore.is_null(request.cert_identifier):
            body['certIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.client_cacert):
            body['clientCACert'] = request.client_cacert
        if not DaraCore.is_null(request.force_https):
            body['forceHttps'] = request.force_https
        if not DaraCore.is_null(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.http_2option):
            body['http2Option'] = request.http_2option
        if not DaraCore.is_null(request.m_tlsenabled):
            body['mTLSEnabled'] = request.m_tlsenabled
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.protocol):
            body['protocol'] = request.protocol
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tls_cipher_suites_config):
            body['tlsCipherSuitesConfig'] = request.tls_cipher_suites_config
        if not DaraCore.is_null(request.tls_max):
            body['tlsMax'] = request.tls_max
        if not DaraCore.is_null(request.tls_min):
            body['tlsMin'] = request.tls_min
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDomain',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/domains',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_domain(
        self,
        request: main_models.CreateDomainRequest,
    ) -> main_models.CreateDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_domain_with_options(request, headers, runtime)

    async def create_domain_async(
        self,
        request: main_models.CreateDomainRequest,
    ) -> main_models.CreateDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_domain_with_options_async(request, headers, runtime)

    def create_environment_with_options(
        self,
        request: main_models.CreateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEnvironmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alias):
            body['alias'] = request.alias
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEnvironment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/environments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_environment_with_options_async(
        self,
        request: main_models.CreateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEnvironmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alias):
            body['alias'] = request.alias
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEnvironment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/environments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_environment(
        self,
        request: main_models.CreateEnvironmentRequest,
    ) -> main_models.CreateEnvironmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_environment_with_options(request, headers, runtime)

    async def create_environment_async(
        self,
        request: main_models.CreateEnvironmentRequest,
    ) -> main_models.CreateEnvironmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_environment_with_options_async(request, headers, runtime)

    def create_gateway_with_options(
        self,
        request: main_models.CreateGatewayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateGatewayResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.charge_type):
            body['chargeType'] = request.charge_type
        if not DaraCore.is_null(request.gateway_edition):
            body['gatewayEdition'] = request.gateway_edition
        if not DaraCore.is_null(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.log_config):
            body['logConfig'] = request.log_config
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.network_access_config):
            body['networkAccessConfig'] = request.network_access_config
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.spec):
            body['spec'] = request.spec
        if not DaraCore.is_null(request.tag):
            body['tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_config):
            body['zoneConfig'] = request.zone_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateGateway',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_with_options_async(
        self,
        request: main_models.CreateGatewayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateGatewayResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.charge_type):
            body['chargeType'] = request.charge_type
        if not DaraCore.is_null(request.gateway_edition):
            body['gatewayEdition'] = request.gateway_edition
        if not DaraCore.is_null(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.log_config):
            body['logConfig'] = request.log_config
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.network_access_config):
            body['networkAccessConfig'] = request.network_access_config
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.spec):
            body['spec'] = request.spec
        if not DaraCore.is_null(request.tag):
            body['tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_config):
            body['zoneConfig'] = request.zone_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateGateway',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway(
        self,
        request: main_models.CreateGatewayRequest,
    ) -> main_models.CreateGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_gateway_with_options(request, headers, runtime)

    async def create_gateway_async(
        self,
        request: main_models.CreateGatewayRequest,
    ) -> main_models.CreateGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_gateway_with_options_async(request, headers, runtime)

    def create_http_api_with_options(
        self,
        request: main_models.CreateHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateHttpApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_protocols):
            body['agentProtocols'] = request.agent_protocols
        if not DaraCore.is_null(request.ai_protocols):
            body['aiProtocols'] = request.ai_protocols
        if not DaraCore.is_null(request.auth_config):
            body['authConfig'] = request.auth_config
        if not DaraCore.is_null(request.base_path):
            body['basePath'] = request.base_path
        if not DaraCore.is_null(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.enable_auth):
            body['enableAuth'] = request.enable_auth
        if not DaraCore.is_null(request.first_byte_timeout):
            body['firstByteTimeout'] = request.first_byte_timeout
        if not DaraCore.is_null(request.ingress_config):
            body['ingressConfig'] = request.ingress_config
        if not DaraCore.is_null(request.model_category):
            body['modelCategory'] = request.model_category
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.protocols):
            body['protocols'] = request.protocols
        if not DaraCore.is_null(request.remove_base_path_on_forward):
            body['removeBasePathOnForward'] = request.remove_base_path_on_forward
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        if not DaraCore.is_null(request.version_config):
            body['versionConfig'] = request.version_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_http_api_with_options_async(
        self,
        request: main_models.CreateHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateHttpApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_protocols):
            body['agentProtocols'] = request.agent_protocols
        if not DaraCore.is_null(request.ai_protocols):
            body['aiProtocols'] = request.ai_protocols
        if not DaraCore.is_null(request.auth_config):
            body['authConfig'] = request.auth_config
        if not DaraCore.is_null(request.base_path):
            body['basePath'] = request.base_path
        if not DaraCore.is_null(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.enable_auth):
            body['enableAuth'] = request.enable_auth
        if not DaraCore.is_null(request.first_byte_timeout):
            body['firstByteTimeout'] = request.first_byte_timeout
        if not DaraCore.is_null(request.ingress_config):
            body['ingressConfig'] = request.ingress_config
        if not DaraCore.is_null(request.model_category):
            body['modelCategory'] = request.model_category
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.protocols):
            body['protocols'] = request.protocols
        if not DaraCore.is_null(request.remove_base_path_on_forward):
            body['removeBasePathOnForward'] = request.remove_base_path_on_forward
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        if not DaraCore.is_null(request.version_config):
            body['versionConfig'] = request.version_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_http_api(
        self,
        request: main_models.CreateHttpApiRequest,
    ) -> main_models.CreateHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_http_api_with_options(request, headers, runtime)

    async def create_http_api_async(
        self,
        request: main_models.CreateHttpApiRequest,
    ) -> main_models.CreateHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_http_api_with_options_async(request, headers, runtime)

    def create_http_api_operation_with_options(
        self,
        http_api_id: str,
        request: main_models.CreateHttpApiOperationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateHttpApiOperationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.operations):
            body['operations'] = request.operations
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateHttpApiOperation',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/operations',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHttpApiOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_http_api_operation_with_options_async(
        self,
        http_api_id: str,
        request: main_models.CreateHttpApiOperationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateHttpApiOperationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.operations):
            body['operations'] = request.operations
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateHttpApiOperation',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/operations',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHttpApiOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_http_api_operation(
        self,
        http_api_id: str,
        request: main_models.CreateHttpApiOperationRequest,
    ) -> main_models.CreateHttpApiOperationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_http_api_operation_with_options(http_api_id, request, headers, runtime)

    async def create_http_api_operation_async(
        self,
        http_api_id: str,
        request: main_models.CreateHttpApiOperationRequest,
    ) -> main_models.CreateHttpApiOperationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_http_api_operation_with_options_async(http_api_id, request, headers, runtime)

    def create_http_api_route_with_options(
        self,
        http_api_id: str,
        request: main_models.CreateHttpApiRouteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateHttpApiRouteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not DaraCore.is_null(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.match):
            body['match'] = request.match
        if not DaraCore.is_null(request.mcp_route_config):
            body['mcpRouteConfig'] = request.mcp_route_config
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateHttpApiRoute',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/routes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHttpApiRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_http_api_route_with_options_async(
        self,
        http_api_id: str,
        request: main_models.CreateHttpApiRouteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateHttpApiRouteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not DaraCore.is_null(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.match):
            body['match'] = request.match
        if not DaraCore.is_null(request.mcp_route_config):
            body['mcpRouteConfig'] = request.mcp_route_config
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateHttpApiRoute',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/routes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHttpApiRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_http_api_route(
        self,
        http_api_id: str,
        request: main_models.CreateHttpApiRouteRequest,
    ) -> main_models.CreateHttpApiRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_http_api_route_with_options(http_api_id, request, headers, runtime)

    async def create_http_api_route_async(
        self,
        http_api_id: str,
        request: main_models.CreateHttpApiRouteRequest,
    ) -> main_models.CreateHttpApiRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_http_api_route_with_options_async(http_api_id, request, headers, runtime)

    def create_mcp_server_with_options(
        self,
        request: main_models.CreateMcpServerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcpServerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.assembled_sources):
            body['assembledSources'] = request.assembled_sources
        if not DaraCore.is_null(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not DaraCore.is_null(request.create_from_type):
            body['createFromType'] = request.create_from_type
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not DaraCore.is_null(request.exposed_uri_path):
            body['exposedUriPath'] = request.exposed_uri_path
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gray_mcp_server_configs):
            body['grayMcpServerConfigs'] = request.gray_mcp_server_configs
        if not DaraCore.is_null(request.match):
            body['match'] = request.match
        if not DaraCore.is_null(request.mcp_statistics_enable):
            body['mcpStatisticsEnable'] = request.mcp_statistics_enable
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.protocol):
            body['protocol'] = request.protocol
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcp_server_with_options_async(
        self,
        request: main_models.CreateMcpServerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcpServerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.assembled_sources):
            body['assembledSources'] = request.assembled_sources
        if not DaraCore.is_null(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not DaraCore.is_null(request.create_from_type):
            body['createFromType'] = request.create_from_type
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not DaraCore.is_null(request.exposed_uri_path):
            body['exposedUriPath'] = request.exposed_uri_path
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gray_mcp_server_configs):
            body['grayMcpServerConfigs'] = request.gray_mcp_server_configs
        if not DaraCore.is_null(request.match):
            body['match'] = request.match
        if not DaraCore.is_null(request.mcp_statistics_enable):
            body['mcpStatisticsEnable'] = request.mcp_statistics_enable
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.protocol):
            body['protocol'] = request.protocol
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcp_server(
        self,
        request: main_models.CreateMcpServerRequest,
    ) -> main_models.CreateMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_mcp_server_with_options(request, headers, runtime)

    async def create_mcp_server_async(
        self,
        request: main_models.CreateMcpServerRequest,
    ) -> main_models.CreateMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_mcp_server_with_options_async(request, headers, runtime)

    def create_plugin_attachment_with_options(
        self,
        request: main_models.CreatePluginAttachmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePluginAttachmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not DaraCore.is_null(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.plugin_config):
            body['pluginConfig'] = request.plugin_config
        if not DaraCore.is_null(request.plugin_id):
            body['pluginId'] = request.plugin_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePluginAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-attachments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePluginAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_plugin_attachment_with_options_async(
        self,
        request: main_models.CreatePluginAttachmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePluginAttachmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not DaraCore.is_null(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.plugin_config):
            body['pluginConfig'] = request.plugin_config
        if not DaraCore.is_null(request.plugin_id):
            body['pluginId'] = request.plugin_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePluginAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-attachments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePluginAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_plugin_attachment(
        self,
        request: main_models.CreatePluginAttachmentRequest,
    ) -> main_models.CreatePluginAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_plugin_attachment_with_options(request, headers, runtime)

    async def create_plugin_attachment_async(
        self,
        request: main_models.CreatePluginAttachmentRequest,
    ) -> main_models.CreatePluginAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_plugin_attachment_with_options_async(request, headers, runtime)

    def create_policy_with_options(
        self,
        request: main_models.CreatePolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.class_name):
            body['className'] = request.class_name
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v2/policies',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_with_options_async(
        self,
        request: main_models.CreatePolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.class_name):
            body['className'] = request.class_name
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v2/policies',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.create_policy_with_options(request, headers, runtime)

    async def create_policy_async(
        self,
        request: main_models.CreatePolicyRequest,
    ) -> main_models.CreatePolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_policy_with_options_async(request, headers, runtime)

    def create_policy_attachment_with_options(
        self,
        request: main_models.CreatePolicyAttachmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyAttachmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attach_resource_id):
            body['attachResourceId'] = request.attach_resource_id
        if not DaraCore.is_null(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.policy_id):
            body['policyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicyAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policy-attachments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_attachment_with_options_async(
        self,
        request: main_models.CreatePolicyAttachmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyAttachmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attach_resource_id):
            body['attachResourceId'] = request.attach_resource_id
        if not DaraCore.is_null(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.policy_id):
            body['policyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicyAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policy-attachments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy_attachment(
        self,
        request: main_models.CreatePolicyAttachmentRequest,
    ) -> main_models.CreatePolicyAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_policy_attachment_with_options(request, headers, runtime)

    async def create_policy_attachment_async(
        self,
        request: main_models.CreatePolicyAttachmentRequest,
    ) -> main_models.CreatePolicyAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_policy_attachment_with_options_async(request, headers, runtime)

    def create_service_with_options(
        self,
        request: main_models.CreateServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.service_configs):
            body['serviceConfigs'] = request.service_configs
        if not DaraCore.is_null(request.source_type):
            body['sourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateService',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_with_options_async(
        self,
        request: main_models.CreateServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.service_configs):
            body['serviceConfigs'] = request.service_configs
        if not DaraCore.is_null(request.source_type):
            body['sourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateService',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service(
        self,
        request: main_models.CreateServiceRequest,
    ) -> main_models.CreateServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_service_with_options(request, headers, runtime)

    async def create_service_async(
        self,
        request: main_models.CreateServiceRequest,
    ) -> main_models.CreateServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_service_with_options_async(request, headers, runtime)

    def create_service_version_with_options(
        self,
        service_id: str,
        request: main_models.CreateServiceVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['labels'] = request.labels
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceVersion',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}/versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_version_with_options_async(
        self,
        service_id: str,
        request: main_models.CreateServiceVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['labels'] = request.labels
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceVersion',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}/versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_version(
        self,
        service_id: str,
        request: main_models.CreateServiceVersionRequest,
    ) -> main_models.CreateServiceVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_service_version_with_options(service_id, request, headers, runtime)

    async def create_service_version_async(
        self,
        service_id: str,
        request: main_models.CreateServiceVersionRequest,
    ) -> main_models.CreateServiceVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_service_version_with_options_async(service_id, request, headers, runtime)

    def create_source_with_options(
        self,
        request: main_models.CreateSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.k_8s_source_config):
            body['k8sSourceConfig'] = request.k_8s_source_config
        if not DaraCore.is_null(request.nacos_source_config):
            body['nacosSourceConfig'] = request.nacos_source_config
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSource',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/sources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_source_with_options_async(
        self,
        request: main_models.CreateSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.k_8s_source_config):
            body['k8sSourceConfig'] = request.k_8s_source_config
        if not DaraCore.is_null(request.nacos_source_config):
            body['nacosSourceConfig'] = request.nacos_source_config
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSource',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/sources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_source(
        self,
        request: main_models.CreateSourceRequest,
    ) -> main_models.CreateSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_source_with_options(request, headers, runtime)

    async def create_source_async(
        self,
        request: main_models.CreateSourceRequest,
    ) -> main_models.CreateSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_source_with_options_async(request, headers, runtime)

    def delete_consumer_with_options(
        self,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConsumerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_consumer_with_options_async(
        self,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConsumerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_consumer(
        self,
        consumer_id: str,
    ) -> main_models.DeleteConsumerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_consumer_with_options(consumer_id, headers, runtime)

    async def delete_consumer_async(
        self,
        consumer_id: str,
    ) -> main_models.DeleteConsumerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_consumer_with_options_async(consumer_id, headers, runtime)

    def delete_consumer_authorization_rule_with_options(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumerAuthorizationRuleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}/authorization-rules/{DaraURL.percent_encode(consumer_authorization_rule_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConsumerAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_consumer_authorization_rule_with_options_async(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumerAuthorizationRuleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}/authorization-rules/{DaraURL.percent_encode(consumer_authorization_rule_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConsumerAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_consumer_authorization_rule(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
    ) -> main_models.DeleteConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_consumer_authorization_rule_with_options(consumer_authorization_rule_id, consumer_id, headers, runtime)

    async def delete_consumer_authorization_rule_async(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
    ) -> main_models.DeleteConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_consumer_authorization_rule_with_options_async(consumer_authorization_rule_id, consumer_id, headers, runtime)

    def delete_domain_with_options(
        self,
        domain_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomain',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/domains/{DaraURL.percent_encode(domain_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        domain_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomain',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/domains/{DaraURL.percent_encode(domain_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain(
        self,
        domain_id: str,
    ) -> main_models.DeleteDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_domain_with_options(domain_id, headers, runtime)

    async def delete_domain_async(
        self,
        domain_id: str,
    ) -> main_models.DeleteDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_domain_with_options_async(domain_id, headers, runtime)

    def delete_environment_with_options(
        self,
        environment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnvironmentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnvironment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/environments/{DaraURL.percent_encode(environment_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_environment_with_options_async(
        self,
        environment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnvironmentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnvironment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/environments/{DaraURL.percent_encode(environment_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_environment(
        self,
        environment_id: str,
    ) -> main_models.DeleteEnvironmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_environment_with_options(environment_id, headers, runtime)

    async def delete_environment_async(
        self,
        environment_id: str,
    ) -> main_models.DeleteEnvironmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_environment_with_options_async(environment_id, headers, runtime)

    def delete_gateway_with_options(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteGateway',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_with_options_async(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteGateway',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway(
        self,
        gateway_id: str,
    ) -> main_models.DeleteGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_gateway_with_options(gateway_id, headers, runtime)

    async def delete_gateway_async(
        self,
        gateway_id: str,
    ) -> main_models.DeleteGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_gateway_with_options_async(gateway_id, headers, runtime)

    def delete_gateway_security_group_rule_with_options(
        self,
        gateway_id: str,
        security_group_rule_id: str,
        request: main_models.DeleteGatewaySecurityGroupRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewaySecurityGroupRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cascading_delete):
            query['cascadingDelete'] = request.cascading_delete
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewaySecurityGroupRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/security-group-rules/{DaraURL.percent_encode(security_group_rule_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewaySecurityGroupRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_security_group_rule_with_options_async(
        self,
        gateway_id: str,
        security_group_rule_id: str,
        request: main_models.DeleteGatewaySecurityGroupRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewaySecurityGroupRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cascading_delete):
            query['cascadingDelete'] = request.cascading_delete
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewaySecurityGroupRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/security-group-rules/{DaraURL.percent_encode(security_group_rule_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewaySecurityGroupRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_security_group_rule(
        self,
        gateway_id: str,
        security_group_rule_id: str,
        request: main_models.DeleteGatewaySecurityGroupRuleRequest,
    ) -> main_models.DeleteGatewaySecurityGroupRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_gateway_security_group_rule_with_options(gateway_id, security_group_rule_id, request, headers, runtime)

    async def delete_gateway_security_group_rule_async(
        self,
        gateway_id: str,
        security_group_rule_id: str,
        request: main_models.DeleteGatewaySecurityGroupRuleRequest,
    ) -> main_models.DeleteGatewaySecurityGroupRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_gateway_security_group_rule_with_options_async(gateway_id, security_group_rule_id, request, headers, runtime)

    def delete_http_api_with_options(
        self,
        http_api_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHttpApiResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_http_api_with_options_async(
        self,
        http_api_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHttpApiResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_http_api(
        self,
        http_api_id: str,
    ) -> main_models.DeleteHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_http_api_with_options(http_api_id, headers, runtime)

    async def delete_http_api_async(
        self,
        http_api_id: str,
    ) -> main_models.DeleteHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_http_api_with_options_async(http_api_id, headers, runtime)

    def delete_http_api_operation_with_options(
        self,
        http_api_id: str,
        operation_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHttpApiOperationResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteHttpApiOperation',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/operations/{DaraURL.percent_encode(operation_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHttpApiOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_http_api_operation_with_options_async(
        self,
        http_api_id: str,
        operation_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHttpApiOperationResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteHttpApiOperation',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/operations/{DaraURL.percent_encode(operation_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHttpApiOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_http_api_operation(
        self,
        http_api_id: str,
        operation_id: str,
    ) -> main_models.DeleteHttpApiOperationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_http_api_operation_with_options(http_api_id, operation_id, headers, runtime)

    async def delete_http_api_operation_async(
        self,
        http_api_id: str,
        operation_id: str,
    ) -> main_models.DeleteHttpApiOperationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_http_api_operation_with_options_async(http_api_id, operation_id, headers, runtime)

    def delete_http_api_route_with_options(
        self,
        http_api_id: str,
        route_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHttpApiRouteResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteHttpApiRoute',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/routes/{DaraURL.percent_encode(route_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHttpApiRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_http_api_route_with_options_async(
        self,
        http_api_id: str,
        route_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHttpApiRouteResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteHttpApiRoute',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/routes/{DaraURL.percent_encode(route_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHttpApiRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_http_api_route(
        self,
        http_api_id: str,
        route_id: str,
    ) -> main_models.DeleteHttpApiRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_http_api_route_with_options(http_api_id, route_id, headers, runtime)

    async def delete_http_api_route_async(
        self,
        http_api_id: str,
        route_id: str,
    ) -> main_models.DeleteHttpApiRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_http_api_route_with_options_async(http_api_id, route_id, headers, runtime)

    def delete_mcp_server_with_options(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcpServerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mcp_server_with_options_async(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcpServerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mcp_server(
        self,
        mcp_server_id: str,
    ) -> main_models.DeleteMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_mcp_server_with_options(mcp_server_id, headers, runtime)

    async def delete_mcp_server_async(
        self,
        mcp_server_id: str,
    ) -> main_models.DeleteMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_mcp_server_with_options_async(mcp_server_id, headers, runtime)

    def delete_plugin_attachment_with_options(
        self,
        plugin_attachment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePluginAttachmentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePluginAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-attachments/{DaraURL.percent_encode(plugin_attachment_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePluginAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_plugin_attachment_with_options_async(
        self,
        plugin_attachment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePluginAttachmentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePluginAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-attachments/{DaraURL.percent_encode(plugin_attachment_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePluginAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_plugin_attachment(
        self,
        plugin_attachment_id: str,
    ) -> main_models.DeletePluginAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_plugin_attachment_with_options(plugin_attachment_id, headers, runtime)

    async def delete_plugin_attachment_async(
        self,
        plugin_attachment_id: str,
    ) -> main_models.DeletePluginAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_plugin_attachment_with_options_async(plugin_attachment_id, headers, runtime)

    def delete_policy_with_options(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v2/policies/{DaraURL.percent_encode(policy_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_with_options_async(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v2/policies/{DaraURL.percent_encode(policy_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy(
        self,
        policy_id: str,
    ) -> main_models.DeletePolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_policy_with_options(policy_id, headers, runtime)

    async def delete_policy_async(
        self,
        policy_id: str,
    ) -> main_models.DeletePolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_policy_with_options_async(policy_id, headers, runtime)

    def delete_policy_attachment_with_options(
        self,
        policy_attachment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyAttachmentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicyAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policy-attachments/{DaraURL.percent_encode(policy_attachment_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_attachment_with_options_async(
        self,
        policy_attachment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyAttachmentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicyAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policy-attachments/{DaraURL.percent_encode(policy_attachment_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy_attachment(
        self,
        policy_attachment_id: str,
    ) -> main_models.DeletePolicyAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_policy_attachment_with_options(policy_attachment_id, headers, runtime)

    async def delete_policy_attachment_async(
        self,
        policy_attachment_id: str,
    ) -> main_models.DeletePolicyAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_policy_attachment_with_options_async(policy_attachment_id, headers, runtime)

    def delete_service_with_options(
        self,
        service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteService',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_with_options_async(
        self,
        service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteService',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service(
        self,
        service_id: str,
    ) -> main_models.DeleteServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_service_with_options(service_id, headers, runtime)

    async def delete_service_async(
        self,
        service_id: str,
    ) -> main_models.DeleteServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_service_with_options_async(service_id, headers, runtime)

    def delete_service_version_with_options(
        self,
        service_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceVersion',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}/versions/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_version_with_options_async(
        self,
        service_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceVersion',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}/versions/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_version(
        self,
        service_id: str,
        name: str,
    ) -> main_models.DeleteServiceVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_service_version_with_options(service_id, name, headers, runtime)

    async def delete_service_version_async(
        self,
        service_id: str,
        name: str,
    ) -> main_models.DeleteServiceVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_service_version_with_options_async(service_id, name, headers, runtime)

    def delete_source_with_options(
        self,
        source_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSource',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/sources/{DaraURL.percent_encode(source_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_source_with_options_async(
        self,
        source_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSource',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/sources/{DaraURL.percent_encode(source_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_source(
        self,
        source_id: str,
    ) -> main_models.DeleteSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_source_with_options(source_id, headers, runtime)

    async def delete_source_async(
        self,
        source_id: str,
    ) -> main_models.DeleteSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_source_with_options_async(source_id, headers, runtime)

    def deploy_http_api_with_options(
        self,
        http_api_id: str,
        request: main_models.DeployHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeployHttpApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.http_api_config):
            body['httpApiConfig'] = request.http_api_config
        if not DaraCore.is_null(request.rest_api_config):
            body['restApiConfig'] = request.rest_api_config
        if not DaraCore.is_null(request.route_id):
            body['routeId'] = request.route_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeployHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/deploy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_http_api_with_options_async(
        self,
        http_api_id: str,
        request: main_models.DeployHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeployHttpApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.http_api_config):
            body['httpApiConfig'] = request.http_api_config
        if not DaraCore.is_null(request.rest_api_config):
            body['restApiConfig'] = request.rest_api_config
        if not DaraCore.is_null(request.route_id):
            body['routeId'] = request.route_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeployHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/deploy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_http_api(
        self,
        http_api_id: str,
        request: main_models.DeployHttpApiRequest,
    ) -> main_models.DeployHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.deploy_http_api_with_options(http_api_id, request, headers, runtime)

    async def deploy_http_api_async(
        self,
        http_api_id: str,
        request: main_models.DeployHttpApiRequest,
    ) -> main_models.DeployHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.deploy_http_api_with_options_async(http_api_id, request, headers, runtime)

    def deploy_mcp_server_with_options(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeployMcpServerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeployMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}/deploy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_mcp_server_with_options_async(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeployMcpServerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeployMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}/deploy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_mcp_server(
        self,
        mcp_server_id: str,
    ) -> main_models.DeployMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.deploy_mcp_server_with_options(mcp_server_id, headers, runtime)

    async def deploy_mcp_server_async(
        self,
        mcp_server_id: str,
    ) -> main_models.DeployMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.deploy_mcp_server_with_options_async(mcp_server_id, headers, runtime)

    def export_http_api_with_options(
        self,
        http_api_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExportHttpApiResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ExportHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/export',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_http_api_with_options_async(
        self,
        http_api_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExportHttpApiResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ExportHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/export',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_http_api(
        self,
        http_api_id: str,
    ) -> main_models.ExportHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.export_http_api_with_options(http_api_id, headers, runtime)

    async def export_http_api_async(
        self,
        http_api_id: str,
    ) -> main_models.ExportHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.export_http_api_with_options_async(http_api_id, headers, runtime)

    def get_consumer_with_options(
        self,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConsumer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consumer_with_options_async(
        self,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConsumer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consumer(
        self,
        consumer_id: str,
    ) -> main_models.GetConsumerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_consumer_with_options(consumer_id, headers, runtime)

    async def get_consumer_async(
        self,
        consumer_id: str,
    ) -> main_models.GetConsumerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_consumer_with_options_async(consumer_id, headers, runtime)

    def get_consumer_authorization_rule_with_options(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumerAuthorizationRuleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}/authorization-rules/{DaraURL.percent_encode(consumer_authorization_rule_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumerAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consumer_authorization_rule_with_options_async(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumerAuthorizationRuleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}/authorization-rules/{DaraURL.percent_encode(consumer_authorization_rule_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumerAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consumer_authorization_rule(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
    ) -> main_models.GetConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_consumer_authorization_rule_with_options(consumer_authorization_rule_id, consumer_id, headers, runtime)

    async def get_consumer_authorization_rule_async(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
    ) -> main_models.GetConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_consumer_authorization_rule_with_options_async(consumer_authorization_rule_id, consumer_id, headers, runtime)

    def get_dashboard_with_options(
        self,
        gateway_id: str,
        tmp_req: main_models.GetDashboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDashboardResponse:
        tmp_req.validate()
        request = main_models.GetDashboardShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.api_id):
            query['apiId'] = request.api_id
        if not DaraCore.is_null(request.filter_shrink):
            query['filter'] = request.filter_shrink
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.plugin_class_id):
            query['pluginClassId'] = request.plugin_class_id
        if not DaraCore.is_null(request.plugin_id):
            query['pluginId'] = request.plugin_id
        if not DaraCore.is_null(request.route_id):
            query['routeId'] = request.route_id
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        if not DaraCore.is_null(request.upstream_cluster):
            query['upstreamCluster'] = request.upstream_cluster
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDashboard',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/dashboards',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDashboardResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dashboard_with_options_async(
        self,
        gateway_id: str,
        tmp_req: main_models.GetDashboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDashboardResponse:
        tmp_req.validate()
        request = main_models.GetDashboardShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.api_id):
            query['apiId'] = request.api_id
        if not DaraCore.is_null(request.filter_shrink):
            query['filter'] = request.filter_shrink
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.plugin_class_id):
            query['pluginClassId'] = request.plugin_class_id
        if not DaraCore.is_null(request.plugin_id):
            query['pluginId'] = request.plugin_id
        if not DaraCore.is_null(request.route_id):
            query['routeId'] = request.route_id
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        if not DaraCore.is_null(request.upstream_cluster):
            query['upstreamCluster'] = request.upstream_cluster
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDashboard',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/dashboards',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDashboardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dashboard(
        self,
        gateway_id: str,
        request: main_models.GetDashboardRequest,
    ) -> main_models.GetDashboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_dashboard_with_options(gateway_id, request, headers, runtime)

    async def get_dashboard_async(
        self,
        gateway_id: str,
        request: main_models.GetDashboardRequest,
    ) -> main_models.GetDashboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_dashboard_with_options_async(gateway_id, request, headers, runtime)

    def get_domain_with_options(
        self,
        domain_id: str,
        request: main_models.GetDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.with_statistics):
            query['withStatistics'] = request.with_statistics
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDomain',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/domains/{DaraURL.percent_encode(domain_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_domain_with_options_async(
        self,
        domain_id: str,
        request: main_models.GetDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.with_statistics):
            query['withStatistics'] = request.with_statistics
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDomain',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/domains/{DaraURL.percent_encode(domain_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_domain(
        self,
        domain_id: str,
        request: main_models.GetDomainRequest,
    ) -> main_models.GetDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_domain_with_options(domain_id, request, headers, runtime)

    async def get_domain_async(
        self,
        domain_id: str,
        request: main_models.GetDomainRequest,
    ) -> main_models.GetDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_domain_with_options_async(domain_id, request, headers, runtime)

    def get_environment_with_options(
        self,
        environment_id: str,
        request: main_models.GetEnvironmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEnvironmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.with_statistics):
            query['withStatistics'] = request.with_statistics
        if not DaraCore.is_null(request.with_vpc_info):
            query['withVpcInfo'] = request.with_vpc_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEnvironment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/environments/{DaraURL.percent_encode(environment_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_environment_with_options_async(
        self,
        environment_id: str,
        request: main_models.GetEnvironmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEnvironmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.with_statistics):
            query['withStatistics'] = request.with_statistics
        if not DaraCore.is_null(request.with_vpc_info):
            query['withVpcInfo'] = request.with_vpc_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEnvironment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/environments/{DaraURL.percent_encode(environment_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_environment(
        self,
        environment_id: str,
        request: main_models.GetEnvironmentRequest,
    ) -> main_models.GetEnvironmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_environment_with_options(environment_id, request, headers, runtime)

    async def get_environment_async(
        self,
        environment_id: str,
        request: main_models.GetEnvironmentRequest,
    ) -> main_models.GetEnvironmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_environment_with_options_async(environment_id, request, headers, runtime)

    def get_gateway_with_options(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetGateway',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gateway_with_options_async(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetGateway',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gateway(
        self,
        gateway_id: str,
    ) -> main_models.GetGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_gateway_with_options(gateway_id, headers, runtime)

    async def get_gateway_async(
        self,
        gateway_id: str,
    ) -> main_models.GetGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_gateway_with_options_async(gateway_id, headers, runtime)

    def get_http_api_with_options(
        self,
        http_api_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHttpApiResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_http_api_with_options_async(
        self,
        http_api_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHttpApiResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_http_api(
        self,
        http_api_id: str,
    ) -> main_models.GetHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_http_api_with_options(http_api_id, headers, runtime)

    async def get_http_api_async(
        self,
        http_api_id: str,
    ) -> main_models.GetHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_http_api_with_options_async(http_api_id, headers, runtime)

    def get_http_api_operation_with_options(
        self,
        http_api_id: str,
        operation_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHttpApiOperationResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetHttpApiOperation',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/operations/{DaraURL.percent_encode(operation_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHttpApiOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_http_api_operation_with_options_async(
        self,
        http_api_id: str,
        operation_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHttpApiOperationResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetHttpApiOperation',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/operations/{DaraURL.percent_encode(operation_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHttpApiOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_http_api_operation(
        self,
        http_api_id: str,
        operation_id: str,
    ) -> main_models.GetHttpApiOperationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_http_api_operation_with_options(http_api_id, operation_id, headers, runtime)

    async def get_http_api_operation_async(
        self,
        http_api_id: str,
        operation_id: str,
    ) -> main_models.GetHttpApiOperationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_http_api_operation_with_options_async(http_api_id, operation_id, headers, runtime)

    def get_http_api_route_with_options(
        self,
        http_api_id: str,
        route_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHttpApiRouteResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetHttpApiRoute',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/routes/{DaraURL.percent_encode(route_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHttpApiRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_http_api_route_with_options_async(
        self,
        http_api_id: str,
        route_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHttpApiRouteResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetHttpApiRoute',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/routes/{DaraURL.percent_encode(route_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHttpApiRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_http_api_route(
        self,
        http_api_id: str,
        route_id: str,
    ) -> main_models.GetHttpApiRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_http_api_route_with_options(http_api_id, route_id, headers, runtime)

    async def get_http_api_route_async(
        self,
        http_api_id: str,
        route_id: str,
    ) -> main_models.GetHttpApiRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_http_api_route_with_options_async(http_api_id, route_id, headers, runtime)

    def get_mcp_server_with_options(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMcpServerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mcp_server_with_options_async(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMcpServerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mcp_server(
        self,
        mcp_server_id: str,
    ) -> main_models.GetMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_mcp_server_with_options(mcp_server_id, headers, runtime)

    async def get_mcp_server_async(
        self,
        mcp_server_id: str,
    ) -> main_models.GetMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_mcp_server_with_options_async(mcp_server_id, headers, runtime)

    def get_plugin_attachment_with_options(
        self,
        plugin_attachment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPluginAttachmentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPluginAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-attachments/{DaraURL.percent_encode(plugin_attachment_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPluginAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_plugin_attachment_with_options_async(
        self,
        plugin_attachment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPluginAttachmentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPluginAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-attachments/{DaraURL.percent_encode(plugin_attachment_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPluginAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_plugin_attachment(
        self,
        plugin_attachment_id: str,
    ) -> main_models.GetPluginAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_plugin_attachment_with_options(plugin_attachment_id, headers, runtime)

    async def get_plugin_attachment_async(
        self,
        plugin_attachment_id: str,
    ) -> main_models.GetPluginAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_plugin_attachment_with_options_async(plugin_attachment_id, headers, runtime)

    def get_policy_with_options(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v2/policies/{DaraURL.percent_encode(policy_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_with_options_async(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v2/policies/{DaraURL.percent_encode(policy_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy(
        self,
        policy_id: str,
    ) -> main_models.GetPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_policy_with_options(policy_id, headers, runtime)

    async def get_policy_async(
        self,
        policy_id: str,
    ) -> main_models.GetPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_policy_with_options_async(policy_id, headers, runtime)

    def get_policy_attachment_with_options(
        self,
        policy_attachment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyAttachmentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPolicyAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policy-attachments/{DaraURL.percent_encode(policy_attachment_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPolicyAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_attachment_with_options_async(
        self,
        policy_attachment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyAttachmentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPolicyAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policy-attachments/{DaraURL.percent_encode(policy_attachment_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPolicyAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy_attachment(
        self,
        policy_attachment_id: str,
    ) -> main_models.GetPolicyAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_policy_attachment_with_options(policy_attachment_id, headers, runtime)

    async def get_policy_attachment_async(
        self,
        policy_attachment_id: str,
    ) -> main_models.GetPolicyAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_policy_attachment_with_options_async(policy_attachment_id, headers, runtime)

    def get_resource_overview_with_options(
        self,
        request: main_models.GetResourceOverviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceOverviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceOverview',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/overview/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_overview_with_options_async(
        self,
        request: main_models.GetResourceOverviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceOverviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceOverview',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/overview/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_overview(
        self,
        request: main_models.GetResourceOverviewRequest,
    ) -> main_models.GetResourceOverviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_resource_overview_with_options(request, headers, runtime)

    async def get_resource_overview_async(
        self,
        request: main_models.GetResourceOverviewRequest,
    ) -> main_models.GetResourceOverviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_resource_overview_with_options_async(request, headers, runtime)

    def get_service_with_options(
        self,
        service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetService',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_with_options_async(
        self,
        service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetService',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service(
        self,
        service_id: str,
    ) -> main_models.GetServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_service_with_options(service_id, headers, runtime)

    async def get_service_async(
        self,
        service_id: str,
    ) -> main_models.GetServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_service_with_options_async(service_id, headers, runtime)

    def get_source_with_options(
        self,
        source_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSource',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/sources/{DaraURL.percent_encode(source_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_source_with_options_async(
        self,
        source_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSource',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/sources/{DaraURL.percent_encode(source_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_source(
        self,
        source_id: str,
    ) -> main_models.GetSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_source_with_options(source_id, headers, runtime)

    async def get_source_async(
        self,
        source_id: str,
    ) -> main_models.GetSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_source_with_options_async(source_id, headers, runtime)

    def get_trace_config_with_options(
        self,
        gateway_id: str,
        request: main_models.GetTraceConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTraceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTraceConfig',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/trace',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTraceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trace_config_with_options_async(
        self,
        gateway_id: str,
        request: main_models.GetTraceConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTraceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTraceConfig',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/trace',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTraceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trace_config(
        self,
        gateway_id: str,
        request: main_models.GetTraceConfigRequest,
    ) -> main_models.GetTraceConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_trace_config_with_options(gateway_id, request, headers, runtime)

    async def get_trace_config_async(
        self,
        gateway_id: str,
        request: main_models.GetTraceConfigRequest,
    ) -> main_models.GetTraceConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_trace_config_with_options_async(gateway_id, request, headers, runtime)

    def import_http_api_with_options(
        self,
        request: main_models.ImportHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ImportHttpApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.mcp_route_id):
            body['mcpRouteId'] = request.mcp_route_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.spec_content_base_64):
            body['specContentBase64'] = request.spec_content_base_64
        if not DaraCore.is_null(request.spec_file_url):
            body['specFileUrl'] = request.spec_file_url
        if not DaraCore.is_null(request.spec_oss_config):
            body['specOssConfig'] = request.spec_oss_config
        if not DaraCore.is_null(request.strategy):
            body['strategy'] = request.strategy
        if not DaraCore.is_null(request.target_http_api_id):
            body['targetHttpApiId'] = request.target_http_api_id
        if not DaraCore.is_null(request.version_config):
            body['versionConfig'] = request.version_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/import',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_http_api_with_options_async(
        self,
        request: main_models.ImportHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ImportHttpApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.mcp_route_id):
            body['mcpRouteId'] = request.mcp_route_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.spec_content_base_64):
            body['specContentBase64'] = request.spec_content_base_64
        if not DaraCore.is_null(request.spec_file_url):
            body['specFileUrl'] = request.spec_file_url
        if not DaraCore.is_null(request.spec_oss_config):
            body['specOssConfig'] = request.spec_oss_config
        if not DaraCore.is_null(request.strategy):
            body['strategy'] = request.strategy
        if not DaraCore.is_null(request.target_http_api_id):
            body['targetHttpApiId'] = request.target_http_api_id
        if not DaraCore.is_null(request.version_config):
            body['versionConfig'] = request.version_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/import',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_http_api(
        self,
        request: main_models.ImportHttpApiRequest,
    ) -> main_models.ImportHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.import_http_api_with_options(request, headers, runtime)

    async def import_http_api_async(
        self,
        request: main_models.ImportHttpApiRequest,
    ) -> main_models.ImportHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.import_http_api_with_options_async(request, headers, runtime)

    def install_plugin_with_options(
        self,
        request: main_models.InstallPluginRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallPluginResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.gateway_ids):
            body['gatewayIds'] = request.gateway_ids
        if not DaraCore.is_null(request.plugin_class_id):
            body['pluginClassId'] = request.plugin_class_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InstallPlugin',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugins/',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallPluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_plugin_with_options_async(
        self,
        request: main_models.InstallPluginRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallPluginResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.gateway_ids):
            body['gatewayIds'] = request.gateway_ids
        if not DaraCore.is_null(request.plugin_class_id):
            body['pluginClassId'] = request.plugin_class_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InstallPlugin',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugins/',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallPluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_plugin(
        self,
        request: main_models.InstallPluginRequest,
    ) -> main_models.InstallPluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.install_plugin_with_options(request, headers, runtime)

    async def install_plugin_async(
        self,
        request: main_models.InstallPluginRequest,
    ) -> main_models.InstallPluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.install_plugin_with_options_async(request, headers, runtime)

    def list_consumers_with_options(
        self,
        request: main_models.ListConsumersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumers',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_consumers_with_options_async(
        self,
        request: main_models.ListConsumersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumers',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_consumers(
        self,
        request: main_models.ListConsumersRequest,
    ) -> main_models.ListConsumersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_consumers_with_options(request, headers, runtime)

    async def list_consumers_async(
        self,
        request: main_models.ListConsumersRequest,
    ) -> main_models.ListConsumersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_consumers_with_options_async(request, headers, runtime)

    def list_domains_with_options(
        self,
        request: main_models.ListDomainsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDomains',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/domains',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_domains_with_options_async(
        self,
        request: main_models.ListDomainsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDomains',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/domains',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_domains(
        self,
        request: main_models.ListDomainsRequest,
    ) -> main_models.ListDomainsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_domains_with_options(request, headers, runtime)

    async def list_domains_async(
        self,
        request: main_models.ListDomainsRequest,
    ) -> main_models.ListDomainsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_domains_with_options_async(request, headers, runtime)

    def list_environments_with_options(
        self,
        request: main_models.ListEnvironmentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvironmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias_like):
            query['aliasLike'] = request.alias_like
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_name_like):
            query['gatewayNameLike'] = request.gateway_name_like
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvironments',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/environments',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvironmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environments_with_options_async(
        self,
        request: main_models.ListEnvironmentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvironmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias_like):
            query['aliasLike'] = request.alias_like
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_name_like):
            query['gatewayNameLike'] = request.gateway_name_like
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvironments',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/environments',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvironmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environments(
        self,
        request: main_models.ListEnvironmentsRequest,
    ) -> main_models.ListEnvironmentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_environments_with_options(request, headers, runtime)

    async def list_environments_async(
        self,
        request: main_models.ListEnvironmentsRequest,
    ) -> main_models.ListEnvironmentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_environments_with_options_async(request, headers, runtime)

    def list_gateway_features_with_options(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayFeaturesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayFeatures',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/gateway-features',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayFeaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_features_with_options_async(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayFeaturesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayFeatures',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/gateway-features',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayFeaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_features(
        self,
        gateway_id: str,
    ) -> main_models.ListGatewayFeaturesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_gateway_features_with_options(gateway_id, headers, runtime)

    async def list_gateway_features_async(
        self,
        gateway_id: str,
    ) -> main_models.ListGatewayFeaturesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_gateway_features_with_options_async(gateway_id, headers, runtime)

    def list_gateways_with_options(
        self,
        tmp_req: main_models.ListGatewaysRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewaysResponse:
        tmp_req.validate()
        request = main_models.ListGatewaysShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGateways',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewaysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateways_with_options_async(
        self,
        tmp_req: main_models.ListGatewaysRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewaysResponse:
        tmp_req.validate()
        request = main_models.ListGatewaysShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGateways',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewaysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateways(
        self,
        request: main_models.ListGatewaysRequest,
    ) -> main_models.ListGatewaysResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_gateways_with_options(request, headers, runtime)

    async def list_gateways_async(
        self,
        request: main_models.ListGatewaysRequest,
    ) -> main_models.ListGatewaysResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_gateways_with_options_async(request, headers, runtime)

    def list_http_api_operations_with_options(
        self,
        http_api_id: str,
        request: main_models.ListHttpApiOperationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListHttpApiOperationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_authorization_rule_id):
            query['consumerAuthorizationRuleId'] = request.consumer_authorization_rule_id
        if not DaraCore.is_null(request.enable_auth):
            query['enableAuth'] = request.enable_auth
        if not DaraCore.is_null(request.for_deploy):
            query['forDeploy'] = request.for_deploy
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.method):
            query['method'] = request.method
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.path_like):
            query['pathLike'] = request.path_like
        if not DaraCore.is_null(request.with_consumer_in_environment_id):
            query['withConsumerInEnvironmentId'] = request.with_consumer_in_environment_id
        if not DaraCore.is_null(request.with_consumer_info_by_id):
            query['withConsumerInfoById'] = request.with_consumer_info_by_id
        if not DaraCore.is_null(request.with_plugin_attachment_by_plugin_id):
            query['withPluginAttachmentByPluginId'] = request.with_plugin_attachment_by_plugin_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHttpApiOperations',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/operations',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHttpApiOperationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_http_api_operations_with_options_async(
        self,
        http_api_id: str,
        request: main_models.ListHttpApiOperationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListHttpApiOperationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_authorization_rule_id):
            query['consumerAuthorizationRuleId'] = request.consumer_authorization_rule_id
        if not DaraCore.is_null(request.enable_auth):
            query['enableAuth'] = request.enable_auth
        if not DaraCore.is_null(request.for_deploy):
            query['forDeploy'] = request.for_deploy
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.method):
            query['method'] = request.method
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.path_like):
            query['pathLike'] = request.path_like
        if not DaraCore.is_null(request.with_consumer_in_environment_id):
            query['withConsumerInEnvironmentId'] = request.with_consumer_in_environment_id
        if not DaraCore.is_null(request.with_consumer_info_by_id):
            query['withConsumerInfoById'] = request.with_consumer_info_by_id
        if not DaraCore.is_null(request.with_plugin_attachment_by_plugin_id):
            query['withPluginAttachmentByPluginId'] = request.with_plugin_attachment_by_plugin_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHttpApiOperations',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/operations',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHttpApiOperationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_http_api_operations(
        self,
        http_api_id: str,
        request: main_models.ListHttpApiOperationsRequest,
    ) -> main_models.ListHttpApiOperationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_http_api_operations_with_options(http_api_id, request, headers, runtime)

    async def list_http_api_operations_async(
        self,
        http_api_id: str,
        request: main_models.ListHttpApiOperationsRequest,
    ) -> main_models.ListHttpApiOperationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_http_api_operations_with_options_async(http_api_id, request, headers, runtime)

    def list_http_api_routes_with_options(
        self,
        http_api_id: str,
        request: main_models.ListHttpApiRoutesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListHttpApiRoutesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_authorization_rule_id):
            query['consumerAuthorizationRuleId'] = request.consumer_authorization_rule_id
        if not DaraCore.is_null(request.deploy_statuses):
            query['deployStatuses'] = request.deploy_statuses
        if not DaraCore.is_null(request.domain_id):
            query['domainId'] = request.domain_id
        if not DaraCore.is_null(request.environment_id):
            query['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.for_deploy):
            query['forDeploy'] = request.for_deploy
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.path_like):
            query['pathLike'] = request.path_like
        if not DaraCore.is_null(request.with_auth_policy_info):
            query['withAuthPolicyInfo'] = request.with_auth_policy_info
        if not DaraCore.is_null(request.with_consumer_info_by_id):
            query['withConsumerInfoById'] = request.with_consumer_info_by_id
        if not DaraCore.is_null(request.with_plugin_attachment_by_plugin_id):
            query['withPluginAttachmentByPluginId'] = request.with_plugin_attachment_by_plugin_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHttpApiRoutes',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/routes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHttpApiRoutesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_http_api_routes_with_options_async(
        self,
        http_api_id: str,
        request: main_models.ListHttpApiRoutesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListHttpApiRoutesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_authorization_rule_id):
            query['consumerAuthorizationRuleId'] = request.consumer_authorization_rule_id
        if not DaraCore.is_null(request.deploy_statuses):
            query['deployStatuses'] = request.deploy_statuses
        if not DaraCore.is_null(request.domain_id):
            query['domainId'] = request.domain_id
        if not DaraCore.is_null(request.environment_id):
            query['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.for_deploy):
            query['forDeploy'] = request.for_deploy
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.path_like):
            query['pathLike'] = request.path_like
        if not DaraCore.is_null(request.with_auth_policy_info):
            query['withAuthPolicyInfo'] = request.with_auth_policy_info
        if not DaraCore.is_null(request.with_consumer_info_by_id):
            query['withConsumerInfoById'] = request.with_consumer_info_by_id
        if not DaraCore.is_null(request.with_plugin_attachment_by_plugin_id):
            query['withPluginAttachmentByPluginId'] = request.with_plugin_attachment_by_plugin_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHttpApiRoutes',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/routes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHttpApiRoutesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_http_api_routes(
        self,
        http_api_id: str,
        request: main_models.ListHttpApiRoutesRequest,
    ) -> main_models.ListHttpApiRoutesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_http_api_routes_with_options(http_api_id, request, headers, runtime)

    async def list_http_api_routes_async(
        self,
        http_api_id: str,
        request: main_models.ListHttpApiRoutesRequest,
    ) -> main_models.ListHttpApiRoutesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_http_api_routes_with_options_async(http_api_id, request, headers, runtime)

    def list_http_apis_with_options(
        self,
        request: main_models.ListHttpApisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListHttpApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.types):
            query['types'] = request.types
        if not DaraCore.is_null(request.with_apis_published_to_environment):
            query['withAPIsPublishedToEnvironment'] = request.with_apis_published_to_environment
        if not DaraCore.is_null(request.with_auth_policy_in_environment_id):
            query['withAuthPolicyInEnvironmentId'] = request.with_auth_policy_in_environment_id
        if not DaraCore.is_null(request.with_auth_policy_list):
            query['withAuthPolicyList'] = request.with_auth_policy_list
        if not DaraCore.is_null(request.with_consumer_info_by_id):
            query['withConsumerInfoById'] = request.with_consumer_info_by_id
        if not DaraCore.is_null(request.with_environment_info):
            query['withEnvironmentInfo'] = request.with_environment_info
        if not DaraCore.is_null(request.with_environment_info_by_id):
            query['withEnvironmentInfoById'] = request.with_environment_info_by_id
        if not DaraCore.is_null(request.with_ingress_info):
            query['withIngressInfo'] = request.with_ingress_info
        if not DaraCore.is_null(request.with_plugin_attachment_by_plugin_id):
            query['withPluginAttachmentByPluginId'] = request.with_plugin_attachment_by_plugin_id
        if not DaraCore.is_null(request.with_policy_configs):
            query['withPolicyConfigs'] = request.with_policy_configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHttpApis',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHttpApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_http_apis_with_options_async(
        self,
        request: main_models.ListHttpApisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListHttpApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.types):
            query['types'] = request.types
        if not DaraCore.is_null(request.with_apis_published_to_environment):
            query['withAPIsPublishedToEnvironment'] = request.with_apis_published_to_environment
        if not DaraCore.is_null(request.with_auth_policy_in_environment_id):
            query['withAuthPolicyInEnvironmentId'] = request.with_auth_policy_in_environment_id
        if not DaraCore.is_null(request.with_auth_policy_list):
            query['withAuthPolicyList'] = request.with_auth_policy_list
        if not DaraCore.is_null(request.with_consumer_info_by_id):
            query['withConsumerInfoById'] = request.with_consumer_info_by_id
        if not DaraCore.is_null(request.with_environment_info):
            query['withEnvironmentInfo'] = request.with_environment_info
        if not DaraCore.is_null(request.with_environment_info_by_id):
            query['withEnvironmentInfoById'] = request.with_environment_info_by_id
        if not DaraCore.is_null(request.with_ingress_info):
            query['withIngressInfo'] = request.with_ingress_info
        if not DaraCore.is_null(request.with_plugin_attachment_by_plugin_id):
            query['withPluginAttachmentByPluginId'] = request.with_plugin_attachment_by_plugin_id
        if not DaraCore.is_null(request.with_policy_configs):
            query['withPolicyConfigs'] = request.with_policy_configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHttpApis',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHttpApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_http_apis(
        self,
        request: main_models.ListHttpApisRequest,
    ) -> main_models.ListHttpApisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_http_apis_with_options(request, headers, runtime)

    async def list_http_apis_async(
        self,
        request: main_models.ListHttpApisRequest,
    ) -> main_models.ListHttpApisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_http_apis_with_options_async(request, headers, runtime)

    def list_mcp_servers_with_options(
        self,
        request: main_models.ListMcpServersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMcpServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_from_types):
            query['createFromTypes'] = request.create_from_types
        if not DaraCore.is_null(request.deploy_statuses):
            query['deployStatuses'] = request.deploy_statuses
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMcpServers',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcpServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcp_servers_with_options_async(
        self,
        request: main_models.ListMcpServersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMcpServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_from_types):
            query['createFromTypes'] = request.create_from_types
        if not DaraCore.is_null(request.deploy_statuses):
            query['deployStatuses'] = request.deploy_statuses
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMcpServers',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcpServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcp_servers(
        self,
        request: main_models.ListMcpServersRequest,
    ) -> main_models.ListMcpServersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_mcp_servers_with_options(request, headers, runtime)

    async def list_mcp_servers_async(
        self,
        request: main_models.ListMcpServersRequest,
    ) -> main_models.ListMcpServersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_mcp_servers_with_options_async(request, headers, runtime)

    def list_plugin_attachments_with_options(
        self,
        request: main_models.ListPluginAttachmentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPluginAttachmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not DaraCore.is_null(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.attach_resource_types):
            query['attachResourceTypes'] = request.attach_resource_types
        if not DaraCore.is_null(request.environment_id):
            query['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.plugin_id):
            query['pluginId'] = request.plugin_id
        if not DaraCore.is_null(request.with_parent_resource):
            query['withParentResource'] = request.with_parent_resource
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPluginAttachments',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-attachments',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPluginAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_plugin_attachments_with_options_async(
        self,
        request: main_models.ListPluginAttachmentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPluginAttachmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not DaraCore.is_null(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.attach_resource_types):
            query['attachResourceTypes'] = request.attach_resource_types
        if not DaraCore.is_null(request.environment_id):
            query['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.plugin_id):
            query['pluginId'] = request.plugin_id
        if not DaraCore.is_null(request.with_parent_resource):
            query['withParentResource'] = request.with_parent_resource
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPluginAttachments',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-attachments',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPluginAttachmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_plugin_attachments(
        self,
        request: main_models.ListPluginAttachmentsRequest,
    ) -> main_models.ListPluginAttachmentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_plugin_attachments_with_options(request, headers, runtime)

    async def list_plugin_attachments_async(
        self,
        request: main_models.ListPluginAttachmentsRequest,
    ) -> main_models.ListPluginAttachmentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_plugin_attachments_with_options_async(request, headers, runtime)

    def list_plugins_with_options(
        self,
        request: main_models.ListPluginsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPluginsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not DaraCore.is_null(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.include_builtin_ai_gateway):
            query['includeBuiltinAiGateway'] = request.include_builtin_ai_gateway
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.plugin_class_id):
            query['pluginClassId'] = request.plugin_class_id
        if not DaraCore.is_null(request.plugin_class_name):
            query['pluginClassName'] = request.plugin_class_name
        if not DaraCore.is_null(request.with_attachment_info):
            query['withAttachmentInfo'] = request.with_attachment_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPlugins',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugins',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPluginsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_plugins_with_options_async(
        self,
        request: main_models.ListPluginsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPluginsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not DaraCore.is_null(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.include_builtin_ai_gateway):
            query['includeBuiltinAiGateway'] = request.include_builtin_ai_gateway
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.plugin_class_id):
            query['pluginClassId'] = request.plugin_class_id
        if not DaraCore.is_null(request.plugin_class_name):
            query['pluginClassName'] = request.plugin_class_name
        if not DaraCore.is_null(request.with_attachment_info):
            query['withAttachmentInfo'] = request.with_attachment_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPlugins',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugins',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPluginsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_plugins(
        self,
        request: main_models.ListPluginsRequest,
    ) -> main_models.ListPluginsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_plugins_with_options(request, headers, runtime)

    async def list_plugins_async(
        self,
        request: main_models.ListPluginsRequest,
    ) -> main_models.ListPluginsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_plugins_with_options_async(request, headers, runtime)

    def list_policies_with_options(
        self,
        request: main_models.ListPoliciesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not DaraCore.is_null(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.environment_id):
            query['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.with_attachments):
            query['withAttachments'] = request.with_attachments
        if not DaraCore.is_null(request.with_system_policy):
            query['withSystemPolicy'] = request.with_system_policy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicies',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policies',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_with_options_async(
        self,
        request: main_models.ListPoliciesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not DaraCore.is_null(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.environment_id):
            query['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.with_attachments):
            query['withAttachments'] = request.with_attachments
        if not DaraCore.is_null(request.with_system_policy):
            query['withSystemPolicy'] = request.with_system_policy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicies',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policies',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.list_policies_with_options(request, headers, runtime)

    async def list_policies_async(
        self,
        request: main_models.ListPoliciesRequest,
    ) -> main_models.ListPoliciesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_policies_with_options_async(request, headers, runtime)

    def list_policy_classes_with_options(
        self,
        request: main_models.ListPolicyClassesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicyClassesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not DaraCore.is_null(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.direction):
            query['direction'] = request.direction
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicyClasses',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policy-classes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPolicyClassesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policy_classes_with_options_async(
        self,
        request: main_models.ListPolicyClassesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicyClassesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not DaraCore.is_null(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.direction):
            query['direction'] = request.direction
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicyClasses',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policy-classes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPolicyClassesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policy_classes(
        self,
        request: main_models.ListPolicyClassesRequest,
    ) -> main_models.ListPolicyClassesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_policy_classes_with_options(request, headers, runtime)

    async def list_policy_classes_async(
        self,
        request: main_models.ListPolicyClassesRequest,
    ) -> main_models.ListPolicyClassesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_policy_classes_with_options_async(request, headers, runtime)

    def list_services_with_options(
        self,
        request: main_models.ListServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_type):
            query['sourceType'] = request.source_type
        if not DaraCore.is_null(request.source_types):
            query['sourceTypes'] = request.source_types
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServices',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services',
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
        request: main_models.ListServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_type):
            query['sourceType'] = request.source_type
        if not DaraCore.is_null(request.source_types):
            query['sourceTypes'] = request.source_types
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServices',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services',
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
        request: main_models.ListServicesRequest,
    ) -> main_models.ListServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_services_with_options(request, headers, runtime)

    async def list_services_async(
        self,
        request: main_models.ListServicesRequest,
    ) -> main_models.ListServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_services_with_options_async(request, headers, runtime)

    def list_ssl_certs_with_options(
        self,
        request: main_models.ListSslCertsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSslCertsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_name_like):
            query['certNameLike'] = request.cert_name_like
        if not DaraCore.is_null(request.domain_name):
            query['domainName'] = request.domain_name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSslCerts',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ssl/certs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSslCertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ssl_certs_with_options_async(
        self,
        request: main_models.ListSslCertsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSslCertsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_name_like):
            query['certNameLike'] = request.cert_name_like
        if not DaraCore.is_null(request.domain_name):
            query['domainName'] = request.domain_name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSslCerts',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ssl/certs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.list_ssl_certs_with_options(request, headers, runtime)

    async def list_ssl_certs_async(
        self,
        request: main_models.ListSslCertsRequest,
    ) -> main_models.ListSslCertsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_ssl_certs_with_options_async(request, headers, runtime)

    def list_zones_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListZonesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListZones',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/zones',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_zones_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListZonesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListZones',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/zones',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_zones(self) -> main_models.ListZonesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_zones_with_options(headers, runtime)

    async def list_zones_async(self) -> main_models.ListZonesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_zones_with_options_async(headers, runtime)

    def query_consumer_authorization_rules_with_options(
        self,
        request: main_models.QueryConsumerAuthorizationRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryConsumerAuthorizationRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name_like):
            query['apiNameLike'] = request.api_name_like
        if not DaraCore.is_null(request.consumer_id):
            query['consumerId'] = request.consumer_id
        if not DaraCore.is_null(request.consumer_name_like):
            query['consumerNameLike'] = request.consumer_name_like
        if not DaraCore.is_null(request.environment_id):
            query['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.group_by_api):
            query['groupByApi'] = request.group_by_api
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_resource_id):
            query['parentResourceId'] = request.parent_resource_id
        if not DaraCore.is_null(request.resource_id):
            query['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.resource_types):
            query['resourceTypes'] = request.resource_types
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryConsumerAuthorizationRules',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/authorization-rules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryConsumerAuthorizationRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_consumer_authorization_rules_with_options_async(
        self,
        request: main_models.QueryConsumerAuthorizationRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryConsumerAuthorizationRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name_like):
            query['apiNameLike'] = request.api_name_like
        if not DaraCore.is_null(request.consumer_id):
            query['consumerId'] = request.consumer_id
        if not DaraCore.is_null(request.consumer_name_like):
            query['consumerNameLike'] = request.consumer_name_like
        if not DaraCore.is_null(request.environment_id):
            query['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.group_by_api):
            query['groupByApi'] = request.group_by_api
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_resource_id):
            query['parentResourceId'] = request.parent_resource_id
        if not DaraCore.is_null(request.resource_id):
            query['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.resource_types):
            query['resourceTypes'] = request.resource_types
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryConsumerAuthorizationRules',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/authorization-rules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryConsumerAuthorizationRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_consumer_authorization_rules(
        self,
        request: main_models.QueryConsumerAuthorizationRulesRequest,
    ) -> main_models.QueryConsumerAuthorizationRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_consumer_authorization_rules_with_options(request, headers, runtime)

    async def query_consumer_authorization_rules_async(
        self,
        request: main_models.QueryConsumerAuthorizationRulesRequest,
    ) -> main_models.QueryConsumerAuthorizationRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_consumer_authorization_rules_with_options_async(request, headers, runtime)

    def remove_consumer_authorization_rule_with_options(
        self,
        consumer_authorization_rule_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveConsumerAuthorizationRuleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/authorization-rules/{DaraURL.percent_encode(consumer_authorization_rule_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveConsumerAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_consumer_authorization_rule_with_options_async(
        self,
        consumer_authorization_rule_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveConsumerAuthorizationRuleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/authorization-rules/{DaraURL.percent_encode(consumer_authorization_rule_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveConsumerAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_consumer_authorization_rule(
        self,
        consumer_authorization_rule_id: str,
    ) -> main_models.RemoveConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_consumer_authorization_rule_with_options(consumer_authorization_rule_id, headers, runtime)

    async def remove_consumer_authorization_rule_async(
        self,
        consumer_authorization_rule_id: str,
    ) -> main_models.RemoveConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_consumer_authorization_rule_with_options_async(consumer_authorization_rule_id, headers, runtime)

    def restart_gateway_with_options(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartGatewayResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RestartGateway',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/restart',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_gateway_with_options_async(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartGatewayResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RestartGateway',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/restart',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_gateway(
        self,
        gateway_id: str,
    ) -> main_models.RestartGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.restart_gateway_with_options(gateway_id, headers, runtime)

    async def restart_gateway_async(
        self,
        gateway_id: str,
    ) -> main_models.RestartGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.restart_gateway_with_options_async(gateway_id, headers, runtime)

    def sync_mcpservers_with_options(
        self,
        request: main_models.SyncMCPServersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SyncMCPServersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.nacos_mcp_servers):
            body['nacosMcpServers'] = request.nacos_mcp_servers
        if not DaraCore.is_null(request.namespace):
            body['namespace'] = request.namespace
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SyncMCPServers',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/sync-mcp-server',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncMCPServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_mcpservers_with_options_async(
        self,
        request: main_models.SyncMCPServersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SyncMCPServersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.nacos_mcp_servers):
            body['nacosMcpServers'] = request.nacos_mcp_servers
        if not DaraCore.is_null(request.namespace):
            body['namespace'] = request.namespace
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SyncMCPServers',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/sync-mcp-server',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncMCPServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_mcpservers(
        self,
        request: main_models.SyncMCPServersRequest,
    ) -> main_models.SyncMCPServersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.sync_mcpservers_with_options(request, headers, runtime)

    async def sync_mcpservers_async(
        self,
        request: main_models.SyncMCPServersRequest,
    ) -> main_models.SyncMCPServersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.sync_mcpservers_with_options_async(request, headers, runtime)

    def un_deploy_mcp_server_with_options(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnDeployMcpServerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'UnDeployMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}/undeploy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnDeployMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_deploy_mcp_server_with_options_async(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnDeployMcpServerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'UnDeployMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}/undeploy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnDeployMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_deploy_mcp_server(
        self,
        mcp_server_id: str,
    ) -> main_models.UnDeployMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.un_deploy_mcp_server_with_options(mcp_server_id, headers, runtime)

    async def un_deploy_mcp_server_async(
        self,
        mcp_server_id: str,
    ) -> main_models.UnDeployMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.un_deploy_mcp_server_with_options_async(mcp_server_id, headers, runtime)

    def undeploy_http_api_with_options(
        self,
        http_api_id: str,
        request: main_models.UndeployHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UndeployHttpApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.operation_id):
            body['operationId'] = request.operation_id
        if not DaraCore.is_null(request.route_id):
            body['routeId'] = request.route_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UndeployHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/undeploy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UndeployHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def undeploy_http_api_with_options_async(
        self,
        http_api_id: str,
        request: main_models.UndeployHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UndeployHttpApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.operation_id):
            body['operationId'] = request.operation_id
        if not DaraCore.is_null(request.route_id):
            body['routeId'] = request.route_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UndeployHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/undeploy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UndeployHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def undeploy_http_api(
        self,
        http_api_id: str,
        request: main_models.UndeployHttpApiRequest,
    ) -> main_models.UndeployHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.undeploy_http_api_with_options(http_api_id, request, headers, runtime)

    async def undeploy_http_api_async(
        self,
        http_api_id: str,
        request: main_models.UndeployHttpApiRequest,
    ) -> main_models.UndeployHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.undeploy_http_api_with_options_async(http_api_id, request, headers, runtime)

    def uninstall_plugin_with_options(
        self,
        plugin_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UninstallPluginResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'UninstallPlugin',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugins/{DaraURL.percent_encode(plugin_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallPluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_plugin_with_options_async(
        self,
        plugin_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UninstallPluginResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'UninstallPlugin',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugins/{DaraURL.percent_encode(plugin_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallPluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_plugin(
        self,
        plugin_id: str,
    ) -> main_models.UninstallPluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.uninstall_plugin_with_options(plugin_id, headers, runtime)

    async def uninstall_plugin_async(
        self,
        plugin_id: str,
    ) -> main_models.UninstallPluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.uninstall_plugin_with_options_async(plugin_id, headers, runtime)

    def update_and_attach_policy_with_options(
        self,
        policy_id: str,
        request: main_models.UpdateAndAttachPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAndAttachPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not DaraCore.is_null(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAndAttachPolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policies/{DaraURL.percent_encode(policy_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAndAttachPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_and_attach_policy_with_options_async(
        self,
        policy_id: str,
        request: main_models.UpdateAndAttachPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAndAttachPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not DaraCore.is_null(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAndAttachPolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policies/{DaraURL.percent_encode(policy_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAndAttachPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_and_attach_policy(
        self,
        policy_id: str,
        request: main_models.UpdateAndAttachPolicyRequest,
    ) -> main_models.UpdateAndAttachPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_and_attach_policy_with_options(policy_id, request, headers, runtime)

    async def update_and_attach_policy_async(
        self,
        policy_id: str,
        request: main_models.UpdateAndAttachPolicyRequest,
    ) -> main_models.UpdateAndAttachPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_and_attach_policy_with_options_async(policy_id, request, headers, runtime)

    def update_consumer_with_options(
        self,
        consumer_id: str,
        request: main_models.UpdateConsumerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConsumerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ak_sk_identity_configs):
            body['akSkIdentityConfigs'] = request.ak_sk_identity_configs
        if not DaraCore.is_null(request.apikey_identity_config):
            body['apikeyIdentityConfig'] = request.apikey_identity_config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.jwt_identity_config):
            body['jwtIdentityConfig'] = request.jwt_identity_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConsumer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConsumerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_consumer_with_options_async(
        self,
        consumer_id: str,
        request: main_models.UpdateConsumerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConsumerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ak_sk_identity_configs):
            body['akSkIdentityConfigs'] = request.ak_sk_identity_configs
        if not DaraCore.is_null(request.apikey_identity_config):
            body['apikeyIdentityConfig'] = request.apikey_identity_config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.jwt_identity_config):
            body['jwtIdentityConfig'] = request.jwt_identity_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConsumer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConsumerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_consumer(
        self,
        consumer_id: str,
        request: main_models.UpdateConsumerRequest,
    ) -> main_models.UpdateConsumerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_consumer_with_options(consumer_id, request, headers, runtime)

    async def update_consumer_async(
        self,
        consumer_id: str,
        request: main_models.UpdateConsumerRequest,
    ) -> main_models.UpdateConsumerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_consumer_with_options_async(consumer_id, request, headers, runtime)

    def update_consumer_authorization_rule_with_options(
        self,
        consumer_id: str,
        consumer_authorization_rule_id: str,
        request: main_models.UpdateConsumerAuthorizationRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConsumerAuthorizationRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.authorization_resource_infos):
            body['authorizationResourceInfos'] = request.authorization_resource_infos
        if not DaraCore.is_null(request.expire_mode):
            body['expireMode'] = request.expire_mode
        if not DaraCore.is_null(request.expire_timestamp):
            body['expireTimestamp'] = request.expire_timestamp
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}/authorization-rules/{DaraURL.percent_encode(consumer_authorization_rule_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConsumerAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_consumer_authorization_rule_with_options_async(
        self,
        consumer_id: str,
        consumer_authorization_rule_id: str,
        request: main_models.UpdateConsumerAuthorizationRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConsumerAuthorizationRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.authorization_resource_infos):
            body['authorizationResourceInfos'] = request.authorization_resource_infos
        if not DaraCore.is_null(request.expire_mode):
            body['expireMode'] = request.expire_mode
        if not DaraCore.is_null(request.expire_timestamp):
            body['expireTimestamp'] = request.expire_timestamp
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}/authorization-rules/{DaraURL.percent_encode(consumer_authorization_rule_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConsumerAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_consumer_authorization_rule(
        self,
        consumer_id: str,
        consumer_authorization_rule_id: str,
        request: main_models.UpdateConsumerAuthorizationRuleRequest,
    ) -> main_models.UpdateConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_consumer_authorization_rule_with_options(consumer_id, consumer_authorization_rule_id, request, headers, runtime)

    async def update_consumer_authorization_rule_async(
        self,
        consumer_id: str,
        consumer_authorization_rule_id: str,
        request: main_models.UpdateConsumerAuthorizationRuleRequest,
    ) -> main_models.UpdateConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_consumer_authorization_rule_with_options_async(consumer_id, consumer_authorization_rule_id, request, headers, runtime)

    def update_domain_with_options(
        self,
        domain_id: str,
        request: main_models.UpdateDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ca_cert_identifier):
            body['caCertIdentifier'] = request.ca_cert_identifier
        if not DaraCore.is_null(request.cert_identifier):
            body['certIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.client_cacert):
            body['clientCACert'] = request.client_cacert
        if not DaraCore.is_null(request.force_https):
            body['forceHttps'] = request.force_https
        if not DaraCore.is_null(request.http_2option):
            body['http2Option'] = request.http_2option
        if not DaraCore.is_null(request.m_tlsenabled):
            body['mTLSEnabled'] = request.m_tlsenabled
        if not DaraCore.is_null(request.protocol):
            body['protocol'] = request.protocol
        if not DaraCore.is_null(request.tls_cipher_suites_config):
            body['tlsCipherSuitesConfig'] = request.tls_cipher_suites_config
        if not DaraCore.is_null(request.tls_max):
            body['tlsMax'] = request.tls_max
        if not DaraCore.is_null(request.tls_min):
            body['tlsMin'] = request.tls_min
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomain',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/domains/{DaraURL.percent_encode(domain_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_domain_with_options_async(
        self,
        domain_id: str,
        request: main_models.UpdateDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ca_cert_identifier):
            body['caCertIdentifier'] = request.ca_cert_identifier
        if not DaraCore.is_null(request.cert_identifier):
            body['certIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.client_cacert):
            body['clientCACert'] = request.client_cacert
        if not DaraCore.is_null(request.force_https):
            body['forceHttps'] = request.force_https
        if not DaraCore.is_null(request.http_2option):
            body['http2Option'] = request.http_2option
        if not DaraCore.is_null(request.m_tlsenabled):
            body['mTLSEnabled'] = request.m_tlsenabled
        if not DaraCore.is_null(request.protocol):
            body['protocol'] = request.protocol
        if not DaraCore.is_null(request.tls_cipher_suites_config):
            body['tlsCipherSuitesConfig'] = request.tls_cipher_suites_config
        if not DaraCore.is_null(request.tls_max):
            body['tlsMax'] = request.tls_max
        if not DaraCore.is_null(request.tls_min):
            body['tlsMin'] = request.tls_min
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomain',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/domains/{DaraURL.percent_encode(domain_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_domain(
        self,
        domain_id: str,
        request: main_models.UpdateDomainRequest,
    ) -> main_models.UpdateDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_domain_with_options(domain_id, request, headers, runtime)

    async def update_domain_async(
        self,
        domain_id: str,
        request: main_models.UpdateDomainRequest,
    ) -> main_models.UpdateDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_domain_with_options_async(domain_id, request, headers, runtime)

    def update_environment_with_options(
        self,
        environment_id: str,
        request: main_models.UpdateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEnvironmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alias):
            body['alias'] = request.alias
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEnvironment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/environments/{DaraURL.percent_encode(environment_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_environment_with_options_async(
        self,
        environment_id: str,
        request: main_models.UpdateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEnvironmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alias):
            body['alias'] = request.alias
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEnvironment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/environments/{DaraURL.percent_encode(environment_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_environment(
        self,
        environment_id: str,
        request: main_models.UpdateEnvironmentRequest,
    ) -> main_models.UpdateEnvironmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_environment_with_options(environment_id, request, headers, runtime)

    async def update_environment_async(
        self,
        environment_id: str,
        request: main_models.UpdateEnvironmentRequest,
    ) -> main_models.UpdateEnvironmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_environment_with_options_async(environment_id, request, headers, runtime)

    def update_gateway_feature_with_options(
        self,
        gateway_id: str,
        name: str,
        request: main_models.UpdateGatewayFeatureRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayFeatureResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.value):
            body['value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayFeature',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/gateway-features/{DaraURL.percent_encode(name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_feature_with_options_async(
        self,
        gateway_id: str,
        name: str,
        request: main_models.UpdateGatewayFeatureRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayFeatureResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.value):
            body['value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayFeature',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/gateway-features/{DaraURL.percent_encode(name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_feature(
        self,
        gateway_id: str,
        name: str,
        request: main_models.UpdateGatewayFeatureRequest,
    ) -> main_models.UpdateGatewayFeatureResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_gateway_feature_with_options(gateway_id, name, request, headers, runtime)

    async def update_gateway_feature_async(
        self,
        gateway_id: str,
        name: str,
        request: main_models.UpdateGatewayFeatureRequest,
    ) -> main_models.UpdateGatewayFeatureResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_gateway_feature_with_options_async(gateway_id, name, request, headers, runtime)

    def update_gateway_name_with_options(
        self,
        gateway_id: str,
        request: main_models.UpdateGatewayNameRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayName',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/name',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_name_with_options_async(
        self,
        gateway_id: str,
        request: main_models.UpdateGatewayNameRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayName',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/name',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_name(
        self,
        gateway_id: str,
        request: main_models.UpdateGatewayNameRequest,
    ) -> main_models.UpdateGatewayNameResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_gateway_name_with_options(gateway_id, request, headers, runtime)

    async def update_gateway_name_async(
        self,
        gateway_id: str,
        request: main_models.UpdateGatewayNameRequest,
    ) -> main_models.UpdateGatewayNameResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_gateway_name_with_options_async(gateway_id, request, headers, runtime)

    def update_http_api_with_options(
        self,
        http_api_id: str,
        request: main_models.UpdateHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHttpApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_protocols):
            body['agentProtocols'] = request.agent_protocols
        if not DaraCore.is_null(request.ai_protocols):
            body['aiProtocols'] = request.ai_protocols
        if not DaraCore.is_null(request.auth_config):
            body['authConfig'] = request.auth_config
        if not DaraCore.is_null(request.base_path):
            body['basePath'] = request.base_path
        if not DaraCore.is_null(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.enable_auth):
            body['enableAuth'] = request.enable_auth
        if not DaraCore.is_null(request.first_byte_timeout):
            body['firstByteTimeout'] = request.first_byte_timeout
        if not DaraCore.is_null(request.ingress_config):
            body['ingressConfig'] = request.ingress_config
        if not DaraCore.is_null(request.only_change_config):
            body['onlyChangeConfig'] = request.only_change_config
        if not DaraCore.is_null(request.protocols):
            body['protocols'] = request.protocols
        if not DaraCore.is_null(request.remove_base_path_on_forward):
            body['removeBasePathOnForward'] = request.remove_base_path_on_forward
        if not DaraCore.is_null(request.version_config):
            body['versionConfig'] = request.version_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_http_api_with_options_async(
        self,
        http_api_id: str,
        request: main_models.UpdateHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHttpApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_protocols):
            body['agentProtocols'] = request.agent_protocols
        if not DaraCore.is_null(request.ai_protocols):
            body['aiProtocols'] = request.ai_protocols
        if not DaraCore.is_null(request.auth_config):
            body['authConfig'] = request.auth_config
        if not DaraCore.is_null(request.base_path):
            body['basePath'] = request.base_path
        if not DaraCore.is_null(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.enable_auth):
            body['enableAuth'] = request.enable_auth
        if not DaraCore.is_null(request.first_byte_timeout):
            body['firstByteTimeout'] = request.first_byte_timeout
        if not DaraCore.is_null(request.ingress_config):
            body['ingressConfig'] = request.ingress_config
        if not DaraCore.is_null(request.only_change_config):
            body['onlyChangeConfig'] = request.only_change_config
        if not DaraCore.is_null(request.protocols):
            body['protocols'] = request.protocols
        if not DaraCore.is_null(request.remove_base_path_on_forward):
            body['removeBasePathOnForward'] = request.remove_base_path_on_forward
        if not DaraCore.is_null(request.version_config):
            body['versionConfig'] = request.version_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_http_api(
        self,
        http_api_id: str,
        request: main_models.UpdateHttpApiRequest,
    ) -> main_models.UpdateHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_http_api_with_options(http_api_id, request, headers, runtime)

    async def update_http_api_async(
        self,
        http_api_id: str,
        request: main_models.UpdateHttpApiRequest,
    ) -> main_models.UpdateHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_http_api_with_options_async(http_api_id, request, headers, runtime)

    def update_http_api_operation_with_options(
        self,
        http_api_id: str,
        operation_id: str,
        request: main_models.UpdateHttpApiOperationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHttpApiOperationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.operation):
            body['operation'] = request.operation
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHttpApiOperation',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/operations/{DaraURL.percent_encode(operation_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHttpApiOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_http_api_operation_with_options_async(
        self,
        http_api_id: str,
        operation_id: str,
        request: main_models.UpdateHttpApiOperationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHttpApiOperationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.operation):
            body['operation'] = request.operation
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHttpApiOperation',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/operations/{DaraURL.percent_encode(operation_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHttpApiOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_http_api_operation(
        self,
        http_api_id: str,
        operation_id: str,
        request: main_models.UpdateHttpApiOperationRequest,
    ) -> main_models.UpdateHttpApiOperationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_http_api_operation_with_options(http_api_id, operation_id, request, headers, runtime)

    async def update_http_api_operation_async(
        self,
        http_api_id: str,
        operation_id: str,
        request: main_models.UpdateHttpApiOperationRequest,
    ) -> main_models.UpdateHttpApiOperationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_http_api_operation_with_options_async(http_api_id, operation_id, request, headers, runtime)

    def update_http_api_route_with_options(
        self,
        http_api_id: str,
        route_id: str,
        request: main_models.UpdateHttpApiRouteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHttpApiRouteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not DaraCore.is_null(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.match):
            body['match'] = request.match
        if not DaraCore.is_null(request.mcp_route_config):
            body['mcpRouteConfig'] = request.mcp_route_config
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHttpApiRoute',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/routes/{DaraURL.percent_encode(route_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHttpApiRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_http_api_route_with_options_async(
        self,
        http_api_id: str,
        route_id: str,
        request: main_models.UpdateHttpApiRouteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHttpApiRouteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not DaraCore.is_null(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.match):
            body['match'] = request.match
        if not DaraCore.is_null(request.mcp_route_config):
            body['mcpRouteConfig'] = request.mcp_route_config
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHttpApiRoute',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/routes/{DaraURL.percent_encode(route_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHttpApiRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_http_api_route(
        self,
        http_api_id: str,
        route_id: str,
        request: main_models.UpdateHttpApiRouteRequest,
    ) -> main_models.UpdateHttpApiRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_http_api_route_with_options(http_api_id, route_id, request, headers, runtime)

    async def update_http_api_route_async(
        self,
        http_api_id: str,
        route_id: str,
        request: main_models.UpdateHttpApiRouteRequest,
    ) -> main_models.UpdateHttpApiRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_http_api_route_with_options_async(http_api_id, route_id, request, headers, runtime)

    def update_mcp_server_with_options(
        self,
        mcp_server_id: str,
        request: main_models.UpdateMcpServerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMcpServerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.assembled_sources):
            body['assembledSources'] = request.assembled_sources
        if not DaraCore.is_null(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not DaraCore.is_null(request.create_from_type):
            body['createFromType'] = request.create_from_type
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not DaraCore.is_null(request.exposed_uri_path):
            body['exposedUriPath'] = request.exposed_uri_path
        if not DaraCore.is_null(request.gray_mcp_server_configs):
            body['grayMcpServerConfigs'] = request.gray_mcp_server_configs
        if not DaraCore.is_null(request.match):
            body['match'] = request.match
        if not DaraCore.is_null(request.mcp_statistics_enable):
            body['mcpStatisticsEnable'] = request.mcp_statistics_enable
        if not DaraCore.is_null(request.protocol):
            body['protocol'] = request.protocol
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mcp_server_with_options_async(
        self,
        mcp_server_id: str,
        request: main_models.UpdateMcpServerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMcpServerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.assembled_sources):
            body['assembledSources'] = request.assembled_sources
        if not DaraCore.is_null(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not DaraCore.is_null(request.create_from_type):
            body['createFromType'] = request.create_from_type
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not DaraCore.is_null(request.exposed_uri_path):
            body['exposedUriPath'] = request.exposed_uri_path
        if not DaraCore.is_null(request.gray_mcp_server_configs):
            body['grayMcpServerConfigs'] = request.gray_mcp_server_configs
        if not DaraCore.is_null(request.match):
            body['match'] = request.match
        if not DaraCore.is_null(request.mcp_statistics_enable):
            body['mcpStatisticsEnable'] = request.mcp_statistics_enable
        if not DaraCore.is_null(request.protocol):
            body['protocol'] = request.protocol
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mcp_server(
        self,
        mcp_server_id: str,
        request: main_models.UpdateMcpServerRequest,
    ) -> main_models.UpdateMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_mcp_server_with_options(mcp_server_id, request, headers, runtime)

    async def update_mcp_server_async(
        self,
        mcp_server_id: str,
        request: main_models.UpdateMcpServerRequest,
    ) -> main_models.UpdateMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_mcp_server_with_options_async(mcp_server_id, request, headers, runtime)

    def update_plugin_attachment_with_options(
        self,
        plugin_attachment_id: str,
        request: main_models.UpdatePluginAttachmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePluginAttachmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.plugin_config):
            body['pluginConfig'] = request.plugin_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePluginAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-attachments/{DaraURL.percent_encode(plugin_attachment_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePluginAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_plugin_attachment_with_options_async(
        self,
        plugin_attachment_id: str,
        request: main_models.UpdatePluginAttachmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePluginAttachmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.plugin_config):
            body['pluginConfig'] = request.plugin_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePluginAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-attachments/{DaraURL.percent_encode(plugin_attachment_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePluginAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_plugin_attachment(
        self,
        plugin_attachment_id: str,
        request: main_models.UpdatePluginAttachmentRequest,
    ) -> main_models.UpdatePluginAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_plugin_attachment_with_options(plugin_attachment_id, request, headers, runtime)

    async def update_plugin_attachment_async(
        self,
        plugin_attachment_id: str,
        request: main_models.UpdatePluginAttachmentRequest,
    ) -> main_models.UpdatePluginAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_plugin_attachment_with_options_async(plugin_attachment_id, request, headers, runtime)

    def update_policy_with_options(
        self,
        policy_id: str,
        request: main_models.UpdatePolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v2/policies/{DaraURL.percent_encode(policy_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_policy_with_options_async(
        self,
        policy_id: str,
        request: main_models.UpdatePolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v2/policies/{DaraURL.percent_encode(policy_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_policy(
        self,
        policy_id: str,
        request: main_models.UpdatePolicyRequest,
    ) -> main_models.UpdatePolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_policy_with_options(policy_id, request, headers, runtime)

    async def update_policy_async(
        self,
        policy_id: str,
        request: main_models.UpdatePolicyRequest,
    ) -> main_models.UpdatePolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_policy_with_options_async(policy_id, request, headers, runtime)

    def update_service_with_options(
        self,
        service_id: str,
        request: main_models.UpdateServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.addresses):
            body['addresses'] = request.addresses
        if not DaraCore.is_null(request.agent_service_config):
            body['agentServiceConfig'] = request.agent_service_config
        if not DaraCore.is_null(request.ai_service_config):
            body['aiServiceConfig'] = request.ai_service_config
        if not DaraCore.is_null(request.dns_servers):
            body['dnsServers'] = request.dns_servers
        if not DaraCore.is_null(request.health_check_config):
            body['healthCheckConfig'] = request.health_check_config
        if not DaraCore.is_null(request.healthy_panic_threshold):
            body['healthyPanicThreshold'] = request.healthy_panic_threshold
        if not DaraCore.is_null(request.outlier_detection_config):
            body['outlierDetectionConfig'] = request.outlier_detection_config
        if not DaraCore.is_null(request.ports):
            body['ports'] = request.ports
        if not DaraCore.is_null(request.protocol):
            body['protocol'] = request.protocol
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateService',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_with_options_async(
        self,
        service_id: str,
        request: main_models.UpdateServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.addresses):
            body['addresses'] = request.addresses
        if not DaraCore.is_null(request.agent_service_config):
            body['agentServiceConfig'] = request.agent_service_config
        if not DaraCore.is_null(request.ai_service_config):
            body['aiServiceConfig'] = request.ai_service_config
        if not DaraCore.is_null(request.dns_servers):
            body['dnsServers'] = request.dns_servers
        if not DaraCore.is_null(request.health_check_config):
            body['healthCheckConfig'] = request.health_check_config
        if not DaraCore.is_null(request.healthy_panic_threshold):
            body['healthyPanicThreshold'] = request.healthy_panic_threshold
        if not DaraCore.is_null(request.outlier_detection_config):
            body['outlierDetectionConfig'] = request.outlier_detection_config
        if not DaraCore.is_null(request.ports):
            body['ports'] = request.ports
        if not DaraCore.is_null(request.protocol):
            body['protocol'] = request.protocol
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateService',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service(
        self,
        service_id: str,
        request: main_models.UpdateServiceRequest,
    ) -> main_models.UpdateServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_service_with_options(service_id, request, headers, runtime)

    async def update_service_async(
        self,
        service_id: str,
        request: main_models.UpdateServiceRequest,
    ) -> main_models.UpdateServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_service_with_options_async(service_id, request, headers, runtime)

    def update_service_version_with_options(
        self,
        service_id: str,
        name: str,
        request: main_models.UpdateServiceVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceVersion',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}/versions/{DaraURL.percent_encode(name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_version_with_options_async(
        self,
        service_id: str,
        name: str,
        request: main_models.UpdateServiceVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceVersion',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}/versions/{DaraURL.percent_encode(name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_version(
        self,
        service_id: str,
        name: str,
        request: main_models.UpdateServiceVersionRequest,
    ) -> main_models.UpdateServiceVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_service_version_with_options(service_id, name, request, headers, runtime)

    async def update_service_version_async(
        self,
        service_id: str,
        name: str,
        request: main_models.UpdateServiceVersionRequest,
    ) -> main_models.UpdateServiceVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_service_version_with_options_async(service_id, name, request, headers, runtime)

    def upgrade_gateway_with_options(
        self,
        gateway_id: str,
        request: main_models.UpgradeGatewayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeGateway',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/upgrade',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_gateway_with_options_async(
        self,
        gateway_id: str,
        request: main_models.UpgradeGatewayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeGateway',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/upgrade',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_gateway(
        self,
        gateway_id: str,
        request: main_models.UpgradeGatewayRequest,
    ) -> main_models.UpgradeGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.upgrade_gateway_with_options(gateway_id, request, headers, runtime)

    async def upgrade_gateway_async(
        self,
        gateway_id: str,
        request: main_models.UpgradeGatewayRequest,
    ) -> main_models.UpgradeGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.upgrade_gateway_with_options_async(gateway_id, request, headers, runtime)
