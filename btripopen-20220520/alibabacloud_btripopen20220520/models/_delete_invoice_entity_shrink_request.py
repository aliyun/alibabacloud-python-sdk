# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteInvoiceEntityShrinkRequest(DaraModel):
    def __init__(
        self,
        del_all: bool = None,
        entities_shrink: str = None,
        third_part_id: str = None,
    ):
        # Specifies whether to delete all applicable personnel. If del_all is set to true, all entities under the invoice header are deleted, and the entity list parameter is not validated.
        self.del_all = del_all
        # The entity list. This parameter is required when del_all is set to false or null.
        self.entities_shrink = entities_shrink
        # The third-party invoice ID.
        # 
        # This parameter is required.
        self.third_part_id = third_part_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.del_all is not None:
            result['del_all'] = self.del_all

        if self.entities_shrink is not None:
            result['entities'] = self.entities_shrink

        if self.third_part_id is not None:
            result['third_part_id'] = self.third_part_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('del_all') is not None:
            self.del_all = m.get('del_all')

        if m.get('entities') is not None:
            self.entities_shrink = m.get('entities')

        if m.get('third_part_id') is not None:
            self.third_part_id = m.get('third_part_id')

        return self

