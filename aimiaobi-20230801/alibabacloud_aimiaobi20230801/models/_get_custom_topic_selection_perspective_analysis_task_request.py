# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCustomTopicSelectionPerspectiveAnalysisTaskRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        task_id: str = None,
    ):
        # Unique identifier of the workspace: [AgentKey](https://help.aliyun.com/document_detail/2587494.html)
        # 
        # This parameter is required.
        self.agent_key = agent_key
        # Unique ID of the task.
        # 
        # > The system generates a TaskId by default. If you specify the same TaskId for multiple tasks, those tasks belong to the same conversation group.
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
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

