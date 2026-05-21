# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateScheduledBackupConfigRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        data_keep_quantity: int = None,
        dst_region: str = None,
        enabled: bool = None,
        hour: int = None,
        instance_id: str = None,
        manual_data_keep_quantity: int = None,
        schedule_type: str = None,
        week: str = None,
        zone_id: str = None,
    ):
        self.region_id = region_id
        self.data_keep_quantity = data_keep_quantity
        self.dst_region = dst_region
        self.enabled = enabled
        self.hour = hour
        self.instance_id = instance_id
        self.manual_data_keep_quantity = manual_data_keep_quantity
        self.schedule_type = schedule_type
        self.week = week
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.data_keep_quantity is not None:
            result['dataKeepQuantity'] = self.data_keep_quantity

        if self.dst_region is not None:
            result['dstRegion'] = self.dst_region

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.hour is not None:
            result['hour'] = self.hour

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.manual_data_keep_quantity is not None:
            result['manualDataKeepQuantity'] = self.manual_data_keep_quantity

        if self.schedule_type is not None:
            result['scheduleType'] = self.schedule_type

        if self.week is not None:
            result['week'] = self.week

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('dataKeepQuantity') is not None:
            self.data_keep_quantity = m.get('dataKeepQuantity')

        if m.get('dstRegion') is not None:
            self.dst_region = m.get('dstRegion')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('hour') is not None:
            self.hour = m.get('hour')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('manualDataKeepQuantity') is not None:
            self.manual_data_keep_quantity = m.get('manualDataKeepQuantity')

        if m.get('scheduleType') is not None:
            self.schedule_type = m.get('scheduleType')

        if m.get('week') is not None:
            self.week = m.get('week')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

