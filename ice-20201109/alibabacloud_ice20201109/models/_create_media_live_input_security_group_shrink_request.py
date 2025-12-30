# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMediaLiveInputSecurityGroupShrinkRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        whitelist_rules_shrink: str = None,
    ):
        # The name of the security group. Letters, digits, hyphens (-), and underscores (_) are supported. The maximum length is 64 characters.
        # 
        # This parameter is required.
        self.name = name
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

        if self.whitelist_rules_shrink is not None:
            result['WhitelistRules'] = self.whitelist_rules_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('WhitelistRules') is not None:
            self.whitelist_rules_shrink = m.get('WhitelistRules')

        return self

