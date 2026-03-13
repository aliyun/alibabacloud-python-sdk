# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InvoiceRuleSaveShrinkRequest(DaraModel):
    def __init__(
        self,
        all_employe: bool = None,
        entities_shrink: str = None,
        scope: int = None,
        third_part_id: str = None,
    ):
        self.all_employe = all_employe
        self.entities_shrink = entities_shrink
        self.scope = scope
        # This parameter is required.
        self.third_part_id = third_part_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_employe is not None:
            result['all_employe'] = self.all_employe

        if self.entities_shrink is not None:
            result['entities'] = self.entities_shrink

        if self.scope is not None:
            result['scope'] = self.scope

        if self.third_part_id is not None:
            result['third_part_id'] = self.third_part_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all_employe') is not None:
            self.all_employe = m.get('all_employe')

        if m.get('entities') is not None:
            self.entities_shrink = m.get('entities')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('third_part_id') is not None:
            self.third_part_id = m.get('third_part_id')

        return self

