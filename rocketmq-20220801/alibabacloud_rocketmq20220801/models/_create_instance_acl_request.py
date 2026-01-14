# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateInstanceAclRequest(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        decision: str = None,
        ip_whitelists: List[str] = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The type of operations that can be performed on the resource.
        # 
        # The following types of operations are supported based on the resource type:
        # 
        # *   Topic: Pub, Sub, and Pub|Sub
        # *   Group: Sub
        # 
        # Valid values:
        # 
        # *   Sub: subscribe
        # *   Pub|Sub: publish and subscribe
        # *   Pub: publish
        # 
        # This parameter is required.
        self.actions = actions
        # The decision result of the authorization.
        # 
        # Valid values:
        # 
        # *   Deny
        # *   Allow
        # 
        # This parameter is required.
        self.decision = decision
        # The IP addresses in the whitelist.
        self.ip_whitelists = ip_whitelists
        # The name of the resource on which you want to grant permissions.
        # 
        # This parameter is required.
        self.resource_name = resource_name
        # The type of the resource on which you want to grant permissions.
        # 
        # Valid values:
        # 
        # *   Group
        # *   Topic
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['actions'] = self.actions

        if self.decision is not None:
            result['decision'] = self.decision

        if self.ip_whitelists is not None:
            result['ipWhitelists'] = self.ip_whitelists

        if self.resource_name is not None:
            result['resourceName'] = self.resource_name

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')

        if m.get('decision') is not None:
            self.decision = m.get('decision')

        if m.get('ipWhitelists') is not None:
            self.ip_whitelists = m.get('ipWhitelists')

        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

