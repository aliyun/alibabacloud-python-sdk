# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetInstanceRecordConfigRequest(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        expiration_days: int = None,
        instance_id: str = None,
        record_storage_target: str = None,
        region_id: str = None,
        resource_region_id: str = None,
    ):
        # This parameter is required.
        self.enabled = enabled
        self.expiration_days = expiration_days
        # This parameter is required.
        self.instance_id = instance_id
        self.record_storage_target = record_storage_target
        self.region_id = region_id
        self.resource_region_id = resource_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.expiration_days is not None:
            result['ExpirationDays'] = self.expiration_days

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.record_storage_target is not None:
            result['RecordStorageTarget'] = self.record_storage_target

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('ExpirationDays') is not None:
            self.expiration_days = m.get('ExpirationDays')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RecordStorageTarget') is not None:
            self.record_storage_target = m.get('RecordStorageTarget')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        return self

