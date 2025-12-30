# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMediaLiveInputSecurityGroupShrinkRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        security_group_id: str = None,
        whitelist_rules_shrink: str = None,
    ):
        # The name of the security group. Letters, digits, hyphens (-), and underscores (_) are supported. It can be up to 64 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the security group.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id
        # The security group rules.
        # 
        # This parameter is required.
        self.whitelist_rules_shrink = whitelist_rules_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.whitelist_rules_shrink is not None:
            result['WhitelistRules'] = self.whitelist_rules_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('WhitelistRules') is not None:
            self.whitelist_rules_shrink = m.get('WhitelistRules')

        return self

