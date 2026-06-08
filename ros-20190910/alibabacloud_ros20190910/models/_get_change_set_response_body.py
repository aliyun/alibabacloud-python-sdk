# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class GetChangeSetResponseBody(DaraModel):
    def __init__(
        self,
        change_set_id: str = None,
        change_set_name: str = None,
        change_set_type: str = None,
        changes: List[Dict[str, Any]] = None,
        create_time: str = None,
        description: str = None,
        disable_rollback: bool = None,
        execution_status: str = None,
        log: main_models.GetChangeSetResponseBodyLog = None,
        parameters: List[main_models.GetChangeSetResponseBodyParameters] = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        stack_id: str = None,
        stack_name: str = None,
        status: str = None,
        status_reason: str = None,
        tags: List[main_models.GetChangeSetResponseBodyTags] = None,
        template_body: str = None,
        timeout_in_minutes: int = None,
    ):
        # The ID of the change set.
        self.change_set_id = change_set_id
        # The name of the change set.
        self.change_set_name = change_set_name
        # The type of the change set.
        self.change_set_type = change_set_type
        # The changes of the change set.
        self.changes = changes
        # The time when the change set was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the change set.
        self.description = description
        # Indicates whether rollback was performed when the stack failed to be created or updated.
        self.disable_rollback = disable_rollback
        # The execution status of the change set.
        self.execution_status = execution_status
        # The output logs of the change set.
        self.log = log
        # The parameters of the stack.
        self.parameters = parameters
        # The region ID of the change set.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        # The ID of the stack with which the change set is associated.
        self.stack_id = stack_id
        # The name of the stack with which the change set is associated.
        self.stack_name = stack_name
        # The status of the change set.
        self.status = status
        # The reason why the change set is in its current state.
        self.status_reason = status_reason
        self.tags = tags
        # The template body of the change set.
        # 
        # > This parameter takes effect only if you set ShowTemplate to true.
        self.template_body = template_body
        # The timeout period that is specified for the stack creation or update operation.
        self.timeout_in_minutes = timeout_in_minutes

    def validate(self):
        if self.log:
            self.log.validate()
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id

        if self.change_set_name is not None:
            result['ChangeSetName'] = self.change_set_name

        if self.change_set_type is not None:
            result['ChangeSetType'] = self.change_set_type

        if self.changes is not None:
            result['Changes'] = self.changes

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback

        if self.execution_status is not None:
            result['ExecutionStatus'] = self.execution_status

        if self.log is not None:
            result['Log'] = self.log.to_map()

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        if self.stack_name is not None:
            result['StackName'] = self.stack_name

        if self.status is not None:
            result['Status'] = self.status

        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.template_body is not None:
            result['TemplateBody'] = self.template_body

        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')

        if m.get('ChangeSetName') is not None:
            self.change_set_name = m.get('ChangeSetName')

        if m.get('ChangeSetType') is not None:
            self.change_set_type = m.get('ChangeSetType')

        if m.get('Changes') is not None:
            self.changes = m.get('Changes')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')

        if m.get('ExecutionStatus') is not None:
            self.execution_status = m.get('ExecutionStatus')

        if m.get('Log') is not None:
            temp_model = main_models.GetChangeSetResponseBodyLog()
            self.log = temp_model.from_map(m.get('Log'))

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.GetChangeSetResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetChangeSetResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')

        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')

        return self

class GetChangeSetResponseBodyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetChangeSetResponseBodyParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The key of the parameter.
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

class GetChangeSetResponseBodyLog(DaraModel):
    def __init__(
        self,
        terraform_logs: List[main_models.GetChangeSetResponseBodyLogTerraformLogs] = None,
    ):
        # The Terraform logs. This parameter is returned only for change sets of Terraform stacks.
        # 
        # > This parameter is not returned for change sets that are in the Creating state. This parameter indicates the logs of the change set creation operation for Terraform stacks.
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
                temp_model = main_models.GetChangeSetResponseBodyLogTerraformLogs()
                self.terraform_logs.append(temp_model.from_map(k1))

        return self

class GetChangeSetResponseBodyLogTerraformLogs(DaraModel):
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
        # For more information about Terraform commands, see [Command](https://www.terraform.io/cli/commands).
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

