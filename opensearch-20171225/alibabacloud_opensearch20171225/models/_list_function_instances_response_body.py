# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class ListFunctionInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: int = None,
        message: str = None,
        request_id: str = None,
        result: List[main_models.ListFunctionInstancesResponseBodyResult] = None,
        status: str = None,
        total_count: int = None,
    ):
        # The error code. If no error occurs, the parameter is left empty.
        self.code = code
        # The HTTP status code.
        self.http_code = http_code
        # The time consumed for the request, in milliseconds.
        self.latency = latency
        # The error message. If no error occurs, the parameter is left empty.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The information about the instances.
        self.result = result
        # The status of the request.
        self.status = status
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

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

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

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

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListFunctionInstancesResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFunctionInstancesResponseBodyResult(DaraModel):
    def __init__(
        self,
        belongs: main_models.ListFunctionInstancesResponseBodyResultBelongs = None,
        create_parameters: List[main_models.ListFunctionInstancesResponseBodyResultCreateParameters] = None,
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
        usage_parameters: List[main_models.ListFunctionInstancesResponseBodyResultUsageParameters] = None,
        version_id: int = None,
    ):
        # The information about the instance.
        self.belongs = belongs
        # The parameters of the instance.
        self.create_parameters = create_parameters
        # The time when the instance was created.
        self.create_time = create_time
        # The cron expression used to schedule training, in the format of (Minutes Hours DayofMonth Month DayofWeek). If the value is empty, it indicates that no periodic training is performed.
        self.cron = cron
        # The description.
        self.description = description
        # The extended information, which is a JSON string. It includes model evaluation information and error information.
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
        # *   builtin: The instance is created by system.
        self.source = source
        # The state of the instance. Valid values:
        # 
        # 1.  unavailable: No model is available. Models must be trained before you can use them.
        # 2.  available: Models can be used.
        self.status = status
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
            temp_model = main_models.ListFunctionInstancesResponseBodyResultBelongs()
            self.belongs = temp_model.from_map(m.get('Belongs'))

        self.create_parameters = []
        if m.get('CreateParameters') is not None:
            for k1 in m.get('CreateParameters'):
                temp_model = main_models.ListFunctionInstancesResponseBodyResultCreateParameters()
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

        self.usage_parameters = []
        if m.get('UsageParameters') is not None:
            for k1 in m.get('UsageParameters'):
                temp_model = main_models.ListFunctionInstancesResponseBodyResultUsageParameters()
                self.usage_parameters.append(temp_model.from_map(k1))

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

class ListFunctionInstancesResponseBodyResultUsageParameters(DaraModel):
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

class ListFunctionInstancesResponseBodyResultCreateParameters(DaraModel):
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

class ListFunctionInstancesResponseBodyResultBelongs(DaraModel):
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

