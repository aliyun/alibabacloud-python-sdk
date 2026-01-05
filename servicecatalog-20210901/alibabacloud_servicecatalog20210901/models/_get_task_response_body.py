# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class GetTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_detail: main_models.GetTaskResponseBodyTaskDetail = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The details of the task.
        self.task_detail = task_detail

    def validate(self):
        if self.task_detail:
            self.task_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_detail is not None:
            result['TaskDetail'] = self.task_detail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskDetail') is not None:
            temp_model = main_models.GetTaskResponseBodyTaskDetail()
            self.task_detail = temp_model.from_map(m.get('TaskDetail'))

        return self

class GetTaskResponseBodyTaskDetail(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        log: main_models.GetTaskResponseBodyTaskDetailLog = None,
        outputs: List[main_models.GetTaskResponseBodyTaskDetailOutputs] = None,
        parameters: List[main_models.GetTaskResponseBodyTaskDetailParameters] = None,
        portfolio_id: str = None,
        product_id: str = None,
        product_name: str = None,
        product_version_id: str = None,
        product_version_name: str = None,
        provisioned_product_id: str = None,
        provisioned_product_name: str = None,
        status: str = None,
        status_message: str = None,
        task_id: str = None,
        task_tags: List[main_models.GetTaskResponseBodyTaskDetailTaskTags] = None,
        task_type: str = None,
        update_time: str = None,
    ):
        # The time when the task was created.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The logs of the instance.
        self.log = log
        # The output parameters of the template.
        self.outputs = outputs
        # The parameters that are specified in the template.
        self.parameters = parameters
        # The ID of the product portfolio.
        self.portfolio_id = portfolio_id
        # The ID of the product.
        self.product_id = product_id
        # The name of the product.
        self.product_name = product_name
        # The ID of the product version.
        self.product_version_id = product_version_id
        # The name of the product version.
        self.product_version_name = product_version_name
        # The ID of the product instance.
        self.provisioned_product_id = provisioned_product_id
        # The name of the product instance.
        self.provisioned_product_name = provisioned_product_name
        # The state of the task. Valid values:
        # 
        # *   Succeeded: The task was successful.
        # *   InProgress: The task was in progress.
        # *   Failed: The task failed.
        self.status = status
        # The message that is returned for the status of the task.
        # 
        # > This parameter is returned only when Failed is returned for the Status parameter.
        self.status_message = status_message
        # The ID of the task.
        self.task_id = task_id
        # The custom tags.
        self.task_tags = task_tags
        # The type of the task. Valid values:
        # 
        # *   LaunchProduct: a task that launches the product.
        # *   UpdateProvisionedProduct: a task that updates the information about the product instance.
        # *   TerminateProvisionedProduct: a task that terminates the product instance.
        self.task_type = task_type
        # The time when the task was last modified.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.update_time = update_time

    def validate(self):
        if self.log:
            self.log.validate()
        if self.outputs:
            for v1 in self.outputs:
                 if v1:
                    v1.validate()
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()
        if self.task_tags:
            for v1 in self.task_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.log is not None:
            result['Log'] = self.log.to_map()

        result['Outputs'] = []
        if self.outputs is not None:
            for k1 in self.outputs:
                result['Outputs'].append(k1.to_map() if k1 else None)

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id

        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name

        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id

        if self.provisioned_product_name is not None:
            result['ProvisionedProductName'] = self.provisioned_product_name

        if self.status is not None:
            result['Status'] = self.status

        if self.status_message is not None:
            result['StatusMessage'] = self.status_message

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        result['TaskTags'] = []
        if self.task_tags is not None:
            for k1 in self.task_tags:
                result['TaskTags'].append(k1.to_map() if k1 else None)

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Log') is not None:
            temp_model = main_models.GetTaskResponseBodyTaskDetailLog()
            self.log = temp_model.from_map(m.get('Log'))

        self.outputs = []
        if m.get('Outputs') is not None:
            for k1 in m.get('Outputs'):
                temp_model = main_models.GetTaskResponseBodyTaskDetailOutputs()
                self.outputs.append(temp_model.from_map(k1))

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.GetTaskResponseBodyTaskDetailParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')

        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')

        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')

        if m.get('ProvisionedProductName') is not None:
            self.provisioned_product_name = m.get('ProvisionedProductName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        self.task_tags = []
        if m.get('TaskTags') is not None:
            for k1 in m.get('TaskTags'):
                temp_model = main_models.GetTaskResponseBodyTaskDetailTaskTags()
                self.task_tags.append(temp_model.from_map(k1))

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetTaskResponseBodyTaskDetailTaskTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The custom tag key.
        # 
        # The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        self.key = key
        # The custom tag value.
        # 
        # The value must be 1 to 128 characters in length. It cannot start with `acs:` and cannot contain `http://` or `https://`.
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

class GetTaskResponseBodyTaskDetailParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The name of the input parameter for the template.
        self.parameter_key = parameter_key
        # The value of the input parameter for the template.
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

class GetTaskResponseBodyTaskDetailOutputs(DaraModel):
    def __init__(
        self,
        description: str = None,
        output_key: str = None,
        output_value: str = None,
    ):
        # The description of the output parameter for the template.
        self.description = description
        # The name of the output parameter for the template.
        self.output_key = output_key
        # The value of the output parameter for the template.
        self.output_value = output_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.output_key is not None:
            result['OutputKey'] = self.output_key

        if self.output_value is not None:
            result['OutputValue'] = self.output_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('OutputKey') is not None:
            self.output_key = m.get('OutputKey')

        if m.get('OutputValue') is not None:
            self.output_value = m.get('OutputValue')

        return self

class GetTaskResponseBodyTaskDetailLog(DaraModel):
    def __init__(
        self,
        terraform_logs: List[main_models.GetTaskResponseBodyTaskDetailLogTerraformLogs] = None,
    ):
        # The Terraform logs.
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
                temp_model = main_models.GetTaskResponseBodyTaskDetailLogTerraformLogs()
                self.terraform_logs.append(temp_model.from_map(k1))

        return self

class GetTaskResponseBodyTaskDetailLogTerraformLogs(DaraModel):
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
        # *   stdout: a standard output stream
        # *   stderr: a standard error stream
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

