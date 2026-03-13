# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TriggerProcessTaskRequest(DaraModel):
    def __init__(
        self,
        action_type: str = None,
        task_id: str = None,
    ):
        # The type of the action. Valid values:
        # 
        # *   **remove**: cancels blocking or isolation.
        # *   **retry**: submits the task again.
        # 
        # This parameter is required.
        self.action_type = action_type
        # The ID of the handling task.
        # 
        # >  You can call the [DescribeProcessTasks](~~DescribeProcessTasks~~) operation to query the IDs of handling tasks.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

