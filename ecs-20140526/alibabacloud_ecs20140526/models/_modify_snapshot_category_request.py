# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySnapshotCategoryRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        retention_days: int = None,
        snapshot_id: str = None,
    ):
        # The snapshot type.
        # 
        # - Archive: Archive snapshot
        self.category = category
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The retention period of the snapshot in days. The retention period starts from the time when the snapshot is created, which is specified by CreationTime. A standard snapshot must be retained for at least 14 days after it is created before it can be archived.
        # 
        # Archive snapshots have a retention period limit and must be retained as archive snapshots for at least 60 days. When you calculate the retention period of an archive snapshot, the period during which the snapshot was retained as a standard snapshot is deducted. If you delete an archive snapshot before it is retained for 60 days, you are charged for 60 days of archive storage. For more information, see [Snapshot billing](https://help.aliyun.com/document_detail/56159.html).
        # 
        # Valid values: 74 to 65536.
        # 
        # > If you do not specify this parameter, the snapshot is permanently retained.
        self.retention_days = retention_days
        # The snapshot ID.
        # 
        # This parameter is required.
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

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

        return self

