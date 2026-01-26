# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OpenArmsServiceSecondVersionRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        type: str = None,
    ):
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The type of the service. Valid values:
        # 
        # *   `arms`: ARMS
        # *   `arms_app`: Application Monitoring
        # *   `arms_web`: Browser Monitoring
        # *   `prometheus_monitor`: Managed Service for Prometheus
        # *   `synthetic_post`: Synthetic Monitoring
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

