# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateAndAttachPolicyRequest(DaraModel):
    def __init__(
        self,
        attach_resource_ids: List[str] = None,
        attach_resource_type: str = None,
        class_name: str = None,
        config: str = None,
        description: str = None,
        environment_id: str = None,
        gateway_id: str = None,
        name: str = None,
    ):
        # The IDs of the resources to be associated with the policy.
        # 
        # This parameter is required.
        self.attach_resource_ids = attach_resource_ids
        # The supported resource type. Valid values:
        # 
        # *   HttpApi: an HTTP API
        # *   Operation: an operation in an HTTP API
        # *   GatewayRoute: a route
        # *   GatewayService: a service
        # *   GatewayServicePort: a service port
        # *   Domain: a domain name
        # *   Gateway: an instance
        # 
        # This parameter is required.
        self.attach_resource_type = attach_resource_type
        # The class name supported by the policy. Different policies support different resources. This parameter is used in combination with AttachResourceType.
        # 
        # *   RateLimit: throttles traffic. Supported: HttpApi, Operation, and GatewayRoute.
        # *   ConcurrencyLimit: controls concurrency. Supported: HttpApi, Operation, and GatewayRoute.
        # *   CircuitBreaker: breaks circuits and downgrades traffic. Supported: HttpApi, Operation, and GatewayRoute.
        # *   HttpRewrite: rewrites HTTP traffic. Supported: HttpApi, Operation, and GatewayRoute.
        # *   HeaderModify: modifies headers. Supported: HttpApi, Operation, and GatewayRoute.
        # *   Cors: supports CORS. Supported: HttpApi, Operation, and GatewayRoute.
        # *   FlowCopy: replicates traffic. Supported: HttpApi, Operation, and GatewayRoute.
        # *   Timeout: times out requests. Supported: HttpApi, Operation, and GatewayRoute.
        # *   Retry: retries requests. Supported: HttpApi, Operation, and GatewayRoute.
        # *   IpAccessControl: implements IP address-based access control. Supported: HttpApi, Operation, GatewayRoute, Domain, and Gateway.
        # *   DirectResponse: mocks responses. Supported: Operation and GatewayRoute.
        # *   Redirect: redirects traffic. Supported: GatewayRoute.
        # *   Fallback: implements fallback. Supported: Operation and GatewayRoute.
        # *   ServiceTls: implements TLS authentication. Supported: GatewayService.
        # *   ServiceLb: balances loads. Supported: GatewayService.
        # *   ServicePortTls: implements service port TLS authentication. Supported: GatewayServicePort.
        # *   Waf: implements WAF protection. Supported: GatewayRoute and Gateway.
        # *   JWTAuth: implements global JWT authentication. Supported: Gateway.
        # *   OIDCAuth: implements global OIDC authentication. Supported: Gateway.
        # *   ExternalZAuth: implements custom authentication. Supported: Gateway.
        # 
        # This parameter is required.
        self.class_name = class_name
        # The policy configurations.
        # 
        # This parameter is required.
        self.config = config
        # The policy description.
        self.description = description
        # The environment ID.
        self.environment_id = environment_id
        # The instance ID.
        self.gateway_id = gateway_id
        # The policy name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_resource_ids is not None:
            result['attachResourceIds'] = self.attach_resource_ids

        if self.attach_resource_type is not None:
            result['attachResourceType'] = self.attach_resource_type

        if self.class_name is not None:
            result['className'] = self.class_name

        if self.config is not None:
            result['config'] = self.config

        if self.description is not None:
            result['description'] = self.description

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachResourceIds') is not None:
            self.attach_resource_ids = m.get('attachResourceIds')

        if m.get('attachResourceType') is not None:
            self.attach_resource_type = m.get('attachResourceType')

        if m.get('className') is not None:
            self.class_name = m.get('className')

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

