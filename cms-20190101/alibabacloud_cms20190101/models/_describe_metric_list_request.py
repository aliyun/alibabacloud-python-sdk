# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMetricListRequest(DaraModel):
    def __init__(
        self,
        dimensions: str = None,
        end_time: str = None,
        express: str = None,
        length: str = None,
        metric_name: str = None,
        namespace: str = None,
        next_token: str = None,
        period: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The dimensions that specify the resources to be monitored.
        # 
        # Format: a collection of key-value pairs, such as `{"userId":"120886317861****"}` and `{"instanceId":"i-2ze2d6j5uhg20x47****"}`.
        # 
        # > A single request can be used to query a maximum of 50 instances.
        self.dimensions = dimensions
        # The end of the time range to query. The following formats are supported:
        # 
        # - UNIX timestamp: the number of milliseconds that have elapsed since 00:00:00 UTC on January 1, 1970.
        # 
        # - Format: YYYY-MM-DD hh:mm:ss.
        # 
        # > The interval between \\`StartTime\\` and \\`EndTime\\` must be less than or equal to 31 days.
        self.end_time = end_time
        # The expression that is used for real-time computing based on the query results.
        # 
        # > Only the groupby expression is supported. This expression is similar to the GROUP BY statement in databases.
        self.express = express
        # The number of entries to return on each page for a paged query.
        # 
        # > The maximum value of \\`Length\\` in a single request is 1440.
        self.length = length
        # The name of the metric.
        # 
        # For more information, see [Metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The namespace of the cloud service.
        # 
        # For more information, see [Metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # This parameter is required.
        self.namespace = namespace
        # The pagination cursor.
        # 
        # > If you do not set this parameter, the first page of data is returned. If a value is returned for this parameter, it indicates that more data is available. To retrieve the next page, use the returned value as the \\`NextToken\\` in your next request. A null value indicates that all data has been retrieved.
        self.next_token = next_token
        # The statistical period of the monitoring data.
        # 
        # Valid values: 15, 60, 900, and 3600.
        # 
        # Unit: seconds.
        # 
        # > - If you do not set this parameter, the reporting period that was specified when the metric was registered is used.
        # 
        # - The statistical period of each metric (`MetricName`) of a cloud service is different. For more information, see [Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.period = period
        self.region_id = region_id
        # The beginning of the time range to query. The following formats are supported:
        # 
        # - UNIX timestamp: the number of milliseconds that have elapsed since 00:00:00 UTC on January 1, 1970.
        # 
        # - Format: YYYY-MM-DD hh:mm:ss.
        # 
        # > * The time range is a left-open and right-closed interval. The value of \\`StartTime\\` must be earlier than the value of \\`EndTime\\`.
        # 
        # - The interval between \\`StartTime\\` and \\`EndTime\\` must be less than or equal to 31 days.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.express is not None:
            result['Express'] = self.express

        if self.length is not None:
            result['Length'] = self.length

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Express') is not None:
            self.express = m.get('Express')

        if m.get('Length') is not None:
            self.length = m.get('Length')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

