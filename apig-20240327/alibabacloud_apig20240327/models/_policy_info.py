# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class PolicyInfo(DaraModel):
    def __init__(
        self,
        attachments: List[main_models.Attachment] = None,
        class_alias: str = None,
        class_name: str = None,
        config: str = None,
        direction: str = None,
        execute_priority: str = None,
        execute_stage: str = None,
        name: str = None,
        policy_id: str = None,
        type: str = None,
    ):
        # The mount information.
        self.attachments = attachments
        # The policy class alias.
        self.class_alias = class_alias
        # The class name supported by the policy. Different policies support different mount points. This parameter is used in combination with AttachResourceType.
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
        self.class_name = class_name
        # The policy configurations.
        self.config = config
        # The direction of traffic on which the policy takes effect. Valid values:
        # 
        # *   OutBound
        # *   InBound
        # *   Both
        self.direction = direction
        # The execution priority.
        self.execute_priority = execute_priority
        # The execution phase.
        # 
        # Valid values:
        # 
        # *   PluginStatistic
        # *   PluginAuthorization
        # *   PluginPre
        # *   PluginAuthentication
        # *   PluginDefault
        # *   PluginPost
        self.execute_stage = execute_stage
        # The policy name.
        self.name = name
        # The policy ID.
        self.policy_id = policy_id
        # The policy type.
        self.type = type

    def validate(self):
        if self.attachments:
            for v1 in self.attachments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['attachments'] = []
        if self.attachments is not None:
            for k1 in self.attachments:
                result['attachments'].append(k1.to_map() if k1 else None)

        if self.class_alias is not None:
            result['classAlias'] = self.class_alias

        if self.class_name is not None:
            result['className'] = self.class_name

        if self.config is not None:
            result['config'] = self.config

        if self.direction is not None:
            result['direction'] = self.direction

        if self.execute_priority is not None:
            result['executePriority'] = self.execute_priority

        if self.execute_stage is not None:
            result['executeStage'] = self.execute_stage

        if self.name is not None:
            result['name'] = self.name

        if self.policy_id is not None:
            result['policyId'] = self.policy_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('attachments') is not None:
            for k1 in m.get('attachments'):
                temp_model = main_models.Attachment()
                self.attachments.append(temp_model.from_map(k1))

        if m.get('classAlias') is not None:
            self.class_alias = m.get('classAlias')

        if m.get('className') is not None:
            self.class_name = m.get('className')

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('direction') is not None:
            self.direction = m.get('direction')

        if m.get('executePriority') is not None:
            self.execute_priority = m.get('executePriority')

        if m.get('executeStage') is not None:
            self.execute_stage = m.get('executeStage')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

