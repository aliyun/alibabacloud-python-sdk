# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResizeAIDBClusterModelRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dry_run: bool = None,
        region_id: str = None,
        target_capacity: int = None,
    ):
        # The ID of the PolarDB AI 3.0 logical instance.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to perform a read-only capacity dry run.
        self.dry_run = dry_run
        # The region ID. Requests are routed based on the region to which the instance belongs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The target total capacity. The abstract capacity unit is 1000, which equals one L20N equivalent card. The value must be a positive integer.
        # 
        # This parameter is required.
        self.target_capacity = target_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.target_capacity is not None:
            result['TargetCapacity'] = self.target_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TargetCapacity') is not None:
            self.target_capacity = m.get('TargetCapacity')

        return self

