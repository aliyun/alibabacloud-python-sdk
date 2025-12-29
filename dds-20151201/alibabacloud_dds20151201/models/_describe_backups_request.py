# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupsRequest(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        backup_job_id: str = None,
        dbinstance_id: str = None,
        dest_region: str = None,
        end_time: str = None,
        node_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        src_region: str = None,
        start_time: str = None,
    ):
        # The ID of the backup set. You can call the [CreateBackup](https://help.aliyun.com/document_detail/62171.html) operation to query the backup set ID.
        # 
        # If you set the **DBInstanceId** parameter to the ID of a sharded cluster instance, the number of backup IDs is the same as the number of shard nodes. Multiple backup IDs are separated with commas (,).
        self.backup_id = backup_id
        self.backup_job_id = backup_job_id
        # The instance ID.
        # 
        # > If you set this parameter to the ID of a sharded cluster instance, you must also specify the **NodeId** parameter.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The region ID of the Cross-regional backup.
        # 
        # >  This parameter is required for the Cross-regional backup.
        self.dest_region = dest_region
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC. The end time must be later than the start time.
        self.end_time = end_time
        # The ID of the shard node in the sharded cluster instance.
        # 
        # > This parameter takes effect only when you set the **DBInstanceId** parameter to the ID of a sharded cluster instance.
        self.node_id = node_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. Pages start from page 1. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**
        # *   **100**
        self.page_size = page_size
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The region ID of the instance.
        # 
        # >- This parameter is required if you want to query the backup sets of a released instance.
        # >-  This parameter is required if you want to query cross-region backups.
        self.src_region = src_region
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.backup_job_id is not None:
            result['BackupJobId'] = self.backup_job_id

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dest_region is not None:
            result['DestRegion'] = self.dest_region

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.node_id is not None:
            result['NodeId'] = self.node_id

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

        if self.src_region is not None:
            result['SrcRegion'] = self.src_region

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BackupJobId') is not None:
            self.backup_job_id = m.get('BackupJobId')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DestRegion') is not None:
            self.dest_region = m.get('DestRegion')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

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

        if m.get('SrcRegion') is not None:
            self.src_region = m.get('SrcRegion')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

