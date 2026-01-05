# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLineageRelationshipShrinkRequest(DaraModel):
    def __init__(
        self,
        dst_entity_shrink: str = None,
        src_entity_shrink: str = None,
        task_shrink: str = None,
    ):
        # The destination entity.
        self.dst_entity_shrink = dst_entity_shrink
        # The source entity.
        self.src_entity_shrink = src_entity_shrink
        # The task information.
        self.task_shrink = task_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dst_entity_shrink is not None:
            result['DstEntity'] = self.dst_entity_shrink

        if self.src_entity_shrink is not None:
            result['SrcEntity'] = self.src_entity_shrink

        if self.task_shrink is not None:
            result['Task'] = self.task_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstEntity') is not None:
            self.dst_entity_shrink = m.get('DstEntity')

        if m.get('SrcEntity') is not None:
            self.src_entity_shrink = m.get('SrcEntity')

        if m.get('Task') is not None:
            self.task_shrink = m.get('Task')

        return self

