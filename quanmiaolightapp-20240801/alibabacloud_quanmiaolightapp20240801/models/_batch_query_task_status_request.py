# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchQueryTaskStatusRequest(DaraModel):
    def __init__(
        self,
        task_code: str = None,
        task_ids: List[str] = None,
    ):
        # This parameter is required.
        self.task_code = task_code
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_code is not None:
            result['taskCode'] = self.task_code

        if self.task_ids is not None:
            result['taskIds'] = self.task_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskCode') is not None:
            self.task_code = m.get('taskCode')

        if m.get('taskIds') is not None:
            self.task_ids = m.get('taskIds')

        return self

