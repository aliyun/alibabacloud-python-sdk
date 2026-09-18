# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class PrometheusMultiTrigger(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.PrometheusSimpleExpression] = None,
        duration_secs: int = None,
        expression_type: str = None,
        logic_operator: str = None,
        operator: str = None,
        query_name: str = None,
        severity: str = None,
        threshold: float = None,
    ):
        # The list of sub-conditions. This parameter is used when expressionType is set to COMPOSITE. Each item contains queryName, operator, and threshold.
        self.conditions = conditions
        # The duration, in seconds, for which the data must continuously meet the condition before the alert is triggered. If this parameter is not specified, the value of conditionConfig.durationSecs is inherited.
        self.duration_secs = duration_secs
        # The expression type. Valid values:
        # - SIMPLE: single-query threshold.
        # - COMPOSITE: multi-query AND/OR/UNLESS combination.
        self.expression_type = expression_type
        # The logical operator. This parameter is used when expressionType is set to COMPOSITE. Valid values: AND, OR, and UNLESS.
        self.logic_operator = logic_operator
        # The comparison operator. This parameter is used when expressionType is set to SIMPLE. Valid values: GT, GE, LT, LE, EQ, and NE.
        self.operator = operator
        # The referenced query name. This parameter is used when expressionType is set to SIMPLE. The value corresponds to QueryConfigUnified.queries[].name.
        self.query_name = query_name
        # The alert severity level. The priority order is CRITICAL > ERROR > WARN / WARNING > INFO. When multiple triggers are defined, they are sorted by this priority, and the first match fires the alert.
        self.severity = severity
        # The comparison threshold. This parameter is used when expressionType is set to SIMPLE.
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
                temp_model = main_models.PrometheusSimpleExpression()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('durationSecs') is not None:
            self.duration_secs = m.get('durationSecs')

        if m.get('expressionType') is not None:
            self.expression_type = m.get('expressionType')

        if m.get('logicOperator') is not None:
            self.logic_operator = m.get('logicOperator')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('queryName') is not None:
            self.query_name = m.get('queryName')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        return self

