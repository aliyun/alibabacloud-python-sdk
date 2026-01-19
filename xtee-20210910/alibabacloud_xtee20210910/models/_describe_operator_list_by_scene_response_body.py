# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeOperatorListBySceneResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: List[main_models.DescribeOperatorListBySceneResponseBodyResultObject] = None,
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
            result['requestId'] = self.request_id

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeOperatorListBySceneResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        return self

class DescribeOperatorListBySceneResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        field_type: str = None,
        operators: List[main_models.DescribeOperatorListBySceneResponseBodyResultObjectOperators] = None,
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
                temp_model = main_models.DescribeOperatorListBySceneResponseBodyResultObjectOperators()
                self.operators.append(temp_model.from_map(k1))

        return self

class DescribeOperatorListBySceneResponseBodyResultObjectOperators(DaraModel):
    def __init__(
        self,
        code: str = None,
        has_right_variable: bool = None,
        memo: str = None,
        name: str = None,
        right_variables: List[main_models.DescribeOperatorListBySceneResponseBodyResultObjectOperatorsRightVariables] = None,
    ):
        # Operator code
        self.code = code
        # Whether it contains a right variable
        self.has_right_variable = has_right_variable
        # Description
        self.memo = memo
        # Operator name
        self.name = name
        # Right variable object
        self.right_variables = right_variables

    def validate(self):
        if self.right_variables:
            for v1 in self.right_variables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.has_right_variable is not None:
            result['hasRightVariable'] = self.has_right_variable

        if self.memo is not None:
            result['memo'] = self.memo

        if self.name is not None:
            result['name'] = self.name

        result['rightVariables'] = []
        if self.right_variables is not None:
            for k1 in self.right_variables:
                result['rightVariables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('hasRightVariable') is not None:
            self.has_right_variable = m.get('hasRightVariable')

        if m.get('memo') is not None:
            self.memo = m.get('memo')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.right_variables = []
        if m.get('rightVariables') is not None:
            for k1 in m.get('rightVariables'):
                temp_model = main_models.DescribeOperatorListBySceneResponseBodyResultObjectOperatorsRightVariables()
                self.right_variables.append(temp_model.from_map(k1))

        return self

class DescribeOperatorListBySceneResponseBodyResultObjectOperatorsRightVariables(DaraModel):
    def __init__(
        self,
        field_name: str = None,
        field_type: str = None,
        field_value: str = None,
    ):
        # Field name.
        self.field_name = field_name
        # Field type.
        self.field_type = field_type
        # Field value.
        self.field_value = field_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_name is not None:
            result['fieldName'] = self.field_name

        if self.field_type is not None:
            result['fieldType'] = self.field_type

        if self.field_value is not None:
            result['fieldValue'] = self.field_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldName') is not None:
            self.field_name = m.get('fieldName')

        if m.get('fieldType') is not None:
            self.field_type = m.get('fieldType')

        if m.get('fieldValue') is not None:
            self.field_value = m.get('fieldValue')

        return self

