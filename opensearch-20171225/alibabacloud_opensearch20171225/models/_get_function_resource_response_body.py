# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class GetFunctionResourceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: float = None,
        message: str = None,
        request_id: str = None,
        result: main_models.GetFunctionResourceResponseBodyResult = None,
        status: str = None,
    ):
        # The error code returned. If no error occurs, this value is empty.
        self.code = code
        # The HTTP status code returned.
        self.http_code = http_code
        # The time consumed for the API request. Unit: milliseconds.
        self.latency = latency
        # The error message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.result = result
        # The HTTP status code. Valid values:
        # 
        # *   OK
        # *   FAIL
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
            temp_model = main_models.GetFunctionResourceResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetFunctionResourceResponseBodyResult(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        data: main_models.GetFunctionResourceResponseBodyResultData = None,
        description: str = None,
        function_name: str = None,
        modify_time: int = None,
        referenced_instances: List[str] = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The time when the resource was created. Unit: milliseconds.
        self.create_time = create_time
        # The resource data. The data structure varies with the resource type.
        self.data = data
        # The description of the resource.
        self.description = description
        # The name of the feature.
        self.function_name = function_name
        # The time when the resource was modified. Unit: milliseconds.
        self.modify_time = modify_time
        # The algorithm instances that are referenced.
        self.referenced_instances = referenced_instances
        # The name of the resource.
        self.resource_name = resource_name
        # The type of the resource.
        self.resource_type = resource_type

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.function_name is not None:
            result['FunctionName'] = self.function_name

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.referenced_instances is not None:
            result['ReferencedInstances'] = self.referenced_instances

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Data') is not None:
            temp_model = main_models.GetFunctionResourceResponseBodyResultData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ReferencedInstances') is not None:
            self.referenced_instances = m.get('ReferencedInstances')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class GetFunctionResourceResponseBodyResultData(DaraModel):
    def __init__(
        self,
        content: str = None,
        generators: List[main_models.GetFunctionResourceResponseBodyResultDataGenerators] = None,
    ):
        # The content of the file that corresponds to a resource of the raw_file type.
        self.content = content
        # The feature generators that correspond to resources of the feature_generator type.
        self.generators = generators

    def validate(self):
        if self.generators:
            for v1 in self.generators:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        result['Generators'] = []
        if self.generators is not None:
            for k1 in self.generators:
                result['Generators'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        self.generators = []
        if m.get('Generators') is not None:
            for k1 in m.get('Generators'):
                temp_model = main_models.GetFunctionResourceResponseBodyResultDataGenerators()
                self.generators.append(temp_model.from_map(k1))

        return self

class GetFunctionResourceResponseBodyResultDataGenerators(DaraModel):
    def __init__(
        self,
        generator: str = None,
        input: main_models.GetFunctionResourceResponseBodyResultDataGeneratorsInput = None,
        output: str = None,
    ):
        # The type of the feature generator.
        self.generator = generator
        # The input.
        self.input = input
        # The name of the output feature.
        self.output = output

    def validate(self):
        if self.input:
            self.input.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.generator is not None:
            result['Generator'] = self.generator

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.output is not None:
            result['Output'] = self.output

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Generator') is not None:
            self.generator = m.get('Generator')

        if m.get('Input') is not None:
            temp_model = main_models.GetFunctionResourceResponseBodyResultDataGeneratorsInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('Output') is not None:
            self.output = m.get('Output')

        return self

class GetFunctionResourceResponseBodyResultDataGeneratorsInput(DaraModel):
    def __init__(
        self,
        features: List[main_models.GetFunctionResourceResponseBodyResultDataGeneratorsInputFeatures] = None,
    ):
        # The input features.
        self.features = features

    def validate(self):
        if self.features:
            for v1 in self.features:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Features'] = []
        if self.features is not None:
            for k1 in self.features:
                result['Features'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.features = []
        if m.get('Features') is not None:
            for k1 in m.get('Features'):
                temp_model = main_models.GetFunctionResourceResponseBodyResultDataGeneratorsInputFeatures()
                self.features.append(temp_model.from_map(k1))

        return self

class GetFunctionResourceResponseBodyResultDataGeneratorsInputFeatures(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The name of the feature.
        self.name = name
        # The type of the feature.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

