# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMetricsRequest(DaraModel):
    def __init__(
        self,
        dimensions: str = None,
        end_time: str = None,
        job_id: str = None,
        length: str = None,
        metric_name: str = None,
        namespace: str = None,
        next_token: str = None,
        period: str = None,
        start_time: str = None,
        token: str = None,
    ):
        # (Required) The request parameters.
        self.dimensions = dimensions
        # The end time of the query. Default value: the current time.
        self.end_time = end_time
        # The job ID.
        self.job_id = job_id
        # The number of entries per query. This parameter is used for paged query with paging. Default value: 1000.
        self.length = length
        # The metric name. Not populated. Not in use.
        self.metric_name = metric_name
        # The data namespace of the cloud service. For information about the data namespaces of cloud services, see cloud service monitoring items.
        self.namespace = namespace
        # The pagination token. If you do not set this parameter, data on the first page is returned. If a value is returned for this parameter, more pages are available. You can set NextToken to the returned value to retrieve the next page. Repeat this process until a null value is returned, which indicates that all data has been retrieved.
        self.next_token = next_token
        # The statistical period of the monitoring data. Unit: seconds. Valid values: 15, 60, 900, and 3600.
        self.period = period
        # The start time (UTC) of the time range for querying monitoring data. Default value: one hour before the current time.
        self.start_time = start_time
        # The temporary token used for authentication.
        self.token = token

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

        if self.job_id is not None:
            result['JobId'] = self.job_id

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

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

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

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

