# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListResponseRuleFieldsResponseBody(DaraModel):
    def __init__(
        self,
        list_response_rule_fields: List[main_models.ListResponseRuleFieldsResponseBodyListResponseRuleFields] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The list of response rule fields.
        self.list_response_rule_fields = list_response_rule_fields
        # The maximum number of entries to return in this request.
        self.max_results = max_results
        # The pagination token for the next query. Valid values: leave this parameter empty for the first query or if no more results exist. If a next query exists, set this parameter to the NextToken value returned by the previous API call.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.list_response_rule_fields:
            for v1 in self.list_response_rule_fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ListResponseRuleFields'] = []
        if self.list_response_rule_fields is not None:
            for k1 in self.list_response_rule_fields:
                result['ListResponseRuleFields'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list_response_rule_fields = []
        if m.get('ListResponseRuleFields') is not None:
            for k1 in m.get('ListResponseRuleFields'):
                temp_model = main_models.ListResponseRuleFieldsResponseBodyListResponseRuleFields()
                self.list_response_rule_fields.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListResponseRuleFieldsResponseBodyListResponseRuleFields(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        field: str = None,
        field_name: str = None,
        field_normalization: str = None,
        right_value: List[main_models.ListResponseRuleFieldsResponseBodyListResponseRuleFieldsRightValue] = None,
        support_operators: List[main_models.ListResponseRuleFieldsResponseBodyListResponseRuleFieldsSupportOperators] = None,
    ):
        # The data type of the automated response rule condition field.
        self.data_type = data_type
        # The whitelisted field.
        self.field = field
        # The name of the rule field.
        self.field_name = field_name
        # The normalization object type to which the field belongs.
        self.field_normalization = field_normalization
        # The list of optional enumeration values for the field. This parameter is not returned if no enumeration values are available.
        self.right_value = right_value
        # The English descriptions of the operators.
        self.support_operators = support_operators

    def validate(self):
        if self.right_value:
            for v1 in self.right_value:
                 if v1:
                    v1.validate()
        if self.support_operators:
            for v1 in self.support_operators:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.field is not None:
            result['Field'] = self.field

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.field_normalization is not None:
            result['FieldNormalization'] = self.field_normalization

        result['RightValue'] = []
        if self.right_value is not None:
            for k1 in self.right_value:
                result['RightValue'].append(k1.to_map() if k1 else None)

        result['SupportOperators'] = []
        if self.support_operators is not None:
            for k1 in self.support_operators:
                result['SupportOperators'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('FieldNormalization') is not None:
            self.field_normalization = m.get('FieldNormalization')

        self.right_value = []
        if m.get('RightValue') is not None:
            for k1 in m.get('RightValue'):
                temp_model = main_models.ListResponseRuleFieldsResponseBodyListResponseRuleFieldsRightValue()
                self.right_value.append(temp_model.from_map(k1))

        self.support_operators = []
        if m.get('SupportOperators') is not None:
            for k1 in m.get('SupportOperators'):
                temp_model = main_models.ListResponseRuleFieldsResponseBodyListResponseRuleFieldsSupportOperators()
                self.support_operators.append(temp_model.from_map(k1))

        return self

class ListResponseRuleFieldsResponseBodyListResponseRuleFieldsSupportOperators(DaraModel):
    def __init__(
        self,
        has_right_value: str = None,
        index: int = None,
        operator: str = None,
        operator_name: str = None,
        support_data_type: str = None,
    ):
        # Indicates whether a right-side value is required. Valid values:
        # - true: Required.
        # - false: Not required.
        self.has_right_value = has_right_value
        # The position of the operator in the operator list.
        self.index = index
        # The aggregation method for the dispatch rule condition. Valid values:
        # 
        # - `=`: equal to
        # - `<>`: not equal to
        # - `in`: contains
        # - `not in`: does not contain
        # - `REGEXP`: matches the regular expression
        # - `NOT REGEXP`: does not match the regular expression
        self.operator = operator
        # The display name of the operator.
        self.operator_name = operator_name
        # The data types supported by the current operator, separated by commas.
        self.support_data_type = support_data_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_right_value is not None:
            result['HasRightValue'] = self.has_right_value

        if self.index is not None:
            result['Index'] = self.index

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name

        if self.support_data_type is not None:
            result['SupportDataType'] = self.support_data_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasRightValue') is not None:
            self.has_right_value = m.get('HasRightValue')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')

        if m.get('SupportDataType') is not None:
            self.support_data_type = m.get('SupportDataType')

        return self

class ListResponseRuleFieldsResponseBodyListResponseRuleFieldsRightValue(DaraModel):
    def __init__(
        self,
        value: str = None,
        value_name: str = None,
    ):
        # The right-side value.
        self.value = value
        # The display name of the enumeration value.
        self.value_name = value_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.value is not None:
            result['Value'] = self.value

        if self.value_name is not None:
            result['ValueName'] = self.value_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('ValueName') is not None:
            self.value_name = m.get('ValueName')

        return self

