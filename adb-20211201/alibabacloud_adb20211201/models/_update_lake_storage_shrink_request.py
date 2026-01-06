# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLakeStorageShrinkRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        description: str = None,
        lake_storage_id: str = None,
        permissions_shrink: str = None,
        region_id: str = None,
    ):
        # The ID of the AnalyticDB for MySQL cluster that is associated with the lake storage.
        self.dbcluster_id = dbcluster_id
        # The description of the lake storage.
        self.description = description
        # The unique identifier of the lake storage.
        self.lake_storage_id = lake_storage_id
        # The permissions on the lake storage.
        self.permissions_shrink = permissions_shrink
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.description is not None:
            result['Description'] = self.description

        if self.lake_storage_id is not None:
            result['LakeStorageId'] = self.lake_storage_id

        if self.permissions_shrink is not None:
            result['Permissions'] = self.permissions_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LakeStorageId') is not None:
            self.lake_storage_id = m.get('LakeStorageId')

        if m.get('Permissions') is not None:
            self.permissions_shrink = m.get('Permissions')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

