# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDDosEventAttackTypeRequest(DaraModel):
    def __init__(
        self,
        event_type: str = None,
        ip: str = None,
        start_time: int = None,
    ):
        # The type of the attack event that you want to query. Valid values:
        # 
        # *   **defense**: attack events that trigger traffic scrubbing
        # *   **blackhole**: attack events that trigger blackhole filtering
        # 
        # This parameter is required.
        self.event_type = event_type
        # The IP address of the attacked Anti-DDoS Pro or Anti-DDoS Premium instance.
        # 
        # This parameter is required.
        self.ip = ip
        # The UNIX timestamp when the query starts. Unit: seconds.
        # 
        # > You can call the [DescribeDDosAllEventList](https://help.aliyun.com/document_detail/188604.html) operation to query the beginning time of all attack events.
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

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

