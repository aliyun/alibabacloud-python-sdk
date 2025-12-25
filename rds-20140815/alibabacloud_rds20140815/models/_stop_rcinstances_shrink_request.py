# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopRCInstancesShrinkRequest(DaraModel):
    def __init__(
        self,
        batch_optimization: str = None,
        force_stop: bool = None,
        instance_ids_shrink: str = None,
        region_id: str = None,
    ):
        # The batch operation mode. Set the value to **AllTogether**. In this mode, if all instances are stopped, a success message is returned. If an instance fails the verification, none of the instances can be stopped and an error message is returned.
        self.batch_optimization = batch_optimization
        # Specifies whether to forcefully stop the instance. Valid values:
        # 
        # *   **true**: forcefully stops the instance. If an instance fails to stop due to system or network issues, a forced stop can be triggered, **though it may result in data loss.**
        # *   **false**: does not forcefully stop the instance. This is the default value.
        self.force_stop = force_stop
        # The node IDs.
        self.instance_ids_shrink = instance_ids_shrink
        # The region ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/26243.html) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_optimization is not None:
            result['BatchOptimization'] = self.batch_optimization

        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop

        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchOptimization') is not None:
            self.batch_optimization = m.get('BatchOptimization')

        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')

        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

