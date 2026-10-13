# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSnapshotRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        file_system_id: str = None,
        retention_days: int = None,
        snapshot_name: str = None,
    ):
        # The snapshot description.
        # 
        # Limits:
        # 
        # - The description must be 2 to 256 characters in length.
        # - The description cannot start with `http://` or `https://`.
        # - Default value: empty.
        self.description = description
        # The ID of the Advanced Extreme NAS file system. The value must start with `extreme-`, such as `extreme-01dd****`.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The retention period of the snapshot.
        # 
        # Unit: days.
        # 
        # Valid values:
        # 
        # - -1 (default): The snapshot is permanently retained and is automatically deleted when the snapshot quota is reached.
        # - 1 to 65536: The snapshot is retained for the specified number of days. The snapshot is subject to automatic release after the retention period expires.
        self.retention_days = retention_days
        # The snapshot name.
        # 
        # Limits:
        # 
        # - The name must be 2 to 128 characters in length and can contain letters and digits. The name must start with a letter and cannot start with `http://` or `https://`.
        # - The name can contain digits, colons (:), underscores (_), or hyphens (-).
        # - The name cannot start with auto to avoid conflicts with automatic snapshot names.
        self.snapshot_name = snapshot_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days

        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')

        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')

        return self

