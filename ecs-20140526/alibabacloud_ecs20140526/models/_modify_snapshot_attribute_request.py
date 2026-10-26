# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySnapshotAttributeRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        disable_instant_access: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        retention_days: int = None,
        snapshot_id: str = None,
        snapshot_name: str = None,
    ):
        # The description of the snapshot. The description can be empty and can be up to 256 characters in length. It cannot start with http:// or https://.
        self.description = description
        # Specifies whether to shutdown the instant access feature for the snapshot. Valid values:
        # - true: shutdown the instant access feature.
        # - false: do not shutdown the instant access feature.
        # Default value: false.
        # 
        # > **[Deprecated]** This parameter is deprecated. Standard snapshots of ESSD cloud disks have been upgraded to [instant access by default](https://help.aliyun.com/document_detail/193667.html). You do not need to perform additional configurations, and no additional fees are incurred.
        self.disable_instant_access = disable_instant_access
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The retention period of the snapshot in days. When you specify this parameter, the retention period is calculated from the **creation time** of the snapshot. The creation time is represented in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format and displayed in UTC. Valid values: 1 to 65536.
        # > You can only extend the retention period of a snapshot. You cannot shorten the existing retention period.
        self.retention_days = retention_days
        # The snapshot ID.
        # 
        # This parameter is required.
        self.snapshot_id = snapshot_id
        # The display name of the snapshot. The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character and cannot start with http:// or https://. It can contain digits, colons (:), underscores (_), and hyphens (-). To prevent name conflicts with automatic snapshots, the name cannot start with auto.
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

        if self.disable_instant_access is not None:
            result['DisableInstantAccess'] = self.disable_instant_access

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisableInstantAccess') is not None:
            self.disable_instant_access = m.get('DisableInstantAccess')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')

        return self

