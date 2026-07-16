# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class MetricsTrigger(DaraModel):
    def __init__(
        self,
        condition_logic_operator: str = None,
        conditions: List[main_models.TriggerCondition] = None,
        cool_down_interval: int = None,
        evaluation_count: int = None,
        time_constraints: List[main_models.TimeConstraint] = None,
        time_window: int = None,
    ):
        # The logical relationship between multiple metrics. Valid values:
        # 
        # *   And
        # *   Or (default)
        self.condition_logic_operator = condition_logic_operator
        # The trigger conditions for the metric.
        self.conditions = conditions
        # The cooldown interval. Unit: seconds. Valid values: 0 to 10800.
        self.cool_down_interval = cool_down_interval
        # The number of times that the statistics are collected. This parameter is required. Valid values: 1 to 5.
        # 
        # This parameter is required.
        self.evaluation_count = evaluation_count
        # The limits on time.
        self.time_constraints = time_constraints
        # The time window for statistics. This parameter is required. Unit: seconds. Valid values: 30 to 1800.
        # 
        # This parameter is required.
        self.time_window = time_window

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()
        if self.time_constraints:
            for v1 in self.time_constraints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition_logic_operator is not None:
            result['ConditionLogicOperator'] = self.condition_logic_operator

        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.cool_down_interval is not None:
            result['CoolDownInterval'] = self.cool_down_interval

        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count

        result['TimeConstraints'] = []
        if self.time_constraints is not None:
            for k1 in self.time_constraints:
                result['TimeConstraints'].append(k1.to_map() if k1 else None)

        if self.time_window is not None:
            result['TimeWindow'] = self.time_window

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionLogicOperator') is not None:
            self.condition_logic_operator = m.get('ConditionLogicOperator')

        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.TriggerCondition()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('CoolDownInterval') is not None:
            self.cool_down_interval = m.get('CoolDownInterval')

        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')

        self.time_constraints = []
        if m.get('TimeConstraints') is not None:
            for k1 in m.get('TimeConstraints'):
                temp_model = main_models.TimeConstraint()
                self.time_constraints.append(temp_model.from_map(k1))

        if m.get('TimeWindow') is not None:
            self.time_window = m.get('TimeWindow')

        return self

