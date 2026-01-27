# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class CreateRCSnapshotRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        disk_id: str = None,
        instant_access: bool = None,
        instant_access_retention_days: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        retention_days: int = None,
        tag: List[main_models.CreateRCSnapshotRequestTag] = None,
        zone_id: str = None,
    ):
        # The snapshot description. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        # 
        # By default, this parameter is left empty.
        self.description = description
        # The cloud disk ID.
        self.disk_id = disk_id
        # This parameter is deprecated.
        self.instant_access = instant_access
        # This parameter is deprecated.
        self.instant_access_retention_days = instant_access_retention_days
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # The retention period of the snapshot. Valid values: 1 to 65536. Unit: days. The snapshot is automatically released when its retention period expires.
        # 
        # By default, this parameter is left empty, which specifies that the snapshot is not automatically released.
        self.retention_days = retention_days
        self.tag = tag
        # This parameter has been deprecated.
        self.zone_id = zone_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.instant_access is not None:
            result['InstantAccess'] = self.instant_access

        if self.instant_access_retention_days is not None:
            result['InstantAccessRetentionDays'] = self.instant_access_retention_days

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('InstantAccess') is not None:
            self.instant_access = m.get('InstantAccess')

        if m.get('InstantAccessRetentionDays') is not None:
            self.instant_access_retention_days = m.get('InstantAccessRetentionDays')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateRCSnapshotRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateRCSnapshotRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

