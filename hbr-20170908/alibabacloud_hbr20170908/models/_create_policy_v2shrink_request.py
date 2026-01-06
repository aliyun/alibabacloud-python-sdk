# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePolicyV2ShrinkRequest(DaraModel):
    def __init__(
        self,
        policy_description: str = None,
        policy_name: str = None,
        policy_type: str = None,
        rules_shrink: str = None,
    ):
        # The description of the backup policy.
        self.policy_description = policy_description
        # The name of the backup policy.
        self.policy_name = policy_name
        # The policy type. Valid values:
        # 
        # *   **STANDARD**: the general backup policy. This type of policy applies to backups other than Elastic Compute Service (ECS) instance backup.
        # *   **UDM_ECS_ONLY**: This type of policy applies only to ECS instance backup.
        # 
        # If the policy type is not specified, Cloud Backup automatically sets the policy type based on whether the backup vault is specified in the rules of the policy:
        # 
        # *   If the backup vault is specified, Cloud Backup sets the policy type to **STANDARD**.
        # *   If the backup vault is not specified, Cloud Backup sets the policy type to **UDM_ECS_ONLY**.
        self.policy_type = policy_type
        # The rules in the backup policy.
        self.rules_shrink = rules_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.rules_shrink is not None:
            result['Rules'] = self.rules_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('Rules') is not None:
            self.rules_shrink = m.get('Rules')

        return self

