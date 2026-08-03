# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTrailDeliveryMetricDataRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        metric_name: str = None,
        period: int = None,
        start_time: str = None,
        trail_name: str = None,
    ):
        # The end of the time window for the query. Specify the time in ISO 8601 format: \\"YYYY-MM-DDThh:mm:ssZ\\". The \\"Z\\" indicates UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The name of the delivery monitoring metric. Valid values:
        # 
        # - `delivery_sls_success_count`: The number of logs successfully delivered to SLS.
        # 
        # - `delivery_sls_fail_count`: The number of logs that failed to be delivered to SLS.
        # 
        # - `delivery_oss_success_count`: The number of logs successfully delivered to OSS.
        # 
        # - `delivery_oss_fail_count`: The number of logs that failed to be delivered to OSS.
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The statistical period for the metric data, in seconds. The value must be 60 or a multiple of 60.
        # 
        # Recommended values: 60, 900, and 3600.
        # 
        # This parameter is required.
        self.period = period
        # The start of the time window for the query. Specify the time in ISO 8601 format: \\"YYYY-MM-DDThh:mm:ssZ\\". The \\"Z\\" indicates UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The name of the trail.
        # 
        # This parameter is required.
        self.trail_name = trail_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.period is not None:
            result['Period'] = self.period

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.trail_name is not None:
            result['TrailName'] = self.trail_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TrailName') is not None:
            self.trail_name = m.get('TrailName')

        return self

