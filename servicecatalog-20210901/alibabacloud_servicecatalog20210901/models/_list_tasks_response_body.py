# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class ListTasksResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        task_details: List[main_models.ListTasksResponseBodyTaskDetails] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.task_details = task_details
        self.total_count = total_count

    def validate(self):
        if self.task_details:
            for v1 in self.task_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TaskDetails'] = []
        if self.task_details is not None:
            for k1 in self.task_details:
                result['TaskDetails'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.task_details = []
        if m.get('TaskDetails') is not None:
            for k1 in m.get('TaskDetails'):
                temp_model = main_models.ListTasksResponseBodyTaskDetails()
                self.task_details.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTasksResponseBodyTaskDetails(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        log: main_models.ListTasksResponseBodyTaskDetailsLog = None,
        outputs: List[main_models.ListTasksResponseBodyTaskDetailsOutputs] = None,
        parameters: List[main_models.ListTasksResponseBodyTaskDetailsParameters] = None,
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
        task_type: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.log = log
        self.outputs = outputs
        self.parameters = parameters
        self.portfolio_id = portfolio_id
        self.product_id = product_id
        self.product_name = product_name
        self.product_version_id = product_version_id
        self.product_version_name = product_version_name
        self.provisioned_product_id = provisioned_product_id
        self.provisioned_product_name = provisioned_product_name
        self.status = status
        self.status_message = status_message
        # 代表资源名称的资源属性字段
        self.task_id = task_id
        self.task_type = task_type
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
            temp_model = main_models.ListTasksResponseBodyTaskDetailsLog()
            self.log = temp_model.from_map(m.get('Log'))

        self.outputs = []
        if m.get('Outputs') is not None:
            for k1 in m.get('Outputs'):
                temp_model = main_models.ListTasksResponseBodyTaskDetailsOutputs()
                self.outputs.append(temp_model.from_map(k1))

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.ListTasksResponseBodyTaskDetailsParameters()
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

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListTasksResponseBodyTaskDetailsParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
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

class ListTasksResponseBodyTaskDetailsOutputs(DaraModel):
    def __init__(
        self,
        description: str = None,
        output_key: str = None,
        output_value: str = None,
    ):
        self.description = description
        self.output_key = output_key
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

class ListTasksResponseBodyTaskDetailsLog(DaraModel):
    def __init__(
        self,
        terraform_logs: List[main_models.ListTasksResponseBodyTaskDetailsLogTerraformLogs] = None,
    ):
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
                temp_model = main_models.ListTasksResponseBodyTaskDetailsLogTerraformLogs()
                self.terraform_logs.append(temp_model.from_map(k1))

        return self

class ListTasksResponseBodyTaskDetailsLogTerraformLogs(DaraModel):
    def __init__(
        self,
        command: str = None,
        content: str = None,
        stream: str = None,
    ):
        self.command = command
        self.content = content
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

