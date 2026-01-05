# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class ListAclRelationsResponseBody(DaraModel):
    def __init__(
        self,
        acl_relations: List[main_models.ListAclRelationsResponseBodyAclRelations] = None,
        request_id: str = None,
    ):
        # The relations between the specified ACL and the listeners.
        self.acl_relations = acl_relations
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.acl_relations:
            for v1 in self.acl_relations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AclRelations'] = []
        if self.acl_relations is not None:
            for k1 in self.acl_relations:
                result['AclRelations'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_relations = []
        if m.get('AclRelations') is not None:
            for k1 in m.get('AclRelations'):
                temp_model = main_models.ListAclRelationsResponseBodyAclRelations()
                self.acl_relations.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAclRelationsResponseBodyAclRelations(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        related_listeners: List[main_models.ListAclRelationsResponseBodyAclRelationsRelatedListeners] = None,
    ):
        # ACL ID
        self.acl_id = acl_id
        # The listeners that are associated with the ACL.
        self.related_listeners = related_listeners

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
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        result['RelatedListeners'] = []
        if self.related_listeners is not None:
            for k1 in self.related_listeners:
                result['RelatedListeners'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        self.related_listeners = []
        if m.get('RelatedListeners') is not None:
            for k1 in m.get('RelatedListeners'):
                temp_model = main_models.ListAclRelationsResponseBodyAclRelationsRelatedListeners()
                self.related_listeners.append(temp_model.from_map(k1))

        return self

class ListAclRelationsResponseBodyAclRelationsRelatedListeners(DaraModel):
    def __init__(
        self,
        listener_id: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        load_balancer_id: str = None,
        status: str = None,
    ):
        # The listener ID.
        self.listener_id = listener_id
        # The listener port.
        self.listener_port = listener_port
        # The listener protocol.
        self.listener_protocol = listener_protocol
        # The ID of the SLB instance.
        self.load_balancer_id = load_balancer_id
        # The association status between the ACL and the listener.
        # 
        # *   **Associating**
        # *   **Associated**
        # *   **Dissociating**
        self.status = status

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

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

