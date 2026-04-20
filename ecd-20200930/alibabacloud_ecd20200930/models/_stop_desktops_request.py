# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class StopDesktopsRequest(DaraModel):
    def __init__(
        self,
        create_snapshot: str = None,
        desktop_id: List[str] = None,
        os_update: bool = None,
        patch_id: str = None,
        region_id: str = None,
        stopped_mode: str = None,
    ):
        self.create_snapshot = create_snapshot
        # The cloud computer IDs. You can specify the IDs of 1 to 100 cloud computers.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # Whether to perform a patch update when the update is ready. A value of true indicates that a patch update is performed.
        self.os_update = os_update
        self.patch_id = patch_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The billing mode after you stop the cloud computer.
        # 
        # Default value: StopCharging. Valid values:
        # 
        # *   StopCharging: After the cloud computer is stopped, the system automatically reclaims computing resources. You are no longer charged for computing resources. However, you are still charged for storage resources.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   KeepCharging: After the cloud computer is stopped, the system does not reclaim resources to prevent insufficient resources and startup failures. You are still charged for the resources.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.stopped_mode = stopped_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_snapshot is not None:
            result['CreateSnapshot'] = self.create_snapshot

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.os_update is not None:
            result['OsUpdate'] = self.os_update

        if self.patch_id is not None:
            result['PatchId'] = self.patch_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stopped_mode is not None:
            result['StoppedMode'] = self.stopped_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateSnapshot') is not None:
            self.create_snapshot = m.get('CreateSnapshot')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('OsUpdate') is not None:
            self.os_update = m.get('OsUpdate')

        if m.get('PatchId') is not None:
            self.patch_id = m.get('PatchId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StoppedMode') is not None:
            self.stopped_mode = m.get('StoppedMode')

        return self

