# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class Triggers(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        condition: str = None,
        conditions: List[main_models.TriggerConditions] = None,
        count_condition: str = None,
        count_operator: str = None,
        count_threshold: int = None,
        duration_secs: int = None,
        expression_type: str = None,
        logic_operator: str = None,
        match_field: str = None,
        match_operator: str = None,
        match_value: str = None,
        max: float = None,
        metric_name: str = None,
        min: float = None,
        operator: str = None,
        period: int = None,
        pre_condition: str = None,
        query_name: str = None,
        severity: str = None,
        statistics: str = None,
        threshold: Any = None,
        times: int = None,
    ):
        # The comparison operator when the condition type is CLOUD_MONITORING_CONDITION.
        self.comparison_operator = comparison_operator
        # The match expression when the condition type is SLS_MULTI_CONDITION. This corresponds to the V1 condition and is preserved as-is without parsing.
        self.condition = condition
        # The list of sub-conditions when the condition type is UMODEL_METRICSET_MULTI or PROMETHEUS_MULTI with expressionType=COMPOSITE. Each item contains queryName, operator, and threshold.
        self.conditions = conditions
        # The count match expression when the condition type is SLS_MULTI_CONDITION. This corresponds to the V1 countCondition and is preserved as-is without parsing.
        self.count_condition = count_condition
        # **[Deprecated]** The write path for SLS_MULTI_CONDITION has been disabled. Use countCondition instead.
        self.count_operator = count_operator
        # **[Deprecated]** The write path for SLS_MULTI_CONDITION has been disabled. Use countCondition instead.
        self.count_threshold = count_threshold
        # The duration in seconds during which data must continuously meet the condition before an alert is triggered. If not specified, the value is inherited from conditionConfig.durationSecs. This parameter is used by UMODEL_METRICSET_MULTI_CONDITION and PROMETHEUS_MULTI_CONDITION.
        self.duration_secs = duration_secs
        # The expression type. Set to SIMPLE or COMPOSITE when the condition type is UMODEL_METRICSET_MULTI_CONDITION or PROMETHEUS_MULTI_CONDITION.
        self.expression_type = expression_type
        # The logical operator when the condition type is UMODEL_METRICSET_MULTI or PROMETHEUS_MULTI with expressionType=COMPOSITE. Valid values: AND, OR, and UNLESS.
        self.logic_operator = logic_operator
        # **[Deprecated]** The write path for SLS_MULTI_CONDITION has been disabled. Use condition instead.
        self.match_field = match_field
        # **[Deprecated]** The write path for SLS_MULTI_CONDITION has been disabled. Use condition instead.
        self.match_operator = match_operator
        # **[Deprecated]** The write path for SLS_MULTI_CONDITION has been disabled. Use condition instead.
        self.match_value = match_value
        # The upper bound of the range when the condition type is UMODEL_METRICSET_MULTI with expressionType=SIMPLE. This parameter is required when operator is set to IN_RANGE or OUT_OF_RANGE. The value must be greater than or equal to min.
        self.max = max
        # The metric name when the condition type is CLOUD_MONITORING_CONDITION with expressionType=COMPOSITE. For SIMPLE expression type, the metric name is specified at the conditionConfig level by the metricName parameter.
        self.metric_name = metric_name
        # The lower bound of the range when the condition type is UMODEL_METRICSET_MULTI with expressionType=SIMPLE. This parameter is required when operator is set to IN_RANGE or OUT_OF_RANGE.
        self.min = min
        # The operator. For UMODEL_METRICSET_MULTI or PROMETHEUS_MULTI with expressionType=SIMPLE, this is a comparison operator (GT/GE/LT/LE/EQ/NE/IN_RANGE/OUT_OF_RANGE/PRESENT/NOT_PRESENT/ABOVE_UPPER/BELOW_LOWER/OUT_OF_BAND). For SLS_MULTI_CONDITION, this is aligned with the V1 caseList.type (HAS_DATA/HAS_DATA_COUNT/HAS_DATA_MATCH/HAS_DATA_MATCH_COUNT).
        self.operator = operator
        # The collection period in seconds when the condition type is CLOUD_MONITORING_CONDITION with expressionType=COMPOSITE. For SIMPLE expression type, the period is specified at the conditionConfig level by the period parameter.
        self.period = period
        # The precondition when the condition type is CLOUD_MONITORING_CONDITION.
        self.pre_condition = pre_condition
        # The referenced query name when the condition type is UMODEL_METRICSET_MULTI or PROMETHEUS_MULTI with expressionType=SIMPLE. This corresponds to QueryConfigUnified.queries[].name.
        self.query_name = query_name
        # The severity level. The priority order is CRITICAL > ERROR > WARN / WARNING > INFO. When multiple triggers exist, they are sorted by this priority, and the first match triggers the alert. This parameter takes effect when the condition type is SLS_MULTI_CONDITION or CLOUD_MONITORING_CONDITION with expressionType=SIMPLE.
        self.severity = severity
        # The statistical method when the condition type is CLOUD_MONITORING_CONDITION.
        self.statistics = statistics
        # The threshold value. For CLOUD_MONITORING_CONDITION, this is a string. For UMODEL_METRICSET_MULTI and PROMETHEUS_MULTI, this is a numeric value.
        self.threshold = threshold
        # The number of consecutive times the condition must be met before an alert is triggered when the condition type is CLOUD_MONITORING_CONDITION with expressionType=SIMPLE. Each entry has its own independent setting.
        self.times = times

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
        if self.comparison_operator is not None:
            result['comparisonOperator'] = self.comparison_operator

        if self.condition is not None:
            result['condition'] = self.condition

        result['conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['conditions'].append(k1.to_map() if k1 else None)

        if self.count_condition is not None:
            result['countCondition'] = self.count_condition

        if self.count_operator is not None:
            result['countOperator'] = self.count_operator

        if self.count_threshold is not None:
            result['countThreshold'] = self.count_threshold

        if self.duration_secs is not None:
            result['durationSecs'] = self.duration_secs

        if self.expression_type is not None:
            result['expressionType'] = self.expression_type

        if self.logic_operator is not None:
            result['logicOperator'] = self.logic_operator

        if self.match_field is not None:
            result['matchField'] = self.match_field

        if self.match_operator is not None:
            result['matchOperator'] = self.match_operator

        if self.match_value is not None:
            result['matchValue'] = self.match_value

        if self.max is not None:
            result['max'] = self.max

        if self.metric_name is not None:
            result['metricName'] = self.metric_name

        if self.min is not None:
            result['min'] = self.min

        if self.operator is not None:
            result['operator'] = self.operator

        if self.period is not None:
            result['period'] = self.period

        if self.pre_condition is not None:
            result['preCondition'] = self.pre_condition

        if self.query_name is not None:
            result['queryName'] = self.query_name

        if self.severity is not None:
            result['severity'] = self.severity

        if self.statistics is not None:
            result['statistics'] = self.statistics

        if self.threshold is not None:
            result['threshold'] = self.threshold

        if self.times is not None:
            result['times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comparisonOperator') is not None:
            self.comparison_operator = m.get('comparisonOperator')

        if m.get('condition') is not None:
            self.condition = m.get('condition')

        self.conditions = []
        if m.get('conditions') is not None:
            for k1 in m.get('conditions'):
                temp_model = main_models.TriggerConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('countCondition') is not None:
            self.count_condition = m.get('countCondition')

        if m.get('countOperator') is not None:
            self.count_operator = m.get('countOperator')

        if m.get('countThreshold') is not None:
            self.count_threshold = m.get('countThreshold')

        if m.get('durationSecs') is not None:
            self.duration_secs = m.get('durationSecs')

        if m.get('expressionType') is not None:
            self.expression_type = m.get('expressionType')

        if m.get('logicOperator') is not None:
            self.logic_operator = m.get('logicOperator')

        if m.get('matchField') is not None:
            self.match_field = m.get('matchField')

        if m.get('matchOperator') is not None:
            self.match_operator = m.get('matchOperator')

        if m.get('matchValue') is not None:
            self.match_value = m.get('matchValue')

        if m.get('max') is not None:
            self.max = m.get('max')

        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')

        if m.get('min') is not None:
            self.min = m.get('min')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('period') is not None:
            self.period = m.get('period')

        if m.get('preCondition') is not None:
            self.pre_condition = m.get('preCondition')

        if m.get('queryName') is not None:
            self.query_name = m.get('queryName')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('statistics') is not None:
            self.statistics = m.get('statistics')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        if m.get('times') is not None:
            self.times = m.get('times')

        return self

