# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddosbgp20180720 import models as main_models
from darabonba.model import DaraModel

class DescribeDdosEventResponseBody(DaraModel):
    def __init__(
        self,
        events: List[main_models.DescribeDdosEventResponseBodyEvents] = None,
        request_id: str = None,
        total: int = None,
    ):
        # The details of the DDoS attack events.
        self.events = events
        # The ID of the request.
        self.request_id = request_id
        # The total number of DDoS attack events returned.
        self.total = total

    def validate(self):
        if self.events:
            for v1 in self.events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Events'] = []
        if self.events is not None:
            for k1 in self.events:
                result['Events'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k1 in m.get('Events'):
                temp_model = main_models.DescribeDdosEventResponseBodyEvents()
                self.events.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeDdosEventResponseBodyEvents(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        ip: str = None,
        mbps: int = None,
        pps: int = None,
        start_time: int = None,
        status: str = None,
    ):
        # The end time of the attack. The time is a UNIX timestamp in seconds.
        self.end_time = end_time
        # The attacked IP address.
        self.ip = ip
        # The traffic volume at the start of the attack. Unit: Mbit/s.
        self.mbps = mbps
        # The packet rate at the start of the attack. Unit: pps.
        self.pps = pps
        # The end time of the attack. The time is a UNIX timestamp in seconds.
        self.start_time = start_time
        # The current status of the attack event. Valid values:
        # 
        # - **hole_begin**: Indicates that the attacked IP address is in the blackhole filtering status.
        # - **hole_end**: Indicates that the attacked IP address is removed from the blackhole filtering status.
        # - **defense_begin**: Indicates that the system scrubs traffic.
        # - **defense_end**: Indicates that the attack ends and the system scrubs traffic no more.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.mbps is not None:
            result['Mbps'] = self.mbps

        if self.pps is not None:
            result['Pps'] = self.pps

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Mbps') is not None:
            self.mbps = m.get('Mbps')

        if m.get('Pps') is not None:
            self.pps = m.get('Pps')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

