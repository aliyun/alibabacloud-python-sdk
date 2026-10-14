# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSnapshotsRequest(DaraModel):
    def __init__(
        self,
        disk_id: str = None,
        ens_region_id: str = None,
        ens_region_ids: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        snapshot_id: str = None,
        snapshot_name: str = None,
    ):
        # The ID of the specified cloud disk.
        self.disk_id = disk_id
        # The ID of the ENS edge zone. You can call [DescribeEnsRegions](https://help.aliyun.com/document_detail/2637662.html) to query edge zone IDs.
        self.ens_region_id = ens_region_id
        # The array of ENS edge zone IDs. Array length: 1 to 100.
        self.ens_region_ids = ens_region_ids
        # The instance ID.
        self.instance_id = instance_id
        # The page number of the current query.
        self.page_number = page_number
        # The number of entries per page in a paged query.
        self.page_size = page_size
        # The snapshot ID. The value can be a JSON array that consists of up to 100 snapshot IDs. Separate multiple IDs with commas (,).
        self.snapshot_id = snapshot_id
        # The display name of the snapshot. The name must be 2 to 128 characters in length and must start with a letter or a Chinese character. It cannot start with `http://` or `https://`. It can contain digits, colons (:), underscores (_), or hyphens (-).
        self.snapshot_name = snapshot_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.ens_region_ids is not None:
            result['EnsRegionIds'] = self.ens_region_ids

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('EnsRegionIds') is not None:
            self.ens_region_ids = m.get('EnsRegionIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')

        return self

