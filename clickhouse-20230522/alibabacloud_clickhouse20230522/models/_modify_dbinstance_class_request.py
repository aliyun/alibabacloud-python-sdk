# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceClassRequest(DaraModel):
    def __init__(
        self,
        computing_group_id: str = None,
        dbinstance_id: str = None,
        node_count: int = None,
        node_scale_max: int = None,
        node_scale_min: int = None,
        region_id: str = None,
        scale_max: int = None,
        scale_min: int = None,
        storage_quota: int = None,
        storage_type: str = None,
    ):
        self.computing_group_id = computing_group_id
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.node_count = node_count
        self.node_scale_max = node_scale_max
        self.node_scale_min = node_scale_min
        # The region ID.
        self.region_id = region_id
        # The maximum capacity for elastic scaling.
        self.scale_max = scale_max
        # The minimum capacity for elastic scaling.
        self.scale_min = scale_min
        self.storage_quota = storage_quota
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.computing_group_id is not None:
            result['ComputingGroupId'] = self.computing_group_id

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.node_scale_max is not None:
            result['NodeScaleMax'] = self.node_scale_max

        if self.node_scale_min is not None:
            result['NodeScaleMin'] = self.node_scale_min

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max

        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min

        if self.storage_quota is not None:
            result['StorageQuota'] = self.storage_quota

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputingGroupId') is not None:
            self.computing_group_id = m.get('ComputingGroupId')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('NodeScaleMax') is not None:
            self.node_scale_max = m.get('NodeScaleMax')

        if m.get('NodeScaleMin') is not None:
            self.node_scale_min = m.get('NodeScaleMin')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')

        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')

        if m.get('StorageQuota') is not None:
            self.storage_quota = m.get('StorageQuota')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

