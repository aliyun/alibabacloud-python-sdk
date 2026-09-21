# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUniBackupPolicyDetailRequest(DaraModel):
    def __init__(
        self,
        policy_id: str = None,
    ):
        # The ID of the anti-ransomware backup policy for databases.
        # >Call the [DescribeUniBackupPolicies](~~DescribeUniBackupPolicies~~) operation to obtain this parameter.
        # 
        # If DescribeUniBackupPolicies returns an empty list, activate the anti-ransomware feature of Security Center first, make sure that the Security Center agent is installed on the ECS instance and the database has been discovered, and then call CreateUniBackupPolicy to create a backup policy.
        # 
        # This parameter is required.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        return self

