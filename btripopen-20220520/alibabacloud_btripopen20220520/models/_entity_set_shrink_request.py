# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EntitySetShrinkRequest(DaraModel):
    def __init__(
        self,
        entity_dolist_shrink: str = None,
        thirdpart_id: str = None,
    ):
        self.entity_dolist_shrink = entity_dolist_shrink
        # This parameter is required.
        self.thirdpart_id = thirdpart_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_dolist_shrink is not None:
            result['entity_d_o_list'] = self.entity_dolist_shrink

        if self.thirdpart_id is not None:
            result['thirdpart_id'] = self.thirdpart_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entity_d_o_list') is not None:
            self.entity_dolist_shrink = m.get('entity_d_o_list')

        if m.get('thirdpart_id') is not None:
            self.thirdpart_id = m.get('thirdpart_id')

        return self

