# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOssCheckTaskInfoRequest(DaraModel):
    def __init__(
        self,
        parent_task_id: str = None,
    ):
        self.parent_task_id = parent_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parent_task_id is not None:
            result['ParentTaskId'] = self.parent_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParentTaskId') is not None:
            self.parent_task_id = m.get('ParentTaskId')

        return self

