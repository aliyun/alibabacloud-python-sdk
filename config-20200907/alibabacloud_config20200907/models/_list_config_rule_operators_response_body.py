# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class ListConfigRuleOperatorsResponseBody(DaraModel):
    def __init__(
        self,
        operators: List[main_models.ListConfigRuleOperatorsResponseBodyOperators] = None,
        request_id: str = None,
    ):
        # A list of operators.
        self.operators = operators
        # The ID of the request.
        self.request_id = request_id

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
        result['Operators'] = []
        if self.operators is not None:
            for k1 in self.operators:
                result['Operators'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operators = []
        if m.get('Operators') is not None:
            for k1 in m.get('Operators'):
                temp_model = main_models.ListConfigRuleOperatorsResponseBodyOperators()
                self.operators.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListConfigRuleOperatorsResponseBodyOperators(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        description: str = None,
        name: str = None,
        operator: str = None,
    ):
        # The data type that the operator applies to.
        self.data_type = data_type
        # The description of the operator, which can be used to explain why a resource is non-compliant.
        self.description = description
        # The name of the operator.
        self.name = name
        # The operator for the rule\\"s input parameter. The available operators vary based on the data type retrieved using SelectPath.
        # 
        # - If the data type is String, valid values are:
        # 
        #   - StringEquals: equals.
        # 
        #   - NotStringEquals: does not equal.
        # 
        #   - StringIn: is in.
        # 
        #   - NotStringIn: is not in.
        # 
        #   - StringContains: contains.
        # 
        #   - NotStringContains: does not contain.
        # 
        # - If the data type is Number, valid values are:
        # 
        #   - Equals: equals.
        # 
        #   - NotEquals: does not equal.
        # 
        #   - Less: is less than.
        # 
        #   - LessOrEquals: is less than or equal to.
        # 
        #   - Greater: is greater than.
        # 
        #   - GreaterOrEquals: is greater than or equal to.
        # 
        # - If the data type is a Base64-encoded string, valid values are:
        # 
        #   - Base64Contains: contains.
        # 
        #   - NotBase64Contains: does not contain.
        # 
        #   - Base64ContainsAll: contains all.
        # 
        #   - Base64ExcludeAll: excludes all.
        # 
        # - If the data type is Array, valid values are:
        # 
        #   - Contains: contains.
        # 
        #   - NotContains: does not contain.
        # 
        #   - In: is in.
        # 
        #   - NotIn: is not in.
        # 
        #   - ContainsAll: contains all.
        # 
        #   - ExcludeAll: excludes all.
        # 
        #   - IsEmpty: is empty.
        self.operator = operator

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.operator is not None:
            result['Operator'] = self.operator

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        return self

