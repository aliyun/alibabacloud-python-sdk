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
        # List of attachment point IDs.
        # 
        # This parameter is required.
        self.attach_resource_ids = attach_resource_ids
        # Types of attachment points supported by the policy.
        # 
        # - HttpApi: HttpApi.
        # - Operation: Operation of HttpApi.
        # - GatewayRoute: Gateway route.
        # - GatewayService: Gateway service.
        # - GatewayServicePort: Gateway service port.
        # - Domain: Gateway domain.
        # - Gateway: Gateway.
        # 
        # This parameter is required.
        self.attach_resource_type = attach_resource_type
        # The class name types supported by the policy. Different policies support different attachment points, to be used in conjunction with `attachResourceType`.
        # 
        # - RateLimit: Traffic control, supports HttpApi, Operation, GatewayRoute.
        # - ConcurrencyLimit: Concurrency control, supports HttpApi, Operation, GatewayRoute.
        # - CircuitBreaker: Circuit breaking and degradation, supports HttpApi, Operation, GatewayRoute.
        # - HttpRewrite: HTTP rewrite, supports HttpApi, Operation, GatewayRoute.
        # - HeaderModify: Header modification, supports HttpApi, Operation, GatewayRoute.
        # - Cors: Cross-origin, supports HttpApi, Operation, GatewayRoute.
        # - FlowCopy: Traffic replication, supports HttpApi, Operation, GatewayRoute.
        # - Timeout: Timeout, supports HttpApi, Operation, GatewayRoute.
        # - Retry: Retry, supports HttpApi, Operation, GatewayRoute.
        # - IpAccessControl: IP access control, supports HttpApi, Operation, GatewayRoute, Domain, Gateway.
        # - DirectResponse: Mock, supports Operation, GatewayRoute.
        # - Redirect: Redirection, supports GatewayRoute.
        # - Fallback: Fallback, supports Operation, GatewayRoute.
        # - ServiceTls: Service TLS authentication, supports GatewayService.
        # - ServiceLb: Service load balancing, supports GatewayService.
        # - ServicePortTls: Service port TLS authentication, supports GatewayServicePort.
        # 
        # - Waf: WAF protection, supports GatewayRoute, Gateway.
        # - JWTAuth: JWT global authentication, supports Gateway.
        # - OIDCAuth: OIDC global authentication, supports Gateway.
        # - ExternalZAuth: Custom authorization, supports Gateway.
        # 
        # This parameter is required.
        self.class_name = class_name
        # Configuration information.
        # 
        # This parameter is required.
        self.config = config
        # Policy description.
        self.description = description
        # Environment ID.
        self.environment_id = environment_id
        # Gateway ID.
        self.gateway_id = gateway_id
        # Policy name.
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

