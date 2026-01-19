# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeOperatorListByTypeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: List[main_models.DescribeOperatorListByTypeResponseBodyResultObject] = None,
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
                temp_model = main_models.DescribeOperatorListByTypeResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        return self

class DescribeOperatorListByTypeResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        field_type: str = None,
        operators: List[main_models.DescribeOperatorListByTypeResponseBodyResultObjectOperators] = None,
    ):
        # Return value type
        self.field_type = field_type
        # Operator list
        self.operators = operators

    def validate(self):
        if self.operators:
            for v1 in self.operators:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_type is not None:
            result['fieldType'] = self.field_type

        result['operators'] = []
        if self.operators is not None:
            for k1 in self.operators:
                result['operators'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldType') is not None:
            self.field_type = m.get('fieldType')

        self.operators = []
        if m.get('operators') is not None:
            for k1 in m.get('operators'):
                temp_model = main_models.DescribeOperatorListByTypeResponseBodyResultObjectOperators()
                self.operators.append(temp_model.from_map(k1))

        return self

class DescribeOperatorListByTypeResponseBodyResultObjectOperators(DaraModel):
    def __init__(
        self,
        code: str = None,
        has_right_variable: bool = None,
        name: str = None,
    ):
        # Operator code
        self.code = code
        # Whether it contains a right variable
        self.has_right_variable = has_right_variable
        # Operator name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.has_right_variable is not None:
            result['hasRightVariable'] = self.has_right_variable

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('hasRightVariable') is not None:
            self.has_right_variable = m.get('hasRightVariable')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

