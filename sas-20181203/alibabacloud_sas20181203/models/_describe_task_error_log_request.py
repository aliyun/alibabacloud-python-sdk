# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTaskErrorLogRequest(DaraModel):
    def __init__(
        self,
        build_task_id: str = None,
    ):
        # The ID of the task.
        # 
        # >  You can call the DescribeImageFixTask operation to query the IDs of tasks.
        # 
        # This parameter is required.
        self.build_task_id = build_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_task_id is not None:
            result['BuildTaskId'] = self.build_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildTaskId') is not None:
            self.build_task_id = m.get('BuildTaskId')

        return self

