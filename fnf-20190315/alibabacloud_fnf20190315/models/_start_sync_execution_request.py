# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartSyncExecutionRequest(DaraModel):
    def __init__(
        self,
        execution_name: str = None,
        flow_name: str = None,
        input: str = None,
        qualifier: str = None,
    ):
        # The name of the execution that you want to start. The name must meet the following conventions:
        # 
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must start with a letter or an underscore (_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        # 
        # Different from the StartExecution operation, in the synchronous execution mode, the execution name is no longer required to be unique within a flow. You can choose to provide an execution name to identify the current execution. In this case, the system adds a UUID to the current execution name. The used format is {ExecutionName}:{UUID}. If you do not specify the execution name, the system automatically generates an execution name.
        self.execution_name = execution_name
        # The name of the workflow to be executed.
        # 
        # This parameter is required.
        self.flow_name = flow_name
        # The input of the execution, which is in the JSON format.
        self.input = input
        self.qualifier = qualifier

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

        if self.input is not None:
            result['Input'] = self.input

        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionName') is not None:
            self.execution_name = m.get('ExecutionName')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('Qualifier') is not None:
            self.qualifier = m.get('Qualifier')

        return self

