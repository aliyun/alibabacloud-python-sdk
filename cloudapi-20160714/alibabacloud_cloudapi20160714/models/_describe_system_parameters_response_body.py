# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeSystemParametersResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        system_params: main_models.DescribeSystemParametersResponseBodySystemParams = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned information about system parameters. It is an array that consists of SystemParam data.
        self.system_params = system_params

    def validate(self):
        if self.system_params:
            self.system_params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.system_params is not None:
            result['SystemParams'] = self.system_params.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SystemParams') is not None:
            temp_model = main_models.DescribeSystemParametersResponseBodySystemParams()
            self.system_params = temp_model.from_map(m.get('SystemParams'))

        return self

class DescribeSystemParametersResponseBodySystemParams(DaraModel):
    def __init__(
        self,
        system_param_item: List[main_models.DescribeSystemParametersResponseBodySystemParamsSystemParamItem] = None,
    ):
        self.system_param_item = system_param_item

    def validate(self):
        if self.system_param_item:
            for v1 in self.system_param_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SystemParamItem'] = []
        if self.system_param_item is not None:
            for k1 in self.system_param_item:
                result['SystemParamItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.system_param_item = []
        if m.get('SystemParamItem') is not None:
            for k1 in m.get('SystemParamItem'):
                temp_model = main_models.DescribeSystemParametersResponseBodySystemParamsSystemParamItem()
                self.system_param_item.append(temp_model.from_map(k1))

        return self

class DescribeSystemParametersResponseBodySystemParamsSystemParamItem(DaraModel):
    def __init__(
        self,
        demo_value: str = None,
        description: str = None,
        param_name: str = None,
        param_type: str = None,
    ):
        # Examples
        self.demo_value = demo_value
        # The description of a parameter.
        self.description = description
        # The name of the parameter.
        self.param_name = param_name
        # The type of the parameter.
        self.param_type = param_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value

        if self.description is not None:
            result['Description'] = self.description

        if self.param_name is not None:
            result['ParamName'] = self.param_name

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        return self

