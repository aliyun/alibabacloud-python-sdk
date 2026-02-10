# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListCloudAssetMatchOperatorsResponseBody(DaraModel):
    def __init__(
        self,
        match_type_operators: List[main_models.ListCloudAssetMatchOperatorsResponseBodyMatchTypeOperators] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # List of operator types
        self.match_type_operators = match_type_operators
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.match_type_operators:
            for v1 in self.match_type_operators:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MatchTypeOperators'] = []
        if self.match_type_operators is not None:
            for k1 in self.match_type_operators:
                result['MatchTypeOperators'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.match_type_operators = []
        if m.get('MatchTypeOperators') is not None:
            for k1 in m.get('MatchTypeOperators'):
                temp_model = main_models.ListCloudAssetMatchOperatorsResponseBodyMatchTypeOperators()
                self.match_type_operators.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListCloudAssetMatchOperatorsResponseBodyMatchTypeOperators(DaraModel):
    def __init__(
        self,
        match_operators: List[main_models.ListCloudAssetMatchOperatorsResponseBodyMatchTypeOperatorsMatchOperators] = None,
        type: str = None,
    ):
        # List of operators
        self.match_operators = match_operators
        # The type used by the operator. Values:
        # - LIST 
        # - MAP 
        # - STRING 
        # - BOOLEAN 
        # - FLOAT 
        # - DOUBLE 
        # - INTEGER 
        # - LONG
        self.type = type

    def validate(self):
        if self.match_operators:
            for v1 in self.match_operators:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MatchOperators'] = []
        if self.match_operators is not None:
            for k1 in self.match_operators:
                result['MatchOperators'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.match_operators = []
        if m.get('MatchOperators') is not None:
            for k1 in m.get('MatchOperators'):
                temp_model = main_models.ListCloudAssetMatchOperatorsResponseBodyMatchTypeOperatorsMatchOperators()
                self.match_operators.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListCloudAssetMatchOperatorsResponseBodyMatchTypeOperatorsMatchOperators(DaraModel):
    def __init__(
        self,
        input_pattern: str = None,
        name: str = None,
        show_name: str = None,
        value: str = None,
    ):
        # Operation data types. Values: 
        # - LIST type: 
        # 1. For Name as LIST_CONTAINS, the value is: LIST 
        # 2. For Name as LIST_LENGTH_GT, the value is: PRIMITIVE 
        # 3. For Name as LIST_LENGTH_LT, the value is: PRIMITIVE 
        # 4. For Name as LIST_NOT_CONTAINS, the value is: LIST
        # - STRING type: 
        # 1. For Name as STRING_NOT_IN, the value is: LIST 
        # 2. For Name as STRING_EQ, the value is: PRIMITIVE 
        # 3. For Name as STRING_IN, the value is: LIST 
        # 4. For Name as STRING_NOT_EQ, the value is: PRIMITIVE
        # - BOOLEAN type: 
        # 1. For Name as BOOLEAN_NOT_IN, the value is: LIST 
        # 2. For Name as BOOLEAN_EQ, the value is: PRIMITIVE 
        # 3. For Name as BOOLEAN_IN, the value is: LIST 
        # 4. For Name as BOOLEAN_NOT_EQ, the value is: PRIMITIVE
        # - FLOAT type: 
        # 1. For Name as FLOAT_NOT_IN, the value is: LIST 
        # 2. For Name as FLOAT_EQ, the value is: PRIMITIVE 
        # 3. For Name as FLOAT_IN, the value is: LIST 
        # 4. For Name as FLOAT_NOT_EQ, the value is: PRIMITIVE 
        # 5. For Name as FLOAT_GT, the value is: PRIMITIVE 
        # 6. For Name as FLOAT_GTE, the value is: PRIMITIVE 
        # 7. For Name as FLOAT_LT, the value is: PRIMITIVE 
        # 8. For Name as FLOAT_LTE, the value is: PRIMITIVE
        # - DOUBLE type: 
        # 1. For Name as DOUBLE_NOT_IN, the value is: LIST 
        # 2. For Name as DOUBLE_EQ, the value is: PRIMITIVE 
        # 3. For Name as DOUBLE_IN, the value is: LIST 
        # 4. For Name as DOUBLE_NOT_EQ, the value is: PRIMITIVE 
        # 5. For Name as DOUBLE_GT, the value is: PRIMITIVE 
        # 6. For Name as DOUBLE_GTE, the value is: PRIMITIVE 
        # 7. For Name as DOUBLE_LT, the value is: PRIMITIVE 8. For Name as DOUBLE_LTE, the value is: PRIMITIVE
        # - INTEGER type: 
        # 1. For Name as INTEGER_NOT_IN, the value is: LIST 
        # 2. For Name as INTEGER_EQ, the value is: PRIMITIVE 
        # 3. For Name as INTEGER_IN, the value is: LIST 
        # 4. For Name as INTEGER_NOT_EQ, the value is: PRIMITIVE 
        # 5. For Name as INTEGER_GT, the value is: PRIMITIVE 
        # 6. For Name as INTEGER_GTE, the value is: PRIMITIVE 
        # 7. For Name as INTEGER_LT, the value is: PRIMITIVE 
        # 8. For Name as INTEGER_LTE, the value is: PRIMITIVE
        # - LONG type: 
        # 1. For Name as LONG_NOT_IN, the value is: LIST 
        # 2. For Name as LONG_EQ, the value is: PRIMITIVE 
        # 3. For Name as LONG_IN, the value is: LIST 
        # 4. For Name as LONG_NOT_EQ, the value is: PRIMITIVE 
        # 5. For Name as LONG_GT, the value is: PRIMITIVE 
        # 6. For Name as LONG_GTE, the value is: PRIMITIVE 
        # 7. For Name as LONG_LT, the value is: PRIMITIVE 
        # 8. For Name as LONG_LTE, the value is: PRIMITIVE
        # - INTEGER type (repeated): 
        # 1. For Name as INTEGER_NOT_IN, the value is: LIST 
        # 2. For Name as INTEGER_EQ, the value is: PRIMITIVE 
        # 3. For Name as INTEGER_IN, the value is: LIST 
        # 4. For Name as INTEGER_NOT_EQ, the value is: PRIMITIVE 
        # 5. For Name as INTEGER_GT, the value is: PRIMITIVE 
        # 6. For Name as INTEGER_GTE, the value is: PRIMITIVE 
        # 7. For Name as INTEGER_LT, the value is: PRIMITIVE 
        # 8. For Name as INTEGER_LTE, the value is: PRIMITIVE
        self.input_pattern = input_pattern
        # Unique name of the operator. Values: - LIST type: 
        # 1. LIST_CONTAINS: contains 
        # 2. LIST_LENGTH_GT: length greater than 
        # 3. LIST_LENGTH_LT: length less than 
        # 4. LIST_NOT_CONTAINS: does not contain
        # - STRING type: 
        # 1. STRING_NOT_IN: not in list 
        # 2. STRING_EQ: equals 
        # 3. STRING_IN: in list 
        # 4. STRING_NOT_EQ: not equal
        # - BOOLEAN type: 
        # 1. BOOLEAN_NOT_IN: not in list 
        # 2. BOOLEAN_EQ: equals 
        # 3. BOOLEAN_IN: in list 
        # 4. BOOLEAN_NOT_EQ: not equal
        # - FLOAT type: 1. FLOAT_NOT_IN: not in list 
        # 2. FLOAT_EQ: equals 3. FLOAT_IN: in list 
        # 4. FLOAT_NOT_EQ: not equal 
        # 5. FLOAT_GT: greater than 
        # 6. FLOAT_GTE: greater than or equal to 
        # 7. FLOAT_LT: less than 
        # 8. FLOAT_LTE: less than or equal to
        # - DOUBLE type: 
        # 1. DOUBLE_NOT_IN: not in list 
        # 2. DOUBLE_EQ: equals 
        # 3. DOUBLE_IN: in list 
        # 4. DOUBLE_NOT_EQ: not equal 
        # 5. DOUBLE_GT: greater than 
        # 6. DOUBLE_GTE: greater than or equal to 7
        # . DOUBLE_LT: less than 
        # 8. DOUBLE_LTE: less than or equal to
        # - INTEGER type: 
        # 1. INTEGER_NOT_IN: not in list 
        # 2. INTEGER_EQ: equals 
        # 3. INTEGER_IN: in list 
        # 4. INTEGER_NOT_EQ: not equal 
        # 5. INTEGER_GT: greater than 
        # 6. INTEGER_GTE: greater than or equal to 
        # 7. INTEGER_LT: less than 
        # 8. INTEGER_LTE: less than or equal to
        # - LONG type: 
        # 1. LONG_NOT_IN: not in list 
        # 2. LONG_EQ: equals 
        # 3. LONG_IN: in list 
        # 4. LONG_NOT_EQ: not equal 
        # 5. LONG_GT: greater than 
        # 6. LONG_GTE: greater than or equal to 
        # 7. LONG_LT: less than 
        # 8. LONG_LTE: less than or equal to<details>
        self.name = name
        # Operator display name. Values: - For LIST type: 
        # 1. Contains: includes 
        # 2. SizeGreaterThan: size greater than 
        # 3. SizeLessThan: size less than 
        # 4. NotContains: does not include
        # - For STRING type: 
        # 1. NotIn: not in the list 
        # 2. Equals: equals 
        # 3. In: in the list 
        # 4. NotEquals: does not equal
        # - For BOOLEAN type: 
        # 1. NotIn: not in the list 
        # 2. Equals: equals 
        # 3. In: in the list 
        # 4. NotEquals: does not equal
        # - For FLOAT type: 
        # 1. NotIn: not in the list 
        # 2. Equals: equals 
        # 3. In: in the list 
        # 4. NotEquals: does not equal 
        # 5. >: greater than 
        # 6. >=: greater than or equal to 
        # 7. <: less than 
        # 8. <=: less than or equal to
        # - For DOUBLE type: 
        # 1. NotIn: not in the list 
        # 2. Equals: equals 
        # 3. In: in the list 
        # 4. NotEquals: does not equal 
        # 5. >: greater than 
        # 6. >=: greater than or equal to 
        # 7. <: less than 
        # 8. <=: less than or equal to (Note: There seems to be a repetition here, likely meant to be \\"<=\\" for \\"less than or equal to\\")
        # - For INTEGER type: 
        # 1. NotIn: not in the list 
        # 2. Equals: equals 
        # 3. In: in the list 
        # 4. NotEquals: does not equal 
        # 5. >: greater than 
        # 6. >=: greater than or equal to 
        # 7. <: less than 
        # 8. <=: less than or equal to
        # - For LONG type: 
        # 1. NotIn: not in the list 
        # 2. Equals: equals 
        # 3. In: in the list 
        # 4. NotEquals: does not equal 
        # 5. >: greater than 
        # 6. >=: greater than or equal to 
        # 7. <: less than 
        # 8. <=: less than or equal to
        # - For INTEGER type (repeated): 
        # 1. NotIn: not in the list 
        # 2. Equals: equals 
        # 3. In: in the list 
        # 4. NotEquals: does not equal 
        # 5. >: greater than 
        # 6. >=: greater than or equal to 
        # 7. <: less than 
        # 8. <=: less than or equal to
        self.show_name = show_name
        # Operator value. Options: - For LIST type: 
        # 1. CONTAINS: contains 
        # 2. LENGTH_GT: length greater than 
        # 3. LENGTH_LT: length less than 
        # 4. NOT_CONTAINS: does not contain
        # - For STRING type: 
        # 1. NOT_IN: not in the list 
        # 2. EQ: equals 
        # 3. IN: in the list 
        # 4. NOT_EQ: does not equal
        # - For BOOLEAN type: 
        # 1. NOT_IN: not in the list 
        # 2. EQ: equals 
        # 3. IN: in the list 
        # 4. NOT_EQ: does not equal
        # - For FLOAT type: 
        # 1. NOT_IN: not in the list 
        # 2. EQ: equals 
        # 3. IN: in the list 
        # 4. NOT_EQ: does not equal 
        # 5. GT: greater than 
        # 6. GTE: greater than or equal to 
        # 7. LT: less than 
        # 8. LTE: less than or equal to
        # - For DOUBLE type: 
        # 1. NOT_IN: not in the list 
        # 2. EQ: equals 
        # 3. IN: in the list 
        # 4. NOT_EQ: does not equal 
        # 5. GT: greater than 
        # 6. GTE: greater than or equal to 
        # 7. LT: less than 
        # 8. LTE: less than or equal to
        # - For INTEGER type: 
        # 1. NOT_IN: not in the list 
        # 2. EQ: equals 
        # 3. IN: in the list 
        # 4. NOT_EQ: does not equal 
        # 5. GT: greater than 
        # 6. GTE: greater than or equal to 
        # 7. LT: less than 
        # 8. LTE: less than or equal to
        # - For LONG type: 
        # 1. NOT_IN: not in the list 
        # 2. EQ: equals 
        # 3. IN: in the list 
        # 4. NOT_EQ: does not equal 
        # 5. GT: greater than 
        # 6. GTE: greater than or equal to 
        # 7. LT: less than 
        # 8. LTE: less than or equal to
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_pattern is not None:
            result['InputPattern'] = self.input_pattern

        if self.name is not None:
            result['Name'] = self.name

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputPattern') is not None:
            self.input_pattern = m.get('InputPattern')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

