# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TravelStandardScopeSaveRequest(DaraModel):
    def __init__(
        self,
        from_group: bool = None,
        rule_id: int = None,
        scope: int = None,
    ):
        self.from_group = from_group
        # This parameter is required.
        self.rule_id = rule_id
        # This parameter is required.
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_group is not None:
            result['from_group'] = self.from_group

        if self.rule_id is not None:
            result['rule_id'] = self.rule_id

        if self.scope is not None:
            result['scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from_group') is not None:
            self.from_group = m.get('from_group')

        if m.get('rule_id') is not None:
            self.rule_id = m.get('rule_id')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        return self

