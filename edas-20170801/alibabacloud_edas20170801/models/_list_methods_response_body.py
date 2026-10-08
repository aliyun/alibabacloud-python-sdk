# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListMethodsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        service_method_list: main_models.ListMethodsResponseBodyServiceMethodList = None,
    ):
        # The HTTP status code.
        self.code = code
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        self.service_method_list = service_method_list

    def validate(self):
        if self.service_method_list:
            self.service_method_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_method_list is not None:
            result['ServiceMethodList'] = self.service_method_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceMethodList') is not None:
            temp_model = main_models.ListMethodsResponseBodyServiceMethodList()
            self.service_method_list = temp_model.from_map(m.get('ServiceMethodList'))

        return self

class ListMethodsResponseBodyServiceMethodList(DaraModel):
    def __init__(
        self,
        service_method: List[main_models.ListMethodsResponseBodyServiceMethodListServiceMethod] = None,
    ):
        self.service_method = service_method

    def validate(self):
        if self.service_method:
            for v1 in self.service_method:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ServiceMethod'] = []
        if self.service_method is not None:
            for k1 in self.service_method:
                result['ServiceMethod'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.service_method = []
        if m.get('ServiceMethod') is not None:
            for k1 in m.get('ServiceMethod'):
                temp_model = main_models.ListMethodsResponseBodyServiceMethodListServiceMethod()
                self.service_method.append(temp_model.from_map(k1))

        return self

class ListMethodsResponseBodyServiceMethodListServiceMethod(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        input_params: main_models.ListMethodsResponseBodyServiceMethodListServiceMethodInputParams = None,
        method_name: str = None,
        output: str = None,
        param_types: main_models.ListMethodsResponseBodyServiceMethodListServiceMethodParamTypes = None,
        service_name: str = None,
    ):
        self.app_name = app_name
        self.input_params = input_params
        self.method_name = method_name
        self.output = output
        self.param_types = param_types
        self.service_name = service_name

    def validate(self):
        if self.input_params:
            self.input_params.validate()
        if self.param_types:
            self.param_types.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.input_params is not None:
            result['InputParams'] = self.input_params.to_map()

        if self.method_name is not None:
            result['MethodName'] = self.method_name

        if self.output is not None:
            result['Output'] = self.output

        if self.param_types is not None:
            result['ParamTypes'] = self.param_types.to_map()

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('InputParams') is not None:
            temp_model = main_models.ListMethodsResponseBodyServiceMethodListServiceMethodInputParams()
            self.input_params = temp_model.from_map(m.get('InputParams'))

        if m.get('MethodName') is not None:
            self.method_name = m.get('MethodName')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('ParamTypes') is not None:
            temp_model = main_models.ListMethodsResponseBodyServiceMethodListServiceMethodParamTypes()
            self.param_types = temp_model.from_map(m.get('ParamTypes'))

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

class ListMethodsResponseBodyServiceMethodListServiceMethodParamTypes(DaraModel):
    def __init__(
        self,
        param_type: List[str] = None,
    ):
        self.param_type = param_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param_type is not None:
            result['ParamType'] = self.param_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        return self

class ListMethodsResponseBodyServiceMethodListServiceMethodInputParams(DaraModel):
    def __init__(
        self,
        input_param: List[str] = None,
    ):
        self.input_param = input_param

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_param is not None:
            result['InputParam'] = self.input_param

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputParam') is not None:
            self.input_param = m.get('InputParam')

        return self

