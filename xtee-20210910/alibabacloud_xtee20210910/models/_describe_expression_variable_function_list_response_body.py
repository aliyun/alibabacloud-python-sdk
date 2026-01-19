# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeExpressionVariableFunctionListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: List[main_models.DescribeExpressionVariableFunctionListResponseBodyResultObject] = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return object
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeExpressionVariableFunctionListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        return self

class DescribeExpressionVariableFunctionListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        description: str = None,
        key: str = None,
        max_param_size: int = None,
        min_param_size: int = None,
        param_types: str = None,
        redirect: bool = None,
        return_types: str = None,
        value: str = None,
    ):
        # Description information.
        self.description = description
        # Function name
        self.key = key
        # Maximum number of parameters
        self.max_param_size = max_param_size
        # Minimum number of parameters
        self.min_param_size = min_param_size
        # Parameter types
        self.param_types = param_types
        # Whether it is directly invoked
        self.redirect = redirect
        # Method return types
        self.return_types = return_types
        # Function value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.key is not None:
            result['key'] = self.key

        if self.max_param_size is not None:
            result['maxParamSize'] = self.max_param_size

        if self.min_param_size is not None:
            result['minParamSize'] = self.min_param_size

        if self.param_types is not None:
            result['paramTypes'] = self.param_types

        if self.redirect is not None:
            result['redirect'] = self.redirect

        if self.return_types is not None:
            result['returnTypes'] = self.return_types

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('maxParamSize') is not None:
            self.max_param_size = m.get('maxParamSize')

        if m.get('minParamSize') is not None:
            self.min_param_size = m.get('minParamSize')

        if m.get('paramTypes') is not None:
            self.param_types = m.get('paramTypes')

        if m.get('redirect') is not None:
            self.redirect = m.get('redirect')

        if m.get('returnTypes') is not None:
            self.return_types = m.get('returnTypes')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

