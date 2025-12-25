# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class JudgeNodeMetaDesc(DaraModel):
    def __init__(
        self,
        actual_value: str = None,
        data_type: int = None,
        expression_meta_desc: main_models.JudgeNodeMetaDescExpressionMetaDesc = None,
        field: str = None,
        field_type: int = None,
        symbol: int = None,
        value: str = None,
    ):
        self.actual_value = actual_value
        self.data_type = data_type
        self.expression_meta_desc = expression_meta_desc
        self.field = field
        self.field_type = field_type
        self.symbol = symbol
        self.value = value

    def validate(self):
        if self.expression_meta_desc:
            self.expression_meta_desc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_value is not None:
            result['ActualValue'] = self.actual_value

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.expression_meta_desc is not None:
            result['ExpressionMetaDesc'] = self.expression_meta_desc.to_map()

        if self.field is not None:
            result['Field'] = self.field

        if self.field_type is not None:
            result['FieldType'] = self.field_type

        if self.symbol is not None:
            result['Symbol'] = self.symbol

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualValue') is not None:
            self.actual_value = m.get('ActualValue')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('ExpressionMetaDesc') is not None:
            temp_model = main_models.JudgeNodeMetaDescExpressionMetaDesc()
            self.expression_meta_desc = temp_model.from_map(m.get('ExpressionMetaDesc'))

        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('FieldType') is not None:
            self.field_type = m.get('FieldType')

        if m.get('Symbol') is not None:
            self.symbol = m.get('Symbol')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class JudgeNodeMetaDescExpressionMetaDesc(DaraModel):
    def __init__(
        self,
        left_field_type: int = None,
        left_operand: str = None,
        operator: str = None,
        right_field_type: int = None,
        right_operand: str = None,
        rounding_mode: str = None,
    ):
        self.left_field_type = left_field_type
        self.left_operand = left_operand
        self.operator = operator
        self.right_field_type = right_field_type
        self.right_operand = right_operand
        self.rounding_mode = rounding_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.left_field_type is not None:
            result['LeftFieldType'] = self.left_field_type

        if self.left_operand is not None:
            result['LeftOperand'] = self.left_operand

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.right_field_type is not None:
            result['RightFieldType'] = self.right_field_type

        if self.right_operand is not None:
            result['RightOperand'] = self.right_operand

        if self.rounding_mode is not None:
            result['RoundingMode'] = self.rounding_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LeftFieldType') is not None:
            self.left_field_type = m.get('LeftFieldType')

        if m.get('LeftOperand') is not None:
            self.left_operand = m.get('LeftOperand')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('RightFieldType') is not None:
            self.right_field_type = m.get('RightFieldType')

        if m.get('RightOperand') is not None:
            self.right_operand = m.get('RightOperand')

        if m.get('RoundingMode') is not None:
            self.rounding_mode = m.get('RoundingMode')

        return self

