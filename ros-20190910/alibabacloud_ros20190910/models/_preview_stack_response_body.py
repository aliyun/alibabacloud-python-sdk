# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class PreviewStackResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        stack: main_models.PreviewStackResponseBodyStack = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the stack that is previewed.
        self.stack = stack

    def validate(self):
        if self.stack:
            self.stack.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stack is not None:
            result['Stack'] = self.stack.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Stack') is not None:
            temp_model = main_models.PreviewStackResponseBodyStack()
            self.stack = temp_model.from_map(m.get('Stack'))

        return self

class PreviewStackResponseBodyStack(DaraModel):
    def __init__(
        self,
        description: str = None,
        disable_rollback: bool = None,
        log: main_models.PreviewStackResponseBodyStackLog = None,
        parameters: List[main_models.PreviewStackResponseBodyStackParameters] = None,
        region_id: str = None,
        resources: List[main_models.PreviewStackResponseBodyStackResources] = None,
        stack_name: str = None,
        stack_policy_body: Dict[str, Any] = None,
        template_description: str = None,
        timeout_in_minutes: int = None,
    ):
        # The description of the stack.
        self.description = description
        # Indicates whether rollback is disabled for the resources when the stack fails to be created.
        self.disable_rollback = disable_rollback
        # The log that is generated when the stack is run.
        self.log = log
        # The parameters of the stack.
        self.parameters = parameters
        # The region where the stack resides.
        self.region_id = region_id
        # The resources in the stack.
        self.resources = resources
        # The stack name.
        self.stack_name = stack_name
        # The structure that contains the stack policy body.
        self.stack_policy_body = stack_policy_body
        # The description of the template.
        self.template_description = template_description
        # The timeout period for creating the stack.
        # 
        # Unit: minutes.
        self.timeout_in_minutes = timeout_in_minutes

    def validate(self):
        if self.log:
            self.log.validate()
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback

        if self.log is not None:
            result['Log'] = self.log.to_map()

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        if self.stack_name is not None:
            result['StackName'] = self.stack_name

        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body

        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description

        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')

        if m.get('Log') is not None:
            temp_model = main_models.PreviewStackResponseBodyStackLog()
            self.log = temp_model.from_map(m.get('Log'))

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.PreviewStackResponseBodyStackParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.PreviewStackResponseBodyStackResources()
                self.resources.append(temp_model.from_map(k1))

        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')

        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')

        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')

        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')

        return self

class PreviewStackResponseBodyStackResources(DaraModel):
    def __init__(
        self,
        acs_resource_type: str = None,
        action: str = None,
        description: str = None,
        logical_resource_id: str = None,
        physical_resource_id: str = None,
        properties: Dict[str, Any] = None,
        replacement: str = None,
        required_by: List[str] = None,
        resource_type: str = None,
        stack: Dict[str, Any] = None,
    ):
        # The resource type of an Alibaba Cloud service.
        self.acs_resource_type = acs_resource_type
        # The action that is performed on the resource. Valid values:
        # 
        # *   Add
        # *   Modify
        # *   Remove
        # *   None
        self.action = action
        # The description of the resource.
        self.description = description
        # The logical ID of the resource.
        self.logical_resource_id = logical_resource_id
        # The physical ID of the resource.
        # 
        # This parameter is returned only if Action is set to Modify or Remove.
        self.physical_resource_id = physical_resource_id
        # The resource properties.
        self.properties = properties
        # Indicates whether a replacement update is performed on the template. Valid values:
        # 
        # *   True: A replacement update is performed on the template.
        # *   False: A change is made on the template.
        # *   Conditional: A replacement update may be performed on the template. You can check whether a replacement update is performed when the template is in use.
        # 
        # > This parameter is returned only if Action is set to Modify.
        self.replacement = replacement
        # The resources on which the stack depends.
        self.required_by = required_by
        # The resource type.
        self.resource_type = resource_type
        # The information about the nested stack. The data structure of the value is the same as the data structure of the entire response.
        self.stack = stack

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acs_resource_type is not None:
            result['AcsResourceType'] = self.acs_resource_type

        if self.action is not None:
            result['Action'] = self.action

        if self.description is not None:
            result['Description'] = self.description

        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id

        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.replacement is not None:
            result['Replacement'] = self.replacement

        if self.required_by is not None:
            result['RequiredBy'] = self.required_by

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.stack is not None:
            result['Stack'] = self.stack

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcsResourceType') is not None:
            self.acs_resource_type = m.get('AcsResourceType')

        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')

        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('Replacement') is not None:
            self.replacement = m.get('Replacement')

        if m.get('RequiredBy') is not None:
            self.required_by = m.get('RequiredBy')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Stack') is not None:
            self.stack = m.get('Stack')

        return self

class PreviewStackResponseBodyStackParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The name of the parameter.
        self.parameter_key = parameter_key
        # The value of the parameter.
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key

        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        return self

class PreviewStackResponseBodyStackLog(DaraModel):
    def __init__(
        self,
        terraform_logs: List[main_models.PreviewStackResponseBodyStackLogTerraformLogs] = None,
    ):
        # The Terraform logs. This parameter is returned only if the stack is a Terraform stack.
        # 
        # > This parameter contains the logs of previewing the stack.
        self.terraform_logs = terraform_logs

    def validate(self):
        if self.terraform_logs:
            for v1 in self.terraform_logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TerraformLogs'] = []
        if self.terraform_logs is not None:
            for k1 in self.terraform_logs:
                result['TerraformLogs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.terraform_logs = []
        if m.get('TerraformLogs') is not None:
            for k1 in m.get('TerraformLogs'):
                temp_model = main_models.PreviewStackResponseBodyStackLogTerraformLogs()
                self.terraform_logs.append(temp_model.from_map(k1))

        return self

class PreviewStackResponseBodyStackLogTerraformLogs(DaraModel):
    def __init__(
        self,
        command: str = None,
        content: str = None,
        stream: str = None,
    ):
        # The name of the Terraform command that is run. Valid values:
        # 
        # *   apply
        # *   plan
        # *   destroy
        # *   version
        # 
        # For more information about Terraform commands, see [Basic CLI Features](https://www.terraform.io/cli/commands).
        self.command = command
        # The content of the output stream that is returned after the command is run.
        self.content = content
        # The output stream. Valid values:
        # 
        # *   stdout: standard output stream
        # *   stderr: standard error stream
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command is not None:
            result['Command'] = self.command

        if self.content is not None:
            result['Content'] = self.content

        if self.stream is not None:
            result['Stream'] = self.stream

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        return self

