# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupPolicyRequest(DaraModel):
    def __init__(
        self,
        backup_policy_mode: str = None,
        compress_type: str = None,
        dbinstance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        released_keep_policy: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The backup type. Valid values:
        # * **DataBackupPolicy**: data backup
        # * **LogBackupPolicy**: log backup
        self.backup_policy_mode = backup_policy_mode
        # The backup compression method. Valid values:
        # * **0**: no compression
        # * **1**: zlib compression
        # * **2**: parallel zlib compression
        # * **4**: QuickLZ compression with fast restoration for individual databases and tables enabled
        # * **8**: QuickLZ compression without fast restoration for individual databases and tables supported
        self.compress_type = compress_type
        # The instance ID. You can call DescribeDBInstances to obtain the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The archived backup data retention policy for deleted **MySQL** instances. Valid values:
        # 
        # * **None**: No archived backups are retained.
        # * **Lastest**: Only the last archived backup is retained.
        # * **All**: All archived backups are retained.
        self.released_keep_policy = released_keep_policy
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_policy_mode is not None:
            result['BackupPolicyMode'] = self.backup_policy_mode

        if self.compress_type is not None:
            result['CompressType'] = self.compress_type

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.released_keep_policy is not None:
            result['ReleasedKeepPolicy'] = self.released_keep_policy

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPolicyMode') is not None:
            self.backup_policy_mode = m.get('BackupPolicyMode')

        if m.get('CompressType') is not None:
            self.compress_type = m.get('CompressType')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ReleasedKeepPolicy') is not None:
            self.released_keep_policy = m.get('ReleasedKeepPolicy')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

