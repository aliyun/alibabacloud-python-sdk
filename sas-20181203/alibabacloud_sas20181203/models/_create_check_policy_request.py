# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCheckPolicyRequest(DaraModel):
    def __init__(
        self,
        dependent_policy_id: int = None,
        policy_show_name: str = None,
        policy_type: str = None,
        type: str = None,
    ):
        # The ID of the parent policy.
        #       
        # (The specific dependency order from low to high is Section -> Requirement -> Standard)
        self.dependent_policy_id = dependent_policy_id
        # The name of the custom policy.
        # 
        # This parameter is required.
        self.policy_show_name = policy_show_name
        # The policy category type for custom check rules:
        # - **STANDARD**: Add to a standard.
        # - **REQUIREMENT**: Add to a requirement.
        # - **SECTION**: Add to a section.
        # 
        # This parameter is required.
        self.policy_type = policy_type
        # The name of the major policy category (required when PolicyType is STANDARD):
        # - **AISPM**: AI Configuration Management (AISPM).
        # - **IDENTITY_PERMISSION**: Identity and Permission Management (CIEM).
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

        if m.get('PolicyShowName') is not None:
            self.policy_show_name = m.get('PolicyShowName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

