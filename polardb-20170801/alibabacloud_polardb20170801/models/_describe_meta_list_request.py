# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMetaListRequest(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        dbcluster_id: str = None,
        get_db_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        restore_time: str = None,
        security_token: str = None,
    ):
        # The ID of the data backup file.
        # 
        # >*   When you run a query, you must specify the `BackId` or `RestoreTime` parameter.
        # >*   You can call the [DescribeBackups](https://help.aliyun.com/document_detail/98102.html) operation to query the ID of the backup set.
        self.backup_id = backup_id
        # The ID of the cluster.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query the details of all clusters under your account.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specify the specific database name (such as `test_db`) to query the names of all data tables that can be restored in the desired database.
        # 
        # >*   You can specify only one database name each time.
        # >*   If you do not specify this parameter, you can query the names of all databases that can be restored in the current backup set. However, you cannot query the names of data tables in each database.
        self.get_db_name = get_db_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # *   **30**
        # 
        # *   **50**
        # 
        # *   **100**
        # 
        #     Default value: **30**.
        self.page_size = page_size
        # The ID of the region in which the instance resides. You can call the [DescribeDBClusterAttribute](https://help.aliyun.com/document_detail/2319132.html) operation to query the region ID of the instance.
        self.region_code = region_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The point in time for the restoration. Specify the time in the YYYY-MM-DDThh:mmZ format. The time must be in UTC.
        # 
        # >  When you run a query, you must specify the `BackId` or `RestoreTime` parameter. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/98102.html) operation to query the point in time for the restoration.
        self.restore_time = restore_time
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.get_db_name is not None:
            result['GetDbName'] = self.get_db_name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_code is not None:
            result['RegionCode'] = self.region_code

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('GetDbName') is not None:
            self.get_db_name = m.get('GetDbName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

