# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDcdnWafPolicyRequest(DaraModel):
    def __init__(
        self,
        policy_id: int = None,
        policy_name: str = None,
        policy_status: str = None,
    ):
        # The ID of the protection policy that you want to modify. You can specify only one ID in each request.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The new name of the protection policy.
        # 
        # > You must specify PolicyName or PolicyStatus.
        self.policy_name = policy_name
        # The new status of the protection policy. Valid values:
        # 
        # *   **on**
        # *   **off**
        # 
        # > You must specify PolicyName or PolicyStatus.
        self.policy_status = policy_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_status is not None:
            result['PolicyStatus'] = self.policy_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyStatus') is not None:
            self.policy_status = m.get('PolicyStatus')

        return self

