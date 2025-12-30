# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateIpcOrderRequest(DaraModel):
    def __init__(
        self,
        capability: str = None,
        device_id: str = None,
        period: str = None,
    ):
        self.capability = capability
        self.device_id = device_id
        self.period = period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capability is not None:
            result['Capability'] = self.capability

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.period is not None:
            result['Period'] = self.period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capability') is not None:
            self.capability = m.get('Capability')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        return self

