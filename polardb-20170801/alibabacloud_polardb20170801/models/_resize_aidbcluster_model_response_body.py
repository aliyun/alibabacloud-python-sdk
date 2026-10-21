# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResizeAIDBClusterModelResponseBody(DaraModel):
    def __init__(
        self,
        current_capacity: int = None,
        dbcluster_id: str = None,
        dry_run: bool = None,
        pool_hit_capacity: int = None,
        pool_hit_ratio: float = None,
        request_id: str = None,
        required_delta: int = None,
        target_capacity: int = None,
    ):
        # The current measured capacity of the instance. This parameter is returned only when DryRun is set to true.
        self.current_capacity = current_capacity
        # The ID of the PolarDB AI 3.0 logical instance.
        self.dbcluster_id = dbcluster_id
        # Indicates whether the current request performs a capacity dry run only.
        self.dry_run = dry_run
        # The capacity that can be directly borrowed from the large pool without reshaping. This parameter is returned only when DryRun is set to true.
        self.pool_hit_capacity = pool_hit_capacity
        # The direct hit ratio of the large pool. Valid values: 0 to 1. This parameter is returned only when DryRun is set to true.
        self.pool_hit_ratio = pool_hit_ratio
        # Id of the request
        self.request_id = request_id
        # The positive difference between the target capacity and the current capacity. This parameter is returned only when DryRun is set to true.
        self.required_delta = required_delta
        # The target total capacity.
        self.target_capacity = target_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_capacity is not None:
            result['CurrentCapacity'] = self.current_capacity

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.pool_hit_capacity is not None:
            result['PoolHitCapacity'] = self.pool_hit_capacity

        if self.pool_hit_ratio is not None:
            result['PoolHitRatio'] = self.pool_hit_ratio

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.required_delta is not None:
            result['RequiredDelta'] = self.required_delta

        if self.target_capacity is not None:
            result['TargetCapacity'] = self.target_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentCapacity') is not None:
            self.current_capacity = m.get('CurrentCapacity')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('PoolHitCapacity') is not None:
            self.pool_hit_capacity = m.get('PoolHitCapacity')

        if m.get('PoolHitRatio') is not None:
            self.pool_hit_ratio = m.get('PoolHitRatio')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RequiredDelta') is not None:
            self.required_delta = m.get('RequiredDelta')

        if m.get('TargetCapacity') is not None:
            self.target_capacity = m.get('TargetCapacity')

        return self

