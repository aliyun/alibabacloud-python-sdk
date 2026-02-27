# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeletePolicyRequest(DaraModel):
    def __init__(
        self,
        policy_name: str = None,
    ):
        # The name of the permission policy.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, and hyphen (-).
        # 
        # This parameter is required.
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        return self

