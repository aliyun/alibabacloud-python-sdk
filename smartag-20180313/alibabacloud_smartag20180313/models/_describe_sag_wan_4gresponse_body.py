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
        # The IP address of the 4G SIM card.
        self.ip = ip
        # The MAC address of the 4G SIM card.
        self.mac = mac
        # The priority of the 4G SIM card. The default value is **99**, which indicates the lowest priority and cannot be modified.
        self.priority = priority
        # The request ID.
        self.request_id = request_id
        # The status of the 4G SIM card. Valid value:
        # 
        # *   **Normal**: The 4G SIM card is available.
        # *   **Abnormal**: The 4G SIM card encountered an error.
        # *   **Unavailable**: No 4G SIM card is inserted.
        self.status = status
        # The signal strength of the 4G network. Valid values:
        # 
        # *   **High**: strong signals.
        # *   **Middle**: medium-strength signals.
        # *   **Low**: weak signals.
        # *   **Unavailable**: no signal.
        self.strength = strength
        # The network status of the 4G SIM card. Valid values:
        # 
        # *   **active**: The 4G SIM card is used to establish the active connection. Network traffic is transmitted over the 4G SIM card first.
        # *   **standby**: The 4G SIM card is used to establish a standby connection. Network traffic is not transmitted over the 4G SIM card unless the active connection fails.
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

