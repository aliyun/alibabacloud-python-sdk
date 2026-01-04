# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteConditionalAccessPolicyRequest(DaraModel):
    def __init__(
        self,
        conditional_access_policy_id: str = None,
        instance_id: str = None,
    ):
        # Conditional Access Policy ID
        # 
        # This parameter is required.
        self.conditional_access_policy_id = conditional_access_policy_id
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conditional_access_policy_id is not None:
            result['ConditionalAccessPolicyId'] = self.conditional_access_policy_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionalAccessPolicyId') is not None:
            self.conditional_access_policy_id = m.get('ConditionalAccessPolicyId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

