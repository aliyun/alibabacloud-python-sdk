# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeElasticQpsRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        interval: str = None,
        ip: str = None,
        region: str = None,
        start_time: int = None,
    ):
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # >  This UNIX timestamp must indicate a point in time that is accurate to the minute.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The sampling interval. Unit: seconds. The value must be a multiple of 60. Default value: 60. Unit: seconds. The query result varies depending on the sampling interval.
        self.interval = interval
        # The IP address of the Anti-DDoS Proxy instance to query.
        self.ip = ip
        # The type of the service. Valid values:
        # 
        # *   **cn**: Anti-DDoS Proxy (Chinese Mainland)
        # *   **cn-hongkong**: Anti-DDoS Proxy (Outside Chinese Mainland)
        # 
        # This parameter is required.
        self.region = region
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # >  This UNIX timestamp must indicate a point in time that is accurate to the minute.
        # 
        # This parameter is required.
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

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.region is not None:
            result['Region'] = self.region

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

