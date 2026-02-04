# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDcdnWafGroupRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        rules: str = None,
    ):
        # The ID of the custom WAF rule group.
        # 
        # This parameter is required.
        self.id = id
        # The name of the custom WAF rule group.
        self.name = name
        # The incremental modifications of the rules in the custom WAF rule group. The value is a JSON string.
        self.rules = rules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.rules is not None:
            result['Rules'] = self.rules

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Rules') is not None:
            self.rules = m.get('Rules')

        return self

