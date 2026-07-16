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
        # An array of 1 to 100 cloud desktop IDs.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # Specifies whether to apply pending patch updates.
        self.os_update = os_update
        self.patch_id = patch_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to get a list of regions that Elastic Desktop Service supports.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies the billing mode for the cloud desktops after they are stopped.
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

