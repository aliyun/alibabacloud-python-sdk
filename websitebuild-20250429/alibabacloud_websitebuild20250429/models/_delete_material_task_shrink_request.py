# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMaterialTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        task_ids_shrink: str = None,
    ):
        # This parameter is required.
        self.task_ids_shrink = task_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_ids_shrink is not None:
            result['TaskIds'] = self.task_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskIds') is not None:
            self.task_ids_shrink = m.get('TaskIds')

        return self

