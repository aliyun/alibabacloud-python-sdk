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
        # The dimensions that specify the resources whose monitoring data you want to query.
        # 
        # Set the value to a collection of key-value pairs. A typical key-value pair is `instanceId:i-2ze2d6j5uhg20x47****`.
        # 
        # >  You can query a maximum of 50 instances in a single request.
        self.dimensions = dimensions
        # The end of the time range to query. The following formats are supported:
        # 
        # *   UNIX timestamp: the number of milliseconds that have elapsed since 00:00:00 Thursday, January 1, 1970
        # *   UTC time: the UTC time that follows the YYYY-MM-DDThh:mm:ssZ format
        self.end_time = end_time
        # The expression that is used to compute the query results in real time.
        # 
        # >  Only the groupby expression is supported. This expression is similar to the GROUP BY statement that is used in databases.
        self.express = express
        # The number of entries to return on each page.
        # 
        # >  The maximum value of the Length parameter in a request is 1440.
        self.length = length
        # The name of the metric.
        # 
        # For more information about metric names, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The namespace of the cloud service. Format: acs_service name.
        # 
        # For more information about the namespaces of cloud services, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # This parameter is required.
        self.namespace = namespace
        # The paging token.
        # 
        # >  If this parameter is not specified, the data on the first page is returned. A return value other than Null of this parameter indicates that not all entries have been returned. You can use this value as an input parameter to obtain entries on the next page. The value Null indicates that all query results have been returned.
        self.next_token = next_token
        # The interval at which the monitoring data is queried.
        # 
        # Valid values: 60, 300, and 900.
        # 
        # Unit: seconds.
        # 
        # >  Configure this parameter based on your business scenario.
        self.period = period
        self.region_id = region_id
        # The beginning of the time range to query. The following formats are supported:
        # 
        # *   UNIX timestamp: the number of milliseconds that have elapsed since 00:00:00 Thursday, January 1, 1970
        # *   UTC time: the UTC time that follows the YYYY-MM-DDThh:mm:ssZ format
        # 
        # >  The specified period includes the end time and excludes the start time. The start time must be earlier than the end time.
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

