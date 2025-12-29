# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeActiveOperationTaskCountResponseBody(DaraModel):
    def __init__(
        self,
        need_pop: int = None,
        request_id: str = None,
        task_count: int = None,
    ):
        # Indicates whether any O\\&M tasks need pop-up windows to notify users actions. Valid values:
        # 
        # *   **0**: No O\\&M tasks need pop-up windows to notify users actions.
        # *   **1**: Some O\\&M tasks need pop-up windows to notify users actions.
        self.need_pop = need_pop
        # The request ID.
        self.request_id = request_id
        # The number of pending O\\&M tasks.
        self.task_count = task_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.need_pop is not None:
            result['NeedPop'] = self.need_pop

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_count is not None:
            result['TaskCount'] = self.task_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NeedPop') is not None:
            self.need_pop = m.get('NeedPop')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskCount') is not None:
            self.task_count = m.get('TaskCount')

        return self

