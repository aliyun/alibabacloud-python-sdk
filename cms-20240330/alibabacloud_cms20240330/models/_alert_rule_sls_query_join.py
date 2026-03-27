# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class AlertRuleSlsQueryJoin(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.AlertRuleSlsQueryJoinConditions] = None,
        type: str = None,
    ):
        # List of connection conditions.
        self.conditions = conditions
        # Set operation type.
        # CrossJoin: Cartesian product
        # FullJoin: Full outer join
        # InnerJoin: Inner join
        # LeftExclude: Left anti join
        # RightExclude: Right anti join
        # LeftJoin: Left outer join
        # RightJoin: Right outer join
        # NoJoin: No merge
        # Concat: Concatenation
        # 
        # See also: https://help.aliyun.com/zh/sls/user-guide/set-query-statistics-statement
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['conditions'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('conditions') is not None:
            for k1 in m.get('conditions'):
                temp_model = main_models.AlertRuleSlsQueryJoinConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class AlertRuleSlsQueryJoinConditions(DaraModel):
    def __init__(
        self,
        first_field: str = None,
        oper: str = None,
        second_field: str = None,
    ):
        # Left-hand operand of the condition, formatted as $<query_idx>.<result_set_field_name>.
        self.first_field = first_field
        # Comparison operator; valid values: <, >, ==, !=, <=, >=.
        self.oper = oper
        # Right-hand operand of the condition, formatted as $<query_idx>.<result_set_field_name>.
        self.second_field = second_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.first_field is not None:
            result['firstField'] = self.first_field

        if self.oper is not None:
            result['oper'] = self.oper

        if self.second_field is not None:
            result['secondField'] = self.second_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('firstField') is not None:
            self.first_field = m.get('firstField')

        if m.get('oper') is not None:
            self.oper = m.get('oper')

        if m.get('secondField') is not None:
            self.second_field = m.get('secondField')

        return self

