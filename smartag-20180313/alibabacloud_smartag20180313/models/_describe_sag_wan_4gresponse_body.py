# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSagWan4GResponseBody(DaraModel):
    def __init__(
        self,
        ip: str = None,
        mac: str = None,
        priority: int = None,
        request_id: str = None,
        status: str = None,
        strength: str = None,
        traffic_state: str = None,
    ):
        # The IP address of the 4G NIC.
        self.ip = ip
        # The MAC address of the 4G NIC.
        self.mac = mac
        # The priority of the 4G NIC. The default value is **99**, which indicates the lowest priority. The priority cannot be modified.
        self.priority = priority
        # The request ID.
        self.request_id = request_id
        # The status of the 4G NIC. Valid values:
        # - **Normal**: The status is normal.
        # - **Abnormal**: The status is abnormal.
        # - **Unavailable**: No 4G NIC is available.
        self.status = status
        # The 4G signal strength. Valid values:
        # - **High**: Strong.
        # - **Middle**: Medium.
        # - **Low**: Weak.
        # - **Unavailable**: No signal.
        self.strength = strength
        # The traffic status of the 4G NIC. Valid values:
        # - **active**: The 4G NIC acts as the active link, and current traffic is transmitted through this 4G NIC.
        # - **standby**: The 4G NIC acts as the standby link and does not forward traffic. If the active link fails, traffic is transmitted through this 4G NIC.
        self.traffic_state = traffic_state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.strength is not None:
            result['Strength'] = self.strength

        if self.traffic_state is not None:
            result['TrafficState'] = self.traffic_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Strength') is not None:
            self.strength = m.get('Strength')

        if m.get('TrafficState') is not None:
            self.traffic_state = m.get('TrafficState')

        return self

