# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class GetFunctionInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.GetFunctionInstanceResponseBodyResult = None,
        status: str = None,
    ):
        # The error code. If no error occurs, this parameter is left empty.
        self.code = code
        # The HTTP status code.
        self.http_code = http_code
        # The time consumed for the request, in milliseconds.
        self.latency = latency
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The details of the instance.
        self.result = result
        # The status of the request.
        self.status = status

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.latency is not None:
            result['Latency'] = self.latency

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('Latency') is not None:
            self.latency = m.get('Latency')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetFunctionInstanceResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetFunctionInstanceResponseBodyResult(DaraModel):
    def __init__(
        self,
        belongs: main_models.GetFunctionInstanceResponseBodyResultBelongs = None,
        create_parameters: List[main_models.GetFunctionInstanceResponseBodyResultCreateParameters] = None,
        create_time: int = None,
        cron: str = None,
        description: str = None,
        extend_info: str = None,
        function_name: str = None,
        function_type: str = None,
        instance_name: str = None,
        model_type: str = None,
        source: str = None,
        status: str = None,
        task: main_models.GetFunctionInstanceResponseBodyResultTask = None,
        usage_parameters: List[main_models.GetFunctionInstanceResponseBodyResultUsageParameters] = None,
        version_id: int = None,
    ):
        # The information about the instance.
        self.belongs = belongs
        # The parameters that are used to create the instance.
        self.create_parameters = create_parameters
        # The time when the task was created. Unit: milliseconds.
        self.create_time = create_time
        # The cron expression used to schedule training, in the format of (Minutes Hours DayofMonth Month DayofWeek). If the value is empty, it indicates that no periodic training is performed.
        self.cron = cron
        # The description of the instance.
        self.description = description
        # The extended information, which is a JSON string.
        self.extend_info = extend_info
        # The name of the feature.
        self.function_name = function_name
        # The type of the feature.
        self.function_type = function_type
        # The name of the instance.
        self.instance_name = instance_name
        # The type of the model.
        self.model_type = model_type
        # How the instance is created. Valid values:
        # 
        # *   user: The instance is created by user.
        # *   builtin: The instance is created by the system.
        self.source = source
        # The status of the instance. Valid values:
        # 
        # 1.  unavailable: No model is available. Models must be trained before you can use them.
        # 2.  available: Models can be used.
        self.status = status
        # The information about the training task. This parameter is not displayed if no task is available.
        self.task = task
        # The parameters that are used.
        self.usage_parameters = usage_parameters
        # The ID of the version.
        self.version_id = version_id

    def validate(self):
        if self.belongs:
            self.belongs.validate()
        if self.create_parameters:
            for v1 in self.create_parameters:
                 if v1:
                    v1.validate()
        if self.task:
            self.task.validate()
        if self.usage_parameters:
            for v1 in self.usage_parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.belongs is not None:
            result['Belongs'] = self.belongs.to_map()

        result['CreateParameters'] = []
        if self.create_parameters is not None:
            for k1 in self.create_parameters:
                result['CreateParameters'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cron is not None:
            result['Cron'] = self.cron

        if self.description is not None:
            result['Description'] = self.description

        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

        if self.function_name is not None:
            result['FunctionName'] = self.function_name

        if self.function_type is not None:
            result['FunctionType'] = self.function_type

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.task is not None:
            result['Task'] = self.task.to_map()

        result['UsageParameters'] = []
        if self.usage_parameters is not None:
            for k1 in self.usage_parameters:
                result['UsageParameters'].append(k1.to_map() if k1 else None)

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Belongs') is not None:
            temp_model = main_models.GetFunctionInstanceResponseBodyResultBelongs()
            self.belongs = temp_model.from_map(m.get('Belongs'))

        self.create_parameters = []
        if m.get('CreateParameters') is not None:
            for k1 in m.get('CreateParameters'):
                temp_model = main_models.GetFunctionInstanceResponseBodyResultCreateParameters()
                self.create_parameters.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Cron') is not None:
            self.cron = m.get('Cron')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Task') is not None:
            temp_model = main_models.GetFunctionInstanceResponseBodyResultTask()
            self.task = temp_model.from_map(m.get('Task'))

        self.usage_parameters = []
        if m.get('UsageParameters') is not None:
            for k1 in m.get('UsageParameters'):
                temp_model = main_models.GetFunctionInstanceResponseBodyResultUsageParameters()
                self.usage_parameters.append(temp_model.from_map(k1))

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

class GetFunctionInstanceResponseBodyResultUsageParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the parameter.
        self.name = name
        # The value of the parameter.
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

class GetFunctionInstanceResponseBodyResultTask(DaraModel):
    def __init__(
        self,
        dag_status: str = None,
        last_run_time: int = None,
    ):
        # The status of the task. Valid values:
        # 
        # *   success: succeeded
        # *   failed: failed
        # *   untrained: to be trained
        # *   pending: being scheduled
        # *   running: being trained
        self.dag_status = dag_status
        # The time consumed for the most recent run, in milliseconds.
        self.last_run_time = last_run_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dag_status is not None:
            result['DagStatus'] = self.dag_status

        if self.last_run_time is not None:
            result['LastRunTime'] = self.last_run_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagStatus') is not None:
            self.dag_status = m.get('DagStatus')

        if m.get('LastRunTime') is not None:
            self.last_run_time = m.get('LastRunTime')

        return self

class GetFunctionInstanceResponseBodyResultCreateParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the parameter.
        self.name = name
        # The value of the parameter.
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

class GetFunctionInstanceResponseBodyResultBelongs(DaraModel):
    def __init__(
        self,
        category: str = None,
        domain: str = None,
        language: str = None,
    ):
        # The category.
        self.category = category
        # The industry.
        self.domain = domain
        # The abbreviation of the language that applies.
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.language is not None:
            result['Language'] = self.language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        return self

