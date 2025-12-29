# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class GetFunctionVersionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.GetFunctionVersionResponseBodyResult = None,
        status: str = None,
    ):
        # The error code.
        self.code = code
        # The HTTP status code.
        self.http_code = http_code
        # The maximum duration for which a task can be executed.
        self.latency = latency
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The result body.
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
            temp_model = main_models.GetFunctionVersionResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetFunctionVersionResponseBodyResult(DaraModel):
    def __init__(
        self,
        function_name: str = None,
        function_type: str = None,
        model_type: str = None,
        version_config: main_models.GetFunctionVersionResponseBodyResultVersionConfig = None,
        version_id: int = None,
        version_name: str = None,
    ):
        # The name of the feature.
        self.function_name = function_name
        # The type of the feature. Valid values:
        # 
        # *   PAAS
        # *   SAAS
        self.function_type = function_type
        # The type of the model.
        self.model_type = model_type
        # The configuration information.
        self.version_config = version_config
        # The ID of the version.
        self.version_id = version_id
        # The name of the version.
        self.version_name = version_name

    def validate(self):
        if self.version_config:
            self.version_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function_name is not None:
            result['FunctionName'] = self.function_name

        if self.function_type is not None:
            result['FunctionType'] = self.function_type

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.version_config is not None:
            result['VersionConfig'] = self.version_config.to_map()

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('VersionConfig') is not None:
            temp_model = main_models.GetFunctionVersionResponseBodyResultVersionConfig()
            self.version_config = temp_model.from_map(m.get('VersionConfig'))

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

class GetFunctionVersionResponseBodyResultVersionConfig(DaraModel):
    def __init__(
        self,
        create_parameters: List[main_models.GetFunctionVersionResponseBodyResultVersionConfigCreateParameters] = None,
        depends: List[main_models.GetFunctionVersionResponseBodyResultVersionConfigDepends] = None,
        usage_parameters: List[main_models.GetFunctionVersionResponseBodyResultVersionConfigUsageParameters] = None,
    ):
        # The parameters that are used to create the instance.
        self.create_parameters = create_parameters
        # The dependencies of the instance.
        self.depends = depends
        # The parameters that are used during online use of the instance.
        self.usage_parameters = usage_parameters

    def validate(self):
        if self.create_parameters:
            for v1 in self.create_parameters:
                 if v1:
                    v1.validate()
        if self.depends:
            for v1 in self.depends:
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
        result['CreateParameters'] = []
        if self.create_parameters is not None:
            for k1 in self.create_parameters:
                result['CreateParameters'].append(k1.to_map() if k1 else None)

        result['Depends'] = []
        if self.depends is not None:
            for k1 in self.depends:
                result['Depends'].append(k1.to_map() if k1 else None)

        result['UsageParameters'] = []
        if self.usage_parameters is not None:
            for k1 in self.usage_parameters:
                result['UsageParameters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.create_parameters = []
        if m.get('CreateParameters') is not None:
            for k1 in m.get('CreateParameters'):
                temp_model = main_models.GetFunctionVersionResponseBodyResultVersionConfigCreateParameters()
                self.create_parameters.append(temp_model.from_map(k1))

        self.depends = []
        if m.get('Depends') is not None:
            for k1 in m.get('Depends'):
                temp_model = main_models.GetFunctionVersionResponseBodyResultVersionConfigDepends()
                self.depends.append(temp_model.from_map(k1))

        self.usage_parameters = []
        if m.get('UsageParameters') is not None:
            for k1 in m.get('UsageParameters'):
                temp_model = main_models.GetFunctionVersionResponseBodyResultVersionConfigUsageParameters()
                self.usage_parameters.append(temp_model.from_map(k1))

        return self

class GetFunctionVersionResponseBodyResultVersionConfigUsageParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        required: str = None,
    ):
        # The name of the instance.
        self.name = name
        # Indicates whether the parameter is required.
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.required is not None:
            result['Required'] = self.required

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        return self

class GetFunctionVersionResponseBodyResultVersionConfigDepends(DaraModel):
    def __init__(
        self,
        condition: str = None,
        dependency: str = None,
        description: str = None,
    ):
        # The condition.
        self.condition = condition
        # The dependency.
        self.dependency = dependency
        # The description.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['Condition'] = self.condition

        if self.dependency is not None:
            result['Dependency'] = self.dependency

        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')

        if m.get('Dependency') is not None:
            self.dependency = m.get('Dependency')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

class GetFunctionVersionResponseBodyResultVersionConfigCreateParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        required: str = None,
    ):
        # The name of the parameter.
        self.name = name
        # Indicates whether the parameter is required.
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.required is not None:
            result['Required'] = self.required

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        return self

