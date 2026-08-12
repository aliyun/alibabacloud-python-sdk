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
        conditions: List[main_models.TriggerConditions] = None,
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
        # The comparison operator for CLOUD_MONITORING_CONDITION.
        self.comparison_operator = comparison_operator
        # The list of sub-conditions for UMODEL_METRICSET_MULTI or PROMETHEUS_MULTI with expressionType=COMPOSITE. Each item contains queryName, operator, and threshold.
        self.conditions = conditions
        # The count comparison operator for SLS_MULTI_CONDITION. Valid values: GTE, GT, EQ, LTE, and LT.
        self.count_operator = count_operator
        # The count threshold for SLS_MULTI_CONDITION. An alert is triggered when this threshold is met.
        self.count_threshold = count_threshold
        # The duration in seconds during which data must continuously meet the condition before an alert is triggered. If this parameter is not specified, the value of conditionConfig.durationSecs is inherited. This parameter is used by UMODEL_METRICSET_MULTI_CONDITION and PROMETHEUS_MULTI_CONDITION.
        self.duration_secs = duration_secs
        # The expression type. Valid values: SIMPLE and COMPOSITE. This parameter takes effect for UMODEL_METRICSET_MULTI_CONDITION and PROMETHEUS_MULTI_CONDITION.
        self.expression_type = expression_type
        # The logical operator for UMODEL_METRICSET_MULTI or PROMETHEUS_MULTI with expressionType=COMPOSITE. Valid values: AND, OR, and UNLESS.
        self.logic_operator = logic_operator
        # The log field name for SLS_MULTI_CONDITION. This parameter is required when matchOperator is set to CONTAINS, EQUALS, or REGEX. When matchOperator is set to PRESENT or NOT_PRESENT, specify the field name.
        self.match_field = match_field
        # The log match operator for SLS_MULTI_CONDITION. Valid values: PRESENT, NOT_PRESENT, CONTAINS, EQUALS, and REGEX. If this parameter is left empty, any data matches.
        self.match_operator = match_operator
        # The log match value for SLS_MULTI_CONDITION. This parameter is required when matchOperator is set to CONTAINS, EQUALS, or REGEX.
        self.match_value = match_value
        # The upper bound of the range for UMODEL_METRICSET_MULTI with expressionType=SIMPLE. This parameter is required when operator is set to IN_RANGE or OUT_OF_RANGE. The value must be greater than or equal to min.
        self.max = max
        # The metric name. This parameter is used for CLOUD_MONITORING_CONDITION with expressionType=COMPOSITE. For SIMPLE, the metric name is specified at the conditionConfig level by the metricName parameter.
        self.metric_name = metric_name
        # The lower bound of the range for UMODEL_METRICSET_MULTI with expressionType=SIMPLE. This parameter is required when operator is set to IN_RANGE or OUT_OF_RANGE.
        self.min = min
        # The comparison operator for UMODEL_METRICSET_MULTI or PROMETHEUS_MULTI with expressionType=SIMPLE.
        self.operator = operator
        # The aggregation period in seconds. This parameter is used for CLOUD_MONITORING_CONDITION with expressionType=COMPOSITE. For SIMPLE, the period is specified at the conditionConfig level by the period parameter.
        self.period = period
        # The precondition for CLOUD_MONITORING_CONDITION.
        self.pre_condition = pre_condition
        # The referenced query name for UMODEL_METRICSET_MULTI or PROMETHEUS_MULTI with expressionType=SIMPLE. This corresponds to QueryConfigUnified.queries[].name.
        self.query_name = query_name
        # The severity level. Priority order: CRITICAL > ERROR > WARN / WARNING > INFO. When multiple triggers exist, they are sorted by this priority, and the first match triggers the alert. This parameter takes effect for SLS_MULTI_CONDITION and CLOUD_MONITORING_CONDITION with expressionType=SIMPLE.
        self.severity = severity
        # The statistical method for CLOUD_MONITORING_CONDITION.
        self.statistics = statistics
        # The threshold value. For CLOUD_MONITORING_CONDITION, this is a string. For UMODEL_METRICSET_MULTI and PROMETHEUS_MULTI, this is a numeric value.
        self.threshold = threshold
        # The number of consecutive times the condition must be met before an alert is triggered. This parameter is used for CLOUD_MONITORING_CONDITION with expressionType=SIMPLE and is set independently for each entry.
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

        result['conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['conditions'].append(k1.to_map() if k1 else None)

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

        self.conditions = []
        if m.get('conditions') is not None:
            for k1 in m.get('conditions'):
                temp_model = main_models.TriggerConditions()
                self.conditions.append(temp_model.from_map(k1))

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

