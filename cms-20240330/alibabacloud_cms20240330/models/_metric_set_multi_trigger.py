# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class MetricSetMultiTrigger(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.MetricSetTriggerSimpleExpression] = None,
        duration_secs: int = None,
        expression_type: str = None,
        logic_operator: str = None,
        max: float = None,
        min: float = None,
        operator: str = None,
        query_name: str = None,
        severity: str = None,
        threshold: float = None,
    ):
        self.conditions = conditions
        self.duration_secs = duration_secs
        self.expression_type = expression_type
        self.logic_operator = logic_operator
        self.max = max
        self.min = min
        self.operator = operator
        self.query_name = query_name
        self.severity = severity
        self.threshold = threshold

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

        if self.duration_secs is not None:
            result['durationSecs'] = self.duration_secs

        if self.expression_type is not None:
            result['expressionType'] = self.expression_type

        if self.logic_operator is not None:
            result['logicOperator'] = self.logic_operator

        if self.max is not None:
            result['max'] = self.max

        if self.min is not None:
            result['min'] = self.min

        if self.operator is not None:
            result['operator'] = self.operator

        if self.query_name is not None:
            result['queryName'] = self.query_name

        if self.severity is not None:
            result['severity'] = self.severity

        if self.threshold is not None:
            result['threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('conditions') is not None:
            for k1 in m.get('conditions'):
                temp_model = main_models.MetricSetTriggerSimpleExpression()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('durationSecs') is not None:
            self.duration_secs = m.get('durationSecs')

        if m.get('expressionType') is not None:
            self.expression_type = m.get('expressionType')

        if m.get('logicOperator') is not None:
            self.logic_operator = m.get('logicOperator')

        if m.get('max') is not None:
            self.max = m.get('max')

        if m.get('min') is not None:
            self.min = m.get('min')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('queryName') is not None:
            self.query_name = m.get('queryName')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        return self

