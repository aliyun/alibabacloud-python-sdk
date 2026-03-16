# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartExecutionRequest(DaraModel):
    def __init__(
        self,
        callback_fn_ftask_token: str = None,
        execution_name: str = None,
        flow_name: str = None,
        input: str = None,
        qualifier: str = None,
    ):
        # Specifies that the **TaskToken**-related tasks are called back after the execution in the flow ends.
        self.callback_fn_ftask_token = callback_fn_ftask_token
        # The name of the execution. The execution name is unique within a workflow. Configure this parameter based on the following rules:
        # 
        # *   The name must start with a letter or an underscore (_).
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
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
        if self.callback_fn_ftask_token is not None:
            result['CallbackFnFTaskToken'] = self.callback_fn_ftask_token

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
        if m.get('CallbackFnFTaskToken') is not None:
            self.callback_fn_ftask_token = m.get('CallbackFnFTaskToken')

        if m.get('ExecutionName') is not None:
            self.execution_name = m.get('ExecutionName')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('Qualifier') is not None:
            self.qualifier = m.get('Qualifier')

        return self

