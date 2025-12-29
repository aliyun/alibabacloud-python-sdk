# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ListExecutionLogsResponseBody(DaraModel):
    def __init__(
        self,
        execution_logs: List[main_models.ListExecutionLogsResponseBodyExecutionLogs] = None,
        is_truncated: bool = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The logs of the execution.
        self.execution_logs = execution_logs
        # Indicates whether the log is truncated.
        self.is_truncated = is_truncated
        # The number of entries per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.execution_logs:
            for v1 in self.execution_logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ExecutionLogs'] = []
        if self.execution_logs is not None:
            for k1 in self.execution_logs:
                result['ExecutionLogs'].append(k1.to_map() if k1 else None)

        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.execution_logs = []
        if m.get('ExecutionLogs') is not None:
            for k1 in m.get('ExecutionLogs'):
                temp_model = main_models.ListExecutionLogsResponseBodyExecutionLogs()
                self.execution_logs.append(temp_model.from_map(k1))

        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListExecutionLogsResponseBodyExecutionLogs(DaraModel):
    def __init__(
        self,
        log_type: str = None,
        message: str = None,
        task_execution_id: str = None,
        timestamp: str = None,
    ):
        # The log type.
        self.log_type = log_type
        # The details of the task execution.
        self.message = message
        # The task execution ID.
        self.task_execution_id = task_execution_id
        # The timestamp when the task was run.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_type is not None:
            result['LogType'] = self.log_type

        if self.message is not None:
            result['Message'] = self.message

        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

