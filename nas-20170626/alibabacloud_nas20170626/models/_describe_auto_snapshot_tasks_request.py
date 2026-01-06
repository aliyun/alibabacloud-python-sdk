# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAutoSnapshotTasksRequest(DaraModel):
    def __init__(
        self,
        auto_snapshot_policy_ids: str = None,
        file_system_ids: str = None,
        file_system_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The IDs of automatic snapshot policies.
        # 
        # You can specify a maximum of 100 policy IDs. If you want to query the tasks of multiple automatic snapshot policies, you must separate the policy IDs with commas (,).
        self.auto_snapshot_policy_ids = auto_snapshot_policy_ids
        # The ID of the file system.
        # 
        # You can specify a maximum of 100 file system IDs. If you want to query the snapshots of multiple file systems, you must separate the file system IDs with commas (,).
        self.file_system_ids = file_system_ids
        # The type of the file system.
        # 
        # Valid value: extreme, which indicates Extreme NAS file systems.
        # 
        # This parameter is required.
        self.file_system_type = file_system_type
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_number = page_number
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_snapshot_policy_ids is not None:
            result['AutoSnapshotPolicyIds'] = self.auto_snapshot_policy_ids

        if self.file_system_ids is not None:
            result['FileSystemIds'] = self.file_system_ids

        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyIds') is not None:
            self.auto_snapshot_policy_ids = m.get('AutoSnapshotPolicyIds')

        if m.get('FileSystemIds') is not None:
            self.file_system_ids = m.get('FileSystemIds')

        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

