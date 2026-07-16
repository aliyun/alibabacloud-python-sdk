# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AutoscalingMetricSpec(DaraModel):
    def __init__(
        self,
        metric_name: str = None,
        stabilization_window_seconds: int = None,
        target_value: int = None,
        tolerance: str = None,
    ):
        # The name of the metric for autoscaling. This can be a predefined or a custom metric.
        self.metric_name = metric_name
        # The cooldown period, in seconds, after a scaling activity. This prevents the service from initiating another scaling action before the effects of the previous one are observable, stabilizing resource fluctuations.
        self.stabilization_window_seconds = stabilization_window_seconds
        # The target value for the specified metric. The autoscaling service tries to maintain the metric at or near this value.
        self.target_value = target_value
        # The acceptable deviation from the `TargetValue`, specified as a percentage string. A scaling action is triggered only if the metric value moves outside the range defined by the `TargetValue` and this tolerance. This prevents scaling actions based on minor fluctuations.
        self.tolerance = tolerance

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.stabilization_window_seconds is not None:
            result['StabilizationWindowSeconds'] = self.stabilization_window_seconds

        if self.target_value is not None:
            result['TargetValue'] = self.target_value

        if self.tolerance is not None:
            result['Tolerance'] = self.tolerance

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('StabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('StabilizationWindowSeconds')

        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')

        if m.get('Tolerance') is not None:
            self.tolerance = m.get('Tolerance')

        return self

