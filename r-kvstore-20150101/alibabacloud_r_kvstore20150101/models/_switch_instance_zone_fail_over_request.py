# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchInstanceZoneFailOverRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        site_fault_time: str = None,
        target_zone_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The duration for which the fault lasts. Unit: minutes.
        # 
        # Valid values:
        # 
        # *   5
        # *   10
        self.site_fault_time = site_fault_time
        # The ID of the destination zone.
        self.target_zone_id = target_zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.site_fault_time is not None:
            result['SiteFaultTime'] = self.site_fault_time

        if self.target_zone_id is not None:
            result['TargetZoneId'] = self.target_zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SiteFaultTime') is not None:
            self.site_fault_time = m.get('SiteFaultTime')

        if m.get('TargetZoneId') is not None:
            self.target_zone_id = m.get('TargetZoneId')

        return self

