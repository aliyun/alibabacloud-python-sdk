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
        # The end of the query time range, specified as a UNIX timestamp in seconds.
        # 
        # > The timestamp must be the start of a minute.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The sampling interval, in seconds. The value must be a multiple of 60. The default value is 60.
        self.interval = interval
        # The IP address of the Anti-DDoS instance to query.
        self.ip = ip
        # The service region. Valid values:
        # 
        # - **cn**: Chinese mainland.
        # 
        # - **cn-hongkong**: Outside Chinese mainland.
        # 
        # This parameter is required.
        self.region = region
        # The start of the query time range, specified as a UNIX timestamp in seconds.
        # 
        # > The timestamp must be the start of a minute.
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

