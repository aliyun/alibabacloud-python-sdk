# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBClustersWithBackupsRequest(DaraModel):
    def __init__(
        self,
        dbcluster_description: str = None,
        dbcluster_ids: str = None,
        dbtype: str = None,
        dbversion: str = None,
        is_deleted: int = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The name of the cluster. The name must meet the following requirements:
        # 
        # *   It cannot start with `http://` or `https://`.
        # *   It must be 2 to 256 characters in length.
        self.dbcluster_description = dbcluster_description
        # The ID of the cluster. If you need to specify multiple cluster IDs, separate the cluster IDs with commas (,).
        self.dbcluster_ids = dbcluster_ids
        # The type of the database engine. Valid values:
        # 
        # *   **MySQL**
        # *   **PostgreSQL**
        # *   **Oracle**
        self.dbtype = dbtype
        # The version of the database engine.
        # 
        # *   Valid values for the MySQL database engine:
        # 
        #     *   **5.6**
        #     *   **5.7**
        #     *   **8.0**
        # 
        # *   Valid values for the PostgreSQL database engine:
        # 
        #     *   **11**
        #     *   **14**
        # 
        # *   Valid value for the Oracle database engine: **11**
        self.dbversion = dbversion
        # Specifies whether the cluster is deleted. Valid values:
        # 
        # *   **0**: not deleted
        # *   **1**: deleted
        self.is_deleted = is_deleted
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. The value must be a positive integer that does not exceed the maximum value of the INTEGER data type. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30**
        # *   **50**
        # *   **100**
        # 
        # Default value: 30.
        self.page_size = page_size
        # The region ID of the cluster.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query information about regions.
        # 
        # This parameter is required.
        self.region_id = region_id
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
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description

        if self.dbcluster_ids is not None:
            result['DBClusterIds'] = self.dbcluster_ids

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')

        if m.get('DBClusterIds') is not None:
            self.dbcluster_ids = m.get('DBClusterIds')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

