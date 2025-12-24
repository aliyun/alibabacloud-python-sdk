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
        # The snapshot description. It can be empty or up to 256 characters in length. It cannot start with http:// or https://.
        self.description = description
        # Specifies whether to disable the instant access feature. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        # 
        # >  This parameter is no longer used. By default, new standard snapshots of Enterprise SSDs (ESSDs) are upgraded to instant access snapshots free of charge without the need for additional configurations. For more information, see [Use the instant access feature](https://help.aliyun.com/document_detail/193667.html).
        self.disable_instant_access = disable_instant_access
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The retention period of the snapshot. After you specify this parameter, the end time of the new retention period is the specified number of days apart from the **creation time** of the snapshot, which follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format and is displayed in UTC. Valid values: 1 to 65536.
        # 
        # >  You can extend the retention period of the snapshot and cannot shorten the retention period.
        self.retention_days = retention_days
        # The ID of the snapshot.
        # 
        # This parameter is required.
        self.snapshot_id = snapshot_id
        # The name of the snapshot. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https://. It can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        # 
        # The name cannot start with auto because snapshots whose names start with auto are recognized as automatic snapshots.
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

