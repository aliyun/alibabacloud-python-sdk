# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopExecutionRequest(DaraModel):
    def __init__(
        self,
        cause: str = None,
        error: str = None,
        execution_name: str = None,
        flow_name: str = None,
    ):
        # The reason for stopping the execution. The value must be 1 to 4,096 characters in length.
        self.cause = cause
        # The error code for stopping the execution. The error code must be 1 to 128 characters in length.
        self.error = error
        # The name of the execution to be stopped. You can call the **ListExecutions** operation to obtain the value of this parameter.
        # 
        # This parameter is required.
        self.execution_name = execution_name
        # The name of the workflow to be stopped. You can call the **ListFlows** operation to obtain the value of this parameter.
        # 
        # This parameter is required.
        self.flow_name = flow_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cause is not None:
            result['Cause'] = self.cause

        if self.error is not None:
            result['Error'] = self.error

        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cause') is not None:
            self.cause = m.get('Cause')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('ExecutionName') is not None:
            self.execution_name = m.get('ExecutionName')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        return self

