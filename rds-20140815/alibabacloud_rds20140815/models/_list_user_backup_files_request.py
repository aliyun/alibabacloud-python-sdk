# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserBackupFilesRequest(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        comment: str = None,
        oss_url: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
        tags: str = None,
    ):
        # The user backup ID.
        self.backup_id = backup_id
        # The comment of the user backup to query.
        # >You can enter part of the comment for fuzzy matching.
        self.comment = comment
        # The OSS download URL of the user backup file. For information about how to obtain the OSS download URL of a user backup file, see [How do I obtain the URL of an uploaded object?](https://help.aliyun.com/document_detail/39607.html).
        self.oss_url = oss_url
        self.owner_id = owner_id
        # The region ID. You can call DescribeRegions to query the available regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID. You can call DescribeDBInstanceAttribute to query the resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The status of the user backup file. Valid values:
        # * **Importing**: The backup is being imported.
        # * **Failed**: The import failed.
        # * **CheckSuccess**: The verification passed.
        # * **BackupSuccess**: The import succeeded.
        # * **Deleted**: The backup is deleted.
        self.status = status
        # The tag information used to query the user backup.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

