# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTopicSelectionPerspectiveAnalysisTaskRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        task_id: str = None,
    ):
        # The unique identifier of the workspace. For more information, see [AgentKey](https://help.aliyun.com/document_detail/2587494.html).
        # 
        # This parameter is required.
        self.agent_key = agent_key
        # The unique ID of the task.
        # 
        # > This parameter is optional. The system automatically generates a task ID. If subsequent tasks have the same TaskId, they are considered part of the same conversation.
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

