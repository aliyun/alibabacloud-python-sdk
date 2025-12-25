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
        self.conditions = conditions
        # 集合操作类型。
        #   ● CrossJoin： 笛卡尔积
        #   ● FullJoin：全联
        #   ● InnerJoin：内联
        #   ● LeftExclude： 左斥
        #   ● RightExclude：右斥
        #   ● LeftJoin：左联
        #   ● RightJoin：右联
        #   ● NoJoin：不合并
        #   ● Concat： 拼接
        #   https://help.aliyun.com/zh/sls/user-guide/set-query-statistics-statement
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
        # 条件的左操作参数，格式为$<query_idx>.<结果集字段名>
        self.first_field = first_field
        # <, >, ==, !=, <=, >=
        self.oper = oper
        # 条件的右操作参数，格式为$<query_idx>.<结果集字段名>
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

