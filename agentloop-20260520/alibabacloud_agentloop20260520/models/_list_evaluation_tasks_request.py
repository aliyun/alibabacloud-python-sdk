# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEvaluationTasksRequest(DaraModel):
    def __init__(
        self,
        agent_space: str = None,
        channel: str = None,
        data_type: str = None,
        max_results: int = None,
        next_token: str = None,
        status: str = None,
        task_mode: str = None,
        task_name: str = None,
    ):
        # The AgentSpace name.
        self.agent_space = agent_space
        # The filter condition for the task source. If this parameter is not specified, tasks from the default source are queried.
        self.channel = channel
        # The data source type of the evaluation object. Set this parameter to `trace` for trace-based evaluation.
        self.data_type = data_type
        # The number of entries per page. Default value: 20. Maximum value: 100.
        self.max_results = max_results
        # The pagination token for the next page, obtained from the previous response.
        self.next_token = next_token
        # The filter condition for the evaluation task status.
        self.status = status
        # The evaluation task mode. If this parameter is not specified, the default value is `batch`.
        self.task_mode = task_mode
        # The fuzzy match condition for the task name.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space is not None:
            result['agentSpace'] = self.agent_space

        if self.channel is not None:
            result['channel'] = self.channel

        if self.data_type is not None:
            result['dataType'] = self.data_type

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.status is not None:
            result['status'] = self.status

        if self.task_mode is not None:
            result['taskMode'] = self.task_mode

        if self.task_name is not None:
            result['taskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpace') is not None:
            self.agent_space = m.get('agentSpace')

        if m.get('channel') is not None:
            self.channel = m.get('channel')

        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskMode') is not None:
            self.task_mode = m.get('taskMode')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        return self

