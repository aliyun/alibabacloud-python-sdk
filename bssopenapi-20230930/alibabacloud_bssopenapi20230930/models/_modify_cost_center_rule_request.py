# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class ModifyCostCenterRuleRequest(DaraModel):
    def __init__(
        self,
        cost_center_id: int = None,
        filter_expression: main_models.ModifyCostCenterRuleRequestFilterExpression = None,
        nbid: str = None,
        owner_account_id: int = None,
    ):
        self.cost_center_id = cost_center_id
        self.filter_expression = filter_expression
        self.nbid = nbid
        self.owner_account_id = owner_account_id

    def validate(self):
        if self.filter_expression:
            self.filter_expression.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id

        if self.filter_expression is not None:
            result['FilterExpression'] = self.filter_expression.to_map()

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')

        if m.get('FilterExpression') is not None:
            temp_model = main_models.ModifyCostCenterRuleRequestFilterExpression()
            self.filter_expression = temp_model.from_map(m.get('FilterExpression'))

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')

        return self

class ModifyCostCenterRuleRequestFilterExpression(DaraModel):
    def __init__(
        self,
        expression_type: str = None,
        filter_values: main_models.ModifyCostCenterRuleRequestFilterExpressionFilterValues = None,
        operand: Any = None,
        operands: List[Any] = None,
        operator_type: str = None,
    ):
        self.expression_type = expression_type
        self.filter_values = filter_values
        self.operand = operand
        self.operands = operands
        self.operator_type = operator_type

    def validate(self):
        if self.filter_values:
            self.filter_values.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression_type is not None:
            result['ExpressionType'] = self.expression_type

        if self.filter_values is not None:
            result['FilterValues'] = self.filter_values.to_map()

        if self.operand is not None:
            result['Operand'] = self.operand

        if self.operands is not None:
            result['Operands'] = self.operands

        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpressionType') is not None:
            self.expression_type = m.get('ExpressionType')

        if m.get('FilterValues') is not None:
            temp_model = main_models.ModifyCostCenterRuleRequestFilterExpressionFilterValues()
            self.filter_values = temp_model.from_map(m.get('FilterValues'))

        if m.get('Operand') is not None:
            self.operand = m.get('Operand')

        if m.get('Operands') is not None:
            self.operands = m.get('Operands')

        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')

        return self

class ModifyCostCenterRuleRequestFilterExpressionFilterValues(DaraModel):
    def __init__(
        self,
        code: str = None,
        code_name: str = None,
        select_type: str = None,
        values: List[str] = None,
    ):
        self.code = code
        self.code_name = code_name
        self.select_type = select_type
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.code_name is not None:
            result['CodeName'] = self.code_name

        if self.select_type is not None:
            result['SelectType'] = self.select_type

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CodeName') is not None:
            self.code_name = m.get('CodeName')

        if m.get('SelectType') is not None:
            self.select_type = m.get('SelectType')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

