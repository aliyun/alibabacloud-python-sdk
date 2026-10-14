# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDDosEventIspRequest(DaraModel):
    def __init__(
        self,
        event_type: str = None,
        ip: str = None,
        range: int = None,
        start_time: int = None,
    ):
        # The event type of the attack event to query. Valid values:
        # 
        # - **defense**: traffic scrubbing events for volumetric attacks.
        # - **blackhole**: blackhole filtering events for volumetric attacks.
        # 
        # This parameter is required.
        self.event_type = event_type
        # The attacked IP Address of Anti-DDoS Proxy instance.
        # 
        # This parameter is required.
        self.ip = ip
        # The number of data entries to return.
        self.range = range
        # The start timestamp of the event to query. Unit: seconds.
        # 
        # > You can call [DescribeDDosAllEventList](https://help.aliyun.com/document_detail/473646.html) to query the start time of all events.
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

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

