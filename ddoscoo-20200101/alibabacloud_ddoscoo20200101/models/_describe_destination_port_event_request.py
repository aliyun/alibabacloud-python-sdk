# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDestinationPortEventRequest(DaraModel):
    def __init__(
        self,
        event_type: str = None,
        ip: str = None,
        range: int = None,
        region: str = None,
        start_time: int = None,
    ):
        # The type of the attack event that you want to query. Valid values:
        # 
        # *   **defense**: attack events that trigger traffic scrubbing.
        # *   **blackhole**: attack events that trigger blackhole filtering.
        # 
        # This parameter is required.
        self.event_type = event_type
        # The IP address of the attacker.
        # 
        # This parameter is required.
        self.ip = ip
        # The number of destination ports to return. The ports are sorted in descending order of the number of received request packets. By default, the first **10** ports are returned.
        # 
        # This parameter is required.
        self.range = range
        # The region in which your service is deployed. Valid values:
        # 
        # *   **cn**: a region in the Chinese mainland.
        # *   **cn-hongkong**: a region outside the Chinese mainland.
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
        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.range is not None:
            result['Range'] = self.range

        if self.region is not None:
            result['Region'] = self.region

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Range') is not None:
            self.range = m.get('Range')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

