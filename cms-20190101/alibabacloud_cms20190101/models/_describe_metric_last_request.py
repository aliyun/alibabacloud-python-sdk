# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMetricLastRequest(DaraModel):
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
        # The monitoring dimensions of the specified resource.
        # 
        # Format: a collection of `key:value` pairs. Example: `{"userId":"120886317861****"}` or `{"instanceId":"i-2ze2d6j5uhg20x47****"}`.
        # 
        # > A maximum of 50 instances can be queried in a single request.
        self.dimensions = dimensions
        # The end time for querying the metric.
        # 
        # The system automatically limits the query start time (query window size) based on data granularity:
        # 1. Second-level data: The maximum query span is 20 minutes (start time = Max(startTime, EndTime - 20min)).
        # 2. Minute-level data: The maximum query span is 2 hours (start time = Max(startTime, EndTime - 2h)).
        # 3. Hour-level data: The maximum query span is 2 days (start time = Max(startTime, EndTime - 2d)).
        # 
        # > If the specified startTime is earlier than the limit, the system automatically uses the limit as the actual query start time.
        self.end_time = end_time
        # The expression for real-time computation on existing query results.
        self.express = express
        # The number of entries per page for monitoring data. This parameter is used for paged query.
        # 
        # Default value: 1000, which indicates 1000 entries of monitoring data per page.
        # 
        # > The maximum value of Length in a single request is 1440.
        self.length = length
        # The metric name of the cloud service.
        # 
        # For information about metric names, see [Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The namespace of the cloud service.
        # 
        # For information about namespaces of cloud services, see [Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # This parameter is required.
        self.namespace = namespace
        # The pagination cursor.
        # 
        # - If the query results that match the filter conditions exceed the page size, a pagination cursor is returned.
        # - To retrieve the next page of data, use the returned cursor value as the request parameter until no cursor value is returned, which indicates that all data has been retrieved.
        self.next_token = next_token
        # The statistical period of the monitoring data.
        # 
        # Valid values: 15, 60, 900, and 3600.
        # 
        # Unit: seconds.
        # 
        # > - If you do not set the statistical period, monitoring data is queried based on the reporting period that was specified when the metric was registered.
        #     - The statistical period varies by metric (`MetricName`) for each cloud service. For more information, see the `Min Periods` column on the metric list page of the target cloud service in [Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        self.period = period
        self.region_id = region_id
        # The start time.
        # 
        # Two formats are supported: 1. A UNIX timestamp string in milliseconds (ms), which represents the number of milliseconds elapsed since 1970-01-01 00:00:00 UTC. 2. A time string in the ISO 8601 format of YYYY-MM-DDThh:mm:ssZ in UTC.
        # 
        # > The query range uses a left-exclusive and right-inclusive mode. StartTime cannot be equal to or greater than EndTime, and the interval between them must be less than or equal to 31 days.
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

