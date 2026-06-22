# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class TriggerCondition(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        metric_name: str = None,
        statistics: str = None,
        tags: List[main_models.Tag] = None,
        threshold: float = None,
    ):
        # The comparison operator. This parameter is required. Valid values:
        # 
        # *   EQ: equal to
        # *   NE: not equal to
        # *   GT: greater than
        # *   LT: less than
        # *   GE: greater than or equal to
        # *   LE: less than or equal to
        # 
        # This parameter is required.
        self.comparison_operator = comparison_operator
        # The name of the metric. This parameter is required and cannot be an empty string. You can view the metric name in [Add Auto Scaling Rules](https://help.aliyun.com/document_detail/445658.html).
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The name of the statistic. This parameter is required. Valid values:
        # 
        # *   MAX
        # *   MIN
        # *   AVG
        # 
        # This parameter is required.
        self.statistics = statistics
        # The tags for the metrics of a partition. This parameter is available for only metrics that contain ByPartition. For other metrics, leave this parameter empty.
        self.tags = tags
        # The trigger threshold. This parameter is required.
        # 
        # This parameter is required.
        self.threshold = threshold

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.Tag()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

