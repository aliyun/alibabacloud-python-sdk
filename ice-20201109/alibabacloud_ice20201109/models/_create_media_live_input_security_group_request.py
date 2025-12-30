# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateMediaLiveInputSecurityGroupRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        whitelist_rules: List[str] = None,
    ):
        # The name of the security group. Letters, digits, hyphens (-), and underscores (_) are supported. The maximum length is 64 characters.
        # 
        # This parameter is required.
        self.name = name
        # The security group rules.
        # 
        # This parameter is required.
        self.whitelist_rules = whitelist_rules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.whitelist_rules is not None:
            result['WhitelistRules'] = self.whitelist_rules

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('WhitelistRules') is not None:
            self.whitelist_rules = m.get('WhitelistRules')

        return self

