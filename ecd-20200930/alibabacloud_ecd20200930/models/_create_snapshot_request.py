# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSnapshotRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        desktop_id: str = None,
        region_id: str = None,
        snapshot_name: str = None,
        source_disk_type: str = None,
    ):
        # The description of the snapshot. The description can be up to 128 characters in length.
        self.description = description
        # The ID of the cloud computer.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the snapshot. The name must be 2 to 127 characters in length. The name must start with a letter. The name can contain letters, digits, underscores (_), and hyphens (-). The name cannot start with `auto` because snapshots whose names start with auto are recognized as automatic snapshots.
        # 
        # This parameter is required.
        self.snapshot_name = snapshot_name
        # The type of the disk for which you want to create a snapshot.
        # 
        # Valid values:
        # 
        # *   system: system disk
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   data: data disk
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # This parameter is required.
        self.source_disk_type = source_disk_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name

        if self.source_disk_type is not None:
            result['SourceDiskType'] = self.source_disk_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')

        if m.get('SourceDiskType') is not None:
            self.source_disk_type = m.get('SourceDiskType')

        return self

