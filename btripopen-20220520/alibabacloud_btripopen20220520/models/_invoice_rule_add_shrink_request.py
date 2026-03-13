# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InvoiceRuleAddShrinkRequest(DaraModel):
    def __init__(
        self,
        entities_shrink: str = None,
        third_part_id: str = None,
    ):
        # This parameter is required.
        self.entities_shrink = entities_shrink
        # This parameter is required.
        self.third_part_id = third_part_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entities_shrink is not None:
            result['entities'] = self.entities_shrink

        if self.third_part_id is not None:
            result['third_part_id'] = self.third_part_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entities') is not None:
            self.entities_shrink = m.get('entities')

        if m.get('third_part_id') is not None:
            self.third_part_id = m.get('third_part_id')

        return self

