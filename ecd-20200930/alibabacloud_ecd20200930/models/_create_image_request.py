# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateImageRequest(DaraModel):
    def __init__(
        self,
        auto_clean_userdata: bool = None,
        data_snapshot_ids: List[str] = None,
        description: str = None,
        desktop_id: str = None,
        disk_type: str = None,
        image_name: str = None,
        image_resource_type: str = None,
        region_id: str = None,
        snapshot_id: str = None,
        snapshot_ids: List[str] = None,
    ):
        # Specifies whether to clear personal user data. If this parameter is set to `true`, the created image clears data in all directories under `C:\\Users` except the `Administrator` and `Public` directories.
        self.auto_clean_userdata = auto_clean_userdata
        # The list of data cloud disk snapshot IDs. To include data cloud disks when creating an image, specify the corresponding data cloud disk snapshot IDs. A maximum of 100 IDs are supported.
        self.data_snapshot_ids = data_snapshot_ids
        # The description of the image. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The cloud computer ID.
        self.desktop_id = desktop_id
        # The disk data included in the image.
        self.disk_type = disk_type
        # The image name. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). The name must start with a letter or a Chinese character and cannot start with `http://` or `https://`.
        self.image_name = image_name
        # This parameter is not publicly available.
        self.image_resource_type = image_resource_type
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the regions supported by WUYING Workspace.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The snapshot ID.
        self.snapshot_id = snapshot_id
        # The list of snapshot IDs.
        self.snapshot_ids = snapshot_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_clean_userdata is not None:
            result['AutoCleanUserdata'] = self.auto_clean_userdata

        if self.data_snapshot_ids is not None:
            result['DataSnapshotIds'] = self.data_snapshot_ids

        if self.description is not None:
            result['Description'] = self.description

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.image_resource_type is not None:
            result['ImageResourceType'] = self.image_resource_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.snapshot_ids is not None:
            result['SnapshotIds'] = self.snapshot_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCleanUserdata') is not None:
            self.auto_clean_userdata = m.get('AutoCleanUserdata')

        if m.get('DataSnapshotIds') is not None:
            self.data_snapshot_ids = m.get('DataSnapshotIds')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImageResourceType') is not None:
            self.image_resource_type = m.get('ImageResourceType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('SnapshotIds') is not None:
            self.snapshot_ids = m.get('SnapshotIds')

        return self

