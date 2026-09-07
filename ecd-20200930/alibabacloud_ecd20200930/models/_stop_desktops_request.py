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
        # Specifies whether to create a snapshot.
        self.create_snapshot = create_snapshot
        # The cloud computer IDs. You can specify 1 to 100 IDs.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # Specifies whether to perform a patch update when an update is ready. A value of true indicates that the patch update is performed.
        self.os_update = os_update
        # The patch ID.
        self.patch_id = patch_id
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The billing mode after the cloud computers are stopped.
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

