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
        # The details about the DDoS attack event.
        self.events = events
        # The request ID.
        self.request_id = request_id
        # The total number of DDoS attack events that are returned.
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
        # The time when the DDoS attack stopped. This value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time
        # The attacked IP address.
        self.ip = ip
        # The volume of the request traffic at the start of the DDoS attack. Unit: Mbit/s.
        self.mbps = mbps
        # The number of packets at the start of the DDoS attack. Unit: packets per second (PPS).
        self.pps = pps
        # The time when the DDoS attack started. This value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time
        # The status of the DDoS attack event. Valid values:
        # 
        # *   **hole_begin**: indicates that blackhole filtering is triggered for the attacked IP address.
        # *   **hole_end**: indicates that blackhole filtering is deactivated for the attacked IP address.
        # *   **defense_begin**: indicates that attack traffic is being scrubbed.
        # *   **defense_end**: indicates that attack traffic is scrubbed.
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

