# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegisterLineageRelationShrinkRequest(DaraModel):
    def __init__(
        self,
        lineage_relation_register_voshrink: str = None,
    ):
        # The structure whose lineage you want to register to DataWorks.
        # 
        # This parameter is required.
        self.lineage_relation_register_voshrink = lineage_relation_register_voshrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lineage_relation_register_voshrink is not None:
            result['LineageRelationRegisterVO'] = self.lineage_relation_register_voshrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineageRelationRegisterVO') is not None:
            self.lineage_relation_register_voshrink = m.get('LineageRelationRegisterVO')

        return self

