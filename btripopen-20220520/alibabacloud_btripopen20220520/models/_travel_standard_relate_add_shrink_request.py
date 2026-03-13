# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TravelStandardRelateAddShrinkRequest(DaraModel):
    def __init__(
        self,
        add_list_shrink: str = None,
        from_group: bool = None,
        rule_id: int = None,
    ):
        self.add_list_shrink = add_list_shrink
        self.from_group = from_group
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_list_shrink is not None:
            result['add_list'] = self.add_list_shrink

        if self.from_group is not None:
            result['from_group'] = self.from_group

        if self.rule_id is not None:
            result['rule_id'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('add_list') is not None:
            self.add_list_shrink = m.get('add_list')

        if m.get('from_group') is not None:
            self.from_group = m.get('from_group')

        if m.get('rule_id') is not None:
            self.rule_id = m.get('rule_id')

        return self

