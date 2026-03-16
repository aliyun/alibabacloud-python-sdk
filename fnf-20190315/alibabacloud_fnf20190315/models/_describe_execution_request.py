# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeExecutionRequest(DaraModel):
    def __init__(
        self,
        execution_name: str = None,
        flow_name: str = None,
        wait_time_seconds: int = None,
    ):
        # The name of the execution.
        # 
        # This parameter is required.
        self.execution_name = execution_name
        # The name of the workflow.
        # 
        # This parameter is required.
        self.flow_name = flow_name
        # The maximum period of time for long polling waits. Valid values: 0 to 60. Unit: seconds. Configure this parameter based on the following rules:
        # 
        # *   If the value is 0, the system immediately returns the current execution status.
        # *   If the value is greater than 0, the long polling request waits until the execution ends or the specified period elapses.
        self.wait_time_seconds = wait_time_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.wait_time_seconds is not None:
            result['WaitTimeSeconds'] = self.wait_time_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionName') is not None:
            self.execution_name = m.get('ExecutionName')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('WaitTimeSeconds') is not None:
            self.wait_time_seconds = m.get('WaitTimeSeconds')

        return self

