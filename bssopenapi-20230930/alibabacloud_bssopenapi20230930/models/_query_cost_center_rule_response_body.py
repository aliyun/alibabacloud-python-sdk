# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class QueryCostCenterRuleResponseBody(DaraModel):
    def __init__(
        self,
        cost_center_id: int = None,
        filter_expression: main_models.QueryCostCenterRuleResponseBodyFilterExpression = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        is_deleted: int = None,
        metadata: Any = None,
        owner_account_id: int = None,
        request_id: str = None,
        root_cost_center_id: int = None,
        status: str = None,
    ):
        self.cost_center_id = cost_center_id
        self.filter_expression = filter_expression
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.is_deleted = is_deleted
        self.metadata = metadata
        self.owner_account_id = owner_account_id
        # Id of the request
        self.request_id = request_id
        self.root_cost_center_id = root_cost_center_id
        self.status = status

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

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_cost_center_id is not None:
            result['RootCostCenterId'] = self.root_cost_center_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')

        if m.get('FilterExpression') is not None:
            temp_model = main_models.QueryCostCenterRuleResponseBodyFilterExpression()
            self.filter_expression = temp_model.from_map(m.get('FilterExpression'))

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootCostCenterId') is not None:
            self.root_cost_center_id = m.get('RootCostCenterId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class QueryCostCenterRuleResponseBodyFilterExpression(DaraModel):
    def __init__(
        self,
        expression_type: str = None,
        filter_values: main_models.QueryCostCenterRuleResponseBodyFilterExpressionFilterValues = None,
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
            temp_model = main_models.QueryCostCenterRuleResponseBodyFilterExpressionFilterValues()
            self.filter_values = temp_model.from_map(m.get('FilterValues'))

        if m.get('Operand') is not None:
            self.operand = m.get('Operand')

        if m.get('Operands') is not None:
            self.operands = m.get('Operands')

        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')

        return self

class QueryCostCenterRuleResponseBodyFilterExpressionFilterValues(DaraModel):
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

