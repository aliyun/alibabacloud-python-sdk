# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReadyForServiceRequest(DaraModel):
    def __init__(
        self,
        device_id: str = None,
        instance_id: str = None,
        outbound_scenario: bool = None,
        user_id: str = None,
    ):
        self.device_id = device_id
        # This parameter is required.
        self.instance_id = instance_id
        self.outbound_scenario = outbound_scenario
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.outbound_scenario is not None:
            result['OutboundScenario'] = self.outbound_scenario

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OutboundScenario') is not None:
            self.outbound_scenario = m.get('OutboundScenario')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

