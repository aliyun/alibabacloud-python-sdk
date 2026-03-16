# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fnf20190315 import models as main_models
from darabonba.model import DaraModel

class StartSyncExecutionResponseBody(DaraModel):
    def __init__(
        self,
        environment: main_models.StartSyncExecutionResponseBodyEnvironment = None,
        error_code: str = None,
        error_message: str = None,
        flow_name: str = None,
        name: str = None,
        output: str = None,
        request_id: str = None,
        started_time: str = None,
        status: str = None,
        stopped_time: str = None,
    ):
        self.environment = environment
        # The error code that is returned if the execution failed.
        self.error_code = error_code
        # The error message that indicates the execution timed out.
        self.error_message = error_message
        # The name of the flow.
        self.flow_name = flow_name
        # The name of the execution.
        self.name = name
        # The output of the execution, which is in the JSON format.
        self.output = output
        # The request ID.
        self.request_id = request_id
        # The time when the execution started.
        self.started_time = started_time
        # The status of the execution. Valid values:
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
        if self.environment:
            self.environment.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment is not None:
            result['Environment'] = self.environment.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

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
        if m.get('Environment') is not None:
            temp_model = main_models.StartSyncExecutionResponseBodyEnvironment()
            self.environment = temp_model.from_map(m.get('Environment'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

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

class StartSyncExecutionResponseBodyEnvironment(DaraModel):
    def __init__(
        self,
        variables: List[main_models.StartSyncExecutionResponseBodyEnvironmentVariables] = None,
    ):
        self.variables = variables

    def validate(self):
        if self.variables:
            for v1 in self.variables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Variables'] = []
        if self.variables is not None:
            for k1 in self.variables:
                result['Variables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.variables = []
        if m.get('Variables') is not None:
            for k1 in m.get('Variables'):
                temp_model = main_models.StartSyncExecutionResponseBodyEnvironmentVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class StartSyncExecutionResponseBodyEnvironmentVariables(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

