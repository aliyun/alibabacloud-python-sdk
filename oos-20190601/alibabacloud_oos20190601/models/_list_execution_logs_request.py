# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListExecutionLogsRequest(DaraModel):
    def __init__(
        self,
        execution_id: str = None,
        log_type: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        task_execution_id: str = None,
    ):
        # The ID of the execution.
        # 
        # This parameter is required.
        self.execution_id = execution_id
        # The type of the log.
        self.log_type = log_type
        # The number of entries to return on each page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the region in which you want to query the logs of the execution.
        self.region_id = region_id
        # The execution ID of the task.
        self.task_execution_id = task_execution_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id

        if self.log_type is not None:
            result['LogType'] = self.log_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')

        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')

        return self

