# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class ListSecurityPolicyRelationsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        secrity_policy_relations: List[main_models.ListSecurityPolicyRelationsResponseBodySecrityPolicyRelations] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The security policies and the listeners that are associated with the security policies.
        self.secrity_policy_relations = secrity_policy_relations

    def validate(self):
        if self.secrity_policy_relations:
            for v1 in self.secrity_policy_relations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SecrityPolicyRelations'] = []
        if self.secrity_policy_relations is not None:
            for k1 in self.secrity_policy_relations:
                result['SecrityPolicyRelations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.secrity_policy_relations = []
        if m.get('SecrityPolicyRelations') is not None:
            for k1 in m.get('SecrityPolicyRelations'):
                temp_model = main_models.ListSecurityPolicyRelationsResponseBodySecrityPolicyRelations()
                self.secrity_policy_relations.append(temp_model.from_map(k1))

        return self

class ListSecurityPolicyRelationsResponseBodySecrityPolicyRelations(DaraModel):
    def __init__(
        self,
        related_listeners: List[main_models.ListSecurityPolicyRelationsResponseBodySecrityPolicyRelationsRelatedListeners] = None,
        security_policy_id: str = None,
    ):
        # The listeners that are associated with the security policy.
        self.related_listeners = related_listeners
        # The security policy ID.
        self.security_policy_id = security_policy_id

    def validate(self):
        if self.related_listeners:
            for v1 in self.related_listeners:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RelatedListeners'] = []
        if self.related_listeners is not None:
            for k1 in self.related_listeners:
                result['RelatedListeners'].append(k1.to_map() if k1 else None)

        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.related_listeners = []
        if m.get('RelatedListeners') is not None:
            for k1 in m.get('RelatedListeners'):
                temp_model = main_models.ListSecurityPolicyRelationsResponseBodySecrityPolicyRelationsRelatedListeners()
                self.related_listeners.append(temp_model.from_map(k1))

        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')

        return self

class ListSecurityPolicyRelationsResponseBodySecrityPolicyRelationsRelatedListeners(DaraModel):
    def __init__(
        self,
        listener_id: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        load_balancer_id: str = None,
    ):
        # The listener ID.
        self.listener_id = listener_id
        # The listener port.
        self.listener_port = listener_port
        # The listener protocol.
        self.listener_protocol = listener_protocol
        # The Server Load Balancer (SLB) instance ID.
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        return self

