# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLakeStorageRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        lake_storage_id: str = None,
        region_id: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The lake storage ID.
        self.lake_storage_id = lake_storage_id
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

        if self.lake_storage_id is not None:
            result['LakeStorageId'] = self.lake_storage_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('LakeStorageId') is not None:
            self.lake_storage_id = m.get('LakeStorageId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

