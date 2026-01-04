# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDDosAllEventListResponseBody(DaraModel):
    def __init__(
        self,
        attack_events: List[main_models.DescribeDDosAllEventListResponseBodyAttackEvents] = None,
        request_id: str = None,
        total: int = None,
    ):
        # The DDoS attack events.
        self.attack_events = attack_events
        # The ID of the request.
        self.request_id = request_id
        # The total number of DDoS attack events.
        self.total = total

    def validate(self):
        if self.attack_events:
            for v1 in self.attack_events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttackEvents'] = []
        if self.attack_events is not None:
            for k1 in self.attack_events:
                result['AttackEvents'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attack_events = []
        if m.get('AttackEvents') is not None:
            for k1 in m.get('AttackEvents'):
                temp_model = main_models.DescribeDDosAllEventListResponseBodyAttackEvents()
                self.attack_events.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeDDosAllEventListResponseBodyAttackEvents(DaraModel):
    def __init__(
        self,
        area: str = None,
        end_time: int = None,
        event_type: str = None,
        ip: str = None,
        mbps: int = None,
        port: str = None,
        pps: int = None,
        start_time: int = None,
    ):
        # The source location or region from which the attack was initiated. Valid values:
        # 
        # *   **cn**: Chinese mainland
        # *   **alb-cn-hongkong-gf-2**: China (Hongkong)
        # *   **alb-us-west-1-gf-2**: US (Silicon Valley)
        # *   **alb-ap-northeast-1-gf-1**: Japan (Tokyo)
        # *   **alb-ap-southeast-gf-1**: Singapore
        # *   **alb-eu-central-1-gf-1**: Germany (Frankfurt)
        # *   **alb-eu-central-1-gf-1** or **selb-eu-west-1-gf-1a**: UK (London)
        # *   **alb-us-east-gf-1**: US (Virginia)
        # *   **CT-yundi**: China (Hongkong) This value is returned only for Anti-DDoS Premium instances of the Secure Chinese Mainland Acceleration (Sec-CMA) mitigation plan.
        self.area = area
        # The time when the DDoS attack stopped. This value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time
        # The type of the DDoS attack event. Valid values:
        # 
        # *   **web-cc**: resource exhaustion attacks
        # *   **cc**: connection flood attacks
        # *   **defense**: DDoS attacks that trigger traffic scrubbing
        # *   **blackhole**: DDoS attacks that trigger blackhole filtering
        self.event_type = event_type
        # The attacked object. The attacked object varies based on the attack event type. The following list describes different attacked objects of different attack event types:
        # 
        # *   If **EventType** is set to **web-cc**, the value of this parameter indicates the domain name of the attacked website.
        # *   If **EventType** is set to **cc**, the value of this parameter indicates the IP address of the attacked Anti-DDoS Pro or Anti-DDoS Premium instance.
        # *   If **EventType** is set to **defense** or **blackhole**, the value of this parameter indicates the IP address of the attacked Anti-DDoS Pro or Anti-DDoS Premium instance.
        self.ip = ip
        # The peak bandwidth of the attack traffic. Unit: Mbit/s.
        self.mbps = mbps
        # The attacked port.
        # 
        # > If **EventType** is set to **web-cc**, this parameter is not returned.
        self.port = port
        # The peak packet forwarding rate of attack traffic. Unit: packets per second (pps).
        self.pps = pps
        # The time when the DDoS attack started. This value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.mbps is not None:
            result['Mbps'] = self.mbps

        if self.port is not None:
            result['Port'] = self.port

        if self.pps is not None:
            result['Pps'] = self.pps

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Mbps') is not None:
            self.mbps = m.get('Mbps')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Pps') is not None:
            self.pps = m.get('Pps')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

