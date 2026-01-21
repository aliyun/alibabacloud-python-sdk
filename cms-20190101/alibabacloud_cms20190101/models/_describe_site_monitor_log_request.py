# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSiteMonitorLogRequest(DaraModel):
    def __init__(
        self,
        browser: str = None,
        browser_info: str = None,
        city: str = None,
        device: str = None,
        end_time: str = None,
        filter: str = None,
        isp: str = None,
        length: int = None,
        metric_name: str = None,
        next_token: str = None,
        region_id: str = None,
        start_time: str = None,
        task_ids: str = None,
    ):
        self.browser = browser
        self.browser_info = browser_info
        # The city identification code.
        self.city = city
        self.device = device
        # The end of the time range to query. Valid values:
        # 
        # *   UNIX timestamp: the number of milliseconds that have elapsed since 00:00:00 Thursday, January 1, 1970
        # *   UTC time: the UTC time that follows the YYYY-MM-DDThh:mm:ssZ format
        # 
        # >  We recommend that you use UNIX timestamps to prevent time zone-related issues.
        self.end_time = end_time
        # The filter condition.
        # 
        # You can specify a simple expression, for example, `TotalTime>100`. In this case, the operation returns only the data for instant test tasks whose total response time exceeds 100 milliseconds.
        self.filter = filter
        # The carrier identification code.
        self.isp = isp
        # The number of entries to return on each page. Valid values: 1 to 1440.
        self.length = length
        # The name of the metric.
        # 
        # Only the `ProbeLog` metric is supported.
        self.metric_name = metric_name
        # The token that is used to initiate the next request if the response of the current request is truncated. You can use the token to initiate another request and obtain the remaining records.``
        self.next_token = next_token
        self.region_id = region_id
        # The start of the time range to query. The following formats are supported:
        # 
        # *   UNIX timestamp: the number of milliseconds that have elapsed since 00:00:00 Thursday, January 1, 1970
        # *   UTC time: the UTC time that follows the YYYY-MM-DDThh:mm:ssZ format
        # 
        # > 
        # 
        # *   The specified time range includes the end time and excludes the start time. The start time must be earlier than the end time.\\
        #     We recommend that you use UNIX timestamps to prevent time zone-related issues.
        self.start_time = start_time
        # The IDs of the instant test tasks. Separate multiple task IDs with commas (,).
        # 
        # This parameter is required.
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.browser is not None:
            result['Browser'] = self.browser

        if self.browser_info is not None:
            result['BrowserInfo'] = self.browser_info

        if self.city is not None:
            result['City'] = self.city

        if self.device is not None:
            result['Device'] = self.device

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.length is not None:
            result['Length'] = self.length

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Browser') is not None:
            self.browser = m.get('Browser')

        if m.get('BrowserInfo') is not None:
            self.browser_info = m.get('BrowserInfo')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Device') is not None:
            self.device = m.get('Device')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('Length') is not None:
            self.length = m.get('Length')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')

        return self

