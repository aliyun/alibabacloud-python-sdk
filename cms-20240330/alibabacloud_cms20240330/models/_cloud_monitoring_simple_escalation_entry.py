# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudMonitoringSimpleEscalationEntry(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        pre_condition: str = None,
        severity: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # The comparison operator.
        self.comparison_operator = comparison_operator
        # The precondition.
        self.pre_condition = pre_condition
        # The severity level.
        self.severity = severity
        # The statistics method.
        self.statistics = statistics
        # The threshold.
        self.threshold = threshold
        # The number of consecutive times the condition is triggered.
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comparison_operator is not None:
            result['comparisonOperator'] = self.comparison_operator

        if self.pre_condition is not None:
            result['preCondition'] = self.pre_condition

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

        if m.get('preCondition') is not None:
            self.pre_condition = m.get('preCondition')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('statistics') is not None:
            self.statistics = m.get('statistics')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        if m.get('times') is not None:
            self.times = m.get('times')

        return self

