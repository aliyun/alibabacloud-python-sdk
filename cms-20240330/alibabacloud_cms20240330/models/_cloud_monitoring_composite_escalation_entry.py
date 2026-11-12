# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudMonitoringCompositeEscalationEntry(DaraModel):
    def __init__(
        self,
        abs_deviation: float = None,
        baseline_period: str = None,
        comparison_operator: str = None,
        metric_name: str = None,
        period: int = None,
        pre_condition: str = None,
        sensitivity: str = None,
        statistics: str = None,
        threshold: str = None,
    ):
        # The minimum deviation or absolute deviation dead zone for the dynamic baseline. This parameter takes effect only when the comparisonOperator is set to a baseline operator. If the absolute difference between the current value and the boundary is less than the absDeviation value, no alert is triggered. The unit is the same as the metric unit. The value must be greater than or equal to 0. A value of 0 indicates no limit.
        self.abs_deviation = abs_deviation
        # The baseline period. This parameter takes effect only when the comparisonOperator is set to a baseline operator. Valid values: AUTO (automatic identification), DAILY (daily), WEEKLY (weekly), and NONE (no period). If you set this parameter to WEEKLY, the backend automatically extends the historical training window to at least 14 days. Specific identification results are not returned for automatic identification.
        self.baseline_period = baseline_period
        # The comparison operator.
        self.comparison_operator = comparison_operator
        # The metric name.
        self.metric_name = metric_name
        # The collection period in seconds.
        self.period = period
        # The precondition.
        self.pre_condition = pre_condition
        # The sensitivity of the dynamic baseline. This parameter takes effect only when the comparisonOperator is set to a baseline operator. Valid values: HIGH (narrowest band and most sensitive), MEDIUM (medium), and LOW (widest band and least sensitive).
        self.sensitivity = sensitivity
        # The statistical method.
        self.statistics = statistics
        # The threshold.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abs_deviation is not None:
            result['absDeviation'] = self.abs_deviation

        if self.baseline_period is not None:
            result['baselinePeriod'] = self.baseline_period

        if self.comparison_operator is not None:
            result['comparisonOperator'] = self.comparison_operator

        if self.metric_name is not None:
            result['metricName'] = self.metric_name

        if self.period is not None:
            result['period'] = self.period

        if self.pre_condition is not None:
            result['preCondition'] = self.pre_condition

        if self.sensitivity is not None:
            result['sensitivity'] = self.sensitivity

        if self.statistics is not None:
            result['statistics'] = self.statistics

        if self.threshold is not None:
            result['threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('absDeviation') is not None:
            self.abs_deviation = m.get('absDeviation')

        if m.get('baselinePeriod') is not None:
            self.baseline_period = m.get('baselinePeriod')

        if m.get('comparisonOperator') is not None:
            self.comparison_operator = m.get('comparisonOperator')

        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')

        if m.get('period') is not None:
            self.period = m.get('period')

        if m.get('preCondition') is not None:
            self.pre_condition = m.get('preCondition')

        if m.get('sensitivity') is not None:
            self.sensitivity = m.get('sensitivity')

        if m.get('statistics') is not None:
            self.statistics = m.get('statistics')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        return self

