# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachPolicyToRoleRequest(DaraModel):
    def __init__(
        self,
        policy_name: str = None,
        policy_type: str = None,
        resource_group_id: str = None,
        role_name: str = None,
    ):
        # The name of the policy.
        self.policy_name = policy_name
        # The type of the policy. Valid values: `System` and `Custom`.
        self.policy_type = policy_type
        self.resource_group_id = resource_group_id
        # The name of the RAM role.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

