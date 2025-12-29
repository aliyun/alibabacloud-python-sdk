# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupDBsRequest(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        restore_time: str = None,
        source_dbinstance: str = None,
    ):
        # The backup ID.
        # 
        # > 
        # 
        # *   You can call the [DescribeBackups](https://help.aliyun.com/document_detail/62172.html) operation to query the backup ID.
        # 
        # *   You must specify one of the **RestoreTime** and BackupId parameters.
        self.backup_id = backup_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return per page. Default value: 30. Valid values: **30**, **50**, and **100**.
        self.page_size = page_size
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The point in time to which the instance is restored. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > 
        # 
        # *   The time can be a point in time within the previous seven days. The time must be earlier than the current time, but later than the time when the instance was created.
        # 
        # *   You must specify one of the RestoreTime and **BackupId** parameters.
        self.restore_time = restore_time
        # The ID of the source instance.
        self.source_dbinstance = source_dbinstance

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time

        if self.source_dbinstance is not None:
            result['SourceDBInstance'] = self.source_dbinstance

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')

        if m.get('SourceDBInstance') is not None:
            self.source_dbinstance = m.get('SourceDBInstance')

        return self

