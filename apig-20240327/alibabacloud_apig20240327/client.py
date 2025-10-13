# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_apig20240327 import models as apig20240327_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_gateway_security_group_rule_with_options(
        self,
        gateway_id: str,
        request: apig20240327_models.AddGatewaySecurityGroupRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.AddGatewaySecurityGroupRuleResponse:
        """
        @summary Authorize the security group for gateway to access services
        
        @param request: AddGatewaySecurityGroupRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddGatewaySecurityGroupRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.port_ranges):
            body['portRanges'] = request.port_ranges
        if not UtilClient.is_unset(request.security_group_id):
            body['securityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddGatewaySecurityGroupRule',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/security-group-rules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.AddGatewaySecurityGroupRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_gateway_security_group_rule_with_options_async(
        self,
        gateway_id: str,
        request: apig20240327_models.AddGatewaySecurityGroupRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.AddGatewaySecurityGroupRuleResponse:
        """
        @summary Authorize the security group for gateway to access services
        
        @param request: AddGatewaySecurityGroupRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddGatewaySecurityGroupRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.port_ranges):
            body['portRanges'] = request.port_ranges
        if not UtilClient.is_unset(request.security_group_id):
            body['securityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddGatewaySecurityGroupRule',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/security-group-rules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.AddGatewaySecurityGroupRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_gateway_security_group_rule(
        self,
        gateway_id: str,
        request: apig20240327_models.AddGatewaySecurityGroupRuleRequest,
    ) -> apig20240327_models.AddGatewaySecurityGroupRuleResponse:
        """
        @summary Authorize the security group for gateway to access services
        
        @param request: AddGatewaySecurityGroupRuleRequest
        @return: AddGatewaySecurityGroupRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_gateway_security_group_rule_with_options(gateway_id, request, headers, runtime)

    async def add_gateway_security_group_rule_async(
        self,
        gateway_id: str,
        request: apig20240327_models.AddGatewaySecurityGroupRuleRequest,
    ) -> apig20240327_models.AddGatewaySecurityGroupRuleResponse:
        """
        @summary Authorize the security group for gateway to access services
        
        @param request: AddGatewaySecurityGroupRuleRequest
        @return: AddGatewaySecurityGroupRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_gateway_security_group_rule_with_options_async(gateway_id, request, headers, runtime)

    def batch_delete_consumer_authorization_rule_with_options(
        self,
        request: apig20240327_models.BatchDeleteConsumerAuthorizationRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.BatchDeleteConsumerAuthorizationRuleResponse:
        """
        @summary Removes consumer authentication rules.
        
        @param request: BatchDeleteConsumerAuthorizationRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteConsumerAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_authorization_rule_ids):
            query['consumerAuthorizationRuleIds'] = request.consumer_authorization_rule_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteConsumerAuthorizationRule',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/authorization-rules',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.BatchDeleteConsumerAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_consumer_authorization_rule_with_options_async(
        self,
        request: apig20240327_models.BatchDeleteConsumerAuthorizationRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.BatchDeleteConsumerAuthorizationRuleResponse:
        """
        @summary Removes consumer authentication rules.
        
        @param request: BatchDeleteConsumerAuthorizationRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteConsumerAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_authorization_rule_ids):
            query['consumerAuthorizationRuleIds'] = request.consumer_authorization_rule_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteConsumerAuthorizationRule',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/authorization-rules',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.BatchDeleteConsumerAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_consumer_authorization_rule(
        self,
        request: apig20240327_models.BatchDeleteConsumerAuthorizationRuleRequest,
    ) -> apig20240327_models.BatchDeleteConsumerAuthorizationRuleResponse:
        """
        @summary Removes consumer authentication rules.
        
        @param request: BatchDeleteConsumerAuthorizationRuleRequest
        @return: BatchDeleteConsumerAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_delete_consumer_authorization_rule_with_options(request, headers, runtime)

    async def batch_delete_consumer_authorization_rule_async(
        self,
        request: apig20240327_models.BatchDeleteConsumerAuthorizationRuleRequest,
    ) -> apig20240327_models.BatchDeleteConsumerAuthorizationRuleResponse:
        """
        @summary Removes consumer authentication rules.
        
        @param request: BatchDeleteConsumerAuthorizationRuleRequest
        @return: BatchDeleteConsumerAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_delete_consumer_authorization_rule_with_options_async(request, headers, runtime)

    def change_resource_group_with_options(
        self,
        request: apig20240327_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ChangeResourceGroupResponse:
        """
        @summary Resource Group Transfer
        
        @param request: ChangeResourceGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/move-resource-group',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: apig20240327_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ChangeResourceGroupResponse:
        """
        @summary Resource Group Transfer
        
        @param request: ChangeResourceGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/move-resource-group',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: apig20240327_models.ChangeResourceGroupRequest,
    ) -> apig20240327_models.ChangeResourceGroupResponse:
        """
        @summary Resource Group Transfer
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.change_resource_group_with_options(request, headers, runtime)

    async def change_resource_group_async(
        self,
        request: apig20240327_models.ChangeResourceGroupRequest,
    ) -> apig20240327_models.ChangeResourceGroupResponse:
        """
        @summary Resource Group Transfer
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.change_resource_group_with_options_async(request, headers, runtime)

    def create_and_attach_policy_with_options(
        self,
        request: apig20240327_models.CreateAndAttachPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateAndAttachPolicyResponse:
        """
        @summary CreateAndAttachPolicy
        
        @param request: CreateAndAttachPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAndAttachPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not UtilClient.is_unset(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not UtilClient.is_unset(request.class_name):
            body['className'] = request.class_name
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.environment_id):
            body['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAndAttachPolicy',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/policies',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateAndAttachPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_and_attach_policy_with_options_async(
        self,
        request: apig20240327_models.CreateAndAttachPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateAndAttachPolicyResponse:
        """
        @summary CreateAndAttachPolicy
        
        @param request: CreateAndAttachPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAndAttachPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not UtilClient.is_unset(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not UtilClient.is_unset(request.class_name):
            body['className'] = request.class_name
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.environment_id):
            body['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAndAttachPolicy',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/policies',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateAndAttachPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_and_attach_policy(
        self,
        request: apig20240327_models.CreateAndAttachPolicyRequest,
    ) -> apig20240327_models.CreateAndAttachPolicyResponse:
        """
        @summary CreateAndAttachPolicy
        
        @param request: CreateAndAttachPolicyRequest
        @return: CreateAndAttachPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_and_attach_policy_with_options(request, headers, runtime)

    async def create_and_attach_policy_async(
        self,
        request: apig20240327_models.CreateAndAttachPolicyRequest,
    ) -> apig20240327_models.CreateAndAttachPolicyResponse:
        """
        @summary CreateAndAttachPolicy
        
        @param request: CreateAndAttachPolicyRequest
        @return: CreateAndAttachPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_and_attach_policy_with_options_async(request, headers, runtime)

    def create_consumer_with_options(
        self,
        request: apig20240327_models.CreateConsumerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateConsumerResponse:
        """
        @summary 创建消费者
        
        @param request: CreateConsumerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConsumerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_sk_identity_configs):
            body['akSkIdentityConfigs'] = request.ak_sk_identity_configs
        if not UtilClient.is_unset(request.apikey_identity_config):
            body['apikeyIdentityConfig'] = request.apikey_identity_config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        if not UtilClient.is_unset(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not UtilClient.is_unset(request.jwt_identity_config):
            body['jwtIdentityConfig'] = request.jwt_identity_config
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConsumer',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/consumers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateConsumerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_consumer_with_options_async(
        self,
        request: apig20240327_models.CreateConsumerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateConsumerResponse:
        """
        @summary 创建消费者
        
        @param request: CreateConsumerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConsumerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_sk_identity_configs):
            body['akSkIdentityConfigs'] = request.ak_sk_identity_configs
        if not UtilClient.is_unset(request.apikey_identity_config):
            body['apikeyIdentityConfig'] = request.apikey_identity_config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        if not UtilClient.is_unset(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not UtilClient.is_unset(request.jwt_identity_config):
            body['jwtIdentityConfig'] = request.jwt_identity_config
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConsumer',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/consumers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateConsumerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_consumer(
        self,
        request: apig20240327_models.CreateConsumerRequest,
    ) -> apig20240327_models.CreateConsumerResponse:
        """
        @summary 创建消费者
        
        @param request: CreateConsumerRequest
        @return: CreateConsumerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_consumer_with_options(request, headers, runtime)

    async def create_consumer_async(
        self,
        request: apig20240327_models.CreateConsumerRequest,
    ) -> apig20240327_models.CreateConsumerResponse:
        """
        @summary 创建消费者
        
        @param request: CreateConsumerRequest
        @return: CreateConsumerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_consumer_with_options_async(request, headers, runtime)

    def create_consumer_authorization_rule_with_options(
        self,
        consumer_id: str,
        request: apig20240327_models.CreateConsumerAuthorizationRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateConsumerAuthorizationRuleResponse:
        """
        @summary 创建消费者授权规则
        
        @param request: CreateConsumerAuthorizationRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConsumerAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authorization_resource_infos):
            body['authorizationResourceInfos'] = request.authorization_resource_infos
        if not UtilClient.is_unset(request.expire_mode):
            body['expireMode'] = request.expire_mode
        if not UtilClient.is_unset(request.expire_timestamp):
            body['expireTimestamp'] = request.expire_timestamp
        if not UtilClient.is_unset(request.parent_resource_type):
            body['parentResourceType'] = request.parent_resource_type
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConsumerAuthorizationRule',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/consumers/{OpenApiUtilClient.get_encode_param(consumer_id)}/authorization-rules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateConsumerAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_consumer_authorization_rule_with_options_async(
        self,
        consumer_id: str,
        request: apig20240327_models.CreateConsumerAuthorizationRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateConsumerAuthorizationRuleResponse:
        """
        @summary 创建消费者授权规则
        
        @param request: CreateConsumerAuthorizationRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConsumerAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authorization_resource_infos):
            body['authorizationResourceInfos'] = request.authorization_resource_infos
        if not UtilClient.is_unset(request.expire_mode):
            body['expireMode'] = request.expire_mode
        if not UtilClient.is_unset(request.expire_timestamp):
            body['expireTimestamp'] = request.expire_timestamp
        if not UtilClient.is_unset(request.parent_resource_type):
            body['parentResourceType'] = request.parent_resource_type
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConsumerAuthorizationRule',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/consumers/{OpenApiUtilClient.get_encode_param(consumer_id)}/authorization-rules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateConsumerAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_consumer_authorization_rule(
        self,
        consumer_id: str,
        request: apig20240327_models.CreateConsumerAuthorizationRuleRequest,
    ) -> apig20240327_models.CreateConsumerAuthorizationRuleResponse:
        """
        @summary 创建消费者授权规则
        
        @param request: CreateConsumerAuthorizationRuleRequest
        @return: CreateConsumerAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_consumer_authorization_rule_with_options(consumer_id, request, headers, runtime)

    async def create_consumer_authorization_rule_async(
        self,
        consumer_id: str,
        request: apig20240327_models.CreateConsumerAuthorizationRuleRequest,
    ) -> apig20240327_models.CreateConsumerAuthorizationRuleResponse:
        """
        @summary 创建消费者授权规则
        
        @param request: CreateConsumerAuthorizationRuleRequest
        @return: CreateConsumerAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_consumer_authorization_rule_with_options_async(consumer_id, request, headers, runtime)

    def create_consumer_authorization_rules_with_options(
        self,
        request: apig20240327_models.CreateConsumerAuthorizationRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateConsumerAuthorizationRulesResponse:
        """
        @summary Creates a consumer authentication rule.
        
        @param request: CreateConsumerAuthorizationRulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConsumerAuthorizationRulesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authorization_rules):
            body['authorizationRules'] = request.authorization_rules
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConsumerAuthorizationRules',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/authorization-rules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateConsumerAuthorizationRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_consumer_authorization_rules_with_options_async(
        self,
        request: apig20240327_models.CreateConsumerAuthorizationRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateConsumerAuthorizationRulesResponse:
        """
        @summary Creates a consumer authentication rule.
        
        @param request: CreateConsumerAuthorizationRulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConsumerAuthorizationRulesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authorization_rules):
            body['authorizationRules'] = request.authorization_rules
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConsumerAuthorizationRules',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/authorization-rules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateConsumerAuthorizationRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_consumer_authorization_rules(
        self,
        request: apig20240327_models.CreateConsumerAuthorizationRulesRequest,
    ) -> apig20240327_models.CreateConsumerAuthorizationRulesResponse:
        """
        @summary Creates a consumer authentication rule.
        
        @param request: CreateConsumerAuthorizationRulesRequest
        @return: CreateConsumerAuthorizationRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_consumer_authorization_rules_with_options(request, headers, runtime)

    async def create_consumer_authorization_rules_async(
        self,
        request: apig20240327_models.CreateConsumerAuthorizationRulesRequest,
    ) -> apig20240327_models.CreateConsumerAuthorizationRulesResponse:
        """
        @summary Creates a consumer authentication rule.
        
        @param request: CreateConsumerAuthorizationRulesRequest
        @return: CreateConsumerAuthorizationRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_consumer_authorization_rules_with_options_async(request, headers, runtime)

    def create_domain_with_options(
        self,
        request: apig20240327_models.CreateDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateDomainResponse:
        """
        @summary Creates a domain name.
        
        @description Create Domain.
        
        @param request: CreateDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ca_cert_identifier):
            body['caCertIdentifier'] = request.ca_cert_identifier
        if not UtilClient.is_unset(request.cert_identifier):
            body['certIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.client_cacert):
            body['clientCACert'] = request.client_cacert
        if not UtilClient.is_unset(request.force_https):
            body['forceHttps'] = request.force_https
        if not UtilClient.is_unset(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not UtilClient.is_unset(request.http_2option):
            body['http2Option'] = request.http_2option
        if not UtilClient.is_unset(request.m_tlsenabled):
            body['mTLSEnabled'] = request.m_tlsenabled
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.protocol):
            body['protocol'] = request.protocol
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tls_cipher_suites_config):
            body['tlsCipherSuitesConfig'] = request.tls_cipher_suites_config
        if not UtilClient.is_unset(request.tls_max):
            body['tlsMax'] = request.tls_max
        if not UtilClient.is_unset(request.tls_min):
            body['tlsMin'] = request.tls_min
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/domains',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_domain_with_options_async(
        self,
        request: apig20240327_models.CreateDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateDomainResponse:
        """
        @summary Creates a domain name.
        
        @description Create Domain.
        
        @param request: CreateDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ca_cert_identifier):
            body['caCertIdentifier'] = request.ca_cert_identifier
        if not UtilClient.is_unset(request.cert_identifier):
            body['certIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.client_cacert):
            body['clientCACert'] = request.client_cacert
        if not UtilClient.is_unset(request.force_https):
            body['forceHttps'] = request.force_https
        if not UtilClient.is_unset(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not UtilClient.is_unset(request.http_2option):
            body['http2Option'] = request.http_2option
        if not UtilClient.is_unset(request.m_tlsenabled):
            body['mTLSEnabled'] = request.m_tlsenabled
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.protocol):
            body['protocol'] = request.protocol
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tls_cipher_suites_config):
            body['tlsCipherSuitesConfig'] = request.tls_cipher_suites_config
        if not UtilClient.is_unset(request.tls_max):
            body['tlsMax'] = request.tls_max
        if not UtilClient.is_unset(request.tls_min):
            body['tlsMin'] = request.tls_min
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/domains',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_domain(
        self,
        request: apig20240327_models.CreateDomainRequest,
    ) -> apig20240327_models.CreateDomainResponse:
        """
        @summary Creates a domain name.
        
        @description Create Domain.
        
        @param request: CreateDomainRequest
        @return: CreateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_domain_with_options(request, headers, runtime)

    async def create_domain_async(
        self,
        request: apig20240327_models.CreateDomainRequest,
    ) -> apig20240327_models.CreateDomainResponse:
        """
        @summary Creates a domain name.
        
        @description Create Domain.
        
        @param request: CreateDomainRequest
        @return: CreateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_domain_with_options_async(request, headers, runtime)

    def create_environment_with_options(
        self,
        request: apig20240327_models.CreateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateEnvironmentResponse:
        """
        @deprecated OpenAPI CreateEnvironment is deprecated
        
        @summary CreateEnvironment
        
        @description Create environment.
        
        @param request: CreateEnvironmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEnvironmentResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['alias'] = request.alias
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEnvironment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/environments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_environment_with_options_async(
        self,
        request: apig20240327_models.CreateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateEnvironmentResponse:
        """
        @deprecated OpenAPI CreateEnvironment is deprecated
        
        @summary CreateEnvironment
        
        @description Create environment.
        
        @param request: CreateEnvironmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEnvironmentResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['alias'] = request.alias
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEnvironment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/environments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_environment(
        self,
        request: apig20240327_models.CreateEnvironmentRequest,
    ) -> apig20240327_models.CreateEnvironmentResponse:
        """
        @deprecated OpenAPI CreateEnvironment is deprecated
        
        @summary CreateEnvironment
        
        @description Create environment.
        
        @param request: CreateEnvironmentRequest
        @return: CreateEnvironmentResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_environment_with_options(request, headers, runtime)

    async def create_environment_async(
        self,
        request: apig20240327_models.CreateEnvironmentRequest,
    ) -> apig20240327_models.CreateEnvironmentResponse:
        """
        @deprecated OpenAPI CreateEnvironment is deprecated
        
        @summary CreateEnvironment
        
        @description Create environment.
        
        @param request: CreateEnvironmentRequest
        @return: CreateEnvironmentResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_environment_with_options_async(request, headers, runtime)

    def create_gateway_with_options(
        self,
        request: apig20240327_models.CreateGatewayRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateGatewayResponse:
        """
        @summary 创建云原生网关
        
        @param request: CreateGatewayRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGatewayResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.charge_type):
            body['chargeType'] = request.charge_type
        if not UtilClient.is_unset(request.gateway_edition):
            body['gatewayEdition'] = request.gateway_edition
        if not UtilClient.is_unset(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not UtilClient.is_unset(request.log_config):
            body['logConfig'] = request.log_config
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.network_access_config):
            body['networkAccessConfig'] = request.network_access_config
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.spec):
            body['spec'] = request.spec
        if not UtilClient.is_unset(request.tag):
            body['tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_config):
            body['zoneConfig'] = request.zone_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGateway',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_with_options_async(
        self,
        request: apig20240327_models.CreateGatewayRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateGatewayResponse:
        """
        @summary 创建云原生网关
        
        @param request: CreateGatewayRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGatewayResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.charge_type):
            body['chargeType'] = request.charge_type
        if not UtilClient.is_unset(request.gateway_edition):
            body['gatewayEdition'] = request.gateway_edition
        if not UtilClient.is_unset(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not UtilClient.is_unset(request.log_config):
            body['logConfig'] = request.log_config
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.network_access_config):
            body['networkAccessConfig'] = request.network_access_config
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.spec):
            body['spec'] = request.spec
        if not UtilClient.is_unset(request.tag):
            body['tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_config):
            body['zoneConfig'] = request.zone_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGateway',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway(
        self,
        request: apig20240327_models.CreateGatewayRequest,
    ) -> apig20240327_models.CreateGatewayResponse:
        """
        @summary 创建云原生网关
        
        @param request: CreateGatewayRequest
        @return: CreateGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_gateway_with_options(request, headers, runtime)

    async def create_gateway_async(
        self,
        request: apig20240327_models.CreateGatewayRequest,
    ) -> apig20240327_models.CreateGatewayResponse:
        """
        @summary 创建云原生网关
        
        @param request: CreateGatewayRequest
        @return: CreateGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_gateway_with_options_async(request, headers, runtime)

    def create_http_api_with_options(
        self,
        request: apig20240327_models.CreateHttpApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateHttpApiResponse:
        """
        @summary Creates an HTTP API.
        
        @param request: CreateHttpApiRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHttpApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_protocols):
            body['agentProtocols'] = request.agent_protocols
        if not UtilClient.is_unset(request.ai_protocols):
            body['aiProtocols'] = request.ai_protocols
        if not UtilClient.is_unset(request.auth_config):
            body['authConfig'] = request.auth_config
        if not UtilClient.is_unset(request.base_path):
            body['basePath'] = request.base_path
        if not UtilClient.is_unset(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.enable_auth):
            body['enableAuth'] = request.enable_auth
        if not UtilClient.is_unset(request.first_byte_timeout):
            body['firstByteTimeout'] = request.first_byte_timeout
        if not UtilClient.is_unset(request.ingress_config):
            body['ingressConfig'] = request.ingress_config
        if not UtilClient.is_unset(request.model_category):
            body['modelCategory'] = request.model_category
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.protocols):
            body['protocols'] = request.protocols
        if not UtilClient.is_unset(request.remove_base_path_on_forward):
            body['removeBasePathOnForward'] = request.remove_base_path_on_forward
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.version_config):
            body['versionConfig'] = request.version_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_http_api_with_options_async(
        self,
        request: apig20240327_models.CreateHttpApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateHttpApiResponse:
        """
        @summary Creates an HTTP API.
        
        @param request: CreateHttpApiRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHttpApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_protocols):
            body['agentProtocols'] = request.agent_protocols
        if not UtilClient.is_unset(request.ai_protocols):
            body['aiProtocols'] = request.ai_protocols
        if not UtilClient.is_unset(request.auth_config):
            body['authConfig'] = request.auth_config
        if not UtilClient.is_unset(request.base_path):
            body['basePath'] = request.base_path
        if not UtilClient.is_unset(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.enable_auth):
            body['enableAuth'] = request.enable_auth
        if not UtilClient.is_unset(request.first_byte_timeout):
            body['firstByteTimeout'] = request.first_byte_timeout
        if not UtilClient.is_unset(request.ingress_config):
            body['ingressConfig'] = request.ingress_config
        if not UtilClient.is_unset(request.model_category):
            body['modelCategory'] = request.model_category
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.protocols):
            body['protocols'] = request.protocols
        if not UtilClient.is_unset(request.remove_base_path_on_forward):
            body['removeBasePathOnForward'] = request.remove_base_path_on_forward
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.version_config):
            body['versionConfig'] = request.version_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_http_api(
        self,
        request: apig20240327_models.CreateHttpApiRequest,
    ) -> apig20240327_models.CreateHttpApiResponse:
        """
        @summary Creates an HTTP API.
        
        @param request: CreateHttpApiRequest
        @return: CreateHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_http_api_with_options(request, headers, runtime)

    async def create_http_api_async(
        self,
        request: apig20240327_models.CreateHttpApiRequest,
    ) -> apig20240327_models.CreateHttpApiResponse:
        """
        @summary Creates an HTTP API.
        
        @param request: CreateHttpApiRequest
        @return: CreateHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_http_api_with_options_async(request, headers, runtime)

    def create_http_api_operation_with_options(
        self,
        http_api_id: str,
        request: apig20240327_models.CreateHttpApiOperationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateHttpApiOperationResponse:
        """
        @summary Create an Operation for HTTP API
        
        @param request: CreateHttpApiOperationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHttpApiOperationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operations):
            body['operations'] = request.operations
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHttpApiOperation',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/operations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateHttpApiOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_http_api_operation_with_options_async(
        self,
        http_api_id: str,
        request: apig20240327_models.CreateHttpApiOperationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateHttpApiOperationResponse:
        """
        @summary Create an Operation for HTTP API
        
        @param request: CreateHttpApiOperationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHttpApiOperationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operations):
            body['operations'] = request.operations
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHttpApiOperation',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/operations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateHttpApiOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_http_api_operation(
        self,
        http_api_id: str,
        request: apig20240327_models.CreateHttpApiOperationRequest,
    ) -> apig20240327_models.CreateHttpApiOperationResponse:
        """
        @summary Create an Operation for HTTP API
        
        @param request: CreateHttpApiOperationRequest
        @return: CreateHttpApiOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_http_api_operation_with_options(http_api_id, request, headers, runtime)

    async def create_http_api_operation_async(
        self,
        http_api_id: str,
        request: apig20240327_models.CreateHttpApiOperationRequest,
    ) -> apig20240327_models.CreateHttpApiOperationResponse:
        """
        @summary Create an Operation for HTTP API
        
        @param request: CreateHttpApiOperationRequest
        @return: CreateHttpApiOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_http_api_operation_with_options_async(http_api_id, request, headers, runtime)

    def create_http_api_route_with_options(
        self,
        http_api_id: str,
        request: apig20240327_models.CreateHttpApiRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateHttpApiRouteResponse:
        """
        @summary Creates a route for an HTTP API.
        
        @param request: CreateHttpApiRouteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHttpApiRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not UtilClient.is_unset(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not UtilClient.is_unset(request.environment_id):
            body['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.match):
            body['match'] = request.match
        if not UtilClient.is_unset(request.mcp_route_config):
            body['mcpRouteConfig'] = request.mcp_route_config
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHttpApiRoute',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/routes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateHttpApiRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_http_api_route_with_options_async(
        self,
        http_api_id: str,
        request: apig20240327_models.CreateHttpApiRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateHttpApiRouteResponse:
        """
        @summary Creates a route for an HTTP API.
        
        @param request: CreateHttpApiRouteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHttpApiRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not UtilClient.is_unset(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not UtilClient.is_unset(request.environment_id):
            body['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.match):
            body['match'] = request.match
        if not UtilClient.is_unset(request.mcp_route_config):
            body['mcpRouteConfig'] = request.mcp_route_config
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHttpApiRoute',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/routes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateHttpApiRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_http_api_route(
        self,
        http_api_id: str,
        request: apig20240327_models.CreateHttpApiRouteRequest,
    ) -> apig20240327_models.CreateHttpApiRouteResponse:
        """
        @summary Creates a route for an HTTP API.
        
        @param request: CreateHttpApiRouteRequest
        @return: CreateHttpApiRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_http_api_route_with_options(http_api_id, request, headers, runtime)

    async def create_http_api_route_async(
        self,
        http_api_id: str,
        request: apig20240327_models.CreateHttpApiRouteRequest,
    ) -> apig20240327_models.CreateHttpApiRouteResponse:
        """
        @summary Creates a route for an HTTP API.
        
        @param request: CreateHttpApiRouteRequest
        @return: CreateHttpApiRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_http_api_route_with_options_async(http_api_id, request, headers, runtime)

    def create_mcp_server_with_options(
        self,
        request: apig20240327_models.CreateMcpServerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateMcpServerResponse:
        """
        @summary 创建MCP server
        
        @param request: CreateMcpServerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcpServerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assembled_sources):
            body['assembledSources'] = request.assembled_sources
        if not UtilClient.is_unset(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not UtilClient.is_unset(request.exposed_uri_path):
            body['exposedUriPath'] = request.exposed_uri_path
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.match):
            body['match'] = request.match
        if not UtilClient.is_unset(request.mcp_statistics_enable):
            body['mcpStatisticsEnable'] = request.mcp_statistics_enable
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.protocol):
            body['protocol'] = request.protocol
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcpServer',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/mcp-servers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcp_server_with_options_async(
        self,
        request: apig20240327_models.CreateMcpServerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateMcpServerResponse:
        """
        @summary 创建MCP server
        
        @param request: CreateMcpServerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcpServerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assembled_sources):
            body['assembledSources'] = request.assembled_sources
        if not UtilClient.is_unset(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not UtilClient.is_unset(request.exposed_uri_path):
            body['exposedUriPath'] = request.exposed_uri_path
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.match):
            body['match'] = request.match
        if not UtilClient.is_unset(request.mcp_statistics_enable):
            body['mcpStatisticsEnable'] = request.mcp_statistics_enable
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.protocol):
            body['protocol'] = request.protocol
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcpServer',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/mcp-servers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcp_server(
        self,
        request: apig20240327_models.CreateMcpServerRequest,
    ) -> apig20240327_models.CreateMcpServerResponse:
        """
        @summary 创建MCP server
        
        @param request: CreateMcpServerRequest
        @return: CreateMcpServerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_mcp_server_with_options(request, headers, runtime)

    async def create_mcp_server_async(
        self,
        request: apig20240327_models.CreateMcpServerRequest,
    ) -> apig20240327_models.CreateMcpServerResponse:
        """
        @summary 创建MCP server
        
        @param request: CreateMcpServerRequest
        @return: CreateMcpServerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_mcp_server_with_options_async(request, headers, runtime)

    def create_plugin_attachment_with_options(
        self,
        request: apig20240327_models.CreatePluginAttachmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreatePluginAttachmentResponse:
        """
        @summary 创建API
        
        @param request: CreatePluginAttachmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePluginAttachmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not UtilClient.is_unset(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        if not UtilClient.is_unset(request.environment_id):
            body['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.plugin_config):
            body['pluginConfig'] = request.plugin_config
        if not UtilClient.is_unset(request.plugin_id):
            body['pluginId'] = request.plugin_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePluginAttachment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/plugin-attachments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreatePluginAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_plugin_attachment_with_options_async(
        self,
        request: apig20240327_models.CreatePluginAttachmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreatePluginAttachmentResponse:
        """
        @summary 创建API
        
        @param request: CreatePluginAttachmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePluginAttachmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not UtilClient.is_unset(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        if not UtilClient.is_unset(request.environment_id):
            body['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.plugin_config):
            body['pluginConfig'] = request.plugin_config
        if not UtilClient.is_unset(request.plugin_id):
            body['pluginId'] = request.plugin_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePluginAttachment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/plugin-attachments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreatePluginAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_plugin_attachment(
        self,
        request: apig20240327_models.CreatePluginAttachmentRequest,
    ) -> apig20240327_models.CreatePluginAttachmentResponse:
        """
        @summary 创建API
        
        @param request: CreatePluginAttachmentRequest
        @return: CreatePluginAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_plugin_attachment_with_options(request, headers, runtime)

    async def create_plugin_attachment_async(
        self,
        request: apig20240327_models.CreatePluginAttachmentRequest,
    ) -> apig20240327_models.CreatePluginAttachmentResponse:
        """
        @summary 创建API
        
        @param request: CreatePluginAttachmentRequest
        @return: CreatePluginAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_plugin_attachment_with_options_async(request, headers, runtime)

    def create_policy_with_options(
        self,
        request: apig20240327_models.CreatePolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreatePolicyResponse:
        """
        @summary Create Policy
        
        @param request: CreatePolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.class_name):
            body['className'] = request.class_name
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePolicy',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v2/policies',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_with_options_async(
        self,
        request: apig20240327_models.CreatePolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreatePolicyResponse:
        """
        @summary Create Policy
        
        @param request: CreatePolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.class_name):
            body['className'] = request.class_name
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePolicy',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v2/policies',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy(
        self,
        request: apig20240327_models.CreatePolicyRequest,
    ) -> apig20240327_models.CreatePolicyResponse:
        """
        @summary Create Policy
        
        @param request: CreatePolicyRequest
        @return: CreatePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_policy_with_options(request, headers, runtime)

    async def create_policy_async(
        self,
        request: apig20240327_models.CreatePolicyRequest,
    ) -> apig20240327_models.CreatePolicyResponse:
        """
        @summary Create Policy
        
        @param request: CreatePolicyRequest
        @return: CreatePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_policy_with_options_async(request, headers, runtime)

    def create_policy_attachment_with_options(
        self,
        request: apig20240327_models.CreatePolicyAttachmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreatePolicyAttachmentResponse:
        """
        @summary Create policy resource mount
        
        @param request: CreatePolicyAttachmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyAttachmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attach_resource_id):
            body['attachResourceId'] = request.attach_resource_id
        if not UtilClient.is_unset(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not UtilClient.is_unset(request.environment_id):
            body['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.policy_id):
            body['policyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePolicyAttachment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/policy-attachments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreatePolicyAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_attachment_with_options_async(
        self,
        request: apig20240327_models.CreatePolicyAttachmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreatePolicyAttachmentResponse:
        """
        @summary Create policy resource mount
        
        @param request: CreatePolicyAttachmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyAttachmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attach_resource_id):
            body['attachResourceId'] = request.attach_resource_id
        if not UtilClient.is_unset(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not UtilClient.is_unset(request.environment_id):
            body['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.policy_id):
            body['policyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePolicyAttachment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/policy-attachments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreatePolicyAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy_attachment(
        self,
        request: apig20240327_models.CreatePolicyAttachmentRequest,
    ) -> apig20240327_models.CreatePolicyAttachmentResponse:
        """
        @summary Create policy resource mount
        
        @param request: CreatePolicyAttachmentRequest
        @return: CreatePolicyAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_policy_attachment_with_options(request, headers, runtime)

    async def create_policy_attachment_async(
        self,
        request: apig20240327_models.CreatePolicyAttachmentRequest,
    ) -> apig20240327_models.CreatePolicyAttachmentResponse:
        """
        @summary Create policy resource mount
        
        @param request: CreatePolicyAttachmentRequest
        @return: CreatePolicyAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_policy_attachment_with_options_async(request, headers, runtime)

    def create_service_with_options(
        self,
        request: apig20240327_models.CreateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateServiceResponse:
        """
        @summary Creates a service.
        
        @description You can call this operation to create multiple services at a time.
        
        @param request: CreateServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_configs):
            body['serviceConfigs'] = request.service_configs
        if not UtilClient.is_unset(request.source_type):
            body['sourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/services',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_with_options_async(
        self,
        request: apig20240327_models.CreateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.CreateServiceResponse:
        """
        @summary Creates a service.
        
        @description You can call this operation to create multiple services at a time.
        
        @param request: CreateServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_configs):
            body['serviceConfigs'] = request.service_configs
        if not UtilClient.is_unset(request.source_type):
            body['sourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/services',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.CreateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service(
        self,
        request: apig20240327_models.CreateServiceRequest,
    ) -> apig20240327_models.CreateServiceResponse:
        """
        @summary Creates a service.
        
        @description You can call this operation to create multiple services at a time.
        
        @param request: CreateServiceRequest
        @return: CreateServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_with_options(request, headers, runtime)

    async def create_service_async(
        self,
        request: apig20240327_models.CreateServiceRequest,
    ) -> apig20240327_models.CreateServiceResponse:
        """
        @summary Creates a service.
        
        @description You can call this operation to create multiple services at a time.
        
        @param request: CreateServiceRequest
        @return: CreateServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_with_options_async(request, headers, runtime)

    def delete_consumer_with_options(
        self,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteConsumerResponse:
        """
        @summary 删除消费者
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConsumerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteConsumer',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/consumers/{OpenApiUtilClient.get_encode_param(consumer_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteConsumerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_consumer_with_options_async(
        self,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteConsumerResponse:
        """
        @summary 删除消费者
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConsumerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteConsumer',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/consumers/{OpenApiUtilClient.get_encode_param(consumer_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteConsumerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_consumer(
        self,
        consumer_id: str,
    ) -> apig20240327_models.DeleteConsumerResponse:
        """
        @summary 删除消费者
        
        @return: DeleteConsumerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_consumer_with_options(consumer_id, headers, runtime)

    async def delete_consumer_async(
        self,
        consumer_id: str,
    ) -> apig20240327_models.DeleteConsumerResponse:
        """
        @summary 删除消费者
        
        @return: DeleteConsumerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_consumer_with_options_async(consumer_id, headers, runtime)

    def delete_consumer_authorization_rule_with_options(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteConsumerAuthorizationRuleResponse:
        """
        @summary 删除消费者授权规则
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConsumerAuthorizationRuleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteConsumerAuthorizationRule',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/consumers/{OpenApiUtilClient.get_encode_param(consumer_id)}/authorization-rules/{OpenApiUtilClient.get_encode_param(consumer_authorization_rule_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteConsumerAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_consumer_authorization_rule_with_options_async(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteConsumerAuthorizationRuleResponse:
        """
        @summary 删除消费者授权规则
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConsumerAuthorizationRuleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteConsumerAuthorizationRule',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/consumers/{OpenApiUtilClient.get_encode_param(consumer_id)}/authorization-rules/{OpenApiUtilClient.get_encode_param(consumer_authorization_rule_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteConsumerAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_consumer_authorization_rule(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
    ) -> apig20240327_models.DeleteConsumerAuthorizationRuleResponse:
        """
        @summary 删除消费者授权规则
        
        @return: DeleteConsumerAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_consumer_authorization_rule_with_options(consumer_authorization_rule_id, consumer_id, headers, runtime)

    async def delete_consumer_authorization_rule_async(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
    ) -> apig20240327_models.DeleteConsumerAuthorizationRuleResponse:
        """
        @summary 删除消费者授权规则
        
        @return: DeleteConsumerAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_consumer_authorization_rule_with_options_async(consumer_authorization_rule_id, consumer_id, headers, runtime)

    def delete_domain_with_options(
        self,
        domain_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteDomainResponse:
        """
        @summary DeleteDomain
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/domains/{OpenApiUtilClient.get_encode_param(domain_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        domain_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteDomainResponse:
        """
        @summary DeleteDomain
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/domains/{OpenApiUtilClient.get_encode_param(domain_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain(
        self,
        domain_id: str,
    ) -> apig20240327_models.DeleteDomainResponse:
        """
        @summary DeleteDomain
        
        @return: DeleteDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_domain_with_options(domain_id, headers, runtime)

    async def delete_domain_async(
        self,
        domain_id: str,
    ) -> apig20240327_models.DeleteDomainResponse:
        """
        @summary DeleteDomain
        
        @return: DeleteDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_domain_with_options_async(domain_id, headers, runtime)

    def delete_environment_with_options(
        self,
        environment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteEnvironmentResponse:
        """
        @deprecated OpenAPI DeleteEnvironment is deprecated
        
        @summary DeleteEnvironment
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEnvironmentResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEnvironment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/environments/{OpenApiUtilClient.get_encode_param(environment_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_environment_with_options_async(
        self,
        environment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteEnvironmentResponse:
        """
        @deprecated OpenAPI DeleteEnvironment is deprecated
        
        @summary DeleteEnvironment
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEnvironmentResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEnvironment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/environments/{OpenApiUtilClient.get_encode_param(environment_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_environment(
        self,
        environment_id: str,
    ) -> apig20240327_models.DeleteEnvironmentResponse:
        """
        @deprecated OpenAPI DeleteEnvironment is deprecated
        
        @summary DeleteEnvironment
        
        @return: DeleteEnvironmentResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_environment_with_options(environment_id, headers, runtime)

    async def delete_environment_async(
        self,
        environment_id: str,
    ) -> apig20240327_models.DeleteEnvironmentResponse:
        """
        @deprecated OpenAPI DeleteEnvironment is deprecated
        
        @summary DeleteEnvironment
        
        @return: DeleteEnvironmentResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_environment_with_options_async(environment_id, headers, runtime)

    def delete_gateway_with_options(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteGatewayResponse:
        """
        @summary Delete Gateway
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewayResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteGateway',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_with_options_async(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteGatewayResponse:
        """
        @summary Delete Gateway
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewayResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteGateway',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway(
        self,
        gateway_id: str,
    ) -> apig20240327_models.DeleteGatewayResponse:
        """
        @summary Delete Gateway
        
        @return: DeleteGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_gateway_with_options(gateway_id, headers, runtime)

    async def delete_gateway_async(
        self,
        gateway_id: str,
    ) -> apig20240327_models.DeleteGatewayResponse:
        """
        @summary Delete Gateway
        
        @return: DeleteGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_gateway_with_options_async(gateway_id, headers, runtime)

    def delete_gateway_security_group_rule_with_options(
        self,
        gateway_id: str,
        security_group_rule_id: str,
        request: apig20240327_models.DeleteGatewaySecurityGroupRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteGatewaySecurityGroupRuleResponse:
        """
        @summary Delete the security group rule of a gateway
        
        @param request: DeleteGatewaySecurityGroupRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewaySecurityGroupRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cascading_delete):
            query['cascadingDelete'] = request.cascading_delete
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGatewaySecurityGroupRule',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/security-group-rules/{OpenApiUtilClient.get_encode_param(security_group_rule_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteGatewaySecurityGroupRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_security_group_rule_with_options_async(
        self,
        gateway_id: str,
        security_group_rule_id: str,
        request: apig20240327_models.DeleteGatewaySecurityGroupRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteGatewaySecurityGroupRuleResponse:
        """
        @summary Delete the security group rule of a gateway
        
        @param request: DeleteGatewaySecurityGroupRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewaySecurityGroupRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cascading_delete):
            query['cascadingDelete'] = request.cascading_delete
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGatewaySecurityGroupRule',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/security-group-rules/{OpenApiUtilClient.get_encode_param(security_group_rule_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteGatewaySecurityGroupRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_security_group_rule(
        self,
        gateway_id: str,
        security_group_rule_id: str,
        request: apig20240327_models.DeleteGatewaySecurityGroupRuleRequest,
    ) -> apig20240327_models.DeleteGatewaySecurityGroupRuleResponse:
        """
        @summary Delete the security group rule of a gateway
        
        @param request: DeleteGatewaySecurityGroupRuleRequest
        @return: DeleteGatewaySecurityGroupRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_gateway_security_group_rule_with_options(gateway_id, security_group_rule_id, request, headers, runtime)

    async def delete_gateway_security_group_rule_async(
        self,
        gateway_id: str,
        security_group_rule_id: str,
        request: apig20240327_models.DeleteGatewaySecurityGroupRuleRequest,
    ) -> apig20240327_models.DeleteGatewaySecurityGroupRuleResponse:
        """
        @summary Delete the security group rule of a gateway
        
        @param request: DeleteGatewaySecurityGroupRuleRequest
        @return: DeleteGatewaySecurityGroupRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_gateway_security_group_rule_with_options_async(gateway_id, security_group_rule_id, request, headers, runtime)

    def delete_http_api_with_options(
        self,
        http_api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteHttpApiResponse:
        """
        @summary Deletes an HTTP API.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHttpApiResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_http_api_with_options_async(
        self,
        http_api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteHttpApiResponse:
        """
        @summary Deletes an HTTP API.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHttpApiResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_http_api(
        self,
        http_api_id: str,
    ) -> apig20240327_models.DeleteHttpApiResponse:
        """
        @summary Deletes an HTTP API.
        
        @return: DeleteHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_http_api_with_options(http_api_id, headers, runtime)

    async def delete_http_api_async(
        self,
        http_api_id: str,
    ) -> apig20240327_models.DeleteHttpApiResponse:
        """
        @summary Deletes an HTTP API.
        
        @return: DeleteHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_http_api_with_options_async(http_api_id, headers, runtime)

    def delete_http_api_operation_with_options(
        self,
        http_api_id: str,
        operation_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteHttpApiOperationResponse:
        """
        @summary Delete Operation
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHttpApiOperationResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteHttpApiOperation',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/operations/{OpenApiUtilClient.get_encode_param(operation_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteHttpApiOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_http_api_operation_with_options_async(
        self,
        http_api_id: str,
        operation_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteHttpApiOperationResponse:
        """
        @summary Delete Operation
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHttpApiOperationResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteHttpApiOperation',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/operations/{OpenApiUtilClient.get_encode_param(operation_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteHttpApiOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_http_api_operation(
        self,
        http_api_id: str,
        operation_id: str,
    ) -> apig20240327_models.DeleteHttpApiOperationResponse:
        """
        @summary Delete Operation
        
        @return: DeleteHttpApiOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_http_api_operation_with_options(http_api_id, operation_id, headers, runtime)

    async def delete_http_api_operation_async(
        self,
        http_api_id: str,
        operation_id: str,
    ) -> apig20240327_models.DeleteHttpApiOperationResponse:
        """
        @summary Delete Operation
        
        @return: DeleteHttpApiOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_http_api_operation_with_options_async(http_api_id, operation_id, headers, runtime)

    def delete_http_api_route_with_options(
        self,
        http_api_id: str,
        route_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteHttpApiRouteResponse:
        """
        @summary Delete the route of an HttpApi
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHttpApiRouteResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteHttpApiRoute',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/routes/{OpenApiUtilClient.get_encode_param(route_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteHttpApiRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_http_api_route_with_options_async(
        self,
        http_api_id: str,
        route_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteHttpApiRouteResponse:
        """
        @summary Delete the route of an HttpApi
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHttpApiRouteResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteHttpApiRoute',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/routes/{OpenApiUtilClient.get_encode_param(route_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteHttpApiRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_http_api_route(
        self,
        http_api_id: str,
        route_id: str,
    ) -> apig20240327_models.DeleteHttpApiRouteResponse:
        """
        @summary Delete the route of an HttpApi
        
        @return: DeleteHttpApiRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_http_api_route_with_options(http_api_id, route_id, headers, runtime)

    async def delete_http_api_route_async(
        self,
        http_api_id: str,
        route_id: str,
    ) -> apig20240327_models.DeleteHttpApiRouteResponse:
        """
        @summary Delete the route of an HttpApi
        
        @return: DeleteHttpApiRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_http_api_route_with_options_async(http_api_id, route_id, headers, runtime)

    def delete_mcp_server_with_options(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteMcpServerResponse:
        """
        @summary 删除MCP server
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMcpServerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMcpServer',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/mcp-servers/{OpenApiUtilClient.get_encode_param(mcp_server_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mcp_server_with_options_async(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteMcpServerResponse:
        """
        @summary 删除MCP server
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMcpServerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMcpServer',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/mcp-servers/{OpenApiUtilClient.get_encode_param(mcp_server_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mcp_server(
        self,
        mcp_server_id: str,
    ) -> apig20240327_models.DeleteMcpServerResponse:
        """
        @summary 删除MCP server
        
        @return: DeleteMcpServerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_mcp_server_with_options(mcp_server_id, headers, runtime)

    async def delete_mcp_server_async(
        self,
        mcp_server_id: str,
    ) -> apig20240327_models.DeleteMcpServerResponse:
        """
        @summary 删除MCP server
        
        @return: DeleteMcpServerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_mcp_server_with_options_async(mcp_server_id, headers, runtime)

    def delete_plugin_attachment_with_options(
        self,
        plugin_attachment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeletePluginAttachmentResponse:
        """
        @summary 删除挂载规则API
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePluginAttachmentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePluginAttachment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/plugin-attachments/{OpenApiUtilClient.get_encode_param(plugin_attachment_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeletePluginAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_plugin_attachment_with_options_async(
        self,
        plugin_attachment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeletePluginAttachmentResponse:
        """
        @summary 删除挂载规则API
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePluginAttachmentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePluginAttachment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/plugin-attachments/{OpenApiUtilClient.get_encode_param(plugin_attachment_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeletePluginAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_plugin_attachment(
        self,
        plugin_attachment_id: str,
    ) -> apig20240327_models.DeletePluginAttachmentResponse:
        """
        @summary 删除挂载规则API
        
        @return: DeletePluginAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_plugin_attachment_with_options(plugin_attachment_id, headers, runtime)

    async def delete_plugin_attachment_async(
        self,
        plugin_attachment_id: str,
    ) -> apig20240327_models.DeletePluginAttachmentResponse:
        """
        @summary 删除挂载规则API
        
        @return: DeletePluginAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_plugin_attachment_with_options_async(plugin_attachment_id, headers, runtime)

    def delete_policy_with_options(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeletePolicyResponse:
        """
        @summary Delete Policy
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePolicy',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v2/policies/{OpenApiUtilClient.get_encode_param(policy_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeletePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_with_options_async(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeletePolicyResponse:
        """
        @summary Delete Policy
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePolicy',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v2/policies/{OpenApiUtilClient.get_encode_param(policy_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeletePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy(
        self,
        policy_id: str,
    ) -> apig20240327_models.DeletePolicyResponse:
        """
        @summary Delete Policy
        
        @return: DeletePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_policy_with_options(policy_id, headers, runtime)

    async def delete_policy_async(
        self,
        policy_id: str,
    ) -> apig20240327_models.DeletePolicyResponse:
        """
        @summary Delete Policy
        
        @return: DeletePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_policy_with_options_async(policy_id, headers, runtime)

    def delete_policy_attachment_with_options(
        self,
        policy_attachment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeletePolicyAttachmentResponse:
        """
        @summary Delete policy resource attachment
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyAttachmentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePolicyAttachment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/policy-attachments/{OpenApiUtilClient.get_encode_param(policy_attachment_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeletePolicyAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_attachment_with_options_async(
        self,
        policy_attachment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeletePolicyAttachmentResponse:
        """
        @summary Delete policy resource attachment
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyAttachmentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePolicyAttachment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/policy-attachments/{OpenApiUtilClient.get_encode_param(policy_attachment_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeletePolicyAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy_attachment(
        self,
        policy_attachment_id: str,
    ) -> apig20240327_models.DeletePolicyAttachmentResponse:
        """
        @summary Delete policy resource attachment
        
        @return: DeletePolicyAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_policy_attachment_with_options(policy_attachment_id, headers, runtime)

    async def delete_policy_attachment_async(
        self,
        policy_attachment_id: str,
    ) -> apig20240327_models.DeletePolicyAttachmentResponse:
        """
        @summary Delete policy resource attachment
        
        @return: DeletePolicyAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_policy_attachment_with_options_async(policy_attachment_id, headers, runtime)

    def delete_service_with_options(
        self,
        service_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteServiceResponse:
        """
        @summary 删除服务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/services/{OpenApiUtilClient.get_encode_param(service_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_with_options_async(
        self,
        service_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeleteServiceResponse:
        """
        @summary 删除服务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/services/{OpenApiUtilClient.get_encode_param(service_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeleteServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service(
        self,
        service_id: str,
    ) -> apig20240327_models.DeleteServiceResponse:
        """
        @summary 删除服务
        
        @return: DeleteServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_with_options(service_id, headers, runtime)

    async def delete_service_async(
        self,
        service_id: str,
    ) -> apig20240327_models.DeleteServiceResponse:
        """
        @summary 删除服务
        
        @return: DeleteServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_service_with_options_async(service_id, headers, runtime)

    def deploy_http_api_with_options(
        self,
        http_api_id: str,
        request: apig20240327_models.DeployHttpApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeployHttpApiResponse:
        """
        @summary Deploy HttpApi
        
        @param request: DeployHttpApiRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployHttpApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.http_api_config):
            body['httpApiConfig'] = request.http_api_config
        if not UtilClient.is_unset(request.rest_api_config):
            body['restApiConfig'] = request.rest_api_config
        if not UtilClient.is_unset(request.route_id):
            body['routeId'] = request.route_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeployHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/deploy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeployHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_http_api_with_options_async(
        self,
        http_api_id: str,
        request: apig20240327_models.DeployHttpApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeployHttpApiResponse:
        """
        @summary Deploy HttpApi
        
        @param request: DeployHttpApiRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployHttpApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.http_api_config):
            body['httpApiConfig'] = request.http_api_config
        if not UtilClient.is_unset(request.rest_api_config):
            body['restApiConfig'] = request.rest_api_config
        if not UtilClient.is_unset(request.route_id):
            body['routeId'] = request.route_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeployHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/deploy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeployHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_http_api(
        self,
        http_api_id: str,
        request: apig20240327_models.DeployHttpApiRequest,
    ) -> apig20240327_models.DeployHttpApiResponse:
        """
        @summary Deploy HttpApi
        
        @param request: DeployHttpApiRequest
        @return: DeployHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deploy_http_api_with_options(http_api_id, request, headers, runtime)

    async def deploy_http_api_async(
        self,
        http_api_id: str,
        request: apig20240327_models.DeployHttpApiRequest,
    ) -> apig20240327_models.DeployHttpApiResponse:
        """
        @summary Deploy HttpApi
        
        @param request: DeployHttpApiRequest
        @return: DeployHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.deploy_http_api_with_options_async(http_api_id, request, headers, runtime)

    def deploy_mcp_server_with_options(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeployMcpServerResponse:
        """
        @summary 发布MCP server
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployMcpServerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeployMcpServer',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/mcp-servers/{OpenApiUtilClient.get_encode_param(mcp_server_id)}/deploy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeployMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_mcp_server_with_options_async(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.DeployMcpServerResponse:
        """
        @summary 发布MCP server
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployMcpServerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeployMcpServer',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/mcp-servers/{OpenApiUtilClient.get_encode_param(mcp_server_id)}/deploy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.DeployMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_mcp_server(
        self,
        mcp_server_id: str,
    ) -> apig20240327_models.DeployMcpServerResponse:
        """
        @summary 发布MCP server
        
        @return: DeployMcpServerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deploy_mcp_server_with_options(mcp_server_id, headers, runtime)

    async def deploy_mcp_server_async(
        self,
        mcp_server_id: str,
    ) -> apig20240327_models.DeployMcpServerResponse:
        """
        @summary 发布MCP server
        
        @return: DeployMcpServerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.deploy_mcp_server_with_options_async(mcp_server_id, headers, runtime)

    def export_http_api_with_options(
        self,
        http_api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ExportHttpApiResponse:
        """
        @summary Export HTTP API
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportHttpApiResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ExportHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/export',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ExportHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_http_api_with_options_async(
        self,
        http_api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ExportHttpApiResponse:
        """
        @summary Export HTTP API
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportHttpApiResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ExportHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/export',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ExportHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_http_api(
        self,
        http_api_id: str,
    ) -> apig20240327_models.ExportHttpApiResponse:
        """
        @summary Export HTTP API
        
        @return: ExportHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.export_http_api_with_options(http_api_id, headers, runtime)

    async def export_http_api_async(
        self,
        http_api_id: str,
    ) -> apig20240327_models.ExportHttpApiResponse:
        """
        @summary Export HTTP API
        
        @return: ExportHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.export_http_api_with_options_async(http_api_id, headers, runtime)

    def get_consumer_with_options(
        self,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetConsumerResponse:
        """
        @summary 查询消费者
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsumerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetConsumer',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/consumers/{OpenApiUtilClient.get_encode_param(consumer_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetConsumerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consumer_with_options_async(
        self,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetConsumerResponse:
        """
        @summary 查询消费者
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsumerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetConsumer',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/consumers/{OpenApiUtilClient.get_encode_param(consumer_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetConsumerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consumer(
        self,
        consumer_id: str,
    ) -> apig20240327_models.GetConsumerResponse:
        """
        @summary 查询消费者
        
        @return: GetConsumerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_consumer_with_options(consumer_id, headers, runtime)

    async def get_consumer_async(
        self,
        consumer_id: str,
    ) -> apig20240327_models.GetConsumerResponse:
        """
        @summary 查询消费者
        
        @return: GetConsumerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_consumer_with_options_async(consumer_id, headers, runtime)

    def get_consumer_authorization_rule_with_options(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetConsumerAuthorizationRuleResponse:
        """
        @summary 查询消费者授权规则
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsumerAuthorizationRuleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetConsumerAuthorizationRule',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/consumers/{OpenApiUtilClient.get_encode_param(consumer_id)}/authorization-rules/{OpenApiUtilClient.get_encode_param(consumer_authorization_rule_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetConsumerAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consumer_authorization_rule_with_options_async(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetConsumerAuthorizationRuleResponse:
        """
        @summary 查询消费者授权规则
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsumerAuthorizationRuleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetConsumerAuthorizationRule',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/consumers/{OpenApiUtilClient.get_encode_param(consumer_id)}/authorization-rules/{OpenApiUtilClient.get_encode_param(consumer_authorization_rule_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetConsumerAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consumer_authorization_rule(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
    ) -> apig20240327_models.GetConsumerAuthorizationRuleResponse:
        """
        @summary 查询消费者授权规则
        
        @return: GetConsumerAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_consumer_authorization_rule_with_options(consumer_authorization_rule_id, consumer_id, headers, runtime)

    async def get_consumer_authorization_rule_async(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
    ) -> apig20240327_models.GetConsumerAuthorizationRuleResponse:
        """
        @summary 查询消费者授权规则
        
        @return: GetConsumerAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_consumer_authorization_rule_with_options_async(consumer_authorization_rule_id, consumer_id, headers, runtime)

    def get_dashboard_with_options(
        self,
        gateway_id: str,
        tmp_req: apig20240327_models.GetDashboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetDashboardResponse:
        """
        @summary Obtains data from dashboards.
        
        @param tmp_req: GetDashboardRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDashboardResponse
        """
        UtilClient.validate_model(tmp_req)
        request = apig20240327_models.GetDashboardShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.api_id):
            query['apiId'] = request.api_id
        if not UtilClient.is_unset(request.filter_shrink):
            query['filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.plugin_class_id):
            query['pluginClassId'] = request.plugin_class_id
        if not UtilClient.is_unset(request.plugin_id):
            query['pluginId'] = request.plugin_id
        if not UtilClient.is_unset(request.route_id):
            query['routeId'] = request.route_id
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        if not UtilClient.is_unset(request.upstream_cluster):
            query['upstreamCluster'] = request.upstream_cluster
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDashboard',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/dashboards',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetDashboardResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dashboard_with_options_async(
        self,
        gateway_id: str,
        tmp_req: apig20240327_models.GetDashboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetDashboardResponse:
        """
        @summary Obtains data from dashboards.
        
        @param tmp_req: GetDashboardRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDashboardResponse
        """
        UtilClient.validate_model(tmp_req)
        request = apig20240327_models.GetDashboardShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.api_id):
            query['apiId'] = request.api_id
        if not UtilClient.is_unset(request.filter_shrink):
            query['filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.plugin_class_id):
            query['pluginClassId'] = request.plugin_class_id
        if not UtilClient.is_unset(request.plugin_id):
            query['pluginId'] = request.plugin_id
        if not UtilClient.is_unset(request.route_id):
            query['routeId'] = request.route_id
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        if not UtilClient.is_unset(request.upstream_cluster):
            query['upstreamCluster'] = request.upstream_cluster
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDashboard',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/dashboards',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetDashboardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dashboard(
        self,
        gateway_id: str,
        request: apig20240327_models.GetDashboardRequest,
    ) -> apig20240327_models.GetDashboardResponse:
        """
        @summary Obtains data from dashboards.
        
        @param request: GetDashboardRequest
        @return: GetDashboardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_dashboard_with_options(gateway_id, request, headers, runtime)

    async def get_dashboard_async(
        self,
        gateway_id: str,
        request: apig20240327_models.GetDashboardRequest,
    ) -> apig20240327_models.GetDashboardResponse:
        """
        @summary Obtains data from dashboards.
        
        @param request: GetDashboardRequest
        @return: GetDashboardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_dashboard_with_options_async(gateway_id, request, headers, runtime)

    def get_domain_with_options(
        self,
        domain_id: str,
        request: apig20240327_models.GetDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetDomainResponse:
        """
        @summary Queries the information about a domain name.
        
        @param request: GetDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.with_statistics):
            query['withStatistics'] = request.with_statistics
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomain',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/domains/{OpenApiUtilClient.get_encode_param(domain_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_domain_with_options_async(
        self,
        domain_id: str,
        request: apig20240327_models.GetDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetDomainResponse:
        """
        @summary Queries the information about a domain name.
        
        @param request: GetDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.with_statistics):
            query['withStatistics'] = request.with_statistics
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomain',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/domains/{OpenApiUtilClient.get_encode_param(domain_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_domain(
        self,
        domain_id: str,
        request: apig20240327_models.GetDomainRequest,
    ) -> apig20240327_models.GetDomainResponse:
        """
        @summary Queries the information about a domain name.
        
        @param request: GetDomainRequest
        @return: GetDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_domain_with_options(domain_id, request, headers, runtime)

    async def get_domain_async(
        self,
        domain_id: str,
        request: apig20240327_models.GetDomainRequest,
    ) -> apig20240327_models.GetDomainResponse:
        """
        @summary Queries the information about a domain name.
        
        @param request: GetDomainRequest
        @return: GetDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_domain_with_options_async(domain_id, request, headers, runtime)

    def get_environment_with_options(
        self,
        environment_id: str,
        request: apig20240327_models.GetEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetEnvironmentResponse:
        """
        @deprecated OpenAPI GetEnvironment is deprecated
        
        @summary GetEnvironment
        
        @param request: GetEnvironmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEnvironmentResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.with_statistics):
            query['withStatistics'] = request.with_statistics
        if not UtilClient.is_unset(request.with_vpc_info):
            query['withVpcInfo'] = request.with_vpc_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnvironment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/environments/{OpenApiUtilClient.get_encode_param(environment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_environment_with_options_async(
        self,
        environment_id: str,
        request: apig20240327_models.GetEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetEnvironmentResponse:
        """
        @deprecated OpenAPI GetEnvironment is deprecated
        
        @summary GetEnvironment
        
        @param request: GetEnvironmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEnvironmentResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.with_statistics):
            query['withStatistics'] = request.with_statistics
        if not UtilClient.is_unset(request.with_vpc_info):
            query['withVpcInfo'] = request.with_vpc_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnvironment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/environments/{OpenApiUtilClient.get_encode_param(environment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_environment(
        self,
        environment_id: str,
        request: apig20240327_models.GetEnvironmentRequest,
    ) -> apig20240327_models.GetEnvironmentResponse:
        """
        @deprecated OpenAPI GetEnvironment is deprecated
        
        @summary GetEnvironment
        
        @param request: GetEnvironmentRequest
        @return: GetEnvironmentResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_environment_with_options(environment_id, request, headers, runtime)

    async def get_environment_async(
        self,
        environment_id: str,
        request: apig20240327_models.GetEnvironmentRequest,
    ) -> apig20240327_models.GetEnvironmentResponse:
        """
        @deprecated OpenAPI GetEnvironment is deprecated
        
        @summary GetEnvironment
        
        @param request: GetEnvironmentRequest
        @return: GetEnvironmentResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_environment_with_options_async(environment_id, request, headers, runtime)

    def get_gateway_with_options(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetGatewayResponse:
        """
        @summary Queries the basic information about an instance, such as the virtual private cloud (VPC) and vSwitch to which the instance belongs and its ingress.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGatewayResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetGateway',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gateway_with_options_async(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetGatewayResponse:
        """
        @summary Queries the basic information about an instance, such as the virtual private cloud (VPC) and vSwitch to which the instance belongs and its ingress.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGatewayResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetGateway',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gateway(
        self,
        gateway_id: str,
    ) -> apig20240327_models.GetGatewayResponse:
        """
        @summary Queries the basic information about an instance, such as the virtual private cloud (VPC) and vSwitch to which the instance belongs and its ingress.
        
        @return: GetGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_gateway_with_options(gateway_id, headers, runtime)

    async def get_gateway_async(
        self,
        gateway_id: str,
    ) -> apig20240327_models.GetGatewayResponse:
        """
        @summary Queries the basic information about an instance, such as the virtual private cloud (VPC) and vSwitch to which the instance belongs and its ingress.
        
        @return: GetGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_gateway_with_options_async(gateway_id, headers, runtime)

    def get_http_api_with_options(
        self,
        http_api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetHttpApiResponse:
        """
        @summary Read HttpApi
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHttpApiResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_http_api_with_options_async(
        self,
        http_api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetHttpApiResponse:
        """
        @summary Read HttpApi
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHttpApiResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_http_api(
        self,
        http_api_id: str,
    ) -> apig20240327_models.GetHttpApiResponse:
        """
        @summary Read HttpApi
        
        @return: GetHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_http_api_with_options(http_api_id, headers, runtime)

    async def get_http_api_async(
        self,
        http_api_id: str,
    ) -> apig20240327_models.GetHttpApiResponse:
        """
        @summary Read HttpApi
        
        @return: GetHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_http_api_with_options_async(http_api_id, headers, runtime)

    def get_http_api_operation_with_options(
        self,
        http_api_id: str,
        operation_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetHttpApiOperationResponse:
        """
        @summary Get Operation
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHttpApiOperationResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHttpApiOperation',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/operations/{OpenApiUtilClient.get_encode_param(operation_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetHttpApiOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_http_api_operation_with_options_async(
        self,
        http_api_id: str,
        operation_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetHttpApiOperationResponse:
        """
        @summary Get Operation
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHttpApiOperationResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHttpApiOperation',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/operations/{OpenApiUtilClient.get_encode_param(operation_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetHttpApiOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_http_api_operation(
        self,
        http_api_id: str,
        operation_id: str,
    ) -> apig20240327_models.GetHttpApiOperationResponse:
        """
        @summary Get Operation
        
        @return: GetHttpApiOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_http_api_operation_with_options(http_api_id, operation_id, headers, runtime)

    async def get_http_api_operation_async(
        self,
        http_api_id: str,
        operation_id: str,
    ) -> apig20240327_models.GetHttpApiOperationResponse:
        """
        @summary Get Operation
        
        @return: GetHttpApiOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_http_api_operation_with_options_async(http_api_id, operation_id, headers, runtime)

    def get_http_api_route_with_options(
        self,
        http_api_id: str,
        route_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetHttpApiRouteResponse:
        """
        @summary Queries the details of a route of an HTTP API.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHttpApiRouteResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHttpApiRoute',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/routes/{OpenApiUtilClient.get_encode_param(route_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetHttpApiRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_http_api_route_with_options_async(
        self,
        http_api_id: str,
        route_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetHttpApiRouteResponse:
        """
        @summary Queries the details of a route of an HTTP API.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHttpApiRouteResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHttpApiRoute',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/routes/{OpenApiUtilClient.get_encode_param(route_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetHttpApiRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_http_api_route(
        self,
        http_api_id: str,
        route_id: str,
    ) -> apig20240327_models.GetHttpApiRouteResponse:
        """
        @summary Queries the details of a route of an HTTP API.
        
        @return: GetHttpApiRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_http_api_route_with_options(http_api_id, route_id, headers, runtime)

    async def get_http_api_route_async(
        self,
        http_api_id: str,
        route_id: str,
    ) -> apig20240327_models.GetHttpApiRouteResponse:
        """
        @summary Queries the details of a route of an HTTP API.
        
        @return: GetHttpApiRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_http_api_route_with_options_async(http_api_id, route_id, headers, runtime)

    def get_mcp_server_with_options(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetMcpServerResponse:
        """
        @summary 获取MCP server
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMcpServerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMcpServer',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/mcp-servers/{OpenApiUtilClient.get_encode_param(mcp_server_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mcp_server_with_options_async(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetMcpServerResponse:
        """
        @summary 获取MCP server
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMcpServerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMcpServer',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/mcp-servers/{OpenApiUtilClient.get_encode_param(mcp_server_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mcp_server(
        self,
        mcp_server_id: str,
    ) -> apig20240327_models.GetMcpServerResponse:
        """
        @summary 获取MCP server
        
        @return: GetMcpServerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_mcp_server_with_options(mcp_server_id, headers, runtime)

    async def get_mcp_server_async(
        self,
        mcp_server_id: str,
    ) -> apig20240327_models.GetMcpServerResponse:
        """
        @summary 获取MCP server
        
        @return: GetMcpServerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_mcp_server_with_options_async(mcp_server_id, headers, runtime)

    def get_plugin_attachment_with_options(
        self,
        plugin_attachment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetPluginAttachmentResponse:
        """
        @summary GetPluginAttachment。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPluginAttachmentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPluginAttachment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/plugin-attachments/{OpenApiUtilClient.get_encode_param(plugin_attachment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetPluginAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_plugin_attachment_with_options_async(
        self,
        plugin_attachment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetPluginAttachmentResponse:
        """
        @summary GetPluginAttachment。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPluginAttachmentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPluginAttachment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/plugin-attachments/{OpenApiUtilClient.get_encode_param(plugin_attachment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetPluginAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_plugin_attachment(
        self,
        plugin_attachment_id: str,
    ) -> apig20240327_models.GetPluginAttachmentResponse:
        """
        @summary GetPluginAttachment。
        
        @return: GetPluginAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_plugin_attachment_with_options(plugin_attachment_id, headers, runtime)

    async def get_plugin_attachment_async(
        self,
        plugin_attachment_id: str,
    ) -> apig20240327_models.GetPluginAttachmentResponse:
        """
        @summary GetPluginAttachment。
        
        @return: GetPluginAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_plugin_attachment_with_options_async(plugin_attachment_id, headers, runtime)

    def get_policy_with_options(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetPolicyResponse:
        """
        @summary Queries a policy.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPolicyResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPolicy',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v2/policies/{OpenApiUtilClient.get_encode_param(policy_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_with_options_async(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetPolicyResponse:
        """
        @summary Queries a policy.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPolicyResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPolicy',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v2/policies/{OpenApiUtilClient.get_encode_param(policy_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy(
        self,
        policy_id: str,
    ) -> apig20240327_models.GetPolicyResponse:
        """
        @summary Queries a policy.
        
        @return: GetPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_policy_with_options(policy_id, headers, runtime)

    async def get_policy_async(
        self,
        policy_id: str,
    ) -> apig20240327_models.GetPolicyResponse:
        """
        @summary Queries a policy.
        
        @return: GetPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_policy_with_options_async(policy_id, headers, runtime)

    def get_policy_attachment_with_options(
        self,
        policy_attachment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetPolicyAttachmentResponse:
        """
        @summary Query Policy Resource Attachment
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPolicyAttachmentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPolicyAttachment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/policy-attachments/{OpenApiUtilClient.get_encode_param(policy_attachment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetPolicyAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_attachment_with_options_async(
        self,
        policy_attachment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetPolicyAttachmentResponse:
        """
        @summary Query Policy Resource Attachment
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPolicyAttachmentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPolicyAttachment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/policy-attachments/{OpenApiUtilClient.get_encode_param(policy_attachment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetPolicyAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy_attachment(
        self,
        policy_attachment_id: str,
    ) -> apig20240327_models.GetPolicyAttachmentResponse:
        """
        @summary Query Policy Resource Attachment
        
        @return: GetPolicyAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_policy_attachment_with_options(policy_attachment_id, headers, runtime)

    async def get_policy_attachment_async(
        self,
        policy_attachment_id: str,
    ) -> apig20240327_models.GetPolicyAttachmentResponse:
        """
        @summary Query Policy Resource Attachment
        
        @return: GetPolicyAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_policy_attachment_with_options_async(policy_attachment_id, headers, runtime)

    def get_resource_overview_with_options(
        self,
        request: apig20240327_models.GetResourceOverviewRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetResourceOverviewResponse:
        """
        @summary Get resource overview information
        
        @param request: GetResourceOverviewRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceOverviewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceOverview',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/overview/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetResourceOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_overview_with_options_async(
        self,
        request: apig20240327_models.GetResourceOverviewRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetResourceOverviewResponse:
        """
        @summary Get resource overview information
        
        @param request: GetResourceOverviewRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceOverviewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceOverview',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/overview/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetResourceOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_overview(
        self,
        request: apig20240327_models.GetResourceOverviewRequest,
    ) -> apig20240327_models.GetResourceOverviewResponse:
        """
        @summary Get resource overview information
        
        @param request: GetResourceOverviewRequest
        @return: GetResourceOverviewResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_overview_with_options(request, headers, runtime)

    async def get_resource_overview_async(
        self,
        request: apig20240327_models.GetResourceOverviewRequest,
    ) -> apig20240327_models.GetResourceOverviewResponse:
        """
        @summary Get resource overview information
        
        @param request: GetResourceOverviewRequest
        @return: GetResourceOverviewResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_resource_overview_with_options_async(request, headers, runtime)

    def get_service_with_options(
        self,
        service_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetServiceResponse:
        """
        @summary Queries the details of a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetService',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/services/{OpenApiUtilClient.get_encode_param(service_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_with_options_async(
        self,
        service_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetServiceResponse:
        """
        @summary Queries the details of a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetService',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/services/{OpenApiUtilClient.get_encode_param(service_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service(
        self,
        service_id: str,
    ) -> apig20240327_models.GetServiceResponse:
        """
        @summary Queries the details of a service.
        
        @return: GetServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_with_options(service_id, headers, runtime)

    async def get_service_async(
        self,
        service_id: str,
    ) -> apig20240327_models.GetServiceResponse:
        """
        @summary Queries the details of a service.
        
        @return: GetServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_with_options_async(service_id, headers, runtime)

    def get_trace_config_with_options(
        self,
        gateway_id: str,
        request: apig20240327_models.GetTraceConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetTraceConfigResponse:
        """
        @summary Retrieve Tracing Configuration
        
        @param request: GetTraceConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTraceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTraceConfig',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/trace',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetTraceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trace_config_with_options_async(
        self,
        gateway_id: str,
        request: apig20240327_models.GetTraceConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.GetTraceConfigResponse:
        """
        @summary Retrieve Tracing Configuration
        
        @param request: GetTraceConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTraceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTraceConfig',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/trace',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.GetTraceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trace_config(
        self,
        gateway_id: str,
        request: apig20240327_models.GetTraceConfigRequest,
    ) -> apig20240327_models.GetTraceConfigResponse:
        """
        @summary Retrieve Tracing Configuration
        
        @param request: GetTraceConfigRequest
        @return: GetTraceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_trace_config_with_options(gateway_id, request, headers, runtime)

    async def get_trace_config_async(
        self,
        gateway_id: str,
        request: apig20240327_models.GetTraceConfigRequest,
    ) -> apig20240327_models.GetTraceConfigResponse:
        """
        @summary Retrieve Tracing Configuration
        
        @param request: GetTraceConfigRequest
        @return: GetTraceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_trace_config_with_options_async(gateway_id, request, headers, runtime)

    def import_http_api_with_options(
        self,
        request: apig20240327_models.ImportHttpApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ImportHttpApiResponse:
        """
        @summary Imports HTTP APIs. You can call this operation to import OpenAPI 2.0 and OpenAPI 3.0.x definition files to create REST APIs.
        
        @param request: ImportHttpApiRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportHttpApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            body['dryRun'] = request.dry_run
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.mcp_route_id):
            body['mcpRouteId'] = request.mcp_route_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.spec_content_base_64):
            body['specContentBase64'] = request.spec_content_base_64
        if not UtilClient.is_unset(request.spec_file_url):
            body['specFileUrl'] = request.spec_file_url
        if not UtilClient.is_unset(request.spec_oss_config):
            body['specOssConfig'] = request.spec_oss_config
        if not UtilClient.is_unset(request.strategy):
            body['strategy'] = request.strategy
        if not UtilClient.is_unset(request.target_http_api_id):
            body['targetHttpApiId'] = request.target_http_api_id
        if not UtilClient.is_unset(request.version_config):
            body['versionConfig'] = request.version_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/import',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ImportHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_http_api_with_options_async(
        self,
        request: apig20240327_models.ImportHttpApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ImportHttpApiResponse:
        """
        @summary Imports HTTP APIs. You can call this operation to import OpenAPI 2.0 and OpenAPI 3.0.x definition files to create REST APIs.
        
        @param request: ImportHttpApiRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportHttpApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            body['dryRun'] = request.dry_run
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.mcp_route_id):
            body['mcpRouteId'] = request.mcp_route_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.spec_content_base_64):
            body['specContentBase64'] = request.spec_content_base_64
        if not UtilClient.is_unset(request.spec_file_url):
            body['specFileUrl'] = request.spec_file_url
        if not UtilClient.is_unset(request.spec_oss_config):
            body['specOssConfig'] = request.spec_oss_config
        if not UtilClient.is_unset(request.strategy):
            body['strategy'] = request.strategy
        if not UtilClient.is_unset(request.target_http_api_id):
            body['targetHttpApiId'] = request.target_http_api_id
        if not UtilClient.is_unset(request.version_config):
            body['versionConfig'] = request.version_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/import',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ImportHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_http_api(
        self,
        request: apig20240327_models.ImportHttpApiRequest,
    ) -> apig20240327_models.ImportHttpApiResponse:
        """
        @summary Imports HTTP APIs. You can call this operation to import OpenAPI 2.0 and OpenAPI 3.0.x definition files to create REST APIs.
        
        @param request: ImportHttpApiRequest
        @return: ImportHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.import_http_api_with_options(request, headers, runtime)

    async def import_http_api_async(
        self,
        request: apig20240327_models.ImportHttpApiRequest,
    ) -> apig20240327_models.ImportHttpApiResponse:
        """
        @summary Imports HTTP APIs. You can call this operation to import OpenAPI 2.0 and OpenAPI 3.0.x definition files to create REST APIs.
        
        @param request: ImportHttpApiRequest
        @return: ImportHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.import_http_api_with_options_async(request, headers, runtime)

    def install_plugin_with_options(
        self,
        request: apig20240327_models.InstallPluginRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.InstallPluginResponse:
        """
        @summary InstallPlugin
        
        @param request: InstallPluginRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallPluginResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_ids):
            body['gatewayIds'] = request.gateway_ids
        if not UtilClient.is_unset(request.plugin_class_id):
            body['pluginClassId'] = request.plugin_class_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InstallPlugin',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/plugins/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.InstallPluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_plugin_with_options_async(
        self,
        request: apig20240327_models.InstallPluginRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.InstallPluginResponse:
        """
        @summary InstallPlugin
        
        @param request: InstallPluginRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallPluginResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_ids):
            body['gatewayIds'] = request.gateway_ids
        if not UtilClient.is_unset(request.plugin_class_id):
            body['pluginClassId'] = request.plugin_class_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InstallPlugin',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/plugins/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.InstallPluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_plugin(
        self,
        request: apig20240327_models.InstallPluginRequest,
    ) -> apig20240327_models.InstallPluginResponse:
        """
        @summary InstallPlugin
        
        @param request: InstallPluginRequest
        @return: InstallPluginResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_plugin_with_options(request, headers, runtime)

    async def install_plugin_async(
        self,
        request: apig20240327_models.InstallPluginRequest,
    ) -> apig20240327_models.InstallPluginResponse:
        """
        @summary InstallPlugin
        
        @param request: InstallPluginRequest
        @return: InstallPluginResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.install_plugin_with_options_async(request, headers, runtime)

    def list_consumers_with_options(
        self,
        request: apig20240327_models.ListConsumersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListConsumersResponse:
        """
        @summary 查询消费者列表
        
        @param request: ListConsumersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConsumersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not UtilClient.is_unset(request.name_like):
            query['nameLike'] = request.name_like
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConsumers',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/consumers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListConsumersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_consumers_with_options_async(
        self,
        request: apig20240327_models.ListConsumersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListConsumersResponse:
        """
        @summary 查询消费者列表
        
        @param request: ListConsumersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConsumersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not UtilClient.is_unset(request.name_like):
            query['nameLike'] = request.name_like
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConsumers',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/consumers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListConsumersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_consumers(
        self,
        request: apig20240327_models.ListConsumersRequest,
    ) -> apig20240327_models.ListConsumersResponse:
        """
        @summary 查询消费者列表
        
        @param request: ListConsumersRequest
        @return: ListConsumersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_consumers_with_options(request, headers, runtime)

    async def list_consumers_async(
        self,
        request: apig20240327_models.ListConsumersRequest,
    ) -> apig20240327_models.ListConsumersResponse:
        """
        @summary 查询消费者列表
        
        @param request: ListConsumersRequest
        @return: ListConsumersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_consumers_with_options_async(request, headers, runtime)

    def list_domains_with_options(
        self,
        request: apig20240327_models.ListDomainsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListDomainsResponse:
        """
        @summary Queries a list of domain names.
        
        @param request: ListDomainsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not UtilClient.is_unset(request.name_like):
            query['nameLike'] = request.name_like
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDomains',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/domains',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_domains_with_options_async(
        self,
        request: apig20240327_models.ListDomainsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListDomainsResponse:
        """
        @summary Queries a list of domain names.
        
        @param request: ListDomainsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not UtilClient.is_unset(request.name_like):
            query['nameLike'] = request.name_like
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDomains',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/domains',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_domains(
        self,
        request: apig20240327_models.ListDomainsRequest,
    ) -> apig20240327_models.ListDomainsResponse:
        """
        @summary Queries a list of domain names.
        
        @param request: ListDomainsRequest
        @return: ListDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_domains_with_options(request, headers, runtime)

    async def list_domains_async(
        self,
        request: apig20240327_models.ListDomainsRequest,
    ) -> apig20240327_models.ListDomainsResponse:
        """
        @summary Queries a list of domain names.
        
        @param request: ListDomainsRequest
        @return: ListDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_domains_with_options_async(request, headers, runtime)

    def list_environments_with_options(
        self,
        request: apig20240327_models.ListEnvironmentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListEnvironmentsResponse:
        """
        @deprecated OpenAPI ListEnvironments is deprecated
        
        @summary ListEnvironments
        
        @param request: ListEnvironmentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEnvironmentsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_like):
            query['aliasLike'] = request.alias_like
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_name_like):
            query['gatewayNameLike'] = request.gateway_name_like
        if not UtilClient.is_unset(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not UtilClient.is_unset(request.name_like):
            query['nameLike'] = request.name_like
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironments',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/environments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListEnvironmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environments_with_options_async(
        self,
        request: apig20240327_models.ListEnvironmentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListEnvironmentsResponse:
        """
        @deprecated OpenAPI ListEnvironments is deprecated
        
        @summary ListEnvironments
        
        @param request: ListEnvironmentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEnvironmentsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_like):
            query['aliasLike'] = request.alias_like
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_name_like):
            query['gatewayNameLike'] = request.gateway_name_like
        if not UtilClient.is_unset(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not UtilClient.is_unset(request.name_like):
            query['nameLike'] = request.name_like
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironments',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/environments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListEnvironmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environments(
        self,
        request: apig20240327_models.ListEnvironmentsRequest,
    ) -> apig20240327_models.ListEnvironmentsResponse:
        """
        @deprecated OpenAPI ListEnvironments is deprecated
        
        @summary ListEnvironments
        
        @param request: ListEnvironmentsRequest
        @return: ListEnvironmentsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environments_with_options(request, headers, runtime)

    async def list_environments_async(
        self,
        request: apig20240327_models.ListEnvironmentsRequest,
    ) -> apig20240327_models.ListEnvironmentsResponse:
        """
        @deprecated OpenAPI ListEnvironments is deprecated
        
        @summary ListEnvironments
        
        @param request: ListEnvironmentsRequest
        @return: ListEnvironmentsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_environments_with_options_async(request, headers, runtime)

    def list_gateways_with_options(
        self,
        tmp_req: apig20240327_models.ListGatewaysRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListGatewaysResponse:
        """
        @summary Queries a list of instances.
        
        @param tmp_req: ListGatewaysRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGatewaysResponse
        """
        UtilClient.validate_model(tmp_req)
        request = apig20240327_models.ListGatewaysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGateways',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListGatewaysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateways_with_options_async(
        self,
        tmp_req: apig20240327_models.ListGatewaysRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListGatewaysResponse:
        """
        @summary Queries a list of instances.
        
        @param tmp_req: ListGatewaysRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGatewaysResponse
        """
        UtilClient.validate_model(tmp_req)
        request = apig20240327_models.ListGatewaysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGateways',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListGatewaysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateways(
        self,
        request: apig20240327_models.ListGatewaysRequest,
    ) -> apig20240327_models.ListGatewaysResponse:
        """
        @summary Queries a list of instances.
        
        @param request: ListGatewaysRequest
        @return: ListGatewaysResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_gateways_with_options(request, headers, runtime)

    async def list_gateways_async(
        self,
        request: apig20240327_models.ListGatewaysRequest,
    ) -> apig20240327_models.ListGatewaysResponse:
        """
        @summary Queries a list of instances.
        
        @param request: ListGatewaysRequest
        @return: ListGatewaysResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_gateways_with_options_async(request, headers, runtime)

    def list_http_api_operations_with_options(
        self,
        http_api_id: str,
        request: apig20240327_models.ListHttpApiOperationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListHttpApiOperationsResponse:
        """
        @summary List Operations
        
        @param request: ListHttpApiOperationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHttpApiOperationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_authorization_rule_id):
            query['consumerAuthorizationRuleId'] = request.consumer_authorization_rule_id
        if not UtilClient.is_unset(request.enable_auth):
            query['enableAuth'] = request.enable_auth
        if not UtilClient.is_unset(request.for_deploy):
            query['forDeploy'] = request.for_deploy
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.method):
            query['method'] = request.method
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.name_like):
            query['nameLike'] = request.name_like
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.path_like):
            query['pathLike'] = request.path_like
        if not UtilClient.is_unset(request.with_consumer_in_environment_id):
            query['withConsumerInEnvironmentId'] = request.with_consumer_in_environment_id
        if not UtilClient.is_unset(request.with_consumer_info_by_id):
            query['withConsumerInfoById'] = request.with_consumer_info_by_id
        if not UtilClient.is_unset(request.with_plugin_attachment_by_plugin_id):
            query['withPluginAttachmentByPluginId'] = request.with_plugin_attachment_by_plugin_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHttpApiOperations',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/operations',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListHttpApiOperationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_http_api_operations_with_options_async(
        self,
        http_api_id: str,
        request: apig20240327_models.ListHttpApiOperationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListHttpApiOperationsResponse:
        """
        @summary List Operations
        
        @param request: ListHttpApiOperationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHttpApiOperationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_authorization_rule_id):
            query['consumerAuthorizationRuleId'] = request.consumer_authorization_rule_id
        if not UtilClient.is_unset(request.enable_auth):
            query['enableAuth'] = request.enable_auth
        if not UtilClient.is_unset(request.for_deploy):
            query['forDeploy'] = request.for_deploy
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.method):
            query['method'] = request.method
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.name_like):
            query['nameLike'] = request.name_like
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.path_like):
            query['pathLike'] = request.path_like
        if not UtilClient.is_unset(request.with_consumer_in_environment_id):
            query['withConsumerInEnvironmentId'] = request.with_consumer_in_environment_id
        if not UtilClient.is_unset(request.with_consumer_info_by_id):
            query['withConsumerInfoById'] = request.with_consumer_info_by_id
        if not UtilClient.is_unset(request.with_plugin_attachment_by_plugin_id):
            query['withPluginAttachmentByPluginId'] = request.with_plugin_attachment_by_plugin_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHttpApiOperations',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/operations',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListHttpApiOperationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_http_api_operations(
        self,
        http_api_id: str,
        request: apig20240327_models.ListHttpApiOperationsRequest,
    ) -> apig20240327_models.ListHttpApiOperationsResponse:
        """
        @summary List Operations
        
        @param request: ListHttpApiOperationsRequest
        @return: ListHttpApiOperationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_http_api_operations_with_options(http_api_id, request, headers, runtime)

    async def list_http_api_operations_async(
        self,
        http_api_id: str,
        request: apig20240327_models.ListHttpApiOperationsRequest,
    ) -> apig20240327_models.ListHttpApiOperationsResponse:
        """
        @summary List Operations
        
        @param request: ListHttpApiOperationsRequest
        @return: ListHttpApiOperationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_http_api_operations_with_options_async(http_api_id, request, headers, runtime)

    def list_http_api_routes_with_options(
        self,
        http_api_id: str,
        request: apig20240327_models.ListHttpApiRoutesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListHttpApiRoutesResponse:
        """
        @summary Queries the routes of an HTTP API.
        
        @param request: ListHttpApiRoutesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHttpApiRoutesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_authorization_rule_id):
            query['consumerAuthorizationRuleId'] = request.consumer_authorization_rule_id
        if not UtilClient.is_unset(request.deploy_statuses):
            query['deployStatuses'] = request.deploy_statuses
        if not UtilClient.is_unset(request.domain_id):
            query['domainId'] = request.domain_id
        if not UtilClient.is_unset(request.environment_id):
            query['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.for_deploy):
            query['forDeploy'] = request.for_deploy
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.name_like):
            query['nameLike'] = request.name_like
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.path_like):
            query['pathLike'] = request.path_like
        if not UtilClient.is_unset(request.with_auth_policy_info):
            query['withAuthPolicyInfo'] = request.with_auth_policy_info
        if not UtilClient.is_unset(request.with_consumer_info_by_id):
            query['withConsumerInfoById'] = request.with_consumer_info_by_id
        if not UtilClient.is_unset(request.with_plugin_attachment_by_plugin_id):
            query['withPluginAttachmentByPluginId'] = request.with_plugin_attachment_by_plugin_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHttpApiRoutes',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/routes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListHttpApiRoutesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_http_api_routes_with_options_async(
        self,
        http_api_id: str,
        request: apig20240327_models.ListHttpApiRoutesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListHttpApiRoutesResponse:
        """
        @summary Queries the routes of an HTTP API.
        
        @param request: ListHttpApiRoutesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHttpApiRoutesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_authorization_rule_id):
            query['consumerAuthorizationRuleId'] = request.consumer_authorization_rule_id
        if not UtilClient.is_unset(request.deploy_statuses):
            query['deployStatuses'] = request.deploy_statuses
        if not UtilClient.is_unset(request.domain_id):
            query['domainId'] = request.domain_id
        if not UtilClient.is_unset(request.environment_id):
            query['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.for_deploy):
            query['forDeploy'] = request.for_deploy
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.name_like):
            query['nameLike'] = request.name_like
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.path_like):
            query['pathLike'] = request.path_like
        if not UtilClient.is_unset(request.with_auth_policy_info):
            query['withAuthPolicyInfo'] = request.with_auth_policy_info
        if not UtilClient.is_unset(request.with_consumer_info_by_id):
            query['withConsumerInfoById'] = request.with_consumer_info_by_id
        if not UtilClient.is_unset(request.with_plugin_attachment_by_plugin_id):
            query['withPluginAttachmentByPluginId'] = request.with_plugin_attachment_by_plugin_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHttpApiRoutes',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/routes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListHttpApiRoutesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_http_api_routes(
        self,
        http_api_id: str,
        request: apig20240327_models.ListHttpApiRoutesRequest,
    ) -> apig20240327_models.ListHttpApiRoutesResponse:
        """
        @summary Queries the routes of an HTTP API.
        
        @param request: ListHttpApiRoutesRequest
        @return: ListHttpApiRoutesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_http_api_routes_with_options(http_api_id, request, headers, runtime)

    async def list_http_api_routes_async(
        self,
        http_api_id: str,
        request: apig20240327_models.ListHttpApiRoutesRequest,
    ) -> apig20240327_models.ListHttpApiRoutesResponse:
        """
        @summary Queries the routes of an HTTP API.
        
        @param request: ListHttpApiRoutesRequest
        @return: ListHttpApiRoutesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_http_api_routes_with_options_async(http_api_id, request, headers, runtime)

    def list_http_apis_with_options(
        self,
        request: apig20240327_models.ListHttpApisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListHttpApisResponse:
        """
        @summary Queries a list of HTTP APIs.
        
        @param request: ListHttpApisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHttpApisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.types):
            query['types'] = request.types
        if not UtilClient.is_unset(request.with_apis_published_to_environment):
            query['withAPIsPublishedToEnvironment'] = request.with_apis_published_to_environment
        if not UtilClient.is_unset(request.with_auth_policy_in_environment_id):
            query['withAuthPolicyInEnvironmentId'] = request.with_auth_policy_in_environment_id
        if not UtilClient.is_unset(request.with_auth_policy_list):
            query['withAuthPolicyList'] = request.with_auth_policy_list
        if not UtilClient.is_unset(request.with_consumer_info_by_id):
            query['withConsumerInfoById'] = request.with_consumer_info_by_id
        if not UtilClient.is_unset(request.with_environment_info):
            query['withEnvironmentInfo'] = request.with_environment_info
        if not UtilClient.is_unset(request.with_environment_info_by_id):
            query['withEnvironmentInfoById'] = request.with_environment_info_by_id
        if not UtilClient.is_unset(request.with_ingress_info):
            query['withIngressInfo'] = request.with_ingress_info
        if not UtilClient.is_unset(request.with_plugin_attachment_by_plugin_id):
            query['withPluginAttachmentByPluginId'] = request.with_plugin_attachment_by_plugin_id
        if not UtilClient.is_unset(request.with_policy_configs):
            query['withPolicyConfigs'] = request.with_policy_configs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHttpApis',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListHttpApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_http_apis_with_options_async(
        self,
        request: apig20240327_models.ListHttpApisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListHttpApisResponse:
        """
        @summary Queries a list of HTTP APIs.
        
        @param request: ListHttpApisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHttpApisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.types):
            query['types'] = request.types
        if not UtilClient.is_unset(request.with_apis_published_to_environment):
            query['withAPIsPublishedToEnvironment'] = request.with_apis_published_to_environment
        if not UtilClient.is_unset(request.with_auth_policy_in_environment_id):
            query['withAuthPolicyInEnvironmentId'] = request.with_auth_policy_in_environment_id
        if not UtilClient.is_unset(request.with_auth_policy_list):
            query['withAuthPolicyList'] = request.with_auth_policy_list
        if not UtilClient.is_unset(request.with_consumer_info_by_id):
            query['withConsumerInfoById'] = request.with_consumer_info_by_id
        if not UtilClient.is_unset(request.with_environment_info):
            query['withEnvironmentInfo'] = request.with_environment_info
        if not UtilClient.is_unset(request.with_environment_info_by_id):
            query['withEnvironmentInfoById'] = request.with_environment_info_by_id
        if not UtilClient.is_unset(request.with_ingress_info):
            query['withIngressInfo'] = request.with_ingress_info
        if not UtilClient.is_unset(request.with_plugin_attachment_by_plugin_id):
            query['withPluginAttachmentByPluginId'] = request.with_plugin_attachment_by_plugin_id
        if not UtilClient.is_unset(request.with_policy_configs):
            query['withPolicyConfigs'] = request.with_policy_configs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHttpApis',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListHttpApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_http_apis(
        self,
        request: apig20240327_models.ListHttpApisRequest,
    ) -> apig20240327_models.ListHttpApisResponse:
        """
        @summary Queries a list of HTTP APIs.
        
        @param request: ListHttpApisRequest
        @return: ListHttpApisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_http_apis_with_options(request, headers, runtime)

    async def list_http_apis_async(
        self,
        request: apig20240327_models.ListHttpApisRequest,
    ) -> apig20240327_models.ListHttpApisResponse:
        """
        @summary Queries a list of HTTP APIs.
        
        @param request: ListHttpApisRequest
        @return: ListHttpApisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_http_apis_with_options_async(request, headers, runtime)

    def list_mcp_servers_with_options(
        self,
        request: apig20240327_models.ListMcpServersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListMcpServersResponse:
        """
        @summary 获取MCP server列表
        
        @param request: ListMcpServersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMcpServersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_from_types):
            query['createFromTypes'] = request.create_from_types
        if not UtilClient.is_unset(request.deploy_statuses):
            query['deployStatuses'] = request.deploy_statuses
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.name_like):
            query['nameLike'] = request.name_like
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMcpServers',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/mcp-servers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListMcpServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcp_servers_with_options_async(
        self,
        request: apig20240327_models.ListMcpServersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListMcpServersResponse:
        """
        @summary 获取MCP server列表
        
        @param request: ListMcpServersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMcpServersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_from_types):
            query['createFromTypes'] = request.create_from_types
        if not UtilClient.is_unset(request.deploy_statuses):
            query['deployStatuses'] = request.deploy_statuses
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.name_like):
            query['nameLike'] = request.name_like
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMcpServers',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/mcp-servers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListMcpServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcp_servers(
        self,
        request: apig20240327_models.ListMcpServersRequest,
    ) -> apig20240327_models.ListMcpServersResponse:
        """
        @summary 获取MCP server列表
        
        @param request: ListMcpServersRequest
        @return: ListMcpServersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_mcp_servers_with_options(request, headers, runtime)

    async def list_mcp_servers_async(
        self,
        request: apig20240327_models.ListMcpServersRequest,
    ) -> apig20240327_models.ListMcpServersResponse:
        """
        @summary 获取MCP server列表
        
        @param request: ListMcpServersRequest
        @return: ListMcpServersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_mcp_servers_with_options_async(request, headers, runtime)

    def list_plugin_attachments_with_options(
        self,
        request: apig20240327_models.ListPluginAttachmentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListPluginAttachmentsResponse:
        """
        @summary 获取挂载列表
        
        @param request: ListPluginAttachmentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPluginAttachmentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not UtilClient.is_unset(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not UtilClient.is_unset(request.attach_resource_types):
            query['attachResourceTypes'] = request.attach_resource_types
        if not UtilClient.is_unset(request.environment_id):
            query['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.plugin_id):
            query['pluginId'] = request.plugin_id
        if not UtilClient.is_unset(request.with_parent_resource):
            query['withParentResource'] = request.with_parent_resource
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPluginAttachments',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/plugin-attachments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListPluginAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_plugin_attachments_with_options_async(
        self,
        request: apig20240327_models.ListPluginAttachmentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListPluginAttachmentsResponse:
        """
        @summary 获取挂载列表
        
        @param request: ListPluginAttachmentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPluginAttachmentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not UtilClient.is_unset(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not UtilClient.is_unset(request.attach_resource_types):
            query['attachResourceTypes'] = request.attach_resource_types
        if not UtilClient.is_unset(request.environment_id):
            query['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.plugin_id):
            query['pluginId'] = request.plugin_id
        if not UtilClient.is_unset(request.with_parent_resource):
            query['withParentResource'] = request.with_parent_resource
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPluginAttachments',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/plugin-attachments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListPluginAttachmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_plugin_attachments(
        self,
        request: apig20240327_models.ListPluginAttachmentsRequest,
    ) -> apig20240327_models.ListPluginAttachmentsResponse:
        """
        @summary 获取挂载列表
        
        @param request: ListPluginAttachmentsRequest
        @return: ListPluginAttachmentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_plugin_attachments_with_options(request, headers, runtime)

    async def list_plugin_attachments_async(
        self,
        request: apig20240327_models.ListPluginAttachmentsRequest,
    ) -> apig20240327_models.ListPluginAttachmentsResponse:
        """
        @summary 获取挂载列表
        
        @param request: ListPluginAttachmentsRequest
        @return: ListPluginAttachmentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_plugin_attachments_with_options_async(request, headers, runtime)

    def list_plugins_with_options(
        self,
        request: apig20240327_models.ListPluginsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListPluginsResponse:
        """
        @summary ListPlugins
        
        @param request: ListPluginsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPluginsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not UtilClient.is_unset(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not UtilClient.is_unset(request.include_builtin_ai_gateway):
            query['includeBuiltinAiGateway'] = request.include_builtin_ai_gateway
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.plugin_class_id):
            query['pluginClassId'] = request.plugin_class_id
        if not UtilClient.is_unset(request.plugin_class_name):
            query['pluginClassName'] = request.plugin_class_name
        if not UtilClient.is_unset(request.with_attachment_info):
            query['withAttachmentInfo'] = request.with_attachment_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPlugins',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/plugins',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListPluginsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_plugins_with_options_async(
        self,
        request: apig20240327_models.ListPluginsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListPluginsResponse:
        """
        @summary ListPlugins
        
        @param request: ListPluginsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPluginsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not UtilClient.is_unset(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not UtilClient.is_unset(request.include_builtin_ai_gateway):
            query['includeBuiltinAiGateway'] = request.include_builtin_ai_gateway
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.plugin_class_id):
            query['pluginClassId'] = request.plugin_class_id
        if not UtilClient.is_unset(request.plugin_class_name):
            query['pluginClassName'] = request.plugin_class_name
        if not UtilClient.is_unset(request.with_attachment_info):
            query['withAttachmentInfo'] = request.with_attachment_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPlugins',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/plugins',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListPluginsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_plugins(
        self,
        request: apig20240327_models.ListPluginsRequest,
    ) -> apig20240327_models.ListPluginsResponse:
        """
        @summary ListPlugins
        
        @param request: ListPluginsRequest
        @return: ListPluginsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_plugins_with_options(request, headers, runtime)

    async def list_plugins_async(
        self,
        request: apig20240327_models.ListPluginsRequest,
    ) -> apig20240327_models.ListPluginsResponse:
        """
        @summary ListPlugins
        
        @param request: ListPluginsRequest
        @return: ListPluginsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_plugins_with_options_async(request, headers, runtime)

    def list_policies_with_options(
        self,
        request: apig20240327_models.ListPoliciesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListPoliciesResponse:
        """
        @summary ListPolicies
        
        @param request: ListPoliciesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not UtilClient.is_unset(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not UtilClient.is_unset(request.environment_id):
            query['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.with_attachments):
            query['withAttachments'] = request.with_attachments
        if not UtilClient.is_unset(request.with_system_policy):
            query['withSystemPolicy'] = request.with_system_policy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicies',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/policies',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_with_options_async(
        self,
        request: apig20240327_models.ListPoliciesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListPoliciesResponse:
        """
        @summary ListPolicies
        
        @param request: ListPoliciesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not UtilClient.is_unset(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not UtilClient.is_unset(request.environment_id):
            query['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.with_attachments):
            query['withAttachments'] = request.with_attachments
        if not UtilClient.is_unset(request.with_system_policy):
            query['withSystemPolicy'] = request.with_system_policy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicies',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/policies',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policies(
        self,
        request: apig20240327_models.ListPoliciesRequest,
    ) -> apig20240327_models.ListPoliciesResponse:
        """
        @summary ListPolicies
        
        @param request: ListPoliciesRequest
        @return: ListPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_policies_with_options(request, headers, runtime)

    async def list_policies_async(
        self,
        request: apig20240327_models.ListPoliciesRequest,
    ) -> apig20240327_models.ListPoliciesResponse:
        """
        @summary ListPolicies
        
        @param request: ListPoliciesRequest
        @return: ListPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_policies_with_options_async(request, headers, runtime)

    def list_policy_classes_with_options(
        self,
        request: apig20240327_models.ListPolicyClassesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListPolicyClassesResponse:
        """
        @summary ListPolicyClasses
        
        @param request: ListPolicyClassesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPolicyClassesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not UtilClient.is_unset(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not UtilClient.is_unset(request.direction):
            query['direction'] = request.direction
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicyClasses',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/policy-classes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListPolicyClassesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policy_classes_with_options_async(
        self,
        request: apig20240327_models.ListPolicyClassesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListPolicyClassesResponse:
        """
        @summary ListPolicyClasses
        
        @param request: ListPolicyClassesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPolicyClassesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not UtilClient.is_unset(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not UtilClient.is_unset(request.direction):
            query['direction'] = request.direction
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicyClasses',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/policy-classes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListPolicyClassesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policy_classes(
        self,
        request: apig20240327_models.ListPolicyClassesRequest,
    ) -> apig20240327_models.ListPolicyClassesResponse:
        """
        @summary ListPolicyClasses
        
        @param request: ListPolicyClassesRequest
        @return: ListPolicyClassesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_policy_classes_with_options(request, headers, runtime)

    async def list_policy_classes_async(
        self,
        request: apig20240327_models.ListPolicyClassesRequest,
    ) -> apig20240327_models.ListPolicyClassesResponse:
        """
        @summary ListPolicyClasses
        
        @param request: ListPolicyClassesRequest
        @return: ListPolicyClassesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_policy_classes_with_options_async(request, headers, runtime)

    def list_services_with_options(
        self,
        request: apig20240327_models.ListServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListServicesResponse:
        """
        @summary Queries a list of services.
        
        @param request: ListServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_type):
            query['sourceType'] = request.source_type
        if not UtilClient.is_unset(request.source_types):
            query['sourceTypes'] = request.source_types
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/services',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_services_with_options_async(
        self,
        request: apig20240327_models.ListServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListServicesResponse:
        """
        @summary Queries a list of services.
        
        @param request: ListServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_type):
            query['sourceType'] = request.source_type
        if not UtilClient.is_unset(request.source_types):
            query['sourceTypes'] = request.source_types
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/services',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_services(
        self,
        request: apig20240327_models.ListServicesRequest,
    ) -> apig20240327_models.ListServicesResponse:
        """
        @summary Queries a list of services.
        
        @param request: ListServicesRequest
        @return: ListServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_services_with_options(request, headers, runtime)

    async def list_services_async(
        self,
        request: apig20240327_models.ListServicesRequest,
    ) -> apig20240327_models.ListServicesResponse:
        """
        @summary Queries a list of services.
        
        @param request: ListServicesRequest
        @return: ListServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_services_with_options_async(request, headers, runtime)

    def list_ssl_certs_with_options(
        self,
        request: apig20240327_models.ListSslCertsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListSslCertsResponse:
        """
        @summary ListSslCerts
        
        @param request: ListSslCertsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSslCertsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name_like):
            query['certNameLike'] = request.cert_name_like
        if not UtilClient.is_unset(request.domain_name):
            query['domainName'] = request.domain_name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSslCerts',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/ssl/certs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListSslCertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ssl_certs_with_options_async(
        self,
        request: apig20240327_models.ListSslCertsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListSslCertsResponse:
        """
        @summary ListSslCerts
        
        @param request: ListSslCertsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSslCertsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name_like):
            query['certNameLike'] = request.cert_name_like
        if not UtilClient.is_unset(request.domain_name):
            query['domainName'] = request.domain_name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSslCerts',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/ssl/certs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListSslCertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ssl_certs(
        self,
        request: apig20240327_models.ListSslCertsRequest,
    ) -> apig20240327_models.ListSslCertsResponse:
        """
        @summary ListSslCerts
        
        @param request: ListSslCertsRequest
        @return: ListSslCertsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ssl_certs_with_options(request, headers, runtime)

    async def list_ssl_certs_async(
        self,
        request: apig20240327_models.ListSslCertsRequest,
    ) -> apig20240327_models.ListSslCertsResponse:
        """
        @summary ListSslCerts
        
        @param request: ListSslCertsRequest
        @return: ListSslCertsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_ssl_certs_with_options_async(request, headers, runtime)

    def list_zones_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListZonesResponse:
        """
        @summary Retrieve the availability zones under a cloud-native API gateway region
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListZonesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListZones',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/zones',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_zones_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.ListZonesResponse:
        """
        @summary Retrieve the availability zones under a cloud-native API gateway region
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListZonesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListZones',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/zones',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.ListZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_zones(self) -> apig20240327_models.ListZonesResponse:
        """
        @summary Retrieve the availability zones under a cloud-native API gateway region
        
        @return: ListZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_zones_with_options(headers, runtime)

    async def list_zones_async(self) -> apig20240327_models.ListZonesResponse:
        """
        @summary Retrieve the availability zones under a cloud-native API gateway region
        
        @return: ListZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_zones_with_options_async(headers, runtime)

    def query_consumer_authorization_rules_with_options(
        self,
        request: apig20240327_models.QueryConsumerAuthorizationRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.QueryConsumerAuthorizationRulesResponse:
        """
        @summary Queries a list of consumer authentication rules.
        
        @param request: QueryConsumerAuthorizationRulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryConsumerAuthorizationRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name_like):
            query['apiNameLike'] = request.api_name_like
        if not UtilClient.is_unset(request.consumer_id):
            query['consumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.consumer_name_like):
            query['consumerNameLike'] = request.consumer_name_like
        if not UtilClient.is_unset(request.environment_id):
            query['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.group_by_api):
            query['groupByApi'] = request.group_by_api
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_resource_id):
            query['parentResourceId'] = request.parent_resource_id
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.resource_types):
            query['resourceTypes'] = request.resource_types
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryConsumerAuthorizationRules',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/authorization-rules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.QueryConsumerAuthorizationRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_consumer_authorization_rules_with_options_async(
        self,
        request: apig20240327_models.QueryConsumerAuthorizationRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.QueryConsumerAuthorizationRulesResponse:
        """
        @summary Queries a list of consumer authentication rules.
        
        @param request: QueryConsumerAuthorizationRulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryConsumerAuthorizationRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name_like):
            query['apiNameLike'] = request.api_name_like
        if not UtilClient.is_unset(request.consumer_id):
            query['consumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.consumer_name_like):
            query['consumerNameLike'] = request.consumer_name_like
        if not UtilClient.is_unset(request.environment_id):
            query['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.group_by_api):
            query['groupByApi'] = request.group_by_api
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_resource_id):
            query['parentResourceId'] = request.parent_resource_id
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.resource_types):
            query['resourceTypes'] = request.resource_types
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryConsumerAuthorizationRules',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/authorization-rules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.QueryConsumerAuthorizationRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_consumer_authorization_rules(
        self,
        request: apig20240327_models.QueryConsumerAuthorizationRulesRequest,
    ) -> apig20240327_models.QueryConsumerAuthorizationRulesResponse:
        """
        @summary Queries a list of consumer authentication rules.
        
        @param request: QueryConsumerAuthorizationRulesRequest
        @return: QueryConsumerAuthorizationRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_consumer_authorization_rules_with_options(request, headers, runtime)

    async def query_consumer_authorization_rules_async(
        self,
        request: apig20240327_models.QueryConsumerAuthorizationRulesRequest,
    ) -> apig20240327_models.QueryConsumerAuthorizationRulesResponse:
        """
        @summary Queries a list of consumer authentication rules.
        
        @param request: QueryConsumerAuthorizationRulesRequest
        @return: QueryConsumerAuthorizationRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_consumer_authorization_rules_with_options_async(request, headers, runtime)

    def remove_consumer_authorization_rule_with_options(
        self,
        consumer_authorization_rule_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.RemoveConsumerAuthorizationRuleResponse:
        """
        @summary Deletes a consumer authorization rule.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveConsumerAuthorizationRuleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveConsumerAuthorizationRule',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/authorization-rules/{OpenApiUtilClient.get_encode_param(consumer_authorization_rule_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.RemoveConsumerAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_consumer_authorization_rule_with_options_async(
        self,
        consumer_authorization_rule_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.RemoveConsumerAuthorizationRuleResponse:
        """
        @summary Deletes a consumer authorization rule.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveConsumerAuthorizationRuleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveConsumerAuthorizationRule',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/authorization-rules/{OpenApiUtilClient.get_encode_param(consumer_authorization_rule_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.RemoveConsumerAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_consumer_authorization_rule(
        self,
        consumer_authorization_rule_id: str,
    ) -> apig20240327_models.RemoveConsumerAuthorizationRuleResponse:
        """
        @summary Deletes a consumer authorization rule.
        
        @return: RemoveConsumerAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_consumer_authorization_rule_with_options(consumer_authorization_rule_id, headers, runtime)

    async def remove_consumer_authorization_rule_async(
        self,
        consumer_authorization_rule_id: str,
    ) -> apig20240327_models.RemoveConsumerAuthorizationRuleResponse:
        """
        @summary Deletes a consumer authorization rule.
        
        @return: RemoveConsumerAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_consumer_authorization_rule_with_options_async(consumer_authorization_rule_id, headers, runtime)

    def restart_gateway_with_options(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.RestartGatewayResponse:
        """
        @summary Gateway Restart
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartGatewayResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RestartGateway',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/restart',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.RestartGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_gateway_with_options_async(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.RestartGatewayResponse:
        """
        @summary Gateway Restart
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartGatewayResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RestartGateway',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/restart',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.RestartGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_gateway(
        self,
        gateway_id: str,
    ) -> apig20240327_models.RestartGatewayResponse:
        """
        @summary Gateway Restart
        
        @return: RestartGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_gateway_with_options(gateway_id, headers, runtime)

    async def restart_gateway_async(
        self,
        gateway_id: str,
    ) -> apig20240327_models.RestartGatewayResponse:
        """
        @summary Gateway Restart
        
        @return: RestartGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.restart_gateway_with_options_async(gateway_id, headers, runtime)

    def un_deploy_mcp_server_with_options(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UnDeployMcpServerResponse:
        """
        @summary 取消发布MCP server
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnDeployMcpServerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UnDeployMcpServer',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/mcp-servers/{OpenApiUtilClient.get_encode_param(mcp_server_id)}/undeploy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UnDeployMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_deploy_mcp_server_with_options_async(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UnDeployMcpServerResponse:
        """
        @summary 取消发布MCP server
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnDeployMcpServerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UnDeployMcpServer',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/mcp-servers/{OpenApiUtilClient.get_encode_param(mcp_server_id)}/undeploy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UnDeployMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_deploy_mcp_server(
        self,
        mcp_server_id: str,
    ) -> apig20240327_models.UnDeployMcpServerResponse:
        """
        @summary 取消发布MCP server
        
        @return: UnDeployMcpServerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.un_deploy_mcp_server_with_options(mcp_server_id, headers, runtime)

    async def un_deploy_mcp_server_async(
        self,
        mcp_server_id: str,
    ) -> apig20240327_models.UnDeployMcpServerResponse:
        """
        @summary 取消发布MCP server
        
        @return: UnDeployMcpServerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.un_deploy_mcp_server_with_options_async(mcp_server_id, headers, runtime)

    def undeploy_http_api_with_options(
        self,
        http_api_id: str,
        request: apig20240327_models.UndeployHttpApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UndeployHttpApiResponse:
        """
        @summary Unpublishes an HTTP API.
        
        @param request: UndeployHttpApiRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UndeployHttpApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment_id):
            body['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.operation_id):
            body['operationId'] = request.operation_id
        if not UtilClient.is_unset(request.route_id):
            body['routeId'] = request.route_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UndeployHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/undeploy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UndeployHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def undeploy_http_api_with_options_async(
        self,
        http_api_id: str,
        request: apig20240327_models.UndeployHttpApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UndeployHttpApiResponse:
        """
        @summary Unpublishes an HTTP API.
        
        @param request: UndeployHttpApiRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UndeployHttpApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment_id):
            body['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.operation_id):
            body['operationId'] = request.operation_id
        if not UtilClient.is_unset(request.route_id):
            body['routeId'] = request.route_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UndeployHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/undeploy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UndeployHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def undeploy_http_api(
        self,
        http_api_id: str,
        request: apig20240327_models.UndeployHttpApiRequest,
    ) -> apig20240327_models.UndeployHttpApiResponse:
        """
        @summary Unpublishes an HTTP API.
        
        @param request: UndeployHttpApiRequest
        @return: UndeployHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.undeploy_http_api_with_options(http_api_id, request, headers, runtime)

    async def undeploy_http_api_async(
        self,
        http_api_id: str,
        request: apig20240327_models.UndeployHttpApiRequest,
    ) -> apig20240327_models.UndeployHttpApiResponse:
        """
        @summary Unpublishes an HTTP API.
        
        @param request: UndeployHttpApiRequest
        @return: UndeployHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.undeploy_http_api_with_options_async(http_api_id, request, headers, runtime)

    def uninstall_plugin_with_options(
        self,
        plugin_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UninstallPluginResponse:
        """
        @summary UninstallPlugin
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UninstallPluginResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UninstallPlugin',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/plugins/{OpenApiUtilClient.get_encode_param(plugin_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UninstallPluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_plugin_with_options_async(
        self,
        plugin_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UninstallPluginResponse:
        """
        @summary UninstallPlugin
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UninstallPluginResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UninstallPlugin',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/plugins/{OpenApiUtilClient.get_encode_param(plugin_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UninstallPluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_plugin(
        self,
        plugin_id: str,
    ) -> apig20240327_models.UninstallPluginResponse:
        """
        @summary UninstallPlugin
        
        @return: UninstallPluginResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.uninstall_plugin_with_options(plugin_id, headers, runtime)

    async def uninstall_plugin_async(
        self,
        plugin_id: str,
    ) -> apig20240327_models.UninstallPluginResponse:
        """
        @summary UninstallPlugin
        
        @return: UninstallPluginResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.uninstall_plugin_with_options_async(plugin_id, headers, runtime)

    def update_and_attach_policy_with_options(
        self,
        policy_id: str,
        request: apig20240327_models.UpdateAndAttachPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateAndAttachPolicyResponse:
        """
        @summary UpdateAndAttachPolicy
        
        @param request: UpdateAndAttachPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAndAttachPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not UtilClient.is_unset(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.environment_id):
            body['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAndAttachPolicy',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/policies/{OpenApiUtilClient.get_encode_param(policy_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateAndAttachPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_and_attach_policy_with_options_async(
        self,
        policy_id: str,
        request: apig20240327_models.UpdateAndAttachPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateAndAttachPolicyResponse:
        """
        @summary UpdateAndAttachPolicy
        
        @param request: UpdateAndAttachPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAndAttachPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not UtilClient.is_unset(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.environment_id):
            body['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAndAttachPolicy',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/policies/{OpenApiUtilClient.get_encode_param(policy_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateAndAttachPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_and_attach_policy(
        self,
        policy_id: str,
        request: apig20240327_models.UpdateAndAttachPolicyRequest,
    ) -> apig20240327_models.UpdateAndAttachPolicyResponse:
        """
        @summary UpdateAndAttachPolicy
        
        @param request: UpdateAndAttachPolicyRequest
        @return: UpdateAndAttachPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_and_attach_policy_with_options(policy_id, request, headers, runtime)

    async def update_and_attach_policy_async(
        self,
        policy_id: str,
        request: apig20240327_models.UpdateAndAttachPolicyRequest,
    ) -> apig20240327_models.UpdateAndAttachPolicyResponse:
        """
        @summary UpdateAndAttachPolicy
        
        @param request: UpdateAndAttachPolicyRequest
        @return: UpdateAndAttachPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_and_attach_policy_with_options_async(policy_id, request, headers, runtime)

    def update_consumer_with_options(
        self,
        consumer_id: str,
        request: apig20240327_models.UpdateConsumerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateConsumerResponse:
        """
        @summary 更新消费者
        
        @param request: UpdateConsumerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConsumerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_sk_identity_configs):
            body['akSkIdentityConfigs'] = request.ak_sk_identity_configs
        if not UtilClient.is_unset(request.apikey_identity_config):
            body['apikeyIdentityConfig'] = request.apikey_identity_config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        if not UtilClient.is_unset(request.jwt_identity_config):
            body['jwtIdentityConfig'] = request.jwt_identity_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConsumer',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/consumers/{OpenApiUtilClient.get_encode_param(consumer_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateConsumerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_consumer_with_options_async(
        self,
        consumer_id: str,
        request: apig20240327_models.UpdateConsumerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateConsumerResponse:
        """
        @summary 更新消费者
        
        @param request: UpdateConsumerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConsumerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ak_sk_identity_configs):
            body['akSkIdentityConfigs'] = request.ak_sk_identity_configs
        if not UtilClient.is_unset(request.apikey_identity_config):
            body['apikeyIdentityConfig'] = request.apikey_identity_config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        if not UtilClient.is_unset(request.jwt_identity_config):
            body['jwtIdentityConfig'] = request.jwt_identity_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConsumer',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/consumers/{OpenApiUtilClient.get_encode_param(consumer_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateConsumerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_consumer(
        self,
        consumer_id: str,
        request: apig20240327_models.UpdateConsumerRequest,
    ) -> apig20240327_models.UpdateConsumerResponse:
        """
        @summary 更新消费者
        
        @param request: UpdateConsumerRequest
        @return: UpdateConsumerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_consumer_with_options(consumer_id, request, headers, runtime)

    async def update_consumer_async(
        self,
        consumer_id: str,
        request: apig20240327_models.UpdateConsumerRequest,
    ) -> apig20240327_models.UpdateConsumerResponse:
        """
        @summary 更新消费者
        
        @param request: UpdateConsumerRequest
        @return: UpdateConsumerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_consumer_with_options_async(consumer_id, request, headers, runtime)

    def update_consumer_authorization_rule_with_options(
        self,
        consumer_id: str,
        consumer_authorization_rule_id: str,
        request: apig20240327_models.UpdateConsumerAuthorizationRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateConsumerAuthorizationRuleResponse:
        """
        @summary 更新消费者授权规则
        
        @param request: UpdateConsumerAuthorizationRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConsumerAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authorization_resource_infos):
            body['authorizationResourceInfos'] = request.authorization_resource_infos
        if not UtilClient.is_unset(request.expire_mode):
            body['expireMode'] = request.expire_mode
        if not UtilClient.is_unset(request.expire_timestamp):
            body['expireTimestamp'] = request.expire_timestamp
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConsumerAuthorizationRule',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/consumers/{OpenApiUtilClient.get_encode_param(consumer_id)}/authorization-rules/{OpenApiUtilClient.get_encode_param(consumer_authorization_rule_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateConsumerAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_consumer_authorization_rule_with_options_async(
        self,
        consumer_id: str,
        consumer_authorization_rule_id: str,
        request: apig20240327_models.UpdateConsumerAuthorizationRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateConsumerAuthorizationRuleResponse:
        """
        @summary 更新消费者授权规则
        
        @param request: UpdateConsumerAuthorizationRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConsumerAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authorization_resource_infos):
            body['authorizationResourceInfos'] = request.authorization_resource_infos
        if not UtilClient.is_unset(request.expire_mode):
            body['expireMode'] = request.expire_mode
        if not UtilClient.is_unset(request.expire_timestamp):
            body['expireTimestamp'] = request.expire_timestamp
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConsumerAuthorizationRule',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/consumers/{OpenApiUtilClient.get_encode_param(consumer_id)}/authorization-rules/{OpenApiUtilClient.get_encode_param(consumer_authorization_rule_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateConsumerAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_consumer_authorization_rule(
        self,
        consumer_id: str,
        consumer_authorization_rule_id: str,
        request: apig20240327_models.UpdateConsumerAuthorizationRuleRequest,
    ) -> apig20240327_models.UpdateConsumerAuthorizationRuleResponse:
        """
        @summary 更新消费者授权规则
        
        @param request: UpdateConsumerAuthorizationRuleRequest
        @return: UpdateConsumerAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_consumer_authorization_rule_with_options(consumer_id, consumer_authorization_rule_id, request, headers, runtime)

    async def update_consumer_authorization_rule_async(
        self,
        consumer_id: str,
        consumer_authorization_rule_id: str,
        request: apig20240327_models.UpdateConsumerAuthorizationRuleRequest,
    ) -> apig20240327_models.UpdateConsumerAuthorizationRuleResponse:
        """
        @summary 更新消费者授权规则
        
        @param request: UpdateConsumerAuthorizationRuleRequest
        @return: UpdateConsumerAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_consumer_authorization_rule_with_options_async(consumer_id, consumer_authorization_rule_id, request, headers, runtime)

    def update_domain_with_options(
        self,
        domain_id: str,
        request: apig20240327_models.UpdateDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateDomainResponse:
        """
        @summary Updates a domain name.
        
        @param request: UpdateDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDomainResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ca_cert_identifier):
            body['caCertIdentifier'] = request.ca_cert_identifier
        if not UtilClient.is_unset(request.cert_identifier):
            body['certIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.client_cacert):
            body['clientCACert'] = request.client_cacert
        if not UtilClient.is_unset(request.force_https):
            body['forceHttps'] = request.force_https
        if not UtilClient.is_unset(request.http_2option):
            body['http2Option'] = request.http_2option
        if not UtilClient.is_unset(request.m_tlsenabled):
            body['mTLSEnabled'] = request.m_tlsenabled
        if not UtilClient.is_unset(request.protocol):
            body['protocol'] = request.protocol
        if not UtilClient.is_unset(request.tls_cipher_suites_config):
            body['tlsCipherSuitesConfig'] = request.tls_cipher_suites_config
        if not UtilClient.is_unset(request.tls_max):
            body['tlsMax'] = request.tls_max
        if not UtilClient.is_unset(request.tls_min):
            body['tlsMin'] = request.tls_min
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDomain',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/domains/{OpenApiUtilClient.get_encode_param(domain_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_domain_with_options_async(
        self,
        domain_id: str,
        request: apig20240327_models.UpdateDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateDomainResponse:
        """
        @summary Updates a domain name.
        
        @param request: UpdateDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDomainResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ca_cert_identifier):
            body['caCertIdentifier'] = request.ca_cert_identifier
        if not UtilClient.is_unset(request.cert_identifier):
            body['certIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.client_cacert):
            body['clientCACert'] = request.client_cacert
        if not UtilClient.is_unset(request.force_https):
            body['forceHttps'] = request.force_https
        if not UtilClient.is_unset(request.http_2option):
            body['http2Option'] = request.http_2option
        if not UtilClient.is_unset(request.m_tlsenabled):
            body['mTLSEnabled'] = request.m_tlsenabled
        if not UtilClient.is_unset(request.protocol):
            body['protocol'] = request.protocol
        if not UtilClient.is_unset(request.tls_cipher_suites_config):
            body['tlsCipherSuitesConfig'] = request.tls_cipher_suites_config
        if not UtilClient.is_unset(request.tls_max):
            body['tlsMax'] = request.tls_max
        if not UtilClient.is_unset(request.tls_min):
            body['tlsMin'] = request.tls_min
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDomain',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/domains/{OpenApiUtilClient.get_encode_param(domain_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_domain(
        self,
        domain_id: str,
        request: apig20240327_models.UpdateDomainRequest,
    ) -> apig20240327_models.UpdateDomainResponse:
        """
        @summary Updates a domain name.
        
        @param request: UpdateDomainRequest
        @return: UpdateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_domain_with_options(domain_id, request, headers, runtime)

    async def update_domain_async(
        self,
        domain_id: str,
        request: apig20240327_models.UpdateDomainRequest,
    ) -> apig20240327_models.UpdateDomainResponse:
        """
        @summary Updates a domain name.
        
        @param request: UpdateDomainRequest
        @return: UpdateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_domain_with_options_async(domain_id, request, headers, runtime)

    def update_environment_with_options(
        self,
        environment_id: str,
        request: apig20240327_models.UpdateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateEnvironmentResponse:
        """
        @deprecated OpenAPI UpdateEnvironment is deprecated
        
        @summary UpdateEnvironment
        
        @param request: UpdateEnvironmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEnvironmentResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['alias'] = request.alias
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEnvironment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/environments/{OpenApiUtilClient.get_encode_param(environment_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_environment_with_options_async(
        self,
        environment_id: str,
        request: apig20240327_models.UpdateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateEnvironmentResponse:
        """
        @deprecated OpenAPI UpdateEnvironment is deprecated
        
        @summary UpdateEnvironment
        
        @param request: UpdateEnvironmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEnvironmentResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['alias'] = request.alias
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEnvironment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/environments/{OpenApiUtilClient.get_encode_param(environment_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_environment(
        self,
        environment_id: str,
        request: apig20240327_models.UpdateEnvironmentRequest,
    ) -> apig20240327_models.UpdateEnvironmentResponse:
        """
        @deprecated OpenAPI UpdateEnvironment is deprecated
        
        @summary UpdateEnvironment
        
        @param request: UpdateEnvironmentRequest
        @return: UpdateEnvironmentResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_environment_with_options(environment_id, request, headers, runtime)

    async def update_environment_async(
        self,
        environment_id: str,
        request: apig20240327_models.UpdateEnvironmentRequest,
    ) -> apig20240327_models.UpdateEnvironmentResponse:
        """
        @deprecated OpenAPI UpdateEnvironment is deprecated
        
        @summary UpdateEnvironment
        
        @param request: UpdateEnvironmentRequest
        @return: UpdateEnvironmentResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_environment_with_options_async(environment_id, request, headers, runtime)

    def update_gateway_feature_with_options(
        self,
        gateway_id: str,
        name: str,
        request: apig20240327_models.UpdateGatewayFeatureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateGatewayFeatureResponse:
        """
        @summary Get the feature configuration of the gateway
        
        @param request: UpdateGatewayFeatureRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGatewayFeatureResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGatewayFeature',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/gateway-features/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateGatewayFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_feature_with_options_async(
        self,
        gateway_id: str,
        name: str,
        request: apig20240327_models.UpdateGatewayFeatureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateGatewayFeatureResponse:
        """
        @summary Get the feature configuration of the gateway
        
        @param request: UpdateGatewayFeatureRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGatewayFeatureResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGatewayFeature',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/gateway-features/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateGatewayFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_feature(
        self,
        gateway_id: str,
        name: str,
        request: apig20240327_models.UpdateGatewayFeatureRequest,
    ) -> apig20240327_models.UpdateGatewayFeatureResponse:
        """
        @summary Get the feature configuration of the gateway
        
        @param request: UpdateGatewayFeatureRequest
        @return: UpdateGatewayFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_gateway_feature_with_options(gateway_id, name, request, headers, runtime)

    async def update_gateway_feature_async(
        self,
        gateway_id: str,
        name: str,
        request: apig20240327_models.UpdateGatewayFeatureRequest,
    ) -> apig20240327_models.UpdateGatewayFeatureResponse:
        """
        @summary Get the feature configuration of the gateway
        
        @param request: UpdateGatewayFeatureRequest
        @return: UpdateGatewayFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_gateway_feature_with_options_async(gateway_id, name, request, headers, runtime)

    def update_gateway_name_with_options(
        self,
        gateway_id: str,
        request: apig20240327_models.UpdateGatewayNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateGatewayNameResponse:
        """
        @summary Change the name of a gateway instance
        
        @param request: UpdateGatewayNameRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGatewayNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGatewayName',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/name',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateGatewayNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_name_with_options_async(
        self,
        gateway_id: str,
        request: apig20240327_models.UpdateGatewayNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateGatewayNameResponse:
        """
        @summary Change the name of a gateway instance
        
        @param request: UpdateGatewayNameRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGatewayNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGatewayName',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/name',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateGatewayNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_name(
        self,
        gateway_id: str,
        request: apig20240327_models.UpdateGatewayNameRequest,
    ) -> apig20240327_models.UpdateGatewayNameResponse:
        """
        @summary Change the name of a gateway instance
        
        @param request: UpdateGatewayNameRequest
        @return: UpdateGatewayNameResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_gateway_name_with_options(gateway_id, request, headers, runtime)

    async def update_gateway_name_async(
        self,
        gateway_id: str,
        request: apig20240327_models.UpdateGatewayNameRequest,
    ) -> apig20240327_models.UpdateGatewayNameResponse:
        """
        @summary Change the name of a gateway instance
        
        @param request: UpdateGatewayNameRequest
        @return: UpdateGatewayNameResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_gateway_name_with_options_async(gateway_id, request, headers, runtime)

    def update_http_api_with_options(
        self,
        http_api_id: str,
        request: apig20240327_models.UpdateHttpApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateHttpApiResponse:
        """
        @summary Updates an HTTP API.
        
        @param request: UpdateHttpApiRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHttpApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_protocols):
            body['agentProtocols'] = request.agent_protocols
        if not UtilClient.is_unset(request.ai_protocols):
            body['aiProtocols'] = request.ai_protocols
        if not UtilClient.is_unset(request.auth_config):
            body['authConfig'] = request.auth_config
        if not UtilClient.is_unset(request.base_path):
            body['basePath'] = request.base_path
        if not UtilClient.is_unset(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.enable_auth):
            body['enableAuth'] = request.enable_auth
        if not UtilClient.is_unset(request.first_byte_timeout):
            body['firstByteTimeout'] = request.first_byte_timeout
        if not UtilClient.is_unset(request.ingress_config):
            body['ingressConfig'] = request.ingress_config
        if not UtilClient.is_unset(request.only_change_config):
            body['onlyChangeConfig'] = request.only_change_config
        if not UtilClient.is_unset(request.protocols):
            body['protocols'] = request.protocols
        if not UtilClient.is_unset(request.remove_base_path_on_forward):
            body['removeBasePathOnForward'] = request.remove_base_path_on_forward
        if not UtilClient.is_unset(request.version_config):
            body['versionConfig'] = request.version_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_http_api_with_options_async(
        self,
        http_api_id: str,
        request: apig20240327_models.UpdateHttpApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateHttpApiResponse:
        """
        @summary Updates an HTTP API.
        
        @param request: UpdateHttpApiRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHttpApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_protocols):
            body['agentProtocols'] = request.agent_protocols
        if not UtilClient.is_unset(request.ai_protocols):
            body['aiProtocols'] = request.ai_protocols
        if not UtilClient.is_unset(request.auth_config):
            body['authConfig'] = request.auth_config
        if not UtilClient.is_unset(request.base_path):
            body['basePath'] = request.base_path
        if not UtilClient.is_unset(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.enable_auth):
            body['enableAuth'] = request.enable_auth
        if not UtilClient.is_unset(request.first_byte_timeout):
            body['firstByteTimeout'] = request.first_byte_timeout
        if not UtilClient.is_unset(request.ingress_config):
            body['ingressConfig'] = request.ingress_config
        if not UtilClient.is_unset(request.only_change_config):
            body['onlyChangeConfig'] = request.only_change_config
        if not UtilClient.is_unset(request.protocols):
            body['protocols'] = request.protocols
        if not UtilClient.is_unset(request.remove_base_path_on_forward):
            body['removeBasePathOnForward'] = request.remove_base_path_on_forward
        if not UtilClient.is_unset(request.version_config):
            body['versionConfig'] = request.version_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHttpApi',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_http_api(
        self,
        http_api_id: str,
        request: apig20240327_models.UpdateHttpApiRequest,
    ) -> apig20240327_models.UpdateHttpApiResponse:
        """
        @summary Updates an HTTP API.
        
        @param request: UpdateHttpApiRequest
        @return: UpdateHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_http_api_with_options(http_api_id, request, headers, runtime)

    async def update_http_api_async(
        self,
        http_api_id: str,
        request: apig20240327_models.UpdateHttpApiRequest,
    ) -> apig20240327_models.UpdateHttpApiResponse:
        """
        @summary Updates an HTTP API.
        
        @param request: UpdateHttpApiRequest
        @return: UpdateHttpApiResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_http_api_with_options_async(http_api_id, request, headers, runtime)

    def update_http_api_operation_with_options(
        self,
        http_api_id: str,
        operation_id: str,
        request: apig20240327_models.UpdateHttpApiOperationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateHttpApiOperationResponse:
        """
        @summary Update Operation
        
        @param request: UpdateHttpApiOperationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHttpApiOperationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation):
            body['operation'] = request.operation
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHttpApiOperation',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/operations/{OpenApiUtilClient.get_encode_param(operation_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateHttpApiOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_http_api_operation_with_options_async(
        self,
        http_api_id: str,
        operation_id: str,
        request: apig20240327_models.UpdateHttpApiOperationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateHttpApiOperationResponse:
        """
        @summary Update Operation
        
        @param request: UpdateHttpApiOperationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHttpApiOperationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation):
            body['operation'] = request.operation
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHttpApiOperation',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/operations/{OpenApiUtilClient.get_encode_param(operation_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateHttpApiOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_http_api_operation(
        self,
        http_api_id: str,
        operation_id: str,
        request: apig20240327_models.UpdateHttpApiOperationRequest,
    ) -> apig20240327_models.UpdateHttpApiOperationResponse:
        """
        @summary Update Operation
        
        @param request: UpdateHttpApiOperationRequest
        @return: UpdateHttpApiOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_http_api_operation_with_options(http_api_id, operation_id, request, headers, runtime)

    async def update_http_api_operation_async(
        self,
        http_api_id: str,
        operation_id: str,
        request: apig20240327_models.UpdateHttpApiOperationRequest,
    ) -> apig20240327_models.UpdateHttpApiOperationResponse:
        """
        @summary Update Operation
        
        @param request: UpdateHttpApiOperationRequest
        @return: UpdateHttpApiOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_http_api_operation_with_options_async(http_api_id, operation_id, request, headers, runtime)

    def update_http_api_route_with_options(
        self,
        http_api_id: str,
        route_id: str,
        request: apig20240327_models.UpdateHttpApiRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateHttpApiRouteResponse:
        """
        @summary Updates the route of an HTTP API.
        
        @param request: UpdateHttpApiRouteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHttpApiRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not UtilClient.is_unset(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not UtilClient.is_unset(request.environment_id):
            body['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.match):
            body['match'] = request.match
        if not UtilClient.is_unset(request.mcp_route_config):
            body['mcpRouteConfig'] = request.mcp_route_config
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHttpApiRoute',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/routes/{OpenApiUtilClient.get_encode_param(route_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateHttpApiRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_http_api_route_with_options_async(
        self,
        http_api_id: str,
        route_id: str,
        request: apig20240327_models.UpdateHttpApiRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateHttpApiRouteResponse:
        """
        @summary Updates the route of an HTTP API.
        
        @param request: UpdateHttpApiRouteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHttpApiRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not UtilClient.is_unset(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not UtilClient.is_unset(request.environment_id):
            body['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.match):
            body['match'] = request.match
        if not UtilClient.is_unset(request.mcp_route_config):
            body['mcpRouteConfig'] = request.mcp_route_config
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHttpApiRoute',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/http-apis/{OpenApiUtilClient.get_encode_param(http_api_id)}/routes/{OpenApiUtilClient.get_encode_param(route_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateHttpApiRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_http_api_route(
        self,
        http_api_id: str,
        route_id: str,
        request: apig20240327_models.UpdateHttpApiRouteRequest,
    ) -> apig20240327_models.UpdateHttpApiRouteResponse:
        """
        @summary Updates the route of an HTTP API.
        
        @param request: UpdateHttpApiRouteRequest
        @return: UpdateHttpApiRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_http_api_route_with_options(http_api_id, route_id, request, headers, runtime)

    async def update_http_api_route_async(
        self,
        http_api_id: str,
        route_id: str,
        request: apig20240327_models.UpdateHttpApiRouteRequest,
    ) -> apig20240327_models.UpdateHttpApiRouteResponse:
        """
        @summary Updates the route of an HTTP API.
        
        @param request: UpdateHttpApiRouteRequest
        @return: UpdateHttpApiRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_http_api_route_with_options_async(http_api_id, route_id, request, headers, runtime)

    def update_mcp_server_with_options(
        self,
        mcp_server_id: str,
        request: apig20240327_models.UpdateMcpServerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateMcpServerResponse:
        """
        @summary 更新MCP server
        
        @param request: UpdateMcpServerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMcpServerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assembled_sources):
            body['assembledSources'] = request.assembled_sources
        if not UtilClient.is_unset(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not UtilClient.is_unset(request.exposed_uri_path):
            body['exposedUriPath'] = request.exposed_uri_path
        if not UtilClient.is_unset(request.match):
            body['match'] = request.match
        if not UtilClient.is_unset(request.mcp_statistics_enable):
            body['mcpStatisticsEnable'] = request.mcp_statistics_enable
        if not UtilClient.is_unset(request.protocol):
            body['protocol'] = request.protocol
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMcpServer',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/mcp-servers/{OpenApiUtilClient.get_encode_param(mcp_server_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mcp_server_with_options_async(
        self,
        mcp_server_id: str,
        request: apig20240327_models.UpdateMcpServerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdateMcpServerResponse:
        """
        @summary 更新MCP server
        
        @param request: UpdateMcpServerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMcpServerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assembled_sources):
            body['assembledSources'] = request.assembled_sources
        if not UtilClient.is_unset(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not UtilClient.is_unset(request.exposed_uri_path):
            body['exposedUriPath'] = request.exposed_uri_path
        if not UtilClient.is_unset(request.match):
            body['match'] = request.match
        if not UtilClient.is_unset(request.mcp_statistics_enable):
            body['mcpStatisticsEnable'] = request.mcp_statistics_enable
        if not UtilClient.is_unset(request.protocol):
            body['protocol'] = request.protocol
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMcpServer',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/mcp-servers/{OpenApiUtilClient.get_encode_param(mcp_server_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdateMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mcp_server(
        self,
        mcp_server_id: str,
        request: apig20240327_models.UpdateMcpServerRequest,
    ) -> apig20240327_models.UpdateMcpServerResponse:
        """
        @summary 更新MCP server
        
        @param request: UpdateMcpServerRequest
        @return: UpdateMcpServerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_mcp_server_with_options(mcp_server_id, request, headers, runtime)

    async def update_mcp_server_async(
        self,
        mcp_server_id: str,
        request: apig20240327_models.UpdateMcpServerRequest,
    ) -> apig20240327_models.UpdateMcpServerResponse:
        """
        @summary 更新MCP server
        
        @param request: UpdateMcpServerRequest
        @return: UpdateMcpServerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_mcp_server_with_options_async(mcp_server_id, request, headers, runtime)

    def update_plugin_attachment_with_options(
        self,
        plugin_attachment_id: str,
        request: apig20240327_models.UpdatePluginAttachmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdatePluginAttachmentResponse:
        """
        @summary 更新挂载规则API
        
        @param request: UpdatePluginAttachmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePluginAttachmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        if not UtilClient.is_unset(request.plugin_config):
            body['pluginConfig'] = request.plugin_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePluginAttachment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/plugin-attachments/{OpenApiUtilClient.get_encode_param(plugin_attachment_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdatePluginAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_plugin_attachment_with_options_async(
        self,
        plugin_attachment_id: str,
        request: apig20240327_models.UpdatePluginAttachmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdatePluginAttachmentResponse:
        """
        @summary 更新挂载规则API
        
        @param request: UpdatePluginAttachmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePluginAttachmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        if not UtilClient.is_unset(request.plugin_config):
            body['pluginConfig'] = request.plugin_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePluginAttachment',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/plugin-attachments/{OpenApiUtilClient.get_encode_param(plugin_attachment_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdatePluginAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_plugin_attachment(
        self,
        plugin_attachment_id: str,
        request: apig20240327_models.UpdatePluginAttachmentRequest,
    ) -> apig20240327_models.UpdatePluginAttachmentResponse:
        """
        @summary 更新挂载规则API
        
        @param request: UpdatePluginAttachmentRequest
        @return: UpdatePluginAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_plugin_attachment_with_options(plugin_attachment_id, request, headers, runtime)

    async def update_plugin_attachment_async(
        self,
        plugin_attachment_id: str,
        request: apig20240327_models.UpdatePluginAttachmentRequest,
    ) -> apig20240327_models.UpdatePluginAttachmentResponse:
        """
        @summary 更新挂载规则API
        
        @param request: UpdatePluginAttachmentRequest
        @return: UpdatePluginAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_plugin_attachment_with_options_async(plugin_attachment_id, request, headers, runtime)

    def update_policy_with_options(
        self,
        policy_id: str,
        request: apig20240327_models.UpdatePolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdatePolicyResponse:
        """
        @summary Update Policy
        
        @param request: UpdatePolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePolicy',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v2/policies/{OpenApiUtilClient.get_encode_param(policy_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_policy_with_options_async(
        self,
        policy_id: str,
        request: apig20240327_models.UpdatePolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpdatePolicyResponse:
        """
        @summary Update Policy
        
        @param request: UpdatePolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePolicy',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v2/policies/{OpenApiUtilClient.get_encode_param(policy_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpdatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_policy(
        self,
        policy_id: str,
        request: apig20240327_models.UpdatePolicyRequest,
    ) -> apig20240327_models.UpdatePolicyResponse:
        """
        @summary Update Policy
        
        @param request: UpdatePolicyRequest
        @return: UpdatePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_policy_with_options(policy_id, request, headers, runtime)

    async def update_policy_async(
        self,
        policy_id: str,
        request: apig20240327_models.UpdatePolicyRequest,
    ) -> apig20240327_models.UpdatePolicyResponse:
        """
        @summary Update Policy
        
        @param request: UpdatePolicyRequest
        @return: UpdatePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_policy_with_options_async(policy_id, request, headers, runtime)

    def upgrade_gateway_with_options(
        self,
        gateway_id: str,
        request: apig20240327_models.UpgradeGatewayRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpgradeGatewayResponse:
        """
        @summary Upgrade the gateway version
        
        @param request: UpgradeGatewayRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeGatewayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeGateway',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/upgrade',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpgradeGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_gateway_with_options_async(
        self,
        gateway_id: str,
        request: apig20240327_models.UpgradeGatewayRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> apig20240327_models.UpgradeGatewayResponse:
        """
        @summary Upgrade the gateway version
        
        @param request: UpgradeGatewayRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeGatewayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeGateway',
            version='2024-03-27',
            protocol='HTTPS',
            pathname=f'/v1/gateways/{OpenApiUtilClient.get_encode_param(gateway_id)}/upgrade',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            apig20240327_models.UpgradeGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_gateway(
        self,
        gateway_id: str,
        request: apig20240327_models.UpgradeGatewayRequest,
    ) -> apig20240327_models.UpgradeGatewayResponse:
        """
        @summary Upgrade the gateway version
        
        @param request: UpgradeGatewayRequest
        @return: UpgradeGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upgrade_gateway_with_options(gateway_id, request, headers, runtime)

    async def upgrade_gateway_async(
        self,
        gateway_id: str,
        request: apig20240327_models.UpgradeGatewayRequest,
    ) -> apig20240327_models.UpgradeGatewayResponse:
        """
        @summary Upgrade the gateway version
        
        @param request: UpgradeGatewayRequest
        @return: UpgradeGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upgrade_gateway_with_options_async(gateway_id, request, headers, runtime)
