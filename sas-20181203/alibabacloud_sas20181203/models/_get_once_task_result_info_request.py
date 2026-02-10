# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOnceTaskResultInfoRequest(DaraModel):
    def __init__(
        self,
        task_id: str = None,
        task_name: str = None,
        task_type: str = None,
    ):
        # The ID of the scan task.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The name of the task. Valid values:
        # 
        # *   **CLIENT_PROBLEM_CHECK**: a task of the Security Center agent
        # *   **CLIENT_DEV_OPS**: an O\\&M task of Cloud Assistant
        # *   **ASSET_SECURITY_CHECK**: a task of asset information collection
        # 
        # This parameter is required.
        self.task_name = task_name
        # The type of the task. Valid values:
        # 
        # *   **CLIENT_PROBLEM_CHECK**: a task of the Security Center agent
        # *   **CLIENT_DEV_OPS**: an O\\&M task of Cloud Assistant
        # *   **ASSET_SECURITY_CHECK**: a task of asset information collection
        # 
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

