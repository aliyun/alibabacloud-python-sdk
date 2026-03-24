# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRealtimeDeliveryAccRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        interval: str = None,
        log_store: str = None,
        project: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # The end time must be later than the start time.
        self.end_time = end_time
        # The time granularity of the data entries. Unit: seconds. The value varies based on the values of the **StartTime** and **EndTime** parameters. Valid values:
        # 
        # *   If the time span between StartTime and EndTime is less than 3 days, valid values are **300**, **3600**, and **86400**. Default value: **300**.
        # *   If the time span between StartTime and EndTime is greater than or equal to 3 days and less than 31 days, valid values are **3600** and **86400**. Default value: **3600**.
        # *   If the time span between StartTime and EndTime is 31 days or longer, the valid value is **86400**. Default value: **86400**.
        self.interval = interval
        # The name of the Logstore that stores log data. If you do leave this parameter empty, real-time log deliveries of all Logstores are queried.
        self.log_store = log_store
        # The name of the Log Service project that is used for real-time log delivery. If you do leave this parameter empty, real-time log deliveries of all projects are queried.
        self.project = project
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
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

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.log_store is not None:
            result['LogStore'] = self.log_store

        if self.project is not None:
            result['Project'] = self.project

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

