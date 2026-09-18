# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class MetricSetMultiTrigger(DaraModel):
    def __init__(
        self,
        abs_deviation: float = None,
        baseline_period: str = None,
        conditions: List[main_models.MetricSetTriggerSimpleExpression] = None,
        duration_secs: int = None,
        expression_type: str = None,
        logic_operator: str = None,
        max: float = None,
        min: float = None,
        operator: str = None,
        query_name: str = None,
        sensitivity: str = None,
        severity: str = None,
        threshold: float = None,
    ):
        # The dynamic baseline minimum deviation or absolute deviation dead zone. Effective only for baseline operators. The unit is the same as the metric. The value must be greater than or equal to 0. A value of 0 means no restriction.
        self.abs_deviation = abs_deviation
        # The baseline period. Effective only for baseline operators. Valid values: AUTO (automatic detection), DAILY (daily), WEEKLY (weekly), and NONE (no period). When set to WEEKLY, the backend automatically expands the historical training window to at least 14 days.
        self.baseline_period = baseline_period
        # The list of sub-conditions. Used when expressionType is COMPOSITE. Each item contains queryName, operator, and threshold.
        self.conditions = conditions
        # The duration in seconds that data must continuously meet the condition before an alert is triggered. If not specified, the value is inherited from conditionConfig.durationSecs.
        self.duration_secs = duration_secs
        # The expression type. Valid values: SIMPLE (single-metric threshold) and COMPOSITE (multi-metric AND/OR/UNLESS combination).
        self.expression_type = expression_type
        # The logical operator. Used when expressionType is COMPOSITE. Valid values: AND (all conditions met), OR (any condition met), and UNLESS (first condition met and all others not met).
        self.logic_operator = logic_operator
        # The upper bound of the range. Required when expressionType is SIMPLE and operator is IN_RANGE/OUT_OF_RANGE. The value must be greater than or equal to min.
        self.max = max
        # The lower bound of the range. Required when expressionType is SIMPLE and operator is IN_RANGE/OUT_OF_RANGE.
        self.min = min
        # The comparison operator (used when expressionType is SIMPLE). Valid values: GT (greater than), GE (greater than or equal to), LT (less than), LE (less than or equal to), EQ (equal to), NE (not equal to), IN_RANGE (within range, requires min/max), OUT_OF_RANGE (outside range, requires min/max), PRESENT (field exists, no threshold/min/max required), NOT_PRESENT (field does not exist, no threshold/min/max required), ABOVE_UPPER/BELOW_LOWER/OUT_OF_BAND (dynamic baseline spike/drop/bidirectional, requires sensitivity, no threshold/min/max).
        self.operator = operator
        # The referenced query name (used when expressionType is SIMPLE), corresponding to QueryConfigUnified.queries[].name.
        self.query_name = query_name
        # The dynamic baseline sensitivity. Effective when expressionType is SIMPLE and a baseline operator is used. Valid values: HIGH (narrowest band, most sensitive), MEDIUM, and LOW (widest band, least sensitive).
        self.sensitivity = sensitivity
        # The alert severity level: CRITICAL > ERROR > WARN / WARNING > INFO. Multiple triggers are sorted by this priority, and the first match fires.
        self.severity = severity
        # The comparison threshold. Used when expressionType is SIMPLE and operator is GT/GE/LT/LE/EQ/NE. For IN_RANGE/OUT_OF_RANGE, use min/max instead. Not required for PRESENT/NOT_PRESENT.
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
        if self.abs_deviation is not None:
            result['absDeviation'] = self.abs_deviation

        if self.baseline_period is not None:
            result['baselinePeriod'] = self.baseline_period

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

        if self.sensitivity is not None:
            result['sensitivity'] = self.sensitivity

        if self.severity is not None:
            result['severity'] = self.severity

        if self.threshold is not None:
            result['threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('absDeviation') is not None:
            self.abs_deviation = m.get('absDeviation')

        if m.get('baselinePeriod') is not None:
            self.baseline_period = m.get('baselinePeriod')

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

        if m.get('sensitivity') is not None:
            self.sensitivity = m.get('sensitivity')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        return self

