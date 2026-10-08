# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class GetServiceMethodPageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetServiceMethodPageResponseBodyData = None,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The data that is returned.
        self.data = data
        # The HTTP status code that is returned.
        self.http_code = http_code
        # The additional information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetServiceMethodPageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

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
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The data about the method.
        self.result = result
        # The total number of entries.
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
        parameter_definitions: str = None,
        parameter_details: str = None,
        parameter_names: str = None,
        parameter_types: str = None,
        paths: str = None,
        request_methods: str = None,
        return_definition: main_models.GetServiceMethodPageResponseBodyDataResultReturnDefinition = None,
        return_details: str = None,
        return_type: str = None,
    ):
        # The method.
        self.method_controller = method_controller
        # The name of the method.
        self.name = name
        # The details of the method.
        self.name_detail = name_detail
        # The definition of the parameter.
        self.parameter_definitions = parameter_definitions
        # The details of the parameters.
        self.parameter_details = parameter_details
        # The name of the parameter.
        self.parameter_names = parameter_names
        # The data type of the parameter.
        self.parameter_types = parameter_types
        # The method path.
        self.paths = paths
        # The request method.
        self.request_methods = request_methods
        # The return value.
        self.return_definition = return_definition
        # The details of the response.
        self.return_details = return_details
        # The data format of the response.
        self.return_type = return_type

    def validate(self):
        if self.return_definition:
            self.return_definition.validate()

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

        if self.parameter_definitions is not None:
            result['ParameterDefinitions'] = self.parameter_definitions

        if self.parameter_details is not None:
            result['ParameterDetails'] = self.parameter_details

        if self.parameter_names is not None:
            result['ParameterNames'] = self.parameter_names

        if self.parameter_types is not None:
            result['ParameterTypes'] = self.parameter_types

        if self.paths is not None:
            result['Paths'] = self.paths

        if self.request_methods is not None:
            result['RequestMethods'] = self.request_methods

        if self.return_definition is not None:
            result['ReturnDefinition'] = self.return_definition.to_map()

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

        if m.get('ParameterDefinitions') is not None:
            self.parameter_definitions = m.get('ParameterDefinitions')

        if m.get('ParameterDetails') is not None:
            self.parameter_details = m.get('ParameterDetails')

        if m.get('ParameterNames') is not None:
            self.parameter_names = m.get('ParameterNames')

        if m.get('ParameterTypes') is not None:
            self.parameter_types = m.get('ParameterTypes')

        if m.get('Paths') is not None:
            self.paths = m.get('Paths')

        if m.get('RequestMethods') is not None:
            self.request_methods = m.get('RequestMethods')

        if m.get('ReturnDefinition') is not None:
            temp_model = main_models.GetServiceMethodPageResponseBodyDataResultReturnDefinition()
            self.return_definition = temp_model.from_map(m.get('ReturnDefinition'))

        if m.get('ReturnDetails') is not None:
            self.return_details = m.get('ReturnDetails')

        if m.get('ReturnType') is not None:
            self.return_type = m.get('ReturnType')

        return self

class GetServiceMethodPageResponseBodyDataResultReturnDefinition(DaraModel):
    def __init__(
        self,
        id: str = None,
        type: str = None,
    ):
        # The ID of the return value.
        self.id = id
        # The data format of the response.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

