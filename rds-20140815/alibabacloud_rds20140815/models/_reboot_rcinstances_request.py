# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RebootRCInstancesRequest(DaraModel):
    def __init__(
        self,
        batch_optimization: str = None,
        force_reboot: bool = None,
        instance_ids: List[str] = None,
        region_id: str = None,
    ):
        # The batch operation mode. Set the value to **AllTogether**. In this mode, if all specified instances are restarted, a success message is returned. If an instance fails the verification, none of the specified instances can be restarted and an error message is returned.
        self.batch_optimization = batch_optimization
        # Specifies whether to forcefully restart the instance. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.force_reboot = force_reboot
        # The node IDs.
        self.instance_ids = instance_ids
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

        if self.force_reboot is not None:
            result['ForceReboot'] = self.force_reboot

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchOptimization') is not None:
            self.batch_optimization = m.get('BatchOptimization')

        if m.get('ForceReboot') is not None:
            self.force_reboot = m.get('ForceReboot')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

