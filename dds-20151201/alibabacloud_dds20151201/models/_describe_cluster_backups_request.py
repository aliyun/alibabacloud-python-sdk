# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClusterBackupsRequest(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        backup_job_id: str = None,
        dbinstance_id: str = None,
        dest_region: str = None,
        end_time: str = None,
        is_only_get_cluster_back_up: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        src_region: str = None,
        start_time: str = None,
    ):
        # The ID of the cluster backup.
        self.backup_id = backup_id
        # The ID of the backup job.
        self.backup_job_id = backup_job_id
        # The ID of the instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The region where the geo-redundant backup resides.
        # 
        # > This parameter is required when you query geo-redundant backups.
        self.dest_region = dest_region
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        # 
        # > This parameter is invalid if you specify the BackupId parameter.
        self.end_time = end_time
        # Specifies whether to query the information about the child nodes in the cluster backup. Valid values:
        # 
        # - **true**: Returns only the basic information about the cluster backup, not the backup information about all child nodes.
        # 
        # - **false** (Default): Returns the backup information about all child nodes.
        self.is_only_get_cluster_back_up = is_only_get_cluster_back_up
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. The value must be a positive integer. Default value: **1**.
        self.page_no = page_no
        # The number of entries to return on each page. Valid values:
        # 
        # - **30** (Default)
        # 
        # - **50**
        # 
        # - **100**
        self.page_size = page_size
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The region where the instance resides.
        # 
        # > - This parameter is required when you query the backup sets of a released instance.
        # >
        # > - This parameter is required when you query geo-redundant backups.
        self.src_region = src_region
        # The beginning of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in Coordinated Universal Time (UTC).
        # 
        # > This parameter is invalid if you specify the BackupId parameter.
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

        if self.is_only_get_cluster_back_up is not None:
            result['IsOnlyGetClusterBackUp'] = self.is_only_get_cluster_back_up

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

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

        if m.get('IsOnlyGetClusterBackUp') is not None:
            self.is_only_get_cluster_back_up = m.get('IsOnlyGetClusterBackUp')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

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

