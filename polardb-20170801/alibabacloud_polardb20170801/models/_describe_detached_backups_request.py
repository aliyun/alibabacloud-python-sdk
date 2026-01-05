# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDetachedBackupsRequest(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        backup_mode: str = None,
        backup_region: str = None,
        backup_status: str = None,
        dbcluster_id: str = None,
        end_time: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        # The ID of the backup set.
        self.backup_id = backup_id
        # The backup mode. Valid values:
        # 
        # *   **Automated**
        # *   **Manual**
        self.backup_mode = backup_mode
        # The region where the cross-region data backup file of the instance is stored.
        # 
        # > This parameter is valid only for PolarDB for MySQL clusters.
        self.backup_region = backup_region
        # The status of the backup set. Valid values:
        # 
        # *   **Success**
        # *   **Failed**
        self.backup_status = backup_status
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The end of the time range to query. Specify the time in the `YYYY-MM-DDThh:mmZ` format. The time must be in UTC. The end time must be later than the start time.
        # 
        # This parameter is required.
        self.end_time = end_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. The value must be a positive integer that does not exceed the maximum value of the INTEGER data type. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30**
        # *   **50**
        # *   **100**
        # 
        # Default value: **30**.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The beginning of the time range to query. Specify the time in the `yyyy-MM-ddTHH:mmZ` format. The time must be in UTC.
        # 
        # This parameter is required.
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

        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.backup_region is not None:
            result['BackupRegion'] = self.backup_region

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('BackupRegion') is not None:
            self.backup_region = m.get('BackupRegion')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

