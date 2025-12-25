# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCrossBackupMetaListRequest(DaraModel):
    def __init__(
        self,
        backup_set_id: str = None,
        get_db_name: str = None,
        owner_id: int = None,
        page_index: str = None,
        page_size: str = None,
        pattern: str = None,
        region: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the cross-region backup file that you want to use. You can call the [DescribeCrossRegionBackups](https://help.aliyun.com/document_detail/121733.html) operation to query the ID of the cross-region backup file.
        # 
        # This parameter is required.
        self.backup_set_id = backup_set_id
        # The name of the database that you want to query. The system implements exact match based on the value of this parameter and returns the name of the matched database and the names of the tables in the matched database.
        self.get_db_name = get_db_name
        self.owner_id = owner_id
        # The number of the page to return. Valid values: any non-zero positive integer.
        # 
        # > This parameter only takes effect when you specify the **PageSize** parameter.
        self.page_index = page_index
        # The number of entries to return per page. Default value: **1**.
        # 
        # > This parameter only takes effect when you specify the **PageIndex** parameter.
        self.page_size = page_size
        # The name of the database that you want to query. The system implements fuzzy match based on the value of this parameter and returns only the name of the matched database.
        # 
        # > You can implement fuzzy match and then exact match. For example, you can set the Pattern parameter to test to query the testdb1 and testdb2 databases. Then, you can specify the **GetDbName** parameter to query only the matched database and the tables in the matched database.
        self.pattern = pattern
        # The region ID of the instance.
        self.region = region
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id

        if self.get_db_name is not None:
            result['GetDbName'] = self.get_db_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pattern is not None:
            result['Pattern'] = self.pattern

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')

        if m.get('GetDbName') is not None:
            self.get_db_name = m.get('GetDbName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

