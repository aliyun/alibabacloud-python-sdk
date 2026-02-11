# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class DescribeAutomateResponseConfigFeatureResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.DescribeAutomateResponseConfigFeatureResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeAutomateResponseConfigFeatureResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeAutomateResponseConfigFeatureResponseBodyData(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        feature: str = None,
        right_value_enums: List[main_models.DescribeAutomateResponseConfigFeatureResponseBodyDataRightValueEnums] = None,
        support_operators: List[main_models.DescribeAutomateResponseConfigFeatureResponseBodyDataSupportOperators] = None,
    ):
        # The data type of the condition field in the automated response rule.
        self.data_type = data_type
        # The name of the condition field in the automated response rule.
        self.feature = feature
        # The enumerated values of the right operand for the field.
        self.right_value_enums = right_value_enums
        # The operators that are supported for the condition field.
        self.support_operators = support_operators

    def validate(self):
        if self.right_value_enums:
            for v1 in self.right_value_enums:
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

        if self.feature is not None:
            result['Feature'] = self.feature

        result['RightValueEnums'] = []
        if self.right_value_enums is not None:
            for k1 in self.right_value_enums:
                result['RightValueEnums'].append(k1.to_map() if k1 else None)

        result['SupportOperators'] = []
        if self.support_operators is not None:
            for k1 in self.support_operators:
                result['SupportOperators'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Feature') is not None:
            self.feature = m.get('Feature')

        self.right_value_enums = []
        if m.get('RightValueEnums') is not None:
            for k1 in m.get('RightValueEnums'):
                temp_model = main_models.DescribeAutomateResponseConfigFeatureResponseBodyDataRightValueEnums()
                self.right_value_enums.append(temp_model.from_map(k1))

        self.support_operators = []
        if m.get('SupportOperators') is not None:
            for k1 in m.get('SupportOperators'):
                temp_model = main_models.DescribeAutomateResponseConfigFeatureResponseBodyDataSupportOperators()
                self.support_operators.append(temp_model.from_map(k1))

        return self

class DescribeAutomateResponseConfigFeatureResponseBodyDataSupportOperators(DaraModel):
    def __init__(
        self,
        has_right_value: bool = None,
        index: int = None,
        operator: str = None,
        operator_desc_cn: str = None,
        operator_desc_en: str = None,
        operator_name: str = None,
        support_data_type: str = None,
        support_tag: List[str] = None,
    ):
        # Indicates whether the right operand is required. Valid values:
        # 
        # *   true
        # *   false
        self.has_right_value = has_right_value
        # The position of the operator in the operator list.
        self.index = index
        # The operator.
        self.operator = operator
        # The description of the operator in Chinese.
        self.operator_desc_cn = operator_desc_cn
        # The description of the operator in English.
        self.operator_desc_en = operator_desc_en
        # The name of the operator.
        self.operator_name = operator_name
        # The data types that are supported by the operator. The data types are separated by commas (,).
        self.support_data_type = support_data_type
        # The scenarios that are supported by the operator. Multiple scenarios are separated by commas (,), such as aggregation scenarios. By default, this parameter is empty.
        self.support_tag = support_tag

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

        if self.operator_desc_cn is not None:
            result['OperatorDescCn'] = self.operator_desc_cn

        if self.operator_desc_en is not None:
            result['OperatorDescEn'] = self.operator_desc_en

        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name

        if self.support_data_type is not None:
            result['SupportDataType'] = self.support_data_type

        if self.support_tag is not None:
            result['SupportTag'] = self.support_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasRightValue') is not None:
            self.has_right_value = m.get('HasRightValue')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('OperatorDescCn') is not None:
            self.operator_desc_cn = m.get('OperatorDescCn')

        if m.get('OperatorDescEn') is not None:
            self.operator_desc_en = m.get('OperatorDescEn')

        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')

        if m.get('SupportDataType') is not None:
            self.support_data_type = m.get('SupportDataType')

        if m.get('SupportTag') is not None:
            self.support_tag = m.get('SupportTag')

        return self

class DescribeAutomateResponseConfigFeatureResponseBodyDataRightValueEnums(DaraModel):
    def __init__(
        self,
        value: str = None,
        value_mds: str = None,
    ):
        # The enumerated value of the right operand.
        self.value = value
        # The internal code of the enumerated value.
        self.value_mds = value_mds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.value is not None:
            result['Value'] = self.value

        if self.value_mds is not None:
            result['ValueMds'] = self.value_mds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('ValueMds') is not None:
            self.value_mds = m.get('ValueMds')

        return self

