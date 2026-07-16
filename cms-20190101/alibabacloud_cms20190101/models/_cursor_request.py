# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class CursorRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        matchers: List[main_models.Matcher] = None,
        metric: str = None,
        namespace: str = None,
        period: int = None,
        start_time: str = None,
    ):
        # The end of the time range to query.
        # 
        # Unit: milliseconds.
        # 
        # > - Unix timestamp: the number of milliseconds that have elapsed since 00:00:00 on January 1, 1970. The value is in the YYYY-MM-DDThh:mm:ssZ format. For example, 2023-01-01T00:00:00Z indicates 00:00:00 on January 1, 2023 (GMT).
        # - If you do not specify an end time, the end time is unlimited. You do not need to specify this parameter when you export data in real time.
        # - The time to live (TTL) of monitoring data varies based on the statistical granularity in CloudMonitor. Configure a proper time range based on the TTL of the data that corresponds to the `Period` parameter.
        self.end_time = end_time
        # The dimension information of the metric.
        self.matchers = matchers
        # The metric name of the cloud service.
        # 
        # For information about how to obtain the metric name of a cloud service, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # This parameter is required.
        self.metric = metric
        # The data namespace of the cloud service.
        # 
        # For information about how to obtain the data namespace of a cloud service, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # This parameter is required.
        self.namespace = namespace
        # The statistical period of the metric.
        # 
        # Unit: seconds.
        # 
        # > The statistical period of a metric is typically 60 seconds. For special values, see the `Period` parameter in [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # This parameter is required.
        self.period = period
        # The beginning of the time range to query.
        # 
        # The value is in the YYYY-MM-DDThh:mm:ssZ format. For example, 2023-01-01T00:00:00Z indicates 00:00:00 on January 1, 2023 (GMT).
        # 
        # > The time to live (TTL) of monitoring data varies based on the statistical granularity in CloudMonitor. Configure a proper time range based on the TTL of the data that corresponds to the `Period` parameter.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        if self.matchers:
            for v1 in self.matchers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['Matchers'] = []
        if self.matchers is not None:
            for k1 in self.matchers:
                result['Matchers'].append(k1.to_map() if k1 else None)

        if self.metric is not None:
            result['Metric'] = self.metric

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.period is not None:
            result['Period'] = self.period

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.matchers = []
        if m.get('Matchers') is not None:
            for k1 in m.get('Matchers'):
                temp_model = main_models.Matcher()
                self.matchers.append(temp_model.from_map(k1))

        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

