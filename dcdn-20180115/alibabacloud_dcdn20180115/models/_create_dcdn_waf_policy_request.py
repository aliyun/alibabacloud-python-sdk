# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDcdnWafPolicyRequest(DaraModel):
    def __init__(
        self,
        defense_scene: str = None,
        policy_name: str = None,
        policy_status: str = None,
        policy_type: str = None,
    ):
        # The type of the WAF protection policy. Valid values:
        # 
        # *   waf_group: basic web protection
        # *   custom_acl: custom protection
        # *   whitelist: IP address whitelist
        # *   ip_blacklist: IP address blacklist
        # *   region_block: region blacklist
        # *   bot: bot management
        # 
        # This parameter is required.
        self.defense_scene = defense_scene
        # The name of the protection policy. The name can be up to 64 characters in length and can contain letters, digits, and underscores (_).
        # 
        # This parameter is required.
        self.policy_name = policy_name
        # The status of the protection policy. Valid values:
        # 
        # *   on: The policy is enabled.
        # *   off: The policy is disabled.
        # 
        # This parameter is required.
        self.policy_status = policy_status
        # Specifies whether to set the current policy as the default policy. Valid values:
        # 
        # *   default: sets the current policy as the default policy.
        # *   custom: does not set the current policy as the default policy.
        # 
        # This parameter is required.
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defense_scene is not None:
            result['DefenseScene'] = self.defense_scene

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_status is not None:
            result['PolicyStatus'] = self.policy_status

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseScene') is not None:
            self.defense_scene = m.get('DefenseScene')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyStatus') is not None:
            self.policy_status = m.get('PolicyStatus')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

