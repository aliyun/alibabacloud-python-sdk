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
        # The list of attack events.
        self.attack_events = attack_events
        # The request ID.
        self.request_id = request_id
        # The total number of attack events returned.
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
        # The source region of the attack. Valid values:
        # 
        # - **cn**: the Chinese mainland.
        # - **alb-cn-hongkong-gf-2**: Hong Kong (China).
        # - **alb-us-west-1-gf-2**: US (Silicon Valley).
        # - **alb-ap-northeast-1-gf-1**: Japan (Tokyo).
        # - **alb-ap-southeast-gf-1**: Singapore.
        # - **alb-eu-central-1-gf-1**: Germany (Frankfurt).
        # - **alb-eu-west-1-gf-1** and **selb-eu-west-1-gf-1a**: UK (London).
        # - **alb-us-east-gf-1**: US (Virginia).
        # - **CT-yundi**: Hong Kong (China). This value applies only to Anti-DDoS Pro and Anti-DDoS Premium secure acceleration line instances.
        self.area = area
        # The end time of the attack. The value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time
        # The type of the DDoS attack event. Valid values:
        # 
        # - **web-cc**: web resource exhaustion attack.
        # - **cc**: connection flood attack.
        # - **defense**: volumetric attack (scrubbing event).
        # - **blackhole**: volumetric attack (blackhole filtering event).
        self.event_type = event_type
        # The attacked object. The attacked object varies based on the attack event type:
        # 
        # - Web resource exhaustion attack (**EventType** is **web-cc**): this parameter indicates the attacked website domain name.
        # - Connection flood attack (**EventType** is **cc**): this parameter indicates the attacked IP address of the Anti-DDoS Pro or Anti-DDoS Premium instance.
        # - Volumetric attack (**EventType** is **defense** or **blackhole**): this parameter indicates the attacked IP address of the Anti-DDoS Pro or Anti-DDoS Premium instance.
        self.ip = ip
        # The peak bandwidth of the attack traffic. Unit: Mbit/s.
        self.mbps = mbps
        # The attacked port number.
        # 
        # > This parameter is not returned for web resource exhaustion attacks (**EventType** is **web-cc**).
        self.port = port
        # The peak packet forwarding rate of the attack traffic. Unit: pps.
        self.pps = pps
        # The start time of the attack. The value is a UNIX timestamp. Unit: seconds.
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

