# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchGetVideoClipTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        task_id_list_shrink: str = None,
    ):
        self.task_id_list_shrink = task_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id_list_shrink is not None:
            result['taskIdList'] = self.task_id_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskIdList') is not None:
            self.task_id_list_shrink = m.get('taskIdList')

        return self

