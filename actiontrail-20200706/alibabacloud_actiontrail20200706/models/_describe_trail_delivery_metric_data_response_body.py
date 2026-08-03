# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_actiontrail20200706 import models as main_models
from darabonba.model import DaraModel

class DescribeTrailDeliveryMetricDataResponseBody(DaraModel):
    def __init__(
        self,
        metric_list: List[main_models.DescribeTrailDeliveryMetricDataResponseBodyMetricList] = None,
        request_id: str = None,
    ):
        # A list of data points for the delivery monitoring metric.
        self.metric_list = metric_list
        # The unique ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.metric_list:
            for v1 in self.metric_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MetricList'] = []
        if self.metric_list is not None:
            for k1 in self.metric_list:
                result['MetricList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metric_list = []
        if m.get('MetricList') is not None:
            for k1 in m.get('MetricList'):
                temp_model = main_models.DescribeTrailDeliveryMetricDataResponseBodyMetricList()
                self.metric_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeTrailDeliveryMetricDataResponseBodyMetricList(DaraModel):
    def __init__(
        self,
        count: int = None,
        timestamp: int = None,
    ):
        # The value of the metric. The meaning of this parameter depends on the value of the `MetricName` parameter in the request.
        # 
        # For example, if `MetricName` is set to `delivery_sls_success_count`, `Count` indicates the number of logs successfully delivered to SLS.
        self.count = count
        # The Unix timestamp, in milliseconds, that marks the start of the time window for this data point.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

