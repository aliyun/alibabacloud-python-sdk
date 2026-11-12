# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudMonitoringSimpleEscalationEntry(DaraModel):
    def __init__(
        self,
        abs_deviation: float = None,
        baseline_period: str = None,
        comparison_operator: str = None,
        pre_condition: str = None,
        sensitivity: str = None,
        severity: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # The minimum deviation or absolute deviation dead zone for dynamic baselines (effective only for baseline comparison operators). No alert is triggered if |current value - boundary| < absDeviation. The unit is the same as the metric. The value must be greater than or equal to 0. A value of 0 means no limit.
        self.abs_deviation = abs_deviation
        # The baseline period (effective only for baseline comparison operators). Valid values: AUTO for automatic identification, DAILY for daily, WEEKLY for weekly, and NONE for no period. For weekly periods, the backend automatically expands the historical training window to 14 days or more. Automatic identification cannot return specific identification results.
        self.baseline_period = baseline_period
        # The comparison operator. GreaterThanThreshold or LessThanThreshold is used for static thresholds. ABOVE_UPPER, BELOW_LOWER, or OUT_OF_BAND is used for dynamic baseline spikes, drops, or bidirectional changes, which requires the sensitivity parameter. The threshold parameter is not used for baselines and can be omitted.
        self.comparison_operator = comparison_operator
        # The precondition.
        self.pre_condition = pre_condition
        # The dynamic baseline sensitivity (effective only for baseline comparison operators). Valid values: HIGH for the narrowest and most sensitive band, MEDIUM for medium, and LOW for the widest and least sensitive band.
        self.sensitivity = sensitivity
        # The severity level.
        self.severity = severity
        # The statistical method.
        self.statistics = statistics
        # The threshold.
        self.threshold = threshold
        # The number of consecutive triggers.
        self.times = times

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

        if self.pre_condition is not None:
            result['preCondition'] = self.pre_condition

        if self.sensitivity is not None:
            result['sensitivity'] = self.sensitivity

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
        if m.get('absDeviation') is not None:
            self.abs_deviation = m.get('absDeviation')

        if m.get('baselinePeriod') is not None:
            self.baseline_period = m.get('baselinePeriod')

        if m.get('comparisonOperator') is not None:
            self.comparison_operator = m.get('comparisonOperator')

        if m.get('preCondition') is not None:
            self.pre_condition = m.get('preCondition')

        if m.get('sensitivity') is not None:
            self.sensitivity = m.get('sensitivity')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('statistics') is not None:
            self.statistics = m.get('statistics')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        if m.get('times') is not None:
            self.times = m.get('times')

        return self

