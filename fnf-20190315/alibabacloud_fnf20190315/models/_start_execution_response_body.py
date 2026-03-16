# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartExecutionResponseBody(DaraModel):
    def __init__(
        self,
        flow_definition: str = None,
        flow_name: str = None,
        input: str = None,
        name: str = None,
        output: str = None,
        request_id: str = None,
        started_time: str = None,
        status: str = None,
        stopped_time: str = None,
    ):
        # The definition of the flow.
        self.flow_definition = flow_definition
        # The name of the workflow.
        self.flow_name = flow_name
        # The input of the execution, which is in the JSON format.
        self.input = input
        # The name of the execution.
        self.name = name
        # The execution result, which is in the JSON format.
        self.output = output
        # The request ID.
        self.request_id = request_id
        # The time when the execution started.
        self.started_time = started_time
        # The execution status. Valid values:
        # 
        # *   **Starting**
        # *   **Running**
        # *   **Stopped**
        # *   **Succeeded**
        # *   **Failed**
        # *   **TimedOut**
        self.status = status
        # The time when the execution stopped.
        self.stopped_time = stopped_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_definition is not None:
            result['FlowDefinition'] = self.flow_definition

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.input is not None:
            result['Input'] = self.input

        if self.name is not None:
            result['Name'] = self.name

        if self.output is not None:
            result['Output'] = self.output

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.started_time is not None:
            result['StartedTime'] = self.started_time

        if self.status is not None:
            result['Status'] = self.status

        if self.stopped_time is not None:
            result['StoppedTime'] = self.stopped_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowDefinition') is not None:
            self.flow_definition = m.get('FlowDefinition')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StoppedTime') is not None:
            self.stopped_time = m.get('StoppedTime')

        return self

