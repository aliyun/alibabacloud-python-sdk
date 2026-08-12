# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudMonitoringCompositeEscalationEntry(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        metric_name: str = None,
        period: int = None,
        pre_condition: str = None,
        statistics: str = None,
        threshold: str = None,
    ):
        # The comparison operator.
        self.comparison_operator = comparison_operator
        # The metric name.
        self.metric_name = metric_name
        # The collection period, in seconds.
        self.period = period
        # The precondition.
        self.pre_condition = pre_condition
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
        if self.comparison_operator is not None:
            result['comparisonOperator'] = self.comparison_operator

        if self.metric_name is not None:
            result['metricName'] = self.metric_name

        if self.period is not None:
            result['period'] = self.period

        if self.pre_condition is not None:
            result['preCondition'] = self.pre_condition

        if self.statistics is not None:
            result['statistics'] = self.statistics

        if self.threshold is not None:
            result['threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comparisonOperator') is not None:
            self.comparison_operator = m.get('comparisonOperator')

        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')

        if m.get('period') is not None:
            self.period = m.get('period')

        if m.get('preCondition') is not None:
            self.pre_condition = m.get('preCondition')

        if m.get('statistics') is not None:
            self.statistics = m.get('statistics')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        return self

