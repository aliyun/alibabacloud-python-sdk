# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class GetServiceMethodPageResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetServiceMethodPageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetServiceMethodPageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetServiceMethodPageResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        result: List[main_models.GetServiceMethodPageResponseBodyDataResult] = None,
        total_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.result = result
        self.total_size = total_size

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.GetServiceMethodPageResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class GetServiceMethodPageResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        method_controller: str = None,
        name: str = None,
        name_detail: str = None,
        parameter_definitions: List[main_models.GetServiceMethodPageResponseBodyDataResultParameterDefinitions] = None,
        parameter_details: List[str] = None,
        parameter_types: List[str] = None,
        paths: List[str] = None,
        request_methods: List[str] = None,
        return_details: str = None,
        return_type: str = None,
    ):
        self.method_controller = method_controller
        self.name = name
        self.name_detail = name_detail
        self.parameter_definitions = parameter_definitions
        self.parameter_details = parameter_details
        self.parameter_types = parameter_types
        self.paths = paths
        self.request_methods = request_methods
        self.return_details = return_details
        self.return_type = return_type

    def validate(self):
        if self.parameter_definitions:
            for v1 in self.parameter_definitions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.method_controller is not None:
            result['MethodController'] = self.method_controller

        if self.name is not None:
            result['Name'] = self.name

        if self.name_detail is not None:
            result['NameDetail'] = self.name_detail

        result['ParameterDefinitions'] = []
        if self.parameter_definitions is not None:
            for k1 in self.parameter_definitions:
                result['ParameterDefinitions'].append(k1.to_map() if k1 else None)

        if self.parameter_details is not None:
            result['ParameterDetails'] = self.parameter_details

        if self.parameter_types is not None:
            result['ParameterTypes'] = self.parameter_types

        if self.paths is not None:
            result['Paths'] = self.paths

        if self.request_methods is not None:
            result['RequestMethods'] = self.request_methods

        if self.return_details is not None:
            result['ReturnDetails'] = self.return_details

        if self.return_type is not None:
            result['ReturnType'] = self.return_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MethodController') is not None:
            self.method_controller = m.get('MethodController')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NameDetail') is not None:
            self.name_detail = m.get('NameDetail')

        self.parameter_definitions = []
        if m.get('ParameterDefinitions') is not None:
            for k1 in m.get('ParameterDefinitions'):
                temp_model = main_models.GetServiceMethodPageResponseBodyDataResultParameterDefinitions()
                self.parameter_definitions.append(temp_model.from_map(k1))

        if m.get('ParameterDetails') is not None:
            self.parameter_details = m.get('ParameterDetails')

        if m.get('ParameterTypes') is not None:
            self.parameter_types = m.get('ParameterTypes')

        if m.get('Paths') is not None:
            self.paths = m.get('Paths')

        if m.get('RequestMethods') is not None:
            self.request_methods = m.get('RequestMethods')

        if m.get('ReturnDetails') is not None:
            self.return_details = m.get('ReturnDetails')

        if m.get('ReturnType') is not None:
            self.return_type = m.get('ReturnType')

        return self

class GetServiceMethodPageResponseBodyDataResultParameterDefinitions(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        type: str = None,
    ):
        self.description = description
        self.name = name
        self.type = type

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

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

