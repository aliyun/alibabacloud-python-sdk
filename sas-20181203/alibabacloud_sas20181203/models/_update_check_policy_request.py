# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCheckPolicyRequest(DaraModel):
    def __init__(
        self,
        dependent_policy_id: int = None,
        policy_id: int = None,
        policy_show_name: str = None,
        policy_type: str = None,
        type: str = None,
    ):
        # ID of the associated parent policy.
        # 
        # (The specific dependency hierarchy, from low to high, is Section -> Requirement -> Standard).
        self.dependent_policy_id = dependent_policy_id
        # ID of the custom policy.
        # > You can obtain this parameter by calling the [ListCheckPolicies](~~ListCheckPolicies~~) API.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # Name of the custom classification.
        self.policy_show_name = policy_show_name
        # Classification type of the custom check item rule:
        # - **STANDARD**: Add to standard.
        # - **REQUIREMENT**: Add to requirement.
        # - **SECTION**: Add to section.
        # 
        # This parameter is required.
        self.policy_type = policy_type
        # Name of the associated major policy category (required when PolicyType is STANDARD):
        # - **AISPM**: AI Configuration Management (AISPM).
        # - **RISK**: Security Risk.
        # - **COMPLIANCE**: Compliance Risk.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dependent_policy_id is not None:
            result['DependentPolicyId'] = self.dependent_policy_id

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_show_name is not None:
            result['PolicyShowName'] = self.policy_show_name

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DependentPolicyId') is not None:
            self.dependent_policy_id = m.get('DependentPolicyId')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyShowName') is not None:
            self.policy_show_name = m.get('PolicyShowName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

