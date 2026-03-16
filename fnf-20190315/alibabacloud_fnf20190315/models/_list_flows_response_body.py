# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fnf20190315 import models as main_models
from darabonba.model import DaraModel

class ListFlowsResponseBody(DaraModel):
    def __init__(
        self,
        flows: List[main_models.ListFlowsResponseBodyFlows] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The details of flows.
        self.flows = flows
        # The start key for the next query. This parameter is not returned if all results have been returned.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.flows:
            for v1 in self.flows:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Flows'] = []
        if self.flows is not None:
            for k1 in self.flows:
                result['Flows'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flows = []
        if m.get('Flows') is not None:
            for k1 in m.get('Flows'):
                temp_model = main_models.ListFlowsResponseBodyFlows()
                self.flows.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListFlowsResponseBodyFlows(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        definition: str = None,
        description: str = None,
        environment: main_models.ListFlowsResponseBodyFlowsEnvironment = None,
        execution_mode: str = None,
        id: str = None,
        last_modified_time: str = None,
        name: str = None,
        resource_group_id: str = None,
        role_arn: str = None,
        type: str = None,
    ):
        # The time when the flow was created.
        self.created_time = created_time
        # The definition of the flow. The definition must comply with the Flow Definition Language (FDL) syntax.
        self.definition = definition
        # The description of the flow.
        self.description = description
        self.environment = environment
        # The execution mode or the enumeration type. Valid values: Express and Standard. A value of Standard indicates an empty string.
        self.execution_mode = execution_mode
        # The unique ID of the flow.
        self.id = id
        # The time when the flow was last modified.
        self.last_modified_time = last_modified_time
        # The name of the flow.
        self.name = name
        self.resource_group_id = resource_group_id
        # The Alibaba Cloud resource name (ARN) of the specified Resource Access Management (RAM) role that Serverless Workflow assumes to invoke resources when the flow is executed.
        self.role_arn = role_arn
        # The type of the flow.
        self.type = type

    def validate(self):
        if self.environment:
            self.environment.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.definition is not None:
            result['Definition'] = self.definition

        if self.description is not None:
            result['Description'] = self.description

        if self.environment is not None:
            result['Environment'] = self.environment.to_map()

        if self.execution_mode is not None:
            result['ExecutionMode'] = self.execution_mode

        if self.id is not None:
            result['Id'] = self.id

        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Definition') is not None:
            self.definition = m.get('Definition')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Environment') is not None:
            temp_model = main_models.ListFlowsResponseBodyFlowsEnvironment()
            self.environment = temp_model.from_map(m.get('Environment'))

        if m.get('ExecutionMode') is not None:
            self.execution_mode = m.get('ExecutionMode')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListFlowsResponseBodyFlowsEnvironment(DaraModel):
    def __init__(
        self,
        variables: List[main_models.ListFlowsResponseBodyFlowsEnvironmentVariables] = None,
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
                temp_model = main_models.ListFlowsResponseBodyFlowsEnvironmentVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class ListFlowsResponseBodyFlowsEnvironmentVariables(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        value: str = None,
    ):
        self.description = description
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

