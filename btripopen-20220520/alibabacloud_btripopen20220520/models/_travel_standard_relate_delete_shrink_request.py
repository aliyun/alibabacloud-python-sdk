# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TravelStandardRelateDeleteShrinkRequest(DaraModel):
    def __init__(
        self,
        from_group: bool = None,
        remove_list_shrink: str = None,
        rule_id: int = None,
    ):
        self.from_group = from_group
        self.remove_list_shrink = remove_list_shrink
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_group is not None:
            result['from_group'] = self.from_group

        if self.remove_list_shrink is not None:
            result['remove_list'] = self.remove_list_shrink

        if self.rule_id is not None:
            result['rule_id'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from_group') is not None:
            self.from_group = m.get('from_group')

        if m.get('remove_list') is not None:
            self.remove_list_shrink = m.get('remove_list')

        if m.get('rule_id') is not None:
            self.rule_id = m.get('rule_id')

        return self

