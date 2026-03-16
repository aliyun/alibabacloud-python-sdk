# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fnf20190315 import models as main_models
from darabonba.model import DaraModel

class ListExecutionsResponseBody(DaraModel):
    def __init__(
        self,
        executions: List[main_models.ListExecutionsResponseBodyExecutions] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The information about executions.
        self.executions = executions
        # The start key for the next query. This parameter is not returned if this is the last query.
        # 
        # >  This parameter may not be displayed in the response because no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.executions:
            for v1 in self.executions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Executions'] = []
        if self.executions is not None:
            for k1 in self.executions:
                result['Executions'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.executions = []
        if m.get('Executions') is not None:
            for k1 in m.get('Executions'):
                temp_model = main_models.ListExecutionsResponseBodyExecutions()
                self.executions.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListExecutionsResponseBodyExecutions(DaraModel):
    def __init__(
        self,
        environment: main_models.ListExecutionsResponseBodyExecutionsEnvironment = None,
        flow_definition: str = None,
        flow_name: str = None,
        input: str = None,
        name: str = None,
        output: str = None,
        started_time: str = None,
        status: str = None,
        stopped_time: str = None,
    ):
        self.environment = environment
        # The definition of the flow.
        self.flow_definition = flow_definition
        # The name of the flow.
        self.flow_name = flow_name
        # The input of the execution, which is in the JSON format.
        self.input = input
        # The name of the execution.
        self.name = name
        # The output of the execution, which is in the JSON format
        self.output = output
        # The time when the execution started.
        self.started_time = started_time
        # The status of the execution.
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
            temp_model = main_models.ListExecutionsResponseBodyExecutionsEnvironment()
            self.environment = temp_model.from_map(m.get('Environment'))

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

        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StoppedTime') is not None:
            self.stopped_time = m.get('StoppedTime')

        return self

class ListExecutionsResponseBodyExecutionsEnvironment(DaraModel):
    def __init__(
        self,
        variables: List[main_models.ListExecutionsResponseBodyExecutionsEnvironmentVariables] = None,
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
                temp_model = main_models.ListExecutionsResponseBodyExecutionsEnvironmentVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class ListExecutionsResponseBodyExecutionsEnvironmentVariables(DaraModel):
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

