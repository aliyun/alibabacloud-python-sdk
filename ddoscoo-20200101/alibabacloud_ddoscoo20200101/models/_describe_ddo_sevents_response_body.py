# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDDoSEventsResponseBody(DaraModel):
    def __init__(
        self,
        ddo_sevents: List[main_models.DescribeDDoSEventsResponseBodyDDoSEvents] = None,
        request_id: str = None,
        total: int = None,
    ):
        # The DDoS attack events.
        self.ddo_sevents = ddo_sevents
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned attack events.
        self.total = total

    def validate(self):
        if self.ddo_sevents:
            for v1 in self.ddo_sevents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DDoSEvents'] = []
        if self.ddo_sevents is not None:
            for k1 in self.ddo_sevents:
                result['DDoSEvents'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ddo_sevents = []
        if m.get('DDoSEvents') is not None:
            for k1 in m.get('DDoSEvents'):
                temp_model = main_models.DescribeDDoSEventsResponseBodyDDoSEvents()
                self.ddo_sevents.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeDDoSEventsResponseBodyDDoSEvents(DaraModel):
    def __init__(
        self,
        bps: int = None,
        end_time: int = None,
        event_type: str = None,
        ip: str = None,
        port: str = None,
        pps: int = None,
        region: str = None,
        start_time: int = None,
    ):
        # The bandwidth of attack traffic. Unit: bit/s.
        self.bps = bps
        # The time when the DDoS attack stopped. The value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time
        # The type of the attack event. Valid values:
        # 
        # *   **defense**: traffic scrubbing events
        # *   **blackhole**: blackhole filtering events
        self.event_type = event_type
        # The attacked IP address.
        self.ip = ip
        # The attacked port.
        self.port = port
        # The packet forwarding rate of attack traffic. Unit: packets per second (pps).
        self.pps = pps
        # The region from which the attack was launched. Valid values:
        # 
        # *   **cn**: a region in the Chinese mainland
        # *   **alb-ap-northeast-1-gf-x**: Japan (Tokyo)
        # *   **alb-ap-southeast-gf-x**: Singapore
        # *   **alb-cn-hongkong-gf-x**: Hong Kong (China)
        # *   **alb-eu-central-1-gf-x**: Germany (Frankfurt)
        # *   **alb-us-west-1-gf-x**: US (Silicon Valley)
        # 
        # > The values except **cn** are returned only when **RegionId** is set to **ap-southeast-1**.
        self.region = region
        # The time when the DDoS attack started. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bps is not None:
            result['Bps'] = self.bps

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.port is not None:
            result['Port'] = self.port

        if self.pps is not None:
            result['Pps'] = self.pps

        if self.region is not None:
            result['Region'] = self.region

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Pps') is not None:
            self.pps = m.get('Pps')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

