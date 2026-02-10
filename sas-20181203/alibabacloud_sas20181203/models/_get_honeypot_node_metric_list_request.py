# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetHoneypotNodeMetricListRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        express: str = None,
        length: str = None,
        metric_name: str = None,
        namespace: str = None,
        node_id: str = None,
        period: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query. Valid values:
        # 
        # *   UNIX timestamp: the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC
        # *   Date format: YYYY-MM-DDThh:mm:ssZ
        self.end_time = end_time
        # The expression that is used to compute the query results in real time.
        # 
        # >  Only the groupby expression is supported. This expression is similar to the GROUP BY statement that applies to databases.
        self.express = express
        # The number of entries per page.
        # 
        # >  The maximum value of the Length parameter in a request is 1440.
        self.length = length
        # The metric that is used to monitor the cloud service.
        self.metric_name = metric_name
        # The namespace of the cloud service. Format: acs_cloud service name.
        self.namespace = namespace
        # The management node ID.
        self.node_id = node_id
        # The time interval. Unit: seconds. Valid values: 60, 300, and 900.
        self.period = period
        # The beginning of the time range to query. The following formats are supported:
        # 
        # *   UNIX timestamp: the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC
        # *   Date format: YYYY-MM-DDThh:mm:ssZ
        # *   The interval between the start time and the end time is less than or equal to 31 days.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.period is not None:
            result['Period'] = self.period

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

