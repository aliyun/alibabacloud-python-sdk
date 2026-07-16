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
        # The capability. Valid values:
        # 
        # - understand: Image understanding. Supports the analysis of 300 images per day.
        # 
        # - understand-reid: Image understanding with person re-identification (ReID). Supports the analysis of 300 images per day.
        # 
        # - search: Search. Supports 75 searches per day.
        # 
        # - understand-search: Image understanding and search. Supports the analysis of 300 images and 75 searches per day.
        # 
        # - understand-reid-search: Image understanding with ReID and search. Supports the analysis of 300 images and 75 searches per day.
        self.capability = capability
        # The device ID.
        self.device_id = device_id
        # The subscription period. Valid values:
        # 
        # - month: A monthly subscription, calculated as 30 days.
        # 
        # - quarter: A quarterly subscription, calculated as 90 days.
        # 
        # - year: An annual subscription, calculated as 365 days.
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

