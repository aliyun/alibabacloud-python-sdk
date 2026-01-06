# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSnapshotsRequest(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        file_system_type: str = None,
        page_number: int = None,
        page_size: int = None,
        snapshot_ids: str = None,
        snapshot_name: str = None,
        snapshot_type: str = None,
        status: str = None,
    ):
        # The ID of the file system.
        self.file_system_id = file_system_id
        # The type of the file system.
        # 
        # Valid value: extreme, which indicates Extreme File Storage NAS (NAS) file systems.
        self.file_system_type = file_system_type
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The snapshot IDs.
        # 
        # You can specify a maximum of 100 snapshot IDs. You must separate snapshot IDs with commas (,).
        self.snapshot_ids = snapshot_ids
        # The snapshot name.
        self.snapshot_name = snapshot_name
        # The type of the snapshot.
        # 
        # Valid values:
        # 
        # *   auto: auto snapshot
        # *   user: manual snapshot
        # *   all (default): all snapshot types
        self.snapshot_type = snapshot_type
        # The status of the snapshot.
        # 
        # Valid values:
        # 
        # *   progressing: The snapshot is being created.
        # *   accomplished: The snapshot is created.
        # *   failed: The snapshot fails to be created.
        # *   all (default): all snapshot states.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.snapshot_ids is not None:
            result['SnapshotIds'] = self.snapshot_ids

        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name

        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SnapshotIds') is not None:
            self.snapshot_ids = m.get('SnapshotIds')

        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')

        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

