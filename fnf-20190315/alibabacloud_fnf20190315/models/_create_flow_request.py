# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fnf20190315 import models as main_models
from darabonba.model import DaraModel

class CreateFlowRequest(DaraModel):
    def __init__(
        self,
        definition: str = None,
        description: str = None,
        environment: main_models.CreateFlowRequestEnvironment = None,
        execution_mode: str = None,
        external_storage_location: str = None,
        name: str = None,
        resource_group_id: str = None,
        role_arn: str = None,
        type: str = None,
    ):
        # The definition of the workflow. The definition must comply with the flow definition language (FDL) syntax. Considering compatibility, the system supports two flow definition specifications.
        # 
        # >  In the preceding flow definition example, Name:my_flow_name is the workflow name, which must be consistent with the input parameter Name
        # 
        # This parameter is required.
        self.definition = definition
        # The description of the flow.
        # 
        # This parameter is required.
        self.description = description
        self.environment = environment
        # The execution mode. Valid values: Express and Standard. Considering compatibility, an empty string is equivalent to the Standard execution mode.
        self.execution_mode = execution_mode
        # The path of the external storage.
        self.external_storage_location = external_storage_location
        # The name of the flow. The name is unique within the same region and cannot be modified after the flow is created. Set this parameter based on the following rules:
        # 
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must start with a letter or an underscore (_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.name = name
        self.resource_group_id = resource_group_id
        # The Alibaba Cloud resource name (ARN) of the authorized role on which the execution of the flow relies. During the execution of the flow, CloudFlow assumes the role to call API operations of relevant services.
        self.role_arn = role_arn
        # The type of the flow. Set this parameter to **FDL**.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.environment:
            self.environment.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.definition is not None:
            result['Definition'] = self.definition

        if self.description is not None:
            result['Description'] = self.description

        if self.environment is not None:
            result['Environment'] = self.environment.to_map()

        if self.execution_mode is not None:
            result['ExecutionMode'] = self.execution_mode

        if self.external_storage_location is not None:
            result['ExternalStorageLocation'] = self.external_storage_location

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
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Environment') is not None:
            temp_model = main_models.CreateFlowRequestEnvironment()
            self.environment = temp_model.from_map(m.get('Environment'))

        if m.get('ExecutionMode') is not None:
            self.execution_mode = m.get('ExecutionMode')

        if m.get('ExternalStorageLocation') is not None:
            self.external_storage_location = m.get('ExternalStorageLocation')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateFlowRequestEnvironment(DaraModel):
    def __init__(
        self,
        variables: List[main_models.CreateFlowRequestEnvironmentVariables] = None,
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
                temp_model = main_models.CreateFlowRequestEnvironmentVariables()
                self.variables.append(temp_model.from_map(k1))

        return self



class CreateFlowRequestEnvironmentVariables(DaraModel):
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

