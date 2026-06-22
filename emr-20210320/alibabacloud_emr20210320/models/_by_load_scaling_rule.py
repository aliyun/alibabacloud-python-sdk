# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ByLoadScalingRule(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        cool_down_interval: int = None,
        evaluation_count: int = None,
        metric_name: str = None,
        statistics: str = None,
        threshold: float = None,
        time_window: int = None,
    ):
        # 比较符。
        # 
        # This parameter is required.
        self.comparison_operator = comparison_operator
        self.cool_down_interval = cool_down_interval
        # 统计次数。
        # 
        # This parameter is required.
        self.evaluation_count = evaluation_count
        # 指标名称。指标名称需要在 ListAutoScalingMetrics 接口返回的指标名称列表中。
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # 统计量名称。
        # 
        # This parameter is required.
        self.statistics = statistics
        # 阈值。
        # 
        # This parameter is required.
        self.threshold = threshold
        # 统计窗口。单位为秒。
        # 
        # This parameter is required.
        self.time_window = time_window

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator

        if self.cool_down_interval is not None:
            result['CoolDownInterval'] = self.cool_down_interval

        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.time_window is not None:
            result['TimeWindow'] = self.time_window

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')

        if m.get('CoolDownInterval') is not None:
            self.cool_down_interval = m.get('CoolDownInterval')

        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('TimeWindow') is not None:
            self.time_window = m.get('TimeWindow')

        return self

